import { Handle, Position } from '@xyflow/react';
import '../App.css';

interface ReverbNodeData {
  id: string;
  roomSize: number;
}

export default function ReverbNode({ data }: { data: ReverbNodeData }) {
  return (
    <div className="node">
      <div className="node__header">Reverb</div>
      <div className="node__body">
        <div className="node__info">{data.id}</div>
        <div className="node__info">Room: {data.roomSize}</div>
      </div>
      <Handle type="target" position={Position.Left} />
      <Handle type="source" position={Position.Right} />
      <Handle type="target" id="PotiAdapter" position={Position.Bottom} isValidConnection={(c) => c.sourceHandle === 'PotiConnector'} />
    </div>
  );
}
