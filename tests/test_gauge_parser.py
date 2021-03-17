import unittest
import os

from application.models.gauge_data_models import ClientObjects
from application.parsers.gauge_parser import gauge_parser
from tests.test_config import *

TEST_SPEC_PATH = os.path.join(RESOURCE_DIR, "updated_test_specification.spec")
ALT_TEST_SPEC_PATH = os.path.join(RESOURCE_DIR, "test_spec_alternative_heading_style.spec")
TEST_CPT_PATH = os.path.join(RESOURCE_DIR, "test_concept.cpt")
TEST_RESOURCE_PATH = os.path.join(RESOURCE_DIR, "testElements/resourceTest.json")


class ParserTest(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = gauge_parser()

    # Scenarios
    def test_parse_spec_finds_all_scenarios(self):
        scenarios = self.parser.parse_spec(TEST_SPEC_PATH)
        self.assertEqual(len(scenarios), 2)

    def test_parse_spec_alternative_heading_style(self):
        scenarios = self.parser.parse_spec(ALT_TEST_SPEC_PATH)
        self.assertEqual(len(scenarios), 7)


    def test_parse_spec_gets_correct_source_files(self):
        scenarios = self.parser.parse_spec(TEST_SPEC_PATH)
        source_files = set()
        for scenario in scenarios:
            source_files.add(scenario.source_file)
        self.assertEqual(len(source_files), 1)
        self.assertTrue("test_specification.spec" in source_files)

    def test_parse_spec_gets_all_steps(self):
        scenarios = self.parser.parse_spec(TEST_SPEC_PATH)

        expectedSteps = list()
        expectedSteps.append(["Step 1","Step 2","Step 3"])
        expectedSteps.append(["Step with $Variable$", "Step 2", "Step 3"])

        for i, scenario in enumerate(scenarios):
            self.assertEqual(scenario.steps,expectedSteps[i])

    def test_parse_spec_gets_scenario_names(self):
        scenarios = self.parser.parse_spec(TEST_SPEC_PATH)

        expectedScenarioNames = list()
        expectedScenarioNames.append("Scenario 1")
        expectedScenarioNames.append("Scenario 2")

        for i, scenario in enumerate(scenarios):
            self.assertEqual(scenario.name, expectedScenarioNames[i])

    def test_parse_spec_gets_server_side_node(self):
        scenarios = self.parser.parse_spec(TEST_SPEC_PATH)

        expectedServer = list()
        expectedServer.append("http://test/server/side")
        expectedServer.append("null")
        expectedServer.append("null")
        expectedServer.append("null")

        for i, scenario in enumerate(scenarios):
            self.assertEqual(scenario.web,expectedServer[i])

    # Concepts
    def test_parse_cpt_finds_all_scenarios(self):
        concepts = self.parser.parse_cpt(TEST_CPT_PATH)
        self.assertEqual(len(concepts), 1)

    def test_parse_cpt_gets_all_steps(self):
        concepts = self.parser.parse_cpt(TEST_CPT_PATH)

        expectedSteps = list()
        expectedSteps.append(["Step 1","Step 2","Step 3"])

        for i, scenario in enumerate(concepts):
            self.assertEqual(scenario.steps,expectedSteps[i])

    def test_parse_cpt_gets_scenario_names(self):
        concepts = self.parser.parse_cpt(TEST_CPT_PATH)

        expected_concept_names = list()
        expected_concept_names.append("Test Concept")

        for i, scenario in enumerate(concepts):
            self.assertEqual(scenario.name, expected_concept_names[i])

    def test_parse_resource_file(self):
        clientObjects = self.parser.parse_resource(TEST_RESOURCE_PATH)
        print(clientObjects)
        keys = list()
        values = list()
        types = list()
        keys.append('Test1')
        keys.append('Test2')
        values.append('h2')
        values.append('h2')
        types.append('css')
        types.append('css')

        for i, keyObjects in enumerate(clientObjects.keys):
            self.assertEqual(keys[i], clientObjects.keys[i])

        for i , valueObjects in enumerate(clientObjects.values):
            self.assertEqual(values[i], clientObjects.values[i])

        for i , typeObject in enumerate(clientObjects.types):
            self.assertEqual(types[i], clientObjects.types[i])



if __name__ == '__main__':
    unittest.main()
