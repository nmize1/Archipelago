from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
import re
from . import rules

if TYPE_CHECKING:
    from .world import SimpsonsHitNRunWorld

@dataclass
class ItemDef:
    # Item info
    id: int
    type: ItemClassification
    # Info needed if the item is a car
    is_car: bool = False
    level: list[int] = field(default_factory=list)
    size: str = ""

ITEM_DEFS = {
    "Homer - Casual": ItemDef(121789, ItemClassification.filler),
    "Homer - Muumuu": ItemDef(121790, ItemClassification.filler),
    "Homer - Chosen One": ItemDef(121791, ItemClassification.filler),
    "Bart - Tall": ItemDef(121792, ItemClassification.filler),
    "Bart - Football": ItemDef(121793, ItemClassification.filler),
    "Bart - Ninja": ItemDef(121794, ItemClassification.filler),
    "Lisa - Cool": ItemDef(121795, ItemClassification.progression),
    "Lisa - Floreda": ItemDef(121796, ItemClassification.filler),
    "Lisa - Hockey": ItemDef(121797, ItemClassification.filler),
    "Marge - Classy": ItemDef(121798, ItemClassification.filler),
    "Marge - Inmate": ItemDef(121799, ItemClassification.progression),
    "Marge - Police": ItemDef(121800, ItemClassification.progression),
    "Apu - American": ItemDef(121801, ItemClassification.progression),
    "Apu - Army": ItemDef(121802, ItemClassification.filler),
    "Apu - B-sharps": ItemDef(121803, ItemClassification.filler),
    "Bart - Hugo": ItemDef(121804, ItemClassification.filler),
    "Bart - Cadet": ItemDef(121805, ItemClassification.filler),
    "Bart - Bartman": ItemDef(121806, ItemClassification.filler),
    "Homer - Dirty": ItemDef(121807, ItemClassification.filler),
    "Homer - Evil": ItemDef(121808, ItemClassification.filler),
    "Homer - Donut": ItemDef(121809, ItemClassification.filler),

    "Family Sedan": ItemDef(121810, ItemClassification.useful, True, [1], "Small"),
    "Plow King": ItemDef(121811, ItemClassification.progression, True, [1], "Large"),
    "Duff Truck": ItemDef(121812, ItemClassification.useful, True, [1], "Large"),
    "Surveillance Van": ItemDef(121813, ItemClassification.useful, True, [1], "Medium"),
    "Pickup Truck": ItemDef(121814, ItemClassification.useful, True, [1], "Medium"),
    "Electaurus": ItemDef(121815, ItemClassification.useful, True, [1], "Small"),

    "Mr. Plow": ItemDef(121816, ItemClassification.progression, True, [2], "Medium"),
    "Limo": ItemDef(121817, ItemClassification.useful, True, [2], "Small"),
    "Fire Truck": ItemDef(121818, ItemClassification.useful, True, [2], "Large"),
    "WWII Vehicle": ItemDef(121819, ItemClassification.useful, True, [2], "Medium"),
    "Moe's Sedan": ItemDef(121820, ItemClassification.useful, True, [2], "Small"),

    "School Bus": ItemDef(121821, ItemClassification.progression, True, [3], "Large"),
    "Donut Truck": ItemDef(121822, ItemClassification.useful, True, [3], "Medium"),
    "Nerd Car": ItemDef(121823, ItemClassification.useful, True, [3], "Small"),
    "Skinner's Sedan": ItemDef(121824, ItemClassification.useful, True, [3], "Medium"),
    "Book Burning Van": ItemDef(121825, ItemClassification.useful, True, [3], "Medium"),

    "Tractor": ItemDef(121826, ItemClassification.useful, True, [4], "Medium"),
    "Curator": ItemDef(121827, ItemClassification.useful, True, [4], "Small"),
    "Krusty's Limo": ItemDef(121828, ItemClassification.useful, True, [4], "Small"),
    "Kremlin": ItemDef(121829, ItemClassification.useful, True, [4], "Small"),
    "Clown Car": ItemDef(121830, ItemClassification.useful, True, [4], "Small"),

    "Car Built For Homer": ItemDef(121831, ItemClassification.progression, True, [5], "Small"),
    "Cola Truck": ItemDef(121832, ItemClassification.useful, True, [5], "Large"),
    "Police Car": ItemDef(121833, ItemClassification.useful, True, [5], "Small"),
    "Hover Car": ItemDef(121834, ItemClassification.useful, True, [5], "Small"),
    "El Carro Loco": ItemDef(121835, ItemClassification.useful, True, [5], "Small"),

    "Globex Super Villain Car": ItemDef(121836, ItemClassification.progression, True, [6], "Small"),
    "Armored Truck": ItemDef(121837, ItemClassification.useful, True, [6], "Large"),
    "Chase Sedan": ItemDef(121838, ItemClassification.useful, True, [6], "Small"),
    "Bandit": ItemDef(121839, ItemClassification.useful, True, [6], "Small"),
    "36 Stutz Bearcat": ItemDef(121840, ItemClassification.useful, True, [6], "Small"),

    "Zombie Car": ItemDef(121841, ItemClassification.progression, True, [7], "Small"),
    "Hearse": ItemDef(121842, ItemClassification.useful, True, [7], "Small"),
    "Mr. Burns' Limo": ItemDef(121843, ItemClassification.useful, True, [7], "Medium"),
    "Hover Bike": ItemDef(121844, ItemClassification.useful, True, [7], "Small"),
    "Open Wheel Race Car": ItemDef(121845, ItemClassification.useful, True, [7], "Small"),

    "Honor Roller": ItemDef(121846, ItemClassification.useful, True, [2], "Small"),
    "Malibu Stacy Car": ItemDef(121847, ItemClassification.useful, True, [3], "Small"),
    "Canyonero": ItemDef(121848, ItemClassification.useful, True, [4], "Medium"),
    "Longhorn": ItemDef(121849, ItemClassification.useful, True, [5], "Small"),
    "Ferrini - Red": ItemDef(121850, ItemClassification.useful, True, [6], "Small"),
    "70's Sports Car": ItemDef(121851, ItemClassification.useful, True, [7], "Small"),

    "Launch": ItemDef(121852, ItemClassification.trap),
    "Level 1": ItemDef(121853, ItemClassification.progression),
    "Level 2": ItemDef(121854, ItemClassification.progression),
    "Level 3": ItemDef(121855, ItemClassification.progression),
    "Level 4": ItemDef(121856, ItemClassification.progression),
    "Level 5": ItemDef(121857, ItemClassification.progression),
    "Level 6": ItemDef(121858, ItemClassification.progression),
    "Level 7": ItemDef(121859, ItemClassification.progression),

    "Homer Attack": ItemDef(121860, ItemClassification.progression),
    "Bart Attack": ItemDef(121861, ItemClassification.progression),
    "Lisa Attack": ItemDef(121862, ItemClassification.progression),
    "Marge Attack": ItemDef(121863, ItemClassification.progression),
    "Apu Attack": ItemDef(121864, ItemClassification.progression),

    "Homer Progressive Jump": ItemDef(121865, ItemClassification.progression),
    "Bart Progressive Jump": ItemDef(121866, ItemClassification.progression),
    "Lisa Progressive Jump": ItemDef(121867, ItemClassification.progression),
    "Marge Progressive Jump": ItemDef(121868, ItemClassification.progression),
    "Apu Progressive Jump": ItemDef(121869, ItemClassification.progression),

    "Homer E-Brake": ItemDef(121870, ItemClassification.progression),
    "Bart E-Brake": ItemDef(121871, ItemClassification.progression),
    "Lisa E-Brake": ItemDef(121872, ItemClassification.progression),
    "Marge E-Brake": ItemDef(121873, ItemClassification.progression),
    "Apu E-Brake": ItemDef(121874, ItemClassification.progression),

    "Wrench": ItemDef(121875, ItemClassification.filler),
    "Hit N Run Reset": ItemDef(121876, ItemClassification.filler),
    "10 Coins": ItemDef(121877, ItemClassification.filler),
    "Hit N Run": ItemDef(121878, ItemClassification.trap),
    "Duff Trap": ItemDef(121879, ItemClassification.trap),

    "Speed Rocket": ItemDef(121880, ItemClassification.useful, True, [1], "Small"),
    "Monorail Car": ItemDef(121881, ItemClassification.useful, True, [2], "Medium"),
    "Knight Boat": ItemDef(121882, ItemClassification.useful, True, [3], "Small"),
    "ATV": ItemDef(121883, ItemClassification.useful, True, [4], "Small"),
    "Obliteratatron Big Wheel Truck": ItemDef(121884, ItemClassification.useful, True, [5], "Extra Large"),
    "Planet Hype 50's Car": ItemDef(121885, ItemClassification.useful, True, [6], "Small"),
    "R/C Buggy": ItemDef(121886, ItemClassification.useful, True, [7], "Extra Small"),

    "Progressive Wallet Upgrade": ItemDef(121887, ItemClassification.progression),
    "Progressive Level": ItemDef(121888, ItemClassification.progression),

    "Eject": ItemDef(121889, ItemClassification.trap),

    "Homer Checkered Flag": ItemDef(121890, ItemClassification.progression),
    "Bart Checkered Flag": ItemDef(121891, ItemClassification.progression),
    "Lisa Checkered Flag": ItemDef(121892, ItemClassification.progression),
    "Marge Checkered Flag": ItemDef(121893, ItemClassification.progression),
    "Apu Checkered Flag": ItemDef(121894, ItemClassification.progression),

    "Homer Gagfinder": ItemDef(121895, ItemClassification.progression),
    "Bart Gagfinder": ItemDef(121896, ItemClassification.progression),
    "Lisa Gagfinder": ItemDef(121897, ItemClassification.progression),
    "Marge Gagfinder": ItemDef(121898, ItemClassification.progression),
    "Apu Gagfinder": ItemDef(121899, ItemClassification.progression),

    "Mini School Bus": ItemDef(121900, ItemClassification.filler, True, [1], "Large"),
    "Glass Truck": ItemDef(121901, ItemClassification.filler, True, [1], "Medium"),
    "Minivan": ItemDef(121902, ItemClassification.filler, True, [1], "Medium"),
    "Pizza Van": ItemDef(121903, ItemClassification.filler, True, [2], "Medium"),
    "Taxi": ItemDef(121904, ItemClassification.filler, True, [2], "Small"),
    "Sedan B": ItemDef(121905, ItemClassification.filler, True, [2], "Small"),
    "Fish Van": ItemDef(121906, ItemClassification.filler, True, [3], "Medium"),
    "Garbage Truck": ItemDef(121907, ItemClassification.filler, True, [4], "Large"),
    "Nuclear Waste Truck": ItemDef(121908, ItemClassification.filler, True, [4], "Medium"),
    "Pickup": ItemDef(121909, ItemClassification.filler, True, [1, 3, 6], "Medium"),
    "Sports Car A": ItemDef(121910, ItemClassification.filler, True, [3], "Small"),
    "Compact Car": ItemDef(121911, ItemClassification.filler, True, [3, 4, 6], "Small"),
    "SUV": ItemDef(121912, ItemClassification.filler, True, [4, 5], "Small"),
    "Hallo Hearse": ItemDef(121913, ItemClassification.filler, True, [7], "Small"),
    "Coffin Car": ItemDef(121914, ItemClassification.filler, True, [7], "Small"),
    "Ghost Ship": ItemDef(121915, ItemClassification.filler, True, [7], "Small"),
    "Witch Broom": ItemDef(121916, ItemClassification.filler, True, [7], "Small"),
    "Sedan A": ItemDef(121917, ItemClassification.filler, True, [8], "Small"),
    "Station Wagon": ItemDef(121918, ItemClassification.filler, True, [8], "Small"),
    "Ice Cream Truck": ItemDef(121919, ItemClassification.filler, True, [8], "Large"),
    "Bonestorm Truck": ItemDef(121920, ItemClassification.filler, True, [8], "Large"),
    "Cell Phone Car": ItemDef(121921, ItemClassification.filler, True, [8], "Small"),
    "Milk Truck": ItemDef(121922, ItemClassification.filler, True, [8], "Large"),
    "Nonuplets Minivan": ItemDef(121923, ItemClassification.filler, True, [8], "Medium"),
    "Ferrini - Black": ItemDef(121924, ItemClassification.filler, True, [8], "Small"),

    "Homer Frink-o-Matic Wasp Bumper": ItemDef(121925, ItemClassification.progression),
    "Bart Frink-o-Matic Wasp Bumper": ItemDef(121926, ItemClassification.progression),
    "Lisa Frink-o-Matic Wasp Bumper": ItemDef(121927, ItemClassification.progression),
    "Marge Frink-o-Matic Wasp Bumper": ItemDef(121928, ItemClassification.progression),
    "Apu Frink-o-Matic Wasp Bumper": ItemDef(121929, ItemClassification.progression),

    "Traffic Trap": ItemDef(121930, ItemClassification.trap),
    "Cube Van": ItemDef(121931, ItemClassification.filler, True, [8], "Large"),
    "WWII Vehicle W\ Rocket": ItemDef(121932, ItemClassification.useful),
    "Audi TT": ItemDef(121933, ItemClassification.useful, True, [8], "Small"),
    "Vote Quimby Truck": ItemDef(121934, ItemClassification.useful, True, [5], "Large"),
    "Ambulance": ItemDef(121935, ItemClassification.useful, True, [5], "Large"),
    "Sports Car B": ItemDef(121936, ItemClassification.useful, True, [2, 5], "Small"),
    "Itchy and Scratchy Movie Truck": ItemDef(121937, ItemClassification.progression, True, [6], "Large"),
    "Burns Armored Truck": ItemDef(121938, ItemClassification.progression, True, [6], "Large"),

    "Homer Forward": ItemDef(121939, ItemClassification.progression),
    "Bart Forward": ItemDef(121940, ItemClassification.progression),
    "Lisa Forward": ItemDef(121941, ItemClassification.progression),
    "Marge Forward": ItemDef(121942, ItemClassification.progression),
    "Apu Forward": ItemDef(121943, ItemClassification.progression),
}


ITEM_NAME_TO_ID = {name: item.id for name, item in ITEM_DEFS.items()}
DEFAULT_ITEM_CLASSIFICATIONS = {name: item.type for name, item in ITEM_DEFS.items()}
prog_cars = []

class SimpsonsHitNRunItem(Item):
    game = "Simpsons Hit and Run"

def get_random_filler_item_name(world: SimpsonsHitNRunWorld) -> str:
    trap_items = [name for name, item in ITEM_DEFS.items() if item.type == ItemClassification.trap]
    filler_items = ["Wrench", "Hit N Run Reset", "10 Coins"]
    if world.random.randint(0, 99) < world.options.filler_traps:
        return world.random.choice(trap_items)
    else:
        return world.random.choice(filler_items)

def create_item_with_correct_classification(world: SimpsonsHitNRunWorld, name: str, make_prog: bool = False) -> SimpsonsHitNRunItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    if make_prog:
        classification = ItemClassification.progression

    return SimpsonsHitNRunItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: SimpsonsHitNRunWorld) -> None:
    characters = {"Homer", "Bart", "Lisa", "Marge", "Apu"}

    def get_character(name: str) -> str | None:
        first_word = name.split()[0]
        return first_word if first_word in characters else None

    for i in range(1, 8):
        cars = [name for name, item in ITEM_DEFS.items() if item.is_car and (i in item.level or 8 in item.level)]
        prog_cars.append(world.random.choice(cars))

    for size in ("Small", "Medium", "Large"):
        cars = [name for name, item in ITEM_DEFS.items() if item.is_car and item.size == size]
        prog_cars.append(world.random.choice(cars))

    # Missionlocks
    num_locks = int(49 * (world.options.missionlocks / 100))
    pattern = re.compile(r'^\(L([1-7])M([1-7])\)\s+.+')
    mission_locked = world.random.sample([loc.name for loc in world.get_locations() if pattern.match(loc.name)], num_locks)
    chosen_cars = world.random.sample(rules.any_car, num_locks)

    for mission, car in zip(mission_locked, chosen_cars):
        rules.missionlockdict[mission] = car
        prog_cars.append(car)

    itempool: list[Item] = []

    keyword_to_option = {
        "Jump": "shufflejump",
        "Attack": "shuffleattack",
        "Gagfinder": "shufflegagfinder",
        "Flag": "shufflecheckeredflags",
        "Brake": "shuffleebrake",
        "Forward": "shuffleforward",
        "Bumper": "shufflebumpers"
    }

    # add items to itempool, make sure there's at least one car for each level and of each size marked prog, only add moves if they're shuffled
    for name, item_def in ITEM_DEFS.items():
        if name in prog_cars:
            itempool.append(world.create_item(name, True))
        else:
            char = get_character(name)
            skip = False

            for keyword, option_attr in keyword_to_option.items():
                if keyword in name:
                    option_value = getattr(world.options, option_attr)
                    if "None" in option_value or (char is not None and char not in option_value and "All" not in option_value):
                        skip = True
                        world.push_precollected(world.create_item(name))
                        if "Jump" in name:
                            world.push_precollected(world.create_item(name))
                    break

            if "Level" in name:
                if ("Progressive" in name) == world.options.shufflelevels:
                    skip = True

            if skip:
                continue

            if "Progressive" in name:
                # 2 jumps, so create 1 more
                if "Jump" in name:
                    itempool.append(world.create_item(name))

                # 6 wallets, so create 5 more
                # 6 level items, so create 5 more
                elif "Wallet" in name or "Level" in name:
                    for i in range(5):
                        itempool.append(world.create_item(name))


            itempool.append(world.create_item(name))

    start_items = []

    if world.options.shufflelevels:
        start_level = world.random.randint(1,7)
        world.push_precollected(world.create_item(f"Level {start_level}"))
        start_items.append(f"Level {start_level}")
    else:
        start_level = 1
        world.push_precollected(world.create_item("Progressive Level"))
        # don't put in start items because we only made enough earlier counting this one

    if world.options.startingcarshuffle:
        cars = [name for name, item in ITEM_DEFS.items() if item.is_car and (start_level in item.level or 8 in item.level)]
        start_car = world.create_item(world.random.choice(cars))
        world.push_precollected(start_car)
        start_items.append(start_car.name)
    else:
        start_cars = ["Family Sedan", "Honor Roller", "Malibu Stacy Car", "Canyonero", "Longhorn", "Ferrini - Red", "70's Sports Car"]
        start_car = world.create_item(start_cars[start_level - 1])
        world.push_precollected(start_car)
        start_items.append(start_car.name)

    itempool = [item for item in itempool if item.name not in start_items]

    num_items = len(itempool)

    num_unfilled_locs = len(world.multiworld.get_unfilled_locations(world.player))

    needed_filler = num_unfilled_locs - num_items
    itempool += [world.create_filler() for _ in range(needed_filler)]

    world.multiworld.itempool += itempool

