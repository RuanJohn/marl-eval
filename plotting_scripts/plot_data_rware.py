# python3
# Copyright 2022 InstaDeep Ltd. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import os

import matplotlib.pyplot as plt

from marl_eval.plotting_tools.plotting import (
    aggregate_scores,
    performance_profiles,
    plot_single_task,
    probability_of_improvement,
    sample_efficiency_curves,
)
from marl_eval.utils.data_processing_utils import (
    create_matrices_for_rliable,
    data_process_pipeline,
)

base_folder_name = "cent-experiments-rware"
ENV_NAME = "RobotWarehouse"
SAVE_PDF = True

data_dir = f"data/{base_folder_name}/merged_data/metrics.json"
png_plot_dir = f"plots/{base_folder_name}/png/"
pdf_plot_dir = f"plots/{base_folder_name}/pdf/"

legend_map = {
    "ff_mappo": "MAPPO NN",
    "ff_ippo": "IPPO NN",
    "ff_ppo_central": "PPO Central NN",
}

##############################
# Read in and process data
##############################
METRICS_TO_NORMALIZE = ["mean_episode_return"]

with open(data_dir) as f:
    raw_data = json.load(f)

processed_data = data_process_pipeline(
    raw_data=raw_data, metrics_to_normalize=METRICS_TO_NORMALIZE
)

environment_comparison_matrix, sample_effeciency_matrix = create_matrices_for_rliable(
    data_dictionary=processed_data,
    environment_name=ENV_NAME,
    metrics_to_normalize=METRICS_TO_NORMALIZE,
)

# Create folder for storing plots
if not os.path.exists(png_plot_dir):
    os.makedirs(png_plot_dir)
if not os.path.exists(pdf_plot_dir):
    os.makedirs(pdf_plot_dir)


##############################
# Probability of improvement
# Aggregate scores
# Performance profiles
##############################

# These should be done with normalized data

# probability of improvement
fig = probability_of_improvement(
    environment_comparison_matrix,
    metric_name="mean_episode_return",
    metrics_to_normalize=METRICS_TO_NORMALIZE,
    algorithms_to_compare=[
        ["ff_ppo_central", "ff_ippo"],
        ["ff_ppo_central", "ff_mappo"],
        ["ff_mappo", "ff_ippo"],
    ],
    legend_map=legend_map,
)
fig.figure.savefig(f"{png_plot_dir}prob_of_improvement.png", bbox_inches="tight")
if SAVE_PDF:
    fig.figure.savefig(f"{pdf_plot_dir}prob_of_improvement.pdf", bbox_inches="tight")

# aggregate scores
fig, _, _ = aggregate_scores(  # type: ignore
    environment_comparison_matrix,
    metric_name="mean_episode_return",
    metrics_to_normalize=METRICS_TO_NORMALIZE,
    save_tabular_as_latex=True,
    legend_map=legend_map,
)
fig.figure.savefig(f"{png_plot_dir}aggregate_scores.png", bbox_inches="tight")
if SAVE_PDF:
    fig.figure.savefig(f"{pdf_plot_dir}aggregate_scores.pdf", bbox_inches="tight")

# performance profiles
fig = performance_profiles(
    environment_comparison_matrix,
    metric_name="mean_episode_return",
    metrics_to_normalize=METRICS_TO_NORMALIZE,
    legend_map=legend_map,
)
fig.figure.savefig(f"{png_plot_dir}performance_profile.png", bbox_inches="tight")
if SAVE_PDF:
    fig.figure.savefig(f"{pdf_plot_dir}performance_profile.pdf", bbox_inches="tight")


##############################
# Plot episode return data
##############################

# This should not be done with normalized data

METRICS_TO_NORMALIZE = []

with open(data_dir) as f:
    raw_data = json.load(f)

processed_data = data_process_pipeline(
    raw_data=raw_data, metrics_to_normalize=METRICS_TO_NORMALIZE
)

environment_comparison_matrix, sample_effeciency_matrix = create_matrices_for_rliable(
    data_dictionary=processed_data,
    environment_name=ENV_NAME,
    metrics_to_normalize=METRICS_TO_NORMALIZE,
)

# Get all tasks
tasks = list(processed_data[ENV_NAME.lower()].keys())

# Aggregate data over a single tasks
for task in tasks:
    fig = plot_single_task(
        processed_data=processed_data,
        environment_name=ENV_NAME,
        task_name=task,
        metric_name="mean_episode_return",
        metrics_to_normalize=METRICS_TO_NORMALIZE,
        legend_map=legend_map,
    )

    fig.figure.savefig(
        f"{png_plot_dir}rware_{task}_agg_return.png", bbox_inches="tight"
    )
    if SAVE_PDF:
        fig.figure.savefig(
            f"{pdf_plot_dir}rware_{task}_agg_return.pdf", bbox_inches="tight"
        )

    # Close the figure object
    plt.close(fig.figure)

# Aggregate data over all environment tasks.

fig, _, _ = sample_efficiency_curves(  # type: ignore
    sample_effeciency_matrix,
    metric_name="mean_episode_return",
    metrics_to_normalize=METRICS_TO_NORMALIZE,
    legend_map=legend_map,
)
fig.figure.savefig(
    f"{png_plot_dir}return_sample_effeciency_curve.png", bbox_inches="tight"
)
if SAVE_PDF:
    fig.figure.savefig(
        f"{pdf_plot_dir}return_sample_effeciency_curve.pdf", bbox_inches="tight"
    )
