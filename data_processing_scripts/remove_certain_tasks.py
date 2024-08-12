import json


def filter_json(data, tasks_to_remove):
    filtered_data = {}
    for env_name, env_tasks in data.items():
        filtered_env_tasks = {}
        for task_name, task_algos in env_tasks.items():
            if task_name not in tasks_to_remove:
                filtered_env_tasks[task_name] = task_algos
        if filtered_env_tasks:
            filtered_data[env_name] = filtered_env_tasks
    return filtered_data


# Example usage:
input_file = "data/gen-matrax-ppo/merged_data/metrics.json"
output_file = "data/gen-matrax-ppo/merged_data/metrics.json"
tasks_to_remove = [
    "matrax-4-ag-4-act",
]  # Replace with your list of tasks to remove

# Read the input JSON file
with open(input_file, "r") as f:
    data = json.load(f)

# Filter the data
filtered_data = filter_json(data, tasks_to_remove)

# Write the filtered data to the output JSON file
with open(output_file, "w") as f:
    json.dump(filtered_data, f, indent=2)