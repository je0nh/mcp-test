import os
import json
from fastmcp import FastMCP

mcp = FastMCP(name="mcp-test")

DOCS_DIR = "./documents"

@mcp.resource("config://app")
def get_config():
    return json.dumps({
        "version": "1.0",
        "description": "This is a test configuration for FastMCP.",
        "settings": {
            "option1": True,
            "option2": "value2",
            "option3": 12345
        }
    }, ensure_ascii=False)

@mcp.resource("docs://{filename}")
def get_documents(filename: str):
    path = os.path.join(DOCS_DIR, filename)
    if not os.path.exists(path):
        return json.dumps({"error": "File not found"})
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return content
