# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#

class LevelSanity(Choice):
    """Choose how you want missions to be sent in the multiworld. Levels logically require the level access item and at least 1 car from that level or higher. You're guaranteed to start with a level and it's default car with either option.
       Linear will remove levels from the pool. Instead, you will start at the tutorial mission and play through the game in order. LxM7 will always reward you the next level instead of a random item. You'll still need to find a car from the next level.
       Levels will add levels to the pool. You'll start the game with a random level and it's required items and receive levels from the multiworld. Missions will still be played in order for each level.
       """
    display_name = "Levelsanity"
    option_linear = 0
    option_levels = 1
    default = 1

class MoveRando(Toggle):
    """Choose whether or not to shuffle moves into the item pool.
       Moves that are shuffled are Double Jump, Kick, and Ground Pound
       and have logical implications for wasp and card collection.
       """

    display_name = "Move Randomizer"

class WaspPercent(Range):
    """ Percent of Wasps required to goal. If your goal is not Wasps and Cards, then this will be in addition to your goal."""
    display_name = "Required Wasp Percent"
    range_start = 0
    range_end = 100
    default = 50

class CardPercent(Range):
    """Percent of Cards required to goal. If your goal is not Wasps and Cards, then this will be in addition to your goal."""
    display_name = "Required Card Percent"
    range_start = 0
    range_end = 100
    default = 50



# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["levelsanity"] = LevelSanity
    options["moverandomizer"] = MoveRando
    options["wasppercent"] = WaspPercent
    options["cardpercent"] = CardPercent
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options
