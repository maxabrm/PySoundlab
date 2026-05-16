import { ReactFlow, useNodesState, useEdgesState, addEdge } from '@xyflow/react';
import type { Node, Edge, Connection } from '@xyflow/react';
import '@xyflow/react/dist/style.css';
import './App.css';
import AudioInputNode from './Nodes/AudioInputNode';
import AudioOutputNode from './Nodes/AudioOutputNode';
import PotitNode from './Nodes/PotiNode';
import DelayNode from './Nodes/DelayNode';
import FilterNode from './Nodes/FilterNode';
import GainNode from './Nodes/GainNode';
import ReverbNode from './Nodes/ReverbNode';
import { useState }  from 'react';
import { buildGraphPayload } from './utils/buildGraphPayload';

const nodeTypes = {
  AudioInput: AudioInputNode,
  AudioOutput: AudioOutputNode,
  Poti: PotitNode,
  Delay: DelayNode,
  Filter: FilterNode,
  Gain: GainNode,
  Reverb: ReverbNode,
};

export default function App() {
  const [nodes, setNodes, onNodesChange] = useNodesState<Node>([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState<Edge>([]);
  const [selectedNode, setSelectedNode] = useState<Node | null>(null);
  const [nodeCounters, setNodeCounters] = useState<Record<string, number>>({});
  const [generatedCode, setGeneratedCode] = useState('');
  const [copied, setCopied] = useState(false);

  function copyCode() {
    if (!generatedCode) return;
    navigator.clipboard.writeText(generatedCode);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  }

  async function generateCode() {
    const payload = buildGraphPayload(nodes, edges);
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
    Reverb:      { roomSize: 50 },
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
    <div className="app">

      <div className="sidebar">
        <h3 className="panel-title">Nodes</h3>
        <button onClick={() => addNode('AudioInput')}>+ Audio Input</button>
        <button onClick={() => addNode('AudioOutput')}>+ Audio Output</button>
        <button onClick={() => addNode('Poti')}>+ Poti</button>
        <button onClick={() => addNode('Delay')}>+ Delay</button>
        <button onClick={() => addNode('Filter')}>+ Filter</button>
        <button onClick={() => addNode('Gain')}>+ Gain</button>
        <button onClick={() => addNode('Reverb')}>+ Reverb</button>
      </div>

      <div className="canvas">
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

      <div className="right-panel">

        <div className="node-editor">
          <h3 className="panel-title">Node Editor</h3>
          {selectedNode ? (
            <div className="node-editor__fields">
              <p className="node-editor__type">{selectedNode.type}</p>
              {Object.entries(selectedNode.data).map(([key, value]) => (
                <div key={key} className="node-editor__field">
                  <label className="node-editor__label">{key}</label>
                  <input
                    className="node-editor__input"
                    type={typeof value === 'number' ? 'number' : 'text'}
                    value={value as string}
                    onChange={(e) => updateNodeData(key, e.target.value)}
                  />
                </div>
              ))}
            </div>
          ) : (
            <p className="node-editor__empty">Keine Node ausgewählt</p>
          )}
        </div>

        <div className="code-panel">
          <h3 className="panel-title">Code</h3>
          <button onClick={generateCode}>Code generieren</button>
          <div className="code-display-wrapper">
            <button className="copy-btn" onClick={copyCode}>
              {copied ? '✓' : '⧉'}
            </button>
            <pre className="code-display">
              {generatedCode || '// Hier steht bald Code!'}
            </pre>
          </div>
        </div>

      </div>
    </div>
  );
}
