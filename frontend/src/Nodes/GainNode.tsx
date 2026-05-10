import { Handle, Position } from '@xyflow/react';
import '../App.css';

interface GainNodeData {
  id: string;
  gain: number;
}

export default function GainNode({ data }: { data: GainNodeData }) {
  return (
    <div className="node">
      <div className="node__header">Gain</div>
      <div className="node__body">
        <div className="node__info">{data.id}</div>
        <div className="node__info">Gain: {data.gain}</div>
      </div>
      <Handle type="target" position={Position.Left} />
      <Handle type="source" position={Position.Right} />
      <Handle type="target" id="PotiAdapter" position={Position.Bottom} isValidConnection={(c) => c.sourceHandle === 'PotiConnector'} />
    </div>
  );
}
