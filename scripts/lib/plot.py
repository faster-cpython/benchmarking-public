from pathlib import Path
from typing import Any, Dict


from matplotlib import pyplot as plt
import matplotlib
import numpy as np


matplotlib.use("agg")


from lib import result


def get_data(result: result.Result) -> Dict[str, Any]:
    results = {}

    for benchmark in result.contents["benchmarks"]:
        if "metadata" in benchmark:
            name = benchmark["metadata"]["name"]
        else:
            name = result.contents["metadata"]["name"]
        data = []
        for run in benchmark["runs"]:
            data.extend(run.get("values", []))
        results[name] = np.array(data, dtype=np.float64)

    return results


def remove_outliers(values, m=2):
    return values[abs(values - np.mean(values)) < m * np.std(values)]


def plot_diff_pair(ax, data):
    master_data = []
    all_data = []

    for name, values, mean in data:
        idx = np.round(np.linspace(0, len(values) - 1, 100)).astype(int)
        all_data.append(values[idx])
        master_data.extend(values)

    all_data.append(master_data)

    violin = ax.violinplot(
        all_data,
        vert=False,
        showmeans=True,
        showmedians=False,
        widths=1.0,
        quantiles=[[0.1, 0.9]] * len(all_data),
    )

    violin["cquantiles"].set_linestyle(":")

    return master_data


def formatter(val, pos):
    return f"{val:.02f}x"


def calculate_diffs(ref_values, head_values, outlier_rejection=True):
    if outlier_rejection:
        ref_values = remove_outliers(ref_values)
        head_values = remove_outliers(head_values)
    values = np.outer(ref_values, 1.0 / head_values).flatten()
    values.sort()
    return values, values.mean()


def plot_diff(
    ref: result.Result, head: result.Result, output_filename: Path, title: str
) -> None:
    ref_data = get_data(ref)
    head_data = get_data(head)

    combined_data = [
        (name, *calculate_diffs(ref, head_data[name]))
        for name, ref in ref_data.items()
        if name in head_data
    ]
    combined_data.sort(key=lambda x: x[2])

    fig, axs = plt.subplots(
        figsize=(8, 2 + len(combined_data) * 0.3), layout="constrained"
    )
    plt.axvline(1.0)
    plot_diff_pair(axs, combined_data)
    names = [x[0] for x in combined_data]
    names.append("ALL")
    axs.set_yticks(np.arange(len(names)) + 1, names)
    axs.set_ylim(0, len(names) + 1)
    axs.tick_params(axis="x", bottom=True, top=True, labelbottom=True, labeltop=True)
    axs.xaxis.set_major_formatter(formatter)
    axs.grid()
    axs.set_title(title)

    plt.savefig(output_filename)
    plt.close()
