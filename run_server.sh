#!/bin/bash
# Wrapper script to run MCP server with the virtual environment's Python

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Use the virtual environment's Python
exec "$SCRIPT_DIR/.venv/bin/python3" "$SCRIPT_DIR/mcp_server.py"
