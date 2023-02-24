# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](https://github.com/faster-cpython/benchmarking/actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

<!-- START table -->
## linux x86_64
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-02-24](results/bm-20230224-3.12.0a5%2B-7404033) | faster-cpython | backedge_c | 3.12.0a5+ | 7404033 | [1.30x faster](results/bm-20230224-3.12.0a5%2B-7404033/bm-20230224-linux-x86_64-faster%252dcpython-backedge_counter-3.12.0a5%2B-7404033-vs-3.10.4.md) | [1.04x faster](results/bm-20230224-3.12.0a5%2B-7404033/bm-20230224-linux-x86_64-faster%252dcpython-backedge_counter-3.12.0a5%2B-7404033-vs-3.11.0.md) | [1.00x faster](results/bm-20230224-3.12.0a5%2B-7404033/bm-20230224-linux-x86_64-faster%252dcpython-backedge_counter-3.12.0a5%2B-7404033-vs-base.md) |
| [2023-02-24](results/bm-20230224-3.12.0a5%2B-1fa3890) | python | 1fa38906f0 | 3.12.0a5+ | 1fa3890 | [1.30x faster](results/bm-20230224-3.12.0a5%2B-1fa3890/bm-20230224-linux-x86_64-python-1fa38906f0b228e6b0a6-3.12.0a5%2B-1fa3890-vs-3.10.4.md) | [1.03x faster](results/bm-20230224-3.12.0a5%2B-1fa3890/bm-20230224-linux-x86_64-python-1fa38906f0b228e6b0a6-3.12.0a5%2B-1fa3890-vs-3.11.0.md) |  |
| [2023-02-23](results/bm-20230223-3.12.0a5%2B-19b61a7) | iritkatriel | fetch_rest | 3.12.0a5+ | 19b61a7 | [1.29x faster](results/bm-20230223-3.12.0a5%2B-19b61a7/bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-19b61a7-vs-3.10.4.md) | [1.03x faster](results/bm-20230223-3.12.0a5%2B-19b61a7/bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-19b61a7-vs-3.11.0.md) | [1.00x slower](results/bm-20230223-3.12.0a5%2B-19b61a7/bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-19b61a7-vs-base.md) |
| [2023-02-23](results/bm-20230223-3.12.0a5%2B-d83af14) | iritkatriel | fetch_rest | 3.12.0a5+ | d83af14 | [1.30x faster](results/bm-20230223-3.12.0a5%2B-d83af14/bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-d83af14-vs-3.10.4.md) | [1.04x faster](results/bm-20230223-3.12.0a5%2B-d83af14/bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-d83af14-vs-3.11.0.md) | [1.01x faster](results/bm-20230223-3.12.0a5%2B-d83af14/bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-d83af14-vs-base.md) |
| [2023-02-23](results/bm-20230223-3.12.0a5%2B-c3a1783) | python | c3a178398c | 3.12.0a5+ | c3a1783 | [1.29x faster](results/bm-20230223-3.12.0a5%2B-c3a1783/bm-20230223-linux-x86_64-python-c3a178398c199038f3a0-3.12.0a5%2B-c3a1783-vs-3.10.4.md) | [1.03x faster](results/bm-20230223-3.12.0a5%2B-c3a1783/bm-20230223-linux-x86_64-python-c3a178398c199038f3a0-3.12.0a5%2B-c3a1783-vs-3.11.0.md) |  |
| [2023-02-23](results/bm-20230223-3.12.0a5%2B-d579d2e) | faster-cpython | pep_669 | 3.12.0a5+ | d579d2e | [1.31x faster](results/bm-20230223-3.12.0a5%2B-d579d2e/bm-20230223-linux-x86_64-faster%252dcpython-pep_669-3.12.0a5%2B-d579d2e-vs-3.10.4.md) | [1.05x faster](results/bm-20230223-3.12.0a5%2B-d579d2e/bm-20230223-linux-x86_64-faster%252dcpython-pep_669-3.12.0a5%2B-d579d2e-vs-3.11.0.md) | [1.01x faster](results/bm-20230223-3.12.0a5%2B-d579d2e/bm-20230223-linux-x86_64-faster%252dcpython-pep_669-3.12.0a5%2B-d579d2e-vs-base.md) |
| [2023-02-23](results/bm-20230223-3.12.0a5%2B-22b8d77) | python | 22b8d77b98 | 3.12.0a5+ | 22b8d77 | [1.30x faster](results/bm-20230223-3.12.0a5%2B-22b8d77/bm-20230223-linux-x86_64-python-22b8d77b98a5944e688b-3.12.0a5%2B-22b8d77-vs-3.10.4.md) | [1.04x faster](results/bm-20230223-3.12.0a5%2B-22b8d77/bm-20230223-linux-x86_64-python-22b8d77b98a5944e688b-3.12.0a5%2B-22b8d77-vs-3.11.0.md) |  |
| [2023-02-22](results/bm-20230222-3.12.0a5%2B-39ace64) | brandtbucher | compare_an | 3.12.0a5+ | 39ace64 | [1.30x faster](results/bm-20230222-3.12.0a5%2B-39ace64/bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5%2B-39ace64-vs-3.10.4.md) | [1.04x faster](results/bm-20230222-3.12.0a5%2B-39ace64/bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5%2B-39ace64-vs-3.11.0.md) | [1.00x slower](results/bm-20230222-3.12.0a5%2B-39ace64/bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5%2B-39ace64-vs-base.md) |
| [2023-02-22](results/bm-20230222-3.12.0a5%2B-d5c7954) | python | d5c7954d0c | 3.12.0a5+ | d5c7954 | [1.31x faster](results/bm-20230222-3.12.0a5%2B-d5c7954/bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5%2B-d5c7954-vs-3.10.4.md) | [1.05x faster](results/bm-20230222-3.12.0a5%2B-d5c7954/bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5%2B-d5c7954-vs-3.11.0.md) |  |
| [2023-02-21](results/bm-20230221-3.12.0a5%2B-cdd2a84) | brandtbucher | quicken_at | 3.12.0a5+ | cdd2a84 | [1.30x faster](results/bm-20230221-3.12.0a5%2B-cdd2a84/bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5%2B-cdd2a84-vs-3.10.4.md) | [1.04x faster](results/bm-20230221-3.12.0a5%2B-cdd2a84/bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5%2B-cdd2a84-vs-3.11.0.md) | [1.00x slower](results/bm-20230221-3.12.0a5%2B-cdd2a84/bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5%2B-cdd2a84-vs-base.md) |
| [2023-02-21](results/bm-20230221-3.12.0a5%2B-cf0df30) | brandtbucher | shrink_loa | 3.12.0a5+ | cf0df30 | [1.31x faster](results/bm-20230221-3.12.0a5%2B-cf0df30/bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5%2B-cf0df30-vs-3.10.4.md) | [1.04x faster](results/bm-20230221-3.12.0a5%2B-cf0df30/bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5%2B-cf0df30-vs-3.11.0.md) | [1.00x slower](results/bm-20230221-3.12.0a5%2B-cf0df30/bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5%2B-cf0df30-vs-base.md) |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.25x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.25x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## darwin arm64
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-02-18](results/bm-20230218-3.12.0a5%2B-61f1e67) | python | main | 3.12.0a5+ | 61f1e67 | [1.21x faster \*](results/bm-20230218-3.12.0a5%2B-61f1e67/bm-20230218-darwin-arm64-python-main-3.12.0a5%2B-61f1e67-vs-3.10.4.md) | [1.01x slower \*](results/bm-20230218-3.12.0a5%2B-61f1e67/bm-20230218-darwin-arm64-python-main-3.12.0a5%2B-61f1e67-vs-3.11.0.md) |  |
| [2023-02-11](results/bm-20230211-3.12.0a5%2B-3eb12df) | python | main | 3.12.0a5+ | 3eb12df | [1.24x faster \*](results/bm-20230211-3.12.0a5%2B-3eb12df/bm-20230211-darwin-arm64-python-main-3.12.0a5%2B-3eb12df-vs-3.10.4.md) | [1.02x faster \*](results/bm-20230211-3.12.0a5%2B-3eb12df/bm-20230211-darwin-arm64-python-main-3.12.0a5%2B-3eb12df-vs-3.11.0.md) |  |
| [2023-02-04](results/bm-20230204-3.12.0a4%2B-5a2b984) | python | main | 3.12.0a4+ | 5a2b984 | [1.23x faster \*](results/bm-20230204-3.12.0a4%2B-5a2b984/bm-20230204-darwin-arm64-python-main-3.12.0a4%2B-5a2b984-vs-3.10.4.md) | [1.01x faster \*](results/bm-20230204-3.12.0a4%2B-5a2b984/bm-20230204-darwin-arm64-python-main-3.12.0a4%2B-5a2b984-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | deaf509e8f | 3.11.0 | deaf509 | [1.22x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.22x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |


<!-- END table -->

`*` indicates that the exact same versions of pyperformance was not used.

![Longitudinal speed improvement](/longitudinal.png)

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

