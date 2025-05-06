import json

# Path to your JSON file
json_file = "results/GhanaBase2060DV/GhanaBase2060DV.json"

# Load and inspect JSON
with open(json_file, "r") as f:
    data = json.load(f)

# Show top-level keys
print("Top-level keys in JSON:", list(data.keys()))

# Look into the Vars section
vars_data = data.get("Vars", [])
print(f"\n'Vars' is a {type(vars_data)} with {len(vars_data)} entries.")

# Print first 5 entries clearly
for i, item in enumerate(vars_data[:5]):
    print(f"\nEntry {i+1}:")
    for key, value in item.items():
        print(f"  {key}: {value}")

# Look for any fields besides 'VarName' and 'X'
extra_keys_found = set()

for item in vars_data:
    for key in item:
        if key not in {"VarName", "X"}:
            extra_keys_found.add(key)

print("\nExtra keys found in 'Vars':", extra_keys_found)
