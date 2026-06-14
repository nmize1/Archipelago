from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.field_resolvers import FromOption
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule, FieldResolver
from .options import StarsToGoal

if TYPE_CHECKING:
    from .world import SQ64World

can_jump = Has("Progressive Jump")
can_double_jump = Has("Progressive Jump", 2)
can_wall_jump = Has("Wall Jump")
can_spin = Has("Spin")
can_dive = Has("Dive")
can_backflip = Has("Backflip")
can_glide = Has("Glide")
can_dash = Has("Dash")
can_swim = Has("Swim")
can_ground_pound = Has("Ground Pound")
can_extend_jump = can_double_jump | can_spin | can_dash | can_glide
can_attack = can_jump | can_spin

can_hub_box = Has("HUB: Box Button")
can_l1_box = Has("L1: Box Button")
can_l1_portal = Has("L1: Portals")

can_access_l1 = Has("Level 1")

def set_all_rules(world: SQ64World) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: SQ64World) -> None:
    hub_to_l1 = world.get_entrance("HUB to L1")
    hub_boxes = world.get_entrance("HUB to HUB Boxes")
    hub_enemies = world.get_entrance("HUB to HUB Enemies")

    l1_boxes = world.get_entrance("L1 to L1 Boxes")
    l1_enemies = world.get_entrance("L1 to L1 Enemies")


    world.set_rule(hub_to_l1, can_access_l1)
    world.set_rule(hub_boxes, can_jump | can_backflip)
    world.set_rule(hub_enemies, can_attack)
    world.set_rule(l1_boxes, can_jump | can_backflip)
    world.set_rule(l1_enemies, can_attack)

def set_all_location_rules(world: SQ64World) -> None:
    #hub
    l2star = world.get_location("HUB: L2 Star")
    l3star = world.get_location("HUB: L3 Star")
    l4star = world.get_location("HUB: L4 Star")
    hub_red_star = world.get_location("HUB: Red Coin Star")
    hub_life = world.get_location("HUB: Tower Extra Life")

    #l1
    boss_slime_star = world.get_location("L1: Defeat Boss Slime Star")
    precarious_star = world.get_location("L1: Precarious Platforms Star")
    secret_star = world.get_location("L1: The Tower's Secret Star")
    cave_star = world.get_location("L1: Red Coins in the Cave Star")
    l1_80_star = world.get_location("L1: 80 Coin Star")
    l1_short_cliff_box = world.get_location("L1: Coin Box on Shortest Cliff")
    l1_tower_box = world.get_location("L1: Coin Box on Tower Ramp Balcony")
    l1_boss_life = world.get_location("L1: Boss Cliff Extra Life")
    l1_2d_life = world.get_location("L1: 2D Extra Life")

    world.set_rule(l2star, can_jump)
    world.set_rule(l3star, can_swim & can_ground_pound)
    world.set_rule(l4star, can_jump)
    world.set_rule(hub_red_star, can_double_jump & can_wall_jump & can_hub_box)
    world.set_rule(hub_life, can_double_jump)

    world.set_rule(boss_slime_star, can_double_jump & can_wall_jump & can_extend_jump)
    world.set_rule(secret_star, can_ground_pound & can_jump & can_wall_jump & can_l1_portal & can_extend_jump)
    world.set_rule(precarious_star, can_jump & can_wall_jump & can_extend_jump)
    world.set_rule(cave_star, can_jump & can_glide & can_l1_portal)
    world.set_rule(l1_80_star, can_jump & can_ground_pound & can_l1_portal & can_glide & can_l1_box)

    world.set_rule(l1_tower_box, can_wall_jump)
    world.set_rule(l1_short_cliff_box, can_l1_box)

    world.set_rule(l1_boss_life, can_double_jump & can_wall_jump & can_extend_jump)
    world.set_rule(l1_2d_life, can_ground_pound & can_jump & can_wall_jump & can_l1_portal & can_extend_jump)

def set_completion_condition(world: SQ64World) -> None:
    star_count = Has("Star", FromOption(StarsToGoal))
    world.set_completion_rule(star_count)

