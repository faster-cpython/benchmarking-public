# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](https://github.com/faster-cpython/benchmarking/actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

<!-- START table -->
## linux x86_64 (linux)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-03-18](results/bm-20230318-3.12.0a6%2B-3adb23a) | python | main | 3.12.0a6+ | 3adb23a | [1.30x faster \*](results/bm-20230318-3.12.0a6%2B-3adb23a/bm-20230318-linux-x86_64-python-main-3.12.0a6%2B-3adb23a-vs-3.10.4.md) | [1.04x faster \*](results/bm-20230318-3.12.0a6%2B-3adb23a/bm-20230318-linux-x86_64-python-main-3.12.0a6%2B-3adb23a-vs-3.11.0.md) |  |
| [2023-03-17](results/bm-20230317-3.12.0a6%2B-4f5774f) | python | 4f5774f648 | 3.12.0a6+ | 4f5774f | [1.31x faster \*](results/bm-20230317-3.12.0a6%2B-4f5774f/bm-20230317-linux-x86_64-python-4f5774f648eafd1a7076-3.12.0a6%2B-4f5774f-vs-3.10.4.md) | [1.04x faster \*](results/bm-20230317-3.12.0a6%2B-4f5774f/bm-20230317-linux-x86_64-python-4f5774f648eafd1a7076-3.12.0a6%2B-4f5774f-vs-3.11.0.md) |  |
| [2023-03-16](results/bm-20230316-3.12.0a6%2B-034e2bf) | brandtbucher | de_epfreez | 3.12.0a6+ | 034e2bf | [1.29x faster \*](results/bm-20230316-3.12.0a6%2B-034e2bf/bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6%2B-034e2bf-vs-3.10.4.md) | [1.03x faster \*](results/bm-20230316-3.12.0a6%2B-034e2bf/bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6%2B-034e2bf-vs-3.11.0.md) | [1.01x slower](results/bm-20230316-3.12.0a6%2B-034e2bf/bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6%2B-034e2bf-vs-base.md) |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.25x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.25x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## darwin arm64 (darwin)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-03-18](results/bm-20230318-3.12.0a6%2B-3adb23a) | python | main | 3.12.0a6+ | 3adb23a | [1.20x faster \*](results/bm-20230318-3.12.0a6%2B-3adb23a/bm-20230318-darwin-arm64-python-main-3.12.0a6%2B-3adb23a-vs-3.10.4.md) | [1.02x slower \*](results/bm-20230318-3.12.0a6%2B-3adb23a/bm-20230318-darwin-arm64-python-main-3.12.0a6%2B-3adb23a-vs-3.11.0.md) |  |
| [2023-03-11](results/bm-20230311-3.12.0a6%2B-bb396ee) | python | main | 3.12.0a6+ | bb396ee | [1.19x faster \*](results/bm-20230311-3.12.0a6%2B-bb396ee/bm-20230311-darwin-arm64-python-main-3.12.0a6%2B-bb396ee-vs-3.10.4.md) | [1.02x slower \*](results/bm-20230311-3.12.0a6%2B-bb396ee/bm-20230311-darwin-arm64-python-main-3.12.0a6%2B-bb396ee-vs-3.11.0.md) |  |
| [2023-03-06](results/bm-20230306-3.12.0a5%2B-d3ca042) | python | main | 3.12.0a5+ | d3ca042 | [1.20x faster \*](results/bm-20230306-3.12.0a5%2B-d3ca042/bm-20230306-darwin-arm64-python-main-3.12.0a5%2B-d3ca042-vs-3.10.4.md) | [1.02x slower \*](results/bm-20230306-3.12.0a5%2B-d3ca042/bm-20230306-darwin-arm64-python-main-3.12.0a5%2B-d3ca042-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | deaf509e8f | 3.11.0 | deaf509 | [1.22x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.22x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |


<!-- END table -->

`*` indicates that the exact same versions of pyperformance was not used.

![Longitudinal speed improvement](/longitudinal.png)

Improvement of the geometric mean of all benchmarks vs. 3.10.4, computed with `pyperf compare`.
The results have a resolution of 0.01.

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

