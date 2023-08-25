
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 0e5eee0
- commit date: 2023-08-20
- overall geometric mean: 1.07x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-pythonperf2-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 286 ms: 1.00x faster                                          |
| docutils       | 2.86 sec                                                     | 2.90 sec: 1.02x slower                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-pythonperf2-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 87.5 ms: 1.04x faster                                         |
| pidigits       | 251 ms                                                       | 260 ms: 1.04x slower                                          |
| float          | 74.2 ms                                                      | 78.5 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-pythonperf2-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 144 ms: 1.09x faster                                          |
| regex_dna      | 227 ms                                                       | 242 ms: 1.07x slower                                          |
| Geometric mean | (ref)                                                        | 1.01x faster                                                  |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-pythonperf2-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                         |
| unpickle_pure_python | 241 us                                                       | 205 us: 1.17x faster                                          |
| json_loads           | 28.7 us                                                      | 24.5 us: 1.17x faster                                         |
| xml_etree_parse      | 158 ms                                                       | 146 ms: 1.08x faster                                          |
| tomli_loads          | 2.26 sec                                                     | 2.18 sec: 1.04x faster                                        |
| pickle_pure_python   | 319 us                                                       | 322 us: 1.01x slower                                          |
| pickle_dict          | 30.8 us                                                      | 31.5 us: 1.02x slower                                         |
| unpickle_list        | 4.53 us                                                      | 4.69 us: 1.03x slower                                         |
| pickle               | 9.64 us                                                      | 10.0 us: 1.04x slower                                         |
| xml_etree_process    | 56.5 ms                                                      | 59.1 ms: 1.05x slower                                         |
| unpickle             | 13.4 us                                                      | 14.3 us: 1.07x slower                                         |
| xml_etree_generate   | 80.5 ms                                                      | 86.3 ms: 1.07x slower                                         |
| pickle_list          | 3.83 us                                                      | 4.23 us: 1.11x slower                                         |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                  |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-pythonperf2-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                         |
| python_startup_no_site | 7.76 ms                                                      | 8.49 ms: 1.09x slower                                         |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-pythonperf2-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 9.99 ms: 1.10x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-pythonperf2-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 150 us: 3.49x faster                                          |
| asyncio_tcp              | 753 ms                                                       | 383 ms: 1.97x faster                                          |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                        |
| generators               | 56.0 ms                                                      | 36.5 ms: 1.54x faster                                         |
| chaos                    | 80.9 ms                                                      | 62.7 ms: 1.29x faster                                         |
| json_dumps               | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                         |
| deltablue                | 4.00 ms                                                      | 3.18 ms: 1.26x faster                                         |
| fannkuch                 | 429 ms                                                       | 342 ms: 1.25x faster                                          |
| mypy2                    | 451 ms                                                       | 366 ms: 1.23x faster                                          |
| hexiom                   | 7.13 ms                                                      | 5.79 ms: 1.23x faster                                         |
| coroutines               | 27.6 ms                                                      | 22.4 ms: 1.23x faster                                         |
| richards_super           | 61.0 ms                                                      | 51.5 ms: 1.19x faster                                         |
| unpickle_pure_python     | 241 us                                                       | 205 us: 1.17x faster                                          |
| json_loads               | 28.7 us                                                      | 24.5 us: 1.17x faster                                         |
| scimark_lu               | 115 ms                                                       | 97.9 ms: 1.17x faster                                         |
| comprehensions           | 24.6 us                                                      | 21.6 us: 1.14x faster                                         |
| nqueens                  | 103 ms                                                       | 90.1 ms: 1.14x faster                                         |
| async_tree_memoization   | 630 ms                                                       | 553 ms: 1.14x faster                                          |
| go                       | 164 ms                                                       | 145 ms: 1.13x faster                                          |
| async_tree_none          | 519 ms                                                       | 459 ms: 1.13x faster                                          |
| json                     | 5.65 ms                                                      | 5.08 ms: 1.11x faster                                         |
| async_tree_io            | 1.17 sec                                                     | 1.06 sec: 1.11x faster                                        |
| sqlglot_parse            | 1.53 ms                                                      | 1.38 ms: 1.11x faster                                         |
| mako                     | 11.0 ms                                                      | 9.99 ms: 1.10x faster                                         |
| regex_compile            | 158 ms                                                       | 144 ms: 1.09x faster                                          |
| logging_format           | 8.11 us                                                      | 7.42 us: 1.09x faster                                         |
| richards                 | 48.3 ms                                                      | 44.4 ms: 1.09x faster                                         |
| mdp                      | 2.75 sec                                                     | 2.52 sec: 1.09x faster                                        |
| xml_etree_parse          | 158 ms                                                       | 146 ms: 1.08x faster                                          |
| logging_simple           | 7.19 us                                                      | 6.67 us: 1.08x faster                                         |
| sqlglot_transpile        | 1.92 ms                                                      | 1.78 ms: 1.08x faster                                         |
| sqlglot_normalize        | 126 ms                                                       | 117 ms: 1.07x faster                                          |
| gc_traversal             | 3.85 ms                                                      | 3.59 ms: 1.07x faster                                         |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 704 ms: 1.06x faster                                          |
| raytrace                 | 317 ms                                                       | 299 ms: 1.06x faster                                          |
| bench_thread_pool        | 1.01 ms                                                      | 957 us: 1.06x faster                                          |
| deepcopy                 | 399 us                                                       | 379 us: 1.05x faster                                          |
| logging_silent           | 101 ns                                                       | 95.7 ns: 1.05x faster                                         |
| pycparser                | 1.32 sec                                                     | 1.26 sec: 1.05x faster                                        |
| tomli_loads              | 2.26 sec                                                     | 2.18 sec: 1.04x faster                                        |
| meteor_contest           | 131 ms                                                       | 126 ms: 1.04x faster                                          |
| nbody                    | 90.7 ms                                                      | 87.5 ms: 1.04x faster                                         |
| sqlglot_optimize         | 59.8 ms                                                      | 57.8 ms: 1.04x faster                                         |
| dulwich_log              | 68.4 ms                                                      | 66.6 ms: 1.03x faster                                         |
| deepcopy_memo            | 38.8 us                                                      | 38.0 us: 1.02x faster                                         |
| crypto_pyaes             | 83.4 ms                                                      | 81.7 ms: 1.02x faster                                         |
| scimark_sor              | 111 ms                                                       | 109 ms: 1.02x faster                                          |
| pyflate                  | 449 ms                                                       | 442 ms: 1.02x faster                                          |
| spectral_norm            | 93.3 ms                                                      | 92.6 ms: 1.01x faster                                         |
| 2to3                     | 288 ms                                                       | 286 ms: 1.00x faster                                          |
| pickle_pure_python       | 319 us                                                       | 322 us: 1.01x slower                                          |
| pprint_pformat           | 1.63 sec                                                     | 1.64 sec: 1.01x slower                                        |
| pathlib                  | 19.1 ms                                                      | 19.2 ms: 1.01x slower                                         |
| scimark_monte_carlo      | 68.2 ms                                                      | 68.9 ms: 1.01x slower                                         |
| docutils                 | 2.86 sec                                                     | 2.90 sec: 1.02x slower                                        |
| pickle_dict              | 30.8 us                                                      | 31.5 us: 1.02x slower                                         |
| pprint_safe_repr         | 784 ms                                                       | 807 ms: 1.03x slower                                          |
| telco                    | 6.86 ms                                                      | 7.09 ms: 1.03x slower                                         |
| unpickle_list            | 4.53 us                                                      | 4.69 us: 1.03x slower                                         |
| pidigits                 | 251 ms                                                       | 260 ms: 1.04x slower                                          |
| pickle                   | 9.64 us                                                      | 10.0 us: 1.04x slower                                         |
| xml_etree_process        | 56.5 ms                                                      | 59.1 ms: 1.05x slower                                         |
| scimark_fft              | 285 ms                                                       | 299 ms: 1.05x slower                                          |
| coverage                 | 84.8 ms                                                      | 89.2 ms: 1.05x slower                                         |
| float                    | 74.2 ms                                                      | 78.5 ms: 1.06x slower                                         |
| regex_dna                | 227 ms                                                       | 242 ms: 1.07x slower                                          |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.32 ms: 1.07x slower                                         |
| unpickle                 | 13.4 us                                                      | 14.3 us: 1.07x slower                                         |
| python_startup           | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                         |
| xml_etree_generate       | 80.5 ms                                                      | 86.3 ms: 1.07x slower                                         |
| sqlite_synth             | 2.50 us                                                      | 2.72 us: 1.09x slower                                         |
| python_startup_no_site   | 7.76 ms                                                      | 8.49 ms: 1.09x slower                                         |
| pickle_list              | 3.83 us                                                      | 4.23 us: 1.11x slower                                         |
| unpack_sequence          | 45.6 ns                                                      | 54.5 ns: 1.19x slower                                         |
| async_generators         | 316 ms                                                       | 391 ms: 1.24x slower                                          |
| dask                     | 410 ms                                                       | 569 ms: 1.39x slower                                          |
| Geometric mean           | (ref)                                                        | 1.07x faster                                                  |

Benchmark hidden because not significant (7): deepcopy_reduce, tornado_http, xml_etree_iterparse, regex_v8, regex_effbot, create_gc_cycles, bench_mp_pool
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x
