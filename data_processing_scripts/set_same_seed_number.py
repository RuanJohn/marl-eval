import json
import random


def standardize_seeds(data, num_seeds=5):
    for env_name, env_data in data.items():
        for task_name, task_data in env_data.items():
            for algo_name, algo_data in task_data.items():
                # Get all existing seeds
                existing_seeds = list(algo_data.keys())

                # Print the original count
                print(
                    f"{env_name}/{task_name}/{algo_name}: Before: {len(existing_seeds)}",
                    end="",
                )

                # If we have more than num_seeds, randomly select num_seeds
                if len(existing_seeds) > num_seeds:
                    selected_seeds = random.sample(existing_seeds, num_seeds)
                else:
                    # If we have less than or equal to num_seeds, use all existing seeds
                    selected_seeds = existing_seeds

                # Create a new dictionary with standardized seed names
                new_algo_data = {}
                for i, seed in enumerate(selected_seeds):
                    new_algo_data[f"seed_{i}"] = algo_data[seed]

                # Replace the old algo_data with the new one
                task_data[algo_name] = new_algo_data

                # Print the new count
                print(f", After: {len(new_algo_data)}")

    return data


base_folder_name = "cent-experiments-smax"

# Replace 'your_file.json' with your actual JSON file name
json_filename = f"./data/{base_folder_name}/merged_data/metrics.json"
new_json_filename = f"./data/{base_folder_name}/merged_data/metrics.json"

# Load the JSON file
with open(json_filename, "r") as f:
    data = json.load(f)

print("Processing and standardizing seeds:")
# Standardize the seeds
standardized_data = standardize_seeds(data, num_seeds=6)

# Save the result to a new JSON file
with open(new_json_filename, "w") as f:
    json.dump(standardized_data, f, indent=2)

print("\nProcessing complete. Check 'metrics_seed_processed.json' for the result.")
