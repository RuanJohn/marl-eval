from marl_eval.json_tools import concatenate_json_files, pull_neptune_data

neptune_tags = [
    # "generalised-matrix-game-ppo",
    # "generalised-matrix-game-tabular",
    # "true-shadow-first-experiment",
    # "matrax-test-experiment",
    # "cent-experiments-matrax",
    # "explore-long-experiment",
    # "true-shadow-long-experiment-tpu-v4",
    # "cent-experiments-lbf",
    # "cent-experiments-rware",
    "cent-experiments-smax",
]

# base_folder_name = "matrax-climbing-full"
# base_folder_name = "explore-long-experiment"
# base_folder_name = "true-shadow-long-experiment-tpu-v4"
# base_folder_name = "cent-experiments-lbf"
# base_folder_name = "cent-experiments-rware"
base_folder_name = "cent-experiments-smax"

for tag in neptune_tags:
    pull_neptune_data(
        project_name="ruan-marl-masters/centralised-marl-msc",
        tags=[tag],
        store_directory=f"./data/{base_folder_name}",
    )

concatenate_json_files(
    input_directory=f"./data/{base_folder_name}",
    output_json_path=f"./data/{base_folder_name}/merged_data",
)
