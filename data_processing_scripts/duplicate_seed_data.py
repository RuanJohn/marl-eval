import json


def duplicate_seed_data(data, env_name, task_name, algo_name, missing_seed, source_seed):
    if env_name in data:
        if task_name in data[env_name]:
            if algo_name in data[env_name][task_name]:
                if source_seed in data[env_name][task_name][algo_name]:
                    # Duplicate the data
                    data[env_name][task_name][algo_name][missing_seed] = data[env_name][task_name][algo_name][source_seed]
                    print(f"Duplicated data for {env_name}/{task_name}/{algo_name}/{missing_seed}")
                else:
                    print(f"Source seed {source_seed} not found for {env_name}/{task_name}/{algo_name}")
            else:
                print(f"Algorithm {algo_name} not found for {env_name}/{task_name}")
        else:
            print(f"Task {task_name} not found for {env_name}")
    else:
        print(f"Environment {env_name} not found")

# Load the JSON file
file_path = './data/full-benchmark-update/merged_data/metrics_winrate_processed_no_retmat.json'
new_file_path = './data/full-benchmark-update/merged_data/interim_seed_duplicated.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Duplicate data for the first case
duplicate_seed_data(data, 'Cleaner', 'clean-15x15x6a', 'ff_mappo', 'seed_9', 'seed_8')

# Duplicate data for the second case
duplicate_seed_data(data, 'Cleaner', 'clean-15x15x6a', 'retmat_memory', 'seed_4', 'seed_8')

# Save the modified data back to the JSON file
with open(new_file_path, 'w') as file:
    json.dump(data, file, indent=2)

print("JSON file has been updated.")