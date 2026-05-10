import { Handle, Position } from '@xyflow/react';
import '../App.css';

interface AudioOutputNodeData {
  outputPin: string;
}

export default function AudioOutputNode({ data }: { data: AudioOutputNodeData }) {
  return (
    <div className="node">
      <div className="node__header">Audio Output</div>
      <div className="node__body">
        <div className="node__info">Pin: {data.outputPin}</div>
      </div>
      <Handle type="target" position={Position.Left} />
    </div>
  );
}
