from dataclasses import dataclass


@dataclass
class Scenario:
    name: str
    source_file: str
    steps: list
    web: list = None


@dataclass
class Concept:
    name: str
    steps: list
    web: list = None

@dataclass
class ClientObjects:
    keys: list
    values: list
    types: list

# @dataclass
# class Step:
#     name: str
#     clientSides: str


