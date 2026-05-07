import NodeMapper
import Core.Graph.Graph as Graph
import Core.Node.Node as Node
import Models.GraphModel as GraphModel
import Models.NodeModel as NodeModel


class GraphMapper:
    @classmethod
    def map_graph_model_to_graph(graph_model: GraphModel.GraphModel) -> Graph.Graph:
        graph = Graph.Graph()
        node_id_map = {node_id: str, Node: Node}

        # Map nodes
        for node_model in graph_model.nodes:
            node = NodeMapper.NodeMapper.createNode(node_model)
            graph.add_node(node)
            node_id_map[node_model.id] = node

        # Map connections
        for connection in graph_model.connections:
            node1 = node_id_map.get(connection.node1_id)
            node2 = node_id_map.get(connection.node2_id)
            if node1 and node2:
                graph.add_connection(node1, node2)
                
        return graph