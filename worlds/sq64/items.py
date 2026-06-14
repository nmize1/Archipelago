from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import SQ64World

ITEM_NAME_TO_ID = {
    "Progressive Jump": 1,
    "Wall Jump": 2,
    "Swim": 3,
    "Spin": 4,
    "Dive": 5,
    "Backflip": 6,
    "Glide": 7,
    "Dash": 8,
    "Ground Pound": 9,
    "HUB: Box Button": 10,
    "Level 1": 11,
    "L1: Box Button": 12,
    "L1: Portals": 13,
    "Extra Life": 14,
    "Star": 15
}

DEFAULT_ITEM_CLASSIFICATION = {
    "Progressive Jump": ItemClassification.progression,
    "Wall Jump": ItemClassification.progression,
    "Swim": ItemClassification.progression,
    "Spin": ItemClassification.progression,
    "Dive": ItemClassification.useful,
    "Backflip": ItemClassification.progression,
    "Glide": ItemClassification.progression,
    "Dash": ItemClassification.progression,
    "Ground Pound": ItemClassification.progression,
    "HUB: Box Button": ItemClassification.progression,
    "Level 1": ItemClassification.progression,
    "L1: Box Button": ItemClassification.progression,
    "L1: Portals": ItemClassification.progression,
    "Extra Life": ItemClassification.filler,
    "Star": ItemClassification.progression_skip_balancing
}

class SQ64Item(Item):
    game = "Star Quest 64"


def get_random_filler_item_name(world: SQ64World) -> str:
    return "Extra Life"

def create_item_with_correct_classification(world: SQ64World, name: str) -> SQ64Item:
    classification = DEFAULT_ITEM_CLASSIFICATION[name]

    return SQ64Item(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: SQ64World) -> None:
    itempool: list[Item] = []

    for item, _ in ITEM_NAME_TO_ID.items():
        if item not in ["Star", "Extra Life"]:
            itempool.append(world.create_item(item))

    itempool.append(world.create_item("Progressive Jump")) #second jump

    for _ in range(world.options.stars_to_goal):
        itempool.append(world.create_item("Star"))

    num_items = len(itempool)

    num_unfilled_locs = len(world.multiworld.get_unfilled_locations(world.player))

    needed_filler = num_unfilled_locs - num_items
    itempool += [world.create_filler() for _ in range(needed_filler)]
    world.multiworld.itempool += itempool

