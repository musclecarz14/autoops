import json
from pathlib import Path

p = Path("data/tools.json")
data = json.loads(p.read_text())

assert isinstance(data, list) and data, "tools.json must contain tools"

required = {"name", "category", "pricing", "description", "url"}
seen = set()

for i, tool in enumerate(data):
    missing = required - set(tool)

    assert not missing, f"Record {i} is missing: {missing}"
    assert tool["name"] not in seen, f"Duplicate tool: {tool['name']}"
    assert tool["url"].startswith(("https://", "http://")), f"Bad URL: {tool['url']}"
    assert len(tool["description"]) >= 20, f"Description too short: {tool['name']}"

    seen.add(tool["name"])

print(f"Validated {len(data)} tools.")
