import json, urllib.request, sys
from pathlib import Path

p=Path("data/tools.json")
data=json.loads(p.read_text())
assert isinstance(data,list) and data, "tools.json must contain tools"
required={"name","category","pricing","description","url"}
seen=set()
for i,t in enumerate(data):
    missing=required-set(t)
    assert not missing, f"record {i} missing {missing}"
    assert t["name"] not in seen, f"duplicate tool: {t['name']}"
    seen.add(t["name"])
    assert t["url"].startswith(("https://","http://")), f"bad URL: {t['url']}"
    assert len(t["description"]) >= 20, f"description too short: {t['name']}"
print(f"Validated {len(data)} tools.")
