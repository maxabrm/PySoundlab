import {Handle, Position} from '@xyflow/react';

interface AudioInputNodeData {
  type: string;
  inputPin: string;
}

export default function AudioInputNode({ data }: { data: AudioInputNodeData })
{
  return (
    <div style={{ padding: '10px', border: '1px solid black', borderRadius: 5, backgroundColor: 'white' }}>
      
      <div>AudioInput</div>
      <div>Pin:{data.inputPin}</div>
      <Handle type="source" position={Position.Right} />
    </div>
  );
}