# Object classes from AP core, to represent an entire MultiWorld and this individual World that's part of it
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState
from ..Locations import location_name_to_location
# Object classes from Manual -- extending AP core -- representing items and locations that are used in generation
from ..Items import SimpsonsHitAndRunItem
from Options import OptionError
from ..Locations import SimpsonsHitAndRunLocation

# Raw JSON data from the Manual apworld, respectively:
#          data/game.json, data/items.json, data/locations.json, data/regions.json
#
from ..Data import game_table, item_table, location_table, region_table

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value

# calling logging.info("message") anywhere below in this file will output the message to both console and log file
import logging
import uuid

########################################################################################
## Order of method calls when the world generates:
##    1. create_regions - Creates regions and locations
##    2. create_items - Creates the item pool
##    3. set_rules - Creates rules for accessing regions and locations
##    4. generate_basic - Runs any post item pool options, like place item/category
##    5. pre_fill - Creates the victory location
##
## The create_item method is used by plando and start_inventory settings to create an item from an item name.
## The fill_slot_data method will be used to send data to the Manual client for later use, like deathlink.
########################################################################################

card_table = []

# Called before regions and locations are created. Not clear why you'd want this, but it's here. Victory location is included, but Victory event is not placed yet.
def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after regions and locations are created, in case you want to see or modify that information. Victory location is included.
def after_create_regions(world: World, multiworld: MultiWorld, player: int, cards_data):
    # Use this hook to remove locations from the world

    all_chosen_card_names = []

    if world.options.cardlogic != 0:
        raise OptionError("Chosen cardlogic level is not implemented.")

    if world.options.cardlogic == 0:
        logic = 'carless'
    elif world.options.cardlogic == 1:
        logic = 'car'
    elif world.options.cardlogic == 2:
        logic = 'glitched'

    for level, level_cards in cards_data.items():
        if world.options.shufflecards:
            valid_cards = [card for card in level_cards if card[logic] != "N/A"]
            c_cards = world.random.sample(valid_cards, 7)
        else:
            c_cards = level_cards[:7]

        for card in c_cards:
            card_table.append({
                "id": location_name_to_location[card["Desc"]]["id"],
                "level": level,
                "name": card["Desc"],
                "X": card["X"],
                "Y": card["Y"],
                "Z": card["Z"],
                "category": [f"{level} CARD"]
            })
            all_chosen_card_names.append(card["Desc"])

    card_table.sort(key=lambda c: (int(c["level"].split()[-1]), c["id"]))

    if not hasattr(multiworld, "generation_is_fake"):
        locationNamesToRemove = [
            loc["name"] for loc in world.location_table
            if "CARD" in loc["name"] and loc["name"] not in all_chosen_card_names
        ]
    else:
        print("FAKE GENERATION")
        locationNamesToRemove = []

    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name in locationNamesToRemove:
                    region.locations.remove(location)

    if hasattr(multiworld, "clear_location_cache"):
        multiworld.clear_location_cache()

# The item pool before starting items are processed, in case you want to see the raw item pool at that stage
def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# The item pool after starting items are processed but before filler is added, in case you want to see the raw item pool at that stage
def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    # Use this hook to remove items from the item pool
    itemNamesToRemove = [] # List of item names
    itemNamesToStart = []

    #Add starting items and set locations for linear setting
    #Linear: Place level 1 and family sedan in start inventory. Remove regular level items.
    if world.options.levelsanity == 0:
        itemNamesToStart.extend(["Level 1", "Family Sedan"])
        itemNamesToRemove.extend(["Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6", "Level 7", "Family Sedan"])
        #print(item_pool)

    #level: Place  level and it's starting car in start inventory and remove progressive level items
    elif world.options.levelsanity == 1:
        lvl = world.random.randrange(6)
        if lvl == 0:
            itemNamesToStart.extend(["Level 1", "Family Sedan"])
            itemNamesToRemove.extend(["Level 1", "Family Sedan"])
        elif lvl == 1:
            itemNamesToStart.extend(["Level 2", "Honor Roller"])
            itemNamesToRemove.extend(["Level 2", "Honor Roller"])
        elif lvl == 2:
            itemNamesToStart.extend(["Level 3", "Malibu Stacy Car"])
            itemNamesToRemove.extend(["Level 3", "Malibu Stacy Car"])
        elif lvl == 3:
            itemNamesToStart.extend(["Level 4", "Canyonero"])
            itemNamesToRemove.extend(["Level 4", "Canyonero"])
        elif lvl == 4:
            itemNamesToStart.extend(["Level 5", "Longhorn"])
            itemNamesToRemove.extend(["Level 5", "Longhorn"])
        elif lvl == 5:
            itemNamesToStart.extend(["Level 6", "Ferrini - Red"])
            itemNamesToRemove.extend(["Level 6", "Ferrini - Red"])
        elif lvl == 6:
            itemNamesToStart.extend(["Level 7", "70s Sports Car"])
            itemNamesToRemove.extend(["Level 7", "70s Sports Car"])

        for i in range(6):
            itemNamesToRemove.append("Progressive Level")

    else:
        raise OptionError("Levelsanity option not recognized.")

    if world.options.shuffleebrake == False:
        itemNamesToStart.extend(["Homer E-Brake", "Bart E-Brake", "Lisa E-Brake", "Marge E-Brake", "Apu E-Brake"])
        itemNamesToRemove.extend(["Homer E-Brake", "Bart E-Brake", "Lisa E-Brake", "Marge E-Brake", "Apu E-Brake"])

    if world.options.moverandomizer == False:
        itemNamesToStart.extend(["Homer Attack", "Bart Attack", "Lisa Attack", "Marge Attack", "Apu Attack"])
        itemNamesToRemove.extend(["Homer Attack", "Bart Attack", "Lisa Attack", "Marge Attack", "Apu Attack"])
        for i in range(2):
            itemNamesToStart.extend(["Homer Progressive Jump", "Bart Progressive Jump", "Lisa Progressive Jump",
                                      "Marge Progressive Jump", "Apu Progressive Jump"])
            itemNamesToRemove.extend(["Homer Progressive Jump", "Bart Progressive Jump", "Lisa Progressive Jump",
                                      "Marge Progressive Jump", "Apu Progressive Jump"])

    if world.options.startjumplevel > 0 and world.options.moverandomizer == True:
        for i in range(world.options.startjumplevel):
            itemNamesToStart.extend(["Homer Progressive Jump", "Bart Progressive Jump", "Lisa Progressive Jump",
                                      "Marge Progressive Jump", "Apu Progressive Jump"])
            itemNamesToRemove.extend(["Homer Progressive Jump", "Bart Progressive Jump", "Lisa Progressive Jump",
                                      "Marge Progressive Jump", "Apu Progressive Jump"])

    if world.options.shufflegagfinder == False:
        itemNamesToRemove.extend(["Homer Gagfinder", "Bart Gagfinder", "Lisa Gagfinder", "Marge Gagfinder", "Apu Gagfinder"])

    if world.options.shufflecheckeredflags == False:
        itemNamesToRemove.extend(["Homer Checkered Flag", "Bart Checkered Flag", "Lisa Checkered Flag", "Marge Checkered Flag", "Apu Checkered Flag"])

    if world.options.eject == False:
        itemNamesToRemove.extend(["Eject"] * 20)

    if world.options.duff == False:
        itemNamesToRemove.extend(["Duff Trap"] * 20)

    if world.options.hnr == False:
        itemNamesToRemove.extend(["Hit N Run"] * 20)

    if world.options.launch == False:
        itemNamesToRemove.extend(["Launch"] * 20)

    for itemName in itemNamesToStart:
        item = next(i for i in item_pool if i.name == itemName)
        multiworld.push_precollected(next(i for i in item_pool if i == item))

    for itemName in itemNamesToRemove:
        item = next(i for i in item_pool if i.name == itemName)
        item_pool.remove(item)

    return item_pool

    # Some other useful hook options:

    ## Place an item at a specific location
    # location = next(l for l in multiworld.get_unfilled_locations(player=player) if l.name == "Location Name")
    # item_to_place = next(i for i in item_pool if i.name == "Item Name")
    # location.place_locked_item(item_to_place)
    # item_pool.remove(item_to_place)

# The complete item pool prior to being set for generation is provided here, in case you want to make changes to it
def after_create_items(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# Called before rules for accessing regions and locations are created. Not clear why you'd want this, but it's here.
def before_set_rules(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after rules for accessing regions and locations are created, in case you want to see or modify that information.
def after_set_rules(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to modify the access rules for a given location

    def Example_Rule(state: CollectionState) -> bool:
        # Calculated rules take a CollectionState object and return a boolean
        # True if the player can access the location
        # CollectionState is defined in BaseClasses
        return True

    ## Common functions:
    # location = world.get_location(location_name, player)
    # location.access_rule = Example_Rule

    ## Combine rules:
    # old_rule = location.access_rule
    # location.access_rule = lambda state: old_rule(state) and Example_Rule(state)
    # OR
    # location.access_rule = lambda state: old_rule(state) or Example_Rule(state)

# The item name to create is provided before the item is created, in case you want to make changes to it
def before_create_item(item_name: str, world: World, multiworld: MultiWorld, player: int) -> str:
    return item_name

# The item that was created is provided after creation, in case you want to modify the item
def after_create_item(item: SimpsonsHitAndRunItem, world: World, multiworld: MultiWorld, player: int) -> SimpsonsHitAndRunItem:
    return item

# This method is run towards the end of pre-generation, before the place_item options have been handled and before AP generation occurs
def before_generate_basic(world: World, multiworld: MultiWorld, player: int) -> list:
    pass

# This method is run at the very end of pre-generation, once the place_item options have been handled and before AP generation occurs
def after_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This is called before slot data is set and provides an empty dict ({}), in case you want to modify it before Manual does
def before_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called after slot data is set and provides the slot data at the time, in case you want to check and modify it after Manual is done with it
def after_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    slot_data["id"] = str(uuid.uuid4())

    # Generate costs for shops
    min = world.options.minprice
    max = world.options.maxprice
    if min > max:
        print(f"Simpsons: Min shop price {min} is greater than max shop price {max}. Setting min and max to {max}.")
        min = max
    scale = world.options.shopscalemod

    slot_data["costs"] = [
        world.random.randint(
            min * (1 if level == 1 else (level - 1) * scale),
            max * (1 if level == 1 else (level - 1) * scale)
        )
        for level in range(1, 8)
        for _ in range(6)
    ]


    return slot_data

# This is called right at the end, in case you want to write stuff to the spoiler log
def before_write_spoiler(world: World, multiworld: MultiWorld, spoiler_handle) -> None:
    pass
