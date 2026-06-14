from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items
from ..simpsonshitnrun.locations import create_regular_locations

if TYPE_CHECKING:
    from .world import SQ64World

LOCATION_NAME_TO_ID = {
    "HUB: L2 Star": 1,
    "HUB: L3 Star": 2,
    "HUB: L4 Star": 3,
    "HUB: Red Coin Star": 4,
    "L1: Defeat Boss Slime Star": 5,
    "L1: Precarious Platforms Star": 6,
    "L1: The Tower's Secret Star": 7,
    "L1: Red Coins in the Cave Star": 8,
    "L1: 80 Coin Star": 9,
    "L1: Coin Box Near Beach": 10,
    "L1: Coin Box Behind Tallest Cliff": 11,
    "L1: Coin Box on Shortest Cliff": 12,
    "L1: Coin Box on Tower Ramp Balcony": 13,
    "HUB: Coin Box Near Spawn": 14,
    "HUB: Coin Box in Tower": 15,
    "HUB: Read Star List Sign": 16,
    "L1: Read Star List Sign": 17,
    "L1: Read Crossroad Sign": 18,
    "HUB: Read Tower Sign": 19,
    "HUB: Tower Extra Life": 20,
    "L1: Boss Cliff Extra Life": 21,
    "L1: 2D Extra Life": 22,
    "L1: Falling Block Extra Life": 23,
    "HUB: Talk to Saphy": 24,
    "L1: Talk to Saphy": 25,
    "L1: Blue Slime 1": 26,
    "L1: Blue Slime 2": 27,
    "L1: Blue Slime 3": 28,
    "L1: Red Slime 1": 29,
    "L1: Red Slime 2": 30,
    "L1: 2D Blue Slime 1": 31,
    "L1: 2D Blue Slime 2": 32,
    "L1: 2D Blue Slime 3": 33,
    "L1: Cave Flying Slime 1": 34,
    "L1: Cave Flying Slime 2": 35,
    "L1: Cave Flying Slime 3": 36,
    "L1: Cave Flying Slime 4": 37,
    "L1: Cave Flying Slime 5": 38,
    "L1: Cave Flying Slime 6": 39,
    "HUB: Red Slime 1": 40,
    "HUB: Red Slime 2": 41,
    "HUB: Red Slime 3": 42
}

class SQ64Location(Location):
    game = "Star Quest 64"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: SQ64World) -> None:
    create_regular_locations(world)

def create_regular_locations(world: SQ64World) -> None:
    hub = world.get_region("HUB")
    hub_boxes = world.get_region("HUB Boxes")
    hub_enemies = world.get_region("HUB Enemies")
    l1 = world.get_region("Level 1")
    l1_boxes = world.get_region("Level 1 Boxes")
    l1_enemies = world.get_region("Level 1 Enemies")

    l1_boxes.add_locations(get_location_names_with_ids([
        "L1: Coin Box Near Beach", "L1: Coin Box Behind Tallest Cliff",
        "L1: Coin Box on Shortest Cliff", "L1: Coin Box on Tower Ramp Balcony"
    ]))

    l1_enemies.add_locations(get_location_names_with_ids([
        "L1: Blue Slime 1", "L1: Blue Slime 2", "L1: Blue Slime 3", "L1: Red Slime 1", "L1: Red Slime 2",
        "L1: 2D Blue Slime 1", "L1: 2D Blue Slime 2", "L1: 2D Blue Slime 3", "L1: Cave Flying Slime 1",
        "L1: Cave Flying Slime 2", "L1: Cave Flying Slime 3", "L1: Cave Flying Slime 4", "L1: Cave Flying Slime 5", "L1: Cave Flying Slime 6"
    ]))

    l1.add_locations(get_location_names_with_ids([
        "L1: Defeat Boss Slime Star", "L1: Precarious Platforms Star", "L1: The Tower's Secret Star",
        "L1: Red Coins in the Cave Star", "L1: 80 Coin Star", "L1: Read Star List Sign", "L1: Read Crossroad Sign",
        "L1: Boss Cliff Extra Life", "L1: 2D Extra Life", "L1: Falling Block Extra Life", "L1: Talk to Saphy"
    ]))

    hub_boxes.add_locations(get_location_names_with_ids([
        "HUB: Coin Box Near Spawn", "HUB: Coin Box in Tower"
    ]))

    hub_enemies.add_locations(get_location_names_with_ids([
        "HUB: Red Slime 1", "HUB: Red Slime 2", "HUB: Red Slime 3"
    ]))

    hub.add_locations(get_location_names_with_ids([
        "HUB: L2 Star", "HUB: L3 Star", "HUB: L4 Star", "HUB: Red Coin Star", "HUB: Read Star List Sign",
        "HUB: Read Tower Sign", "HUB: Tower Extra Life", "HUB: Talk to Saphy"
    ]))
