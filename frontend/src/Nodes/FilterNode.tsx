import { Handle, Position } from '@xyflow/react';
import '../App.css';

interface FilterNodeData {
  id: string;
  frequency: number;
}

export default function FilterNode({ data }: { data: FilterNodeData }) {
  return (
    <div className="node">
      <div className="node__header">Filter</div>
      <div className="node__body">
        <div className="node__info">{data.id}</div>
        <div className="node__info">Freq: {data.frequency} Hz</div>
      </div>
      <Handle type="target" position={Position.Left} />
      <Handle type="source" position={Position.Right} />
      <Handle type="target" id="PotiAdapter" position={Position.Bottom} isValidConnection={(c) => c.sourceHandle === 'PotiConnector'} />
    </div>
  );
}
