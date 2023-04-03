# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](https://github.com/faster-cpython/benchmarking/actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

<!-- START table -->
## linux x86_64 (linux)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-04-01](results/bm-20230401-3.12.0a6%2B-06249ec) | python | main | 3.12.0a6+ | 06249ec | [1.29x faster](results/bm-20230401-3.12.0a6%2B-06249ec/bm-20230401-linux-x86_64-python-main-3.12.0a6%2B-06249ec-vs-3.10.4.md) | [1.03x faster](results/bm-20230401-3.12.0a6%2B-06249ec/bm-20230401-linux-x86_64-python-main-3.12.0a6%2B-06249ec-vs-3.11.0.md) |  |
| [2023-03-29](results/bm-20230329-3.12.0a6%2B-e375bff) | python | e375bff037 | 3.12.0a6+ | e375bff | [1.29x faster](results/bm-20230329-3.12.0a6%2B-e375bff/bm-20230329-linux-x86_64-python-e375bff03736f809fbc2-3.12.0a6%2B-e375bff-vs-3.10.4.md) | [1.03x faster](results/bm-20230329-3.12.0a6%2B-e375bff/bm-20230329-linux-x86_64-python-e375bff03736f809fbc2-3.12.0a6%2B-e375bff-vs-3.11.0.md) |  |
| [2023-03-27](results/bm-20230327-3.12.0a6%2B-e53ac85) | ericsnowcurrently | isolate_in | 3.12.0a6+ | e53ac85 | [1.30x faster](results/bm-20230327-3.12.0a6%2B-e53ac85/bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6%2B-e53ac85-vs-3.10.4.md) | [1.04x faster](results/bm-20230327-3.12.0a6%2B-e53ac85/bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6%2B-e53ac85-vs-3.11.0.md) | [1.00x slower](results/bm-20230327-3.12.0a6%2B-e53ac85/bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6%2B-e53ac85-vs-base.md) |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | deaf509e8f | 3.11.0 | deaf509 | [1.25x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | 9d38120e33 | 3.10.4 | 9d38120 |  | [1.25x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120-vs-3.11.0.md) |  |

## linux x86_64 (pythonperf2)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-04-01](results/bm-20230401-3.12.0a6%2B-06249ec) | python | main | 3.12.0a6+ | 06249ec | [1.24x faster](results/bm-20230401-3.12.0a6%2B-06249ec/bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6%2B-06249ec-vs-3.10.4.md) | [1.02x faster](results/bm-20230401-3.12.0a6%2B-06249ec/bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6%2B-06249ec-vs-3.11.0.md) |  |
| [2023-03-25](results/bm-20230325-3.12.0a6%2B-30a306c) | python | main | 3.12.0a6+ | 30a306c | [1.26x faster](results/bm-20230325-3.12.0a6%2B-30a306c/bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6%2B-30a306c-vs-3.10.4.md) | [1.03x faster](results/bm-20230325-3.12.0a6%2B-30a306c/bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6%2B-30a306c-vs-3.11.0.md) |  |
| [2023-03-06](results/bm-20230306-3.12.0a5%2B-f533f21) | python | f533f216e6 | 3.12.0a5+ | f533f21 | [1.26x faster](results/bm-20230306-3.12.0a5%2B-f533f21/bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5%2B-f533f21-vs-3.10.4.md) | [1.03x faster](results/bm-20230306-3.12.0a5%2B-f533f21/bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5%2B-f533f21-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | deaf509e8f | 3.11.0 | deaf509 | [1.22x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.22x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## windows amd64 (pythonperf1)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-04-01](results/bm-20230401-3.12.0a6%2B-06249ec) | python | main | 3.12.0a6+ | 06249ec | [1.19x faster](results/bm-20230401-3.12.0a6%2B-06249ec/bm-20230401-pythonperf1-amd64-python-main-3.12.0a6%2B-06249ec-vs-3.10.4.md) | [1.07x faster](results/bm-20230401-3.12.0a6%2B-06249ec/bm-20230401-pythonperf1-amd64-python-main-3.12.0a6%2B-06249ec-vs-3.11.0.md) |  |
| [2023-03-25](results/bm-20230325-3.12.0a6%2B-30a306c) | python | main | 3.12.0a6+ | 30a306c | [1.21x faster](results/bm-20230325-3.12.0a6%2B-30a306c/bm-20230325-pythonperf1-amd64-python-main-3.12.0a6%2B-30a306c-vs-3.10.4.md) | [1.09x faster](results/bm-20230325-3.12.0a6%2B-30a306c/bm-20230325-pythonperf1-amd64-python-main-3.12.0a6%2B-30a306c-vs-3.11.0.md) |  |
| [2023-03-24](results/bm-20230324-3.12.0a6%2B-d494091) | python | d49409196e | 3.12.0a6+ | d494091 | [1.23x faster](results/bm-20230324-3.12.0a6%2B-d494091/bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6%2B-d494091-vs-3.10.4.md) | [1.11x faster](results/bm-20230324-3.12.0a6%2B-d494091/bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6%2B-d494091-vs-3.11.0.md) |  |
| [2023-01-13](results/bm-20230113-3.12.0a4%2B-010576c) | python | 010576c6ea | 3.12.0a4+ | 010576c | [1.20x faster](results/bm-20230113-3.12.0a4%2B-010576c/bm-20230113-pythonperf1-amd64-python-010576c6ea7e687cf2cb-3.12.0a4%2B-010576c-vs-3.10.4.md) | [1.09x faster](results/bm-20230113-3.12.0a4%2B-010576c/bm-20230113-pythonperf1-amd64-python-010576c6ea7e687cf2cb-3.12.0a4%2B-010576c-vs-3.11.0.md) |  |
| [2022-11-12](results/bm-20221112-3.12.0a1%2B-99972dc) | python | 99972dc745 | 3.12.0a1+ | 99972dc | [1.16x faster](results/bm-20221112-3.12.0a1%2B-99972dc/bm-20221112-pythonperf1-amd64-python-99972dc7450f1266e392-3.12.0a1%2B-99972dc-vs-3.10.4.md) | [1.05x faster](results/bm-20221112-3.12.0a1%2B-99972dc/bm-20221112-pythonperf1-amd64-python-99972dc7450f1266e392-3.12.0a1%2B-99972dc-vs-3.11.0.md) |  |
| [2022-11-11](results/bm-20221111-3.12.0a1%2B-3dd6ee2) | python | 3dd6ee2c00 | 3.12.0a1+ | 3dd6ee2 | [1.16x faster](results/bm-20221111-3.12.0a1%2B-3dd6ee2/bm-20221111-pythonperf1-amd64-python-3dd6ee2c0022cb49e5cb-3.12.0a1%2B-3dd6ee2-vs-3.10.4.md) | [1.05x faster](results/bm-20221111-3.12.0a1%2B-3dd6ee2/bm-20221111-pythonperf1-amd64-python-3dd6ee2c0022cb49e5cb-3.12.0a1%2B-3dd6ee2-vs-3.11.0.md) |  |
| [2022-11-10](results/bm-20221110-3.12.0a1%2B-6dedf42) | python | 6dedf42527 | 3.12.0a1+ | 6dedf42 | [1.16x faster](results/bm-20221110-3.12.0a1%2B-6dedf42/bm-20221110-pythonperf1-amd64-python-6dedf42527fddbed8ef6-3.12.0a1%2B-6dedf42-vs-3.10.4.md) | [1.05x faster](results/bm-20221110-3.12.0a1%2B-6dedf42/bm-20221110-pythonperf1-amd64-python-6dedf42527fddbed8ef6-3.12.0a1%2B-6dedf42-vs-3.11.0.md) |  |
| [2022-11-09](results/bm-20221109-3.12.0a1%2B-c03e05c) | python | c03e05c2e7 | 3.12.0a1+ | c03e05c | [1.09x faster](results/bm-20221109-3.12.0a1%2B-c03e05c/bm-20221109-pythonperf1-amd64-python-c03e05c2e72f3ea5e797-3.12.0a1%2B-c03e05c-vs-3.10.4.md) | [1.01x slower](results/bm-20221109-3.12.0a1%2B-c03e05c/bm-20221109-pythonperf1-amd64-python-c03e05c2e72f3ea5e797-3.12.0a1%2B-c03e05c-vs-3.11.0.md) |  |
| [2022-11-04](results/bm-20221104-3.12.0a1%2B-044bcc1) | python | 044bcc1771 | 3.12.0a1+ | 044bcc1 | [1.11x faster](results/bm-20221104-3.12.0a1%2B-044bcc1/bm-20221104-pythonperf1-amd64-python-044bcc1771fe7e2f8eba-3.12.0a1%2B-044bcc1-vs-3.10.4.md) | [1.00x slower](results/bm-20221104-3.12.0a1%2B-044bcc1/bm-20221104-pythonperf1-amd64-python-044bcc1771fe7e2f8eba-3.12.0a1%2B-044bcc1-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | deaf509e8f | 3.11.0 | deaf509 | [1.11x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | 9d38120e33 | 3.10.4 | 9d38120 |  | [1.11x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120-vs-3.11.0.md) |  |

## darwin arm64 (darwin)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-04-01](results/bm-20230401-3.12.0a6%2B-06249ec) | python | main | 3.12.0a6+ | 06249ec | [1.19x faster](results/bm-20230401-3.12.0a6%2B-06249ec/bm-20230401-darwin-arm64-python-main-3.12.0a6%2B-06249ec-vs-3.10.4.md) | [1.01x slower](results/bm-20230401-3.12.0a6%2B-06249ec/bm-20230401-darwin-arm64-python-main-3.12.0a6%2B-06249ec-vs-3.11.0.md) |  |
| [2023-03-25](results/bm-20230325-3.12.0a6%2B-30a306c) | python | main | 3.12.0a6+ | 30a306c | [1.19x faster](results/bm-20230325-3.12.0a6%2B-30a306c/bm-20230325-darwin-arm64-python-main-3.12.0a6%2B-30a306c-vs-3.10.4.md) | [1.02x slower](results/bm-20230325-3.12.0a6%2B-30a306c/bm-20230325-darwin-arm64-python-main-3.12.0a6%2B-30a306c-vs-3.11.0.md) |  |
| [2023-03-18](results/bm-20230318-3.12.0a6%2B-3adb23a) | python | main | 3.12.0a6+ | 3adb23a | [1.20x faster](results/bm-20230318-3.12.0a6%2B-3adb23a/bm-20230318-darwin-arm64-python-main-3.12.0a6%2B-3adb23a-vs-3.10.4.md) | [1.00x slower](results/bm-20230318-3.12.0a6%2B-3adb23a/bm-20230318-darwin-arm64-python-main-3.12.0a6%2B-3adb23a-vs-3.11.0.md) |  |
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

