# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](../../actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

<!-- START table -->
## linux x86_64 (linux)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-08-06](results/bm-20230806-3.13.0a0-c209db9) | brandtbucher | justin | 3.13.0a0 | c209db9 | [1.25x faster](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.10.4.md) | [1.00x faster](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.11.0.md) | [1.04x slower](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-base.md) |
| [2023-08-06](results/bm-20230806-3.13.0a0-9564e31) | python | 9564e31cbc | 3.13.0a0 | 9564e31 | [1.30x faster](results/bm-20230806-3.13.0a0-9564e31/bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.10.4.md) | [1.04x faster](results/bm-20230806-3.13.0a0-9564e31/bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.11.0.md) |  |
| [2023-08-05](results/bm-20230805-3.13.0a0-6996b40) | python | main | 3.13.0a0 | 6996b40 | [1.30x faster](results/bm-20230805-3.13.0a0-6996b40/bm-20230805-linux-x86_64-python-main-3.13.0a0-6996b40-vs-3.10.4.md) | [1.04x faster](results/bm-20230805-3.13.0a0-6996b40/bm-20230805-linux-x86_64-python-main-3.13.0a0-6996b40-vs-3.11.0.md) |  |
| [2023-08-05](results/bm-20230805-3.13.0a0-930262f) | brandtbucher | tracing | 3.13.0a0 | 930262f | [1.23x faster](results/bm-20230805-3.13.0a0-930262f/bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f-vs-3.10.4.md) | [1.01x slower](results/bm-20230805-3.13.0a0-930262f/bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f-vs-3.11.0.md) | [1.06x slower](results/bm-20230805-3.13.0a0-930262f/bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f-vs-base.md) |
| [2023-08-05](results/bm-20230805-3.13.0a0-1d32835) | kumaraditya303 | linked_lis | 3.13.0a0 | 1d32835 | [1.31x faster](results/bm-20230805-3.13.0a0-1d32835/bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835-vs-3.10.4.md) | [1.05x faster](results/bm-20230805-3.13.0a0-1d32835/bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835-vs-3.11.0.md) | [1.01x faster](results/bm-20230805-3.13.0a0-1d32835/bm-20230805-linux-x86_64-kumaraditya303-linked_list-3.13.0a0-1d32835-vs-base.md) |
| [2023-08-05](results/bm-20230805-3.13.0a0-85e5b1f) | python | 85e5b1f5b8 | 3.13.0a0 | 85e5b1f | [1.30x faster](results/bm-20230805-3.13.0a0-85e5b1f/bm-20230805-linux-x86_64-python-85e5b1f5b806289744ef-3.13.0a0-85e5b1f-vs-3.10.4.md) | [1.04x faster](results/bm-20230805-3.13.0a0-85e5b1f/bm-20230805-linux-x86_64-python-85e5b1f5b806289744ef-3.13.0a0-85e5b1f-vs-3.11.0.md) |  |
| [2023-08-04](results/bm-20230804-3.13.0a0-2c25bd8) | python | 2c25bd82f4 | 3.13.0a0 | 2c25bd8 | [1.30x faster](results/bm-20230804-3.13.0a0-2c25bd8/bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8-vs-3.10.4.md) | [1.04x faster](results/bm-20230804-3.13.0a0-2c25bd8/bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8-vs-3.11.0.md) |  |
| [2023-08-04](results/bm-20230804-3.13.0a0-e03a937) | brandtbucher | binary_sub | 3.13.0a0 | e03a937 | [1.29x faster](results/bm-20230804-3.13.0a0-e03a937/bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937-vs-3.10.4.md) | [1.04x faster](results/bm-20230804-3.13.0a0-e03a937/bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937-vs-3.11.0.md) | [1.00x slower](results/bm-20230804-3.13.0a0-e03a937/bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937-vs-base.md) |
| [2023-08-05](results/bm-20230805-3.12.0b4%2B-236cdad) | python | 3.12 | 3.12.0b4+ | 236cdad | [1.28x faster](results/bm-20230805-3.12.0b4%2B-236cdad/bm-20230805-linux-x86_64-python-3.12-3.12.0b4%2B-236cdad-vs-3.10.4.md) | [1.03x faster](results/bm-20230805-3.12.0b4%2B-236cdad/bm-20230805-linux-x86_64-python-3.12-3.12.0b4%2B-236cdad-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.25x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.24x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## linux x86_64 (pythonperf2)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-08-06](results/bm-20230806-3.13.0a0-9016d52) | brandtbucher | uops_enabl | 3.13.0a0 | 9016d52 | [1.20x faster](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.10.4.md) | [1.02x slower](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.11.0.md) | [1.06x slower](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-base.md) |
| [2023-08-06](results/bm-20230806-3.13.0a0-c209db9) | brandtbucher | justin | 3.13.0a0 | c209db9 | [1.21x faster](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.10.4.md) | [1.00x slower](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.11.0.md) | [1.04x slower](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-base.md) |
| [2023-08-06](results/bm-20230806-3.13.0a0-9564e31) | python | 9564e31cbc | 3.13.0a0 | 9564e31 | [1.26x faster](results/bm-20230806-3.13.0a0-9564e31/bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.10.4.md) | [1.04x faster](results/bm-20230806-3.13.0a0-9564e31/bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.11.0.md) |  |
| [2023-08-05](results/bm-20230805-3.13.0a0-6996b40) | python | main | 3.13.0a0 | 6996b40 | [1.26x faster](results/bm-20230805-3.13.0a0-6996b40/bm-20230805-pythonperf2-x86_64-python-main-3.13.0a0-6996b40-vs-3.10.4.md) | [1.04x faster](results/bm-20230805-3.13.0a0-6996b40/bm-20230805-pythonperf2-x86_64-python-main-3.13.0a0-6996b40-vs-3.11.0.md) |  |
| [2023-08-04](results/bm-20230804-3.13.0a0-fb9e869) | faster-cpython | gc_scan_ro | 3.13.0a0 | fb9e869 | [1.26x faster](results/bm-20230804-3.13.0a0-fb9e869/bm-20230804-pythonperf2-x86_64-faster%252dcpython-gc_scan_roots-3.13.0a0-fb9e869-vs-3.10.4.md) | [1.03x faster](results/bm-20230804-3.13.0a0-fb9e869/bm-20230804-pythonperf2-x86_64-faster%252dcpython-gc_scan_roots-3.13.0a0-fb9e869-vs-3.11.0.md) | [1.01x slower](results/bm-20230804-3.13.0a0-fb9e869/bm-20230804-pythonperf2-x86_64-faster%252dcpython-gc_scan_roots-3.13.0a0-fb9e869-vs-base.md) |
| [2023-08-04](results/bm-20230804-3.13.0a0-3994224) | faster-cpython | gc_scan_ro | 3.13.0a0 | 3994224 | [1.26x faster](results/bm-20230804-3.13.0a0-3994224/bm-20230804-pythonperf2-x86_64-faster%252dcpython-gc_scan_roots-3.13.0a0-3994224-vs-3.10.4.md) | [1.04x faster](results/bm-20230804-3.13.0a0-3994224/bm-20230804-pythonperf2-x86_64-faster%252dcpython-gc_scan_roots-3.13.0a0-3994224-vs-3.11.0.md) | [1.00x slower](results/bm-20230804-3.13.0a0-3994224/bm-20230804-pythonperf2-x86_64-faster%252dcpython-gc_scan_roots-3.13.0a0-3994224-vs-base.md) |
| [2023-08-04](results/bm-20230804-3.13.0a0-2ba7c7f) | python | 2ba7c7f7b1 | 3.13.0a0 | 2ba7c7f | [1.26x faster](results/bm-20230804-3.13.0a0-2ba7c7f/bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f-vs-3.10.4.md) | [1.04x faster](results/bm-20230804-3.13.0a0-2ba7c7f/bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f-vs-3.11.0.md) |  |
| [2023-08-05](results/bm-20230805-3.12.0b4%2B-236cdad) | python | 3.12 | 3.12.0b4+ | 236cdad | [1.30x faster](results/bm-20230805-3.12.0b4%2B-236cdad/bm-20230805-pythonperf2-x86_64-python-3.12-3.12.0b4%2B-236cdad-vs-3.10.4.md) | [1.07x faster](results/bm-20230805-3.12.0b4%2B-236cdad/bm-20230805-pythonperf2-x86_64-python-3.12-3.12.0b4%2B-236cdad-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.21x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.21x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## windows amd64 (pythonperf1)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-08-06](results/bm-20230806-3.13.0a0-9016d52) | brandtbucher | uops_enabl | 3.13.0a0 | 9016d52 | [1.07x faster](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.10.4.md) | [1.04x slower](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.11.0.md) | [1.03x slower](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-base.md) |
| [2023-08-06](results/bm-20230806-3.13.0a0-c209db9) | brandtbucher | justin | 3.13.0a0 | c209db9 | [1.08x faster](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.10.4.md) | [1.03x slower](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.11.0.md) | [1.02x slower](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9-vs-base.md) |
| [2023-08-06](results/bm-20230806-3.13.0a0-9564e31) | python | 9564e31cbc | 3.13.0a0 | 9564e31 | [1.10x faster](results/bm-20230806-3.13.0a0-9564e31/bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.10.4.md) | [1.02x slower](results/bm-20230806-3.13.0a0-9564e31/bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.11.0.md) |  |
| [2023-08-05](results/bm-20230805-3.13.0a0-6996b40) | python | main | 3.13.0a0 | 6996b40 | [1.10x faster](results/bm-20230805-3.13.0a0-6996b40/bm-20230805-pythonperf1-amd64-python-main-3.13.0a0-6996b40-vs-3.10.4.md) | [1.02x slower](results/bm-20230805-3.13.0a0-6996b40/bm-20230805-pythonperf1-amd64-python-main-3.13.0a0-6996b40-vs-3.11.0.md) |  |
| [2023-08-05](results/bm-20230805-3.12.0b4%2B-236cdad) | python | 3.12 | 3.12.0b4+ | 236cdad | [1.16x faster](results/bm-20230805-3.12.0b4%2B-236cdad/bm-20230805-pythonperf1-amd64-python-3.12-3.12.0b4%2B-236cdad-vs-3.10.4.md) | [1.04x faster](results/bm-20230805-3.12.0b4%2B-236cdad/bm-20230805-pythonperf1-amd64-python-3.12-3.12.0b4%2B-236cdad-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.11x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.12x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## darwin arm64 (darwin)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-08-06](results/bm-20230806-3.13.0a0-9016d52) | brandtbucher | uops_enabl | 3.13.0a0 | 9016d52 | [1.13x faster](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.10.4.md) | [1.07x slower](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.11.0.md) | [1.04x slower](results/bm-20230806-3.13.0a0-9016d52/bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-base.md) |
| [2023-08-06](results/bm-20230806-3.13.0a0-c209db9) | brandtbucher | justin | 3.13.0a0 | c209db9 | [1.15x faster](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.10.4.md) | [1.05x slower](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.11.0.md) | [1.03x slower](results/bm-20230806-3.13.0a0-c209db9/bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9-vs-base.md) |
| [2023-08-06](results/bm-20230806-3.13.0a0-9564e31) | python | 9564e31cbc | 3.13.0a0 | 9564e31 | [1.18x faster](results/bm-20230806-3.13.0a0-9564e31/bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.10.4.md) | [1.03x slower](results/bm-20230806-3.13.0a0-9564e31/bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.11.0.md) |  |
| [2023-08-05](results/bm-20230805-3.13.0a0-6996b40) | python | main | 3.13.0a0 | 6996b40 | [1.18x faster](results/bm-20230805-3.13.0a0-6996b40/bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40-vs-3.10.4.md) | [1.02x slower](results/bm-20230805-3.13.0a0-6996b40/bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40-vs-3.11.0.md) |  |
| [2023-08-05](results/bm-20230805-3.12.0b4%2B-236cdad) | python | 3.12 | 3.12.0b4+ | 236cdad | [1.24x faster](results/bm-20230805-3.12.0b4%2B-236cdad/bm-20230805-darwin-arm64-python-3.12-3.12.0b4%2B-236cdad-vs-3.10.4.md) | [1.03x faster](results/bm-20230805-3.12.0b4%2B-236cdad/bm-20230805-darwin-arm64-python-3.12-3.12.0b4%2B-236cdad-vs-3.11.0.md) |  |
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

