import sys
import unittest
try:
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtTest import QTest
    from PyQt5.QtCore import Qt
except Exception:
    raise unittest.SkipTest("Failed to import PyQt - skipping Main Window UI tests")

from tests.test_config import *

from application.UI.MainWindow import Window
from application.util.config import Config


app = QApplication(sys.argv)

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test_config = Config(OUTPUT_DIR=OUTPUT_DIR)
        self.main_window = Window(self.test_config)

    def test_empty_directory_input(self):
        QTest.mouseClick(self.main_window.parse_btn, Qt.LeftButton)
        self.assertTrue(self.main_window.fileList.count() == 0)
        self.assertTrue(self.main_window.msg_box.isVisible())

    def test_invalid_directory_input(self):
        QTest.keyClicks(self.main_window.filepath_input, "blah blah blah")
        QTest.mouseClick(self.main_window.parse_btn, Qt.LeftButton)
        self.assertTrue(self.main_window.fileList.count() == 0)
        self.assertTrue(self.main_window.msg_box.isVisible())

    def test_valid_directory_input(self):
        QTest.keyClicks(self.main_window.filepath_input, RESOURCE_DIR)
        QTest.mouseClick(self.main_window.parse_btn, Qt.LeftButton)
        self.assertTrue(self.main_window.fileList.count() > 0)

    def test_all_files_selected_by_default(self):
        QTest.keyClicks(self.main_window.filepath_input, RESOURCE_DIR)
        QTest.mouseClick(self.main_window.parse_btn, Qt.LeftButton)
        total = self.main_window.fileList.count()

        selected = list()
        for i in range(total):
            item = self.main_window.fileList.item(i)
            if item.checkState() == 2:
                selected.append(item.text())

        self.assertEqual(len(selected), total)

    def test_clear_all_files(self):
        QTest.keyClicks(self.main_window.filepath_input, RESOURCE_DIR)
        QTest.mouseClick(self.main_window.parse_btn, Qt.LeftButton)
        total = self.main_window.fileList.count()

        QTest.mouseClick(self.main_window.clear_all_btn, Qt.LeftButton)

        selected = list()
        for i in range(total):
            item = self.main_window.fileList.item(i)
            if item.checkState() == 2:
                selected.append(item.text())

        self.assertEqual(len(selected), 0)

    def test_select_all(self):
        QTest.keyClicks(self.main_window.filepath_input, RESOURCE_DIR)
        QTest.mouseClick(self.main_window.parse_btn, Qt.LeftButton)
        total = self.main_window.fileList.count()

        for i in range(total):
            item = self.main_window.fileList.item(i)
            item.setCheckState(0)

        QTest.mouseClick(self.main_window.select_all_btn, Qt.LeftButton)

        selected = list()
        for i in range(total):
            item = self.main_window.fileList.item(i)
            if item.checkState() == 2:
                selected.append(item.text())

        self.assertEqual(len(selected), total)

    def test_draw_graph(self):
        QTest.keyClicks(self.main_window.filepath_input, RESOURCE_DIR)
        QTest.mouseClick(self.main_window.parse_btn, Qt.LeftButton)
        QTest.mouseClick(self.main_window.draw_btn, Qt.LeftButton)
        graph_file_path = os.path.join(OUTPUT_DIR, "graph.html")
        self.assertTrue(os.path.isfile(graph_file_path))

    def test_draw_graph_no_file_selected(self):
        QTest.keyClicks(self.main_window.filepath_input, RESOURCE_DIR)
        QTest.mouseClick(self.main_window.parse_btn, Qt.LeftButton)
        total = self.main_window.fileList.count()

        for i in range(total):
            item = self.main_window.fileList.item(i)
            item.setCheckState(0)

        QTest.mouseClick(self.main_window.draw_btn, Qt.LeftButton)
        graph_file_path = os.path.join(OUTPUT_DIR, "graph.html")
        self.assertFalse(os.path.isfile(graph_file_path))
        self.assertTrue(self.main_window.msg_box.isVisible())
        self.assertEqual(self.main_window.msg_box.informativeText(), "Please select at least one file")

    def test_detect_smell_graph(self):
        QTest.keyClicks(self.main_window.filepath_input, RESOURCE_DIR)
        QTest.mouseClick(self.main_window.parse_btn, Qt.LeftButton)
        QTest.mouseClick(self.main_window.smell_btn, Qt.LeftButton)
        graph_file_path = os.path.join(OUTPUT_DIR, "graph.html")
        self.assertTrue(os.path.isfile(graph_file_path))

    def test_detect_smell_graph_no_file_selected(self):
        QTest.keyClicks(self.main_window.filepath_input, RESOURCE_DIR)
        QTest.mouseClick(self.main_window.parse_btn, Qt.LeftButton)
        total = self.main_window.fileList.count()

        for i in range(total):
            item = self.main_window.fileList.item(i)
            item.setCheckState(0)

        QTest.mouseClick(self.main_window.smell_btn, Qt.LeftButton)
        graph_file_path = os.path.join(OUTPUT_DIR, "graph.html")
        self.assertFalse(os.path.isfile(graph_file_path))
        self.assertTrue(self.main_window.msg_box.isVisible())
        self.assertEqual(self.main_window.msg_box.informativeText(), "Please select at least one file")

    def test_generate_report(self):
        QTest.keyClicks(self.main_window.filepath_input, RESOURCE_DIR)
        QTest.mouseClick(self.main_window.parse_btn, Qt.LeftButton)
        QTest.mouseClick(self.main_window.report_btn, Qt.LeftButton)
        graph_file_path = os.path.join(OUTPUT_DIR, "smell_report.html")
        self.assertTrue(os.path.isfile(graph_file_path))

    def test_detect_smell_graph_no_file_selected(self):
        QTest.keyClicks(self.main_window.filepath_input, RESOURCE_DIR)
        QTest.mouseClick(self.main_window.parse_btn, Qt.LeftButton)
        total = self.main_window.fileList.count()

        for i in range(total):
            item = self.main_window.fileList.item(i)
            item.setCheckState(0)

        QTest.mouseClick(self.main_window.report_btn, Qt.LeftButton)
        graph_file_path = os.path.join(OUTPUT_DIR, "smell_report.html")
        self.assertFalse(os.path.isfile(graph_file_path))
        self.assertTrue(self.main_window.msg_box.isVisible())
        self.assertEqual(self.main_window.msg_box.informativeText(), "Please select at least one file")

    def test_options_btn(self):
        QTest.mouseClick(self.main_window.options_button, Qt.LeftButton)
        self.assertTrue(self.main_window.options.isVisible())

    def test_update_int_option(self):
        QTest.mouseClick(self.main_window.options_button, Qt.LeftButton)
        self.main_window.options.font_input.setValue(24)
        QTest.mouseClick(self.main_window.options.save_btn, Qt.LeftButton)
        self.assertEqual(self.test_config.font_size, 24)

    def test_update_boolean_option(self):
        QTest.mouseClick(self.main_window.options_button, Qt.LeftButton)
        self.main_window.options.show_src_input.setCheckState(0)
        QTest.mouseClick(self.main_window.options.save_btn, Qt.LeftButton)
        self.assertFalse(self.test_config.show_src_file)


if __name__ == '__main__':
    unittest.main()
