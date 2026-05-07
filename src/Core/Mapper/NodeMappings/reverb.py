from Mapper.node_mapper import NodeMapper
from Models.node_model import NodeModel
from Core.Node.nodes import Reverb

@NodeMapper.registerNode("Reverb")
def create_reverb_node(nodeModel: NodeModel) -> Reverb:
    return Reverb(nodeModel.id, nodeModel.parameter, nodeModel.Poti)
