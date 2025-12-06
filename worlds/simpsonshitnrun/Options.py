from dataclasses import dataclass
from Options import (Toggle, Choice, Range, OptionSet, PerGameCommonOptions, DeathLink)

VALID_CHAR_KEYS = ["Homer", "Bart", "Lisa", "Marge", "Apu", "All", "None"]

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

class ShuffleAttack(OptionSet):
    """Choose whether to add Attack to the pool for each character.
       Valid options are Homer, Bart, Lisa, Marge, Apu, All, or None.
    """

    default = frozenset({"All"})
    valid_keys = VALID_CHAR_KEYS
    display_name = "Shuffle Attack"

class ShuffleJump(OptionSet):
    """Choose whether to add Jump to the pool for each character.
       Valid options are Homer, Bart, Lisa, Marge, Apu, All, or None.
    """

    default = frozenset({"All"})
    valid_keys = VALID_CHAR_KEYS
    display_name = "Shuffle Jump"

class StartingJumpLevel(Range):
    """Choose how many Progressive Jump items to start with for each character.
       Characters who aren't included in ShuffleJump will start with Progressive Jump Level 2.
    """
    display_name = "Starting Jump Level"
    range_start = 0
    range_end = 2
    default = 1

class ShuffleGagfinder(OptionSet):
    """Choose whether to add a Gagfinder to the pool for each Character that will be required to
       unlock gags as that character. Valid options are Homer, Bart, Lisa, Marge, Apu, All, or None.
       If None, gags will instead be locked until you receive their Level.
       """

    default = frozenset({"All"})
    valid_keys = VALID_CHAR_KEYS
    display_name = "Shuffle Gagfinder"

class ShuffleCheckeredFlags(OptionSet):
    """Choose whether to add a Checkered Flag to the pool for each Character that will be required to
       unlock races as that character. Valid options are Homer, Bart, Lisa, Marge, Apu, All, or None.
       If None, races will instead be locked until you receive their Level.
       """

    default = frozenset({"All"})
    valid_keys = VALID_CHAR_KEYS
    display_name = "Shuffle Checkered Flags"

class ShuffleForward(OptionSet):
    """Choose whether to shuffle the ability to move forward or drive forward for each character into the item pool.
       Valid options are Homer, Bart, Lisa, Marge, Apu, All, or None.
       **THIS COULD CREATE VERY DIFFICULT SEEDS**
    """

    default = frozenset({"None"})
    valid_keys = VALID_CHAR_KEYS
    display_name = "Shuffle Forward"

class EarlyForward(OptionSet):
    """If enabled and forward is shuffled, try to place each specified character's Forward item early.
       Valid options are Homer, Bart, Lisa, Marge, Apu, All, or None. Does nothing if the character's forward isn't shuffled.
    """

    default = frozenset({"All"})
    valid_keys = VALID_CHAR_KEYS
    display_name = "Early Forward"

class ShuffleEBrakes(OptionSet):
    """Choose whether to shuffle ability to use the E-Brake for each character into the item pool.
       """

    default = frozenset({"All"})
    valid_keys = VALID_CHAR_KEYS
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
       ***CURRENTLY GLITCHED LOGIC LEVEL IS NOT SUPPORTED AND WILL RAISE AN ERROR AND FAIL GENERATION"""

    display_name = "Card Logic"
    option_carless = 0
    option_cars = 1
    option_glitched = 2
    default = 0

class WaspLogic(Choice):
    """Choose logic level for wasps.
       Strict: Wasps cannot be broken with cars and logically require Attack items.
       Unlockable: Adds a "Frink-o-Matic Wasp Bumper" item for each character that allows them to break wasps with cars.
                   Wasps logically require the bumper and a car that can reach them or Attack items.
       Cars: Wasps logically require a car that can reach them or Attack items.
       Open: Wasps logically require Attack items but can be broken with cars."""

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

class ShopScaleMod(Range):
    """The multiplier for shop costs per levels
       L2 costs = L1 * multiplier, L3 = L1 * 2(multiplier), etc"""
    display_name = "Shop Price Level Scale Multiplier"
    range_start = 1
    range_end = 5
    default = 2

class ShopHintPolicy(Choice):
    """Choose the level of hints sent when speaking to Gil for the first time on a level
       All: Hint all items in Gil's shop
       OnlyProg: Only hint progression items in Gil's shop
       None: No shop hints will be created
    """
    display_name = "Shop Hint Policy"
    option_all = 0
    option_onlyprog = 1
    option_none = 2

class ExtraHintPolicy(Toggle):
    """Place extra hints in various places."""
    default = True
    display_name = "Extra Hint Policy"

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
    shuffleattack: ShuffleAttack
    shufflejump: ShuffleJump
    startjumplevel: StartingJumpLevel
    shufflegagfinder: ShuffleGagfinder
    shufflecheckeredflags: ShuffleCheckeredFlags
    shuffleebrake: ShuffleEBrakes
    shuffleforward: ShuffleForward
    earlyforward: EarlyForward
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
    extrahintpolicy: ExtraHintPolicy
    shuffletraffic: ShuffleTraffic
    filler_traps: FillerTrapPercent
    eject: EjectTraps
    duff: DuffTraps
    launch: LaunchTraps
    hnr: HNRTraps
    traffictrap: TrafficTraps


SimpsonsHitAndRunOptions = SimpsonsHitAndRunOptions
