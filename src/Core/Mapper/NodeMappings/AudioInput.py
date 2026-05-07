from Core.Mapper.NodeMapper import NodeMapper
from Models.NodeModel import NodeModel
from Core.Node.Nodes import AudioInput

@NodeMapper.registerNode("AudioInput")
def create_audio_input_node(nodeModel: NodeModel) -> AudioInput:
    return AudioInput(nodeModel.id)
