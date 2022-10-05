from typing import Union, Generator, Callable, Dict, Optional
from .functions import my_filter, my_map, my_unique, my_sort, my_limit, my_regex

def command_processor(cmd1_name: str,
                      value1: str,
                      cmd2_name: Optional[str],
                      value2: Optional[str],
                      data: Generator
                      ) -> list:
    commands: Dict[str, Callable] = {
        'filter': my_filter,
        'map': my_map,
        'unique': my_unique,
        'sort': my_sort,
        'limit': my_limit,
        'regex': my_regex,
    }

    cmd1: Callable = commands[cmd1_name]
    cmd1_result = cmd1(data, value1)

    if not cmd2_name:
        return cmd1_result

    cmd2 = commands[cmd2_name]
    cmd2_result = cmd2(cmd1_result, value2)
    return cmd2_result
