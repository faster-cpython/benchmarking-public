# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](https://github.com/faster-cpython/benchmarking/actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

<!-- START table -->
## linux x86_64 (linux)
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-04-06](results/bm-20230406-3.12.0a7%2B-affedee) | python | affedee8bf | 3.12.0a7+ | affedee | [1.31x faster](results/bm-20230406-3.12.0a7%2B-affedee/bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7%2B-affedee-vs-3.10.4.md) | [1.04x faster](results/bm-20230406-3.12.0a7%2B-affedee/bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7%2B-affedee-vs-3.11.0.md) |  |
| [2023-04-06](results/bm-20230406-3.12.0a7%2B-47a7094) | ericsnowcurrently | tstate_cur | 3.12.0a7+ | 47a7094 | [1.31x faster](results/bm-20230406-3.12.0a7%2B-47a7094/bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-47a7094-vs-3.10.4.md) | [1.04x faster](results/bm-20230406-3.12.0a7%2B-47a7094/bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-47a7094-vs-3.11.0.md) | [1.00x faster](results/bm-20230406-3.12.0a7%2B-47a7094/bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-47a7094-vs-base.md) |
| [2023-04-06](results/bm-20230406-3.12.0a7%2B-52bc2e7) | python | 52bc2e7b9d | 3.12.0a7+ | 52bc2e7 | [1.31x faster](results/bm-20230406-3.12.0a7%2B-52bc2e7/bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7-vs-3.10.4.md) | [1.04x faster](results/bm-20230406-3.12.0a7%2B-52bc2e7/bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7-vs-3.11.0.md) |  |
| [2023-04-06](results/bm-20230406-3.12.0a7%2B-97543c5) | brandtbucher | fold_slice | 3.12.0a7+ | 97543c5 | [1.30x faster](results/bm-20230406-3.12.0a7%2B-97543c5/bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7%2B-97543c5-vs-3.10.4.md) | [1.04x faster](results/bm-20230406-3.12.0a7%2B-97543c5/bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7%2B-97543c5-vs-3.11.0.md) | [1.00x slower](results/bm-20230406-3.12.0a7%2B-97543c5/bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7%2B-97543c5-vs-base.md) |
| [2023-04-06](results/bm-20230406-3.12.0a7%2B-39619f9) | brandtbucher | fold_slice | 3.12.0a7+ | 39619f9 | [1.30x faster](results/bm-20230406-3.12.0a7%2B-39619f9/bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7%2B-39619f9-vs-3.10.4.md) | [1.04x faster](results/bm-20230406-3.12.0a7%2B-39619f9/bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7%2B-39619f9-vs-3.11.0.md) | [1.00x slower](results/bm-20230406-3.12.0a7%2B-39619f9/bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7%2B-39619f9-vs-base.md) |
| [2023-04-04](results/bm-20230404-3.12.0a7%2B-299527e) | ericsnowcurrently | per_interp | 3.12.0a7+ | 299527e | [1.28x faster](results/bm-20230404-3.12.0a7%2B-299527e/bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7%2B-299527e-vs-3.10.4.md) | [1.02x faster](results/bm-20230404-3.12.0a7%2B-299527e/bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7%2B-299527e-vs-3.11.0.md) | [1.01x slower](results/bm-20230404-3.12.0a7%2B-299527e/bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7%2B-299527e-vs-base.md) |
| [2023-04-04](results/bm-20230404-3.12.0a7%2B-f513d5c) | python | f513d5c806 | 3.12.0a7+ | f513d5c | [1.30x faster](results/bm-20230404-3.12.0a7%2B-f513d5c/bm-20230404-linux-x86_64-python-f513d5c80672c76acbda-3.12.0a7%2B-f513d5c-vs-3.10.4.md) | [1.04x faster](results/bm-20230404-3.12.0a7%2B-f513d5c/bm-20230404-linux-x86_64-python-f513d5c80672c76acbda-3.12.0a7%2B-f513d5c-vs-3.11.0.md) |  |
| [2023-04-06](results/bm-20230406-3.12.0a6%2B-030016a) | eduardo-elizondo | immortal_r | 3.12.0a6+ | 030016a | [1.22x faster](results/bm-20230406-3.12.0a6%2B-030016a/bm-20230406-linux-x86_64-eduardo%252delizondo-immortal_references-3.12.0a6%2B-030016a-vs-3.10.4.md) | [1.03x slower](results/bm-20230406-3.12.0a6%2B-030016a/bm-20230406-linux-x86_64-eduardo%252delizondo-immortal_references-3.12.0a6%2B-030016a-vs-3.11.0.md) | [1.06x slower](results/bm-20230406-3.12.0a6%2B-030016a/bm-20230406-linux-x86_64-eduardo%252delizondo-immortal_references-3.12.0a6%2B-030016a-vs-base.md) |
| [2023-04-04](results/bm-20230404-3.12.0a6%2B-d02b607) | brandtbucher | shrink_cal | 3.12.0a6+ | d02b607 | [1.29x faster](results/bm-20230404-3.12.0a6%2B-d02b607/bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6%2B-d02b607-vs-3.10.4.md) | [1.03x faster](results/bm-20230404-3.12.0a6%2B-d02b607/bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6%2B-d02b607-vs-3.11.0.md) | [1.00x slower](results/bm-20230404-3.12.0a6%2B-d02b607/bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6%2B-d02b607-vs-base.md) |
| [2023-04-02](results/bm-20230402-3.12.0a6%2B-385b5d6) | python | 385b5d6e09 | 3.12.0a6+ | 385b5d6 | [1.30x faster](results/bm-20230402-3.12.0a6%2B-385b5d6/bm-20230402-linux-x86_64-python-385b5d6e091da454c3e0-3.12.0a6%2B-385b5d6-vs-3.10.4.md) | [1.03x faster](results/bm-20230402-3.12.0a6%2B-385b5d6/bm-20230402-linux-x86_64-python-385b5d6e091da454c3e0-3.12.0a6%2B-385b5d6-vs-3.11.0.md) |  |
| [2023-04-01](results/bm-20230401-3.12.0a6%2B-848bdbe) | python | 848bdbe166 | 3.12.0a6+ | 848bdbe | [1.29x faster](results/bm-20230401-3.12.0a6%2B-848bdbe/bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6%2B-848bdbe-vs-3.10.4.md) | [1.03x faster](results/bm-20230401-3.12.0a6%2B-848bdbe/bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6%2B-848bdbe-vs-3.11.0.md) |  |
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
| [2023-04-06](results/bm-20230406-3.12.0a6%2B-030016a) | eduardo-elizondo | immortal_r | 3.12.0a6+ | 030016a | [1.02x faster](results/bm-20230406-3.12.0a6%2B-030016a/bm-20230406-pythonperf1-amd64-eduardo%252delizondo-immortal_references-3.12.0a6%2B-030016a-vs-3.10.4.md) | [1.09x slower](results/bm-20230406-3.12.0a6%2B-030016a/bm-20230406-pythonperf1-amd64-eduardo%252delizondo-immortal_references-3.12.0a6%2B-030016a-vs-3.11.0.md) | [1.20x slower](results/bm-20230406-3.12.0a6%2B-030016a/bm-20230406-pythonperf1-amd64-eduardo%252delizondo-immortal_references-3.12.0a6%2B-030016a-vs-base.md) |
| [2023-04-02](results/bm-20230402-3.12.0a6%2B-385b5d6) | python | 385b5d6e09 | 3.12.0a6+ | 385b5d6 | [1.22x faster](results/bm-20230402-3.12.0a6%2B-385b5d6/bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6%2B-385b5d6-vs-3.10.4.md) | [1.10x faster](results/bm-20230402-3.12.0a6%2B-385b5d6/bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6%2B-385b5d6-vs-3.11.0.md) |  |
| [2023-04-01](results/bm-20230401-3.12.0a6%2B-06249ec) | python | main | 3.12.0a6+ | 06249ec | [1.19x faster](results/bm-20230401-3.12.0a6%2B-06249ec/bm-20230401-pythonperf1-amd64-python-main-3.12.0a6%2B-06249ec-vs-3.10.4.md) | [1.07x faster](results/bm-20230401-3.12.0a6%2B-06249ec/bm-20230401-pythonperf1-amd64-python-main-3.12.0a6%2B-06249ec-vs-3.11.0.md) |  |
| [2023-03-06](results/bm-20230306-3.12.0a5%2B-f533f21) | python | f533f216e6 | 3.12.0a5+ | f533f21 | [1.17x faster](results/bm-20230306-3.12.0a5%2B-f533f21/bm-20230306-pythonperf1-amd64-python-f533f216e6aaba3f3663-3.12.0a5%2B-f533f21-vs-3.10.4.md) | [1.06x faster](results/bm-20230306-3.12.0a5%2B-f533f21/bm-20230306-pythonperf1-amd64-python-f533f216e6aaba3f3663-3.12.0a5%2B-f533f21-vs-3.11.0.md) |  |
| [2023-02-26](results/bm-20230226-3.12.0a5%2B-f3cb15c) | python | f3cb15c88a | 3.12.0a5+ | f3cb15c | [1.21x faster](results/bm-20230226-3.12.0a5%2B-f3cb15c/bm-20230226-pythonperf1-amd64-python-f3cb15c88afa2e87067d-3.12.0a5%2B-f3cb15c-vs-3.10.4.md) | [1.09x faster](results/bm-20230226-3.12.0a5%2B-f3cb15c/bm-20230226-pythonperf1-amd64-python-f3cb15c88afa2e87067d-3.12.0a5%2B-f3cb15c-vs-3.11.0.md) |  |
| [2023-02-19](results/bm-20230219-3.12.0a5%2B-b1b375e) | python | b1b375e267 | 3.12.0a5+ | b1b375e | [1.21x faster](results/bm-20230219-3.12.0a5%2B-b1b375e/bm-20230219-pythonperf1-amd64-python-b1b375e2670a58fc37cb-3.12.0a5%2B-b1b375e-vs-3.10.4.md) | [1.09x faster](results/bm-20230219-3.12.0a5%2B-b1b375e/bm-20230219-pythonperf1-amd64-python-b1b375e2670a58fc37cb-3.12.0a5%2B-b1b375e-vs-3.11.0.md) |  |
| [2023-02-13](results/bm-20230213-3.12.0a5%2B-a1f08f5) | python | a1f08f5f19 | 3.12.0a5+ | a1f08f5 | [1.21x faster](results/bm-20230213-3.12.0a5%2B-a1f08f5/bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5-vs-3.10.4.md) | [1.09x faster](results/bm-20230213-3.12.0a5%2B-a1f08f5/bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5-vs-3.11.0.md) |  |
| [2023-02-05](results/bm-20230205-3.12.0a4%2B-ef7c2bf) | python | ef7c2bfcf1 | 3.12.0a4+ | ef7c2bf | [1.20x faster](results/bm-20230205-3.12.0a4%2B-ef7c2bf/bm-20230205-pythonperf1-amd64-python-ef7c2bfcf1fd618438f9-3.12.0a4%2B-ef7c2bf-vs-3.10.4.md) | [1.09x faster](results/bm-20230205-3.12.0a4%2B-ef7c2bf/bm-20230205-pythonperf1-amd64-python-ef7c2bfcf1fd618438f9-3.12.0a4%2B-ef7c2bf-vs-3.11.0.md) |  |
| [2023-01-29](results/bm-20230129-3.12.0a4%2B-c4170c3) | python | c4170c36b0 | 3.12.0a4+ | c4170c3 | [1.21x faster](results/bm-20230129-3.12.0a4%2B-c4170c3/bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3-vs-3.10.4.md) | [1.10x faster](results/bm-20230129-3.12.0a4%2B-c4170c3/bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3-vs-3.11.0.md) |  |
| [2023-01-22](results/bm-20230122-3.12.0a4%2B-d717be0) | python | d717be04dc | 3.12.0a4+ | d717be0 | [1.21x faster](results/bm-20230122-3.12.0a4%2B-d717be0/bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0-vs-3.10.4.md) | [1.09x faster](results/bm-20230122-3.12.0a4%2B-d717be0/bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0-vs-3.11.0.md) |  |
| [2023-01-16](results/bm-20230116-3.12.0a4%2B-7b14c2e) | python | 7b14c2ef19 | 3.12.0a4+ | 7b14c2e | [1.22x faster](results/bm-20230116-3.12.0a4%2B-7b14c2e/bm-20230116-pythonperf1-amd64-python-7b14c2ef194b6eed7967-3.12.0a4%2B-7b14c2e-vs-3.10.4.md) | [1.10x faster](results/bm-20230116-3.12.0a4%2B-7b14c2e/bm-20230116-pythonperf1-amd64-python-7b14c2ef194b6eed7967-3.12.0a4%2B-7b14c2e-vs-3.11.0.md) |  |
| [2023-01-08](results/bm-20230108-3.12.0a3%2B-e47b139) | python | e47b13934b | 3.12.0a3+ | e47b139 | [1.21x faster](results/bm-20230108-3.12.0a3%2B-e47b139/bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.10.4.md) | [1.09x faster](results/bm-20230108-3.12.0a3%2B-e47b139/bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3%2B-e47b139-vs-3.11.0.md) |  |
| [2023-01-01](results/bm-20230101-3.12.0a3%2B-edfbf56) | python | edfbf56f4c | 3.12.0a3+ | edfbf56 | [1.17x faster](results/bm-20230101-3.12.0a3%2B-edfbf56/bm-20230101-pythonperf1-amd64-python-edfbf56f4ca6588dfd20-3.12.0a3%2B-edfbf56-vs-3.10.4.md) | [1.06x faster](results/bm-20230101-3.12.0a3%2B-edfbf56/bm-20230101-pythonperf1-amd64-python-edfbf56f4ca6588dfd20-3.12.0a3%2B-edfbf56-vs-3.11.0.md) |  |
| [2022-12-26](results/bm-20221226-3.12.0a3%2B-ad3c99e) | python | ad3c99e521 | 3.12.0a3+ | ad3c99e | [1.16x faster](results/bm-20221226-3.12.0a3%2B-ad3c99e/bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e-vs-3.10.4.md) | [1.05x faster](results/bm-20221226-3.12.0a3%2B-ad3c99e/bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e-vs-3.11.0.md) |  |
| [2022-12-19](results/bm-20221219-3.12.0a3%2B-702a5bc) | python | 702a5bc463 | 3.12.0a3+ | 702a5bc | [1.17x faster](results/bm-20221219-3.12.0a3%2B-702a5bc/bm-20221219-pythonperf1-amd64-python-702a5bc4637c82dc011e-3.12.0a3%2B-702a5bc-vs-3.10.4.md) | [1.06x faster](results/bm-20221219-3.12.0a3%2B-702a5bc/bm-20221219-pythonperf1-amd64-python-702a5bc4637c82dc011e-3.12.0a3%2B-702a5bc-vs-3.11.0.md) |  |
| [2022-12-11](results/bm-20221211-3.12.0a3%2B-70be5e4) | python | 70be5e42f6 | 3.12.0a3+ | 70be5e4 | [1.17x faster](results/bm-20221211-3.12.0a3%2B-70be5e4/bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.10.4.md) | [1.06x faster](results/bm-20221211-3.12.0a3%2B-70be5e4/bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.11.0.md) |  |
| [2022-12-05](results/bm-20221205-3.12.0a2%2B-e3a3863) | python | e3a3863cb9 | 3.12.0a2+ | e3a3863 | [1.19x faster](results/bm-20221205-3.12.0a2%2B-e3a3863/bm-20221205-pythonperf1-amd64-python-e3a3863cb9561705d3dd-3.12.0a2%2B-e3a3863-vs-3.10.4.md) | [1.07x faster](results/bm-20221205-3.12.0a2%2B-e3a3863/bm-20221205-pythonperf1-amd64-python-e3a3863cb9561705d3dd-3.12.0a2%2B-e3a3863-vs-3.11.0.md) |  |
| [2022-11-28](results/bm-20221128-3.12.0a2%2B-594de16) | python | 594de165bf | 3.12.0a2+ | 594de16 | [1.21x faster](results/bm-20221128-3.12.0a2%2B-594de16/bm-20221128-pythonperf1-amd64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.10.4.md) | [1.09x faster](results/bm-20221128-3.12.0a2%2B-594de16/bm-20221128-pythonperf1-amd64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.11.0.md) |  |
| [2022-11-21](results/bm-20221121-3.12.0a2%2B-cdde29d) | python | cdde29dde9 | 3.12.0a2+ | cdde29d | [1.19x faster](results/bm-20221121-3.12.0a2%2B-cdde29d/bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.10.4.md) | [1.08x faster](results/bm-20221121-3.12.0a2%2B-cdde29d/bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.11.0.md) |  |
| [2022-11-10](results/bm-20221110-3.12.0a1%2B-d8f239d) | python | d8f239d86e | 3.12.0a1+ | d8f239d | [1.14x faster](results/bm-20221110-3.12.0a1%2B-d8f239d/bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1%2B-d8f239d-vs-3.10.4.md) | [1.03x faster](results/bm-20221110-3.12.0a1%2B-d8f239d/bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1%2B-d8f239d-vs-3.11.0.md) |  |
| [2022-11-10](results/bm-20221110-3.12.0a1%2B-f883b7f) | python | f883b7f8ee | 3.12.0a1+ | f883b7f | [1.14x faster](results/bm-20221110-3.12.0a1%2B-f883b7f/bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1%2B-f883b7f-vs-3.10.4.md) | [1.03x faster](results/bm-20221110-3.12.0a1%2B-f883b7f/bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1%2B-f883b7f-vs-3.11.0.md) |  |
| [2022-11-09](results/bm-20221109-3.12.0a1%2B-87f5180) | python | 87f5180cd7 | 3.12.0a1+ | 87f5180 | [1.14x faster](results/bm-20221109-3.12.0a1%2B-87f5180/bm-20221109-pythonperf1-amd64-python-87f5180cd79617223ac5-3.12.0a1%2B-87f5180-vs-3.10.4.md) | [1.03x faster](results/bm-20221109-3.12.0a1%2B-87f5180/bm-20221109-pythonperf1-amd64-python-87f5180cd79617223ac5-3.12.0a1%2B-87f5180-vs-3.11.0.md) |  |
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

