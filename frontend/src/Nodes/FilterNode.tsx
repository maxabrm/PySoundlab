import { Handle, Position} from '@xyflow/react';


interface FilterNodeData {
  id: string
  type: string;
  fixedDelayTime: number;
}

export default function FilterNode({ data }: { data: FilterNodeData })
{
  return (
    <div style={{ padding: '10px', border: '1px solid black', borderRadius: 5, backgroundColor: 'white' }}>
      
      <div>{data.id}</div>
      <Handle type="source" position={Position.Right} />
      <Handle type="target" position={Position.Left} />
      <Handle type="target" id="PotiAdapter"position={Position.Bottom} isValidConnection={(connection) => connection.sourceHandle === 'PotiConnector'}/>
    </div>
  );
}