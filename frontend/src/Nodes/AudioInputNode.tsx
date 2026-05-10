import { Handle, Position } from '@xyflow/react';
import '../App.css';

interface AudioInputNodeData {
  inputPin: string;
}

export default function AudioInputNode({ data }: { data: AudioInputNodeData }) {
  return (
    <div className="node">
      <div className="node__header">Audio Input</div>
      <div className="node__body">
        <div className="node__info">Pin: {data.inputPin}</div>
      </div>
      <Handle type="source" position={Position.Right} />
    </div>
  );
}
