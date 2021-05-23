from application.smells.abstractSmell import AbstractSmell
import networkx as nx

class LongStepName(AbstractSmell):
    def __init__(self, renderer):
        self.renderer = renderer

    def get_smell_name(self) -> str:
        return "Long Step name > 120 characters"

    def get_smell_id(self) -> str:
        return "long_step"

    def get_smell_description(self) -> str:
        return "This step/scenario name is over 120 characters consider using more concise language when naming steps or refactoring into multiple tests/ steps"

    def has_smell(self, graph) -> bool:
        all_nodes = graph.nodes()
        smell_nodes = [node for node in all_nodes if len(node) > 120]
        return len(smell_nodes)>0

    def get_smell_subgraph(self, graph) -> list:
        all_nodes = graph.nodes()
        smell_nodes = [node for node in all_nodes if len(node) > 120]
        
        output_files = list()
        
        for i, node in enumerate(smell_nodes):
            smell_graph = nx.MultiDiGraph()
            if graph.in_degree(node) > 0:
                smell_graph.add_edges_from(graph.in_edges(node, data=True))
            smell_graph.add_edges_from(graph.out_edges(node, data=True))
            for neighour in graph.neighbors(node):
                smell_graph.add_edges_from(graph.out_edges(neighour, data=True))
                for other in graph.neighbors(neighour):
                    smell_graph.add_edges_from(graph.out_edges(other, data=True))

            nx.set_node_attributes(smell_graph, False, "smell")
            nx.set_node_attributes(smell_graph, list(), "smell_names")

            self.renderer.render_graph(smell_graph, f"long-name-smell-{i}.html")
            output_files.append(f"./long-name-smell-{i}.html")

        return output_files
        

    def update_graph(self, graph) -> None:
        all_nodes = graph.nodes()
        smell_nodes = [node for node in all_nodes if len(node) > 120]
        for node in smell_nodes:
            graph.nodes[node]["smell"] = True
            graph.nodes[node]["smell_names"].append(self.get_smell_name())

