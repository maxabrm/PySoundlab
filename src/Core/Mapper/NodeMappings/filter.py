from Mapper.node_mapper import NodeMapper
from Models.node_model import NodeModel 
from Core.Node.nodes import Filter

@NodeMapper.registerNode("Filter")
def create_filter_node(nodeModel: NodeModel) -> Filter:
    return Filter(nodeModel.id, nodeModel.parameter, nodeModel.Poti)