# Visual Pipeline Builder — VectorShift Technical Assessment

## Overview
This project is a **Visual Pipeline Builder** that allows users to construct and validate processing pipelines using a node-based interface.

Users can:
- Create and connect different node types visually
- Define dynamic inputs using templated text (e.g. `{{input}}`)
- Submit the pipeline for server-side validation
- Receive feedback on node count, edge count, and DAG validity

---

## Tech Stack

### Frontend
- React (Create React App)
- React Flow

### Backend
- Python
- FastAPI

---

## Key Features

### 1. Scalable Node Abstraction
- Introduced a reusable `BaseNode` component to handle shared layout, styling, and handle positioning.
- Extracted form and state logic into custom hooks to avoid duplication.
- New node types can be created with minimal code by defining only unique fields.

---

### 2. Unified Styling System
- Implemented a lightweight design system using CSS variables.
- Centralized styles for nodes and buttons to ensure consistency and easy theming.

---

### 3. Dynamic Text Node Logic
- Text nodes automatically resize based on content.
- Template variables defined using `{{variable}}` syntax are parsed and converted into dynamic input handles.
- Logic is extracted into reusable hooks and optimized using memoization.

---

### 4. Frontend ↔ Backend Integration
- Frontend submits pipeline nodes and edges to the backend.
- Backend validates the pipeline by:
  - Counting nodes and edges
  - Detecting cycles using DFS to determine DAG validity
- Results are displayed using a custom modal for improved UX.

---
## Project Structure

```bash
├── frontend/
│ ├── src/
│ │ ├── nodes/
│ │ ├── hooks/
│ │ ├── submit.js
│ └── package.json
├── backend/
│ ├── main.py
│ └── requirements.txt
└── README.md
```

---

## How to Run Locally

### Frontend
```bash
cd frontend
npm install
npm start
```

The app will be available at:  
`http://localhost:3000`

---

## Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

The backend runs on:
`http://localhost:8000`

### Backend API Response Format

{
  "num_nodes": 5,
  "num_edges": 4,
  "is_dag": true
}

##Design Decisions
- ### DRY principle:
  Shared UI and logic extracted into reusable components and hooks.
- ### Separation of concerns:
  UI, state management, and parsing logic are clearly separated.
- ### Maintainability:
  Centralized styling and configuration-driven nodes.
- ### Robust UX:
  Custom modal used instead of browser alerts.

## Notes
- The application is designed to be run locally as per the assessment instructions.
- Deployment was intentionally kept optional to focus on code quality and architecture.
