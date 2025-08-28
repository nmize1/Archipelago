# Object classes from AP core, to represent an entire MultiWorld and this individual World that's part of it
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState

# Object classes from Manual -- extending AP core -- representing items and locations that are used in generation
from ..Items import ManualItem
from ..Locations import ManualLocation

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



# Called before regions and locations are created. Not clear why you'd want this, but it's here. Victory location is included, but Victory event is not placed yet.
def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after regions and locations are created, in case you want to see or modify that information. Victory location is included.
def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to remove locations from the world
    locationNamesToRemove = [] # List of location names

    # Add your code here to calculate which locations to remove

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
    #Add starting items and set locations for linear setting
    #Linear: Place level 1 and family sedan in start inventory. Remove regular level items.
    if world.options.levelsanity == 0:
        multiworld.push_precollected(next(item for item in item_pool if item.name == "Level 1"))
        multiworld.push_precollected(next(item for item in item_pool if item.name == "Family Sedan"))
        item_pool.remove(next(item for item in item_pool if item.name == "Level 1"))
        item_pool.remove(next(item for item in item_pool if item.name == "Family Sedan"))

        itemNamesToRemove = ["Level 2", "Level 3", "Level 4", "Level 5", "Level 6", "Level 7"]
        for itemName in itemNamesToRemove:
            item = next(i for i in item_pool if i.name == itemName)
            print(item.name)
            item_pool.remove(item)
        print(item_pool)

    #level: Place  level and it's starting car in start inventory and remove progressive level items
    elif world.options.levelsanity == 1:
        lvl = world.random.randrange(6)
        if lvl == 0:
            multiworld.push_precollected(next(item for item in item_pool if item.name == "Level 1"))
            multiworld.push_precollected(next(item for item in item_pool if item.name == "Family Sedan"))
            item_pool.remove(next(item for item in item_pool if item.name == "Level 1"))
            item_pool.remove(next(item for item in item_pool if item.name == "Family Sedan"))
        elif lvl == 1:
            multiworld.push_precollected(next(item for item in item_pool if item.name == "Level 2"))
            multiworld.push_precollected(next(item for item in item_pool if item.name == "Honor Roller"))
            item_pool.remove(next(item for item in item_pool if item.name == "Level 2"))
            item_pool.remove(next(item for item in item_pool if item.name == "Honor Roller"))
        elif lvl == 2:
            multiworld.push_precollected(next(item for item in item_pool if item.name == "Level 3"))
            multiworld.push_precollected(next(item for item in item_pool if item.name == "Malibu Stacy Car"))
            item_pool.remove(next(item for item in item_pool if item.name == "Level 3"))
            item_pool.remove(next(item for item in item_pool if item.name == "Malibu Stacy Car"))
        elif lvl == 3:
            multiworld.push_precollected(next(item for item in item_pool if item.name == "Level 4"))
            multiworld.push_precollected(next(item for item in item_pool if item.name == "Canyonero"))
            item_pool.remove(next(item for item in item_pool if item.name == "Level 4"))
            item_pool.remove(next(item for item in item_pool if item.name == "Canyonero"))
        elif lvl == 4:
            multiworld.push_precollected(next(item for item in item_pool if item.name == "Level 5"))
            multiworld.push_precollected(next(item for item in item_pool if item.name == "Longhorn"))
            item_pool.remove(next(item for item in item_pool if item.name == "Level 5"))
            item_pool.remove(next(item for item in item_pool if item.name == "Longhorn"))
        elif lvl == 5:
            multiworld.push_precollected(next(item for item in item_pool if item.name == "Level 6"))
            multiworld.push_precollected(next(item for item in item_pool if item.name == "Ferrini - Red"))
            item_pool.remove(next(item for item in item_pool if item.name == "Level 6"))
            item_pool.remove(next(item for item in item_pool if item.name == "Ferrini - Red"))
        elif lvl == 6:
            multiworld.push_precollected(next(item for item in item_pool if item.name == "Level 7"))
            multiworld.push_precollected(next(item for item in item_pool if item.name == "70's Sports Car"))
            item_pool.remove(next(item for item in item_pool if item.name == "Level 7"))
            item_pool.remove(next(item for item in item_pool if item.name == "70's Sports Car"))

        item_pool = [item for item in item_pool if not item.name.startswith("Progressive Level")]

    else:
        raise OptionError("Levelsanity option not recognized.")

    if world.options.shuffleebrake == False:
        multiworld.push_precollected(next(item for item in item_pool if item.name == "Homer E-Brake"))
        item_pool.remove(next(item for item in item_pool if item.name == "Homer E-Brake"))
        multiworld.push_precollected(next(item for item in item_pool if item.name == "Bart E-Brake"))
        item_pool.remove(next(item for item in item_pool if item.name == "Bart E-Brake"))
        multiworld.push_precollected(next(item for item in item_pool if item.name == "Lisa E-Brake"))
        item_pool.remove(next(item for item in item_pool if item.name == "Lisa E-Brake"))
        multiworld.push_precollected(next(item for item in item_pool if item.name == "Marge E-Brake"))
        item_pool.remove(next(item for item in item_pool if item.name == "Marge E-Brake"))
        multiworld.push_precollected(next(item for item in item_pool if item.name == "Apu E-Brake"))
        item_pool.remove(next(item for item in item_pool if item.name == "Apu E-Brake"))

    if world.options.moverandomizer == False:
        multiworld.push_precollected(next(item for item in item_pool if item.name == "Homer Double Jump"))
        item_pool.remove(next(item for item in item_pool if item.name == "Homer Double Jump"))
        multiworld.push_precollected(next(item for item in item_pool if item.name == "Bart Double Jump"))
        item_pool.remove(next(item for item in item_pool if item.name == "Bart Double Jump"))
        multiworld.push_precollected(next(item for item in item_pool if item.name == "Lisa Double Jump"))
        item_pool.remove(next(item for item in item_pool if item.name == "Lisa Double Jump"))
        multiworld.push_precollected(next(item for item in item_pool if item.name == "Marge Double Jump"))
        item_pool.remove(next(item for item in item_pool if item.name == "Marge Double Jump"))
        multiworld.push_precollected(next(item for item in item_pool if item.name == "Apu Double Jump"))
        item_pool.remove(next(item for item in item_pool if item.name == "Apu Double Jump"))

        multiworld.push_precollected(next(item for item in item_pool if item.name == "Homer Attack"))
        item_pool.remove(next(item for item in item_pool if item.name == "Homer Attack"))
        multiworld.push_precollected(next(item for item in item_pool if item.name == "Bart Attack"))
        item_pool.remove(next(item for item in item_pool if item.name == "Bart Attack"))
        multiworld.push_precollected(next(item for item in item_pool if item.name == "Lisa Attack"))
        item_pool.remove(next(item for item in item_pool if item.name == "Lisa Attack"))
        multiworld.push_precollected(next(item for item in item_pool if item.name == "Marge Attack"))
        item_pool.remove(next(item for item in item_pool if item.name == "Marge Attack"))
        multiworld.push_precollected(next(item for item in item_pool if item.name == "Apu Attack"))
        item_pool.remove(next(item for item in item_pool if item.name == "Apu Attack"))


    # Use this hook to remove items from the item pool
    itemNamesToRemove = [] # List of item names

    # Add your code here to calculate which items to remove.
    #
    # Because multiple copies of an item can exist, you need to add an item name
    # to the list multiple times if you want to remove multiple copies of it.

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
def after_create_item(item: ManualItem, world: World, multiworld: MultiWorld, player: int) -> ManualItem:
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
