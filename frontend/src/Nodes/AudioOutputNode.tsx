import {Handle, Position} from '@xyflow/react';

interface AudioOutputNodeData {
  type: string;
  outputPin: string;
}

export default function AudioOutputNode({ data }: { data: AudioOutputNodeData })
{
  return (
    <div style={{ padding: '10px', border: '1px solid black', borderRadius: 5, backgroundColor: 'white' }}>
      <div>AudioOutput</div>
      <div>Pin:{data.outputPin}</div>
      <Handle type="target" position={Position.Left} />
    </div>
  );
}