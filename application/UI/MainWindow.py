from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QFont
from application.graph.graph_generator import Graph_generator
import sys
import shutil
import os
from application.UI import Options
from application.smells.smellController import SmellController


class Window(QWidget):
    def __init__(self, config):
        self.graph = Graph_generator(config)
        self.config = config
        super().__init__()
        self.setMinimumSize(1000, 600)
        self.setWindowTitle("Gauge Explorer")
        sansFont = QFont("Arial", 10)
        self.setFont(sansFont)
        self.UI()
        self.options = Options.OptionsMenu(config)
        self.smellController = SmellController(output_dir=self.config.OUTPUT_DIR)


    def UI(self):
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        # File input text box.
        self.filepath_input = QLineEdit(self)
        grid_layout.addWidget(self.filepath_input, 0, 0, 1, 3)

        # Browse button.
        self.browse_btn = QPushButton("Browse", self)
        grid_layout.addWidget(self.browse_btn, 0, 3, 1, 1)
        self.browse_btn.clicked.connect(self.browse_click)

        # Parse button.
        self.parse_btn = QPushButton("Parse Folder", self)
        grid_layout.addWidget(self.parse_btn, 1, 0, 1, 4)
        self.parse_btn.clicked.connect(self.parse_click)

        # Select all button
        self.select_all_btn = QPushButton("Select all", self)
        grid_layout.addWidget(self.select_all_btn, 2, 0, 1, 2)
        self.select_all_btn.clicked.connect(self.select_all_click)

        # Clear all button
        self.clear_all_btn = QPushButton("Clear all", self)
        grid_layout.addWidget(self.clear_all_btn, 2, 2, 1, 2)
        self.clear_all_btn.clicked.connect(self.clear_all_click)

        # File list.
        self.fileList = QListWidget(self)
        grid_layout.addWidget(self.fileList, 3, 0, 10, 4)

        # Draw button.
        self.draw_btn = QPushButton("Draw Graph", self)
        grid_layout.addWidget(self.draw_btn, 13, 0, 1, 4)
        self.draw_btn.clicked.connect(self.draw_click)

        # Options button.
        self.options_button = QPushButton("Options", self)
        grid_layout.addWidget(self.options_button, 14, 0, 1, 4)
        self.options_button.clicked.connect(self.options_click)

        # Graph view.
        self.web = QWebEngineView(self)
        grid_layout.addWidget(self.web, 0, 5, 16, 20)

        # Save button.
        self.save_btn = QPushButton("Export graph", self)
        grid_layout.addWidget(self.save_btn, 17, 24)
        self.save_btn.clicked.connect(self.export_graph_click)

        # Smell Report button.
        self.report_btn = QPushButton("Generate Smell Report", self)
        grid_layout.addWidget(self.report_btn, 17, 22)
        self.report_btn.clicked.connect(self.report_click)

        # Detect Smell button
        self.smell_btn = QPushButton("Detect Test Smells", self)
        grid_layout.addWidget(self.smell_btn, 17, 20)
        self.smell_btn.clicked.connect(self.detect_click)
        self.showMaximized()

    def browse_click(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.filepath_input.setText(directory)

    def parse_click(self):
        self.clean_output()
        self.fileList.clear()
        path = self.filepath_input.text()

        if len(path) == 0:
            self.show_error("Please enter a directory path")
            return

        path = r'{}'.format(path)

        # Check if filepath exists
        if not os.path.isdir(path):
            self.show_error("Please enter a valid directory path")
            return

        try:
            items = self.graph.parse_folder(path)
        except:
            self.show_error("Unable to parse folder")
            return

        for item in items:
            self.add_item(item)

    def select_all_click(self):
        for i in range(self.fileList.count()):
            item = self.fileList.item(i)
            item.setCheckState(2)

    def clear_all_click(self):
        for i in range(self.fileList.count()):
            item = self.fileList.item(i)
            item.setCheckState(0)

    def add_item(self, filename):
        item = QListWidgetItem()
        item.setText(filename)
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Checked)
        self.fileList.addItem(item)

    def draw_click(self):
        checked = []
        for i in range(self.fileList.count()):
            item = self.fileList.item(i)
            if item.checkState() == 2:
                checked.append(item.text())
        if len(checked) == 0:
            self.show_error("Please select at least one file")
            return
        try:
            combined = self.graph.combine_graphs(checked)
            self.graph.render_graph(combined)
            self.web.load(
                QUrl.fromLocalFile(QFileInfo(os.path.join(self.config.OUTPUT_DIR, "graph.html")).absoluteFilePath()))
        except Exception as ex:
            print(f"Error processing graph, exception message was{ex}")

    def detect_click(self):
        checked = []
        for i in range(self.fileList.count()):
            item = self.fileList.item(i)
            if item.checkState() == 2:
                checked.append(item.text())
        if len(checked) == 0:
            self.show_error("Please select at least one file")
            return
        try:
            combined = self.graph.combine_graphs(checked)
            self.smellController.detectSmells(combined)
            self.graph.render_graph(combined)
            self.web.load(
                QUrl.fromLocalFile(QFileInfo(os.path.join(self.config.OUTPUT_DIR, "graph.html")).absoluteFilePath()))
        except Exception as ex:
            print(f"Error processing graph, exception message was{ex}")

    def report_click(self):
        checked = []
        for i in range(self.fileList.count()):
            item = self.fileList.item(i)
            if item.checkState() == 2:
                checked.append(item.text())
        if len(checked) == 0:
            self.show_error("Please select at least one file")
            return
        try:
            combined = self.graph.combine_graphs(checked)
            self.smellController.generateSmellReport(combined)
            self.web.load(
                QUrl.fromLocalFile(QFileInfo(os.path.join(self.config.OUTPUT_DIR, "smell_report.html")).absoluteFilePath()))
        except Exception as ex:
            print(f"Error processing graph, exception message was{ex}")

    def export_graph_click(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Export Graph", "",
                                                   "Html Files (*.html)")
        if os.path.exists(f"{self.config.OUTPUT_DIR}/graph.html"):
            shutil.copyfile(f"{self.config.OUTPUT_DIR}/graph.html", file_name)

    def show_error(self, message):
        self.msg_box = QMessageBox(self)
        self.msg_box.setIcon(QMessageBox.Critical)
        self.msg_box.setText("Error")
        self.msg_box.setInformativeText(message)
        self.msg_box.setWindowTitle("Error")
        self.msg_box.show()

    def options_click(self):
        self.options.show()

    def clean_output(self):
        for filename in os.listdir(self.config.OUTPUT_DIR):
            file_path = os.path.join(self.config.OUTPUT_DIR, filename)
            if file_path.endswith(".yaml") or file_path.endswith(".html"):
                os.unlink(file_path)


def main(config):
    App = QApplication(sys.argv)
    window = Window(config)
    window.clean_output()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
