import argparse
import datetime
from pathlib import Path
import re
import sys
from typing import Any, Dict, Iterable, Optional, Tuple


from matplotlib import pyplot as plt
import matplotlib
import numpy as np
import pyperf


matplotlib.use("agg")


try:
    from lib import result
except ImportError:
    sys.path.insert(0, str(Path(__file__).parents[1]))
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
    all_data = []
    violins = []

    for i, (name, values, mean) in enumerate(data):
        if values is not None:
            idx = np.round(np.linspace(0, len(values) - 1, 100)).astype(int)
            violins.append(values[idx])
            all_data.extend(values)
        else:
            violins.append([1.0])
            ax.text(1.01, i + 1, "insignificant")

    violins.append(all_data)

    violin = ax.violinplot(
        violins,
        vert=False,
        showmeans=True,
        showmedians=False,
        widths=1.0,
        quantiles=[[0.1, 0.9]] * len(violins),
    )

    violin["cquantiles"].set_linestyle(":")

    for i, values in enumerate(violins):
        if not np.all(values == [1.0]):
            mean = np.mean(values)
            ax.text(mean, i + 1.3, f"{mean:.04f}", size=8)

    return all_data


def formatter(val, pos):
    return f"{val:.02f}×"


def calculate_diffs(
    ref_values, head_values, outlier_rejection=True
) -> Tuple[Optional[np.ndarray], float]:
    sig, t_score = pyperf._utils.is_significant(ref_values, head_values)

    if not sig:
        return None, 0.0
    else:
        if outlier_rejection:
            ref_values = remove_outliers(ref_values)
            head_values = remove_outliers(head_values)
        values = np.outer(ref_values, 1.0 / head_values).flatten()
        values.sort()
        return values, float(values.mean())


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


def get_micro_version(version):
    micro = version.split(".")[-1].replace("+", "")
    if match := re.match(r"[0-9]+([a-z]+.+)", micro):
        micro = match.groups()[0]
    return micro


def longitudinal_plot(
    results: Iterable[result.Result],
    output_filename: Path,
    bases=["3.10.4", "3.11.0", "3.12.0b1"],
    runners=["linux", "pythonperf2", "darwin", "pythonperf1"],
    names=["linux", "linux2", "macos", "windows"],
    versions=[(3, 11), (3, 12), (3, 13)],
):
    fig, axs = plt.subplots(
        len(versions), 1, figsize=(10, 5 * len(versions)), layout="constrained"
    )

    results = [r for r in results if r.fork == "python"]

    for version, base, ax in zip(versions, bases, axs):
        version_str = ".".join(str(x) for x in version)
        ver_results = [r for r in results if r.parsed_version.release[0:2] == version]

        ax.set_title(f"Python {version_str} vs. {base}")
        ax.yaxis.set_major_formatter(formatter)
        ax.grid()

        for runner_i, (runner, name) in enumerate(zip(runners, names)):
            runner_results = [r for r in ver_results if r.nickname == runner]

            for r in results:
                if r.nickname == runner and r.version == base:
                    ref = r
                    break
            else:
                continue

            runner_results.sort(key=lambda x: x.commit_datetime)
            dates = [
                datetime.datetime.fromisoformat(x.commit_datetime)
                for x in runner_results
            ]
            changes = [
                result.Comparison(ref, r, base).geometric_mean_float
                for r in runner_results
            ]

            ax.plot(
                dates,
                changes,
                "o-",
                markersize=2.5,
                label=name,
                alpha=0.9,
            )

            if runner_i > 0:
                continue

            annotations = set()
            for r, date, change in zip(runner_results, dates, changes):
                micro = get_micro_version(r.version)
                if micro not in annotations and not r.version.endswith("+"):
                    annotations.add(micro)
                    text = ax.annotate(
                        micro,
                        xy=(date, change),
                        xycoords="data",
                        xytext=(-3, 15),
                        textcoords="offset points",
                        rotation=90,
                        arrowprops=dict(arrowstyle="-", connectionstyle="arc"),
                    )
                    text.set_color("#888")
                    text.set_size(8)
                    text.arrow_patch.set_color("#888")

        ylim = ax.get_ylim()
        ax.set_ylim(top=ylim[1] + 0.1)
        ax.legend(loc="upper left")

    fig.suptitle("Performance improvement by major version")

    plt.savefig(output_filename, dpi=150)
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Compare two benchmark .json files")
    parser.add_argument("ref", help="The reference .json file")
    parser.add_argument("head", help="The head .json file")
    parser.add_argument("output", help="Output filename")
    parser.add_argument("title", help="Title of plot")
    args = parser.parse_args()

    plot_diff(
        result.Result.from_filename(Path(args.ref)),
        result.Result.from_filename(Path(args.head)),
        Path(args.output),
        args.title,
    )
