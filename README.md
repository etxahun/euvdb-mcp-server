# 🛡️ EUVDB MCP Server

MCP Server in Python to interact with the [ENISA EUVDB Public Vulnerability API](https://euvd.enisa.europa.eu/), using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/).

This server exposes query tools that can be invoked from MCP-compatible AI assistants like Claude Desktop or Visual Studio Code (VSCode).



## 📁 Project Structure

```
euvdb-mcp-server/
├── Dockerfile # Dockerfile to build the Docker image of the project
├── LICENSE # Project license
├── README.md # Project documentation
├── server.py # MCP server with tools to query the ENISA API
└── pyproject.toml # (optional, if using uv as package manager)
```



## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/etxahun/euvdb-mcp-server.git
cd euvdb-mcp-server
```

### 2. Create virtual environment and install dependencies
**Requirements**: Python 3.10 or higher, and [uv](https://github.com/astral-sh/uv) as environment manager (optional but recommended).

```bash
# Install uv if not already available
curl -LsSf https://astral.sh/uv/install.sh | sh

# Initialize virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv add "mcp[cli]" httpx
```

### 3. Run the MCP server
* **Option A**: Run locally
  ```bash
  uv run server.py
  ```

* **Option B**: From WSL (Windows Subsystem for Linux)
  ```bash
  wsl bash -c 'cd /path/to/euvdb-mcp-server && /home/<user>/.local/bin/uv run server.py'
  ```



## 🧪 Test locally with Docker

Run the following commands from the terminal:

```bash
docker build -t mcp-euvdb .
docker run --rm mcp-euvdb
```



## ⚙️ Integration with Claude in VSCode

1. Open VSCode and ensure the Claude AI Assistant extension is installed.

* **Note**: If you are using "Claude Desktop", installing the extension is not necessary.

2. Open settings.json (Ctrl+Shift+P → "Preferences: Open Settings (JSON)").

3. Add the following:

```json
"mcp": {
    "servers": {
        "euvdb": {
            "command": "wsl.exe",
            "args": [
                "bash",
                "-c",
                "cd /home/<user>/path/to/project/euvdb-mcp-server && /home/<user>/.local/bin/uv run server.py"
            ]
        }
     }
}
```

If the Docker image **mcp-euvdb** has already been built, you can configure **VSCode** to use it directly by modifying the **settings.json** file as follows:

```json
"mcp": {
    "servers": {
        "euvdb": {
           "command": "wsl.exe",
           "args": [
               "docker",
               "run",
               "--rm",
               "-i",
               "mcp-euvdb"
           ]
        }
     }
}
```



## 🧪 Available Tools

The MCP server exposes the following tools:

| Tool                             | Descripction                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| `get_last_vulnerabilities()`     | Latest published vulnerabilities (max 8)                                 
| `get_exploited_vulnerabilities()`| Recently exploited vulnerabilities (max 8)                          |
| `get_critical_vulnerabilities()` | Latest critical vulnerabilities (max 8)                            |
| `get_vulnerability_by_id(id)`    | Query a vulnerability by CVE ID (e.g., CVE-2024-0864)              |
| `get_enisaid(id)`                | Query by ENISA ID (e.g., EUVD-2024-45012)                              |
| `get_advisory(id)`               | Fetch advisory by ID (e.g., cisco-sa-ata19x-...)                     |
| `query_vulnerabilities(...)`     | Advanced query with filters (score, EPSS, date, product, etc.)     |



## 💬 Prompt Examples

* “Query the latest critical vulnerabilities using euvdb.”
* “Look up vulnerability CVE-2024-0864.”
* “Filter vulnerabilities with score > 9 since January 2024.”
* “Show recent advisories related to CISCO.”



## 📄 License

This project is licensed under Apache-2.0.

 

## 🤝 Credits

This server interacts with the [ENISA EUVDB Public Vulnerability API](https://euvd.enisa.europa.eu/), which is open and does not require authentication.

