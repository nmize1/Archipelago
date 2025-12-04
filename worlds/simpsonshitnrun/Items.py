from BaseClasses import Item
from .Data import item_table
from .hooks.Items import before_item_table_processed

item_table = before_item_table_processed(item_table)

######################
# Generate item lookups
######################

item_id_to_name: dict[int, str] = {}
item_name_to_item: dict[str, dict] = {}
item_name_groups: dict[str, str] = {}
advancement_item_names: set[str] = set()
lastItemId = -1

# Replaced manual code with hardcoded ids which are preferable for editing later.
# Need to clean up the rest of the manual stuff that isn't needed anymore.
# id starts at Simpsons' first air date
item_table = [
    {
        "count": 1,
        "name": "Homer - Casual",
        "category": ["Filler"],
        "useful": True,
        "id": 121789,
        "progression": False
    },
    {
        "count": 1,
        "name": "Homer - Muumuu",
        "category": ["Filler"],
        "useful": True,
        "id": 121790,
        "progression": False
    },
    {
        "count": 1,
        "name": "Homer - Chosen One",
        "category": ["Filler"],
        "useful": True,
        "id": 121791,
        "progression": False
    },
    {
        "count": 1,
        "name": "Bart - Tall",
        "category": ["Filler"],
        "useful": True,
        "id": 121792,
        "progression": False
    },
    {
        "count": 1,
        "name": "Bart - Football",
        "category": ["Filler"],
        "useful": True,
        "id": 121793,
        "progression": False
    },
    {
        "count": 1,
        "name": "Bart - Ninja",
        "category": ["Filler"],
        "useful": True,
        "id": 121794,
        "progression": False
    },
    {
        "count": 1,
        "name": "Lisa - Cool",
        "category": ["Progression"],
        "progression": True,
        "id": 121795
    },
    {
        "count": 1,
        "name": "Lisa - Floreda",
        "category": ["Filler"],
        "useful": True,
        "id": 121796,
        "progression": False
    },
    {
        "count": 1,
        "name": "Lisa - Hockey",
        "category": ["Filler"],
        "useful": True,
        "id": 121797,
        "progression": False
    },
    {
        "count": 1,
        "name": "Marge - Classy",
        "category": ["Filler"],
        "useful": True,
        "id": 121798,
        "progression": False
    },
    {
        "count": 1,
        "name": "Marge - Inmate",
        "category": ["Progression"],
        "progression": True,
        "id": 121799
    },
    {
        "count": 1,
        "name": "Marge - Police",
        "category": ["Progression"],
        "progression": True,
        "id": 121800
    },
    {
        "count": 1,
        "name": "Apu - American",
        "category": ["Progression"],
        "progression": True,
        "id": 121801
    },
    {
        "count": 1,
        "name": "Apu - Army",
        "category": ["Filler"],
        "useful": True,
        "id": 121802,
        "progression": False
    },
    {
        "count": 1,
        "name": "Apu - B-sharps",
        "category": ["Filler"],
        "useful": True,
        "id": 121803,
        "progression": False
    },
    {
        "count": 1,
        "name": "Bart - Hugo",
        "category": ["Filler"],
        "useful": True,
        "id": 121804,
        "progression": False
    },
    {
        "count": 1,
        "name": "Bart - Cadet",
        "category": ["Filler"],
        "useful": True,
        "id": 121805,
        "progression": False
    },
    {
        "count": 1,
        "name": "Bart - Bartman",
        "category": ["Filler"],
        "useful": True,
        "id": 121806,
        "progression": False
    },
    {
        "count": 1,
        "name": "Homer - Dirty",
        "category": ["Filler"],
        "useful": True,
        "id": 121807,
        "progression": False
    },
    {
        "count": 1,
        "name": "Homer - Evil",
        "category": ["Filler"],
        "useful": True,
        "id": 121808,
        "progression": False
    },
    {
        "count": 1,
        "name": "Homer - Donut",
        "category": ["Filler"],
        "useful": True,
        "id": 121809,
        "progression": False
    },
    {
        "count": 1,
        "name": "Family Sedan",
        "category": ["Level 1 Cars", "Cars", "Small Cars"],
        "progression": False,
        "useful": True,
        "id": 121810
    },
    {
        "count": 1,
        "name": "Plow King",
        "category": ["Progression", "Level 1 Cars", "Cars", "Large Cars"],
        "progression": True,
        "id": 121811
    },
    {
        "count": 1,
        "name": "Duff Truck",
        "category": ["Cars", "Level 1 Cars", "Large Cars"],
        "useful": True,
        "id": 121812,
        "progression": False
    },
    {
        "count": 1,
        "name": "Surveillance Van",
        "category": ["Cars", "Level 1 Cars", "Medium Cars"],
        "useful": True,
        "id": 121813,
        "progression": False
    },
    {
        "count": 1,
        "name": "Pickup Truck",
        "category": ["Cars", "Level 1 Cars", "Medium Cars"],
        "useful": True,
        "id": 121814,
        "progression": False
    },
    {
        "count": 1,
        "name": "Electaurus",
        "category": ["Cars", "Level 1 Cars", "Small Cars"],
        "useful": True,
        "id": 121815,
        "progression": False
    },
    {
        "count": 1,
        "name": "Mr. Plow",
        "category": ["Progression", "Level 2 Cars", "Cars", "Medium Cars"],
        "progression": True,
        "id": 121816
    },
    {
        "count": 1,
        "name": "Limo",
        "category": ["Cars", "Level 2 Cars", "Small Cars"],
        "useful": True,
        "id": 121817,
        "progression": False
    },
    {
        "count": 1,
        "name": "Fire Truck",
        "category": ["Cars", "Level 2 Cars", "Large Cars"],
        "useful": True,
        "id": 121818,
        "progression": False
    },
    {
        "count": 1,
        "name": "WWII Vehicle",
        "category": ["Cars", "Level 2 Cars", "Medium Cars"],
        "useful": True,
        "id": 121819,
        "progression": False
    },
    {
        "count": 1,
        "name": "Moe's Sedan",
        "category": ["Cars", "Level 2 Cars", "Small Cars"],
        "useful": True,
        "id": 121820,
        "progression": False
    },
    {
        "count": 1,
        "name": "School Bus",
        "category": ["Progression", "Level 3 Cars", "Large Cars"],
        "progression": True,
        "id": 121821
    },
    {
        "count": 1,
        "name": "Donut Truck",
        "category": ["Cars", "Level 3 Cars", "Medium Cars"],
        "useful": True,
        "id": 121822,
        "progression": False
    },
    {
        "count": 1,
        "name": "Nerd Car",
        "category": ["Cars", "Level 3 Cars", "Small Cars"],
        "useful": True,
        "id": 121823,
        "progression": False
    },
    {
        "count": 1,
        "name": "Skinner's Sedan",
        "category": ["Cars", "Level 3 Cars", "Medium Cars"],
        "useful": True,
        "id": 121824,
        "progression": False
    },
    {
        "count": 1,
        "name": "Book Burning Van",
        "category": ["Cars", "Level 3 Cars", "Medium Cars"],
        "useful": True,
        "id": 121825,
        "progression": False
    },
    {
        "count": 1,
        "name": "Tractor",
        "category": ["Cars", "Level 4 Cars", "Medium Cars"],
        "useful": True,
        "id": 121826,
        "progression": False
    },
    {
        "count": 1,
        "name": "Curator",
        "category": ["Cars", "Level 4 Cars", "Small Cars"],
        "useful": True,
        "id": 121827,
        "progression": False
    },
    {
        "count": 1,
        "name": "Krusty's Limo",
        "category": ["Cars", "Level 4 Cars", "Small Cars"],
        "useful": True,
        "id": 121828,
        "progression": False
    },
    {
        "count": 1,
        "name": "Kremlin",
        "category": ["Cars", "Level 4 Cars", "Small Cars"],
        "useful": True,
        "id": 121829,
        "progression": False
    },
    {
        "count": 1,
        "name": "Clown Car",
        "category": ["Cars", "Level 4 Cars", "Small Cars"],
        "useful": True,
        "id": 121830,
        "progression": False
    },
    {
        "count": 1,
        "name": "Car Built For Homer",
        "category": ["Progression", "Level 5 Cars", "Small Cars"],
        "progression": True,
        "id": 121831
    },
    {
        "count": 1,
        "name": "Cola Truck",
        "category": ["Cars", "Level 5 Cars", "Large Cars"],
        "useful": True,
        "id": 121832,
        "progression": False
    },
    {
        "count": 1,
        "name": "Police Car",
        "category": ["Cars", "Level 5 Cars", "Small Cars"],
        "useful": True,
        "id": 121833,
        "progression": False
    },
    {
        "count": 1,
        "name": "Hover Car",
        "category": ["Cars", "Level 5 Cars", "Small Cars"],
        "useful": True,
        "id": 121834,
        "progression": False
    },
    {
        "count": 1,
        "name": "El Carro Loco",
        "category": ["Cars", "Level 5 Cars", "Small Cars"],
        "useful": True,
        "id": 121835,
        "progression": False
    },
    {
        "count": 1,
        "name": "Globex Super Villain Car",
        "category": ["Progression", "Level 6 Cars", "Cars", "Small Cars"],
        "progression": True,
        "id": 121836
    },
    {
        "count": 1,
        "name": "Armored Truck",
        "category": ["Cars", "Level 6 Cars", "Large Cars"],
        "useful": True,
        "id": 121837,
        "progression": False
    },
    {
        "count": 1,
        "name": "Chase Sedan",
        "category": ["Cars", "Level 6 Cars", "Small Cars"],
        "useful": True,
        "id": 121838,
        "progression": False
    },
    {
        "count": 1,
        "name": "Bandit",
        "category": ["Cars", "Level 6 Cars", "Small Cars"],
        "useful": True,
        "id": 121839,
        "progression": False
    },
    {
        "count": 1,
        "name": "36 Stutz Bearcat",
        "category": ["Cars", "Level 6 Cars", "Small Cars"],
        "useful": True,
        "id": 121840,
        "progression": False
    },
    {
        "count": 1,
        "name": "Zombie Car",
        "category": ["Progression", "Level 7 Cars", "Cars", "Small Cars"],
        "progression": True,
        "id": 121841
    },
    {
        "count": 1,
        "name": "Hearse",
        "category": ["Cars", "Level 7 Cars", "Small Cars"],
        "useful": True,
        "id": 121842,
        "progression": False
    },
    {
        "count": 1,
        "name": "Mr. Burns' Limo",
        "category": ["Cars", "Level 7 Cars", "Medium Cars"],
        "useful": True,
        "id": 121843,
        "progression": False
    },
    {
        "count": 1,
        "name": "Hover Bike",
        "category": ["Cars", "Level 7 Cars", "Small Cars"],
        "useful": True,
        "id": 121844,
        "progression": False
    },
    {
        "count": 1,
        "name": "Open Wheel Race Car",
        "category": ["Cars", "Level 7 Cars", "Small Cars"],
        "useful": True,
        "id": 121845,
        "progression": False
    },
    {
        "count": 1,
        "name": "Honor Roller",
        "category": ["Cars", "Level 2 Cars", "Small Cars"],
        "progression": False,
        "useful": True,
        "id": 121846
    },
    {
        "count": 1,
        "name": "Malibu Stacy Car",
        "category": ["Cars", "Level 3 Cars", "Small Cars"],
        "progression": False,
        "useful": True,
        "id": 121847
    },
    {
        "count": 1,
        "name": "Canyonero",
        "category": ["Cars", "Level 4 Cars", "Medium Cars"],
        "progression": False,
        "useful": True,
        "id": 121848
    },
    {
        "count": 1,
        "name": "Longhorn",
        "category": ["Cars", "Level 5 Cars", "Small Cars"],
        "progression": False,
        "useful": True,
        "id": 121849
    },
    {
        "count": 1,
        "name": "Ferrini - Red",
        "category": ["Cars", "Level 6 Cars", "Small Cars"],
        "progression": False,
        "useful": True,
        "id": 121850
    },
    {
        "count": 1,
        "name": "70's Sports Car",
        "category": ["Cars", "Level 7 Cars", "Small Cars"],
        "progression": False,
        "useful": True,
        "id": 121851
    },
    {
        "count": 20,
        "name": "Launch",
        "category": ["Filler"],
        "trap": True,
        "id": 121852,
        "progression": False
    },
    {
        "count": 1,
        "name": "Level 1",
        "category": ["Level"],
        "progression": True,
        "id": 121853
    },
    {
        "count": 1,
        "name": "Level 2",
        "category": ["Level"],
        "progression": True,
        "id": 121854
    },
    {
        "count": 1,
        "name": "Level 3",
        "category": ["Level"],
        "progression": True,
        "id": 121855
    },
    {
        "count": 1,
        "name": "Level 4",
        "category": ["Level"],
        "progression": True,
        "id": 121856
    },
    {
        "count": 1,
        "name": "Level 5",
        "category": ["Level"],
        "progression": True,
        "id": 121857
    },
    {
        "count": 1,
        "name": "Level 6",
        "category": ["Level"],
        "progression": True,
        "id": 121858
    },
    {
        "count": 1,
        "name": "Level 7",
        "category": ["Level"],
        "progression": True,
        "id": 121859
    },
    {
        "count": 1,
        "name": "Homer Attack",
        "category": ["Moves"],
        "progression": True,
        "id": 121860
    },
    {
        "count": 1,
        "name": "Bart Attack",
        "category": ["Moves"],
        "progression": True,
        "id": 121861
    },
    {
        "count": 1,
        "name": "Lisa Attack",
        "category": ["Moves"],
        "progression": True,
        "id": 121862
    },
    {
        "count": 1,
        "name": "Marge Attack",
        "category": ["Moves"],
        "progression": True,
        "id": 121863
    },
    {
        "count": 1,
        "name": "Apu Attack",
        "category": ["Moves"],
        "progression": True,
        "id": 121864
    },
    {
        "count": 2,
        "name": "Homer Progressive Jump",
        "category": ["Moves"],
        "progression": True,
        "id": 121865
    },
    {
        "count": 2,
        "name": "Bart Progressive Jump",
        "category": ["Moves"],
        "progression": True,
        "id": 121866
    },
    {
        "count": 2,
        "name": "Lisa Progressive Jump",
        "category": ["Moves"],
        "progression": True,
        "id": 121867
    },
    {
        "count": 2,
        "name": "Marge Progressive Jump",
        "category": ["Moves"],
        "progression": True,
        "id": 121868
    },
    {
        "count": 2,
        "name": "Apu Progressive Jump",
        "category": ["Moves"],
        "progression": True,
        "id": 121869
    },
    {
        "count": 1,
        "name": "Homer E-Brake",
        "category": ["Moves"],
        "progression": True,
        "id": 121870
    },
    {
        "count": 1,
        "name": "Bart E-Brake",
        "category": ["Moves"],
        "progression": True,
        "id": 121871
    },
    {
        "count": 1,
        "name": "Lisa E-Brake",
        "category": ["Moves"],
        "progression": True,
        "id": 121872
    },
    {
        "count": 1,
        "name": "Marge E-Brake",
        "category": ["Moves"],
        "progression": True,
        "id": 121873
    },
    {
        "count": 1,
        "name": "Apu E-Brake",
        "category": ["Moves"],
        "progression": True,
        "id": 121874
    },
    {
        "count": 1,
        "name": "Homer Checkered Flag",
        "category": ["Races"],
        "progression": True,
        "id": 121890
    },
    {
        "count": 1,
        "name": "Bart Checkered Flag",
        "category": ["Races"],
        "progression": True,
        "id": 121891
    },
    {
        "count": 1,
        "name": "Lisa Checkered Flag",
        "category": ["Races"],
        "progression": True,
        "id": 121892
    },
    {
        "count": 1,
        "name": "Marge Checkered Flag",
        "category": ["Races"],
        "progression": True,
        "id": 121893
    },
    {
        "count": 1,
        "name": "Apu Checkered Flag",
        "category": ["Races"],
        "progression": True,
        "id": 121894
    },
    {
        "count": 1,
        "name": "Homer Gagfinder",
        "category": ["Gags"],
        "progression": True,
        "id": 121895
    },
    {
        "count": 1,
        "name": "Bart Gagfinder",
        "category": ["Gags"],
        "progression": True,
        "id": 121896
    },
    {
        "count": 1,
        "name": "Lisa Gagfinder",
        "category": ["Gags"],
        "progression": True,
        "id": 121897
    },
    {
        "count": 1,
        "name": "Marge Gagfinder",
        "category": ["Gags"],
        "progression": True,
        "id": 121898
    },
    {
        "count": 1,
        "name": "Apu Gagfinder",
        "category": ["Gags"],
        "progression": True,
        "id": 121899
    },
    {
        "count": 50,
        "name": "Wrench",
        "category": ["Filler"],
        "filler": True,
        "id": 121875,
        "progression": False
    },
    {
        "count": 40,
        "name": "Hit N Run Reset",
        "category": ["Filler"],
        "id": 121876,
        "progression": False
    },
    {
        "count": 30,
        "name": "10 Coins",
        "category": ["Filler"],
        "id": 121877,
        "progression": False
    },
    {
        "count": 20,
        "name": "Hit N Run",
        "category": ["Filler"],
        "trap": True,
        "id": 121878,
        "progression": False
    },
    {
        "count": 20,
        "name": "Duff Trap",
        "category": ["Filler"],
        "trap": True,
        "id": 121879,
        "progression": False
    },
    {
        "count": 20,
        "name": "Eject",
        "category": ["Filler"],
        "trap": True,
        "id": 121889,
        "progression": False
    },
    {
        "count": 1,
        "name": "Speed Rocket",
        "category": ["Cars", "Level 1 Cars", "Small Cars"],
        "useful": True,
        "id": 121880,
        "progression": False
    },
    {
        "count": 1,
        "name": "Monorail Car",
        "category": ["Cars", "Level 2 Cars", "Medium Cars"],
        "useful": True,
        "id": 121881,
        "progression": False
    },
    {
        "count": 1,
        "name": "Knight Boat",
        "category": ["Cars", "Level 3 Cars", "Small Cars"],
        "useful": True,
        "id": 121882,
        "progression": False
    },
    {
        "count": 1,
        "name": "ATV",
        "category": ["Cars", "Level 4 Cars", "Small Cars"],
        "useful": True,
        "id": 121883,
        "progression": False
    },
    {
        "count": 1,
        "name": "Obliteratatron Big Wheel Truck",
        "category": ["Cars", "Level 5 Cars", "Extra Large Cars"],
        "useful": True,
        "id": 121884,
        "progression": False
    },
    {
        "count": 1,
        "name": "Planet Hype 50's Car",
        "category": ["Cars", "Level 6 Cars", "Small Cars"],
        "useful": True,
        "id": 121885,
        "progression": False
    },
    {
        "count": 1,
        "name": "R/C Buggy",
        "category": ["Cars", "Level 1 Cars", "Extra Small Cars"],
        "useful": True,
        "id": 121886,
        "progression": False
    },
    {
        "count": 6,
        "name": "Progressive Wallet Upgrade",
        "category": ["Progression"],
        "id": 121887,
        "progression": True
    },
    {
        "count": 6,
        "name": "Progressive Level",
        "category": ["Progression"],
        "id": 121888,
        "progression": True
    },
    {
        "count": 1,
        "name": "Mini School Bus",
        "category": ["Cars", "Traffic", "Filler", "Level 1 Cars", "Large Cars"],
        "id": 121900,
        "progression": False
    },
    {
        "count": 1,
        "name": "Glass Truck",
        "category": ["Cars", "Traffic", "Filler", "Level 1 Cars", "Medium Cars"],
        "id": 121901,
        "progression": False
    },
    {
        "count": 1,
        "name": "Minivan",
        "category": ["Cars", "Traffic", "Filler", "Level 1 Cars", "Medium Cars"],
        "id": 121902,
        "progression": False
    },
    {
        "count": 1,
        "name": "Pizza Van",
        "category": ["Cars", "Traffic", "Filler", "Level 2 Cars", "Medium Cars"],
        "id": 121903,
        "progression": False
    },
    {
        "count": 1,
        "name": "Taxi",
        "category": ["Cars", "Traffic", "Filler", "Level 2 Cars", "Small Cars"],
        "id": 121904,
        "progression": False
    },
    {
        "count": 1,
        "name": "Sedan B",
        "category": ["Cars", "Traffic", "Filler", "Level 2 Cars", "Small Cars"],
        "id": 121905,
        "progression": False
    },
    {
        "count": 1,
        "name": "Fish Van",
        "category": ["Cars", "Traffic", "Filler", "Level 3 Cars", "Medium Cars"],
        "id": 121906,
        "progression": False
    },
    {
        "count": 1,
        "name": "Garbage Truck",
        "category": ["Cars", "Traffic", "Filler", "Level 4 Cars", "Large Cars"],
        "id": 121907,
        "progression": False
    },
    {
        "count": 1,
        "name": "Nuclear Waste Truck",
        "category": ["Cars", "Traffic", "Filler", "Level 4 Cars", "Medium Cars"],
        "id": 121908,
        "progression": False
    },
    {
        "count": 1,
        "name": "Vote Quimby Truck",
        "category": ["Cars", "Traffic", "Filler", "Level 5 Cars", "Large Cars"],
        "id": 121934,
        "progression": False
    },
    {
        "count": 1,
        "name": "Ambulance",
        "category": ["Cars", "Traffic", "Filler", "Level 5 Cars", "Large Cars"],
        "id": 121935,
        "progression": False
    },
    {
        "count": 1,
        "name": "Sports Car B",
        "category": ["Cars", "Traffic", "Filler", "Level 2 Cars", "Level 5 Cars", "Small Cars"],
        "id": 121936,
        "progression": False
    },
    {
        "count": 1,
        "name": "Itchy and Scratchy Movie Truck",
        "category": ["Cars", "Traffic", "Filler", "Level 6 Cars", "Large Cars"],
        "id": 121937,
        "progression": False
    },
    {
        "count": 1,
        "name": "Burns Armored Truck",
        "category": ["Cars", "Traffic", "Filler", "Level 6 Cars", "Large Cars"],
        "id": 121938,
        "progression": False
    },
    {
        "count": 1,
        "name": "Pickup",
        "category": ["Cars", "Traffic", "Filler", "Level 1 Cars", "Level 3 Cars", "Level 6 Cars", "Medium Cars"],
        "id": 121909,
        "progression": False
    },
    {
        "count": 1,
        "name": "Sports Car A",
        "category": ["Cars", "Traffic", "Filler", "Level 3 Cars", "Small Cars"],
        "id": 121910,
        "progression": False
    },
    {
        "count": 1,
        "name": "Compact Car",
        "category": ["Cars", "Traffic", "Filler", "Level 3 Cars", "Level 4 Cars", "Level 6 Cars", "Small Cars"],
        "id": 121911,
        "progression": False
    },
    {
        "count": 1,
        "name": "SUV",
        "category": ["Cars", "Traffic", "Filler", "Level 4 Cars", "Level 5 Cars", "Small Cars"],
        "id": 121912,
        "progression": False
    },
    {
        "count": 1,
        "name": "Hallo Hearse",
        "category": ["Cars", "Traffic", "Filler", "Level 7 Cars", "Small Cars"],
        "id": 121913,
        "progression": False
    },
    {
        "count": 1,
        "name": "Coffin Car",
        "category": ["Cars", "Traffic", "Filler", "Level 7 Cars", "Small Cars"],
        "id": 121914,
        "progression": False
    },
    {
        "count": 1,
        "name": "Ghost Ship",
        "category": ["Cars", "Traffic", "Filler", "Level 7 Cars", "Small Cars"],
        "id": 121915,
        "progression": False
    },
    {
        "count": 1,
        "name": "Witch's Broom",
        "category": ["Cars", "Traffic", "Filler", "Level 7 Cars", "Small Cars"],
        "id": 121916,
        "progression": False
    },
    {
        "count": 1,
        "name": "Sedan A",
        "category": ["Cars", "Traffic", "Filler", "Level Any Cars", "Small Cars"],
        "id": 121917,
        "progression": False
    },
    {
        "count": 1,
        "name": "Station Wagon",
        "category": ["Cars", "Traffic", "Filler", "Level Any Cars", "Small Cars"],
        "id": 121918,
        "progression": False
    },
    {
        "count": 1,
        "name": "Ice Cream Truck",
        "category": ["Cars", "Traffic", "Filler", "Level Any Cars", "Large Cars"],
        "id": 121919,
        "progression": False
    },
    {
        "count": 1,
        "name": "Bonestorm Truck",
        "category": ["Cars", "Traffic", "Filler", "Level Any Cars", "Large Cars"],
        "id": 121920,
        "progression": False
    },
    {
        "count": 1,
        "name": "Cell Phone Car",
        "category": ["Cars", "Traffic", "Filler", "Level Any Cars", "Small Cars"],
        "id": 121921,
        "progression": False
    },
    {
        "count": 1,
        "name": "Milk Truck",
        "category": ["Cars", "Traffic", "Filler", "Level Any Cars", "Large Cars"],
        "id": 121922,
        "progression": False
    },
    {
        "count": 1,
        "name": "Nonuplets Minivan",
        "category": ["Cars", "Traffic", "Filler", "Level Any Cars", "Medium Cars"],
        "id": 121923,
        "progression": False
    },
    {
        "count": 1,
        "name": "Ferrini - Black",
        "category": ["Cars", "Traffic", "Filler", "Level Any Cars", "Small Cars"],
        "id": 121924,
        "progression": False
    },
    {
        "count": 1,
        "name": "Homer Frink-o-Matic Wasp Bumper",
        "category": ["Moves"],
        "progression": True,
        "id": 121925
    },
    {
        "count": 1,
        "name": "Bart Frink-o-Matic Wasp Bumper",
        "category": ["Moves"],
        "progression": True,
        "id": 121926
    },
    {
        "count": 1,
        "name": "Lisa Frink-o-Matic Wasp Bumper",
        "category": ["Moves"],
        "progression": True,
        "id": 121927
    },
    {
        "count": 1,
        "name": "Marge Frink-o-Matic Wasp Bumper",
        "category": ["Moves"],
        "progression": True,
        "id": 121928
    },
    {
        "count": 1,
        "name": "Apu Frink-o-Matic Wasp Bumper",
        "category": ["Moves"],
        "progression": True,
        "id": 121929
    },
    {
        "count": 20,
        "name": "Traffic Trap",
        "category": ["Filler"],
        "trap": True,
        "id": 121930,
        "progression": False
    },
    {
        "count": 1,
        "name": "Cube Van",
        "category": ["Cars", "Traffic", "Filler", "Level Any Cars", "Large Cars"],
        "id": 121931,
        "progression": False
    },
    {
        "count": 1,
        "name": "WWII Vehicle W/ Rocket",
        "category": ["Cars", "Level 7 Cars", "Medium Cars"],
        "useful": True,
        "id": 121932,
        "progression": False
    },
    {
        "count": 1,
        "name": "Audi TT",
        "category": ["Cars", "Level Any Cars", "Small Cars"],
        "useful": True,
        "id": 121933,
        "progression": False
    },
    {
        "count": 1,
        "name": "Homer Forward",
        "category": ["Moves"],
        "progression": True,
        "id": 121938
    },
    {
        "count": 1,
        "name": "Bart Forward",
        "category": ["Moves"],
        "progression": True,
        "id": 121939
    },
    {
        "count": 1,
        "name": "Lisa Forward",
        "category": ["Moves"],
        "progression": True,
        "id": 121940
    },
    {
        "count": 1,
        "name": "Marge Forward",
        "category": ["Moves"],
        "progression": True,
        "id": 121941
    },
    {
        "count": 1,
        "name": "Apu Forward",
        "category": ["Moves"],
        "progression": True,
        "id": 121942 #highest id
    },
]

for item in item_table:
    item_name = item["name"]
    item_id_to_name[item["id"]] = item_name
    item_name_to_item[item_name] = item

    if item["id"] is not None:
        lastItemId = max(lastItemId, item["id"])

    for c in item.get("category", []):
        if c not in item_name_groups:
            item_name_groups[c] = []
        item_name_groups[c].append(item_name)

    for v in item.get("value", {}).keys():
        group_name = f"has_{v.lower().strip()}_value"
        if group_name not in item_name_groups:
            item_name_groups[group_name] = []
        item_name_groups[group_name].append(item_name)

item_id_to_name[None] = "__Victory__"
item_name_to_id = {name: id for id, name in item_id_to_name.items()}


######################
# Item classes
######################


class SimpsonsHitAndRunItem(Item):
    game = "Simpsons Hit and Run"
