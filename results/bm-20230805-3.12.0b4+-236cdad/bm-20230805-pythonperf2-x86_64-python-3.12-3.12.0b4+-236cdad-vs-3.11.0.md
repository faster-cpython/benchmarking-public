
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 236cdad
- commit date: 2023-08-05
- overall geometric mean: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-python-3.12-3.12.0b4+-236cdad |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 286 ms: 1.01x faster                                         |
| docutils       | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-python-3.12-3.12.0b4+-236cdad |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                         |
| float          | 74.2 ms                                                      | 78.1 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-python-3.12-3.12.0b4+-236cdad |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 143 ms: 1.10x faster                                         |
| regex_v8       | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                        |
| regex_effbot   | 3.50 ms                                                      | 3.49 ms: 1.00x faster                                        |
| regex_dna      | 227 ms                                                       | 242 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-python-3.12-3.12.0b4+-236cdad |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                        |
| json_loads           | 28.7 us                                                      | 24.5 us: 1.17x faster                                        |
| unpickle_pure_python | 241 us                                                       | 207 us: 1.16x faster                                         |
| xml_etree_parse      | 158 ms                                                       | 148 ms: 1.07x faster                                         |
| tomli_loads          | 2.26 sec                                                     | 2.17 sec: 1.04x faster                                       |
| xml_etree_iterparse  | 104 ms                                                       | 105 ms: 1.01x slower                                         |
| unpickle_list        | 4.53 us                                                      | 4.65 us: 1.03x slower                                        |
| xml_etree_process    | 56.5 ms                                                      | 58.7 ms: 1.04x slower                                        |
| pickle_dict          | 30.8 us                                                      | 32.3 us: 1.05x slower                                        |
| pickle               | 9.64 us                                                      | 10.1 us: 1.05x slower                                        |
| unpickle             | 13.4 us                                                      | 14.1 us: 1.05x slower                                        |
| xml_etree_generate   | 80.5 ms                                                      | 85.0 ms: 1.06x slower                                        |
| pickle_list          | 3.83 us                                                      | 4.59 us: 1.20x slower                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-python-3.12-3.12.0b4+-236cdad |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.51 ms: 1.10x slower                                        |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-python-3.12-3.12.0b4+-236cdad |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 9.95 ms: 1.10x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-python-3.12-3.12.0b4+-236cdad |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 151 us: 3.46x faster                                         |
| asyncio_tcp              | 753 ms                                                       | 381 ms: 1.98x faster                                         |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                       |
| generators               | 56.0 ms                                                      | 36.3 ms: 1.54x faster                                        |
| json_dumps               | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                        |
| chaos                    | 80.9 ms                                                      | 62.9 ms: 1.29x faster                                        |
| fannkuch                 | 429 ms                                                       | 341 ms: 1.26x faster                                         |
| deltablue                | 4.00 ms                                                      | 3.22 ms: 1.24x faster                                        |
| mypy2                    | 451 ms                                                       | 365 ms: 1.24x faster                                         |
| hexiom                   | 7.13 ms                                                      | 5.79 ms: 1.23x faster                                        |
| coroutines               | 27.6 ms                                                      | 22.9 ms: 1.21x faster                                        |
| richards_super           | 61.0 ms                                                      | 51.4 ms: 1.19x faster                                        |
| scimark_lu               | 115 ms                                                       | 97.3 ms: 1.18x faster                                        |
| json_loads               | 28.7 us                                                      | 24.5 us: 1.17x faster                                        |
| unpickle_pure_python     | 241 us                                                       | 207 us: 1.16x faster                                         |
| nqueens                  | 103 ms                                                       | 88.7 ms: 1.16x faster                                        |
| async_tree_memoization   | 630 ms                                                       | 553 ms: 1.14x faster                                         |
| comprehensions           | 24.6 us                                                      | 21.6 us: 1.14x faster                                        |
| go                       | 164 ms                                                       | 144 ms: 1.14x faster                                         |
| async_tree_none          | 519 ms                                                       | 459 ms: 1.13x faster                                         |
| async_tree_io            | 1.17 sec                                                     | 1.06 sec: 1.11x faster                                       |
| sqlglot_parse            | 1.53 ms                                                      | 1.39 ms: 1.11x faster                                        |
| mako                     | 11.0 ms                                                      | 9.95 ms: 1.10x faster                                        |
| regex_compile            | 158 ms                                                       | 143 ms: 1.10x faster                                         |
| json                     | 5.65 ms                                                      | 5.18 ms: 1.09x faster                                        |
| logging_format           | 8.11 us                                                      | 7.45 us: 1.09x faster                                        |
| logging_silent           | 101 ns                                                       | 93.2 ns: 1.08x faster                                        |
| mdp                      | 2.75 sec                                                     | 2.54 sec: 1.08x faster                                       |
| richards                 | 48.3 ms                                                      | 45.0 ms: 1.07x faster                                        |
| sqlglot_transpile        | 1.92 ms                                                      | 1.79 ms: 1.07x faster                                        |
| sqlglot_normalize        | 126 ms                                                       | 118 ms: 1.07x faster                                         |
| deepcopy_memo            | 38.8 us                                                      | 36.4 us: 1.07x faster                                        |
| xml_etree_parse          | 158 ms                                                       | 148 ms: 1.07x faster                                         |
| deepcopy                 | 399 us                                                       | 376 us: 1.06x faster                                         |
| logging_simple           | 7.19 us                                                      | 6.78 us: 1.06x faster                                        |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 709 ms: 1.06x faster                                         |
| spectral_norm            | 93.3 ms                                                      | 88.9 ms: 1.05x faster                                        |
| tomli_loads              | 2.26 sec                                                     | 2.17 sec: 1.04x faster                                       |
| pycparser                | 1.32 sec                                                     | 1.27 sec: 1.04x faster                                       |
| bench_thread_pool        | 1.01 ms                                                      | 972 us: 1.04x faster                                         |
| dulwich_log              | 68.4 ms                                                      | 65.9 ms: 1.04x faster                                        |
| scimark_sor              | 111 ms                                                       | 107 ms: 1.04x faster                                         |
| sqlglot_optimize         | 59.8 ms                                                      | 57.8 ms: 1.04x faster                                        |
| raytrace                 | 317 ms                                                       | 306 ms: 1.03x faster                                         |
| meteor_contest           | 131 ms                                                       | 127 ms: 1.03x faster                                         |
| crypto_pyaes             | 83.4 ms                                                      | 80.9 ms: 1.03x faster                                        |
| deepcopy_reduce          | 3.51 us                                                      | 3.43 us: 1.02x faster                                        |
| regex_v8                 | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                        |
| pyflate                  | 449 ms                                                       | 442 ms: 1.01x faster                                         |
| pathlib                  | 19.1 ms                                                      | 18.8 ms: 1.01x faster                                        |
| 2to3                     | 288 ms                                                       | 286 ms: 1.01x faster                                         |
| regex_effbot             | 3.50 ms                                                      | 3.49 ms: 1.00x faster                                        |
| pprint_pformat           | 1.63 sec                                                     | 1.64 sec: 1.01x slower                                       |
| xml_etree_iterparse      | 104 ms                                                       | 105 ms: 1.01x slower                                         |
| docutils                 | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                       |
| scimark_monte_carlo      | 68.2 ms                                                      | 69.6 ms: 1.02x slower                                        |
| pprint_safe_repr         | 784 ms                                                       | 804 ms: 1.03x slower                                         |
| unpickle_list            | 4.53 us                                                      | 4.65 us: 1.03x slower                                        |
| create_gc_cycles         | 1.61 ms                                                      | 1.66 ms: 1.03x slower                                        |
| pidigits                 | 251 ms                                                       | 260 ms: 1.03x slower                                         |
| telco                    | 6.86 ms                                                      | 7.12 ms: 1.04x slower                                        |
| xml_etree_process        | 56.5 ms                                                      | 58.7 ms: 1.04x slower                                        |
| scimark_fft              | 285 ms                                                       | 297 ms: 1.04x slower                                         |
| coverage                 | 84.8 ms                                                      | 88.5 ms: 1.04x slower                                        |
| pickle_dict              | 30.8 us                                                      | 32.3 us: 1.05x slower                                        |
| pickle                   | 9.64 us                                                      | 10.1 us: 1.05x slower                                        |
| unpickle                 | 13.4 us                                                      | 14.1 us: 1.05x slower                                        |
| float                    | 74.2 ms                                                      | 78.1 ms: 1.05x slower                                        |
| xml_etree_generate       | 80.5 ms                                                      | 85.0 ms: 1.06x slower                                        |
| regex_dna                | 227 ms                                                       | 242 ms: 1.06x slower                                         |
| python_startup           | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                        |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.34 ms: 1.07x slower                                        |
| sqlite_synth             | 2.50 us                                                      | 2.74 us: 1.10x slower                                        |
| python_startup_no_site   | 7.76 ms                                                      | 8.51 ms: 1.10x slower                                        |
| gc_traversal             | 3.85 ms                                                      | 4.23 ms: 1.10x slower                                        |
| unpack_sequence          | 45.6 ns                                                      | 52.8 ns: 1.16x slower                                        |
| pickle_list              | 3.83 us                                                      | 4.59 us: 1.20x slower                                        |
| async_generators         | 316 ms                                                       | 388 ms: 1.23x slower                                         |
| dask                     | 410 ms                                                       | 563 ms: 1.37x slower                                         |
| Geometric mean           | (ref)                                                        | 1.07x faster                                                 |

Benchmark hidden because not significant (4): pickle_pure_python, tornado_http, nbody, bench_mp_pool
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
