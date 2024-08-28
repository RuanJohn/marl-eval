import json


# Load your JSON data
def load_json(filename):
    with open(filename) as file:
        data = json.load(file)
    return data


# Save the modified data back into JSON
def save_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def remove_retmat(data):
    # Iterate through each env_name
    for env_name, tasks in list(
        data.items()
    ):  # list() to allow modification during iteration
        # Iterate through each task_name
        for task_name, algorithms in list(tasks.items()):
            # If "retmat" is an algorithm under the current task, remove it
            if "ff_ippo" in algorithms:
                del data[env_name][task_name]["ff_ippo"]

            if "ff_mappo" in algorithms:
                del data[env_name][task_name]["ff_mappo"]

            if "ff_ppo_central" in algorithms:
                del data[env_name][task_name]["ff_ppo_central"]

            # if "retmat_cont" in algorithms:
            #     del data[env_name][task_name]["retmat_cont"]
            # If the task becomes empty after removing "retmat", consider removing the task
            # if not data[env_name][task_name]:
            #     del data[env_name][task_name]
            # Optionally, remove the env_name if it becomes empty
            # if not data[env_name]:
            #     del data[env_name]
    return data


# Main function to load, process, and save the JSON data
def main(json_filename, new_json_filename):
    data = load_json(json_filename)
    data = remove_retmat(data)
    save_json(new_json_filename, data)


# Replace 'your_file.json' with your actual JSON file name
# json_filename = "./data/full-benchmark-update/merged_data/metrics_winrate_processed.json"
# new_json_filename = "./data/full-benchmark-update/merged_data/metrics_winrate_processed_no_retmat.json"

base_folder_name = "shadow-long-experiment"

json_filename = f"./data/{base_folder_name}/merged_data/metrics.json"
new_json_filename = f"./data/{base_folder_name}/merged_data/metrics.json"

main(json_filename, new_json_filename)
