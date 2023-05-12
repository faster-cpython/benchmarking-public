# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](https://github.com/faster-cpython/benchmarking/actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

<!-- START table -->
## linux x86_64 (linux)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-05-12](results/bm-20230512-3.12.0a7%2B-434db68) | python | 434db68ee3 | 3.12.0a7+ | 434db68 | [1.28x faster](results/bm-20230512-3.12.0a7%2B-434db68/bm-20230512-linux-x86_64-python-434db68ee31514ddc4aa-3.12.0a7%2B-434db68-vs-3.10.4.md) | [1.03x faster](results/bm-20230512-3.12.0a7%2B-434db68/bm-20230512-linux-x86_64-python-434db68ee31514ddc4aa-3.12.0a7%2B-434db68-vs-3.11.0.md) |  |
| [2023-05-11](results/bm-20230511-3.12.0a7%2B-0449ffe) | python | 0449ffe3a4 | 3.12.0a7+ | 0449ffe | [1.27x faster](results/bm-20230511-3.12.0a7%2B-0449ffe/bm-20230511-linux-x86_64-python-0449ffe3a4ddf03367a5-3.12.0a7%2B-0449ffe-vs-3.10.4.md) | [1.02x faster](results/bm-20230511-3.12.0a7%2B-0449ffe/bm-20230511-linux-x86_64-python-0449ffe3a4ddf03367a5-3.12.0a7%2B-0449ffe-vs-3.11.0.md) |  |
| [2023-05-11](results/bm-20230511-3.12.0a7%2B-2cb76fa) | brandtbucher | always_inl | 3.12.0a7+ | 2cb76fa | [1.28x faster](results/bm-20230511-3.12.0a7%2B-2cb76fa/bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7%2B-2cb76fa-vs-3.10.4.md) | [1.03x faster](results/bm-20230511-3.12.0a7%2B-2cb76fa/bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7%2B-2cb76fa-vs-3.11.0.md) | [1.00x faster](results/bm-20230511-3.12.0a7%2B-2cb76fa/bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7%2B-2cb76fa-vs-base.md) |
| [2023-05-11](results/bm-20230511-3.12.0a7%2B-26d9521) | brandtbucher | eval_frame | 3.12.0a7+ | 26d9521 | [1.28x faster](results/bm-20230511-3.12.0a7%2B-26d9521/bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7%2B-26d9521-vs-3.10.4.md) | [1.03x faster](results/bm-20230511-3.12.0a7%2B-26d9521/bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7%2B-26d9521-vs-3.11.0.md) | [1.01x faster](results/bm-20230511-3.12.0a7%2B-26d9521/bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7%2B-26d9521-vs-base.md) |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.25x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.24x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## linux x86_64 (pythonperf2)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-05-11](results/bm-20230511-3.12.0a7%2B-e629ab6) | python | e629ab6adf | 3.12.0a7+ | e629ab6 | [1.27x faster \*](results/bm-20230511-3.12.0a7%2B-e629ab6/bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7%2B-e629ab6-vs-3.10.4.md) | [1.04x faster \*](results/bm-20230511-3.12.0a7%2B-e629ab6/bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7%2B-e629ab6-vs-3.11.0.md) |  |
| [2023-05-10](results/bm-20230510-3.12.0a7%2B-5418580) | faster-cpython | instrument | 3.12.0a7+ | 5418580 | [1.27x faster \*](results/bm-20230510-3.12.0a7%2B-5418580/bm-20230510-pythonperf2-x86_64-faster%252dcpython-instrument_all_possi-3.12.0a7%2B-5418580-vs-3.10.4.md) | [1.04x faster \*](results/bm-20230510-3.12.0a7%2B-5418580/bm-20230510-pythonperf2-x86_64-faster%252dcpython-instrument_all_possi-3.12.0a7%2B-5418580-vs-3.11.0.md) | [1.01x faster](results/bm-20230510-3.12.0a7%2B-5418580/bm-20230510-pythonperf2-x86_64-faster%252dcpython-instrument_all_possi-3.12.0a7%2B-5418580-vs-base.md) |
| [2023-05-06](results/bm-20230506-3.12.0a7%2B-42f54d1) | python | main | 3.12.0a7+ | 42f54d1 | [1.27x faster \*](results/bm-20230506-3.12.0a7%2B-42f54d1/bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7%2B-42f54d1-vs-3.10.4.md) | [1.04x faster \*](results/bm-20230506-3.12.0a7%2B-42f54d1/bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7%2B-42f54d1-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.21x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.21x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## windows amd64 (pythonperf1)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-05-06](results/bm-20230506-3.12.0a7%2B-42f54d1) | python | main | 3.12.0a7+ | 42f54d1 | [1.16x faster \*](results/bm-20230506-3.12.0a7%2B-42f54d1/bm-20230506-pythonperf1-amd64-python-main-3.12.0a7%2B-42f54d1-vs-3.10.4.md) | [1.05x faster \*](results/bm-20230506-3.12.0a7%2B-42f54d1/bm-20230506-pythonperf1-amd64-python-main-3.12.0a7%2B-42f54d1-vs-3.11.0.md) |  |
| [2023-05-04](results/bm-20230504-3.12.0a7%2B-f3fd844) | ericsnowcurrently | per_interp | 3.12.0a7+ | f3fd844 | [1.15x faster \*](results/bm-20230504-3.12.0a7%2B-f3fd844/bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.10.4.md) | [1.04x faster \*](results/bm-20230504-3.12.0a7%2B-f3fd844/bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.11.0.md) | [1.01x slower](results/bm-20230504-3.12.0a7%2B-f3fd844/bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-base.md) |
| [2023-05-03](results/bm-20230503-3.12.0a7%2B-e95dd40) | python | e95dd40aff | 3.12.0a7+ | e95dd40 | [1.17x faster \*](results/bm-20230503-3.12.0a7%2B-e95dd40/bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7%2B-e95dd40-vs-3.10.4.md) | [1.06x faster \*](results/bm-20230503-3.12.0a7%2B-e95dd40/bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7%2B-e95dd40-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.11x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.12x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## darwin arm64 (darwin)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-05-06](results/bm-20230506-3.12.0a7%2B-42f54d1) | python | main | 3.12.0a7+ | 42f54d1 | [1.15x faster \*](results/bm-20230506-3.12.0a7%2B-42f54d1/bm-20230506-darwin-arm64-python-main-3.12.0a7%2B-42f54d1-vs-3.10.4.md) | [1.05x slower \*](results/bm-20230506-3.12.0a7%2B-42f54d1/bm-20230506-darwin-arm64-python-main-3.12.0a7%2B-42f54d1-vs-3.11.0.md) |  |
| [2023-05-04](results/bm-20230504-3.12.0a7%2B-f3fd844) | ericsnowcurrently | per_interp | 3.12.0a7+ | f3fd844 | [1.15x faster \*](results/bm-20230504-3.12.0a7%2B-f3fd844/bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.10.4.md) | [1.05x slower \*](results/bm-20230504-3.12.0a7%2B-f3fd844/bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.11.0.md) | [1.00x slower](results/bm-20230504-3.12.0a7%2B-f3fd844/bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-base.md) |
| [2023-05-03](results/bm-20230503-3.12.0a7%2B-e95dd40) | python | e95dd40aff | 3.12.0a7+ | e95dd40 | [1.15x faster \*](results/bm-20230503-3.12.0a7%2B-e95dd40/bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7%2B-e95dd40-vs-3.10.4.md) | [1.05x slower \*](results/bm-20230503-3.12.0a7%2B-e95dd40/bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7%2B-e95dd40-vs-3.11.0.md) |  |
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

