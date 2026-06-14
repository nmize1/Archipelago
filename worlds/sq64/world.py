from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World
from . import items, locations, regions, rules, web_world
from . import options as sq64_options

class SQ64World(World):
    """Star Quest 64 is a small 3D platformer made for the 2026 Archipelago Game Jam"""

    game = "Star Quest 64"
    web = web_world.SQ64WebWorld()

    options_dataclass = sq64_options.SQ64Options
    options: sq64_options.SQ64Options

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "HUB"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self):
        rules.set_all_rules(self)

    def create_items(self):
        items.create_all_items(self)

    def create_item(self, name: str) -> items.SQ64Item:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = self.options.as_dict("stars_to_goal")

        slot_data["version"] = "0.0.1"

        return slot_data