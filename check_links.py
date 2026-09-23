import json, urllib.request, sys, time
data=json.load(open("data/tools.json"))
failed=[]
for t in data:
    try:
        req=urllib.request.Request(t["url"],headers={"User-Agent":"AutoOps-LinkChecker/1.0"})
        with urllib.request.urlopen(req,timeout=15) as r:
            if r.status >= 400: failed.append((t["name"],r.status))
    except Exception as e:
        failed.append((t["name"],str(e)))
if failed:
    print("Link check failures:", failed)
    # Do not mutate production data. A failed check blocks deployment so bad data cannot publish.
    sys.exit(1)
print(f"Checked {len(data)} links successfully.")
