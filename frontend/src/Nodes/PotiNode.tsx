import {Handle, Position} from '@xyflow/react';

interface PotiNodeData {
    id: string; 
    inputPin: string;
    resistance: number;
    maxValue: number;
}

export default function PotitNode({ data }: { data: PotiNodeData })
{
  return (
    <div style={{ padding: '10px', border: '1px solid black', borderRadius: 5, backgroundColor: 'white' }}>
      
      <div>{data.id}</div>
      <div>Pin:{data.inputPin}</div>
      <Handle type="source" position={Position.Top} id="PotiConnector" isValidConnection={(connection) => connection.targetHandle === 'PotiAdapter'}/>
    </div>
  );
}