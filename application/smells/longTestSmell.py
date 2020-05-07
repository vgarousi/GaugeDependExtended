from application.smells.abstractSmell import AbstractSmell
import networkx as nx
import os

# Used for test remove me !!!!
from application.graph.graph_generator import Graph_generator
from application.util.config import Config
from application.graph.graph_renderer import GraphRenderer


class LongTestSmell(AbstractSmell):

    def __init__(self, renderer):
        self.renderer = renderer

    def get_smell_name(self) -> str:
        return "Long Test: > 10 steps."

    def get_smell_id(self) -> str:
        return "LongTest"

    def get_smell_description(self) -> str:
        return "These tests have more than 10 steps, consider refactoring to make better use of concepts."

    def has_smell(self, graph) -> bool:
        out_deg = list(graph.out_degree())
        long_tests = [scenario for scenario in out_deg if scenario[1] >= 10]
        return len(long_tests) > 0

    def update_graph(self, graph) -> None:
        out_deg = list(graph.out_degree())
        long_tests = [scenario for scenario in out_deg if scenario[1] >= 10]
        for long_test in long_tests:
            graph.nodes[long_test[0]]["smell"] = True
            graph.nodes[long_test[0]]["smell_names"].append(self.get_smell_name())

    def get_smell_subgraph(self, graph) -> list:
        out_deg = list(graph.out_degree())
        long_tests = [scenario for scenario in out_deg if scenario[1] >= 10]

        output_files = list()

        for i, test in enumerate(long_tests):
            test_scenario = test[0]
            smell_graph = nx.MultiDiGraph()
            if graph.in_degree(test_scenario) > 0:
                smell_graph.add_edges_from(graph.in_edges(test_scenario, data=True))
            smell_graph.add_edges_from(graph.out_edges(test_scenario, data=True))
            for neighour in graph.neighbors(test_scenario):
                smell_graph.add_edges_from(graph.out_edges(neighour, data=True))
                for other in graph.neighbors(neighour):
                    smell_graph.add_edges_from(graph.out_edges(other, data=True))

            nx.set_node_attributes(smell_graph, False, "smell")
            nx.set_node_attributes(smell_graph, list(), "smell_names")

            self.renderer.render_graph(smell_graph, f"long-test-smell-{i}.html")
            output_files.append(f"./long-test-smell-{i}.html")

        return output_files


# To test the smell sub-graph function run this file then inspect generated graph.
if __name__ == "__main__":
    config = Config(OUTPUT_DIR=os.path.join(os.path.dirname(__file__), "..", "..", "output"), show_src_file=False,
                    edge_labels=False)
    renderer = GraphRenderer(config)
    smell = LongTestSmell(renderer)
    generator = Graph_generator(config)
    # data/test_smells/long_test_smell.spec
    graph_filename = generator.generate_spec_graph(
        os.path.join(os.path.dirname(__file__), "..", "..", "data", "test_smells", "long_test_smell.spec"))
    test_graph = nx.read_yaml(os.path.join(config.OUTPUT_DIR, f"{graph_filename}.yaml"))

    smell.update_graph(test_graph)

    renderer.render_graph(test_graph)
