from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class OptionsMenu(QWidget):
    def __init__(self, config):
        super().__init__()
        self.setWindowTitle("Gauge Explorer - Options")
        sansFont = QFont("Arial", 10)
        self.setFont(sansFont)
        self.config = config
        layout = QFormLayout()

        self.font_input = QSpinBox(self)
        self.font_input.setValue(self.config.font_size)
        self.font_input.setMaximum(50)
        self.font_input.setMinimum(5)
        layout.addRow("Graph Font Size", self.font_input)

        self.edge_label_input = QCheckBox(self)
        self.edge_label_input.setChecked(self.config.edge_labels)
        layout.addRow("Show edge labels", self.edge_label_input)

        self.show_deg_input = QCheckBox(self)
        self.show_deg_input.setChecked(self.config.show_node_degree)
        layout.addRow("Show in degree and out degree of nodes ", self.show_deg_input)

        self.level_spacing_input = QSpinBox(self)
        self.level_spacing_input.setMaximum(10000)
        self.level_spacing_input.setValue(config.level_separation)
        self.level_spacing_input.setSingleStep(25)
        layout.addRow("Level Spacing", self.level_spacing_input)

        self.node_distance_input = QSpinBox(self)
        self.node_distance_input.setMaximum(10000)
        self.node_distance_input.setValue(config.node_distance)
        self.node_distance_input.setSingleStep(5)
        layout.addRow("Node Spacing", self.node_distance_input)

        self.show_src_input = QCheckBox(self)
        self.show_src_input.setChecked(config.show_src_file)
        layout.addRow("Show source file name for scenarios", self.show_src_input)

        self.save_btn = QPushButton("Save", self)
        self.save_btn.clicked.connect(self.save_click)
        layout.addRow(self.save_btn)

        self.setLayout(layout)

    def save_click(self):
        self.config.edge_labels = self.edge_label_input.isChecked()
        self.config.show_node_degree = self.show_deg_input.isChecked()
        self.config.font_size = self.font_input.value()
        self.config.node_distance = self.node_distance_input.value()
        self.config.level_separation = self.level_spacing_input.value()
        self.config.show_src_file = self.show_src_input.isChecked()
        self.hide()
        msg = QMessageBox(self)
        msg.setInformativeText("Options saved! You will need to redraw the graph for changes to take effect.")
        msg.show()