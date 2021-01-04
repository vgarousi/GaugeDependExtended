from dataclasses import dataclass


@dataclass
class Scenario:
    name: str
    source_file: str
    steps: list


@dataclass
class Concept:
    name: str
    steps: list
