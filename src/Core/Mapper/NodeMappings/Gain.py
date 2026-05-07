from Mapper.node_mapper import NodeMapper
from Models.node_model import NodeModel 
from Core.Node.nodes import Gain

@NodeMapper.registerNode("Gain")
def create_gain_node(nodeModel: NodeModel) -> Gain:
    return Gain(nodeModel.id, nodeModel.parameter, nodeModel.Poti)