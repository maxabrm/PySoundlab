from fastapi import APIRouter
import Core.Graph.graph as graph
import Core.Node.nodes as nodes
import Core.Node.node as node

router = APIRouter()

@router.post("/addPoti")
def add_poti(node: node.Node, poti: node.Poti):
    node.addPoti(poti)
    return {"message": "Poti added successfully"}

@router .post("/changeNodeParameter")
def change_node_parameter(node: node.Node, parameter: float):
    node.setParameter(parameter)
    return {"message": "Node parameter changed successfully"}

@router.post("/createFilterNode")
def create_filter_node(filter_node: nodes.Filter):
    new_filter_node = nodes.Filter(filter_node.id, filter_node.parameter, filter_node.Poti)
    return {"message": "Filter node created successfully"}

@router.post("/createDelayNode")
def create_delay_node(delay_node: nodes.Delay):
    new_delay_node = nodes.Delay(delay_node.id, delay_node.parameter, delay_node.Poti)
    return {"message": "Delay node created successfully"}

@router.post("/createReverbNode")
def create_reverb_node(reverb_node: nodes.Reverb):
    new_reverb_node = nodes.Reverb(reverb_node.id, reverb_node.parameter, reverb_node.Poti)
    return {"message": "Reverb node created successfully"}  

@router.post("/createAudioInputNode")
def create_audio_input_node(audio_input_node: nodes.AudioInput):
    new_audio_input_node = nodes.AudioInput(audio_input_node.id)
    return {"message": "Audio Input node created successfully"} 

@router.post("/createAudioOutputNode")
def create_audio_output_node(audio_output_node: nodes.AudioOutput):
    new_audio_output_node = nodes.AudioOutput(audio_output_node.id)
    return {"message": "Audio Output node created successfully"}    

@router.post("/createGainNode")
def create_gain_node(gain_node: nodes.Gain):
    new_gain_node = nodes.Gain(gain_node.id, gain_node.parameter, gain_node.Poti)
    return {"message": "Gain node created successfully"}

