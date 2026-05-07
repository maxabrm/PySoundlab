from Mapper.NodeMapper import NodeMapper
from Models.NodeModel import NodeModel
from Core.Node.Nodes import Gain

@NodeMapper.registerNode("Gain")
def create_gain_node(nodeModel: NodeModel) -> Gain:
    return Gain(nodeModel.id, nodeModel.parameter, nodeModel.Poti)