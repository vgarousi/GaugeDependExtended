import unittest
import os
import networkx as nx

from application.graph.graph_renderer import GraphRenderer
from application.util.config import Config
from application.graph.graph_generator import Graph_generator
from application.smells.longTestSmell import LongTestSmell
from tests.test_config import *

NORMAL_TEST_SPEC_PATH = os.path.join(RESOURCE_DIR, "test_specification.spec")
SMELL_TEST_SPEC_PATH = os.path.join(RESOURCE_DIR, "long_test_smell.spec")


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config(OUTPUT_DIR=OUTPUT_DIR, show_src_file=False, edge_labels=False)
        self.renderer = GraphRenderer(config=self.config)
        self.generator = Graph_generator(config=self.config)
        self.smell = LongTestSmell(renderer=self.renderer)

        if not os.path.isdir(OUTPUT_DIR):
            os.mkdir(OUTPUT_DIR)

    def tearDown(self) -> None:
        for filename in os.listdir(self.config.OUTPUT_DIR):
            file_path = os.path.join(self.config.OUTPUT_DIR, filename)
            if file_path.endswith(".yaml") or file_path.endswith(".html"):
                os.unlink(file_path)

    def test_spec_does_not_have_smell(self):
        graph_name = self.generator.generate_spec_graph(NORMAL_TEST_SPEC_PATH)
        graph = nx.read_yaml(f"{self.config.OUTPUT_DIR}/{graph_name}.yaml")
        self.assertFalse(self.smell.has_smell(graph))

    def test_spec_has_smell(self):
        graph_name = self.generator.generate_spec_graph(SMELL_TEST_SPEC_PATH)
        graph = nx.read_yaml(f"{self.config.OUTPUT_DIR}/{graph_name}.yaml")
        self.assertTrue(self.smell.has_smell(graph))

    def test_correct_number_of_smells(self):
        graph_name = self.generator.generate_spec_graph(SMELL_TEST_SPEC_PATH)
        graph = nx.read_yaml(f"{self.config.OUTPUT_DIR}/{graph_name}.yaml")
        output_files = self.smell.get_smell_subgraph(graph)
        self.assertEqual(len(output_files), 1)

    def test_uptdate_graph(self):
        graph_name = self.generator.generate_spec_graph(SMELL_TEST_SPEC_PATH)
        graph = nx.read_yaml(f"{self.config.OUTPUT_DIR}/{graph_name}.yaml")
        self.smell.update_graph(graph)

        self.assertTrue(graph.nodes["Scenario:Long Test"]["smell"])
        self.assertEqual(graph.nodes["Scenario:Long Test"]["smell_names"], ["Long Test: > 10 steps."])


if __name__ == '__main__':
    unittest.main()
