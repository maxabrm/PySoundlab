import { Handle, Position } from '@xyflow/react';
import '../App.css';

interface PotiNodeData {
  id: string;
  inputPin: string;
  resistance: number;
  maxValue: number;
}

export default function PotitNode({ data }: { data: PotiNodeData }) {
  return (
    <div className="node node--poti">
      <div className="node__header">Poti</div>
      <div className="node__body">
        <div className="node__info">{data.id}</div>
        <div className="node__info">Pin: {data.inputPin}</div>
      </div>
      <Handle type="source" position={Position.Top} id="PotiConnector" isValidConnection={(c) => c.targetHandle === 'PotiAdapter'} />
    </div>
  );
}
