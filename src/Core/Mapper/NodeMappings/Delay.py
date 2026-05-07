from Mapper.node_mapper import NodeMapper
from Models.node_model import NodeModel
from Core.Node.nodes import Delay

@NodeMapper.registerNode("Delay")
def create_delay_node(nodeModel: NodeModel) -> Delay:
    return Delay(nodeModel.id, nodeModel.parameter, nodeModel.Poti)
