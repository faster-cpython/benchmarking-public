# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](https://github.com/faster-cpython/benchmarking/actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

<!-- START table -->
## linux x86_64
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-02-10](results/bm-20230210-3.12.0a5%2B-685d559) | faster-cpython | specialize | 3.12.0a5+ | 685d559 | [1.30x faster \*](results/bm-20230210-3.12.0a5%2B-685d559/bm-20230210-linux-x86_64-faster%252dcpython-specialized_send-3.12.0a5%2B-685d559-vs-3.10.4.md) | [1.04x faster \*](results/bm-20230210-3.12.0a5%2B-685d559/bm-20230210-linux-x86_64-faster%252dcpython-specialized_send-3.12.0a5%2B-685d559-vs-3.11.0.md) | [1.01x faster](results/bm-20230210-3.12.0a5%2B-685d559/bm-20230210-linux-x86_64-faster%252dcpython-specialized_send-3.12.0a5%2B-685d559-vs-base.md) |
| [2023-02-10](results/bm-20230210-3.12.0a5%2B-cfb886d) | iritkatriel | int_freeli | 3.12.0a5+ | cfb886d | [1.29x faster \*](results/bm-20230210-3.12.0a5%2B-cfb886d/bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-cfb886d-vs-3.10.4.md) | [1.03x faster \*](results/bm-20230210-3.12.0a5%2B-cfb886d/bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-cfb886d-vs-3.11.0.md) | [1.00x slower](results/bm-20230210-3.12.0a5%2B-cfb886d/bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-cfb886d-vs-base.md) |
| [2023-02-10](results/bm-20230210-3.12.0a5%2B-d40a23c) | python | d40a23c0a1 | 3.12.0a5+ | d40a23c | [1.29x faster \*](results/bm-20230210-3.12.0a5%2B-d40a23c/bm-20230210-linux-x86_64-python-d40a23c0a11060ba7fa0-3.12.0a5%2B-d40a23c-vs-3.10.4.md) | [1.03x faster \*](results/bm-20230210-3.12.0a5%2B-d40a23c/bm-20230210-linux-x86_64-python-d40a23c0a11060ba7fa0-3.12.0a5%2B-d40a23c-vs-3.11.0.md) |  |
| [2023-02-09](results/bm-20230209-3.12.0a5%2B-f1f3af7) | python | f1f3af7b82 | 3.12.0a5+ | f1f3af7 | [1.30x faster \*](results/bm-20230209-3.12.0a5%2B-f1f3af7/bm-20230209-linux-x86_64-python-f1f3af7b8245e61a2e0a-3.12.0a5%2B-f1f3af7-vs-3.10.4.md) | [1.03x faster \*](results/bm-20230209-3.12.0a5%2B-f1f3af7/bm-20230209-linux-x86_64-python-f1f3af7b8245e61a2e0a-3.12.0a5%2B-f1f3af7-vs-3.11.0.md) |  |
| [2023-02-09](results/bm-20230209-3.12.0a5%2B-825f42a) | faster-cpython | pep_669_in | 3.12.0a5+ | 825f42a | [1.31x faster \*](results/bm-20230209-3.12.0a5%2B-825f42a/bm-20230209-linux-x86_64-faster%252dcpython-pep_669_incremental-3.12.0a5%2B-825f42a-vs-3.10.4.md) | [1.04x faster \*](results/bm-20230209-3.12.0a5%2B-825f42a/bm-20230209-linux-x86_64-faster%252dcpython-pep_669_incremental-3.12.0a5%2B-825f42a-vs-3.11.0.md) | [1.01x faster](results/bm-20230209-3.12.0a5%2B-825f42a/bm-20230209-linux-x86_64-faster%252dcpython-pep_669_incremental-3.12.0a5%2B-825f42a-vs-base.md) |
| [2023-02-09](results/bm-20230209-3.12.0a5%2B-827b81b) | iritkatriel | int_freeli | 3.12.0a5+ | 827b81b | [1.29x faster \*](results/bm-20230209-3.12.0a5%2B-827b81b/bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-827b81b-vs-3.10.4.md) | [1.02x faster \*](results/bm-20230209-3.12.0a5%2B-827b81b/bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-827b81b-vs-3.11.0.md) | [1.00x slower](results/bm-20230209-3.12.0a5%2B-827b81b/bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-827b81b-vs-base.md) |
| [2023-02-08](results/bm-20230208-3.12.0a5%2B-d9de079) | python | d9de079248 | 3.12.0a5+ | d9de079 | [1.29x faster \*](results/bm-20230208-3.12.0a5%2B-d9de079/bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5%2B-d9de079-vs-3.10.4.md) | [1.03x faster \*](results/bm-20230208-3.12.0a5%2B-d9de079/bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5%2B-d9de079-vs-3.11.0.md) |  |
| [2023-02-08](results/bm-20230208-3.12.0a5%2B-1134727) | iritkatriel | int_freeli | 3.12.0a5+ | 1134727 | [1.29x faster \*](results/bm-20230208-3.12.0a5%2B-1134727/bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-1134727-vs-3.10.4.md) | [1.02x faster \*](results/bm-20230208-3.12.0a5%2B-1134727/bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-1134727-vs-3.11.0.md) | [1.00x slower](results/bm-20230208-3.12.0a5%2B-1134727/bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-1134727-vs-base.md) |
| [2023-02-08](results/bm-20230208-3.12.0a5%2B-96e2742) | iritkatriel | object_ini | 3.12.0a5+ | 96e2742 | [1.30x faster \*](results/bm-20230208-3.12.0a5%2B-96e2742/bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5%2B-96e2742-vs-3.10.4.md) | [1.03x faster \*](results/bm-20230208-3.12.0a5%2B-96e2742/bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5%2B-96e2742-vs-3.11.0.md) | [1.00x faster](results/bm-20230208-3.12.0a5%2B-96e2742/bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5%2B-96e2742-vs-base.md) |
| [2023-02-08](results/bm-20230208-3.12.0a5%2B-1a4b9a9) | iritkatriel | object_ini | 3.12.0a5+ | 1a4b9a9 | [1.30x faster \*](results/bm-20230208-3.12.0a5%2B-1a4b9a9/bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5%2B-1a4b9a9-vs-3.10.4.md) | [1.03x faster \*](results/bm-20230208-3.12.0a5%2B-1a4b9a9/bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5%2B-1a4b9a9-vs-3.11.0.md) | [1.00x faster](results/bm-20230208-3.12.0a5%2B-1a4b9a9/bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5%2B-1a4b9a9-vs-base.md) |
| [2023-02-08](results/bm-20230208-3.12.0a5%2B-eb49d32) | python | eb49d32b9a | 3.12.0a5+ | eb49d32 | [1.29x faster \*](results/bm-20230208-3.12.0a5%2B-eb49d32/bm-20230208-linux-x86_64-python-eb49d32b9af0b3b01a55-3.12.0a5%2B-eb49d32-vs-3.10.4.md) | [1.03x faster \*](results/bm-20230208-3.12.0a5%2B-eb49d32/bm-20230208-linux-x86_64-python-eb49d32b9af0b3b01a55-3.12.0a5%2B-eb49d32-vs-3.11.0.md) |  |
| [2023-02-08](results/bm-20230208-3.12.0a5%2B-feec49c) | python | feec49c407 | 3.12.0a5+ | feec49c | [1.29x faster \*](results/bm-20230208-3.12.0a5%2B-feec49c/bm-20230208-linux-x86_64-python-feec49c40736fc05626a-3.12.0a5%2B-feec49c-vs-3.10.4.md) | [1.03x faster \*](results/bm-20230208-3.12.0a5%2B-feec49c/bm-20230208-linux-x86_64-python-feec49c40736fc05626a-3.12.0a5%2B-feec49c-vs-3.11.0.md) |  |
| [2023-02-08](results/bm-20230208-3.12.0a5%2B-cd69634) | gvanrossum | call_famil | 3.12.0a5+ | cd69634 | [1.30x faster \*](results/bm-20230208-3.12.0a5%2B-cd69634/bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-cd69634-vs-3.10.4.md) | [1.03x faster \*](results/bm-20230208-3.12.0a5%2B-cd69634/bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-cd69634-vs-3.11.0.md) | [1.00x slower](results/bm-20230208-3.12.0a5%2B-cd69634/bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-cd69634-vs-base.md) |
| [2023-02-08](results/bm-20230208-3.12.0a5%2B-4b64c3e) | brandtbucher | shrink_met | 3.12.0a5+ | 4b64c3e | [1.29x faster \*](results/bm-20230208-3.12.0a5%2B-4b64c3e/bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5%2B-4b64c3e-vs-3.10.4.md) | [1.02x faster \*](results/bm-20230208-3.12.0a5%2B-4b64c3e/bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5%2B-4b64c3e-vs-3.11.0.md) | [1.01x slower](results/bm-20230208-3.12.0a5%2B-4b64c3e/bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5%2B-4b64c3e-vs-base.md) |
| [2023-02-07](results/bm-20230207-3.12.0a5%2B-9595e01) | gvanrossum | call_famil | 3.12.0a5+ | 9595e01 | [1.29x faster \*](results/bm-20230207-3.12.0a5%2B-9595e01/bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-9595e01-vs-3.10.4.md) | [1.03x faster \*](results/bm-20230207-3.12.0a5%2B-9595e01/bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-9595e01-vs-3.11.0.md) | [1.00x slower](results/bm-20230207-3.12.0a5%2B-9595e01/bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-9595e01-vs-base.md) |
| [2023-02-07](results/bm-20230207-3.12.0a5%2B-a9f0144) | python | a9f01448a9 | 3.12.0a5+ | a9f0144 | [1.30x faster \*](results/bm-20230207-3.12.0a5%2B-a9f0144/bm-20230207-linux-x86_64-python-a9f01448a99c6a2ae34d-3.12.0a5%2B-a9f0144-vs-3.10.4.md) | [1.03x faster \*](results/bm-20230207-3.12.0a5%2B-a9f0144/bm-20230207-linux-x86_64-python-a9f01448a99c6a2ae34d-3.12.0a5%2B-a9f0144-vs-3.11.0.md) |  |
| [2023-02-07](results/bm-20230207-3.12.0a4%2B-dec1ab0) | python | main | 3.12.0a4+ | dec1ab0 | [1.29x faster \*](results/bm-20230207-3.12.0a4%2B-dec1ab0/bm-20230207-linux-x86_64-python-main-3.12.0a4%2B-dec1ab0-vs-3.10.4.md) | [1.03x faster \*](results/bm-20230207-3.12.0a4%2B-dec1ab0/bm-20230207-linux-x86_64-python-main-3.12.0a4%2B-dec1ab0-vs-3.11.0.md) |  |
| [2023-02-07](results/bm-20230207-3.12.0a4%2B-f1deb5c) | penguin-wwy | add_return | 3.12.0a4+ | f1deb5c | [1.30x faster \*](results/bm-20230207-3.12.0a4%2B-f1deb5c/bm-20230207-linux-x86_64-penguin%252dwwy-add_return_none-3.12.0a4%2B-f1deb5c-vs-3.10.4.md) | [1.03x faster \*](results/bm-20230207-3.12.0a4%2B-f1deb5c/bm-20230207-linux-x86_64-penguin%252dwwy-add_return_none-3.12.0a4%2B-f1deb5c-vs-3.11.0.md) | [1.01x faster](results/bm-20230207-3.12.0a4%2B-f1deb5c/bm-20230207-linux-x86_64-penguin%252dwwy-add_return_none-3.12.0a4%2B-f1deb5c-vs-base.md) |
| [2023-02-07](results/bm-20230207-3.12.0a4%2B-1f6d134) | brandtbucher | shrink_met | 3.12.0a4+ | 1f6d134 | [1.28x faster \*](results/bm-20230207-3.12.0a4%2B-1f6d134/bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4%2B-1f6d134-vs-3.10.4.md) | [1.02x faster \*](results/bm-20230207-3.12.0a4%2B-1f6d134/bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4%2B-1f6d134-vs-3.11.0.md) | [1.01x slower](results/bm-20230207-3.12.0a4%2B-1f6d134/bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4%2B-1f6d134-vs-base.md) |
| [2023-02-07](results/bm-20230207-3.12.0a4%2B-42ee27f) | iritkatriel | int_float_ | 3.12.0a4+ | 42ee27f | [1.30x faster \*](results/bm-20230207-3.12.0a4%2B-42ee27f/bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4%2B-42ee27f-vs-3.10.4.md) | [1.03x faster \*](results/bm-20230207-3.12.0a4%2B-42ee27f/bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4%2B-42ee27f-vs-3.11.0.md) | [1.00x faster](results/bm-20230207-3.12.0a4%2B-42ee27f/bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4%2B-42ee27f-vs-base.md) |
| [2023-02-07](results/bm-20230207-3.11.2-878ead1) | python | v3.11.2 | 3.11.2 | 878ead1 | [1.26x faster \*](results/bm-20230207-3.11.2-878ead1/bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1-vs-3.10.4.md) | [1.00x slower \*](results/bm-20230207-3.11.2-878ead1/bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.26x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2023-02-07](results/bm-20230207-3.10.10-aad5f6a) | python | v3.10.10 | 3.10.10 | aad5f6a | [1.00x slower \*](results/bm-20230207-3.10.10-aad5f6a/bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a-vs-3.10.4.md) | [1.26x slower \*](results/bm-20230207-3.10.10-aad5f6a/bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a-vs-3.11.0.md) |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.26x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## darwin arm64
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-02-04](results/bm-20230204-3.12.0a4%2B-5a2b984) | python | main | 3.12.0a4+ | 5a2b984 | [1.23x faster \*](results/bm-20230204-3.12.0a4%2B-5a2b984/bm-20230204-darwin-arm64-python-main-3.12.0a4%2B-5a2b984-vs-3.10.4.md) | [1.01x faster \*](results/bm-20230204-3.12.0a4%2B-5a2b984/bm-20230204-darwin-arm64-python-main-3.12.0a4%2B-5a2b984-vs-3.11.0.md) |  |
| [2023-01-28](results/bm-20230128-3.12.0a4%2B-666c084) | python | main | 3.12.0a4+ | 666c084 | [1.23x faster \*](results/bm-20230128-3.12.0a4%2B-666c084/bm-20230128-darwin-arm64-python-main-3.12.0a4%2B-666c084-vs-3.10.4.md) | [1.00x faster \*](results/bm-20230128-3.12.0a4%2B-666c084/bm-20230128-darwin-arm64-python-main-3.12.0a4%2B-666c084-vs-3.11.0.md) |  |
| [2023-01-26](results/bm-20230126-3.12.0a4%2B-e69c1f3) | gvanrossum | e69c1f3e7a | 3.12.0a4+ | e69c1f3 | [1.23x faster \*](results/bm-20230126-3.12.0a4%2B-e69c1f3/bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3-vs-3.10.4.md) | [1.00x faster \*](results/bm-20230126-3.12.0a4%2B-e69c1f3/bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3-vs-3.11.0.md) | [1.00x faster](results/bm-20230126-3.12.0a4%2B-e69c1f3/bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3-vs-base.md) |
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

