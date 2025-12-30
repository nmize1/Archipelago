from collections.abc import Mapping
from typing import Any

from Options import PerGameCommonOptions
from worlds.AutoWorld import World
from . import items, locations, options, regions, rules, web_world

class SimpsonsHitNRunWorld(World):
    """A 2003 Action Adventure game similar to the GTA series starring the Simpsons"""

    game = "Simpsons Hit and Run"

    options_dataclass = options.SimpsonsHitNRunOptions
    options: options.SimpsonsHitNRunOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Hub"
    apworld_version = "0.5.0"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str, make_prog: bool = False) -> items.SimpsonsHitNRunItem:
        return items.create_item_with_correct_classification(self, name, make_prog)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = {}

        slot_data["version"] = self.apworld_version
        common_options = set(PerGameCommonOptions.type_hints.keys())
        for option_key, _ in self.options_dataclass.type_hints.items():
            if option_key in common_options:
                continue
            slot_data[option_key] = getattr(self.options, option_key).value

        slot_data["card_locations"] = [locations.LOCATION_NAME_TO_ID[name] for level in locations.card_table for name in level]

        slot_data["missionlockdic"] = rules.missionlockdict
        slot_data["progcars"] = items.prog_cars
        slot_data["VerifyID"] = f"AP-{self.multiworld.seed_name}-P{self.player}-{self.multiworld.get_file_safe_player_name(self.player)}"

        slot_data["ingamehints"] = self.get_ingame_hints() if self.options.extrahintpolicy else "No hints"

        return slot_data

    def get_ingame_hints(self):
        igh = {}

        for item in items.prog_cars:
            try:
                loc = self.multiworld.find_item(item, self.player)
            except StopIteration:
                continue

            igh[items.ITEM_NAME_TO_ID[item]] = (loc.address, loc.player)

        for _, item in rules.missionlockdict.items():
            if item == "NO MISSIONLOCKS":
                continue

            try:
                loc = self.multiworld.find_item(item, self.player)
            except StopIteration:
                continue

            igh[items.ITEM_NAME_TO_ID[item]] = (loc.address, loc.player)

        return igh
