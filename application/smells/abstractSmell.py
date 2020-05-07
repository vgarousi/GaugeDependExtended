from abc import ABC, abstractmethod
from networkx import Graph

GRAPH_HTML_TEMPLATE = r"""
    <iframe class="embed-responsive-item" src="<!-- Graph File Path -->" frameborder="0" width="100%"
                    height="400px"></iframe>
"""

SMELL_HTML_TEMPLATE = r"""
    <div class="smell_report">
        <h2><!-- Smell Name --></h2>
        <h4>Number of Smells : <!-- No of Smells --></h4>
        <p><!-- Smell Description --></p>
        <p>
            <a class="btn btn-info" data-toggle="collapse" href="#<!-- Smell ID -->_id" role="button"
               aria-expanded="false" aria-controls="collapseExample">
                Show Test Smell Graphs
            </a>
        </p>

        <div class="collapse" id="<!-- Smell ID -->_id">
            <!-- Smell Graphs --> 
        </div>
    </div>
"""


class AbstractSmell(ABC):
    @abstractmethod
    def get_smell_name(self) -> str:
        pass

    @abstractmethod
    def has_smell(self, graph) -> bool:
        pass

    @abstractmethod
    def get_smell_description(self) -> str:
        pass

    @abstractmethod
    def get_smell_id(self) -> str:
        pass

    @abstractmethod
    def update_graph(self, graph) -> None:
        pass

    @abstractmethod
    def get_smell_subgraph(self, graph) -> list:
        pass

    def get_smell_html(self, graph) -> str:
        html_str = SMELL_HTML_TEMPLATE
        html_str = html_str.replace("<!-- Smell Name -->", self.get_smell_name())
        html_str = html_str.replace("<!-- Smell ID -->", self.get_smell_id())
        html_str = html_str.replace("<!-- Smell Description -->", self.get_smell_description())

        graph_paths = self.get_smell_subgraph(graph)

        html_str = html_str.replace("<!-- No of Smells -->", str(len(graph_paths)))

        graph_html = ""

        for graph in graph_paths:
            graph_text = GRAPH_HTML_TEMPLATE
            graph_text = graph_text.replace("<!-- Graph File Path -->", graph)
            graph_html = graph_html + graph_text

        html_str = html_str.replace("<!-- Smell Graphs --> ", graph_html)

        return html_str
