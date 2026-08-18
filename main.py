import json

line = input()
# Parse the JSON, handle missing 'name' key, handle invalid JSON.
try:
    data = json.loads(line)
    print(data.get("name", "not found"))
except json.JSONDecodeError:
    print("invalid json")