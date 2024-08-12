import json

import numpy as np


def load_json(filename):
    with open(filename) as file:
        data = json.load(file)
    return data


# Save the modified data back into JSON
def save_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def interpolate_steps(data):
    for env_name, task_data in data.items():
        for task_name, alg_data in task_data.items():
            for algorithm_name, seed_data in alg_data.items():
                for seed_key, metrics in seed_data.items():
                    if seed_key == "absolute_metrics":
                        continue  # Skip absolute metrics

                    step_keys = sorted(
                        [key for key in metrics.keys() if key.startswith("step_")],
                        key=lambda x: int(x.split("_")[1]),
                    )
                    max_step_index = max(int(key.split("_")[1]) for key in step_keys)

                    if max_step_index < 121:
                    # if max_step_index < 199:
                        # Interpolation
                        x = np.array([int(k.split("_")[1]) for k in step_keys])
                        y_step_count = np.array(
                            [metrics[k]["step_count"] for k in step_keys]
                        )
                        y_elapsed_time = np.array(
                            [metrics[k]["elapsed_time"] for k in step_keys]
                        )

                        metric_keys = [
                            k
                            for k in metrics[step_keys[0]].keys()
                            if k
                            not in ["step_count", "elapsed_time", "steps_per_second"]
                        ]
                        y_metrics = {
                            metric: np.array([metrics[k][metric][0] for k in step_keys])
                            for metric in metric_keys
                        }

                        x_new = np.linspace(
                            0, max_step_index, 122
                        )  # Ensure covering up to step_121
                        # x_new = np.linspace(
                        #     0, max_step_index, 200
                        # )  # Ensure covering up to step_199
                        step_count_interp = np.interp(x_new, x, y_step_count)
                        elapsed_time_interp = np.interp(x_new, x, y_elapsed_time)
                        metrics_interp = {
                            metric: np.interp(x_new, x, y)
                            for metric, y in y_metrics.items()
                        }

                        # Update the data with interpolated values
                        for i in range(
                            len(x_new)
                        ):  # Adjusted to iterate over the new range
                            # Now directly using i to ensure step_121 is included
                            step_key = f"step_{i}"
                            metrics[step_key] = {
                                "step_count": int(step_count_interp[i]),
                                "elapsed_time": elapsed_time_interp[i],
                                "steps_per_second": metrics[step_keys[-1]][
                                    "steps_per_second"
                                ],  # Duplicating the last value
                            }
                            for metric, y in metrics_interp.items():
                                metrics[step_key][metric] = [y[i]]

    return data


# Replace 'your_file.json' with your actual JSON file name
json_filename = "./data/full-benchmark-update/merged_data/metrics_name_processed.json"
new_json_filename = "./data/full-benchmark-update/merged_data/metrics_stepcount_processed.json"

data = load_json(json_filename)
processed_data = interpolate_steps(data)
save_json(new_json_filename, processed_data)
