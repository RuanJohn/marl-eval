import json


def rename_algorithms(data):
    rename_map = {
        "retmat_cont": "retmat",
        "retmat_cont_memory": "retmat_memory",
        "mat_cont": "mat"
    }

    for env_name in data:
        for task_name in data[env_name]:
            algos_to_rename = list(set(data[env_name][task_name].keys()) & set(rename_map.keys()))
            for old_name in algos_to_rename:
                new_name = rename_map[old_name]
                data[env_name][task_name][new_name] = data[env_name][task_name].pop(old_name)
                print(f"Renamed {old_name} to {new_name} in {env_name}/{task_name}")

# Load the JSON file
file_path = 'data/full-benchmark-update/merged_data/interim_seed_duplicated.json'  # Replace with your actual file path
with open(file_path, 'r') as file:
    data = json.load(file)

# Rename the algorithms
rename_algorithms(data)

# Save the modified data back to the JSON file
with open(file_path, 'w') as file:
    json.dump(data, file, indent=2)

print("JSON file has been updated with renamed algorithms.")