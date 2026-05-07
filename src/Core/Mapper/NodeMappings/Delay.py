from Mapper.NodeMapper import NodeMapper
from Models.NodeModel import NodeModel
from Core.Node.Nodes import Delay

@NodeMapper.registerNode("Delay")
def create_delay_node(nodeModel: NodeModel) -> Delay:
    return Delay(nodeModel.id, nodeModel.parameter, nodeModel.Poti)
