from Core.Mapper.NodeMapper import NodeMapper
from Models.NodeModel import NodeModel
from Core.Node.Nodes import Filter

@NodeMapper.registerNode("Filter")
def create_filter_node(nodeModel: NodeModel) -> Filter:
    return Filter(nodeModel.id, nodeModel.parameter, NodeMapper.mapPoti(nodeModel.Poti))