from application.smells.abstractSmell import AbstractSmell
import networkx as nx


class SelfReferencingCptSmell(AbstractSmell):
    def __init__(self, renderer):
        self.renderer = renderer

    def get_smell_name(self) -> str:
        return "Self referencing concept"

    def get_smell_id(self) -> str:
        return "selfReferencing"

    def get_smell_description(self) -> str:
        return "This concept calls itself"

    def has_smell(self, graph) -> bool:
        outdegrees = list(graph.out_degree())
        cpts = [node for node in outdegrees if node[0].startswith("Step:") and node[1] > 0]

        for concept in cpts:
            edges = graph.out_edges(concept[0])
            if (concept[0], concept[0]) in edges:
                return True
        return False

    def get_smell_subgraph(self, graph) -> list:
        outdegrees = list(graph.out_degree())
        cpts = [node for node in outdegrees if node[0].startswith("Step:") and node[1] > 0]

        self_referencing_cpts = list()

        for concept in cpts:
            edges = graph.out_edges(concept[0])
            if (concept[0], concept[0]) in edges:
                self_referencing_cpts.append(concept[0])

        output_files = list()

        for i, concept in enumerate(self_referencing_cpts):
            node = concept
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

            self.renderer.render_graph(smell_graph, f"self-referencing-smell-{i}.html")
            output_files.append(f"./self-referencing-smell-{i}.html")

        return output_files

    def update_graph(self, graph) -> None:
        outdegrees = list(graph.out_degree())
        cpts = [node for node in outdegrees if node[0].startswith("Step:") and node[1] > 0]

        for concept in cpts:
            edges = graph.out_edges(concept[0])
            if (concept[0], concept[0]) in edges:
                graph.nodes[concept[0]]["smell"] = True
                graph.nodes[concept[0]]["smell_names"].append(self.get_smell_name())
