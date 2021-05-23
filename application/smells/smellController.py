from application.smells.longTestSmell import LongTestSmell
from application.smells.unusedCptSmell import UnusedCptSmell
from application.smells.selfReferencingCptSmell import SelfReferencingCptSmell
from application.smells.longStepName import LongStepName
from application.util.config import Config
from application.graph.graph_renderer import GraphRenderer
import os

# Needed for testing delete these imports after
from application.graph.graph_generator import Graph_generator
from networkx import nx

REPORT_HTML_TEMPLATE = r"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Test Smell Report</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous"
</head>
<body>

<div class="container">
    <h1>Test Smell Report</h1>
    <!-- TEST SMELLS -->
</div>


<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
        crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
        crossorigin="anonymous"></script>
</body>
</html>
"""


class SmellController:
    def __init__(self, output_dir):
        self.config = Config(output_dir, show_src_file=False, font_size=16, edge_labels=False, level_separation=1000,
                             node_distance=150)
        self.renderer = GraphRenderer(self.config)
        self.smells = [
            LongTestSmell(self.renderer),
            UnusedCptSmell(self.renderer),
            SelfReferencingCptSmell(self.renderer),
            LongStepName(self.renderer)
        ]

    def detectSmells(self, graph):
        for smell in self.smells:
            smell.update_graph(graph)

    def generateSmellReport(self, graph):
        smell_html = ""

        for smell in self.smells:
            if smell.has_smell(graph):
                smell_html = smell_html + smell.get_smell_html(graph)

        report_html = REPORT_HTML_TEMPLATE
        report_html = report_html.replace("<!-- TEST SMELLS -->", smell_html)

        output_file = open(os.path.join(self.config.OUTPUT_DIR, "smell_report.html"), "w")
        output_file.write(report_html)
        output_file.close()


if __name__ == "__main__":
    pass
