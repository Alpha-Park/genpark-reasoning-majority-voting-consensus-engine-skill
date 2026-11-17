---
name: genpark-reasoning-majority-voting-consensus-engine-skill
description: Compare supplied candidate answers using normalization, token Jaccard similarity, and confidence-weighted voting.
category: Service
version: 1.0.0
license: MIT
tools:
  - execute_reasoning_majority_voting
---

# Genpark Reasoning Majority Voting Consensus Engine Skill

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Genpark Reasoning Majority Voting Consensus Engine Skill**.
Your primary directive is to execute: Compare supplied candidate answers using normalization, token Jaccard similarity, and confidence-weighted voting.
This skill does not generate rollouts or independently verify that an answer is correct.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `execute_reasoning_majority_voting`
- Direct client use supports standard-library-only environments. MCP server operation requires Python 3.10+ and the MCP SDK.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import GenParkReasoningMajorityVotingConsensusEngine

engine = GenParkReasoningMajorityVotingConsensusEngine()
result = engine.resolve_majority_consensus(candidate_rollouts)
```

### Option 2: FastMCP Tool Calling
Install dependencies with `python -m pip install -r requirements.txt` using Python 3.10+ in the environment selected by your MCP client.
Tools registered in `mcp_server.py`:
- `execute_reasoning_majority_voting`

## Core Mathematical & Algorithmic Guardrails
- **Dependencies**: The client uses only the Python standard library; the MCP server requires the official `mcp>=1.0.0,<2` SDK.
- **Interpretation**: Consensus confidence measures agreement among provided candidates, not proof of correctness.
