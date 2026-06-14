from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import SQ64World

def create_and_connect_regions(world: SQ64World) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: SQ64World) -> None:
    hub = Region("HUB", world.player, world.multiworld)
    hub_boxes = Region("HUB Boxes", world.player, world.multiworld)
    hub_enemies = Region("HUB Enemies", world.player, world.multiworld)
    l1 = Region("Level 1", world.player, world.multiworld)
    l1_boxes = Region("Level 1 Boxes", world.player, world.multiworld)
    l1_enemies = Region("Level 1 Enemies", world.player, world.multiworld)

    regions = [hub, hub_boxes, hub_enemies, l1, l1_boxes, l1_enemies]

    world.multiworld.regions += regions

def connect_regions(world: SQ64World) -> None:
    hub = world.get_region("HUB")
    hub_boxes = world.get_region("HUB Boxes")
    hub_enemies = world.get_region("HUB Enemies")
    l1 = world.get_region("Level 1")
    l1_boxes = world.get_region("Level 1 Boxes")
    l1_enemies = world.get_region("Level 1 Enemies")

    hub.connect(l1, "HUB to L1")
    hub.connect(hub_boxes, "HUB to HUB Boxes")
    hub.connect(hub_enemies, "HUB to HUB Enemies")
    l1.connect(l1_boxes, "L1 to L1 Boxes")
    l1.connect(l1_enemies, "L1 to L1 Enemies")