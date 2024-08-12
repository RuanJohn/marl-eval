import json


def filter_json(data, tasks_to_keep):
    filtered_data = {}
    for env_name, env_tasks in data.items():
        kept_tasks = {task: info for task, info in env_tasks.items() if task in tasks_to_keep}
        if kept_tasks:
            filtered_data[env_name] = kept_tasks
    return filtered_data

# Example usage:
input_file = 'data/limited_benchmark/retmat-mat-ppo/merged_data/metrics_winrate_processed.json'
output_file = 'data/limited_benchmark/retmat-mat-ppo/merged_data/task_name_processed.json'
tasks_to_keep = [
    'tiny-4ag',
    'small-4ag',
    '5m_vs_6m',
    '27m_vs_30m',
    'smacv2_10_units',
    '15x15-3p-5f',
    '15x15-4p-5f',
    '6h_vs_8z',
]  # Replace with your list of tasks to keep

# Read the input JSON file
with open(input_file, 'r') as f:
    data = json.load(f)

# Filter the data
filtered_data = filter_json(data, tasks_to_keep)

# Write the filtered data to the output JSON file
with open(output_file, 'w') as f:
    json.dump(filtered_data, f, indent=2)

print(f"Filtered data has been written to {output_file}")