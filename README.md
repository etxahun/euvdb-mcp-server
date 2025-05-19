# 🛡️ EUVDB MCP Server

Servidor MCP en Python que permite interactuar con la API pública de vulnerabilidades de ENISA (EUVDB) mediante el protocolo [Model Context Protocol (MCP)](https://modelcontextprotocol.io/).

Este servidor expone herramientas de consulta que pueden ser invocadas desde asistentes de IA compatibles con MCP, como Claude Desktop o Visual Studio Code (VSCode).

---

## 📁 Estructura del proyecto

```
euvdb-mcp-server/
├── server.py         # Servidor MCP con herramientas para consultar la API de ENISA
├── README.md         # Documentación del proyecto
└── pyproject.toml    # (opcional, si se usa uv como gestor)
```

---

## 🚀 Puesta en marcha

### 1. Clonar el repositorio

```bash
git clone https://github.com/etxahun/euvdb-mcp-server.git
cd euvdb-mcp-server
```

> Sustituye la URL si utilizas GitHub.

---

### 2. Crear entorno virtual e instalar dependencias

Requisitos: Python 3.10 o superior, y [`uv`](https://github.com/astral-sh/uv) como gestor de entorno (opcional pero recomendado).

```bash
# Instalar uv si no lo tienes
curl -LsSf https://astral.sh/uv/install.sh | sh

# Inicializar entorno
uv venv
source .venv/bin/activate

# Instalar dependencias
uv add "mcp[cli]" httpx
```

---

### 3. Ejecutar el servidor MCP

#### Opción A: Ejecución local

```bash
uv run server.py
```

#### Opción B: Desde WSL (Windows Subsystem for Linux)

```bash
wsl bash -c 'cd /ruta/a/euvdb-mcp-server && /home/<user>/.local/bin/uv run server.py'
```

---

## ⚙️ Integración con Claude en VSCode

1. Abre VSCode y asegúrate de tener instalada la extensión oficial de **Claude AI**.
2. Abre el archivo `settings.json` (`Ctrl+Shift+P` → "Preferences: Open Settings (JSON)").
3. Añade lo siguiente:

```json
"mcp.servers": {
  "euvdb": {
    "command": "wsl.exe",
    "args": [
      "bash",
      "-c",
      "cd /home/<user>/path/to/project/euvdb-mcp-server && /home/<user>/.local/bin/uv run server.py"
    ]
  }
}
```

---

## 🧪 Herramientas disponibles

El servidor MCP expone las siguientes herramientas:

| Herramienta                      | Descripción                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| `get_last_vulnerabilities()`     | Últimas vulnerabilidades publicadas (máx 8)                                |
| `get_exploited_vulnerabilities()`| Vulnerabilidades recientemente explotadas (máx 8)                          |
| `get_critical_vulnerabilities()` | Vulnerabilidades críticas más recientes (máx 8)                            |
| `get_vulnerability_by_id(id)`    | Consulta una vulnerabilidad por CVE ID (e.g. `CVE-2024-0864`)              |
| `get_enisaid(id)`                | Consulta por ENISA ID (e.g. `EUVD-2024-45012`)                              |
| `get_advisory(id)`               | Obtiene un aviso por su ID (e.g. `cisco-sa-ata19x-...`)                     |
| `query_vulnerabilities(...)`     | Consulta avanzada con filtros (por score, EPSS, fecha, producto, etc.)     |

---

## 💬 Ejemplos de prompts en Claude

- *“Consulta las últimas vulnerabilidades críticas usando `euvdb`.”*
- *“Busca la vulnerabilidad `CVE-2024-0864`.”*
- *“Filtra vulnerabilidades con score > 9 desde enero de 2024.”*
- *“Dame los avisos recientes relacionados con CISCO.”*

---

## 📄 Licencia

Este proyecto se distribuye bajo licencia Apache-2.0.

---

## 🤝 Créditos

Este servidor consulta la [API pública de vulnerabilidades de ENISA (EUVDB)](https://euvd.enisa.europa.eu/), de acceso libre y sin autenticación.
