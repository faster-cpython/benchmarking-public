# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](../../actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

<!-- START table -->
## linux x86_64 (linux)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-08-10](results/bm-20230810-3.13.0a0-87a3230) | faster-cpython | deepcopy_d | 3.13.0a0 | 87a3230 | [1.30x faster](results/bm-20230810-3.13.0a0-87a3230/bm-20230810-linux-x86_64-faster%252dcpython-deepcopy_demateriali-3.13.0a0-87a3230-vs-3.10.4.md) | [1.04x faster](results/bm-20230810-3.13.0a0-87a3230/bm-20230810-linux-x86_64-faster%252dcpython-deepcopy_demateriali-3.13.0a0-87a3230-vs-3.11.0.md) |  |
| [2023-08-10](results/bm-20230810-3.13.0a0-17ae178) | faster-cpython | always_all | 3.13.0a0 | 17ae178 | [1.30x faster](results/bm-20230810-3.13.0a0-17ae178/bm-20230810-linux-x86_64-faster%252dcpython-always_allocate_valu-3.13.0a0-17ae178-vs-3.10.4.md) | [1.04x faster](results/bm-20230810-3.13.0a0-17ae178/bm-20230810-linux-x86_64-faster%252dcpython-always_allocate_valu-3.13.0a0-17ae178-vs-3.11.0.md) |  |
| [2023-08-08](results/bm-20230808-3.13.0a0-aab6f71) | python | aab6f7173a | 3.13.0a0 | aab6f71 | [1.30x faster](results/bm-20230808-3.13.0a0-aab6f71/bm-20230808-linux-x86_64-python-aab6f7173a3b82559962-3.13.0a0-aab6f71-vs-3.10.4.md) | [1.04x faster](results/bm-20230808-3.13.0a0-aab6f71/bm-20230808-linux-x86_64-python-aab6f7173a3b82559962-3.13.0a0-aab6f71-vs-3.11.0.md) |  |
| [2023-08-07](results/bm-20230807-3.13.0a0-16c9415) | python | 16c9415fba | 3.13.0a0 | 16c9415 | [1.30x faster](results/bm-20230807-3.13.0a0-16c9415/bm-20230807-linux-x86_64-python-16c9415fba4972743f19-3.13.0a0-16c9415-vs-3.10.4.md) | [1.05x faster](results/bm-20230807-3.13.0a0-16c9415/bm-20230807-linux-x86_64-python-16c9415fba4972743f19-3.13.0a0-16c9415-vs-3.11.0.md) |  |
| [2023-08-06](results/bm-20230806-3.13.0a0-9016d52) | brandtbucher | uops_enabl | 3.13.0a0 | 9016d52 | [1.24x faster](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.10.4.md) | [1.00x slower](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.11.0.md) | [1.05x slower](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-base.md) |
| [2023-08-06](results/bm-20230806-3.13.0a0-9564e31) | python | 9564e31cbc | 3.13.0a0 | 9564e31 | [1.30x faster](results/bm-20230806-3.13.0a0-9564e31/bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.10.4.md) | [1.04x faster](results/bm-20230806-3.13.0a0-9564e31/bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.11.0.md) |  |
| [2023-08-05](results/bm-20230805-3.13.0a0-d42d2e6) | brandtbucher | un_materia | 3.13.0a0 | d42d2e6 | [1.30x faster](results/bm-20230805-3.13.0a0-d42d2e6/bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6-vs-3.10.4.md) | [1.04x faster](results/bm-20230805-3.13.0a0-d42d2e6/bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6-vs-3.11.0.md) | [1.00x slower](results/bm-20230805-3.13.0a0-d42d2e6/bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6-vs-base.md) |
| [2023-08-05](results/bm-20230805-3.13.0a0-f565bc6) | brandtbucher | calls | 3.13.0a0 | f565bc6 | [1.30x faster](results/bm-20230805-3.13.0a0-f565bc6/bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6-vs-3.10.4.md) | [1.04x faster](results/bm-20230805-3.13.0a0-f565bc6/bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6-vs-3.11.0.md) | [1.00x slower](results/bm-20230805-3.13.0a0-f565bc6/bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6-vs-base.md) |
| [2023-08-05](results/bm-20230805-3.13.0a0-f077383) | brandtbucher | binary_sub | 3.13.0a0 | f077383 | [1.31x faster](results/bm-20230805-3.13.0a0-f077383/bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383-vs-3.10.4.md) | [1.05x faster](results/bm-20230805-3.13.0a0-f077383/bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383-vs-3.11.0.md) | [1.00x faster](results/bm-20230805-3.13.0a0-f077383/bm-20230805-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-f077383-vs-base.md) |
| [2023-08-05](results/bm-20230805-3.13.0a0-0ccd3bb) | faster-cpython | tweak_ints | 3.13.0a0 | 0ccd3bb | [1.29x faster](results/bm-20230805-3.13.0a0-0ccd3bb/bm-20230805-linux-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb-vs-3.10.4.md) | [1.04x faster](results/bm-20230805-3.13.0a0-0ccd3bb/bm-20230805-linux-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb-vs-3.11.0.md) |  |
| [2023-08-05](results/bm-20230805-3.13.0a0-b2495de) | brandtbucher | un_materia | 3.13.0a0 | b2495de | [1.29x faster](results/bm-20230805-3.13.0a0-b2495de/bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de-vs-3.10.4.md) | [1.04x faster](results/bm-20230805-3.13.0a0-b2495de/bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de-vs-3.11.0.md) | [1.01x slower](results/bm-20230805-3.13.0a0-b2495de/bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de-vs-base.md) |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.25x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.24x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## linux x86_64 (pythonperf2)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-08-07](results/bm-20230807-3.13.0a0-2ac103c) | python | 2ac103c346 | 3.13.0a0 | 2ac103c | [1.26x faster](results/bm-20230807-3.13.0a0-2ac103c/bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c-vs-3.10.4.md) | [1.04x faster](results/bm-20230807-3.13.0a0-2ac103c/bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c-vs-3.11.0.md) |  |
| [2023-08-06](results/bm-20230806-3.13.0a0-9016d52) | brandtbucher | uops_enabl | 3.13.0a0 | 9016d52 | [1.20x faster](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.10.4.md) | [1.02x slower](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.11.0.md) | [1.06x slower](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-base.md) |
| [2023-08-06](results/bm-20230806-3.13.0a0-c209db9) | brandtbucher | justin | 3.13.0a0 | c209db9 | [1.21x faster](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.10.4.md) | [1.00x slower](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.11.0.md) | [1.04x slower](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-base.md) |
| [2023-08-06](results/bm-20230806-3.13.0a0-9564e31) | python | 9564e31cbc | 3.13.0a0 | 9564e31 | [1.26x faster](results/bm-20230806-3.13.0a0-9564e31/bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.10.4.md) | [1.04x faster](results/bm-20230806-3.13.0a0-9564e31/bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.11.0.md) |  |
| [2023-08-05](results/bm-20230805-3.13.0a0-83ffca9) | faster-cpython | tweak_ints | 3.13.0a0 | 83ffca9 | [1.27x faster](results/bm-20230805-3.13.0a0-83ffca9/bm-20230805-pythonperf2-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9-vs-3.10.4.md) | [1.04x faster](results/bm-20230805-3.13.0a0-83ffca9/bm-20230805-pythonperf2-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9-vs-3.11.0.md) | [1.00x faster](results/bm-20230805-3.13.0a0-83ffca9/bm-20230805-pythonperf2-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9-vs-base.md) |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.21x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.21x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## windows amd64 (pythonperf1)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-08-06](results/bm-20230806-3.13.0a0-9016d52) | brandtbucher | uops_enabl | 3.13.0a0 | 9016d52 | [1.07x faster](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.10.4.md) | [1.04x slower](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.11.0.md) | [1.03x slower](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-base.md) |
| [2023-08-06](results/bm-20230806-3.13.0a0-c209db9) | brandtbucher | justin | 3.13.0a0 | c209db9 | [1.08x faster](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.10.4.md) | [1.03x slower](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.11.0.md) | [1.02x slower](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9-vs-base.md) |
| [2023-08-06](results/bm-20230806-3.13.0a0-9564e31) | python | 9564e31cbc | 3.13.0a0 | 9564e31 | [1.10x faster](results/bm-20230806-3.13.0a0-9564e31/bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.10.4.md) | [1.02x slower](results/bm-20230806-3.13.0a0-9564e31/bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.11x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.12x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## darwin arm64 (darwin)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-08-06](results/bm-20230806-3.13.0a0-9016d52) | brandtbucher | uops_enabl | 3.13.0a0 | 9016d52 | [1.13x faster](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.10.4.md) | [1.07x slower](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.11.0.md) | [1.04x slower](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-base.md) |
| [2023-08-06](results/bm-20230806-3.13.0a0-c209db9) | brandtbucher | justin | 3.13.0a0 | c209db9 | [1.15x faster](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.10.4.md) | [1.05x slower](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.11.0.md) | [1.03x slower](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9-vs-base.md) |
| [2023-08-06](results/bm-20230806-3.13.0a0-9564e31) | python | 9564e31cbc | 3.13.0a0 | 9564e31 | [1.18x faster](results/bm-20230806-3.13.0a0-9564e31/bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.10.4.md) | [1.03x slower](results/bm-20230806-3.13.0a0-9564e31/bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.11.0.md) |  |
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

