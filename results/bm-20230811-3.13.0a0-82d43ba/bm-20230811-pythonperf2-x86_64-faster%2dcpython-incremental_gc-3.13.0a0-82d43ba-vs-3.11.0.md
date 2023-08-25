
# Results vs. 3.11.0

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 82d43ba
- commit date: 2023-08-11
- overall geometric mean: 1.01x faster
- HPT reliability: 70.65%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.78 sec: 1.03x faster                                                          |
| tornado_http   | 122 ms                                                       | 129 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 85.8 ms: 1.06x faster                                                           |
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                                            |
| float          | 74.2 ms                                                      | 116 ms: 1.56x slower                                                            |
| Geometric mean | (ref)                                                        | 1.15x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 151 ms: 1.04x faster                                                            |
| regex_effbot   | 3.50 ms                                                      | 3.37 ms: 1.04x faster                                                           |
| regex_v8       | 23.9 ms                                                      | 23.8 ms: 1.01x faster                                                           |
| regex_dna      | 227 ms                                                       | 236 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                           |
| unpickle_pure_python | 241 us                                                       | 218 us: 1.11x faster                                                            |
| json_loads           | 28.7 us                                                      | 26.0 us: 1.11x faster                                                           |
| pickle_pure_python   | 319 us                                                       | 315 us: 1.01x faster                                                            |
| pickle               | 9.64 us                                                      | 9.78 us: 1.01x slower                                                           |
| unpickle_list        | 4.53 us                                                      | 4.64 us: 1.02x slower                                                           |
| pickle_dict          | 30.8 us                                                      | 31.8 us: 1.03x slower                                                           |
| tomli_loads          | 2.26 sec                                                     | 2.38 sec: 1.05x slower                                                          |
| xml_etree_process    | 56.5 ms                                                      | 59.7 ms: 1.06x slower                                                           |
| pickle_list          | 3.83 us                                                      | 4.22 us: 1.10x slower                                                           |
| unpickle             | 13.4 us                                                      | 15.0 us: 1.12x slower                                                           |
| xml_etree_generate   | 80.5 ms                                                      | 96.4 ms: 1.20x slower                                                           |
| xml_etree_parse      | 158 ms                                                       | 543 ms: 3.44x slower                                                            |
| xml_etree_iterparse  | 104 ms                                                       | 515 ms: 4.94x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.23x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.8 ms: 1.10x slower                                                           |
| python_startup_no_site | 7.76 ms                                                      | 8.75 ms: 1.13x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.11x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 156 us: 3.36x faster                                                            |
| asyncio_tcp              | 753 ms                                                       | 369 ms: 2.04x faster                                                            |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.95x faster                                                          |
| async_tree_io            | 1.17 sec                                                     | 726 ms: 1.62x faster                                                            |
| generators               | 56.0 ms                                                      | 36.7 ms: 1.53x faster                                                           |
| async_tree_none          | 519 ms                                                       | 352 ms: 1.47x faster                                                            |
| async_tree_memoization   | 630 ms                                                       | 434 ms: 1.45x faster                                                            |
| json_dumps               | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                           |
| chaos                    | 80.9 ms                                                      | 61.7 ms: 1.31x faster                                                           |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 611 ms: 1.23x faster                                                            |
| coroutines               | 27.6 ms                                                      | 23.5 ms: 1.17x faster                                                           |
| crypto_pyaes             | 83.4 ms                                                      | 73.5 ms: 1.13x faster                                                           |
| raytrace                 | 317 ms                                                       | 280 ms: 1.13x faster                                                            |
| scimark_lu               | 115 ms                                                       | 101 ms: 1.13x faster                                                            |
| nqueens                  | 103 ms                                                       | 91.4 ms: 1.12x faster                                                           |
| comprehensions           | 24.6 us                                                      | 22.0 us: 1.12x faster                                                           |
| fannkuch                 | 429 ms                                                       | 387 ms: 1.11x faster                                                            |
| unpickle_pure_python     | 241 us                                                       | 218 us: 1.11x faster                                                            |
| json_loads               | 28.7 us                                                      | 26.0 us: 1.11x faster                                                           |
| json                     | 5.65 ms                                                      | 5.19 ms: 1.09x faster                                                           |
| logging_format           | 8.11 us                                                      | 7.48 us: 1.09x faster                                                           |
| hexiom                   | 7.13 ms                                                      | 6.58 ms: 1.08x faster                                                           |
| mako                     | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                                           |
| nbody                    | 90.7 ms                                                      | 85.8 ms: 1.06x faster                                                           |
| sqlglot_normalize        | 126 ms                                                       | 119 ms: 1.06x faster                                                            |
| mdp                      | 2.75 sec                                                     | 2.60 sec: 1.06x faster                                                          |
| deltablue                | 4.00 ms                                                      | 3.80 ms: 1.05x faster                                                           |
| deepcopy                 | 399 us                                                       | 380 us: 1.05x faster                                                            |
| deepcopy_memo            | 38.8 us                                                      | 37.0 us: 1.05x faster                                                           |
| logging_simple           | 7.19 us                                                      | 6.87 us: 1.05x faster                                                           |
| regex_compile            | 158 ms                                                       | 151 ms: 1.04x faster                                                            |
| bench_thread_pool        | 1.01 ms                                                      | 971 us: 1.04x faster                                                            |
| pycparser                | 1.32 sec                                                     | 1.27 sec: 1.04x faster                                                          |
| regex_effbot             | 3.50 ms                                                      | 3.37 ms: 1.04x faster                                                           |
| logging_silent           | 101 ns                                                       | 97.4 ns: 1.04x faster                                                           |
| sqlglot_parse            | 1.53 ms                                                      | 1.48 ms: 1.03x faster                                                           |
| meteor_contest           | 131 ms                                                       | 127 ms: 1.03x faster                                                            |
| docutils                 | 2.86 sec                                                     | 2.78 sec: 1.03x faster                                                          |
| richards_super           | 61.0 ms                                                      | 59.5 ms: 1.03x faster                                                           |
| deepcopy_reduce          | 3.51 us                                                      | 3.46 us: 1.02x faster                                                           |
| pickle_pure_python       | 319 us                                                       | 315 us: 1.01x faster                                                            |
| regex_v8                 | 23.9 ms                                                      | 23.8 ms: 1.01x faster                                                           |
| pprint_pformat           | 1.63 sec                                                     | 1.64 sec: 1.01x slower                                                          |
| pickle                   | 9.64 us                                                      | 9.78 us: 1.01x slower                                                           |
| sqlglot_transpile        | 1.92 ms                                                      | 1.95 ms: 1.02x slower                                                           |
| unpickle_list            | 4.53 us                                                      | 4.64 us: 1.02x slower                                                           |
| pprint_safe_repr         | 784 ms                                                       | 803 ms: 1.02x slower                                                            |
| pathlib                  | 19.1 ms                                                      | 19.6 ms: 1.03x slower                                                           |
| pidigits                 | 251 ms                                                       | 260 ms: 1.03x slower                                                            |
| pickle_dict              | 30.8 us                                                      | 31.8 us: 1.03x slower                                                           |
| regex_dna                | 227 ms                                                       | 236 ms: 1.04x slower                                                            |
| create_gc_cycles         | 1.61 ms                                                      | 1.67 ms: 1.04x slower                                                           |
| unpack_sequence          | 45.6 ns                                                      | 47.8 ns: 1.05x slower                                                           |
| tomli_loads              | 2.26 sec                                                     | 2.38 sec: 1.05x slower                                                          |
| xml_etree_process        | 56.5 ms                                                      | 59.7 ms: 1.06x slower                                                           |
| tornado_http             | 122 ms                                                       | 129 ms: 1.06x slower                                                            |
| go                       | 164 ms                                                       | 175 ms: 1.07x slower                                                            |
| sqlite_synth             | 2.50 us                                                      | 2.70 us: 1.08x slower                                                           |
| scimark_fft              | 285 ms                                                       | 308 ms: 1.08x slower                                                            |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.38 ms: 1.08x slower                                                           |
| python_startup           | 10.8 ms                                                      | 11.8 ms: 1.10x slower                                                           |
| richards                 | 48.3 ms                                                      | 53.0 ms: 1.10x slower                                                           |
| pickle_list              | 3.83 us                                                      | 4.22 us: 1.10x slower                                                           |
| bench_mp_pool            | 4.62 ms                                                      | 5.14 ms: 1.11x slower                                                           |
| unpickle                 | 13.4 us                                                      | 15.0 us: 1.12x slower                                                           |
| coverage                 | 84.8 ms                                                      | 95.1 ms: 1.12x slower                                                           |
| python_startup_no_site   | 7.76 ms                                                      | 8.75 ms: 1.13x slower                                                           |
| gc_traversal             | 3.85 ms                                                      | 4.37 ms: 1.14x slower                                                           |
| pyflate                  | 449 ms                                                       | 511 ms: 1.14x slower                                                            |
| telco                    | 6.86 ms                                                      | 8.16 ms: 1.19x slower                                                           |
| xml_etree_generate       | 80.5 ms                                                      | 96.4 ms: 1.20x slower                                                           |
| scimark_sor              | 111 ms                                                       | 142 ms: 1.28x slower                                                            |
| async_generators         | 316 ms                                                       | 405 ms: 1.28x slower                                                            |
| dask                     | 410 ms                                                       | 593 ms: 1.45x slower                                                            |
| float                    | 74.2 ms                                                      | 116 ms: 1.56x slower                                                            |
| xml_etree_parse          | 158 ms                                                       | 543 ms: 3.44x slower                                                            |
| xml_etree_iterparse      | 104 ms                                                       | 515 ms: 4.94x slower                                                            |
| Geometric mean           | (ref)                                                        | 1.01x faster                                                                    |

Benchmark hidden because not significant (5): scimark_monte_carlo, spectral_norm, sqlglot_optimize, dulwich_log, mypy2
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 70.65% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
