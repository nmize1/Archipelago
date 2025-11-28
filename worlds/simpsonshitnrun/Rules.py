from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from worlds.generic.Rules import set_rule, add_rule
from .Regions import regionMap
from .hooks import Rules
from BaseClasses import MultiWorld, CollectionState
from .Helpers import clamp, is_item_enabled, get_items_with_value, is_option_enabled, format_to_valid_identifier, convert_string_to_type
from operator import eq, ge, le
from Options import Choice, Toggle, Range, NamedRange


import re
import math

if TYPE_CHECKING:
    from . import SimpsonsHitAndRunWorld

def infix_to_postfix(expr, location):
    prec = {"&": 2, "|": 2, "!": 3}

    stack = []
    postfix = ""

    try:
        for c in expr:
            if c.isnumeric():
                postfix += c
            elif c in prec:
                while stack and stack[-1] != "(" and prec[c] <= prec[stack[-1]]:
                    postfix += stack.pop()
                stack.append(c)
            elif c == "(":
                stack.append(c)
            elif c == ")":
                while stack and stack[-1] != "(":
                    postfix += stack.pop()
                stack.pop()
        while stack:
            postfix += stack.pop()
    except Exception:
        raise KeyError("Invalid logic format for location/region {}.".format(location))
    return postfix


def evaluate_postfix(expr: str, location: str) -> bool:
    stack = []
    try:
        for c in expr:
            if c == "0":
                stack.append(False)
            elif c == "1":
                stack.append(True)
            elif c == "&":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 and op2)
            elif c == "|":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 or op2)
            elif c == "!":
                op = stack.pop()
                stack.append(not op)
    except Exception:
        raise KeyError("Invalid logic format for location/region {}.".format(location))

    if len(stack) != 1:
        raise KeyError("Invalid logic format for location/region {}.".format(location))
    return stack.pop()

def set_rules(world: SimpsonsHitAndRunWorld, multiworld: MultiWorld, player: int):
    # this is only called when the area (think, location or region) has a "requires" field that is a string
    def checkRequireStringForArea(state: CollectionState, area: dict):
        requires_list = area["requires"]
        # Generate item_counts here so it can be access each time this is called
        if player not in world.item_counts:
            real_pool = multiworld.get_items()
            world.item_counts[player] = {i.name: real_pool.count(i) for i in real_pool if i.player == player}

        # fallback if items_counts[player] not present (will not be accurate to hooks item count)
        items_counts = world.get_item_counts()

        if requires_list == "":
            return True

        for func_name, arg_str in re.findall(r'\{(\w+)\(([^)]*)\)\}', requires_list):
            arg_str = arg_str.strip()

            # Parse arguments based on the function
            if func_name == "waspCarReq":
                # waspCarReq(Character, badcars_list_or_flag)
                if "," in arg_str:
                    first, rest = arg_str.split(",", 1)
                    func_args = [first.strip(), rest.strip()]
                else:
                    # e.g. waspCarReq(Homer) – shouldn't happen, but be defensive
                    func_args = [arg_str.strip()]
            elif func_name == "jumpsRequired":
                # jumpsRequired(Character, jumps, carsize)
                func_args = [p.strip() for p in arg_str.split(",") if p.strip() != ""]
            else:
                # Fallback: old behavior, but stripped
                func_args = [p.strip() for p in arg_str.split(",") if p.strip() != ""]

            func = globals().get(func_name) or getattr(Rules, func_name, None)
            if not callable(func):
                raise ValueError(f"Invalid function `{func_name}` in {area}.")

            result = func(world, multiworld, state, player, *func_args)

            # Replace the original {func(...)} with the result / boolean
            replacement = None
            if isinstance(result, bool):
                replacement = "1" if result else "0"
            else:
                replacement = str(result)

            requires_list = requires_list.replace(
                "{" + func_name + "(" + arg_str + ")}",
                replacement
            )

        # parse user written statement into list of each item
        for item in re.findall(r'\|[^|]+\|', requires_list):
            require_type = 'item'

            if '|@' in item:
                require_type = 'category'

            item_base = item
            item = item.lstrip('|@$').rstrip('|')

            item_parts = item.split(":")  # type: list[str]
            item_name = item
            item_count = "1"


            if len(item_parts) > 1:
                item_name = item_parts[0].strip()
                item_count = item_parts[1].strip()

            total = 0

            if require_type == 'category':
                category_items = [item for item in world.item_name_to_item.values() if "category" in item and item_name in item["category"]]
                category_items_counts = sum([items_counts.get(category_item["name"], 0) for category_item in category_items])
                if item_count.lower() == 'all':
                    item_count = category_items_counts
                elif item_count.lower() == 'half':
                    item_count = int(category_items_counts / 2)
                elif item_count.endswith('%') and len(item_count) > 1:
                    percent = clamp(float(item_count[:-1]) / 100, 0, 1)
                    item_count = math.ceil(category_items_counts * percent)
                else:
                    try:
                        item_count = int(item_count)
                    except ValueError as e:
                        raise ValueError(f"Invalid item count `{item_name}` in {area}.") from e

                for category_item in category_items:
                    total += state.count(category_item["name"], player)

                    if total >= item_count:
                        requires_list = requires_list.replace(item_base, "1")
            elif require_type == 'item':
                item_current_count = items_counts.get(item_name, 0)
                if item_count.lower() == 'all':
                    item_count = item_current_count
                elif item_count.lower() == 'half':
                    item_count = int(item_current_count / 2)
                elif item_count.endswith('%') and len(item_count) > 1:
                    percent = clamp(float(item_count[:-1]) / 100, 0, 1)
                    item_count = math.ceil(item_current_count * percent)
                else:
                    item_count = int(item_count)

                total = state.count(item_name, player)

                if total >= item_count:
                    requires_list = requires_list.replace(item_base, "1")

            if total <= item_count:
                requires_list = requires_list.replace(item_base, "0")

        requires_list = re.sub(r'\s?\bAND\b\s?', '&', requires_list, 0, re.IGNORECASE)
        requires_list = re.sub(r'\s?\bOR\b\s?', '|', requires_list, 0, re.IGNORECASE)

        requires_string = infix_to_postfix("".join(requires_list), area)
        return (evaluate_postfix(requires_string, area))

    # this is only called when the area (think, location or region) has a "requires" field that is a dict
    def checkRequireDictForArea(state: CollectionState, area: dict):
        canAccess = True

        for item in area["requires"]:
            # if the require entry is an object with "or" or a list of items, treat it as a standalone require of its own
            if (isinstance(item, dict) and "or" in item and isinstance(item["or"], list)) or (isinstance(item, list)):
                canAccessOr = True
                or_items = item

                if isinstance(item, dict):
                    or_items = item["or"]

                for or_item in or_items:
                    or_item_parts = or_item.split(":")
                    or_item_name = or_item
                    or_item_count = 1

                    if len(or_item_parts) > 1:
                        or_item_name = or_item_parts[0]
                        or_item_count = int(or_item_parts[1])

                    if not state.has(or_item_name, player, or_item_count):
                        canAccessOr = False

                if canAccessOr:
                    canAccess = True
                    break
            else:
                item_parts = item.split(":")
                item_name = item
                item_count = 1

                if len(item_parts) > 1:
                    item_name = item_parts[0]
                    item_count = int(item_parts[1])

                if not state.has(item_name, player, item_count):
                    canAccess = False

        return canAccess

    # handle any type of checking needed, then ferry the check off to a dedicated method for that check
    def fullLocationOrRegionCheck(state: CollectionState, area: dict):
        # if it's not a usable object of some sort, default to true
        if not area:
            return True

        # don't require the "requires" key for locations and regions if they don't need to use it
        if "requires" not in area.keys():
            return True

        if isinstance(area["requires"], str):
            return checkRequireStringForArea(state, area)
        else:  # item access is in dict form
            return checkRequireDictForArea(state, area)

    used_location_names = []
    # Region access rules
    for region in regionMap.keys():
        used_location_names.extend([l.name for l in multiworld.get_region(region, player).locations])
        if region != "Menu":
            for exitRegion in multiworld.get_region(region, player).exits:
                def fullRegionCheck(state: CollectionState, region=regionMap[region]):
                    return fullLocationOrRegionCheck(state, region)

                set_rule(multiworld.get_entrance(exitRegion.name, player), fullRegionCheck)

    # Location access rules
    for location in world.location_table:
        if location["name"] not in used_location_names:
            continue

        locFromWorld = multiworld.get_location(location["name"], player)

        locationRegion = regionMap[location["region"]] if "region" in location else None

        if "requires" in location: # Location has requires, check them alongside the region requires
            def checkBothLocationAndRegion(state: CollectionState, location=location, region=locationRegion):
                locationCheck = fullLocationOrRegionCheck(state, location)
                regionCheck = True # default to true unless there's a region with requires

                if region:
                    regionCheck = fullLocationOrRegionCheck(state, region)

                return locationCheck and regionCheck

            set_rule(locFromWorld, checkBothLocationAndRegion)
        elif "region" in location: # Only region access required, check the location's region's requires
            def fullRegionCheck(state, region=locationRegion):
                return fullLocationOrRegionCheck(state, region)

            set_rule(locFromWorld, fullRegionCheck)
        else: # No location region and no location requires? It's accessible.
            def allRegionsAccessible(state):
                return True

            set_rule(locFromWorld, allRegionsAccessible)

    # Victory requirement
    multiworld.completion_condition[player] = lambda state: state.has("__Victory__", player)

def YamlEnabled(world: SimpsonsHitAndRunWorld, multiworld: MultiWorld, state: CollectionState, player: int, param: str) -> bool:
    """Is a yaml option enabled?"""
    return is_option_enabled(multiworld, player, param)

def YamlDisabled(world: SimpsonsHitAndRunWorld, multiworld: MultiWorld, state: CollectionState, player: int, param: str) -> bool:
    """Is a yaml option disabled?"""
    return not is_option_enabled(multiworld, player, param)

def YamlCompare(world: SimpsonsHitAndRunWorld, multiworld: MultiWorld, state: CollectionState, player: int, args: str, skipCache: bool = False) -> bool:
    """Is a yaml option's value compared using {comparator} to the requested value
    \nFormat it like {YamlCompare(OptionName==value)}
    \nWhere == can be any of the following: ==, !=, >=, <=, <, >
    \nExample: {YamlCompare(Example_Range > 5)}"""
    comp_symbols = { #Maybe find a better name for this
        '==' : eq,
        '!=' : eq, #complement of ==
        '>=' : ge,
        '<=' : le,
        '=': eq, #Alternate to be like yaml_option
        '<' : ge, #complement of >=
        '>' : le, #complement of <=
    }

    reverse_result = False

    #Find the comparator symbol to split the string with and for logs
    if '==' in args:
        comparator = '=='
    elif '!=' in args:
        comparator = '!='
        reverse_result = True #complement of == thus reverse by default
    elif '>=' in args:
        comparator = '>='
    elif '<=' in args:
        comparator = '<='
    elif '=' in args:
        comparator = '='
    elif '<' in args:
        comparator = '<'
        reverse_result = True #complement of >=
    elif '>' in args:
        comparator = '>'
        reverse_result = True #complement of <=
    else:
        raise  ValueError(f"Could not find a valid comparator in given string '{args}', it must be one of {comp_symbols.keys()}")

    option_name, value = args.split(comparator)

    initial_option_name = str(option_name).strip() #For exception messages
    option_name = format_to_valid_identifier(option_name)

    # Detect !reversing of result like yaml_option
    if option_name.startswith('!'):
        reverse_result = not reverse_result
        option_name = option_name.lstrip('!')
        initial_option_name = initial_option_name.lstrip('!')

    value = value.strip()

    option = getattr(world.options, option_name, None)
    if option is None:
        raise ValueError(f"YamlCompare could not find an option called '{initial_option_name}' to compare against, its either missing on misspelt")

    if not value: #empty string ''
        raise ValueError(f"Could not find a valid value to compare against in given string '{args}'. \nThere must be a value to compare against after the comparator (in this case '{comparator}').")

    if not skipCache: #Cache made for optimization purposes
        cacheindex = option_name + '_' + comp_symbols[comparator].__name__ + '_' + format_to_valid_identifier(value.lower())

        if not hasattr(world, 'yaml_compare_rule_cache'):
            world.yaml_compare_rule_cache = dict[str,bool]()

    if skipCache or world.yaml_compare_rule_cache.get(cacheindex, None) is None:
        try:
            if issubclass(type(option), Choice):
                value = convert_string_to_type(value, str|int)
                if isinstance(value, str):
                    value = option.from_text(value).value

            elif issubclass(type(option), Range):
                if type(option).__base__ == NamedRange:
                    value = convert_string_to_type(value, str|int)
                    if isinstance(value, str):
                        value = option.from_text(value).value

                else:
                    value = convert_string_to_type(value, int)

            elif issubclass(type(option), Toggle):
                value = int(convert_string_to_type(value, bool))

            else:
                raise ValueError(f"YamlCompare does not currently support Option of type {type(option)} \nAsk about it in #Manual-dev and it might be added.")

        except KeyError as ex:
            raise ValueError(f"YamlCompare failed to find the requested value in what the \"{initial_option_name}\" option supports.\
                \nRaw error:\
                \n\n{type(ex).__name__}:{ex}")

        except Exception as ex:
            raise TypeError(f"YamlCompare failed to convert the requested value to what a {type(option).__base__.__name__} option supports.\
                \nCaused By:\
                \n\n{type(ex).__name__}:{ex}")

        if isinstance(value, str) and comp_symbols[comparator].__name__ != 'eq':
            #At this point if its still a string don't try and compare with strings using > < >= <=
            raise ValueError(f'YamlCompare can only compare strings with one of the following: {[s for s, v in comp_symbols.items() if v.__name__ == "eq"]} and you tried to do: "{option.value} {comparator} {value}"')

        result = comp_symbols[comparator](option.value, value)

        if not skipCache:
            world.yaml_compare_rule_cache[cacheindex] = result

    else: #if exists and not skipCache
        result = world.yaml_compare_rule_cache[cacheindex]

    return not result if reverse_result else result