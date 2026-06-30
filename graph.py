from pyvis.network import Network

def create_graph(relationships):

    net = Network(height="750px", width="100%", directed=True)

    nodes = set()

    for source, target in relationships:
        nodes.add(source)
        nodes.add(target)

    for node in nodes:
        net.add_node(node)

    for source, target in relationships:
        net.add_edge(source, target)

    net.write_html("memory_map.html")

    print("✅ Memory Map Created!")