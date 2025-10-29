from base64 import b64encode
import logging
import os
import json
import pkgutil
import re
from pathlib import Path
from typing import Callable, Optional

import Utils
from worlds.generic.Rules import forbid_items_for_player
from worlds.LauncherComponents import Component, SuffixIdentifier, components, Type, launch_subprocess

from .Data import region_table, category_table, meta_table
from .Meta import world_description, world_webworld, enable_region_diagram
from .Locations import location_table, location_id_to_name, location_name_to_id, location_name_to_location, location_name_groups, victory_names
from .Items import item_table, item_id_to_name, item_name_to_id, item_name_to_item, item_name_groups
from .DataValidation import runGenerationDataValidation, runPreFillDataValidation

from .Regions import create_regions
from .Items import SimpsonsHitAndRunItem
from .Rules import set_rules
from .Options import SimpsonsHitAndRunOptions
from .Helpers import is_option_enabled, is_item_enabled, get_option_value

from BaseClasses import ItemClassification, Tutorial, Item
from Options import PerGameCommonOptions
from worlds.AutoWorld import World, WebWorld

from .hooks.World import \
    before_create_regions, after_create_regions, \
    before_create_items_starting, before_create_items_filler, after_create_items, \
    before_create_item, after_create_item, \
    before_set_rules, after_set_rules, \
    before_generate_basic, after_generate_basic, \
    before_fill_slot_data, after_fill_slot_data, before_write_spoiler, card_table
from .hooks.Data import hook_interpret_slot_data

from .SHARContainer import gen

class SimpsonsHitAndRunWorld(World):
    """A 2003 Action Adventure game similar to the GTA series starring the Simpsons"""
    game = "The Simpsons Hit And Run"
    web = world_webworld

    options_dataclass = SimpsonsHitAndRunOptions
    data_version = 2
    required_client_version = (0, 5, 0)
    apworld_version = "0.3.3"
    # These properties are set from the imports of the same name above.
    item_table = item_table
    location_table = location_table # this is likely imported from Data instead of Locations because the Game Complete location should not be in here, but is used for lookups
    category_table = category_table

    item_id_to_name = item_id_to_name
    item_name_to_id = item_name_to_id
    item_name_to_item = item_name_to_item
    item_name_groups = item_name_groups

    item_counts = {}
    start_inventory = {}

    location_id_to_name = location_id_to_name
    location_name_to_id = location_name_to_id
    location_name_to_location = location_name_to_location
    location_name_groups = location_name_groups
    victory_names = victory_names

    mission_locks = {}
    vehicle_item_to_vehicle = {
        "ambul": "Ambulance",
        "apu_v": "Longhorn",
        "atv_v": "ATV",
        "bart_v": "Ferrini - Red",
        "bbman_v": "El Carro Loco",
        "bookb_v": "Book Burning Van",
        "burns_v": "36 Stutz Bearcat",
        "burnsarm": "Burns Armored Truck",
        "carhom_v": "Car Built For Homer",
        "cArmor": "Armored Truck",
        "cBlbart": "Ferrini - Black",
        "cBone": "Bonestorm Truck",
        "cCellA": "Cell Phone Car",
        "cCola": "Cola Truck",
        "cCube": "Cube Van",
        "cCurator": "Curator",
        "cDonut": "Donut Truck",
        "cDuff": "Duff Truck",
        "cFire_v": "Fire Truck",
        "cHears": "Hearse",
        "cKlimo": "Krusty's Limo",
        "cletu_v": "Pickup Truck",
        "cLimo": "Limo",
        "cMilk": "Milk Truck",
        "cNerd": "Nerd Car",
        "cNonup": "Nonuplets Van",
        "coffin": "Coffin Car",
        "comic_v": "Kremlin",
        "compactA": "Compact Car",
        "cSedan": "Chase Sedan",
        "cVan": "Surveillance Van",
        "dune_v": "R/C Buggy",
        "elect_v": "Electaurus",
        "famil_v": "Family Sedan",
        "fishtruc": "Fish Van",
        "fone_v": "Open Wheel Race Car",
        "frink_v": "Hover Car",
        "garbage": "Garbage Truck",
        "glastruc": "Glass Truck",
        "gramp_v": "WWII Vehicle",
        "gramR_v": "WWII Vehicle W/ Rocket",
        "hallo": "Hearse",
        "hbike_v": "Hover Bike",
        "homer_v": "70's Sports Car",
        "honor_v": "Honor Roller",
        "hype_v": "Planet Hype 50's Car",
        "icecream": "Ice Cream Truck",
        "IStruck": "Itchy and Scratchy Movie Truck",
        "knigh_v": "Knight Boat",
        "krust_v": "Clown Car",
        "lisa_v": "Malibu Stacy Car",
        "marge_v": "Canyonero",
        "minivanA": "Minivan",
        "moe_v": "Moe's Sedan",
        "mono_v": "Monorail Car",
        "mrplo_v": "Mr. Plow",
        "nuctruck": "Nuclear Waste Truck",
        "oblit_v": "Obliteratatron Big Wheel Truck",
        "otto_v": "School Bus",
        "pickupA": "Pickup",
        "pizza": "Pizza Van",
        "plowk_v": "Plow King",
        "rocke_v": "Speed Rocket",
        "schoolbu": "Mini School Bus",
        "scorp_v": "Globex Super Villain Car",
        "sedanA": "Sedan A",
        "sedanB": "Sedan B",
        "ship": "Ghost Ship",
        "skinn_v": "Skinner's Sedan",
        "smith_v": "Mr. Burns' Limo",
        "snake_v": "Bandit",
        "sportsA": "Sports Car A",
        "sportsB": "Sports Car B",
        "SUVA": "SUV",
        "taxiA": "Taxi",
        "votetruc": "Vote Quimby Truck",
        "wagonA": "Station Wagon",
        "wiggu_v": "Police Car",
        "willi_v": "Tractor",
        "witchcar": "Witch's Broom",
        "zombi_v": "Zombie Car"
    }

    def interpret_slot_data(self, slot_data: dict[str, any]):
        #this is called by tools like UT

        regen = False
        for key, value in slot_data.items():
            if key in self.options_dataclass.type_hints:
                getattr(self.options, key).value = value
                regen = True

        regen = hook_interpret_slot_data(self, self.player, slot_data) or regen
        return regen

    @classmethod
    def stage_assert_generate(cls, multiworld) -> None:
        runGenerationDataValidation()


    def create_regions(self):
        before_create_regions(self, self.multiworld, self.player)

        create_regions(self, self.multiworld, self.player)

        location_game_complete = self.multiworld.get_location(victory_names[get_option_value(self.multiworld, self.player, 'goal')], self.player)
        location_game_complete.address = None

        for unused_goal in [self.multiworld.get_location(name, self.player) for name in victory_names if name != location_game_complete.name]:
            unused_goal.parent_region.locations.remove(unused_goal)

        location_game_complete.place_locked_item(
            SimpsonsHitAndRunItem("__Victory__", ItemClassification.progression, None, player=self.player))

        data_path = Path("data") / "cards.json"
        cards_data = json.loads(pkgutil.get_data(__name__, str(data_path)).decode())

        after_create_regions(self, self.multiworld, self.player, cards_data)

    def create_items(self):
        # Generate item pool
        pool = []
        traps = []
        configured_item_names = self.item_id_to_name.copy()

        trap_options = {
            "Eject": "eject",
            "Launch": "launch",
            "Duff Trap": "duff",
            "Hit N Run": "hnr"
        }

        cars_by_level = {}
        for item in item_name_to_item.values():
            for category in item.get("category", []):
                match = re.match(r"Level ([1-7]) Car", category)
                if match and not item.get("progression", False):
                    level = int(match.group(1))
                    cars_by_level.setdefault(level, []).append(item)

        for car in [self.random.choice(cars) for cars in cars_by_level.values()]:
            car["progression"] = True

        if (self.options.missionlocks != 0):
            carlocks = self.random.sample(
                list(self.vehicle_item_to_vehicle.keys()),
                int(len(self.vehicle_item_to_vehicle) * (self.options.missionlocks / 100))
            )
            missions = self.random.sample(range(1, 50), len(carlocks))

            self.mission_locks = dict(zip(missions, carlocks))

            for car in self.mission_locks.values():
                item = self.item_name_to_item[self.vehicle_item_to_vehicle[car]]
                item["progression"] = True
        else:
            self.mission_locks = {0 : "NO MISSIONLOCKS"}

        for name in configured_item_names.values():
            item = self.item_name_to_item[name]
            item_count = int(item.get("count", 1))

            if name in trap_options and get_option_value(self.multiworld, self.player, trap_options[name]):
                traps.append(name)

            if "category" in item:
                if not is_item_enabled(self.multiworld, self.player, item):
                    item_count = 0

            if item_count == 0: continue

            for i in range(item_count):
                new_item = self.create_item(name)
                pool.append(new_item)

            if item.get("early"): # only early
                self.multiworld.early_items[self.player][name] = item_count
            if item.get("local"): # only local
                if name not in self.multiworld.local_items[self.player].value:
                    self.options.local_items.value.add(name)


        pool = before_create_items_starting(pool, self, self.multiworld, self.player)

        items_started = []



        self.start_inventory = {i.name: items_started.count(i) for i in items_started}

        pool = before_create_items_filler(pool, self, self.multiworld, self.player)
        pool = self.adjust_filler_items(pool, traps)
        pool = after_create_items(pool, self, self.multiworld, self.player)

        # need to put all of the items in the pool so we can have a full state for placement
        # then will remove specific item placements below from the overall pool
        self.multiworld.itempool += pool

    def create_item(self, name: str) -> Item:
        name = before_create_item(name, self, self.multiworld, self.player)

        item = self.item_name_to_item[name]
        classification = ItemClassification.filler

        if "trap" in item and item["trap"]:
            classification = ItemClassification.trap

        if "useful" in item and item["useful"]:
            classification = ItemClassification.useful

        if "progression" in item and item["progression"]:
            classification = ItemClassification.progression

        if "progression_skip_balancing" in item and item["progression_skip_balancing"]:
            classification = ItemClassification.progression_skip_balancing

        item_object = SimpsonsHitAndRunItem(name, classification,
                                            self.item_name_to_id[name], player=self.player)

        item_object = after_create_item(item_object, self, self.multiworld, self.player)

        return item_object

    def set_rules(self):
        before_set_rules(self, self.multiworld, self.player)

        set_rules(self, self.multiworld, self.player)

        after_set_rules(self, self.multiworld, self.player)

    def generate_basic(self):
        before_generate_basic(self, self.multiworld, self.player)

        # Handle item forbidding
        manual_locations_with_forbid = {location['name']: location for location in location_name_to_location.values() if "dont_place_item" in location or "dont_place_item_category" in location}
        locations_with_forbid = [l for l in self.multiworld.get_unfilled_locations(player=self.player) if l.name in manual_locations_with_forbid.keys()]
        for location in locations_with_forbid:
            manual_location = manual_locations_with_forbid[location.name]
            forbidden_item_names = []

            if "dont_place_item" in manual_location:
                if len(manual_location["dont_place_item"]) == 0:
                    continue

                forbidden_item_names.extend([i["name"] for i in item_name_to_item.values() if i["name"] in manual_location["dont_place_item"]])

            if "dont_place_item_category" in manual_location:
                if len(manual_location["dont_place_item_category"]) == 0:
                    continue

                forbidden_item_names.extend([i["name"] for i in item_name_to_item.values() if "category" in i and set(i["category"]).intersection(manual_location["dont_place_item_category"])])

            if len(forbidden_item_names) > 0:
                forbid_items_for_player(location, forbidden_item_names, self.player)
                forbidden_item_names.clear()

        # Handle specific item placements using fill_restrictive
        manual_locations_with_placements = {location['name']: location for location in location_name_to_location.values() if "place_item" in location or "place_item_category" in location}
        locations_with_placements = [l for l in self.multiworld.get_unfilled_locations(player=self.player) if l.name in manual_locations_with_placements.keys()]
        for location in locations_with_placements:
            manual_location = manual_locations_with_placements[location.name]
            eligible_items = []

            if "place_item" in manual_location:
                if len(manual_location["place_item"]) == 0:
                    continue

                eligible_items = [item for item in self.multiworld.itempool if item.name in manual_location["place_item"] and item.player == self.player]

                if len(eligible_items) == 0:
                    raise Exception("Could not find a suitable item to place at %s. No items that match %s." % (manual_location["name"], ", ".join(manual_location["place_item"])))

            if "place_item_category" in manual_location:
                if len(manual_location["place_item_category"]) == 0:
                    continue

                eligible_item_names = [i["name"] for i in item_name_to_item.values() if "category" in i and set(i["category"]).intersection(manual_location["place_item_category"])]
                eligible_items = [item for item in self.multiworld.itempool if item.name in eligible_item_names and item.player == self.player]

                if len(eligible_items) == 0:
                    raise Exception("Could not find a suitable item to place at %s. No items that match categories %s." % (manual_location["name"], ", ".join(manual_location["place_item_category"])))

            if "dont_place_item" in manual_location:
                if len(manual_location["dont_place_item"]) == 0:
                    continue

                eligible_items = [item for item in eligible_items if item.name not in manual_location["dont_place_item"]]

                if len(eligible_items) == 0:
                    raise Exception("Could not find a suitable item to place at %s. No items that match placed_items(_category) because of forbidden %s." % (manual_location["name"], ", ".join(manual_location["dont_place_item"])))

            if "dont_place_item_category" in manual_location:
                if len(manual_location["dont_place_item_category"]) == 0:
                    continue

                forbidden_item_names = [i["name"] for i in item_name_to_item.values() if "category" in i and set(i["category"]).intersection(manual_location["dont_place_item_category"])]

                eligible_items = [item for item in eligible_items if item.name not in forbidden_item_names]

                if len(eligible_items) == 0:
                    raise Exception("Could not find a suitable item to place at %s. No items that match placed_items(_category) because of forbidden categories %s." % (manual_location["name"], ", ".join(manual_location["dont_place_item_category"])))
                forbidden_item_names.clear()


            # if we made it here and items is empty, then we encountered an unknown issue... but also can't do anything to place, so error
            if len(eligible_items) == 0:
                raise Exception("Custom item placement at location %s failed." % (manual_location["name"]))

            item_to_place = self.random.choice(eligible_items)
            location.place_locked_item(item_to_place)

            # remove the item we're about to place from the pool so it isn't placed twice
            self.multiworld.itempool.remove(item_to_place)


        after_generate_basic(self, self.multiworld, self.player)

        # Enable this in Meta.json to generate a diagram of your manual.  Only works on 0.4.4+
        if enable_region_diagram:
            from Utils import visualize_regions
            visualize_regions(self.multiworld.get_region("Menu", self.player), f"{self.game}_{self.player}.puml")

    def pre_fill(self):
        # DataValidation after all the hooks are done but before fill
        runPreFillDataValidation(self, self.multiworld)

    def fill_slot_data(self):
        slot_data = before_fill_slot_data({}, self, self.multiworld, self.player)

        slot_data["version"] = self.apworld_version
        # slot_data["DeathLink"] = bool(self.multiworld.death_link[self.player].value)
        common_options = set(PerGameCommonOptions.type_hints.keys())
        for option_key, _ in self.options_dataclass.type_hints.items():
            if option_key in common_options:
                continue
            slot_data[option_key] = get_option_value(self.multiworld, self.player, option_key)

        slot_data["card_locations"] = [card["id"] for card in card_table]

        slot_data = after_fill_slot_data(slot_data, self, self.multiworld, self.player)

        return slot_data

    def generate_output(self, output_directory: str):
        filename = f"{self.multiworld.get_out_file_name_base(self.player)}_SHAR"

        traffic_table = (
            self.random.sample(list(self.vehicle_item_to_vehicle.keys()), 35)
            if self.options.shuffletraffic
            else ["NO TRAFFIC"]
        )

        gen(
            output_directory,
            filename,
            f"AP-{self.multiworld.seed_name}-P{self.player}-{self.multiworld.get_file_safe_player_name(self.player)}",
            f"AP-{self.multiworld.seed_name}-P{self.player}",
            card_table,
            traffic_table,
            self.mission_locks,
            self.player
        )

    def write_spoiler(self, spoiler_handle):
        before_write_spoiler(self, self.multiworld, spoiler_handle)

    ###
    # Non-standard AP world methods
    ###

    def add_filler_items(self, item_pool, traps):
        Utils.deprecate("Use adjust_filler_items instead.")
        return self.adjust_filler_items(item_pool, traps)

    def adjust_filler_items(self, item_pool, traps):
        extras = len(self.multiworld.get_unfilled_locations(player=self.player)) - len(item_pool)

        if extras > 0:
            trap_percent = get_option_value(self.multiworld, self.player, "filler_traps")
            if not traps:
                trap_percent = 0

            trap_count = extras * trap_percent // 100
            filler_count = extras - trap_count

            for _ in range(0, trap_count):
                extra_item = self.create_item(self.random.choice(traps))
                item_pool.append(extra_item)

            for _ in range(0, filler_count):
                extra_item = self.create_item("10 Coins")
                item_pool.append(extra_item)
        elif extras < 0:
            logging.warning(f"{self.game} has more items than locations. {abs(extras)} non-progression items will be removed at random.")
            fillers = [item for item in item_pool if item.classification == ItemClassification.filler]
            traps = [item for item in item_pool if item.classification == ItemClassification.trap]
            useful = [item for item in item_pool if item.classification == ItemClassification.useful]
            self.random.shuffle(fillers)
            self.random.shuffle(traps)
            self.random.shuffle(useful)
            for _ in range(0, abs(extras)):
                popped = None
                if fillers:
                    popped = fillers.pop()
                elif traps:
                    popped = traps.pop()
                elif useful:
                    popped = useful.pop()
                else:
                    logging.warning("Could not remove enough non-progression items from the pool.")
                    break
                item_pool.remove(popped)

        return item_pool

    def get_item_counts(self, player: Optional[int] = None, reset: bool = False) -> dict[str, int]:
        """returns the player real item count"""
        if player is None:
            player = self.player
        if not self.item_counts.get(player, {}) or reset:
            real_pool = self.multiworld.get_items()
            self.item_counts[player] = {i.name: real_pool.count(i) for i in real_pool if i.player == player}
        return self.item_counts.get(player)

    def client_data(self):
        return {
            "game": self.game,
            'player_name': self.multiworld.get_player_name(self.player),
            'player_id': self.player,
            'items': self.item_name_to_item,
            'locations': self.location_name_to_location,
            # todo: extract connections out of multiworld.get_regions() instead, in case hooks have modified the regions.
            'regions': region_table,
            'categories': category_table
        }
