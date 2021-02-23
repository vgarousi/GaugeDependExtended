import re
import textwrap
from pyvis.network import Network


class GraphRenderer:
    def __init__(self, config):
        self.config = config

    def get_node_color(self, color):
        return {
            "background": color,
            "border": "black",
            "highlight": {
                "background": "#FB6107"
            }
        }

    def format_node_label(self, label_str, in_degree, out_degree):
        #label_str = re.sub(".*:", "", label_str)
        label = label_str.split(" ")
        for j, word in enumerate(label):
            if j != 0 and j % 4 == 0:
                label[j] = word + '\n'

        #label_str = " ".join(label)
        if self.config.show_node_degree:
            label_str = textwrap.dedent(label_str)
            label_str = '\n'.join(l for line in label_str.splitlines()
                      for l in textwrap.wrap(line, width=20))
            label_str = label_str + f"\n ({in_degree},{out_degree})"
        return label_str

    def render_graph(self, graph, filename="graph.html"):
        net = Network("100%", "100%")

        source_files = list()
        for node in graph.nodes(data=True):
            node_shape = "ellipse"
            node_id = node[0]
            print("node[0] " + node_id)
            #if "Client:" in node[0]:
                #print(node[0])
            node_label = self.format_node_label(node[0], graph.in_degree(node[0]), graph.out_degree(node[0]))
            if "Scenario:" in node[0]:
                node_color = self.get_node_color("#2589BD")
                node_level = 1 if not self.config.show_src_file else 2
                if self.config.show_src_file:
                    source_files.append((node[1]["source_file"], node[0]))
            elif graph.out_degree(node[0]) > 0:
                node_color = self.get_node_color("#009B72")
                node_level = 2 if not self.config.show_src_file else 3
            elif "Client:" in node[0]:
                node_color = self.get_node_color("#90a602")
                node_level = 4 if not self.config.show_src_file else 5
            elif "ServerSide:" in node[0]:
                node_color = self.get_node_color("#6900a6")
                node_level = 5 if not self.config.show_src_file else 6
            else:
                node_color = self.get_node_color("#EC9A29")
                node_level = 3 if not self.config.show_src_file else 4

            if node[1]["smell"]:
                node_color = self.get_node_color("red")
                node_title = "\n".join(node[1]["smell_names"])
                net.add_node(n_id=node_id, label=node_label, level=node_level, color=node_color, shape=node_shape, title=node_title)
            else:
                net.add_node(n_id=node_id, label=node_label, level=node_level, color=node_color, shape=node_shape)

        if self.config.show_src_file:
            for pair in source_files:
                src = pair[0]
                dst = pair[1]
                net.add_node(src, src, shape=node_shape, level=1, color=self.get_node_color("#9FA08E"))
                net.add_edge(src, dst)

        edges = list(graph.edges())
        for src, dst in edges:
            edge_dashes = False
            if src.startswith("Step:") and dst.startswith("Step:"):
                edge_dashes = True
            edge_width = edges.count((src, dst))
            if self.config.edge_labels:
                graph_data = graph.get_edge_data(src, dst)
                labels = list()
                for key in graph_data:
                    labels.append(str(graph_data[key]["label"]))
                edge_label = ",".join(labels)
                net.add_edge(src, dst, dashes=edge_dashes, width=edge_width, label=edge_label)
            else:
                net.add_edge(src, dst, dashes=edge_dashes, width=edge_width)

        net.set_options("""
                var options = {
                  "edges": {
                    "font":{
                        "size": """ + str(self.config.font_size) + """
                    },
                    "arrows": {
                      "to": {
                        "enabled": true
                      }
                    },
                    "color": {
                      "inherit": true,
                      "highlight": "rgba(0,0,0,1)"
                    },
                    "smooth": true
                  },
                  "nodes": {
                    "borderWidth": 0.5,
                    "borderWidthSelected":1,
                     "font": {
                       "color": "rgba(255,255,255,1)",
                       "size": """ + str(self.config.font_size) + """
                     }, 
                     "fixed": {
                        "x": false, 
                        "y": false
                    }
                  },
                  "layout": {
                    "hierarchical": {
                      "enabled": true,
                      "levelSeparation": """ + str(self.config.level_separation) + """,
                      "nodeDistance": 200,
                      "nodeSpacing": 125,
                      "direction": "LR",
                      "damping": "0",
                      "sortMethod": "directed",
                      "overlap": 0
                    }
                  },
                  "physics": {
                    "enabled": false,
                    "hrepulsion": {
                        "centralGravity": 0,
                        "springLength": 100,
                        "springConstant":1,
                        "nodeDistance": 600,
                        "damping": 0
                    },
                    "stabilization": {
                        "enabled": true,
                        "fit": true
                    },
                    "minVelocity": 0.00,
                    "maxVelocity": 0.00,
                    "solver": "hrepulsion"
                  }
                }
            """)
        net.save_graph(f"{self.config.OUTPUT_DIR}/{filename}")
        return f"{self.config.OUTPUT_DIR}/{filename}"


    def configure_graph(self, graph):
        net = Network("70%", "70%")
        net.from_nx(graph)
        net.show_buttons()

        nx_edges = list(graph.edges(data="label"))
        nx_edges.sort(key=lambda edge: edge[0])
        py_vis_edges = net.get_edges()
        py_vis_edges.sort(key=lambda edge: edge["from"])

        for i, edge in enumerate(py_vis_edges):
            edge["label"] = nx_edges[i][2]
            if (edge["from"].startswith("Step:") and edge["from"].startswith("Step:")):
                edge["dashes"] = True

        out_degrees = list(graph.out_degree())
        out_degrees.sort(key=lambda tup: tup[0])
        nodes = net.nodes
        nodes.sort(key=lambda node: node["id"])
        for i, node in enumerate(nodes):
            node["shape"] = "ellipse"
            if "Scenario:" in node['id']:
                node["color"] = {
                    "background": "red",
                    "border": "red",
                    "highlight": {
                        "background": "rgba(255,186,96,1)"
                    }
                }
                node["level"] = 1
                node["label"] = node["label"].replace("Scenario:", "")
            elif out_degrees[i][1] > 0:
                node["color"] = {
                    "background": "green",
                    "border": "green",
                    "highlight": {
                        "background": "rgba(255,186,96,1)"
                    }
                }
                node["level"] = 2
                node["label"] = node["label"].replace("Step:", "")
            elif "Step:" in node['id']:
                node["color"] = {
                    "background": "blue",
                    "border": "blue",
                    "highlight": {
                        "background": "rgba(255,186,96,1)"
                    }
                }
                node["level"] = 3
                node["label"] = node["label"].replace("Step:", "")
            elif "Client:" in node['id']:
                node["color"] = {
                    "background": "purple",
                    "border": "purple",
                    "highlight": {
                        "background": "rgba(255,186,96,1)"
                    }
                }
                node["level"] = 5
                #node["label"] = node["label"].replace("Client Side:", "")

            label = node["label"].split(" ")
            for i, word in enumerate(label):
                if i != 0 and i % 5 == 0:
                    label[i] = word + '\n'

            node["label"] = " ".join(label)

        net.show(f"{self.config.OUTPUT_DIR}/graph.html")


    def stabilizer(self, graph):
        net = Network("70%", "70%")
        net.from_nx(graph)


