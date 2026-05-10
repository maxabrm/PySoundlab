from Core.Mapper.NodeMapper import NodeMapper
from Models.NodeModel import NodeModel
from Core.Node.Nodes import Reverb

@NodeMapper.registerNode("Reverb")
def create_reverb_node(nodeModel: NodeModel) -> Reverb:
    return Reverb(nodeModel.id, nodeModel.parameter, NodeMapper.mapPoti(nodeModel.Poti))
