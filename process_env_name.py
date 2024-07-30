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


# Merge "HeuristicEnemySMAX" into "Smax"
def merge_data(data):
    if "HeuristicEnemySMAX" in data and "Smax" in data:
        # Iterate through the task_names in "HeuristicEnemySMAX"
        for task_name, algorithms in data["HeuristicEnemySMAX"].items():
            if task_name not in data["Smax"]:
                # If task_name does not exist in "Smax", add it
                data["Smax"][task_name] = algorithms
            else:
                # If task_name exists, merge the algorithm_name data
                for algorithm_name, seeds in algorithms.items():
                    if algorithm_name not in data["Smax"][task_name]:
                        data["Smax"][task_name][algorithm_name] = seeds
                    else:
                        # Merge seed data
                        data["Smax"][task_name][algorithm_name].update(seeds)
        # Remove "HeuristicEnemySMAX" from the data
        del data["HeuristicEnemySMAX"]
    return data


# Merge "RobotWarehouse-v0" into "RobotWarehouse"
def merge_data_rware(data):
    if "RobotWarehouse-v0" in data and "RobotWarehouse" in data:
        # Iterate through the task_names in "HeuristicEnemySMAX"
        for task_name, algorithms in data["RobotWarehouse-v0"].items():
            if task_name not in data["RobotWarehouse"]:
                # If task_name does not exist in "Smax", add it
                data["RobotWarehouse"][task_name] = algorithms
            else:
                # If task_name exists, merge the algorithm_name data
                for algorithm_name, seeds in algorithms.items():
                    if algorithm_name not in data["RobotWarehouse"][task_name]:
                        data["RobotWarehouse"][task_name][algorithm_name] = seeds
                    else:
                        # Merge seed data
                        data["RobotWarehouse"][task_name][algorithm_name].update(seeds)
        # Remove "RobotWarehouse-v0" from the data
        del data["RobotWarehouse-v0"]
    return data


# Merge "LevelBasedForaging-v0" into "LevelBasedForaging"
def merge_data_lbf(data):
    if "LevelBasedForaging-v0" in data and "LevelBasedForaging" in data:
        # Iterate through the task_names in "HeuristicEnemySMAX"
        for task_name, algorithms in data["LevelBasedForaging-v0"].items():
            if task_name not in data["LevelBasedForaging"]:
                # If task_name does not exist in "Smax", add it
                data["LevelBasedForaging"][task_name] = algorithms
            else:
                # If task_name exists, merge the algorithm_name data
                for algorithm_name, seeds in algorithms.items():
                    if algorithm_name not in data["LevelBasedForaging"][task_name]:
                        data["LevelBasedForaging"][task_name][algorithm_name] = seeds
                    else:
                        # Merge seed data
                        data["LevelBasedForaging"][task_name][algorithm_name].update(
                            seeds
                        )
        # Remove "RobotWarehouse-v0" from the data
        del data["LevelBasedForaging-v0"]
    return data


# Main function to load, process, and save the JSON data
def main(json_filename, new_json_filename):
    data = load_json(json_filename)
    data = merge_data(data)
    data = merge_data_rware(data)
    data = merge_data_lbf(data)
    save_json(new_json_filename, data)


# Replace 'your_file.json' with your actual JSON file name
json_filename = (
    "./data/full-benchmark-update/merged_data/metrics.json"
)
new_json_filename = "./data/full-benchmark-update/merged_data/metrics_name_processed.json"
main(json_filename, new_json_filename)
