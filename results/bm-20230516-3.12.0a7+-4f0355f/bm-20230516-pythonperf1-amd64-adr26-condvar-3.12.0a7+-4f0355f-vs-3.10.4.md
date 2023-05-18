
# Results vs. 3.10.4

- fork: adr26
- ref: condvar
- machine: windows-amd64
- commit hash: 4f0355f
- commit date: 2023-05-16
- overall geometric mean: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 214 ms: 1.11x faster                                          |
| docutils       | 1.89 sec                                                    | 1.63 sec: 1.16x faster                                        |
| tornado_http   | 109 ms                                                      | 87.4 ms: 1.25x faster                                         |
| Geometric mean | (ref)                                                       | 1.17x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 55.2 ms: 1.09x faster                                         |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                          |
| nbody          | 69.3 ms                                                     | 72.7 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                       | 1.00x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 85.8 ms: 1.21x faster                                         |
| regex_dna      | 132 ms                                                      | 117 ms: 1.13x faster                                          |
| regex_v8       | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                         |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.06x faster                                         |
| Geometric mean | (ref)                                                       | 1.12x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.71 ms: 1.49x faster                                         |
| pickle_pure_python   | 257 us                                                      | 193 us: 1.33x faster                                          |
| unpickle_pure_python | 171 us                                                      | 136 us: 1.26x faster                                          |
| tomli_loads          | 1.62 sec                                                    | 1.39 sec: 1.17x faster                                        |
| xml_etree_process    | 43.4 ms                                                     | 38.9 ms: 1.12x faster                                         |
| xml_etree_parse      | 102 ms                                                      | 93.0 ms: 1.09x faster                                         |
| unpickle             | 9.17 us                                                     | 8.45 us: 1.09x faster                                         |
| json_loads           | 14.2 us                                                     | 13.6 us: 1.04x faster                                         |
| unpickle_list        | 2.81 us                                                     | 2.77 us: 1.02x faster                                         |
| xml_etree_generate   | 54.5 ms                                                     | 57.7 ms: 1.06x slower                                         |
| pickle_list          | 2.59 us                                                     | 2.83 us: 1.09x slower                                         |
| pickle               | 6.80 us                                                     | 7.44 us: 1.09x slower                                         |
| pickle_dict          | 16.9 us                                                     | 18.6 us: 1.10x slower                                         |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                  |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.2 ms: 1.04x faster                                         |
| python_startup_no_site | 15.5 ms                                                     | 16.3 ms: 1.05x slower                                         |
| Geometric mean         | (ref)                                                       | 1.00x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|-----------|:-----------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.87 ms: 1.28x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 99.4 us: 3.27x faster                                         |
| deltablue                | 4.17 ms                                                     | 2.17 ms: 1.93x faster                                         |
| richards_super           | 51.7 ms                                                     | 30.4 ms: 1.70x faster                                         |
| mypy2                    | 352 ms                                                      | 212 ms: 1.66x faster                                          |
| logging_silent           | 96.4 ns                                                     | 61.2 ns: 1.57x faster                                         |
| go                       | 136 ms                                                      | 87.6 ms: 1.55x faster                                         |
| richards                 | 41.2 ms                                                     | 27.0 ms: 1.52x faster                                         |
| sqlglot_parse            | 1.22 ms                                                     | 810 us: 1.50x faster                                          |
| async_tree_memoization   | 497 ms                                                      | 332 ms: 1.50x faster                                          |
| async_tree_none          | 420 ms                                                      | 281 ms: 1.50x faster                                          |
| json_dumps               | 8.50 ms                                                     | 5.71 ms: 1.49x faster                                         |
| asyncio_tcp              | 712 ms                                                      | 484 ms: 1.47x faster                                          |
| async_tree_io            | 1.07 sec                                                    | 728 ms: 1.46x faster                                          |
| scimark_lu               | 85.4 ms                                                     | 59.5 ms: 1.44x faster                                         |
| raytrace                 | 271 ms                                                      | 189 ms: 1.43x faster                                          |
| sqlglot_transpile        | 1.46 ms                                                     | 1.02 ms: 1.43x faster                                         |
| chaos                    | 58.9 ms                                                     | 42.8 ms: 1.38x faster                                         |
| generators               | 31.6 ms                                                     | 23.1 ms: 1.37x faster                                         |
| hexiom                   | 5.52 ms                                                     | 4.05 ms: 1.36x faster                                         |
| crypto_pyaes             | 62.3 ms                                                     | 46.7 ms: 1.33x faster                                         |
| pickle_pure_python       | 257 us                                                      | 193 us: 1.33x faster                                          |
| scimark_sor              | 105 ms                                                      | 80.2 ms: 1.31x faster                                         |
| pyflate                  | 387 ms                                                      | 297 ms: 1.30x faster                                          |
| mako                     | 8.80 ms                                                     | 6.87 ms: 1.28x faster                                         |
| scimark_monte_carlo      | 55.9 ms                                                     | 43.8 ms: 1.27x faster                                         |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 481 ms: 1.27x faster                                          |
| unpickle_pure_python     | 171 us                                                      | 136 us: 1.26x faster                                          |
| pycparser                | 868 ms                                                      | 689 ms: 1.26x faster                                          |
| tornado_http             | 109 ms                                                      | 87.4 ms: 1.25x faster                                         |
| spectral_norm            | 78.0 ms                                                     | 64.3 ms: 1.21x faster                                         |
| regex_compile            | 103 ms                                                      | 85.8 ms: 1.21x faster                                         |
| deepcopy_memo            | 28.5 us                                                     | 23.9 us: 1.19x faster                                         |
| mdp                      | 1.71 sec                                                    | 1.44 sec: 1.19x faster                                        |
| tomli_loads              | 1.62 sec                                                    | 1.39 sec: 1.17x faster                                        |
| docutils                 | 1.89 sec                                                    | 1.63 sec: 1.16x faster                                        |
| bench_thread_pool        | 946 us                                                      | 814 us: 1.16x faster                                          |
| pprint_pformat           | 1.21 sec                                                    | 1.05 sec: 1.15x faster                                        |
| dulwich_log              | 47.6 ms                                                     | 41.6 ms: 1.14x faster                                         |
| aiohttp                  | 1.01 ms                                                     | 886 us: 1.14x faster                                          |
| pprint_safe_repr         | 589 ms                                                      | 519 ms: 1.13x faster                                          |
| sqlglot_optimize         | 39.0 ms                                                     | 34.4 ms: 1.13x faster                                         |
| regex_dna                | 132 ms                                                      | 117 ms: 1.13x faster                                          |
| comprehensions           | 16.0 us                                                     | 14.2 us: 1.12x faster                                         |
| xml_etree_process        | 43.4 ms                                                     | 38.9 ms: 1.12x faster                                         |
| nqueens                  | 67.0 ms                                                     | 60.1 ms: 1.12x faster                                         |
| create_gc_cycles         | 782 us                                                      | 704 us: 1.11x faster                                          |
| 2to3                     | 237 ms                                                      | 214 ms: 1.11x faster                                          |
| fannkuch                 | 258 ms                                                      | 233 ms: 1.11x faster                                          |
| coroutines               | 15.9 ms                                                     | 14.4 ms: 1.10x faster                                         |
| sqlglot_normalize        | 202 ms                                                      | 184 ms: 1.10x faster                                          |
| xml_etree_parse          | 102 ms                                                      | 93.0 ms: 1.09x faster                                         |
| regex_v8                 | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                         |
| sqlite_synth             | 1.84 us                                                     | 1.69 us: 1.09x faster                                         |
| float                    | 60.2 ms                                                     | 55.2 ms: 1.09x faster                                         |
| unpickle                 | 9.17 us                                                     | 8.45 us: 1.09x faster                                         |
| scimark_fft              | 193 ms                                                      | 178 ms: 1.08x faster                                          |
| deepcopy                 | 255 us                                                      | 241 us: 1.06x faster                                          |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.06x faster                                         |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.54 ms: 1.05x faster                                         |
| json_loads               | 14.2 us                                                     | 13.6 us: 1.04x faster                                         |
| python_startup           | 20.0 ms                                                     | 19.2 ms: 1.04x faster                                         |
| unpack_sequence          | 37.8 ns                                                     | 36.5 ns: 1.04x faster                                         |
| unpickle_list            | 2.81 us                                                     | 2.77 us: 1.02x faster                                         |
| async_generators         | 224 ms                                                      | 229 ms: 1.02x slower                                          |
| meteor_contest           | 72.5 ms                                                     | 75.2 ms: 1.04x slower                                         |
| logging_format           | 6.66 us                                                     | 6.92 us: 1.04x slower                                         |
| pidigits                 | 145 ms                                                      | 151 ms: 1.04x slower                                          |
| logging_simple           | 6.20 us                                                     | 6.49 us: 1.05x slower                                         |
| python_startup_no_site   | 15.5 ms                                                     | 16.3 ms: 1.05x slower                                         |
| nbody                    | 69.3 ms                                                     | 72.7 ms: 1.05x slower                                         |
| xml_etree_generate       | 54.5 ms                                                     | 57.7 ms: 1.06x slower                                         |
| pathlib                  | 77.4 ms                                                     | 82.9 ms: 1.07x slower                                         |
| gc_traversal             | 1.34 ms                                                     | 1.46 ms: 1.09x slower                                         |
| pickle_list              | 2.59 us                                                     | 2.83 us: 1.09x slower                                         |
| pickle                   | 6.80 us                                                     | 7.44 us: 1.09x slower                                         |
| telco                    | 3.78 ms                                                     | 4.16 ms: 1.10x slower                                         |
| pickle_dict              | 16.9 us                                                     | 18.6 us: 1.10x slower                                         |
| bench_mp_pool            | 60.7 ms                                                     | 68.1 ms: 1.12x slower                                         |
| dask                     | 305 ms                                                      | 371 ms: 1.22x slower                                          |
| coverage                 | 40.0 ms                                                     | 50.9 ms: 1.27x slower                                         |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                  |

Benchmark hidden because not significant (4): asyncio_tcp_ssl, deepcopy_reduce, json, xml_etree_iterparse
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
