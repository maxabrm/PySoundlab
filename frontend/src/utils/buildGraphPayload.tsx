import type { Node, Edge } from '@xyflow/react';

export function buildGraphPayload(nodes: Node[], edges: Edge[]) {
  type NodeData = Record<string, unknown>;

  // Node zu Poti ermitteln
  const potiByTarget: Record<string, Node> = {};
  const potiEdgeIds = new Set<string>();

  const potiNodes = new Set(nodes.filter((n) => n.type === 'Poti').map((n) => n.id));

  for (const edge of edges) {
    if (potiNodes.has(edge.source)) {
      const potiNode = nodes.find((n) => n.id === edge.source)!;
      potiByTarget[edge.target] = potiNode;
      potiEdgeIds.add(edge.id);
    }
  }

  const mappedNodes = nodes
    .filter((n) => n.type !== 'Poti')
    .map((n) => {
      const d = n.data as NodeData;
      const base = { id: n.id };

      // Poti in Node einbinden
      const poti = potiByTarget[n.id];
      const potiField = poti
        ? (() => {
            const pd = poti.data as NodeData;
            return { id: poti.id, inputPin: pd.inputPin, resistance: Number(pd.resistance), maxValue: Number(pd.maxValue) };
          })()
        : undefined;

      if (n.type === 'AudioInput') return { ...base, type: 'AudioInput', inputPin: d.inputPin, Poti: potiField };
      if (n.type === 'AudioOutput') return { ...base, type: 'AudioOutput', inputPin: d.outputPin, Poti: potiField };
      if (n.type === 'Gain') return { ...base, type: 'Gain', parameter: Number(d.gain), Poti: potiField };
      if (n.type === 'Filter') return { ...base, type: 'Filter', parameter: Number(d.frequency), Poti: potiField };
      if (n.type === 'Delay') return { ...base, type: 'Delay', parameter: Number(d.delayTime), Poti: potiField };
    });

  // Connections ermitteln ohne Poti Connections
  const connections = edges
    .filter((e) => !potiEdgeIds.has(e.id))
    .map((e, i) => ({ id: i, node1_id: e.source, node2_id: e.target }));

  return { nodes: mappedNodes, connections };
}
