from dataclasses import dataclass
from Options import (Toggle, Choice, Range, PerGameCommonOptions, DeathLink)

class FillerTrapPercent(Range):
    """How many fillers will be replaced with traps. 0 means no additional traps, 100 means all fillers are traps."""
    display_name = "Filler Traps"
    range_end = 100


class Goal(Choice):
    """Choose your victory condition."""
    display_name = "Goal"
    default = 0
    option_goal_all_missions_complete = 0
    option_goal_all_story_missions_complete = 1
    option_goal_final_missionl7m7 = 2
    option_goal_wasps_and_cards_collected = 3


class LevelSanity(Choice):
    """Choose how you want missions to be sent in the multiworld. Levels logically
       require the level access item and at least 1 car from that level or higher.
       You're guaranteed to start with a level and it's default car with either option.
       Linear will add progressive levels to the pool. You'll start with Level 1 and
       the Family Sedan, then get the next level each time you receive a progressive
       level item. Levels will add levels to the pool. You'll start the game with
       a random level and it's required items and receive levels from the multiworld.
       Regardless of your choice, missions can be played in any order on an unlocked level.
       """
    display_name = "Levelsanity"
    option_linear = 0
    option_levels = 1
    default = 1

class ShuffleStartingCar(Toggle):
    """Choose whether to shuffle starting car between available cars from your starting level.
       If disabled, you'll always start with your starting level's default car.
        """
    display_name = "Shuffle Starting Car"
    default = True

class MoveRando(Toggle):
    """Choose whether to shuffle moves into the item pool.
       Moves that are shuffled are Double Jump and Attack for each character.
       These have logical implications for wasp and card collection
       as well as L7M4 requiring Homer Double Jump.
       """

    default = True
    display_name = "Move Randomizer"

class StartingJumpLevel(Range):
    """Choose how many Progressive Jump items to start with for each character.
       This option is always 2 if MoveRando is False. CARD LOGIC IS CURRENTLY INCORRECT
       IF STARTING WITH 0 JUMPS"""
    display_name = "Starting Jump Level"
    range_start = 0
    range_end = 2
    default = 1

class ShuffleGagfinder(Toggle):
    """If enabled, add a Gagfinder to the pool for each Character that will be
       required to unlock gags as that character. If disabled, gags will instead
       be locked until you receive their Level.
       """

    default = True
    display_name = "Shuffle Gagfinder"

class ShuffleCheckeredFlags(Toggle):
    """If enabled, add a Checkered Flag to the pool for each Character that will be
       required to unlock races as that character. If disabled, races will instead
       be locked until you receive their Level.
       """

    default = True
    display_name = "Shuffle Checkered Flags"

class ShuffleEBrakes(Toggle):
    """Choose whether to shuffle ability to use the E-Brake
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

class ShuffleCards(Toggle):
    """Randomize card locations. This option adds several possible locations for
       cards. There will still be 49 total cards with 7 in each level."""

    default = True
    display_name = "Shuffle Cards"

class CardLogic(Choice):
    """Choose logic level for cards.
       Carless: Cars are not considered at all in this logic level and cards that cannot be reached without them
                are not available locations for ShuffleCards.
                Note that the card on Level 6 that requires the Itchy and Scratchy Truck will still require it if ShuffleCards is false.
       Cars: Cars are considered in whether you can reach a card.
       Glitched: Glitches and speedrunning tricks are considered in whether you can reach a card.
       ***CURRENTLY ONLY CARLESS LOGIC LEVEL IS SUPPORTED, OTHER OPTIONS WILL RAISE AN ERROR AND FAIL GENERATION"""

    display_name = "Card Logic"
    option_carless = 0
    option_cars = 1
    option_glitched = 2
    default = 0

class WaspLogic(Choice):
    """Choose logic level for wasps.
       Strict: Wasps cannot be broken with cars.
       Unlockable: Adds a "Frink-o-Matic Wasp Bumper" item for each character that allows them to break wasps with cars and logic considers your available cars. - NOT IMPLEMENTED YET.
       Cars: Wasps logic considers your available cars. - NOT IMPLEMENTED YET
       Open: Wasps are not in logic without Attack items but can be broken with cars."""

    display_name = "Wasp Logic"
    option_strict = 0
    option_unlockable = 1
    option_cars = 2
    option_open = 3

class AddMissionLocks(Range):
    """Add car requirements to a percentage of missions"""

    display_name = "Mission Locks"
    range_start = 0
    range_end = 100

class MinShopPrice(Range):
    """The minimum cost of any item in Gil's Shop. If this is greater than the max shop price, then the max will be used instead."""
    display_name = "Min Shop Price"
    range_start = 0
    range_end = 500
    default = 100

class MaxShopPrice(Range):
    """The maximum cost of any item in Gil's Shop."""
    display_name = "Max Shop Price"
    range_start = 0
    range_end = 500
    default = 300

class ShopHintPolicy(Choice):
    """Choose the level of hints sent when speaking to Gil for the first time on a level
       All: Hint all items in Gil's shop
       OnlyProg: Only hint progression items in Gil's shop
    """
    display_name = "Shop Hint Policy"
    option_all = 0
    option_onlyprog = 1

class ShopScaleMod(Range):
    """The multiplier for shop costs per levels
       L2 costs = L1 * multiplier, L3 = L1 * 2(multiplier), etc"""
    display_name = "Shop Price Level Scale Multiplier"
    range_start = 1
    range_end = 5
    default = 2

class ShuffleTraffic(Toggle):
    """Randomize traffic per level"""
    default = True
    display_name = "Shuffle Traffic"

class EjectTraps(Toggle):
    """Whether to include Eject traps in the item pool."""
    default = True
    display_name = "Enable Eject Traps"

class DuffTraps(Toggle):
    """Whether to include Duff traps in the item pool."""
    default = True
    display_name = "Enable Duff Traps"

class LaunchTraps(Toggle):
    """Whether to include Launch traps in the item pool."""
    default = True
    display_name = "Enable Launch Traps"

class HNRTraps(Toggle):
    """Whether to include Hit N Run traps in the item pool."""
    default = True
    display_name = "Enable Hit N Run Traps"

class TrafficTraps(Toggle):
    """Whether to include Traffic traps in the item pool."""
    default = True
    display_name = "Enable Traffic Traps"

@dataclass
class SimpsonsHitAndRunOptions(PerGameCommonOptions):
    goal: Goal
    levelsanity: LevelSanity
    startingcarshuffle: ShuffleStartingCar
    moverandomizer: MoveRando
    startjumplevel: StartingJumpLevel
    shufflegagfinder: ShuffleGagfinder
    shufflecheckeredflags: ShuffleCheckeredFlags
    shuffleebrake: ShuffleEBrakes
    EnableWaspPercent: EnableWaspPercent
    wasppercent: WaspPercent
    EnableCardPercent: EnableCardPercent
    cardpercent: CardPercent
    shufflecards: ShuffleCards
    cardlogic: CardLogic
    wasplogic: WaspLogic
    missionlocks: AddMissionLocks
    minprice: MinShopPrice
    maxprice: MaxShopPrice
    shopscalemod: ShopScaleMod
    shophintpolicy: ShopHintPolicy
    shuffletraffic: ShuffleTraffic
    filler_traps: FillerTrapPercent
    eject: EjectTraps
    duff: DuffTraps
    launch: LaunchTraps
    hnr: HNRTraps
    traffictrap: TrafficTraps


SimpsonsHitAndRunOptions = SimpsonsHitAndRunOptions
