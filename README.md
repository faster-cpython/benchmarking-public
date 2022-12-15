# Faster CPython Benchmark Infrastructure

For documentation about how this works, see the [developer docs](DEVELOPER.md).

## Running benchmarks from the GitHub web UI

Visit the [benchmark action](https://github.com/faster-cpython/benchmarking/actions/workflows/benchmark.yml) and click the "Run Workflow" button.

The available parameters are:

- `fork`: The fork of CPython to benchmark.
  If benchmarking a pull request, this would normally be your GitHub username.
- `ref`: The branch, tag or commit SHA to benchmark.
  If a SHA, it must be the full SHA, since finding it by a prefix is not supported.
- `machine`: The machine to run on.
  One of `linux-amd64` (default), `windows-amd64`, `macos-arm64` or `all`.
- `benchmark_base`: If checked, the base of the selected branch will also be benchmarked.
  The base is determined by running `git merge-base upstream/main $ref`.
- `publish`: If checked, the results will be published in the public [ideas repo](https://github.com/faster-cpython/ideas) upon successful completion.

To watch the progress of the benchmark, select it from the [benchmark action page](https://github.com/faster-cpython/benchmarking/actions/workflows/benchmark.yml).
It may be canceled from there as well.
To show only your benchmark workflows, select your GitHub ID from the "Actor" dropdown.

When the benchmarking is complete, the results are published to this repository and will appear in the [master table](results/README.md).
Each set of benchmarks will have:

- The raw `.json` results from pyperformance.
- Comparisons against important reference releases, as well as the merge base of the branch if `benchmark_base` was selected.  These include
  - A markdown table produced by `pyperf compare_to`.
  - A set of "violin" plots showing the distribution of results for each benchmark.

The most convenient way to get results locally is to clone this repo and `git pull` from it.

## Running benchmarks from the GitHub CLI

To automate benchmarking runs, it may be more convenient to use the [GitHub CLI](https://cli.github.com/).
Once you have `gh` installed and configured, you can run benchmarks by cloning this repository and then from inside it:

```bash
$ gh workflow run benchmark.yml -f fork=me -f ref=my_branch
```

Any of the parameters described above are available at the commandline using the `-f key=value` syntax.

# Results

The following is only a summary of certain key revisions. There is also a [complete list of results](results/README.md).

<!-- START table -->
## linux amd64
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0b3: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2022-03-23](results/bm-20220323-python-main-3.10.4-9d38120) | python | main | 3.10.4 | 9d38120 |  | [1.29x slower](results/bm-20220323-python-main-3.10.4-9d38120/bm-20220323-linux-amd64-python-main-3.10.4-9d38120-vs-3.11.0b3.md) |  |
| [2021-12-08](results/bm-20211208-python-main-3.11.0a3-2e91dba) | python | main | 3.11.0a3 | 2e91dba | [1.19x faster](results/bm-20211208-python-main-3.11.0a3-2e91dba/bm-20211208-linux-amd64-python-main-3.11.0a3-2e91dba-vs-3.10.4.md) | [1.08x slower](results/bm-20211208-python-main-3.11.0a3-2e91dba/bm-20211208-linux-amd64-python-main-3.11.0a3-2e91dba-vs-3.11.0b3.md) |  |
| [2022-01-13](results/bm-20220113-python-main-3.11.0a4-9471106) | python | main | 3.11.0a4 | 9471106 | [1.21x faster](results/bm-20220113-python-main-3.11.0a4-9471106/bm-20220113-linux-amd64-python-main-3.11.0a4-9471106-vs-3.10.4.md) | [1.06x slower](results/bm-20220113-python-main-3.11.0a4-9471106/bm-20220113-linux-amd64-python-main-3.11.0a4-9471106-vs-3.11.0b3.md) |  |
| [2022-02-03](results/bm-20220203-python-main-3.11.0a5-c4e4b91) | python | main | 3.11.0a5 | c4e4b91 | [1.21x faster](results/bm-20220203-python-main-3.11.0a5-c4e4b91/bm-20220203-linux-amd64-python-main-3.11.0a5-c4e4b91-vs-3.10.4.md) | [1.06x slower](results/bm-20220203-python-main-3.11.0a5-c4e4b91/bm-20220203-linux-amd64-python-main-3.11.0a5-c4e4b91-vs-3.11.0b3.md) |  |
| [2022-03-07](results/bm-20220307-python-main-3.11.0a6-3ddfa55) | python | main | 3.11.0a6 | 3ddfa55 | [1.19x faster](results/bm-20220307-python-main-3.11.0a6-3ddfa55/bm-20220307-linux-amd64-python-main-3.11.0a6-3ddfa55-vs-3.10.4.md) | [1.08x slower](results/bm-20220307-python-main-3.11.0a6-3ddfa55/bm-20220307-linux-amd64-python-main-3.11.0a6-3ddfa55-vs-3.11.0b3.md) |  |
| [2022-04-05](results/bm-20220405-python-main-3.11.0a7-2e49bd0) | python | main | 3.11.0a7 | 2e49bd0 | [1.23x faster](results/bm-20220405-python-main-3.11.0a7-2e49bd0/bm-20220405-linux-amd64-python-main-3.11.0a7-2e49bd0-vs-3.10.4.md) | [1.04x slower](results/bm-20220405-python-main-3.11.0a7-2e49bd0/bm-20220405-linux-amd64-python-main-3.11.0a7-2e49bd0-vs-3.11.0b3.md) |  |
| [2022-05-06](results/bm-20220506-python-main-3.11.0b1-8d32a5c) | python | main | 3.11.0b1 | 8d32a5c | [1.28x faster](results/bm-20220506-python-main-3.11.0b1-8d32a5c/bm-20220506-linux-amd64-python-main-3.11.0b1-8d32a5c-vs-3.10.4.md) | [1.01x slower](results/bm-20220506-python-main-3.11.0b1-8d32a5c/bm-20220506-linux-amd64-python-main-3.11.0b1-8d32a5c-vs-3.11.0b3.md) |  |
| [2022-05-30](results/bm-20220530-python-main-3.11.0b2-72f00f4) | python | main | 3.11.0b2 | 72f00f4 | [1.28x faster](results/bm-20220530-python-main-3.11.0b2-72f00f4/bm-20220530-linux-amd64-python-main-3.11.0b2-72f00f4-vs-3.10.4.md) | [1.00x slower](results/bm-20220530-python-main-3.11.0b2-72f00f4/bm-20220530-linux-amd64-python-main-3.11.0b2-72f00f4-vs-3.11.0b3.md) |  |
| [2022-06-01](results/bm-20220601-python-main-3.11.0b3-eb0004c) | python | main | 3.11.0b3 | eb0004c | [1.29x faster](results/bm-20220601-python-main-3.11.0b3-eb0004c/bm-20220601-linux-amd64-python-main-3.11.0b3-eb0004c-vs-3.10.4.md) |  |  |
| [2022-10-22](results/bm-20221022-python-main-3.12.0a1+-f58631b) | python | main | 3.12.0a1+ | f58631b | [1.30x faster \*](results/bm-20221022-python-main-3.12.0a1+-f58631b/bm-20221022-linux-amd64-python-main-3.12.0a1+-f58631b-vs-3.10.4.md) | [1.01x faster \*](results/bm-20221022-python-main-3.12.0a1+-f58631b/bm-20221022-linux-amd64-python-main-3.12.0a1+-f58631b-vs-3.11.0b3.md) |  |
| [2022-11-12](results/bm-20221112-python-main-3.12.0a2+-57be545) | python | main | 3.12.0a2+ | 57be545 | [1.31x faster \*](results/bm-20221112-python-main-3.12.0a2+-57be545/bm-20221112-linux-amd64-python-main-3.12.0a2+-57be545-vs-3.10.4.md) | [1.01x faster \*](results/bm-20221112-python-main-3.12.0a2+-57be545/bm-20221112-linux-amd64-python-main-3.12.0a2+-57be545-vs-3.11.0b3.md) |  |
| [2022-11-19](results/bm-20221119-python-main-3.12.0a3+-b0e1f9c) | python | main | 3.12.0a3+ | b0e1f9c | [1.31x faster \*](results/bm-20221119-python-main-3.12.0a3+-b0e1f9c/bm-20221119-linux-amd64-python-main-3.12.0a3+-b0e1f9c-vs-3.10.4.md) | [1.02x faster \*](results/bm-20221119-python-main-3.12.0a3+-b0e1f9c/bm-20221119-linux-amd64-python-main-3.12.0a3+-b0e1f9c-vs-3.11.0b3.md) |  |

<!-- END table -->

`*` indicates that the exact same versions of pyperformance was not used.
