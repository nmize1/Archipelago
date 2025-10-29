from BaseClasses import Location
from .Data import location_table
from .hooks.Locations import before_location_table_processed


import json
import pkgutil

def add_cards(level, n_id, location_table):
    cards_data = json.loads(pkgutil.get_data(__name__, "data\\cards.json").decode())

    level_cards = cards_data[level]
    for card in level_cards:
        if "Desc" not in card:
            print("Card missing 'Desc':", card)

    id = n_id

    for card in level_cards:
        carless = f" AND {card['carless']})" if card['carless'] and card['carless'] != "N/A" else ")"
        car = f" AND {card['car']})" if card['car'] and card['car'] != "N/A" else ")"
        glitched = f" AND {card['glitched']})" if card['glitched'] and card['glitched'] != "N/A" else ")"

        location_table.append({
            "name": card["Desc"],
            "region": f"{level}",
            "category": [f"{level} CARD"],
            "requires": f"({{YamlCompare(cardlogic==carless)}}{carless} OR "
                        f"({{YamlCompare(cardlogic==cars)}}{car} OR "
                        f"({{YamlCompare(cardlogic==glitched)}}{glitched}",
            "id": id
        })

        id += 1

    return id


location_table = before_location_table_processed(location_table)
victory_names: list[str] = []
# Replaced manual code with hardcoded ids which are preferable for editing later.
# Need to clean up the rest of the manual stuff that isn't needed anymore.
# id starts at Simpsons' first air date + 500 to allow items to grow if needed
location_table = [
    {
        "name": "(L1M1) SMRT",
        "region": "Level 1",
        "category": [
            "Level 1 Mission"
        ],
        "id": 122289
    },
    {
        "name": "(L1M2) Petty Theft Homer",
        "region": "Level 1",
        "category": [
            "Level 1 Mission"
        ],
        "id": 122290
    },
    {
        "name": "(L1M3) Office Spaced",
        "region": "Level 1",
        "category": [
            "Level 1 Mission"
        ],
        "requires": "|Plow King|",
        "id": 122291
    },
    {
        "name": "(L1M4) Blind Big Brother",
        "region": "Level 1",
        "category": [
            "Level 1 Mission"
        ],
        "requires": "|Homer Progressive Jump:1|",
        "id": 122292
    },
    {
        "name": "(L1M5) Flowers By Irene",
        "region": "Level 1",
        "category": [
            "Level 1 Mission"
        ],
        "requires": "",
        "id": 122293
    },
    {
        "name": "(L1M6) BoneStorm Storm",
        "region": "Level 1",
        "category": [
            "Level 1 Mission"
        ],
        "requires": "",
        "id": 122294
    },
    {
        "name": "(L1M7) The Fat and the Furious",
        "region": "Level 1",
        "category": [
            "Level 1 Mission"
        ],
        "requires": "",
        "id": 122295
    },
    {
        "name": "(L1BM) This Old Shanty",
        "region": "Level 1",
        "category": [
            "Bonus Mission"
        ],
        "id": 122296
    },
    {
        "name": "(LVL 1) Time Trial Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)}  AND |Homer Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 1|)",
        "id": 122297
    },
    {
        "name": "(LVL 1) Circuit Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)}  AND |Homer Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 1|)",
        "id": 122298
    },
    {
        "name": "(LVL 1) Checkpoint Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)}  AND |Homer Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 1|)",
        "id": 122299
    },
    {
        "name": "(L2M1) Detention Deficit Disorder",
        "region": "Level 2",
        "category": [
            "Level 2 Mission"
        ],
        "id": 122300
    },
    {
        "name": "(L2M2) Weapons of Mass Delinquency",
        "region": "Level 2",
        "category": [
            "Level 2 Mission"
        ],
        "id": 122301
    },
    {
        "name": "(L2M3) Vox Nerduli",
        "region": "Level 2",
        "category": [
            "Level 2 Mission"
        ],
        "id": 122302
    },
    {
        "name": "(L2M4) Bart 'n' Frink",
        "region": "Level 2",
        "category": [
            "Level 2 Mission"
        ],
        "id": 122303
    },
    {
        "name": "(L2M5) Better Than Beef",
        "region": "Level 2",
        "category": [
            "Level 2 Mission"
        ],
        "id": 122304
    },
    {
        "name": "(L2M6) Monkey See Monkey D'oh",
        "region": "Level 2",
        "category": [
            "Level 2 Mission"
        ],
        "requires": "|Mr. Plow| AND |Bart Progressive Jump:2|",
        "id": 122305
    },
    {
        "name": "(L2M7) Cell-Outs",
        "region": "Level 2",
        "category": [
            "Level 2 Mission"
        ],
        "requires": "",
        "id": 122306
    },
    {
        "name": "(L2BM) Dial B for Blood",
        "region": "Level 2",
        "category": [
            "Bonus Mission"
        ],
        "id": 122307
    },
    {
        "name": "(LVL 2) Time Trial Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Bart Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 2|)",
        "id": 122308
    },
    {
        "name": "(LVL 2) Circuit Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Bart Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 2|)",
        "id": 122309
    },
    {
        "name": "(LVL 2) Checkpoint Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Bart Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 2|)",
        "id": 122310
    },
    {
        "name": "(L3M1) Nerd Race Queen",
        "region": "Level 3",
        "category": [
            "Level 3 Mission"
        ],
        "id": 122311
    },
    {
        "name": "(L3M2) Clueless",
        "region": "Level 3",
        "category": [
            "Level 3 Mission"
        ],
        "id": 122312
    },
    {
        "name": "(L3M3) Bonfire of the Manatees",
        "region": "Level 3",
        "category": [
            "Level 3 Mission"
        ],
        "id": 122313
    },
    {
        "name": "(L3M4) Operation Hellfish",
        "region": "Level 3",
        "category": [
            "Level 3 Mission"
        ],
        "requires": "|School Bus|",
        "id": 122314
    },
    {
        "name": "(L3M5) Slithery Sleuthing",
        "region": "Level 3",
        "category": [
            "Level 3 Mission"
        ],
        "requires": "|Lisa - Cool|",
        "id": 122315
    },
    {
        "region": "Level 3",
        "name": "(L3M6) Fishy Deals",
        "category": [
            "Level 3 Mission"
        ],
        "requires": "",
        "id": 122316
    },
    {
        "name": "(L3M7) The Old Pirate of the Sea",
        "region": "Level 3",
        "category": [
            "Level 3 Mission"
        ],
        "requires": "",
        "id": 122317
    },
    {
        "name": "(L3BM) Princi-Pal",
        "region": "Level 3",
        "category": [
            "Bonus Mission"
        ],
        "id": 122318
    },
    {
        "name": "(LVL 3) Time Trial Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Lisa Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 3|)",
        "id": 122319
    },
    {
        "name": "(LVL 3) Circuit Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Lisa Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 3|)",
        "id": 122320
    },
    {
        "name": "(LVL 3) Checkpoint Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Lisa Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 3|)",
        "id": 122321
    },
    {
        "name": "(L4M1) For a Few Donuts More",
        "region": "Level 4",
        "category": [
            "Level 4 Mission"
        ],
        "id": 122322
    },
    {
        "name": "(L4M2) Redneck Roundup",
        "region": "Level 4",
        "category": [
            "Level 4 Mission"
        ],
        "id": 122323
    },
    {
        "name": "(L4M3) Ketchup Logic",
        "region": "Level 4",
        "category": [
            "Level 4 Mission"
        ],
        "requires": "|Marge - Inmate|",
        "id": 122324
    },
    {
        "name": "(L4M4) Return of the Nearly-Dead",
        "region": "Level 4",
        "category": [
            "Level 4 Mission"
        ],
        "requires": "",
        "id": 122325
    },
    {
        "name": "(L4M5) Wolves Stole My Pills",
        "region": "Level 4",
        "category": [
            "Level 4 Mission"
        ],
        "requires": "",
        "id": 122326
    },
    {
        "name": "(L4M6) The Cola Wars",
        "region": "Level 4",
        "category": [
            "Level 4 Mission"
        ],
        "requires": "|Marge - Police| AND |Marge Progressive Jump:2|",
        "id": 122327
    },
    {
        "name": "(L4M7) From Outer Space",
        "region": "Level 4",
        "category": [
            "Level 4 Mission"
        ],
        "requires": "",
        "id": 122328
    },
    {
        "name": "(L4BM) Beached Love",
        "region": "Level 4",
        "category": [
            "Bonus Mission"
        ],
        "requires": "|Marge Progressive Jump:1|",
        "id": 122329
    },
    {
        "region": "Races",
        "name": "(LVL 4) Checkpoint Race",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Marge Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 4|)",
        "id": 122330
    },
    {
        "name": "(LVL 4) Circuit Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Marge Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 4|)",
        "id": 122331
    },
    {
        "name": "(LVL 4) Time Trial Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Marge Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 4|)",
        "id": 122332
    },
    {
        "name": "(L5M1) Incriminating Caffeine",
        "region": "Level 5",
        "category": [
            "Level 5 Mission"
        ],
        "id": 122333
    },
    {
        "name": "(L5M2) ...and Baby Makes 8",
        "region": "Level 5",
        "category": [
            "Level 5 Mission"
        ],
        "id": 122334
    },
    {
        "name": "(L5M3) Eight is Too Much",
        "region": "Level 5",
        "category": [
            "Level 5 Mission"
        ],
        "requires": "|Car Built For Homer|",
        "id": 122335
    },
    {
        "name": "(L5M4) This Little Piggy",
        "region": "Level 5",
        "category": [
            "Level 5 Mission"
        ],
        "requires": "|Apu - American|",
        "id": 122336
    },
    {
        "name": "(L5M5) Never Trust a Snake",
        "region": "Level 5",
        "category": [
            "Level 5 Mission"
        ],
        "requires": "|Apu Progressive Jump:2| OR {YamlDisabled(moverandomizer)}",
        "id": 122337
    },
    {
        "name": "(L5M6) Kwik Cash",
        "region": "Level 5",
        "category": [
            "Level 5 Mission"
        ],
        "requires": "",
        "id": 122338
    },
    {
        "name": "(L5M7) Curious Curator",
        "region": "Level 5",
        "category": [
            "Level 5 Mission"
        ],
        "requires": "",
        "id": 122339
    },
    {
        "name": "(L5BM) Kinky Frinky",
        "region": "Level 5",
        "category": [
            "Bonus Mission"
        ],
        "id": 122340
    },
    {
        "name": "(LVL 5) Checkpoint Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Apu Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 5|)",
        "id": 122341
    },
    {
        "name": "(LVL 5) Circuit Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Apu Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 5|)",
        "id": 122342
    },
    {
        "name": "(LVL 5) Time Trial Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Apu Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 5|)",
        "id": 122343
    },
    {
        "name": "(L6M1) Going to the Lu'",
        "region": "Level 6",
        "category": [
            "Level 6 Mission"
        ],
        "id": 122344
    },
    {
        "name": "(L6M2) Getting Down with the Clown",
        "region": "Level 6",
        "category": [
            "Level 6 Mission"
        ],
        "id": 122345
    },
    {
        "name": "(L6M3) Lab Coat Caper",
        "region": "Level 6",
        "category": [
            "Level 6 Mission"
        ],
        "id": 122346
    },
    {
        "name": "(L6M4) Duff for Me, Duff for You",
        "region": "Level 6",
        "category": [
            "Level 6 Mission"
        ],
        "id": 122347
    },
    {
        "name": "(L6M5) Full Metal Jackass",
        "region": "Level 6",
        "category": [
            "Level 6 Mission"
        ],
        "id": 122348
    },
    {
        "name": "(L6M6) Set to Kill",
        "region": "Level 6",
        "category": [
            "Level 6 Mission"
        ],
        "requires": "|Globex Super Villain Car|",
        "id": 122349
    },
    {
        "name": "(L6M7) Kang and Kodos Strike Back",
        "region": "Level 6",
        "category": [
            "Level 6 Mission"
        ],
        "id": 122350
    },
    {
        "name": "(L6BM) Milking The Pigs",
        "region": "Level 6",
        "category": [
            "Bonus Mission"
        ],
        "id": 122351
    },
    {
        "name": "(LVL 6) Checkpoint Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Bart Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 6|)",
        "id": 122352
    },
    {
        "name": "(LVL 6) Time Trial Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Bart Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 6|)",
        "id": 122353
    },
    {
        "name": "(LVL 6) Circuit Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Bart Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 6|)",
        "id": 122354
    },
    {
        "name": "(L7M1) Rigor Motors",
        "region": "Level 7",
        "category": [
            "Level 7 Mission"
        ],
        "id": 122355
    },
    {
        "name": "(L7M2) Long Black Probes",
        "region": "Level 7",
        "category": [
            "Level 7 Mission"
        ],
        "requires": "|Zombie Car|",
        "id": 122356
    },
    {
        "name": "(L7M3) Pocket Protector",
        "region": "Level 7",
        "category": [
            "Level 7 Mission"
        ],
        "requires": "",
        "id": 122357
    },
    {
        "name": "(L7M4) There's Something About Monty",
        "region": "Level 7",
        "category": [
            "Level 7 Mission"
        ],
        "requires": "|Homer Progressive Jump:2|",
        "id": 122358
    },
    {
        "name": "(L7M5) Alien \"Auto\"topsy Part 1",
        "region": "Level 7",
        "category": [
            "Level 7 Mission"
        ],
        "requires": "",
        "id": 122359
    },
    {
        "name": "(L7M6) Alien \"Auto\"topsy Part 2",
        "region": "Level 7",
        "category": [
            "Level 7 Mission"
        ],
        "requires": "",
        "id": 122360
    },
    {
        "name": "(L7M7) Alien \"Auto\"topsy Part 3",
        "region": "Level 7",
        "category": [
            "Level 7 Mission"
        ],
        "requires": "",
        "id": 122361
    },
    {
        "name": "(L7BM) Flaming Tires",
        "region": "Level 7",
        "category": [
            "Bonus Mission"
        ],
        "requires": "|Homer Progressive Jump:1|",
        "id": 122362
    },
    {
        "name": "(LVL 7) Time Trial Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Homer Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 7|)",
        "id": 122363
    },
    {
        "name": "(LVL 7) Circuit Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Homer Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 7|)",
        "id": 122364
    },
    {
        "name": "(LVL 7) Checkpoint Race",
        "region": "Races",
        "category": [
            "Bonus Mission"
        ],
        "requires": "({YamlEnabled(shufflecheckeredflags)} AND |Homer Checkered Flag|) OR ({YamlDisabled(shufflecheckeredflags)} AND |Level 7|)",
        "id": 122365
    },
    {
        "name": "(LVL 1) WASP - Small Park Next to Simpsons House",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122366
    },
    {
        "name": "(LVL 1) WASP - Next to the Blue House Besides Simpsons House",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122367
    },
    {
        "name": "(LVL 1) WASP - Flanders Backyard",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122368
    },
    {
        "name": "(LVL 1) WASP - Wiggum's Backyard",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122369
    },
    {
        "name": "(LVL 1) WASP - Kwik-E-Mart Roof",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122370
    },
    {
        "name": "(LVL 1) WASP - Gas Pump Roof",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122371
    },
    {
        "name": "(LVL 1) WASP - Lard Lads Roof",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122372
    },
    {
        "name": "(LVL 1) WASP - School Yard Bus",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122373
    },
    {
        "name": "(LVL 1) WASP - Back Door of School",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122374
    },
    {
        "name": "(LVL 1) WASP - School Roof 1",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122375
    },
    {
        "name": "(LVL 1) WASP - School Roof 2",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122376
    },
    {
        "name": "(LVL 1) WASP - Top of Tower Before Broken Bridge",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122377
    },
    {
        "name": "(LVL 1) WASP - Rocket Car",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122378
    },
    {
        "name": "(LVL 1) WASP - StoneCutters Table 1",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122379
    },
    {
        "name": "(LVL 1) WASP - StoneCutters Table 2",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122380
    },
    {
        "name": "(LVL 1) WASP - Barn Haystack",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122381
    },
    {
        "name": "(LVL 1) WASP - Trailer Park 1",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122382
    },
    {
        "name": "(LVL 1) WASP - Trailer Park 2",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Progressive Jump:2| AND (|Homer Attack|) OR {YamlDisabled(moverandomizer)}",
        "id": 122383
    },
    {
        "name": "(LVL 1) WASP - Atop of Bridge Framework 1",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Progressive Jump:2| AND (|Homer Attack|) OR {YamlDisabled(moverandomizer)}",
        "id": 122384
    },
    {
        "name": "(LVL 1) WASP - Atop of Bridge Framework 2",
        "region": "Collectables",
        "category": [
            "Level 1 WASP"
        ],
        "requires": "|Homer Progressive Jump:2| AND (|Homer Attack|) OR {YamlDisabled(moverandomizer)}",
        "id": 122385
    },
    {
        "name": "(LVL 1) GAG - Simpsons TV",
        "region": "Collectables",
        "category": [
            "Level 1 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND |Level 1|) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122393
    },
    {
        "name": "(LVL 1) GAG - Swings Besides Blue House",
        "region": "Collectables",
        "category": [
            "Level 1 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND |Level 1|) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122394
    },
    {
        "name": "(LVL 1) GAG - Simpsons Grill",
        "region": "Collectables",
        "category": [
            "Level 1 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND |Level 1|) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122395
    },
    {
        "name": "(LVL 1) GAG - Simpsons Swing",
        "region": "Collectables",
        "category": [
            "Level 1 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND |Level 1|) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122396
    },
    {
        "name": "(LVL 1) GAG - Simpsons FireBreathing Tiki",
        "region": "Collectables",
        "category": [
            "Level 1 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND |Level 1|) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122397
    },
    {
        "name": "(LVL 1) GAG - Flanders Bomb Shelter",
        "region": "Collectables",
        "category": [
            "Level 1 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND |Level 1|) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122398
    },
    {
        "name": "(LVL 1) GAG - Tank in Front of Power Plant",
        "region": "Collectables",
        "category": [
            "Level 1 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND |Level 1|) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122399
    },
    {
        "name": "(LVL 1) GAG - Homer's Workstation Meltdown",
        "region": "Collectables",
        "category": [
            "Level 1 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND |Level 1|) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122400
    },
    {
        "name": "(LVL 1) GAG - School Fire Extinguisher",
        "region": "Collectables",
        "category": [
            "Level 1 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND |Level 1|) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122401
    },
    {
        "name": "(LVL 1) GAG - School Fire Alarm",
        "region": "Collectables",
        "category": [
            "Level 1 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND |Level 1|) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122402
    },
    {
        "name": "(LVL 1) GAG - Man in Freezer at Kwik-E-Mart",
        "region": "Collectables",
        "category": [
            "Level 1 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND |Level 1|) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122403
    },
    {
        "name": "(LVL 1) GAG - Silent Alarm in Kwik-E-Mart",
        "region": "Collectables",
        "category": [
            "Level 1 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND |Level 1|) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122404
    },
    {
        "name": "(LVL 1) GAG - Arcade Cabinet in Kwik-E-Mart",
        "region": "Collectables",
        "category": [
            "Level 1 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND |Level 1|) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122405
    },
    {
        "name": "(LVL 1) GAG - Squishee Machine in Kwik-E-Mart",
        "region": "Collectables",
        "category": [
            "Level 1 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND |Level 1|) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122406
    },
    {
        "name": "(LVL 1) GAG - ATM in Kwik-E-Mart",
        "region": "Collectables",
        "category": [
            "Level 1 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND |Level 1|) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122691
    },
    {
        "name": "(LVL 1) Shop Check 1",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": [],
        "id": 122407
    },
    {
        "name": "(LVL 1) Shop Check 2",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": [],
        "id": 122408
    },
    {
        "name": "(LVL 1) Shop Check 3",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": [],
        "id": 122409
    },
    {
        "name": "(LVL 1) Shop Check 4",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": [],
        "id": 122410
    },
    {
        "name": "(LVL 1) Shop Check 5",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": [],
        "id": 122411
    },
    {
        "name": "(LVL 1) Shop Check 6",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": [],
        "id": 122412
    },
    {
        "name": "(LVL 2) WASP - CourtHouse Steps",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122413
    },
    {
        "name": "(LVL 2) WASP - Gazebo Between Museum and Courthouse",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122414
    },
    {
        "name": "(LVL 2) WASP - Museum Steps",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122415
    },
    {
        "name": "(LVL 2) WASP - Hospital Front Yard",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122416
    },
    {
        "name": "(LVL 2) WASP - Roof Across Monkey Building",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "((|Bart Attack|) AND |Bart Progressive Jump:2|)",
        "id": 122417
    },
    {
        "name": "(LVL 2) WASP - Town Hall (Front)",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122418
    },
    {
        "name": "(LVL 2) WASP - Town Hall (Back)",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122419
    },
    {
        "name": "(LVL 2) WASP - Behind Downtown Krusty Burger",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122420
    },
    {
        "name": "(LVL 2) WASP - Monorail Stairs",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122421
    },
    {
        "name": "(LVL 2) WASP - Upstair Beside Monorail",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122422
    },
    {
        "name": "(LVL 2) WASP - Roof Across Monorail",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "((|Bart Attack|) AND |Bart Progressive Jump:2|)",
        "id": 122423
    },
    {
        "name": "(LVL 2) WASP - Stairs Leading atop Trains",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122424
    },
    {
        "name": "(LVL 2) WASP - Across Moving Train",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "((|Bart Attack|) AND |Bart Progressive Jump:2|)",
        "id": 122425
    },
    {
        "name": "(LVL 2) WASP - On Train Past Water Tank",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "((|Bart Attack|) AND |Bart Progressive Jump:2|)",
        "id": 122426
    },
    {
        "name": "(LVL 2) WASP - Inside Trainyard Parking Spot",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "|Bart Attack|",
        "id": 122427
    },
    {
        "name": "(LVL 2) WASP - Car Wash",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122428
    },
    {
        "name": "(LVL 2) WASP - Legitimate Businessman's Rooftop 1",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "((|Bart Attack|) AND |Bart Progressive Jump:2|)",
        "id": 122429
    },
    {
        "name": "(LVL 2) WASP - Legitimate Businessman's Rooftop 2",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "((|Bart Attack|) AND |Bart Progressive Jump:2|)",
        "id": 122430
    },
    {
        "name": "(LVL 2) WASP - Roof Next to Moe's",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "(|Bart Attack| AND |Bart Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122431
    },
    {
        "name": "(LVL 2) WASP - Lard Lads Roof",
        "region": "Collectables",
        "category": [
            "Level 2 WASP"
        ],
        "requires": "((|Bart Attack|) AND |Bart Progressive Jump:2|)",
        "id": 122432
    },
    {
        "name": "(LVL 2) GAG - CATapult",
        "region": "Collectables",
        "category": [
            "Level 2 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 2| OR |Progressive Level:1|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122440
    },
    {
        "name": "(LVL 2) GAG - Cement Truck",
        "region": "Collectables",
        "category": [
            "Level 2 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 2| OR |Progressive Level:1|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122441
    },
    {
        "name": "(LVL 2) GAG - Pickled Egg Jar at Moes",
        "region": "Collectables",
        "category": [
            "Level 2 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 2| OR |Progressive Level:1|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122442
    },
    {
        "name": "(LVL 2) GAG - Slot Machine at Moes",
        "region": "Collectables",
        "category": [
            "Level 2 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 2| OR |Progressive Level:1|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122443
    },
    {
        "name": "(LVL 2) GAG - Love Tester as Moes",
        "region": "Collectables",
        "category": [
            "Level 2 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 2| OR |Progressive Level:1|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122444
    },
    {
        "name": "(LVL 2) GAG - Light up Drinks at Moes",
        "region": "Collectables",
        "category": [
            "Level 2 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 2| OR |Progressive Level:1|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122445
    },
    {
        "name": "(LVL 2) GAG - Rat's Milk Machine atop Legitimate Businessman's Roof",
        "region": "Collectables",
        "category": [
            "Level 2 GAG"
        ],
        "requires": "(({YamlDisabled(shufflegagfinder)} AND (|Level 2| OR |Progressive Level:1|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)) AND (|Bart Progressive Jump:2| OR {YamlDisabled(moverandomizer)})",
        "id": 122446
    },
    {
        "name": "(LVL 2) GAG - Blinding Hans Moleman at the DMV",
        "region": "Collectables",
        "category": [
            "Level 2 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 2| OR |Progressive Level:1|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122447
    },
    {
        "name": "(LVL 2) GAG - Car Ride at Try-N-Save",
        "region": "Collectables",
        "category": [
            "Level 2 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 2| OR |Progressive Level:1|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122448
    },
    {
        "name": "(LVL 2) GAG - Missile Behind Military Antiques",
        "region": "Collectables",
        "category": [
            "Level 2 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 2| OR |Progressive Level:1|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122449
    },
    {
        "name": "(LVL 2) GAG - Dumpster Behind Krusty Burger (Near Police Station)",
        "region": "Collectables",
        "category": [
            "Level 2 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 2| OR |Progressive Level:1|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122450
    },
    {
        "name": "(LVL 2) Shop Check 1",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade|",
        "id": 122451
    },
    {
        "name": "(LVL 2) Shop Check 2",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade|",
        "id": 122452
    },
    {
        "name": "(LVL 2) Shop Check 3",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade|",
        "id": 122453
    },
    {
        "name": "(LVL 2) Shop Check 4",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade|",
        "id": 122454
    },
    {
        "name": "(LVL 2) Shop Check 5",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade|",
        "id": 122455
    },
    {
        "name": "(LVL 2) Shop Check 6",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade|",
        "id": 122456
    },
    {
        "name": "(LVL 3) Shop Check 1",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:2|",
        "id": 122457
    },
    {
        "name": "(LVL 3) Shop Check 2",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:2|",
        "id": 122458
    },
    {
        "name": "(LVL 3) Shop Check 3",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:2|",
        "id": 122459
    },
    {
        "name": "(LVL 3) Shop Check 4",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:2|",
        "id": 122460
    },
    {
        "name": "(LVL 3) Shop Check 5",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:2|",
        "id": 122461
    },
    {
        "name": "(LVL 3) Shop Check 6",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:2|",
        "id": 122462
    },
    {
        "name": "(LVL 3) WASP - Observatory",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "|Lisa Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122463
    },
    {
        "name": "(LVL 3) WASP - Broken Railing Below Dam",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "|Lisa Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122464
    },
    {
        "name": "(LVL 3) WASP - Broken Railing Above Dam (Exit)",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "|Lisa Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122465
    },
    {
        "name": "(LVL 3) WASP - Kamp Krusty Near Stage",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "|Lisa Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122466
    },
    {
        "name": "(LVL 3) WASP - Kamp Krusty Well",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "|Lisa Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122467
    },
    {
        "name": "(LVL 3) WASP - Exit of Kamp Krusty's Well",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "|Lisa Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122468
    },
    {
        "name": "(LVL 3) WASP - Motel Complex",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "|Lisa Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122469
    },
    {
        "name": "(LVL 3) WASP - Duff Brewery Behind Krusty Glass",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "|Lisa Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122470
    },
    {
        "name": "(LVL 3) WASP - Duff Blimp 1",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "|Lisa Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122471
    },
    {
        "name": "(LVL 3) WASP - Duff Blimp 2",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "|Lisa Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122472
    },
    {
        "name": "(LVL 3) WASP - Krusty Studio Left",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "|Lisa Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122473
    },
    {
        "name": "(LVL 3) WASP - Krusty Studio Right",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "|Lisa Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122474
    },
    {
        "name": "(LVL 3) WASP - (Boat) Front end of Boat",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "((|Lisa Attack|) AND |Lisa Progressive Jump:2|)",
        "id": 122475
    },
    {
        "name": "(LVL 3) WASP - (Boat) Next to the Crane",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "((|Lisa Attack|) AND |Lisa Progressive Jump:2|)",
        "id": 122476
    },
    {
        "name": "(LVL 3) WASP - (Boat) Stairs",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "((|Lisa Attack|) AND |Lisa Progressive Jump:2|)",
        "id": 122477
    },
    {
        "name": "(LVL 3) WASP - LightHouse",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "|Lisa Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122478
    },
    {
        "name": "(LVL 3) WASP - Planet Hype",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "|Lisa Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122479
    },
    {
        "name": "(LVL 3) WASP - Beach",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "|Lisa Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122480
    },
    {
        "name": "(LVL 3) WASP - Bowling Rooftop",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "((|Lisa Attack|) AND |Lisa Progressive Jump:2|)",
        "id": 122481
    },
    {
        "name": "(LVL 3) WASP - Comic Book Guy Rooftop",
        "region": "Collectables",
        "category": [
            "Level 3 WASP"
        ],
        "requires": "|Lisa Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122482
    },
    {
        "name": "(LVL 3) GAG - Comic Book Guy Robot",
        "region": "Collectables",
        "category": [
            "Level 3 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 3| OR |Progressive Level:2|)) OR ({YamlEnabled(shufflegagfinder)} AND |Lisa Gagfinder|)",
        "id": 122490
    },
    {
        "name": "(LVL 3) GAG - Comic Book Guy Radioactive Man",
        "region": "Collectables",
        "category": [
            "Level 3 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 3| OR |Progressive Level:2|)) OR ({YamlEnabled(shufflegagfinder)} AND |Lisa Gagfinder|)",
        "id": 122491
    },
    {
        "name": "(LVL 3) GAG - Yellow Dumpster Across Krusty Burger",
        "region": "Collectables",
        "category": [
            "Level 3 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 3| OR |Progressive Level:2|)) OR ({YamlEnabled(shufflegagfinder)} AND |Lisa Gagfinder|)",
        "id": 122492
    },
    {
        "name": "(LVL 3) GAG - Kid Drowning in Ball Pit",
        "region": "Collectables",
        "category": [
            "Level 3 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 3| OR |Progressive Level:2|)) OR ({YamlEnabled(shufflegagfinder)} AND |Lisa Gagfinder|)",
        "id": 122493
    },
    {
        "name": "(LVL 3) GAG - Crane on Ship",
        "region": "Collectables",
        "category": [
            "Level 3 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 3| OR |Progressive Level:2|)) OR ({YamlEnabled(shufflegagfinder)} AND |Lisa Gagfinder|)",
        "id": 122494
    },
    {
        "name": "(LVL 3) GAG - Observatory Alarm",
        "region": "Collectables",
        "category": [
            "Level 3 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 3| OR |Progressive Level:2|)) OR ({YamlEnabled(shufflegagfinder)} AND |Lisa Gagfinder|)",
        "id": 122495
    },
    {
        "name": "(LVL 3) GAG - Perpetual Motion Machine at Observatory",
        "region": "Collectables",
        "category": [
            "Level 3 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 3| OR |Progressive Level:2|)) OR ({YamlEnabled(shufflegagfinder)} AND |Lisa Gagfinder|)",
        "id": 122496
    },
    {
        "name": "(LVL 3) GAG - Telescope at Observatory",
        "region": "Collectables",
        "category": [
            "Level 3 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 3| OR |Progressive Level:2|)) OR ({YamlEnabled(shufflegagfinder)} AND |Lisa Gagfinder|)",
        "id": 122497
    },
    {
        "name": "(LVL 3) GAG - (Observatory) Monkey",
        "region": "Collectables",
        "category": [
            "Level 3 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 3| OR |Progressive Level:2|)) OR ({YamlEnabled(shufflegagfinder)} AND |Lisa Gagfinder|)",
        "id": 122498
    },
    {
        "name": "(LVL 3) GAG - Kamp Krusty Flag",
        "region": "Collectables",
        "category": [
            "Level 3 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 3| OR |Progressive Level:2|)) OR ({YamlEnabled(shufflegagfinder)} AND |Lisa Gagfinder|)",
        "id": 122499
    },
    {
        "name": "(LVL 3) GAG - Boar's Head at Kamp Krusty",
        "region": "Collectables",
        "category": [
            "Level 3 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 3| OR |Progressive Level:2|)) OR ({YamlEnabled(shufflegagfinder)} AND |Lisa Gagfinder|)",
        "id": 122500
    },
    {
        "name": "(LVL 4) WASP - Blue House Before Krusty Glass 1",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122501
    },
    {
        "name": "(LVL 4) WASP - Blue House Before Krusty Glass 2",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122502
    },
    {
        "name": "(LVL 4) WASP - Flander's Backyard",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122503
    },
    {
        "name": "(LVL 4) WASP - Wiggum's Backyard 1",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122504
    },
    {
        "name": "(LVL 4) WASP - Wiggum's Backyard 2",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122505
    },
    {
        "name": "(LVL 4) WASP - Kwik-E-Mart Rooftop",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122506
    },
    {
        "name": "(LVL 4) WASP - Gas Station Rooftop",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122507
    },
    {
        "name": "(LVL 4) WASP - Atop Gasoline Pump",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122508
    },
    {
        "name": "(LVL 4) WASP - Mr. Burns Giant ChessBoard 1",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122509
    },
    {
        "name": "(LVL 4) WASP - Mr. Burns Giant ChessBoard 2",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122510
    },
    {
        "name": "(LVL 4) WASP - Mr. Burns StairCase",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122511
    },
    {
        "name": "(LVL 4) WASP - Mr. Burns Library",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122512
    },
    {
        "name": "(LVL 4) WASP - Outside of Homer's Workstation",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122513
    },
    {
        "name": "(LVL 4) WASP - Atop Trailer Park",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122514
    },
    {
        "name": "(LVL 4) WASP - In Trailer Park",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122515
    },
    {
        "name": "(LVL 4) WASP - Barn",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122516
    },
    {
        "name": "(LVL 4) WASP - Behind School Steps",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122517
    },
    {
        "name": "(LVL 4) WASP - School Rooftop 1",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122518
    },
    {
        "name": "(LVL 4) WASP - School Rooftop 2",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122519
    },
    {
        "name": "(LVL 4) WASP - Atop Tower Before Broken Bridge",
        "region": "Collectables",
        "category": [
            "Level 4 WASP"
        ],
        "requires": "|Marge Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122520
    },
    {
        "name": "(LVL 4) GAG - Simpson TV",
        "region": "Collectables",
        "category": [
            "Level 4 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 4| OR |Progressive Level:3|)) OR ({YamlEnabled(shufflegagfinder)} AND |Marge Gagfinder|)",
        "id": 122528
    },
    {
        "name": "(LVL 4) GAG - Simpsons Swings",
        "region": "Collectables",
        "category": [
            "Level 4 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 4| OR |Progressive Level:3|)) OR ({YamlEnabled(shufflegagfinder)} AND |Marge Gagfinder|)",
        "id": 122529
    },
    {
        "name": "(LVL 4) GAG - Simpsons Grill",
        "region": "Collectables",
        "category": [
            "Level 4 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 4| OR |Progressive Level:3|)) OR ({YamlEnabled(shufflegagfinder)} AND |Marge Gagfinder|)",
        "id": 122530
    },
    {
        "name": "(LVL 4) GAG - Simpsons Fire Breathing Tiki",
        "category": [
            "Level 4 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 4| OR |Progressive Level:3|)) OR ({YamlEnabled(shufflegagfinder)} AND |Marge Gagfinder|)",
        "region": "Collectables",
        "id": 122531
    },
    {
        "name": "(LVL 4) GAG - Krusty Lamp (Bart's Room)",
        "region": "Collectables",
        "category": [
            "Level 4 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 4| OR |Progressive Level:3|)) OR ({YamlEnabled(shufflegagfinder)} AND |Marge Gagfinder|)",
        "id": 122532
    },
    {
        "name": "(LVL 4) GAG - Flanders Bomb Shelter",
        "region": "Collectables",
        "category": [
            "Level 4 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 4| OR |Progressive Level:3|)) OR ({YamlEnabled(shufflegagfinder)} AND |Marge Gagfinder|)",
        "id": 122533
    },
    {
        "name": "(LVL 4) GAG - Tank Outside Power Plant",
        "region": "Collectables",
        "category": [
            "Level 4 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 4| OR |Progressive Level:3|)) OR ({YamlEnabled(shufflegagfinder)} AND |Marge Gagfinder|)",
        "id": 122534
    },
    {
        "name": "(LVL 4) GAG - Homer's Workstation Meltdown",
        "region": "Collectables",
        "category": [
            "Level 4 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 4| OR |Progressive Level:3|)) OR ({YamlEnabled(shufflegagfinder)} AND |Marge Gagfinder|)",
        "id": 122535
    },
    {
        "name": "(LVL 4) GAG - School Fire Extinguisher ",
        "region": "Collectables",
        "category": [
            "Level 4 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 4| OR |Progressive Level:3|)) OR ({YamlEnabled(shufflegagfinder)} AND |Marge Gagfinder|)",
        "id": 122536
    },
    {
        "name": "(LVL 4) GAG - School Fire Alarm",
        "region": "Collectables",
        "category": [
            "Level 4 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 4| OR |Progressive Level:3|)) OR ({YamlEnabled(shufflegagfinder)} AND |Marge Gagfinder|)",
        "id": 122537
    },
    {
        "name": "(LVL 4) GAG - Frozen man in Kwik-E-Mart",
        "region": "Collectables",
        "category": [
            "Level 4 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 4| OR |Progressive Level:3|)) OR ({YamlEnabled(shufflegagfinder)} AND |Marge Gagfinder|)",
        "id": 122538
    },
    {
        "name": "(LVL 4) GAG - Silent Alarm in Kwik-E-Mart",
        "region": "Collectables",
        "category": [
            "Level 4 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 4| OR |Progressive Level:3|)) OR ({YamlEnabled(shufflegagfinder)} AND |Marge Gagfinder|)",
        "id": 122539
    },
    {
        "name": "(LVL 4) GAG - ATM in Kwik-E-Mart",
        "region": "Collectables",
        "category": [
            "Level 4 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 4| OR |Progressive Level:3|)) OR ({YamlEnabled(shufflegagfinder)} AND |Marge Gagfinder|)",
        "id": 122540
    },
    {
        "name": "(LVL 4) GAG - Arcade Cabinet in Kwik-E-Mart",
        "region": "Collectables",
        "category": [
            "Level 4 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 4| OR |Progressive Level:3|)) OR ({YamlEnabled(shufflegagfinder)} AND |Marge Gagfinder|)",
        "id": 122541
    },
    {
        "name": "(LVL 4) GAG - Squishee Machine in Kwik-E-Mart",
        "region": "Collectables",
        "category": [
            "Level 4 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 4| OR |Progressive Level:3|)) OR ({YamlEnabled(shufflegagfinder)} AND |Marge Gagfinder|)",
        "id": 122542
    },
    {
        "name": "(LVL 4) Shop Check 1",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:3|",
        "id": 122543
    },
    {
        "name": "(LVL 4) Shop Check 2",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:3|",
        "id": 122544
    },
    {
        "name": "(LVL 4) Shop Check 3",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:3|",
        "id": 122545
    },
    {
        "name": "(LVL 4) Shop Check 4",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:3|",
        "id": 122546
    },
    {
        "name": "(LVL 4) Shop Check 5",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:3|",
        "id": 122547
    },
    {
        "name": "(LVL 4) Shop Check 6",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:3|",
        "id": 122548
    },
    {
        "name": "(LVL 5) WASP - Front of Hospital",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "|Apu Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122549
    },
    {
        "name": "(LVL 5) WASP - Gazebo Between Museum & Court House",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "|Apu Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122550
    },
    {
        "name": "(LVL 5) WASP - Steps of Town Hall",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "|Apu Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122551
    },
    {
        "name": "(LVL 5) WASP - Museum Steps",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "|Apu Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122552
    },
    {
        "name": "(LVL 5) WASP - Rooftop Next to Moes",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "((|Apu Attack|) AND |Apu Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122553
    },
    {
        "name": "(LVL 5) WASP - Legitimate Businessman's Rooftop 1",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "((|Apu Attack|) AND |Apu Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122554
    },
    {
        "name": "(LVL 5) WASP - Legitimate Businessman's Rooftop 2",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "((|Apu Attack|) AND |Apu Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122555
    },
    {
        "name": "(LVL 5) WASP - Trainyard Stairs",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "|Apu Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122556
    },
    {
        "name": "(LVL 5) WASP - Other Side of Moving Train",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "((|Apu Attack|) AND |Apu Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122557
    },
    {
        "name": "(LVL 5) WASP - Watertower 1",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "((|Apu Attack|) AND |Apu Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122558
    },
    {
        "name": "(LVL 5) WASP - Watertower 2",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "((|Apu Attack|) AND |Apu Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122559
    },
    {
        "name": "(LVL 5) WASP - Police Station Steps",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "|Apu Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122560
    },
    {
        "name": "(LVL 5) WASP - Monorail Stairs",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "|Apu Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122561
    },
    {
        "name": "(LVL 5) WASP - Monorail",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "((|Apu Attack|) AND |Apu Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122562
    },
    {
        "name": "(LVL 5) WASP - Otherside of Monorail 1",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "((|Apu Attack|) AND |Apu Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122563
    },
    {
        "name": "(LVL 5) WASP - Otherside of Monorail 2",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "((|Apu Attack|) AND |Apu Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122564
    },
    {
        "name": "(LVL 5) WASP - Under Giant Purple Beams 1",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "|Apu Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122565
    },
    {
        "name": "(LVL 5) WASP - Under Giant Purple Beams 2",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "|Apu Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122566
    },
    {
        "name": "(LVL 5) WASP - Alleyway Rooftop",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "|Apu Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122567
    },
    {
        "name": "(LVL 5) WASP - Fountain in from Stadium",
        "region": "Collectables",
        "category": [
            "Level 5 WASP"
        ],
        "requires": "((|Apu Attack|) AND |Apu Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122568
    },
    {
        "name": "(LVL 5) GAG - Pickled Egg in Moe's",
        "region": "Collectables",
        "category": [
            "Level 5 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 5| OR |Progressive Level:4|)) OR ({YamlEnabled(shufflegagfinder)} AND |Apu Gagfinder|)",
        "id": 122576
    },
    {
        "name": "(LVL 5) GAG - Slot Machine in Moe's",
        "region": "Collectables",
        "category": [
            "Level 5 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 5| OR |Progressive Level:4|)) OR ({YamlEnabled(shufflegagfinder)} AND |Apu Gagfinder|)",
        "id": 122577
    },
    {
        "name": "(LVL 5) GAG - Love Tester in Moe's",
        "region": "Collectables",
        "category": [
            "Level 5 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 5| OR |Progressive Level:4|)) OR ({YamlEnabled(shufflegagfinder)} AND |Apu Gagfinder|)",
        "id": 122578
    },
    {
        "name": "(LVL 5) GAG - Blind Hans Moleman at the DMV",
        "region": "Collectables",
        "category": [
            "Level 5 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 5| OR |Progressive Level:4|)) OR ({YamlEnabled(shufflegagfinder)} AND |Apu Gagfinder|)",
        "id": 122579
    },
    {
        "name": "(LVL 5) GAG - Dumpster Behind Behind Krusty Burger (Near Police Station)",
        "region": "Collectables",
        "category": [
            "Level 5 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 5| OR |Progressive Level:4|)) OR ({YamlEnabled(shufflegagfinder)} AND |Apu Gagfinder|)",
        "id": 122580
    },
    {
        "name": "(LVL 5) GAG - Light Up Drinks in Moe's",
        "region": "Collectables",
        "category": [
            "Level 5 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 5| OR |Progressive Level:4|)) OR ({YamlEnabled(shufflegagfinder)} AND |Apu Gagfinder|)",
        "id": 122690
    },
    {
        "name": "(LVL 5) Shop Check 1",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:4|",
        "id": 122581
    },
    {
        "name": "(LVL 5) Shop Check 2",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:4|",
        "id": 122582
    },
    {
        "name": "(LVL 5) Shop Check 3",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:4|",
        "id": 122583
    },
    {
        "name": "(LVL 5) Shop Check 4",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:4|",
        "id": 122584
    },
    {
        "name": "(LVL 5) Shop Check 5",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:4|",
        "id": 122585
    },
    {
        "name": "(LVL 5) Shop Check 6",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:4|",
        "id": 122586
    },
    {
        "name": "(LVL 6) Shop Check 1",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:5|",
        "id": 122587
    },
    {
        "name": "(LVL 6) Shop Check 2",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:5|",
        "id": 122588
    },
    {
        "name": "(LVL 6) Shop Check 3",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:5|",
        "id": 122589
    },
    {
        "name": "(LVL 6) WASP - Observatory 1",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122590
    },
    {
        "name": "(LVL 6) WASP - Observatory 2",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122591
    },
    {
        "name": "(LVL 6) WASP - Kamp Krusty 1",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122592
    },
    {
        "name": "(LVL 6) WASP - Kamp Krusty 2",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122593
    },
    {
        "name": "(LVL 6) WASP - Broken Railing Below Dam",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122594
    },
    {
        "name": "(LVL 6) WASP - Broken Railing Exit",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122595
    },
    {
        "name": "(LVL 6) WASP - Motel",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122596
    },
    {
        "name": "(LVL 6) WASP - Duff Brewery Krusty Glass",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122597
    },
    {
        "name": "(LVL 6) WASP - Under Duff Blimp",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122598
    },
    {
        "name": "(LVL 6) WASP - Krusty Studio Left",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122599
    },
    {
        "name": "(LVL 6) WASP - Krusty Studio Right",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122600
    },
    {
        "name": "(LVL 6) WASP - Krusty Studio Balcony",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "((|Bart Attack|) AND |Bart Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122601
    },
    {
        "name": "(LVL 6) WASP - (Boat) Crane",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "((|Bart Attack|) AND |Bart Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122602
    },
    {
        "name": "(LVL 6) WASP - (Boat) Staircase 1",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "((|Bart Attack|) AND |Bart Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122603
    },
    {
        "name": "(LVL 6) WASP - (Boat) Staircase 2",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "((|Bart Attack|) AND |Bart Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122604
    },
    {
        "name": "(LVL 6) WASP - Lighthouse",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122605
    },
    {
        "name": "(LVL 6) WASP - Planet Hype Rooftop",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122606
    },
    {
        "name": "(LVL 6) WASP - Bowling Rooftop",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "((|Bart Attack|) AND |Bart Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122607
    },
    {
        "name": "(LVL 6) WASP - Comic Book Guy Rooftop 1",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122608
    },
    {
        "name": "(LVL 6) WASP - Comic Book Guy Rooftop 2",
        "region": "Collectables",
        "category": [
            "Level 6 WASP"
        ],
        "requires": "|Bart Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122609
    },
    {
        "name": "(LVL 6) GAG - Comic Book Guy Robot",
        "region": "Collectables",
        "category": [
            "Level 6 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 6| OR |Progressive Level:5|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122617
    },
    {
        "name": "(LVL 6) GAG - Comic Book Guy Radioactive Man",
        "region": "Collectables",
        "category": [
            "Level 6 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 6| OR |Progressive Level:5|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122618
    },
    {
        "region": "Collectables",
        "name": "(LVL 6) GAG - Yellow Dumpster Across Krusty Burger",
        "category": [
            "Level 6 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 6| OR |Progressive Level:5|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122619
    },
    {
        "name": "(LVL 6) GAG - Kid Drowning in Ball Pit",
        "region": "Collectables",
        "category": [
            "Level 6 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 6| OR |Progressive Level:5|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122620
    },
    {
        "name": "(LVL 6) GAG - Crane on Ship",
        "region": "Collectables",
        "category": [
            "Level 6 GAG"
        ],
        "requires": "(({YamlDisabled(shufflegagfinder)} AND (|Level 6| OR |Progressive Level:5|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)) AND (|Bart Progressive Jump:2| OR {YamlDisabled(moverandomizer)})",
        "id": 122621
    },
    {
        "name": "(LVL 6) GAG - Observatory Alarm",
        "region": "Collectables",
        "category": [
            "Level 6 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 6| OR |Progressive Level:5|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122622
    },
    {
        "name": "(LVL 6) GAG - Perpetual Motion Machine at Observatory",
        "region": "Collectables",
        "category": [
            "Level 6 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 6| OR |Progressive Level:5|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122623
    },
    {
        "name": "(LVL 6) GAG - Telescope at Observatory",
        "region": "Collectables",
        "category": [
            "Level 6 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 6| OR |Progressive Level:5|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122624
    },
    {
        "name": "(LVL 6) GAG - (Observatory) Monkey",
        "region": "Collectables",
        "category": [
            "Level 6 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 6| OR |Progressive Level:5|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122625
    },
    {
        "name": "(LVL 6) GAG - Kamp Krusty Flag",
        "region": "Collectables",
        "category": [
            "Level 6 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 6| OR |Progressive Level:5|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122626
    },
    {
        "name": "(LVL 6) GAG - Boar's Head at Kamp Krusty",
        "region": "Collectables",
        "category": [
            "Level 6 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 6| OR |Progressive Level:5|)) OR ({YamlEnabled(shufflegagfinder)} AND |Bart Gagfinder|)",
        "id": 122627
    },
    {
        "name": "(LVL 6) Shop Check 4",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:5|",
        "id": 122628
    },
    {
        "name": "(LVL 6) Shop Check 5",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:5|",
        "id": 122629
    },
    {
        "name": "(LVL 6) Shop Check 6",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:5|",
        "id": 122630
    },
    {
        "name": "(LVL 7) Shop Check 1",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:6|",
        "id": 122631
    },
    {
        "name": "(LVL 7) Shop Check 2",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:6|",
        "id": 122632
    },
    {
        "name": "(LVL 7) Shop Check 3",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:6|",
        "id": 122633
    },
    {
        "name": "(LVL 7) WASP - Blue House Haunted Playground",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122634
    },
    {
        "name": "(LVL 7) WASP - Blue House Backyard",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122635
    },
    {
        "name": "(LVL 7) WASP - Simpsons' Backyard",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122636
    },
    {
        "name": "(LVL 7) WASP - Flanders' Backyard",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122637
    },
    {
        "name": "(LVL 7) WASP - Wiggums' Backyard",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122638
    },
    {
        "name": "(LVL 7) WASP - Atop of Kwik-E-Mart",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122639
    },
    {
        "name": "(LVL 7) WASP - Atop of Gasoline",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "((|Homer Attack|) AND |Homer Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122640
    },
    {
        "name": "(LVL 7) WASP - Lard Lad Rooftop",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122641
    },
    {
        "name": "(LVL 7) WASP - Krusty Burger Rooftop",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122642
    },
    {
        "name": "(LVL 7) WASP - School playground",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122643
    },
    {
        "name": "(LVL 7) WASP - The One Being Abducted",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122644
    },
    {
        "name": "(LVL 7) WASP - School Roof 1",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "(|Homer Attack| AND |Homer Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122645
    },
    {
        "name": "(LVL 7) WASP - School Roof 2",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "(|Homer Attack| AND |Homer Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122646
    },
    {
        "name": "(LVL 7) WASP - Bridge Barricade",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122647
    },
    {
        "name": "(LVL 7) WASP - Bridge Frame by Cletus",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "((|Homer Attack|) AND |Homer Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122648
    },
    {
        "name": "(LVL 7) WASP - TrailerPark 1",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "((|Homer Attack|) AND |Homer Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122649
    },
    {
        "name": "(LVL 7) WASP - TrailerPark 2",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "((|Homer Attack|) AND |Homer Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122650
    },
    {
        "name": "(LVL 7) WASP - Barn Silo",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "((|Homer Attack|) AND |Homer Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122651
    },
    {
        "name": "(LVL 7) WASP - Power Plant Parking lot",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "|Homer Attack| OR {YamlDisabled(moverandomizer)}",
        "id": 122652
    },
    {
        "name": "(LVL 7) WASP - Mr. Burns Office",
        "region": "Collectables",
        "category": [
            "Level 7 WASP"
        ],
        "requires": "((|Homer Attack|) AND |Homer Progressive Jump:2|) OR {YamlDisabled(moverandomizer)}",
        "id": 122653
    },
    {
        "name": "(LVL 7) GAG - Simpsons TV",
        "region": "Collectables",
        "category": [
            "Level 7 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 7| OR |Progressive Level:6|)) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122661
    },
    {
        "name": "(LVL 7) GAG - Simpsons Swing",
        "region": "Collectables",
        "category": [
            "Level 7 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 7| OR |Progressive Level:6|)) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122662
    },
    {
        "name": "(LVL 7) GAG - Simpsons Fire Breathing Tiki",
        "region": "Collectables",
        "category": [
            "Level 7 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 7| OR |Progressive Level:6|)) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122663
    },
    {
        "name": "(LVL 7) GAG - Krusty Lamp (Bart's Room)",
        "region": "Collectables",
        "category": [
            "Level 7 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 7| OR |Progressive Level:6|)) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122664
    },
    {
        "name": "(LVL 7) GAG - Clown Bed (Bart's Room)",
        "region": "Collectables",
        "category": [
            "Level 7 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 7| OR |Progressive Level:6|)) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122665
    },
    {
        "name": "(LVL 7) GAG - Flanders' Bomb Shelter",
        "region": "Collectables",
        "category": [
            "Level 7 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 7| OR |Progressive Level:6|)) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122666
    },
    {
        "name": "(LVL 7) GAG - Blue House Haunted Swing",
        "region": "Collectables",
        "category": [
            "Level 7 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 7| OR |Progressive Level:6|)) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122667
    },
    {
        "name": "(LVL 7) GAG - Tank in Power Plant Parking lot",
        "region": "Collectables",
        "category": [
            "Level 7 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 7| OR |Progressive Level:6|)) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122668
    },
    {
        "name": "(LVL 7) GAG - Frozen Man in Kwik-E-Mart",
        "region": "Collectables",
        "category": [
            "Level 7 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 7| OR |Progressive Level:6|)) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122669
    },
    {
        "name": "(LVL 7) GAG - Silent Alarm in Kwik-E-Mart",
        "region": "Collectables",
        "category": [
            "Level 7 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 7| OR |Progressive Level:6|)) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122670
    },
    {
        "name": "(LVL 7) GAG - Squishee Machine in Kwik-E-Mart",
        "region": "Collectables",
        "category": [
            "Level 7 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 7| OR |Progressive Level:6|)) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122671
    },
    {
        "name": "(LVL 7) GAG - ATM in Kwik-E-Mart",
        "region": "Collectables",
        "category": [
            "Level 7 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 7| OR |Progressive Level:6|)) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122672
    },
    {
        "name": "(LVL 7) GAG - Arcade Cabinet in Kwik-E-Mart",
        "region": "Collectables",
        "category": [
            "Level 7 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 7| OR |Progressive Level:6|)) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122673
    },
    {
        "name": "(LVL 7) GAG - School Fire Extinguisher",
        "region": "Collectables",
        "category": [
            "Level 7 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 7| OR |Progressive Level:6|)) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122674
    },
    {
        "name": "(LVL 7) GAG - School Fire Alarm",
        "region": "Collectables",
        "category": [
            "Level 7 GAG"
        ],
        "requires": "({YamlDisabled(shufflegagfinder)} AND (|Level 7| OR |Progressive Level:6|)) OR ({YamlEnabled(shufflegagfinder)} AND |Homer Gagfinder|)",
        "id": 122675
    },
    {
        "name": "(LVL 7) Shop Check 4",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:6|",
        "id": 122676
    },
    {
        "name": "(LVL 7) Shop Check 5",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:6|",
        "id": 122677
    },
    {
        "name": "(LVL 7) Shop Check 6",
        "region": "Collectables",
        "category": [
            "Shop"
        ],
        "requires": "|Progressive Wallet Upgrade:6|",
        "id": 122678
    },
    {
        "name": "(LVL 1) Talk to Barney",
        "region": "Level 1",
        "category": [
            "Level 1 Mission"
        ],
        "requires": [],
        "id": 122679
    },
    {
        "name": "(LVL 2) Talk to Homer",
        "region": "Level 2",
        "category": [
            "Level 2 Mission"
        ],
        "requires": [],
        "id": 122680
    },
    {
        "name": "(LVL 3) Talk to Otto",
        "region": "Level 3",
        "category": [
            "Level 3 Mission"
        ],
        "requires": [],
        "id": 122681
    },
    {
        "name": "(LVL 4) Talk to Willie",
        "region": "Level 4",
        "category": [
            "Level 4 Mission"
        ],
        "requires": [],
        "id": 122682
    },
    {
        "name": "(LVL 5) Talk to Homer",
        "region": "Level 5",
        "category": [
            "Level 5 Mission"
        ],
        "requires": [],
        "id": 122683
    },
    {
        "name": "(LVL 6) Talk to Kearney",
        "region": "Level 6",
        "category": [
            "Level 6 Mission"
        ],
        "requires": [],
        "id": 122684
    },
    {
        "name": "(LVL 7) Talk to Graveyard Zombie",
        "region": "Level 7",
        "category": [
            "Level 7 Mission"
        ],
        "requires": [],
        "id": 122685
    },
    {
        "name": "Goal: All Missions Complete!",
        "category": [],
        "victory": True,
        "requires": "{allMissionsAccessible()} AND {collectedWasps()} AND {collectedCards()}",
        "id": 122686,
        "region": "Manual"
    },
    {
        "name": "Goal: All Story Missions Complete!",
        "category": [],
        "victory": True,
        "requires": "{allStoryMissionsAccessible()} AND {collectedWasps()} AND {collectedCards()}",
        "id": 122687,
        "region": "Manual"
    },
    {
        "name": "Goal: Final Mission(L7M7)",
        "region": "Manual",
        "category": [],
        "victory": True,
        "requires": "(|Level 7| OR |Progressive Level:6|) AND {collectedWasps()} AND {collectedCards()}",
        "id": 122688
    },
    {
        "name": "Goal: Wasps and Cards Collected!",
        "category": [],
        "victory": True,
        "requires": "{collectedWasps()} AND {collectedCards()}",
        "id": 122689,
        "region": "Manual"
    }
]

# Empty 7 length location numbers to fill with later new locations from removing cards from the middle
#card_start_ids = {
#    1: 122386,
#    2: 122433,
#    3: 122483,
#    4: 122521,
#    5: 122569,
#    6: 122610,
#    7: 122654
#}

next_id = 122692
logic_level = "carless"

for level_num in range(1, 8):
    level_name = f"Level {level_num}"
    next_id = add_cards(level_name, next_id, location_table)

for key, _ in enumerate(location_table):
    if "victory" in location_table[key] and location_table[key]["victory"]:
        victory_names.append(location_table[key]["name"])

location_id_to_name: dict[int, str] = {}
location_name_to_location: dict[str, dict] = {}
location_name_groups: dict[str, list[str]] = {}

for item in location_table:
    location_id_to_name[item["id"]] = item["name"]
    location_name_to_location[item["name"]] = item

    for c in item.get("category", []):
        if c not in location_name_groups:
            location_name_groups[c] = []
        location_name_groups[c].append(item["name"])


# location_id_to_name[None] = "__Manual Game Complete__"
location_name_to_id = {name: id for id, name in location_id_to_name.items()}



######################
# Location classes
######################


class SimpsonsHitAndRunLocation(Location):
    game = "Simpsons Hit and Run"
