from dataclasses import dataclass


@dataclass
class Config:
    OUTPUT_DIR: str
    edge_labels: bool = True
    show_node_degree: bool = True
    font_size: int = 16
    level_separation: int = 1000
    node_spacing: int = 100
    show_src_file: bool = True
