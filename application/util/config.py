from dataclasses import dataclass


@dataclass
class Config:
    OUTPUT_DIR: str
    edge_labels: bool = True
    show_node_degree: bool = True
    gravity: float = -100
    font_size: int = 16
    level_separation: int = 300
    node_distance: int = 200
    show_src_file: bool = True
