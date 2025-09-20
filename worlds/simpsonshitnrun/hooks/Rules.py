from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState
from .World import card_table

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.

def allMissionsAccessible(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Has the player finished all missions?"""
    allMissions = []

    mission_categories = [
        "Level 1 Mission",
        "Level 2 Mission",
        "Level 3 Mission",
        "Level 4 Mission",
        "Level 5 Mission",
        "Level 6 Mission",
        "Level 7 Mission",
        "Bonus Mission"
    ]

    for category in mission_categories:
        allMissions += [
            location['name'] for location in world.location_table
            if category in location.get('category', []) and state.can_reach_location(location['name'], player)
        ]

    return len(allMissions) >= 77

def allStoryMissionsAccessible(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Has the player finished all story missions?"""
    allMissions = []

    mission_categories = [
        "Level 1 Mission",
        "Level 2 Mission",
        "Level 3 Mission",
        "Level 4 Mission",
        "Level 5 Mission",
        "Level 6 Mission",
        "Level 7 Mission",
    ]

    for category in mission_categories:
        allMissions += [
            location['name'] for location in world.location_table
            if category in location.get('category', []) and state.can_reach_location(location['name'], player)
        ]

    return len(allMissions) >= 50

def collectedWasps(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Has the player collected enough wasps?"""
    allWasps = []

    wasp_categories = [
        "Level 1 WASP",
        "Level 2 WASP",
        "Level 3 WASP",
        "Level 4 WASP",
        "Level 5 WASP",
        "Level 6 WASP",
        "Level 7 WASP",
    ]

    for category in wasp_categories:
        allWasps += [
            location['name'] for location in world.location_table
            if category in location.get('category', []) and state.can_reach_location(location['name'], player)
        ]

    return len(allWasps) >= (140 * world.options.wasppercent * .01)

def collectedCards(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Has the player collected enough cards?"""
    allCards = []

    card_categories = [
        "Level 1 CARD",
        "Level 2 CARD",
        "Level 3 CARD",
        "Level 4 CARD",
        "Level 5 CARD",
        "Level 6 CARD",
        "Level 7 CARD",
    ]

    for category in card_categories:
        allCards += [
            location['name'] for location in card_table
            if category in location.get('category', []) and state.can_reach_location(location['name'], player)
        ]

    return len(allCards) >= (49 * world.options.cardpercent * .01)

# Rule to expose the can_reach_location core function
def canReachLocation(world: World, multiworld: MultiWorld, state: CollectionState, player: int, location: str):
    """Can the player reach the given location?"""
    if state.can_reach_location(location, player):
        return True
    return False
