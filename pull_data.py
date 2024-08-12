from marl_eval.json_tools import concatenate_json_files, pull_neptune_data

neptune_tags = [
    # "generalised-matrix-game-ppo",
    "generalised-matrix-game-tabular",
]

for tag in neptune_tags:
    pull_neptune_data(
        project_name="ruan-marl-masters/centralised-marl-msc",
        tags=[tag],
        store_directory="./data/gen-matrax-tabular",
    )

concatenate_json_files(
    input_directory="./data/gen-matrax-tabular",
    output_json_path="./data/gen-matrax-tabular/merged_data",
)
