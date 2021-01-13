from dataclasses import dataclass


@dataclass
class Scenario:
    name: str
    source_file: str
    steps: list
    client: list


@dataclass
class Concept:
    name: str
    steps: list
    client: list

# @dataclass
# class Step:
#     name: str
#     clientSides: str


