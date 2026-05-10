import { ReactFlow, useNodesState, useEdgesState, addEdge } from '@xyflow/react';
import type { Node, Edge, Connection } from '@xyflow/react';
import '@xyflow/react/dist/style.css';
import AudioInputNode from './Nodes/AudioInputNode';
import AudioOutputNode from './Nodes/AudioOutputNode';
import PotitNode from './Nodes/PotiNode';
import DelayNode from './Nodes/DelayNode';
import FilterNode from './Nodes/FilterNode';
import GainNode from './Nodes/GainNode';
import { useState } from 'react';
import { buildGraphPayload } from './utils/buildGraphPayload';

const nodeTypes = {
  AudioInput: AudioInputNode,
  AudioOutput: AudioOutputNode,
  Poti: PotitNode,
  Delay: DelayNode,
  Filter: FilterNode,
  Gain: GainNode,
};

export default function App() {
  const [nodes, setNodes, onNodesChange] = useNodesState<Node>([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState<Edge>([]);
  const [selectedNode, setSelectedNode] = useState<Node | null>(null);
  const [nodeCounters, setNodeCounters] = useState<Record<string, number>>({});
  const [generatedCode, setGeneratedCode] = useState('');

  async function generateCode() {
    const payload = buildGraphPayload(nodes, edges);
    console.log('Payload:', JSON.stringify(payload, null, 2));
    try {
      const res = await fetch('http://localhost:8000/graph/generateCode', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
      if (!res.ok) {
        const err = await res.text();
        console.error('Backend error:', res.status, err);
        setGeneratedCode(`Fehler ${res.status}: ${err}`);
        return;
      }
      const data = await res.json();
      console.log('Code raw:', JSON.stringify(data.code));
      setGeneratedCode(data.code ?? '');
    } catch (e) {
      console.error('Fetch failed:', e);
      setGeneratedCode(`Verbindungsfehler: ${e}`);
    }
  }

  function onConnect(connection: Connection) {
    setEdges((prev) => addEdge(connection, prev));
  }

  function onNodeClick(_: React.MouseEvent, node: Node) {
    setSelectedNode(node);
  }

  const defaultData: Record<string, Record<string, unknown>> = {
    AudioInput:  { inputPin: 'A0' },
    AudioOutput: { outputPin: 'A1' },
    Poti:        { inputPin: 'A0', resistance: 10000, maxValue: 1023 },
    Filter:      { frequency: 1000 },
    Gain:        { gain: 1.0 },
    Delay:       { delayTime: 100 },
  };

  function addNode(type: string) {
    const count = (nodeCounters[type] ?? 0) + 1;
    const id = `${type}${count}`;
    setNodeCounters((prev) => ({ ...prev, [type]: count }));
    setNodes((prev) => [...prev, {
      id,
      type,
      position: { x: 200, y: 200 },
      data: { id, ...defaultData[type] },
    }]);
  }

  function updateNodeData(key: string, value: string) {
    if (!selectedNode) return;
    setNodes((prev) => prev.map((n) =>
      n.id === selectedNode.id ? { ...n, data: { ...n.data, [key]: value } } : n
    ));
    setSelectedNode((prev) => prev ? { ...prev, data: { ...prev.data, [key]: value } } : null);
  }

  return (
    <div style={{ display: 'flex', width: '100vw', height: '100vh' }}>

      {/* Linke Sidebar */}
      <div style={{ width: '180px', background: 'darkblue', padding: '16px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
        <h3 style={{ color: 'white', margin: '0 0 12px 0' }}>Nodes</h3>
        <button onClick={() => addNode('AudioInput')}>+ Audio Input</button>
        <button onClick={() => addNode('AudioOutput')}>+ Audio Output</button>
        <button onClick={() => addNode('Poti')}>+ Poti</button>
        <button onClick={() => addNode('Delay')}>+ Delay</button>
        <button onClick={() => addNode('Filter')}>+ Filter</button>
        <button onClick={() => addNode('Gain')}>+ Gain</button>
      </div>

      {/* Canvas */}
      <div style={{ flex: 1 }}>
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onConnect={onConnect}
          onNodeClick={onNodeClick}
          nodeTypes={nodeTypes}
        />
      </div>

      {/* Rechtes Panel */}
      <div style={{ width: '220px', background: 'darkblue', display: 'flex', flexDirection: 'column' }}>

        {/* Node Editor*/}
        <div style={{ height: '30%', padding: '16px', borderBottom: '1px solid #333', overflowY: 'auto' }}>
          <h3 style={{ color: 'white', margin: '0 0 12px 0' }}>Node Editor</h3>
          {selectedNode ? (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <p style={{ color: '#aaa', margin: 0 }}>{selectedNode.type}</p>
              {Object.entries(selectedNode.data).map(([key, value]) => (
                <div key={key} style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  <label style={{ color: '#aaa', fontSize: '12px' }}>{key}</label>
                  <input
                    type={typeof value === 'number' ? 'number' : 'text'}
                    value={value as string}
                    onChange={(e) => updateNodeData(key, e.target.value)}
                    style={{ padding: '4px', borderRadius: '4px', border: '1px solid #555', background: '#2a2a3e', color: 'white' }}
                  />
                </div>
              ))}
            </div>
          ) : (
            <p style={{ color: '#555', fontSize: '12px' }}>Keine Node ausgewählt</p>
          )}
        </div>

        {/* Code Fenster */}
        <div style={{ height: '70%', padding: '16px', overflowY: 'auto' }}>
          <h3 style={{ color: 'white', margin: '0 0 12px 0' }}>Code</h3>
          <button style={{ marginBottom: '8px' }} onClick={generateCode}>
            Code generieren
          </button>
          <pre style={{ height: '70%', overflowY: 'auto', background: '#282c34', color: '#abb2bf', borderRadius: '4px', fontSize: '12px', padding: '8px', margin: 0, whiteSpace: 'pre' }}>
            {generatedCode || '// Hier steht bald Code!'}
          </pre>
        </div>

      </div>
    </div>
  );
}
