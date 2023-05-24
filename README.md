# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](https://github.com/faster-cpython/benchmarking/actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

<!-- START table -->
## linux x86_64 (linux)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-05-23](results/bm-20230523-3.13.0a0-7390302) | kumaraditya303 | no_registe | 3.13.0a0 | 7390302 | [1.30x faster](results/bm-20230523-3.13.0a0-7390302/bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302-vs-3.10.4.md) | [1.04x faster](results/bm-20230523-3.13.0a0-7390302/bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302-vs-3.11.0.md) | [1.01x faster](results/bm-20230523-3.13.0a0-7390302/bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302-vs-base.md) |
| [2023-05-22](results/bm-20230522-3.13.0a0-5ecd8c8) | python | 5ecd8c85f9 | 3.13.0a0 | 5ecd8c8 | [1.28x faster](results/bm-20230522-3.13.0a0-5ecd8c8/bm-20230522-linux-x86_64-python-5ecd8c85f934e13a5ff9-3.13.0a0-5ecd8c8-vs-3.10.4.md) | [1.03x faster](results/bm-20230522-3.13.0a0-5ecd8c8/bm-20230522-linux-x86_64-python-5ecd8c85f934e13a5ff9-3.13.0a0-5ecd8c8-vs-3.11.0.md) |  |
| [2023-05-24](results/bm-20230524-3.12.0a7%2B-c991ccb) | faster-cpython | optimizer_ | 3.12.0a7+ | c991ccb | [1.27x faster](results/bm-20230524-3.12.0a7%2B-c991ccb/bm-20230524-linux-x86_64-faster%252dcpython-optimizer_api-3.12.0a7%2B-c991ccb-vs-3.10.4.md) | [1.02x faster](results/bm-20230524-3.12.0a7%2B-c991ccb/bm-20230524-linux-x86_64-faster%252dcpython-optimizer_api-3.12.0a7%2B-c991ccb-vs-3.11.0.md) | [1.01x slower](results/bm-20230524-3.12.0a7%2B-c991ccb/bm-20230524-linux-x86_64-faster%252dcpython-optimizer_api-3.12.0a7%2B-c991ccb-vs-base.md) |
| [2023-05-21](results/bm-20230521-3.12.0a7%2B-99b6418) | python | main | 3.12.0a7+ | 99b6418 | [1.27x faster](results/bm-20230521-3.12.0a7%2B-99b6418/bm-20230521-linux-x86_64-python-main-3.12.0a7%2B-99b6418-vs-3.10.4.md) | [1.02x faster](results/bm-20230521-3.12.0a7%2B-99b6418/bm-20230521-linux-x86_64-python-main-3.12.0a7%2B-99b6418-vs-3.11.0.md) |  |
| [2023-05-19](results/bm-20230519-3.12.0a7%2B-c26d03d) | python | c26d03d5d6 | 3.12.0a7+ | c26d03d | [1.27x faster](results/bm-20230519-3.12.0a7%2B-c26d03d/bm-20230519-linux-x86_64-python-c26d03d5d6da94367c7f-3.12.0a7%2B-c26d03d-vs-3.10.4.md) | [1.02x faster](results/bm-20230519-3.12.0a7%2B-c26d03d/bm-20230519-linux-x86_64-python-c26d03d5d6da94367c7f-3.12.0a7%2B-c26d03d-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.25x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.24x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## linux x86_64 (pythonperf2)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-05-21](results/bm-20230521-3.12.0a7%2B-99b6418) | python | main | 3.12.0a7+ | 99b6418 | [1.29x faster](results/bm-20230521-3.12.0a7%2B-99b6418/bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7%2B-99b6418-vs-3.10.4.md) | [1.07x faster](results/bm-20230521-3.12.0a7%2B-99b6418/bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7%2B-99b6418-vs-3.11.0.md) |  |
| [2023-05-15](results/bm-20230515-3.12.0a7%2B-b378d99) | python | b378d991f8 | 3.12.0a7+ | b378d99 | [1.29x faster](results/bm-20230515-3.12.0a7%2B-b378d99/bm-20230515-pythonperf2-x86_64-python-b378d991f8cd41c33416-3.12.0a7%2B-b378d99-vs-3.10.4.md) | [1.06x faster](results/bm-20230515-3.12.0a7%2B-b378d99/bm-20230515-pythonperf2-x86_64-python-b378d991f8cd41c33416-3.12.0a7%2B-b378d99-vs-3.11.0.md) |  |
| [2023-05-14](results/bm-20230514-3.12.0a7%2B-2cd1c87) | python | main | 3.12.0a7+ | 2cd1c87 | [1.30x faster](results/bm-20230514-3.12.0a7%2B-2cd1c87/bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7%2B-2cd1c87-vs-3.10.4.md) | [1.07x faster](results/bm-20230514-3.12.0a7%2B-2cd1c87/bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7%2B-2cd1c87-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.21x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.21x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## windows amd64 (pythonperf1)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-05-21](results/bm-20230521-3.12.0a7%2B-99b6418) | python | main | 3.12.0a7+ | 99b6418 | [1.18x faster](results/bm-20230521-3.12.0a7%2B-99b6418/bm-20230521-pythonperf1-amd64-python-main-3.12.0a7%2B-99b6418-vs-3.10.4.md) | [1.05x faster](results/bm-20230521-3.12.0a7%2B-99b6418/bm-20230521-pythonperf1-amd64-python-main-3.12.0a7%2B-99b6418-vs-3.11.0.md) |  |
| [2023-05-17](results/bm-20230517-3.12.0a7%2B-f7df173) | python | f7df173949 | 3.12.0a7+ | f7df173 | [1.18x faster](results/bm-20230517-3.12.0a7%2B-f7df173/bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7%2B-f7df173-vs-3.10.4.md) | [1.06x faster](results/bm-20230517-3.12.0a7%2B-f7df173/bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7%2B-f7df173-vs-3.11.0.md) |  |
| [2023-05-16](results/bm-20230516-3.12.0a7%2B-4f0355f) | adr26 | condvar | 3.12.0a7+ | 4f0355f | [1.17x faster](results/bm-20230516-3.12.0a7%2B-4f0355f/bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7%2B-4f0355f-vs-3.10.4.md) | [1.05x faster](results/bm-20230516-3.12.0a7%2B-4f0355f/bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7%2B-4f0355f-vs-3.11.0.md) | [1.01x faster](results/bm-20230516-3.12.0a7%2B-4f0355f/bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7%2B-4f0355f-vs-base.md) |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.11x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.12x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## darwin arm64 (darwin)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-05-21](results/bm-20230521-3.12.0a7%2B-99b6418) | python | main | 3.12.0a7+ | 99b6418 | [1.19x faster](results/bm-20230521-3.12.0a7%2B-99b6418/bm-20230521-darwin-arm64-python-main-3.12.0a7%2B-99b6418-vs-3.10.4.md) | [1.02x slower](results/bm-20230521-3.12.0a7%2B-99b6418/bm-20230521-darwin-arm64-python-main-3.12.0a7%2B-99b6418-vs-3.11.0.md) |  |
| [2023-05-13](results/bm-20230513-3.12.0a7%2B-7d2deaf) | python | main | 3.12.0a7+ | 7d2deaf | [1.19x faster](results/bm-20230513-3.12.0a7%2B-7d2deaf/bm-20230513-darwin-arm64-python-main-3.12.0a7%2B-7d2deaf-vs-3.10.4.md) | [1.01x slower](results/bm-20230513-3.12.0a7%2B-7d2deaf/bm-20230513-darwin-arm64-python-main-3.12.0a7%2B-7d2deaf-vs-3.11.0.md) |  |
| [2023-05-06](results/bm-20230506-3.12.0a7%2B-42f54d1) | python | main | 3.12.0a7+ | 42f54d1 | [1.15x faster \*](results/bm-20230506-3.12.0a7%2B-42f54d1/bm-20230506-darwin-arm64-python-main-3.12.0a7%2B-42f54d1-vs-3.10.4.md) | [1.05x slower \*](results/bm-20230506-3.12.0a7%2B-42f54d1/bm-20230506-darwin-arm64-python-main-3.12.0a7%2B-42f54d1-vs-3.11.0.md) |  |
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

