import { Handle, Position} from '@xyflow/react';

interface DelayNodeData {
  id: string
  type: string;
  parameter: number;
}

export default function DelayNode({ data }: { data: DelayNodeData })
{
  return (
    <div style={{ padding: '10px', border: '1px solid black', borderRadius: 5, backgroundColor: 'white' }}>
      
      <div>{data.id}</div>
      <Handle type="source" position={Position.Right} />
      <Handle type="target" position={Position.Left} />
      <Handle type="target" id="PotiAdapter" position={Position.Bottom} isValidConnection={(connection) => connection.sourceHandle === "PotiConnector"}/>

    </div>
  );
}