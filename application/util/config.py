from dataclasses import dataclass


@dataclass
class Config:
    OUTPUT_DIR: str
    heading: str = ""
    rpath: str = ""
    edge_labels: bool = True
    physics: bool = True
    show_node_degree: bool = True
    gravity: float = -100
    font_size: int = 16
    level_separation: int = 400
    node_distance: int = 150
    show_src_file: bool = True