import { ReactFlow, useNodesState, useEdgesState } from '@xyflow/react';
import type { Node, Edge } from '@xyflow/react';
import '@xyflow/react/dist/style.css';
import AudioInputNode from './Nodes/AudioINputNode';
import AudioOutputNode from './Nodes/AudioOutputNode';

const nodeTypes = {
  audioInput: AudioInputNode,
  audioOutput: AudioOutputNode,
};

export default function App() {
  const [nodes, setNodes, onNodesChange] = useNodesState<Node>([]);
  const [edges, _, onEdgesChange] = useEdgesState<Edge>([]);

  function addNode(type: string) {
    const newNode = {
      id: crypto.randomUUID(),
      type,
      position: { x: 200, y: 200 },
      data: { inputPin: 'A0' },
    };
    setNodes((prev) => [...prev, newNode]);
  }

  return (
    <div style={{ display: 'flex', width: '100vw', height: '100vh' }}>
      <div style={{ width: '180px', background: '#1a1a2e', padding: '16px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
        <h3 style={{ color: 'white', margin: '0 0 12px 0' }}>Nodes</h3>
        <button onClick={() => addNode('audioInput')}>+ Audio Input</button>
        <button onClick={() => addNode('audioOutput')}>+ Audio Output</button>
      </div>
      <div style={{ flex: 1 }}>
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          nodeTypes={nodeTypes}
        />
      </div>
    </div>
  );
}