from typing import Optional, List
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("euvdb")

BASE_URL = "https://euvdservices.enisa.europa.eu/api"

@mcp.tool()
async def get_last_vulnerabilities() -> List[dict]:
    """Últimas vulnerabilidades reportadas (máx 8)."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/lastvulnerabilities")
        resp.raise_for_status()
        return resp.json()

@mcp.tool()
async def get_exploited_vulnerabilities() -> List[dict]:
    """Últimas vulnerabilidades explotadas (máx 8)."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/exploitedvulnerabilities")
        resp.raise_for_status()
        return resp.json()

@mcp.tool()
async def get_critical_vulnerabilities() -> List[dict]:
    """Últimas vulnerabilidades críticas (máx 8)."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/criticalvulnerabilities")
        resp.raise_for_status()
        return resp.json()

@mcp.tool()
async def get_vulnerability_by_id(id: str) -> dict:
    """Consulta una vulnerabilidad por ID (e.g. CVE-2024-0864)."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/vulnerability", params={"id": id})
        resp.raise_for_status()
        return resp.json()

@mcp.tool()
async def get_enisaid(id: str) -> dict:
    """Consulta una vulnerabilidad por ENISA ID (e.g. EUVD-2024-45012)."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/enisaid", params={"id": id})
        resp.raise_for_status()
        return resp.json()

@mcp.tool()
async def get_advisory(id: str) -> dict:
    """Consulta un aviso por ID (e.g. cisco-sa-xxx)."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/advisory", params={"id": id})
        resp.raise_for_status()
        return resp.json()

@mcp.tool()
async def query_vulnerabilities(
    fromScore: Optional[float] = None,
    toScore: Optional[float] = None,
    fromEpss: Optional[float] = None,
    toEpss: Optional[float] = None,
    fromDate: Optional[str] = None,
    toDate: Optional[str] = None,
    product: Optional[str] = None,
    vendor: Optional[str] = None,
    assigner: Optional[str] = None,
    exploited: Optional[bool] = None,
    page: Optional[int] = None,
    text: Optional[str] = None,
    size: Optional[int] = None
) -> List[dict]:
    """Consulta filtrada del catálogo de vulnerabilidades."""
    params = {
        "fromScore": fromScore,
        "toScore": toScore,
        "fromEpss": fromEpss,
        "toEpss": toEpss,
        "fromDate": fromDate,
        "toDate": toDate,
        "product": product,
        "vendor": vendor,
        "assigner": assigner,
        "exploited": str(exploited).lower() if exploited is not None else None,
        "page": page,
        "text": text,
        "size": size,
    }
    params = {k: v for k, v in params.items() if v is not None}

    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/vulnerabilities", params=params)
        resp.raise_for_status()
        return resp.json()

if __name__ == "__main__":
    mcp.run(transport="stdio")
