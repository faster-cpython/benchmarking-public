"""
Generate summary tables and a visualization of Linux perf profiling results.
"""


import csv
from pathlib import Path
import re
from typing import Dict, List


from matplotlib import pyplot as plt
import numpy as np


ROOT_DIR = Path(__file__).parents[2] / "profiling"
RESULTS_DIR = ROOT_DIR / "results"


# Categories of functions, where each value is a list of regular expressions.
# These are matched in-order.
CATEGORIES: Dict[str, List[str]] = {
    "interpreter": [
        "_PyEvalFramePushAndInit",
        "_PyEval_EvalFrameDefault",
        "_PyFrame_ClearExceptCode",
        "_PyThreadState_PopFrame",
        "initialize_locals",
    ],
    "lookup": [
        "_PyType_Lookup",
        "_Py_dict_lookup",
        "unicodekeys_lookup_unicode",
    ],
    "gc": [
        ".+MaybeUntrack",
        ".+_traverse",
        "PyObject_IS_GC",
        "_PyObject_Visit.+",
        "_PyTrash_.+",
        "gc_collect_main",
        "type_is_gc",
        "visit_.+",
    ],
    "memory": [
        ".+Alloc",
        ".+Dealloc",
        ".+_alloc",
        ".+_dealloc",
        "_?PyMem_.+",
        "_PyObject_Free",
        "_PyObject_Malloc",
    ],
    "dynamic": [
        "_?PyNumber_.+",
        "_?PyObject_.+",
        "type_.+",
    ],
    "library": ["_?sre_.+", "pattern_.+"],
}


def category_for_obj_sym(obj: str, sym: str) -> str:
    if obj == "[kernel.kallsyms]":
        return "kernel"

    if obj.startswith("libc"):
        return "libc"

    if re.match(r".+\.so(\..+)?$", obj):
        return "library"

    if obj == "python":
        for category, patterns in CATEGORIES.items():
            for pattern in patterns:
                if re.match(f"^{pattern}$", sym.split()[0]):
                    return category

    return "unknown"


def generate_results(output_dir: Path = ROOT_DIR, input_dir: Path = RESULTS_DIR):
    results = {}
    categories = {}

    with open(output_dir / "profiling.md", "w") as md:
        for csv_path in sorted(input_dir.glob("*.csv")):
            stem = csv_path.stem.split(".", 1)[0]
            results[stem] = {}

            md.write(f"\n## {stem}\n\n")
            md.write("| percentage | object | symbol | category |\n")
            md.write("| ---: | :--- | :--- | :--- |\n")

            with open(csv_path, newline="") as fd:
                csvreader = csv.reader(fd)
                for row in csvreader:
                    break

                for row in csvreader:
                    self_time, _, obj, sym = row
                    self_time = float(self_time) / 100.0
                    if self_time < 0.01:
                        break

                    category = category_for_obj_sym(obj, sym)
                    categories.setdefault(category, {})
                    categories[category].setdefault((obj, sym), 0.0)
                    categories[category][(obj, sym)] += self_time

                    results[stem].setdefault(category, 0.0)
                    results[stem][category] += self_time

                    md.write(f"| {self_time:.2%} | `{obj}` | `{sym}` | {category} |\n")

        sorted_categories = sorted(
            [
                (sum(val.values()) / len(results), key)
                for (key, val) in categories.items()
            ],
            reverse=True,
        )

        md.write("\n\n## Categories\n")
        for total, category in sorted_categories:
            matches = categories[category]
            md.write(f"\n### {category}\n\n")
            md.write(f"{total:.2%} total\n\n")
            md.write("| percentage | object | symbol |\n")
            md.write("| ---: | :--- | :--- |\n")
            for (obj, sym), self_time in sorted(
                matches.items(), key=lambda x: x[1], reverse=True
            ):
                md.write(f"| {self_time / len(results):.2%} | {obj} | {sym} |\n")

    fig, ax = plt.subplots(figsize=(8, len(results) * 0.3), layout="constrained")

    bottom = np.zeros(len(results))
    names = list(results.keys())[::-1]

    for val, category in sorted_categories:
        if category == "unknown":
            continue
        values = np.array([results[name].get(category, 0.0) for name in names])
        ax.barh(names, values, 0.5, label=f"{category} {val:.2%}", left=bottom)
        bottom += values

    values = 1.0 - bottom
    ax.barh(names, values, 0.5, label="(other functions)", left=bottom, color="#ddd")

    ax.set_xlabel("percentage time")
    ax.legend()
    ax.set_xlim([0, 1])

    fig.savefig(output_dir / "profiling.png")


if __name__ == "__main__":
    generate_results()
