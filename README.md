# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](../../actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

<!-- START table -->
## linux x86_64 (linux)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-08-03](results/bm-20230803-3.13.0a0-14fbd4e) | python | 14fbd4e6b1 | 3.13.0a0 | 14fbd4e | [1.30x faster](results/bm-20230803-3.13.0a0-14fbd4e/bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e-vs-3.10.4.md) | [1.04x faster](results/bm-20230803-3.13.0a0-14fbd4e/bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e-vs-3.11.0.md) |  |
| [2023-08-03](results/bm-20230803-3.13.0a0-8abbc6a) | brandtbucher | immortal_i | 3.13.0a0 | 8abbc6a | [1.30x faster](results/bm-20230803-3.13.0a0-8abbc6a/bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a-vs-3.10.4.md) | [1.04x faster](results/bm-20230803-3.13.0a0-8abbc6a/bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a-vs-3.11.0.md) | [1.00x faster](results/bm-20230803-3.13.0a0-8abbc6a/bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a-vs-base.md) |
| [2023-08-03](results/bm-20230803-3.13.0a0-ccddc2b) | brandtbucher | binary_sub | 3.13.0a0 | ccddc2b | [1.29x faster](results/bm-20230803-3.13.0a0-ccddc2b/bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b-vs-3.10.4.md) | [1.04x faster](results/bm-20230803-3.13.0a0-ccddc2b/bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b-vs-3.11.0.md) | [1.01x slower](results/bm-20230803-3.13.0a0-ccddc2b/bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b-vs-base.md) |
| [2023-07-30](results/bm-20230730-3.13.0a0-8bc0926) | faster-cpython | gc_stats | 3.13.0a0 | 8bc0926 | [1.29x faster](results/bm-20230730-3.13.0a0-8bc0926/bm-20230730-linux-x86_64-faster%252dcpython-gc_stats-3.13.0a0-8bc0926-vs-3.10.4.md) | [1.04x faster](results/bm-20230730-3.13.0a0-8bc0926/bm-20230730-linux-x86_64-faster%252dcpython-gc_stats-3.13.0a0-8bc0926-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.25x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.24x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## linux x86_64 (pythonperf2)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-08-04](results/bm-20230804-3.13.0a0-3994224) | faster-cpython | gc_scan_ro | 3.13.0a0 | 3994224 | [1.26x faster](results/bm-20230804-3.13.0a0-3994224/bm-20230804-pythonperf2-x86_64-faster%252dcpython-gc_scan_roots-3.13.0a0-3994224-vs-3.10.4.md) | [1.04x faster](results/bm-20230804-3.13.0a0-3994224/bm-20230804-pythonperf2-x86_64-faster%252dcpython-gc_scan_roots-3.13.0a0-3994224-vs-3.11.0.md) |  |
| [2023-07-29](results/bm-20230729-3.13.0a0-5113ed7) | python | main | 3.13.0a0 | 5113ed7 | [1.27x faster](results/bm-20230729-3.13.0a0-5113ed7/bm-20230729-pythonperf2-x86_64-python-main-3.13.0a0-5113ed7-vs-3.10.4.md) | [1.04x faster](results/bm-20230729-3.13.0a0-5113ed7/bm-20230729-pythonperf2-x86_64-python-main-3.13.0a0-5113ed7-vs-3.11.0.md) |  |
| [2023-07-24](results/bm-20230724-3.13.0a0-0a9b339) | python | main | 3.13.0a0 | 0a9b339 | [1.26x faster](results/bm-20230724-3.13.0a0-0a9b339/bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339-vs-3.10.4.md) | [1.04x faster](results/bm-20230724-3.13.0a0-0a9b339/bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.21x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.21x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## windows amd64 (pythonperf1)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-07-29](results/bm-20230729-3.13.0a0-5113ed7) | python | main | 3.13.0a0 | 5113ed7 | [1.12x faster](results/bm-20230729-3.13.0a0-5113ed7/bm-20230729-pythonperf1-amd64-python-main-3.13.0a0-5113ed7-vs-3.10.4.md) | [1.00x slower](results/bm-20230729-3.13.0a0-5113ed7/bm-20230729-pythonperf1-amd64-python-main-3.13.0a0-5113ed7-vs-3.11.0.md) |  |
| [2023-07-22](results/bm-20230722-3.13.0a0-9a6b278) | python | main | 3.13.0a0 | 9a6b278 | [1.14x faster](results/bm-20230722-3.13.0a0-9a6b278/bm-20230722-pythonperf1-amd64-python-main-3.13.0a0-9a6b278-vs-3.10.4.md) | [1.02x faster](results/bm-20230722-3.13.0a0-9a6b278/bm-20230722-pythonperf1-amd64-python-main-3.13.0a0-9a6b278-vs-3.11.0.md) |  |
| [2023-07-17](results/bm-20230717-3.13.0a0-ba47232) | brandtbucher | justin | 3.13.0a0 | ba47232 | [1.16x faster](results/bm-20230717-3.13.0a0-ba47232/bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232-vs-3.10.4.md) | [1.04x faster](results/bm-20230717-3.13.0a0-ba47232/bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232-vs-3.11.0.md) | [1.03x slower](results/bm-20230717-3.13.0a0-ba47232/bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232-vs-base.md) |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.11x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.12x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## darwin arm64 (darwin)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-07-29](results/bm-20230729-3.13.0a0-5113ed7) | python | main | 3.13.0a0 | 5113ed7 | [1.17x faster](results/bm-20230729-3.13.0a0-5113ed7/bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7-vs-3.10.4.md) | [1.03x slower](results/bm-20230729-3.13.0a0-5113ed7/bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7-vs-3.11.0.md) |  |
| [2023-07-22](results/bm-20230722-3.13.0a0-9a6b278) | python | main | 3.13.0a0 | 9a6b278 | [1.16x faster](results/bm-20230722-3.13.0a0-9a6b278/bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278-vs-3.10.4.md) | [1.04x slower](results/bm-20230722-3.13.0a0-9a6b278/bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278-vs-3.11.0.md) |  |
| [2023-07-17](results/bm-20230717-3.13.0a0-ba47232) | brandtbucher | justin | 3.13.0a0 | ba47232 | [1.21x faster](results/bm-20230717-3.13.0a0-ba47232/bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232-vs-3.10.4.md) | [1.00x faster](results/bm-20230717-3.13.0a0-ba47232/bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232-vs-3.11.0.md) | [1.02x slower](results/bm-20230717-3.13.0a0-ba47232/bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232-vs-base.md) |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.21x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
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

Visit the 🔒 [benchmark action](../../actions/workflows/benchmark.yml) and click the "Run Workflow" button.

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

To watch the progress of the benchmark, select it from the 🔒 [benchmark action page](../../actions/workflows/benchmark.yml).
It may be canceled from there as well.
To show only your benchmark workflows, select your GitHub ID from the "Actor" dropdown.

When the benchmarking is complete, the results are published to this repository and will appear in the [master table](RESULTS.md).
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

For documentation about how this works, see the [bench_runner project](https://github.com/faster-cpython/bench_runner).

