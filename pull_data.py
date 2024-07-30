from marl_eval.json_tools import concatenate_json_files, pull_neptune_data

neptune_tags = [
        "mat-measure-set-benchmark-lbf",
        "mat-measure-set-benchmark-rware",
        "mat-measure-set-benchmark-smax",
        # "retmat-h2-benchmark-no-brax",
        # "retmat-simple-rewrite-h1-benchmark-no-xpos-no-brax",
        "ruan-measure-set-smax-benchmark",
        "rerun-mava-rec-systems-smax",
        "rware-measure-set-benchmark-small-lr",
        "rerun-mava-rec-systems-rware",
        # "lbf_best_hyperparams",
        # "retmat-h2-first-benchmark",
        # "mat-measure-set-benchmark-mabrax",
        # "vector-cleaner-measure-set-benchmark",
        "vector-connector-measure-set-benchmark",
        # "mat-measure-set-benchmark-vector-cleaner",
        "mat-measure-set-benchmark-vector-connector",
        # "retmat-simple-rewrite-hypothesis-1-benchmark-no-xpos",
        # "retmat-h2-first-benchmark",
        # "mat-measure-set-benchmark-mabrax",
        # "liam-mabrax-benchmark-ppo-2",
        "retmat-new-20M-sweep-benchmark",
    ]

for tag in neptune_tags:
    pull_neptune_data(
        project_name="InstaDeep/Mava",
        tags=[tag],
        store_directory="./data/full-benchmark-update",
    )

concatenate_json_files(
    input_directory="./data/full-benchmark-update",
    output_json_path="./data/full-benchmark-update/merged_data",
)
