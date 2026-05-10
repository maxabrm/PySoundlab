from Core.Mapper.NodeMapper import NodeMapper
import Core.Graph.Graph as Graph
import Models.GraphModel as GraphModel


class GraphMapper:
    @classmethod
    def map_graph_model_to_graph(cls,graphModel: GraphModel.GraphModel) -> Graph.Graph:
        graph = Graph.Graph()
        node_id_map = {}

        # Map nodes
        for node_model in graphModel.nodes:
            node = NodeMapper.createNode(node_model)
            graph.addNode(node)
            node_id_map[node_model.id] = node

        # Map connections
        for connection in graphModel.connections:
            node1 = node_id_map.get(connection.node1_id)
            node2 = node_id_map.get(connection.node2_id)
            if node1 and node2:
                graph.addConnection(node1, node2)

        graph.sortByConnections()
        return graph