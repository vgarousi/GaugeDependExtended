import unittest
import networkx as nx
import os
from application.graph.graph_generator import Graph_generator
from application.util.config import Config
from tests.test_config import *

TEST_SPEC_PATH = os.path.join(RESOURCE_DIR, "test_specification.spec")
TEST_SPEC_PATH_CPT = os.path.join(RESOURCE_DIR, "test_spec_with_concept.spec")
TEST_CPT_PATH = os.path.join(RESOURCE_DIR, "test_concept.cpt")
NEW_TEST_SPEC_PATH = os.path.join(RESOURCE_DIR, "updated_test_specification.spec")
NEW_TEST_CPT_PATH = os.path.join(RESOURCE_DIR, "updated_test_concept.cpt")
RESOURCE_PATH = os.path.join(RESOURCE_DIR, "testElements/resourceTest.json")

class GraphGeneratorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config(OUTPUT_DIR=OUTPUT_DIR)
        self.generator = Graph_generator(self.config)

        if not os.path.isdir(OUTPUT_DIR):
            os.mkdir(OUTPUT_DIR)

    def tearDown(self) -> None:
        for filename in os.listdir(self.config.OUTPUT_DIR):
            file_path = os.path.join(self.config.OUTPUT_DIR, filename)
            if file_path.endswith(".yaml") or file_path.endswith(".html"):
                os.unlink(file_path)

    def test_generate_spec_graph(self):
        output_file = self.generator.generate_spec_graph(TEST_SPEC_PATH)
        output_graph = nx.read_yaml(f"{OUTPUT_DIR}/{output_file}.yaml")
        nodes = list(output_graph.nodes())
        self.assertEqual(len(nodes), 6)

        expected_nodes = ['Scenario:Scenario 1', 'Scenario:Scenario 2', 'Step:Step 1', 'Step:Step 2', 'Step:Step 3',
                          'Step:Step with $Variable$']

        expected_nodes.sort()
        nodes.sort()

        self.assertEqual(nodes, expected_nodes)

        edges = list(output_graph.edges())
        expected_edges = [
            ("Scenario:Scenario 1", "Step:Step 1"),
            ("Scenario:Scenario 1", "Step:Step 2"),
            ("Scenario:Scenario 1", "Step:Step 3"),
            ("Scenario:Scenario 2", "Step:Step with $Variable$"),
            ("Scenario:Scenario 2", "Step:Step 2"),
            ("Scenario:Scenario 2", "Step:Step 3")
        ]

        edges.sort(key=lambda edge: edge[0] + edge[1])
        expected_edges.sort(key=lambda edge: edge[0] + edge[1])

        self.assertEqual(edges, expected_edges)


    def test_generate_concept_graph(self):
        output_file = self.generator.generate_cpt_graph(TEST_CPT_PATH)
        output_graph = nx.read_yaml(f"{OUTPUT_DIR}/{output_file}.yaml")
        nodes = list(output_graph.nodes())

        self.assertEqual(len(nodes), 4)

        expected_nodes = [
            "Step:Test Concept",
            "Step:Step 1",
            "Step:Step 2",
            "Step:Step 3"
        ]

        expected_nodes.sort()
        nodes.sort()

        self.assertEqual(nodes, expected_nodes)

        edges = list(output_graph.edges())
        expected_edges = [
            ("Step:Test Concept", "Step:Step 1"),
            ("Step:Test Concept", "Step:Step 2"),
            ("Step:Test Concept", "Step:Step 3")
        ]

        edges.sort(key=lambda edge: edge[0] + edge[1])
        expected_edges.sort(key=lambda edge: edge[0] + edge[1])

        self.assertEqual(edges, expected_edges)

    def test_scenarios_have_source_files(self):
        output_file = self.generator.generate_spec_graph(TEST_SPEC_PATH)
        output_graph = nx.read_yaml(f"{OUTPUT_DIR}/{output_file}.yaml")
        self.assertEqual(output_graph.nodes["Scenario:Scenario 1"]["source_file"], "test_specification.spec")
        self.assertEqual(output_graph.nodes["Scenario:Scenario 2"]["source_file"], "test_specification.spec")

    def test_edge_labels(self):
        output_file = self.generator.generate_spec_graph(TEST_SPEC_PATH)
        output_graph = nx.read_yaml(f"{OUTPUT_DIR}/{output_file}.yaml")
        edges = list(output_graph.edges(data=True))
        expected_edges = [
            ("Scenario:Scenario 1", "Step:Step 1", {"label": 1}),
            ("Scenario:Scenario 1", "Step:Step 2", {"label": 2}),
            ("Scenario:Scenario 1", "Step:Step 3", {"label": 3}),
            ("Scenario:Scenario 2", "Step:Step with $Variable$", {"label": 1}),
            ("Scenario:Scenario 2", "Step:Step 2", {"label": 2}),
            ("Scenario:Scenario 2", "Step:Step 3", {"label": 3})
        ]

        edges.sort(key=lambda edge: edge[0] + edge[1])
        expected_edges.sort(key=lambda edge: edge[0] + edge[1])

        self.assertEqual(edges, expected_edges)

    def test_combine_graph(self):
        output_files = [self.generator.generate_spec_graph(TEST_SPEC_PATH_CPT), self.generator.generate_cpt_graph(TEST_CPT_PATH)]
        combined_graph = self.generator.combine_graphs(output_files)

        self.assertEqual(len(combined_graph.nodes()), 6)
        expected_nodes = [
            "Scenario:Scenario 1",
            "Step:step a",
            "Step:Test Concept",
            "Step:Step 1",
            "Step:Step 2",
            "Step:Step 3"
        ]

        expected_nodes.sort()
        actual_nodes = list(combined_graph.nodes())
        actual_nodes.sort()

        self.assertEqual(actual_nodes, expected_nodes)

        self.assertEqual(len(combined_graph.edges()), 5)
        expected_edges = [
            ("Scenario:Scenario 1", "Step:step a"),
            ("Scenario:Scenario 1", "Step:Test Concept"),
            ("Step:Test Concept", "Step:Step 1"),
            ("Step:Test Concept", "Step:Step 2"),
            ("Step:Test Concept", "Step:Step 3")
        ]
        expected_edges.sort(key=lambda edge: edge[0] + edge[1])
        actual_edges = list(combined_graph.edges())
        actual_edges.sort(key=lambda edge: edge[0] + edge[1])
        self.assertEqual(actual_edges, expected_edges)

    def test_parse_folder(self):
        output_files = self.generator.parse_folder(RESOURCE_DIR)
        self.assertEqual(len(output_files), 6)

        expected_filenames = [
            "test_concept.cpt",
            "long_test_smell.spec",
            "test_spec_with_concept.spec",
            "test_specification.spec",
            "self_referencing_concept.cpt",
            "long_test_name.spec"
        ]

        expected_filenames.sort()

        output_files.sort()
        self.assertEqual(output_files, expected_filenames)

    def test_server_Side_Spec(self):
        output_file = self.generator.generate_spec_graph(NEW_TEST_SPEC_PATH)
        output_graph = nx.read_yaml(f"{OUTPUT_DIR}/{output_file}.yaml")
        nodes = list(output_graph.nodes())
        self.assertEqual(len(nodes), 15)

        expected_nodes = ['Scenario:Commentfollowedbystar', 'Scenario:Remove lowercase tags', 'Scenario:Remove upper case Tag', 'Scenario:ServerSideTest', 'ServerSide:http://test/server/side', 'Step:\nStep 1.1\n', 'Step:\nStep 2.2\n', 'Step:Step 1', 'Step:Step 1.3', 'Step:Step 1.4', 'Step:Step 2 that contains ', 'Step:Step 2.3', 'Step:Step 2.4', 'Step:Step 3', 'Step:Step 3.2']

        expected_nodes.sort()
        nodes.sort()

        self.assertEqual(nodes, expected_nodes)

        edges = list(output_graph.edges())
        expected_edges = [
            ('Scenario:Commentfollowedbystar', 'Step:\nStep 1.1\n'),
            ('Scenario:Commentfollowedbystar', 'Step:\nStep 2.2\n'),
            ('Scenario:Commentfollowedbystar', 'Step:Step 3.2'),
            ('Scenario:Remove lowercase tags', 'Step:Step 1.4'),
            ('Scenario:Remove lowercase tags', 'Step:Step 2.4'),
            ('Scenario:Remove upper case Tag', 'Step:Step 1.3'),
            ('Scenario:Remove upper case Tag', 'Step:Step 2.3'),
            ('Scenario:ServerSideTest', 'Step:Step 1'),
            ('Scenario:ServerSideTest', 'Step:Step 2 that contains '),
            ('Scenario:ServerSideTest', 'Step:Step 3'),
            ('Step:Step 1', 'ServerSide:http://test/server/side'),
            ('Step:Step 2 that contains ', 'ServerSide:http://test/server/side'),
            ('Step:Step 3', 'ServerSide:http://test/server/side')
        ]

        edges.sort(key=lambda edge: edge[0] + edge[1])
        expected_edges.sort(key=lambda edge: edge[0] + edge[1])

        self.assertEqual(edges, expected_edges)

    def test_updates_generate_concept_graph(self):
        output_file = self.generator.generate_cpt_graph(NEW_TEST_CPT_PATH,RESOURCE_PATH)
        output_graph = nx.read_yaml(f"{OUTPUT_DIR}/{output_file}.yaml")
        nodes = list(output_graph.nodes())
        self.assertEqual(len(nodes), 4)

        expected_nodes = ['Step:"Test1" button click "30"', 'Step:"Test2" button click "30"', 'Step:Step 2.2', 'Step:Step 3.2']

        expected_nodes.sort()
        nodes.sort()

        self.assertEqual(nodes, expected_nodes)

        edges = list(output_graph.edges())
        print(edges)
        expected_edges = [
            ('Step:Step 2.2', 'Step:"Test1" button click "30"'),
            ('Step:Step 3.2', 'Step:"Test2" button click "30"')
        ]

        edges.sort(key=lambda edge: edge[0] + edge[1])
        expected_edges.sort(key=lambda edge: edge[0] + edge[1])

        self.assertEqual(edges, expected_edges)

if __name__ == '__main__':
    unittest.main()
