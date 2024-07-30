import json


def load_json(filename):
    with open(filename) as file:
        data = json.load(file)
    return data


# Save the modified data back into JSON
def save_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def adjust_win_rate(data):
    """Divide all win_rate metrics by 100."""
    for env_name, task_data in data.items():
        for task_name, alg_data in task_data.items():
            for algorithm_name, seed_data in alg_data.items():
                for seed_key, metrics in seed_data.items():
                    for key, step_data in metrics.items():
                        if "win_rate" in step_data:
                            # Divide the win_rate values by 100
                            step_data["win_rate"] = [
                                value / 100 for value in step_data["win_rate"]
                            ]

    return data


# Replace 'your_file.json' with your actual JSON file name
json_filename = "./data/full-benchmark-update/merged_data/metrics_stepcount_processed.json"
new_json_filename = "./data/full-benchmark-update/merged_data/metrics_winrate_processed.json"

data = load_json(json_filename)
processed_data = adjust_win_rate(data)
save_json(new_json_filename, processed_data)
