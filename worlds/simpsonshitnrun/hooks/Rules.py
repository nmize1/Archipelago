from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState
import ast

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

    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if "WASP - " in location.name and state.can_reach_location(location.name, player):
                    allWasps.append(location.name)

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

    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if "CARD - " in location.name and state.can_reach_location(location.name, player):
                    allCards.append(location.name)

    return len(allCards) >= (49 * world.options.cardpercent * .01)

def jumpsRequired(world: World, multiworld: MultiWorld, state: CollectionState, player: int, character: str, jumps: int, carsize: str):
    ret = "("
    jumps = int(jumps)
    if jumps > 0:
        ret += f"|{character} Progressive Jump:{jumps}|"

    carsize = carsize.strip().strip("[]{}(),\"'")
    if carsize != "none":
        sizes = ["Small", "Medium", "Large"]
        try:
            idx = sizes.index(carsize)
        except ValueError:
            print(f"{carsize} is not a valid carsize")
            return ""

        if jumps > 0:
            ret += " AND "
        ret += " OR ".join(f"|@{s} Cars|" for s in sizes[idx:])
        ret += f") OR |{character} Progressive Jump:{jumps + 1}|"

        return ret

    ret += ")"
    if ret == "()":
        ret = f"|{character} Progressive Jump:{0}|"

    return ret

def waspCarReq(world: World, multiworld: MultiWorld, state: CollectionState, player: int, character: str, badcars):
    if world.options.wasplogic == 0 or world.options.wasplogic == 3:
        return f"|{character} Attack|"

    if isinstance(badcars, str):
        try:
            badcars = ast.literal_eval(badcars)
        except:
            badcars = [badcars]

    if badcars is None:
        badcars = []

    cars = [
        "Ambulance", "Longhorn", "ATV", "Ferrini - Red", "El Carro Loco", "Book Burning Van", "36 Stutz Bearcat",
        "Burns Armored Truck", "Car Built For Homer", "Armored Truck", "Ferrini - Black", "Bonestorm Truck",
        "Cell Phone Car", "Cola Truck", "Cube Van", "Curator", "Donut Truck", "Duff Truck", "Fire Truck", "Hearse",
        "Krusty's Limo", "Pickup Truck", "Limo", "Milk Truck", "Nerd Car", "Nonuplets Minivan", "Coffin Car", "Kremlin",
        "Compact Car", "Chase Sedan", "Surveillance Van", "Electaurus", "Family Sedan", "Fish Van", "Open Wheel Race Car",
        "Hover Car", "Garbage Truck", "Glass Truck", "WWII Vehicle", "WWII Vehicle W/ Rocket", "Hearse", "Hover Bike",
        "70's Sports Car", "Honor Roller", "Planet Hype 50's Car", "Ice Cream Truck", "Itchy and Scratchy Movie Truck",
        "Knight Boat", "Clown Car", "Malibu Stacy Car", "Canyonero", "Minivan", "Moe's Sedan", "Monorail Car",
        "Mr. Plow", "Nuclear Waste Truck", "Obliteratatron Big Wheel Truck", "School Bus", "Pickup", "Pizza Van", "Plow King",
        "Speed Rocket", "Mini School Bus", "Globex Super Villain Car", "Sedan A", "Sedan B", "Ghost Ship", "Skinner's Sedan",
        "Mr. Burns' Limo", "Bandit", "Sports Car A", "Sports Car B", "SUV", "Taxi", "Vote Quimby Truck", "Station Wagon",
        "Police Car", "Tractor", "Zombie Car"
    ]

    if badcars == ["all"]:
        allowed = []  # no car requirement
    else:
        allowed = [f"|{car}|" for car in cars if car not in badcars]

    car_logic = " OR ".join(allowed) if allowed else ""

    if world.options.wasplogic == 1:
        if car_logic:
            car_logic = f"(|{character} Frink-o-Matic Wasp Bumper| AND ({car_logic}))"
        else:
            car_logic = f"|{character} Frink-o-Matic Wasp Bumper|"

    if car_logic:
        return f"{car_logic} OR |{character} Attack|"
    else:
        return f"|{character} Attack|"


def CheckSetForCharacter(world: World, multiworld: MultiWorld, state: CollectionState, player: int, option: str, character: str):
    chars = getattr(world.options, option).value
    if isinstance(character, str):
        character = character.strip().strip("'\"")

    if chars is None:
        return False

    if len(chars) == 0:
        return False

    if "All" in chars:
        return True

    return character in chars

def CheckSetForNotCharacter(world: World, multiworld: MultiWorld, state: CollectionState, player: int, option: str, character: str):
    chars = getattr(world.options, option).value
    if isinstance(character, str):
        character = character.strip().strip("'\"")

    if chars is None:
        return True

    if len(chars) == 0:
        return True

    if "All" in chars:
        return False

    return character not in chars

# Rule to expose the can_reach_location core function
def canReachLocation(world: World, multiworld: MultiWorld, state: CollectionState, player: int, location: str):
    """Can the player reach the given location?"""
    if state.can_reach_location(location, player):
        return True
    return False

