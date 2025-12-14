from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Node(BaseModel):
    id: str
    type: str
    position: Dict[str, float]
    data: Dict[str, Any]

class Edge(BaseModel):
    id: str
    source: str
    target: str
    sourceHandle: str | None = None
    targetHandle: str | None = None

class PipelineData(BaseModel):
    nodes: List[Node]
    edges: List[Edge]

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.post('/pipelines/parse')
def parse_pipeline(pipeline: PipelineData):
    num_nodes = len(pipeline.nodes)
    num_edges = len(pipeline.edges)
    
    # Build adjacency list for DAG check
    adj_list = {node.id: [] for node in pipeline.nodes}
    for edge in pipeline.edges:
        if edge.source in adj_list:
            adj_list[edge.source].append(edge.target)
    
    # Check for cycles using DFS
    def is_dag(nodes, adj_list):
        visited = set()
        recursion_stack = set()
        
        def dfs(node):
            visited.add(node)
            recursion_stack.add(node)
            
            for neighbor in adj_list.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in recursion_stack:
                    return True
            
            recursion_stack.remove(node)
            return False
        
        for node in nodes:
            if node not in visited:
                if dfs(node):
                    return False # Cycle detected
        return True

    is_dag_result = is_dag([n.id for n in pipeline.nodes], adj_list)
    
    return {'num_nodes': num_nodes, 'num_edges': num_edges, 'is_dag': is_dag_result}
