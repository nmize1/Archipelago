from dataclasses import dataclass

from Options import Range, PerGameCommonOptions, OptionGroup


class StarsToGoal(Range):
    """
    Number of stars required to goal.
    """
    display_name = "Stars to Goal"

    range_start = 1
    range_end = 15
    default = 10

@dataclass
class SQ64Options(PerGameCommonOptions):
    stars_to_goal: StarsToGoal

option_groups = [
    OptionGroup("Stars", [StarsToGoal])
]