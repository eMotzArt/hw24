import re
from typing import Generator, Union


def my_filter(data: Generator, searched_text: str) -> list:
    res = filter(lambda line: searched_text in line, data)
    return list(res)

def my_map(data: Generator, col_num: Union[str, int]) -> list:
    res = map(lambda line: line.split(' ')[int(col_num)], data)
    return list(res)

def my_unique(data: Generator, *args: tuple) -> list:
    return list(set(data))

def my_sort(data: Generator, type: str) -> list:
    return sorted(data, reverse=True) if type.lower() == 'desc' else sorted(data)

def my_limit(data: Generator, count: str) -> list:
    return list(data)[:int(count)]

def my_regex(data: Generator, regex: str) -> list:
    compiled_regex = re.compile(regex)
    return [line for line in data if compiled_regex.findall(line)]
