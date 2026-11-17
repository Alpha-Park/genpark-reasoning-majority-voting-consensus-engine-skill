# genpark-reasoning-majority-voting-consensus-engine-skill

Combine candidate answers using the existing Python client's answer normalization, token Jaccard similarity, and confidence-weighted voting. The result includes the winning normalized answer, vote percentages, and cluster breakdown.

This tool compares answers supplied by the caller. It does not generate reasoning rollouts, prove answers correct, or call a language model. Its confidence percentage measures agreement within the supplied candidates.

## Direct Python Client

The core client uses only the Python standard library:

```python
from client import GenParkReasoningMajorityVotingConsensusEngine

engine = GenParkReasoningMajorityVotingConsensusEngine()
result = engine.resolve_majority_consensus([
    {"rollout_id": "a", "output_text": "Answer = 42", "confidence_score": 0.9},
    {"rollout_id": "b", "output_text": "42", "confidence_score": 0.8},
])
print(result)
```

## Local MCP Setup

The MCP server exposes `execute_reasoning_majority_voting`, which passes `candidate_rollouts` to the client's consensus algorithm. Running the server requires **Python 3.10+** and the official **`mcp>=1.0.0,<2` SDK**. From the repository directory:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python mcp_server.py
```

On Windows, use `.venv\Scripts\python.exe` instead. The server waits for MCP messages over stdio; it does not expose a public HTTP endpoint.

For Claude Desktop or another MCP client, replace the absolute paths below with your checkout and its environment's Python executable:

```json
{
  "mcpServers": {
    "genpark-reasoning-majority-voting-consensus-engine-skill": {
      "command": "/absolute/path/to/genpark-reasoning-majority-voting-consensus-engine-skill/.venv/bin/python",
      "args": ["/absolute/path/to/genpark-reasoning-majority-voting-consensus-engine-skill/mcp_server.py"]
    }
  }
}
```

Verify the connection by completing `initialize` and requesting `tools/list` from an MCP client. The GitHub repository URL is a source-code location, not an MCP server URL.

## License

MIT. See [LICENSE](LICENSE).
