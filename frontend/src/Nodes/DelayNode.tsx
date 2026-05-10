import { Handle, Position } from '@xyflow/react';
import '../App.css';

interface DelayNodeData {
  id: string;
  delayTime: number;
}

export default function DelayNode({ data }: { data: DelayNodeData }) {
  return (
    <div className="node">
      <div className="node__header">Delay</div>
      <div className="node__body">
        <div className="node__info">{data.id}</div>
        <div className="node__info">Time: {data.delayTime} ms</div>
      </div>
      <Handle type="target" position={Position.Left} />
      <Handle type="source" position={Position.Right} />
      <Handle type="target" id="PotiAdapter" position={Position.Bottom} isValidConnection={(c) => c.sourceHandle === 'PotiConnector'} />
    </div>
  );
}
