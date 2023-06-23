# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](../../actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

<!-- START table -->
## linux x86_64 (linux)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-06-22](results/bm-20230622-3.13.0a0-13237a2) | python | 13237a2da8 | 3.13.0a0 | 13237a2 | [1.31x faster](results/bm-20230622-3.13.0a0-13237a2/bm-20230622-linux-x86_64-python-13237a2da846efef9ce9-3.13.0a0-13237a2-vs-3.10.4.md) | [1.05x faster](results/bm-20230622-3.13.0a0-13237a2/bm-20230622-linux-x86_64-python-13237a2da846efef9ce9-3.13.0a0-13237a2-vs-3.11.0.md) |  |
| [2023-06-22](results/bm-20230622-3.13.0a0-a4e456f) | brandtbucher | un_materia | 3.13.0a0 | a4e456f | [1.30x faster](results/bm-20230622-3.13.0a0-a4e456f/bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f-vs-3.10.4.md) | [1.04x faster](results/bm-20230622-3.13.0a0-a4e456f/bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f-vs-3.11.0.md) | [1.01x slower](results/bm-20230622-3.13.0a0-a4e456f/bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f-vs-base.md) |
| [2023-06-21](results/bm-20230621-3.13.0a0-121fbad) | gvanrossum | optim_exec | 3.13.0a0 | 121fbad | [1.29x faster](results/bm-20230621-3.13.0a0-121fbad/bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad-vs-3.10.4.md) | [1.04x faster](results/bm-20230621-3.13.0a0-121fbad/bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad-vs-3.11.0.md) | [1.01x slower](results/bm-20230621-3.13.0a0-121fbad/bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad-vs-base.md) |
| [2023-06-21](results/bm-20230621-3.13.0a0-f9fa498) | brandtbucher | to_bool | 3.13.0a0 | f9fa498 | [1.30x faster](results/bm-20230621-3.13.0a0-f9fa498/bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498-vs-3.10.4.md) | [1.04x faster](results/bm-20230621-3.13.0a0-f9fa498/bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498-vs-3.11.0.md) | [1.00x faster](results/bm-20230621-3.13.0a0-f9fa498/bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498-vs-base.md) |
| [2023-06-20](results/bm-20230620-3.13.0a0-4d140e5) | python | 4d140e5e06 | 3.13.0a0 | 4d140e5 | [1.29x faster](results/bm-20230620-3.13.0a0-4d140e5/bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5-vs-3.10.4.md) | [1.04x faster](results/bm-20230620-3.13.0a0-4d140e5/bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5-vs-3.11.0.md) |  |
| [2023-06-20](results/bm-20230620-3.13.0a0-757b1cc) | brandtbucher | to_bool | 3.13.0a0 | 757b1cc | [1.29x faster](results/bm-20230620-3.13.0a0-757b1cc/bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc-vs-3.10.4.md) | [1.03x faster](results/bm-20230620-3.13.0a0-757b1cc/bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc-vs-3.11.0.md) | [1.00x slower](results/bm-20230620-3.13.0a0-757b1cc/bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc-vs-base.md) |
| [2023-06-20](results/bm-20230620-3.13.0a0-bab539b) | brandtbucher | to_bool | 3.13.0a0 | bab539b | [1.29x faster](results/bm-20230620-3.13.0a0-bab539b/bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b-vs-3.10.4.md) | [1.04x faster](results/bm-20230620-3.13.0a0-bab539b/bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b-vs-3.11.0.md) | [1.00x slower](results/bm-20230620-3.13.0a0-bab539b/bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b-vs-base.md) |
| [2023-06-20](results/bm-20230620-3.13.0a0-a0bd53a) | brandtbucher | to_bool | 3.13.0a0 | a0bd53a | [1.29x faster](results/bm-20230620-3.13.0a0-a0bd53a/bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a-vs-3.10.4.md) | [1.04x faster](results/bm-20230620-3.13.0a0-a0bd53a/bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a-vs-3.11.0.md) | [1.00x slower](results/bm-20230620-3.13.0a0-a0bd53a/bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a-vs-base.md) |
| [2023-06-19](results/bm-20230619-3.13.0a0-7f97c8e) | python | 7f97c8e367 | 3.13.0a0 | 7f97c8e | [1.30x faster](results/bm-20230619-3.13.0a0-7f97c8e/bm-20230619-linux-x86_64-python-7f97c8e367869e2aebe9-3.13.0a0-7f97c8e-vs-3.10.4.md) | [1.04x faster](results/bm-20230619-3.13.0a0-7f97c8e/bm-20230619-linux-x86_64-python-7f97c8e367869e2aebe9-3.13.0a0-7f97c8e-vs-3.11.0.md) |  |
| [2023-06-19](results/bm-20230619-3.13.0a0-1858db7) | python | 1858db7cbd | 3.13.0a0 | 1858db7 | [1.30x faster](results/bm-20230619-3.13.0a0-1858db7/bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7-vs-3.10.4.md) | [1.04x faster](results/bm-20230619-3.13.0a0-1858db7/bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7-vs-3.11.0.md) |  |
| [2023-06-19](results/bm-20230619-3.13.0a0-6b23e0f) | gvanrossum | optim_exec | 3.13.0a0 | 6b23e0f | [1.30x faster](results/bm-20230619-3.13.0a0-6b23e0f/bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f-vs-3.10.4.md) | [1.04x faster](results/bm-20230619-3.13.0a0-6b23e0f/bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f-vs-3.11.0.md) | [1.00x slower](results/bm-20230619-3.13.0a0-6b23e0f/bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f-vs-base.md) |
| [2023-06-18](results/bm-20230618-3.13.0a0-dba7217) | python | dba7217511 | 3.13.0a0 | dba7217 | [1.30x faster](results/bm-20230618-3.13.0a0-dba7217/bm-20230618-linux-x86_64-python-dba72175116373c1d15e-3.13.0a0-dba7217-vs-3.10.4.md) | [1.04x faster](results/bm-20230618-3.13.0a0-dba7217/bm-20230618-linux-x86_64-python-dba72175116373c1d15e-3.13.0a0-dba7217-vs-3.11.0.md) |  |
| [2023-06-18](results/bm-20230618-3.12.0b2%2B-6baddd9) | python | 6baddd9fb2 | 3.12.0b2+ | 6baddd9 | [1.28x faster](results/bm-20230618-3.12.0b2%2B-6baddd9/bm-20230618-linux-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2%2B-6baddd9-vs-3.10.4.md) | [1.03x faster](results/bm-20230618-3.12.0b2%2B-6baddd9/bm-20230618-linux-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2%2B-6baddd9-vs-3.11.0.md) |  |
| [2023-06-19](results/bm-20230619-3.12.0b3-f992a60) | python | v3.12.0b3 | 3.12.0b3 | f992a60 | [1.28x faster](results/bm-20230619-3.12.0b3-f992a60/bm-20230619-linux-x86_64-python-v3.12.0b3-3.12.0b3-f992a60-vs-3.10.4.md) | [1.03x faster](results/bm-20230619-3.12.0b3-f992a60/bm-20230619-linux-x86_64-python-v3.12.0b3-3.12.0b3-f992a60-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.25x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.24x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## linux x86_64 (pythonperf2)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-06-20](results/bm-20230620-3.13.0a0-155577d) | python | 155577de1b | 3.13.0a0 | 155577d | [1.29x faster](results/bm-20230620-3.13.0a0-155577d/bm-20230620-pythonperf2-x86_64-python-155577de1b6a7f4404b2-3.13.0a0-155577d-vs-3.10.4.md) | [1.06x faster](results/bm-20230620-3.13.0a0-155577d/bm-20230620-pythonperf2-x86_64-python-155577de1b6a7f4404b2-3.13.0a0-155577d-vs-3.11.0.md) |  |
| [2023-06-18](results/bm-20230618-3.13.0a0-1df353e) | faster-cpython | specialize | 3.13.0a0 | 1df353e | [1.29x faster](results/bm-20230618-3.13.0a0-1df353e/bm-20230618-pythonperf2-x86_64-faster%252dcpython-specialize_calls_to_-3.13.0a0-1df353e-vs-3.10.4.md) | [1.06x faster](results/bm-20230618-3.13.0a0-1df353e/bm-20230618-pythonperf2-x86_64-faster%252dcpython-specialize_calls_to_-3.13.0a0-1df353e-vs-3.11.0.md) | [1.00x slower](results/bm-20230618-3.13.0a0-1df353e/bm-20230618-pythonperf2-x86_64-faster%252dcpython-specialize_calls_to_-3.13.0a0-1df353e-vs-base.md) |
| [2023-06-18](results/bm-20230618-3.13.0a0-dba7217) | python | dba7217511 | 3.13.0a0 | dba7217 | [1.29x faster](results/bm-20230618-3.13.0a0-dba7217/bm-20230618-pythonperf2-x86_64-python-dba72175116373c1d15e-3.13.0a0-dba7217-vs-3.10.4.md) | [1.06x faster](results/bm-20230618-3.13.0a0-dba7217/bm-20230618-pythonperf2-x86_64-python-dba72175116373c1d15e-3.13.0a0-dba7217-vs-3.11.0.md) |  |
| [2023-06-18](results/bm-20230618-3.12.0b2%2B-6baddd9) | python | 6baddd9fb2 | 3.12.0b2+ | 6baddd9 | [1.28x faster](results/bm-20230618-3.12.0b2%2B-6baddd9/bm-20230618-pythonperf2-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2%2B-6baddd9-vs-3.10.4.md) | [1.05x faster](results/bm-20230618-3.12.0b2%2B-6baddd9/bm-20230618-pythonperf2-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2%2B-6baddd9-vs-3.11.0.md) |  |
| [2023-06-19](results/bm-20230619-3.12.0b3-f992a60) | python | v3.12.0b3 | 3.12.0b3 | f992a60 | [1.30x faster](results/bm-20230619-3.12.0b3-f992a60/bm-20230619-pythonperf2-x86_64-python-v3.12.0b3-3.12.0b3-f992a60-vs-3.10.4.md) | [1.07x faster](results/bm-20230619-3.12.0b3-f992a60/bm-20230619-pythonperf2-x86_64-python-v3.12.0b3-3.12.0b3-f992a60-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.21x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.21x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## windows amd64 (pythonperf1)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-06-18](results/bm-20230618-3.13.0a0-dba7217) | python | dba7217511 | 3.13.0a0 | dba7217 | [1.16x faster](results/bm-20230618-3.13.0a0-dba7217/bm-20230618-pythonperf1-amd64-python-dba72175116373c1d15e-3.13.0a0-dba7217-vs-3.10.4.md) | [1.04x faster](results/bm-20230618-3.13.0a0-dba7217/bm-20230618-pythonperf1-amd64-python-dba72175116373c1d15e-3.13.0a0-dba7217-vs-3.11.0.md) |  |
| [2023-06-12](results/bm-20230612-3.13.0a0-58f0bda) | python | main | 3.13.0a0 | 58f0bda | [1.13x faster](results/bm-20230612-3.13.0a0-58f0bda/bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda-vs-3.10.4.md) | [1.01x faster](results/bm-20230612-3.13.0a0-58f0bda/bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda-vs-3.11.0.md) |  |
| [2023-06-03](results/bm-20230603-3.13.0a0-eaff9c3) | python | main | 3.13.0a0 | eaff9c3 | [1.16x faster](results/bm-20230603-3.13.0a0-eaff9c3/bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3-vs-3.10.4.md) | [1.04x faster](results/bm-20230603-3.13.0a0-eaff9c3/bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3-vs-3.11.0.md) |  |
| [2023-06-18](results/bm-20230618-3.12.0b2%2B-6baddd9) | python | 6baddd9fb2 | 3.12.0b2+ | 6baddd9 | [1.17x faster](results/bm-20230618-3.12.0b2%2B-6baddd9/bm-20230618-pythonperf1-amd64-python-6baddd9fb25e03040c1c-3.12.0b2%2B-6baddd9-vs-3.10.4.md) | [1.04x faster](results/bm-20230618-3.12.0b2%2B-6baddd9/bm-20230618-pythonperf1-amd64-python-6baddd9fb25e03040c1c-3.12.0b2%2B-6baddd9-vs-3.11.0.md) |  |
| [2023-06-19](results/bm-20230619-3.12.0b3-f992a60) | python | v3.12.0b3 | 3.12.0b3 | f992a60 | [1.17x faster](results/bm-20230619-3.12.0b3-f992a60/bm-20230619-pythonperf1-amd64-python-v3.12.0b3-3.12.0b3-f992a60-vs-3.10.4.md) | [1.05x faster](results/bm-20230619-3.12.0b3-f992a60/bm-20230619-pythonperf1-amd64-python-v3.12.0b3-3.12.0b3-f992a60-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.11x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.12x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## darwin arm64 (darwin)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-06-18](results/bm-20230618-3.13.0a0-dba7217) | python | dba7217511 | 3.13.0a0 | dba7217 | [1.22x faster](results/bm-20230618-3.13.0a0-dba7217/bm-20230618-darwin-arm64-python-dba72175116373c1d15e-3.13.0a0-dba7217-vs-3.10.4.md) | [1.01x faster](results/bm-20230618-3.13.0a0-dba7217/bm-20230618-darwin-arm64-python-dba72175116373c1d15e-3.13.0a0-dba7217-vs-3.11.0.md) |  |
| [2023-06-10](results/bm-20230610-3.13.0a0-3a314f7) | python | main | 3.13.0a0 | 3a314f7 | [1.23x faster](results/bm-20230610-3.13.0a0-3a314f7/bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7-vs-3.10.4.md) | [1.01x faster](results/bm-20230610-3.13.0a0-3a314f7/bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7-vs-3.11.0.md) |  |
| [2023-06-03](results/bm-20230603-3.13.0a0-eaff9c3) | python | main | 3.13.0a0 | eaff9c3 | [1.24x faster](results/bm-20230603-3.13.0a0-eaff9c3/bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3-vs-3.10.4.md) | [1.02x faster](results/bm-20230603-3.13.0a0-eaff9c3/bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3-vs-3.11.0.md) |  |
| [2023-06-18](results/bm-20230618-3.12.0b2%2B-6baddd9) | python | 6baddd9fb2 | 3.12.0b2+ | 6baddd9 | [1.24x faster](results/bm-20230618-3.12.0b2%2B-6baddd9/bm-20230618-darwin-arm64-python-6baddd9fb25e03040c1c-3.12.0b2%2B-6baddd9-vs-3.10.4.md) | [1.02x faster](results/bm-20230618-3.12.0b2%2B-6baddd9/bm-20230618-darwin-arm64-python-6baddd9fb25e03040c1c-3.12.0b2%2B-6baddd9-vs-3.11.0.md) |  |
| [2023-06-19](results/bm-20230619-3.12.0b3-f992a60) | python | v3.12.0b3 | 3.12.0b3 | f992a60 | [1.23x faster](results/bm-20230619-3.12.0b3-f992a60/bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60-vs-3.10.4.md) | [1.02x faster](results/bm-20230619-3.12.0b3-f992a60/bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60-vs-3.11.0.md) |  |
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

