"""Expose the existing consensus algorithm as a local MCP tool over stdio."""

from typing import Any

from mcp.server.fastmcp import FastMCP

from client import GenParkReasoningMajorityVotingConsensusEngine

mcp = FastMCP("genpark-reasoning-majority-voting-consensus-engine-skill")
engine = GenParkReasoningMajorityVotingConsensusEngine()


@mcp.tool()
def execute_reasoning_majority_voting(
    candidate_rollouts: list[dict[str, Any]],
) -> dict[str, Any]:
    """Group supplied reasoning answers and return their weighted consensus."""
    return engine.resolve_majority_consensus(candidate_rollouts)


if __name__ == "__main__":
    mcp.run(transport="stdio")
