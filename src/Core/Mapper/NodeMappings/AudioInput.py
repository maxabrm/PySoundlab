from Mapper.node_mapper import NodeMapper
from Models.node_model import NodeModel
from Core.Node.nodes import AudioInput

@NodeMapper.registerNode("AudioInput")
def create_audio_input_node(nodeModel: NodeModel) -> AudioInput:
    return AudioInput(nodeModel.id)
