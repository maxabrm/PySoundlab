from Mapper.node_mapper import NodeMapper
from Models.node_model import NodeModel
from Core.Node.nodes import AudioOutput

@NodeMapper.registerNode("AudioOutput")
def create_audio_output_node(nodeModel: NodeModel) -> AudioOutput:
    return AudioOutput(nodeModel.id)
