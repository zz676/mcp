#!/usr/bin/env python3
"""Wrapper to run mcp_server.py with the correct Python interpreter."""
import subprocess
import sys
from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent

# Path to the virtual environment's Python
venv_python = script_dir / ".venv" / "bin" / "python3"

# Path to the actual MCP server
mcp_server = script_dir / "mcp_server.py"

# Execute the MCP server with the venv Python
sys.exit(subprocess.call([str(venv_python), str(mcp_server)]))
