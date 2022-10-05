from typing import Generator


def file_reader(file_path: str) -> Generator[str, None, None]:
    with open(file_path) as file:
        for line in file.readlines():
            yield line
