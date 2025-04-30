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
       Moves that are shuffled are Double Jump and Attack for each character.
       These have logical implications for wasp and card collection
       as well as L7M4 requiring Homer Double Jump.
       """

    default = True
    display_name = "Move Randomizer"

class ShuffleEBrakes(Toggle):
    """Choose whether or not to shuffle ability to use the E-Brake
       for each character into the item pool. *WARNING* This is not
       considered in logic and has not been heavily tested.
       It may create unreasonably hard seeds.
       """

    default = True
    display_name = "Shuffle E-Brake"

class EnableWaspPercent(Toggle):
    """Whether to include Wasps in goal requirements.
       This setting is always treated as true if your
       goal is Goal: Wasps and Cards Collected!"""

    default = True
    display_name = "Enable Wasp Requirements"

class WaspPercent(Range):
    """ Percent of Wasps required to goal if Wasp Requirements is enabled."""
    display_name = "Required Wasp Percent"
    range_start = 10
    range_end = 100
    default = 50

class EnableCardPercent(Toggle):
    """Whether to include Cards in goal requirements.
       This setting is always treated as true if your
       goal is Goal: Wasps and Cards Collected!"""

    default = True
    display_name = "Enable Card Requirements"

class CardPercent(Range):
    """Percent of Cards required to goal if Card Requirements is enabled."""
    display_name = "Required Card Percent"
    range_start = 10
    range_end = 100
    default = 50

class MinShopPrice(Range):
    """The minimum cost of any item in Gil's Shop. If this is greater than the max shop price, then the max will be used instead."""
    display_name = "Min Shop Price"
    range_start = 0
    range_end = 1000
    default = 100

class MaxShopPrice(Range):
    """The maximum cost of any item in Gil's Shop."""
    display_name = "Max Shop Price"
    range_start = 0
    range_end = 500
    default = 300

class ShopScaleMod(Range):
    """The multiplier for shop costs per levels
       L2 costs = L1 * multiplier, L3 = L1 * 2(multiplier), etc"""
    display_name = "Shop Price Level Scale Multiplier"
    range_start = 1
    range_end = 5
    default = 2




# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["levelsanity"] = LevelSanity
    options["moverandomizer"] = MoveRando
    options["shuffleebrake"] = ShuffleEBrakes
    options["EnableWaspPercent"] = EnableWaspPercent
    options["wasppercent"] = WaspPercent
    options["EnableCardPercent"] = EnableCardPercent
    options["cardpercent"] = CardPercent
    options["minprice"] = MinShopPrice
    options["maxprice"] = MaxShopPrice
    options["shopscalemod"] = ShopScaleMod
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options
