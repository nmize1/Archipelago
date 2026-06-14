from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups

class SQ64WebWorld(WebWorld):

    game = "Star Quest 64"

    theme = "partyTime"

    setup_en = Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up APQuest for MultiWorld.",
            "English",
            "setup_en.md",
            "setup/en",
            ["Caesius"])

    tutorials = [setup_en]

    option_groups = option_groups