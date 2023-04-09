# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](https://github.com/faster-cpython/benchmarking/actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

<!-- START table -->
## linux x86_64 (linux)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-04-08](results/bm-20230408-3.12.0a7%2B-3516704) | python | main | 3.12.0a7+ | 3516704 | [1.31x faster](results/bm-20230408-3.12.0a7%2B-3516704/bm-20230408-linux-x86_64-python-main-3.12.0a7%2B-3516704-vs-3.10.4.md) | [1.04x faster](results/bm-20230408-3.12.0a7%2B-3516704/bm-20230408-linux-x86_64-python-main-3.12.0a7%2B-3516704-vs-3.11.0.md) |  |
| [2023-04-06](results/bm-20230406-3.12.0a7%2B-affedee) | python | affedee8bf | 3.12.0a7+ | affedee | [1.31x faster](results/bm-20230406-3.12.0a7%2B-affedee/bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7%2B-affedee-vs-3.10.4.md) | [1.04x faster](results/bm-20230406-3.12.0a7%2B-affedee/bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7%2B-affedee-vs-3.11.0.md) |  |
| [2023-04-06](results/bm-20230406-3.12.0a7%2B-47a7094) | ericsnowcurrently | tstate_cur | 3.12.0a7+ | 47a7094 | [1.31x faster](results/bm-20230406-3.12.0a7%2B-47a7094/bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-47a7094-vs-3.10.4.md) | [1.04x faster](results/bm-20230406-3.12.0a7%2B-47a7094/bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-47a7094-vs-3.11.0.md) | [1.00x faster](results/bm-20230406-3.12.0a7%2B-47a7094/bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-47a7094-vs-base.md) |
| [2023-04-06](results/bm-20230406-3.12.0a7%2B-52bc2e7) | python | 52bc2e7b9d | 3.12.0a7+ | 52bc2e7 | [1.31x faster](results/bm-20230406-3.12.0a7%2B-52bc2e7/bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7-vs-3.10.4.md) | [1.04x faster](results/bm-20230406-3.12.0a7%2B-52bc2e7/bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7-vs-3.11.0.md) |  |
| [2023-04-06](results/bm-20230406-3.12.0a7%2B-97543c5) | brandtbucher | fold_slice | 3.12.0a7+ | 97543c5 | [1.30x faster](results/bm-20230406-3.12.0a7%2B-97543c5/bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7%2B-97543c5-vs-3.10.4.md) | [1.04x faster](results/bm-20230406-3.12.0a7%2B-97543c5/bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7%2B-97543c5-vs-3.11.0.md) | [1.00x slower](results/bm-20230406-3.12.0a7%2B-97543c5/bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7%2B-97543c5-vs-base.md) |
| [2023-04-06](results/bm-20230406-3.12.0a7%2B-39619f9) | brandtbucher | fold_slice | 3.12.0a7+ | 39619f9 | [1.30x faster](results/bm-20230406-3.12.0a7%2B-39619f9/bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7%2B-39619f9-vs-3.10.4.md) | [1.04x faster](results/bm-20230406-3.12.0a7%2B-39619f9/bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7%2B-39619f9-vs-3.11.0.md) | [1.00x slower](results/bm-20230406-3.12.0a7%2B-39619f9/bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7%2B-39619f9-vs-base.md) |
| [2023-04-07](results/bm-20230407-3.12.0a6%2B-4a2152f) | iritkatriel | asyncgen | 3.12.0a6+ | 4a2152f | [1.30x faster](results/bm-20230407-3.12.0a6%2B-4a2152f/bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6%2B-4a2152f-vs-3.10.4.md) | [1.03x faster](results/bm-20230407-3.12.0a6%2B-4a2152f/bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6%2B-4a2152f-vs-3.11.0.md) | [1.00x faster](results/bm-20230407-3.12.0a6%2B-4a2152f/bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6%2B-4a2152f-vs-base.md) |
| [2023-04-06](results/bm-20230406-3.12.0a6%2B-030016a) | eduardo-elizondo | immortal_r | 3.12.0a6+ | 030016a | [1.22x faster](results/bm-20230406-3.12.0a6%2B-030016a/bm-20230406-linux-x86_64-eduardo%252delizondo-immortal_references-3.12.0a6%2B-030016a-vs-3.10.4.md) | [1.03x slower](results/bm-20230406-3.12.0a6%2B-030016a/bm-20230406-linux-x86_64-eduardo%252delizondo-immortal_references-3.12.0a6%2B-030016a-vs-3.11.0.md) | [1.06x slower](results/bm-20230406-3.12.0a6%2B-030016a/bm-20230406-linux-x86_64-eduardo%252delizondo-immortal_references-3.12.0a6%2B-030016a-vs-base.md) |
| [2023-04-02](results/bm-20230402-3.12.0a6%2B-385b5d6) | python | 385b5d6e09 | 3.12.0a6+ | 385b5d6 | [1.30x faster](results/bm-20230402-3.12.0a6%2B-385b5d6/bm-20230402-linux-x86_64-python-385b5d6e091da454c3e0-3.12.0a6%2B-385b5d6-vs-3.10.4.md) | [1.03x faster](results/bm-20230402-3.12.0a6%2B-385b5d6/bm-20230402-linux-x86_64-python-385b5d6e091da454c3e0-3.12.0a6%2B-385b5d6-vs-3.11.0.md) |  |
| [2023-04-01](results/bm-20230401-3.12.0a6%2B-848bdbe) | python | 848bdbe166 | 3.12.0a6+ | 848bdbe | [1.29x faster](results/bm-20230401-3.12.0a6%2B-848bdbe/bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6%2B-848bdbe-vs-3.10.4.md) | [1.03x faster](results/bm-20230401-3.12.0a6%2B-848bdbe/bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6%2B-848bdbe-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | deaf509e8f | 3.11.0 | deaf509 | [1.25x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | 9d38120e33 | 3.10.4 | 9d38120 |  | [1.25x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120-vs-3.11.0.md) |  |

## linux x86_64 (pythonperf2)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-04-08](results/bm-20230408-3.12.0a7%2B-3516704) | python | main | 3.12.0a7+ | 3516704 | [1.27x faster](results/bm-20230408-3.12.0a7%2B-3516704/bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7%2B-3516704-vs-3.10.4.md) | [1.04x faster](results/bm-20230408-3.12.0a7%2B-3516704/bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7%2B-3516704-vs-3.11.0.md) |  |
| [2023-04-01](results/bm-20230401-3.12.0a6%2B-06249ec) | python | main | 3.12.0a6+ | 06249ec | [1.24x faster](results/bm-20230401-3.12.0a6%2B-06249ec/bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6%2B-06249ec-vs-3.10.4.md) | [1.02x faster](results/bm-20230401-3.12.0a6%2B-06249ec/bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6%2B-06249ec-vs-3.11.0.md) |  |
| [2023-03-25](results/bm-20230325-3.12.0a6%2B-30a306c) | python | main | 3.12.0a6+ | 30a306c | [1.26x faster](results/bm-20230325-3.12.0a6%2B-30a306c/bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6%2B-30a306c-vs-3.10.4.md) | [1.03x faster](results/bm-20230325-3.12.0a6%2B-30a306c/bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6%2B-30a306c-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | deaf509e8f | 3.11.0 | deaf509 | [1.22x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.22x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## windows amd64 (pythonperf1)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-04-08](results/bm-20230408-3.12.0a7%2B-3516704) | python | main | 3.12.0a7+ | 3516704 | [1.20x faster](results/bm-20230408-3.12.0a7%2B-3516704/bm-20230408-pythonperf1-amd64-python-main-3.12.0a7%2B-3516704-vs-3.10.4.md) | [1.08x faster](results/bm-20230408-3.12.0a7%2B-3516704/bm-20230408-pythonperf1-amd64-python-main-3.12.0a7%2B-3516704-vs-3.11.0.md) |  |
| [2023-04-06](results/bm-20230406-3.12.0a6%2B-030016a) | eduardo-elizondo | immortal_r | 3.12.0a6+ | 030016a | [1.02x faster](results/bm-20230406-3.12.0a6%2B-030016a/bm-20230406-pythonperf1-amd64-eduardo%252delizondo-immortal_references-3.12.0a6%2B-030016a-vs-3.10.4.md) | [1.09x slower](results/bm-20230406-3.12.0a6%2B-030016a/bm-20230406-pythonperf1-amd64-eduardo%252delizondo-immortal_references-3.12.0a6%2B-030016a-vs-3.11.0.md) | [1.20x slower](results/bm-20230406-3.12.0a6%2B-030016a/bm-20230406-pythonperf1-amd64-eduardo%252delizondo-immortal_references-3.12.0a6%2B-030016a-vs-base.md) |
| [2023-04-02](results/bm-20230402-3.12.0a6%2B-385b5d6) | python | 385b5d6e09 | 3.12.0a6+ | 385b5d6 | [1.22x faster](results/bm-20230402-3.12.0a6%2B-385b5d6/bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6%2B-385b5d6-vs-3.10.4.md) | [1.10x faster](results/bm-20230402-3.12.0a6%2B-385b5d6/bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6%2B-385b5d6-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | deaf509e8f | 3.11.0 | deaf509 | [1.11x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | 9d38120e33 | 3.10.4 | 9d38120 |  | [1.11x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120-vs-3.11.0.md) |  |

## darwin arm64 (darwin)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-04-08](results/bm-20230408-3.12.0a7%2B-3516704) | python | main | 3.12.0a7+ | 3516704 | [1.20x faster](results/bm-20230408-3.12.0a7%2B-3516704/bm-20230408-darwin-arm64-python-main-3.12.0a7%2B-3516704-vs-3.10.4.md) | [1.01x slower](results/bm-20230408-3.12.0a7%2B-3516704/bm-20230408-darwin-arm64-python-main-3.12.0a7%2B-3516704-vs-3.11.0.md) |  |
| [2023-04-01](results/bm-20230401-3.12.0a6%2B-06249ec) | python | main | 3.12.0a6+ | 06249ec | [1.19x faster](results/bm-20230401-3.12.0a6%2B-06249ec/bm-20230401-darwin-arm64-python-main-3.12.0a6%2B-06249ec-vs-3.10.4.md) | [1.01x slower](results/bm-20230401-3.12.0a6%2B-06249ec/bm-20230401-darwin-arm64-python-main-3.12.0a6%2B-06249ec-vs-3.11.0.md) |  |
| [2023-03-25](results/bm-20230325-3.12.0a6%2B-30a306c) | python | main | 3.12.0a6+ | 30a306c | [1.19x faster](results/bm-20230325-3.12.0a6%2B-30a306c/bm-20230325-darwin-arm64-python-main-3.12.0a6%2B-30a306c-vs-3.10.4.md) | [1.02x slower](results/bm-20230325-3.12.0a6%2B-30a306c/bm-20230325-darwin-arm64-python-main-3.12.0a6%2B-30a306c-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | deaf509e8f | 3.11.0 | deaf509 | [1.21x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.21x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |


<!-- END table -->

`*` indicates that the exact same versions of pyperformance was not used.

![Longitudinal speed improvement](/longitudinal.png)

Improvement of the geometric mean of key merged benchmarks, computed with `pyperf compare`.
The results have a resolution of 0.01 (1%).

- linux: Intel® Xeon® W-2255 CPU @ 3.70GHz, running Ubuntu 20.04 LTS, gcc 9.4.0
- linux2: 12th Gen Intel® Core™ i9-12900 @ 2.40 GHz, running Ubuntu 22.04 LTS, gcc 11.3.0
- macos: M1 arm64 Mac® Mini, running macOS 13.2.1, clang 1400.0.29.202
- windows: 12th Gen Intel® Core™ i9-12900 @ 2.40 GHz, running Windows 11 Pro (21H2, 22000.1696), MSVC v143

## Documentation

### Running benchmarks from the GitHub web UI

Visit the 🔒 [benchmark action](https://github.com/faster-cpython/benchmarking/actions/workflows/benchmark.yml) and click the "Run Workflow" button.

The available parameters are:

- `fork`: The fork of CPython to benchmark.
  If benchmarking a pull request, this would normally be your GitHub username.
- `ref`: The branch, tag or commit SHA to benchmark.
  If a SHA, it must be the full SHA, since finding it by a prefix is not supported.
- `machine`: The machine to run on.
  One of `linux-amd64` (default), `windows-amd64`, `darwin-arm64` or `all`.
- `benchmark_base`: If checked, the base of the selected branch will also be benchmarked.
  The base is determined by running `git merge-base upstream/main $ref`.
- `pystats`: If checked, collect the pystats from running the benchmarks.
- `publish`: If checked, the results will be published in the public [ideas repo](https://github.com/faster-cpython/ideas) upon successful completion.

To watch the progress of the benchmark, select it from the 🔒 [benchmark action page](https://github.com/faster-cpython/benchmarking/actions/workflows/benchmark.yml).
It may be canceled from there as well.
To show only your benchmark workflows, select your GitHub ID from the "Actor" dropdown.

When the benchmarking is complete, the results are published to this repository and will appear in the [master table](results/README.md).
Each set of benchmarks will have:

- The raw `.json` results from pyperformance.
- Comparisons against important reference releases, as well as the merge base of the branch if `benchmark_base` was selected.  These include
  - A markdown table produced by `pyperf compare_to`.
  - A set of "violin" plots showing the distribution of results for each benchmark.

The most convenient way to get results locally is to clone this repo and `git pull` from it.

### Running benchmarks from the GitHub CLI

To automate benchmarking runs, it may be more convenient to use the [GitHub CLI](https://cli.github.com/).
Once you have `gh` installed and configured, you can run benchmarks by cloning this repository and then from inside it:

```bash
$ gh workflow run benchmark.yml -f fork=me -f ref=my_branch
```

Any of the parameters described above are available at the commandline using the `-f key=value` syntax.

### Collecting Linux perf profiling data

To collect Linux perf sampling profile data for a benchmarking run, run the `_benchmark` action and check the `perf` checkbox.
Follow this by a run of the `_generate` action to regenerate the plots.

### Costs

We are limited to 2,000 compute minutes per month.


| Action | Minutes |
| -- | -- |
| Benchmarks | 7 minutes (most of the time is on self-hosted runners) |
| CI | 10 minutes |

To reduce CI usage, PRs that are only documentation changes should add the `[skip ci]` token to their commit message.

### Analysis changes

This is a changelog of changes that affect the derived data and results:

- 2023-02-09: The plots exclude benchmarks that aren't significant using the same algorithm used by the table results.
  These benchmarks do not contribute to the overall distribution at the top of the plot.

### Developer docs

For documentation about how this works, see the [developer docs](DEVELOPER.md).

