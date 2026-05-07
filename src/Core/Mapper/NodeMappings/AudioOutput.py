from Mapper.NodeMapper import NodeMapper
from Models.NodeModel import NodeModel
from Core.Node.Nodes import AudioOutput

@NodeMapper.registerNode("AudioOutput")
def create_audio_output_node(nodeModel: NodeModel) -> AudioOutput:
    return AudioOutput(nodeModel.id)
