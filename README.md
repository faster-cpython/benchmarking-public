# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](https://github.com/faster-cpython/benchmarking/actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

<!-- START table -->
## linux x86_64 (linux)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-06-09](results/bm-20230609-3.13.0a0-0463633) | brandtbucher | to_bool | 3.13.0a0 | 0463633 | [1.25x faster](results/bm-20230609-3.13.0a0-0463633/bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633-vs-3.10.4.md) | [1.01x faster](results/bm-20230609-3.13.0a0-0463633/bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633-vs-3.11.0.md) | [1.02x slower](results/bm-20230609-3.13.0a0-0463633/bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633-vs-base.md) |
| [2023-06-09](results/bm-20230609-3.13.0a0-1ab78ef) | brandtbucher | specialize | 3.13.0a0 | 1ab78ef | [1.27x faster](results/bm-20230609-3.13.0a0-1ab78ef/bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef-vs-3.10.4.md) | [1.02x faster](results/bm-20230609-3.13.0a0-1ab78ef/bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef-vs-3.11.0.md) | [1.01x slower](results/bm-20230609-3.13.0a0-1ab78ef/bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef-vs-base.md) |
| [2023-06-07](results/bm-20230607-3.13.0a0-27bb264) | brandtbucher | specialize | 3.13.0a0 | 27bb264 | [1.26x faster](results/bm-20230607-3.13.0a0-27bb264/bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264-vs-3.10.4.md) | [1.01x faster](results/bm-20230607-3.13.0a0-27bb264/bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264-vs-3.11.0.md) | [1.02x slower](results/bm-20230607-3.13.0a0-27bb264/bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264-vs-base.md) |
| [2023-06-06](results/bm-20230606-3.13.0a0-5289c7f) | brandtbucher | specialize | 3.13.0a0 | 5289c7f | [1.26x faster](results/bm-20230606-3.13.0a0-5289c7f/bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f-vs-3.10.4.md) | [1.01x faster](results/bm-20230606-3.13.0a0-5289c7f/bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f-vs-3.11.0.md) | [1.02x slower](results/bm-20230606-3.13.0a0-5289c7f/bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f-vs-base.md) |
| [2023-06-06](results/bm-20230606-3.13.0a0-69781b4) | brandtbucher | 69781b4244 | 3.13.0a0 | 69781b4 | [1.26x faster](results/bm-20230606-3.13.0a0-69781b4/bm-20230606-linux-x86_64-brandtbucher-69781b4244a9485837b5-3.13.0a0-69781b4-vs-3.10.4.md) | [1.01x faster](results/bm-20230606-3.13.0a0-69781b4/bm-20230606-linux-x86_64-brandtbucher-69781b4244a9485837b5-3.13.0a0-69781b4-vs-3.11.0.md) | [1.02x slower](results/bm-20230606-3.13.0a0-69781b4/bm-20230606-linux-x86_64-brandtbucher-69781b4244a9485837b5-3.13.0a0-69781b4-vs-base.md) |
| [2023-06-07](results/bm-20230607-3.12.0a7%2B-82b39b9) | mdboom | match_nogi | 3.12.0a7+ | 82b39b9 | [1.31x faster](results/bm-20230607-3.12.0a7%2B-82b39b9/bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7%2B-82b39b9-vs-3.10.4.md) | [1.05x faster](results/bm-20230607-3.12.0a7%2B-82b39b9/bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7%2B-82b39b9-vs-3.11.0.md) | [1.04x faster \*](results/bm-20230607-3.12.0a7%2B-82b39b9/bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7%2B-82b39b9-vs-base.md) |
| [2023-04-27](results/bm-20230427-3.12.0a4-d595911) | mdboom | nogil_d595 | 3.12.0a4 | d595911 | [1.21x faster](results/bm-20230427-3.12.0a4-d595911/bm-20230427-linux-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911-vs-3.10.4.md) | [1.03x slower](results/bm-20230427-3.12.0a4-d595911/bm-20230427-linux-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911-vs-3.11.0.md) |  |
| [2023-06-06](results/bm-20230606-3.11.4-d2340ef) | python | v3.11.4 | 3.11.4 | d2340ef | [1.25x faster](results/bm-20230606-3.11.4-d2340ef/bm-20230606-linux-x86_64-python-v3.11.4-3.11.4-d2340ef-vs-3.10.4.md) | [1.00x slower](results/bm-20230606-3.11.4-d2340ef/bm-20230606-linux-x86_64-python-v3.11.4-3.11.4-d2340ef-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.25x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.24x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## linux x86_64 (pythonperf2)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-06-05](results/bm-20230605-3.13.0a0-0689340) | python | 0689340366 | 3.13.0a0 | 0689340 | [1.30x faster](results/bm-20230605-3.13.0a0-0689340/bm-20230605-pythonperf2-x86_64-python-06893403668961fdbd5d-3.13.0a0-0689340-vs-3.10.4.md) | [1.07x faster](results/bm-20230605-3.13.0a0-0689340/bm-20230605-pythonperf2-x86_64-python-06893403668961fdbd5d-3.13.0a0-0689340-vs-3.11.0.md) |  |
| [2023-06-03](results/bm-20230603-3.13.0a0-eaff9c3) | python | main | 3.13.0a0 | eaff9c3 | [1.31x faster](results/bm-20230603-3.13.0a0-eaff9c3/bm-20230603-pythonperf2-x86_64-python-main-3.13.0a0-eaff9c3-vs-3.10.4.md) | [1.08x faster](results/bm-20230603-3.13.0a0-eaff9c3/bm-20230603-pythonperf2-x86_64-python-main-3.13.0a0-eaff9c3-vs-3.11.0.md) |  |
| [2023-06-02](results/bm-20230602-3.13.0a0-6cde1a4) | faster-cpython | remove_rem | 3.13.0a0 | 6cde1a4 | [1.29x faster](results/bm-20230602-3.13.0a0-6cde1a4/bm-20230602-pythonperf2-x86_64-faster%252dcpython-remove_remaining_sup-3.13.0a0-6cde1a4-vs-3.10.4.md) | [1.06x faster](results/bm-20230602-3.13.0a0-6cde1a4/bm-20230602-pythonperf2-x86_64-faster%252dcpython-remove_remaining_sup-3.13.0a0-6cde1a4-vs-3.11.0.md) | [1.01x slower](results/bm-20230602-3.13.0a0-6cde1a4/bm-20230602-pythonperf2-x86_64-faster%252dcpython-remove_remaining_sup-3.13.0a0-6cde1a4-vs-base.md) |
| [2023-04-27](results/bm-20230427-3.12.0a4-d595911) | mdboom | nogil_d595 | 3.12.0a4 | d595911 | [1.18x faster](results/bm-20230427-3.12.0a4-d595911/bm-20230427-pythonperf2-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911-vs-3.10.4.md) | [1.02x slower](results/bm-20230427-3.12.0a4-d595911/bm-20230427-pythonperf2-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911-vs-3.11.0.md) |  |
| [2023-06-06](results/bm-20230606-3.11.4-d2340ef) | python | v3.11.4 | 3.11.4 | d2340ef | [1.21x faster](results/bm-20230606-3.11.4-d2340ef/bm-20230606-pythonperf2-x86_64-python-v3.11.4-3.11.4-d2340ef-vs-3.10.4.md) | [1.00x faster](results/bm-20230606-3.11.4-d2340ef/bm-20230606-pythonperf2-x86_64-python-v3.11.4-3.11.4-d2340ef-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.21x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.21x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## windows amd64 (pythonperf1)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-06-03](results/bm-20230603-3.13.0a0-eaff9c3) | python | main | 3.13.0a0 | eaff9c3 | [1.16x faster](results/bm-20230603-3.13.0a0-eaff9c3/bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3-vs-3.10.4.md) | [1.04x faster](results/bm-20230603-3.13.0a0-eaff9c3/bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3-vs-3.11.0.md) |  |
| [2023-05-28](results/bm-20230528-3.13.0a0-3a5be87) | python | main | 3.13.0a0 | 3a5be87 | [1.20x faster](results/bm-20230528-3.13.0a0-3a5be87/bm-20230528-pythonperf1-amd64-python-main-3.13.0a0-3a5be87-vs-3.10.4.md) | [1.07x faster](results/bm-20230528-3.13.0a0-3a5be87/bm-20230528-pythonperf1-amd64-python-main-3.13.0a0-3a5be87-vs-3.11.0.md) |  |
| [2023-05-21](results/bm-20230521-3.12.0a7%2B-99b6418) | python | main | 3.12.0a7+ | 99b6418 | [1.18x faster](results/bm-20230521-3.12.0a7%2B-99b6418/bm-20230521-pythonperf1-amd64-python-main-3.12.0a7%2B-99b6418-vs-3.10.4.md) | [1.05x faster](results/bm-20230521-3.12.0a7%2B-99b6418/bm-20230521-pythonperf1-amd64-python-main-3.12.0a7%2B-99b6418-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.11x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.12x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## darwin arm64 (darwin)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-06-03](results/bm-20230603-3.13.0a0-eaff9c3) | python | main | 3.13.0a0 | eaff9c3 | [1.24x faster](results/bm-20230603-3.13.0a0-eaff9c3/bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3-vs-3.10.4.md) | [1.02x faster](results/bm-20230603-3.13.0a0-eaff9c3/bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3-vs-3.11.0.md) |  |
| [2023-05-28](results/bm-20230528-3.13.0a0-3a5be87) | python | main | 3.13.0a0 | 3a5be87 | [1.19x faster](results/bm-20230528-3.13.0a0-3a5be87/bm-20230528-darwin-arm64-python-main-3.13.0a0-3a5be87-vs-3.10.4.md) | [1.02x slower](results/bm-20230528-3.13.0a0-3a5be87/bm-20230528-darwin-arm64-python-main-3.13.0a0-3a5be87-vs-3.11.0.md) |  |
| [2023-05-21](results/bm-20230521-3.12.0a7%2B-99b6418) | python | main | 3.12.0a7+ | 99b6418 | [1.19x faster](results/bm-20230521-3.12.0a7%2B-99b6418/bm-20230521-darwin-arm64-python-main-3.12.0a7%2B-99b6418-vs-3.10.4.md) | [1.02x slower](results/bm-20230521-3.12.0a7%2B-99b6418/bm-20230521-darwin-arm64-python-main-3.12.0a7%2B-99b6418-vs-3.11.0.md) |  |
| [2023-06-06](results/bm-20230606-3.11.4-d2340ef) | python | v3.11.4 | 3.11.4 | d2340ef | [1.25x faster](results/bm-20230606-3.11.4-d2340ef/bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef-vs-3.10.4.md) | [1.02x faster](results/bm-20230606-3.11.4-d2340ef/bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef-vs-3.11.0.md) |  |
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

