import unittest
from application.parsers import markdown_processor
from bs4 import BeautifulSoup
import os
from tests.test_config import *

TEST_SPEC_PATH = os.path.join(RESOURCE_DIR, "test_specification.spec")
TEST_CPT_PATH = os.path.join(RESOURCE_DIR, "test_concept.cpt")


class MarkdownProcessorTests(unittest.TestCase):
    def test_spec_title(self):
        with open(TEST_SPEC_PATH) as input_file:
            string = input_file.read()
            html = markdown_processor.process_markdown(string)
            soup = BeautifulSoup(html, 'html.parser')

            titles = list(soup.findAll("h1"))
            self.assertEqual(len(titles), 1)

            self.assertEqual(titles[0].get_text(), "Spec Title")

    def test_scenario_names(self):
        with open(TEST_SPEC_PATH) as input_file:
            string = input_file.read()
            html = markdown_processor.process_markdown(string)
            soup = BeautifulSoup(html, 'html.parser')

            scenario_names = list(soup.findAll("h2"))

            self.assertEqual(len(scenario_names), 2)

            expected_scenario_names = ["Scenario 1", "Scenario 2"]

            for i, h2_element in enumerate(scenario_names):
                self.assertEqual(h2_element.get_text(), expected_scenario_names[i])

    def test_tags_removed(self):
        with open(TEST_SPEC_PATH) as input_file:
            string = input_file.read()
            html = markdown_processor.process_markdown(string)
            self.assertTrue("Tags:" not in html)

    def test_comments_removed(self):
        with open(TEST_SPEC_PATH) as input_file:
            string = input_file.read()
            html = markdown_processor.process_markdown(string)
            self.assertTrue("comment" not in html)

    def test_variables_replaced(self):
        with open(TEST_SPEC_PATH) as input_file:
            string = input_file.read()
            html = markdown_processor.process_markdown(string)
            self.assertTrue("$Variable$" in html)

if __name__ == '__main__':
    unittest.main()
