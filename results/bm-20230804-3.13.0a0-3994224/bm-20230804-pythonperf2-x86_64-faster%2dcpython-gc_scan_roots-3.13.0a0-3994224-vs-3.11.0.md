
# Results vs. 3.11.0

- fork: faster-cpython
- ref: gc_scan_roots
- machine: linux-x86_64
- commit hash: 3994224
- commit date: 2023-08-04
- overall geometric mean: 1.04x faster
- HPT reliability: 74.65%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 3.00 sec: 1.05x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 87.7 ms: 1.03x faster                                                          |
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                                           |
| float          | 74.2 ms                                                      | 82.4 ms: 1.11x slower                                                          |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 148 ms: 1.07x faster                                                           |
| regex_v8       | 23.9 ms                                                      | 23.9 ms: 1.00x faster                                                          |
| regex_effbot   | 3.50 ms                                                      | 3.74 ms: 1.07x slower                                                          |
| regex_dna      | 227 ms                                                       | 248 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                          |
| json_loads           | 28.7 us                                                      | 25.3 us: 1.14x faster                                                          |
| xml_etree_parse      | 158 ms                                                       | 143 ms: 1.10x faster                                                           |
| unpickle_pure_python | 241 us                                                       | 232 us: 1.04x faster                                                           |
| pickle_pure_python   | 319 us                                                       | 318 us: 1.00x faster                                                           |
| tomli_loads          | 2.26 sec                                                     | 2.29 sec: 1.01x slower                                                         |
| pickle_dict          | 30.8 us                                                      | 31.9 us: 1.04x slower                                                          |
| xml_etree_process    | 56.5 ms                                                      | 58.9 ms: 1.04x slower                                                          |
| pickle               | 9.64 us                                                      | 10.1 us: 1.05x slower                                                          |
| xml_etree_generate   | 80.5 ms                                                      | 85.6 ms: 1.06x slower                                                          |
| unpickle_list        | 4.53 us                                                      | 4.83 us: 1.07x slower                                                          |
| unpickle             | 13.4 us                                                      | 15.1 us: 1.12x slower                                                          |
| pickle_list          | 3.83 us                                                      | 4.36 us: 1.14x slower                                                          |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                                          |
| python_startup_no_site | 7.76 ms                                                      | 8.64 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 151 us: 3.45x faster                                                           |
| asyncio_tcp              | 753 ms                                                       | 368 ms: 2.05x faster                                                           |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.95x faster                                                         |
| generators               | 56.0 ms                                                      | 36.6 ms: 1.53x faster                                                          |
| json_dumps               | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                          |
| chaos                    | 80.9 ms                                                      | 62.2 ms: 1.30x faster                                                          |
| mypy2                    | 451 ms                                                       | 372 ms: 1.21x faster                                                           |
| scimark_lu               | 115 ms                                                       | 97.3 ms: 1.18x faster                                                          |
| coroutines               | 27.6 ms                                                      | 23.5 ms: 1.17x faster                                                          |
| crypto_pyaes             | 83.4 ms                                                      | 73.2 ms: 1.14x faster                                                          |
| nqueens                  | 103 ms                                                       | 90.3 ms: 1.14x faster                                                          |
| json_loads               | 28.7 us                                                      | 25.3 us: 1.14x faster                                                          |
| raytrace                 | 317 ms                                                       | 279 ms: 1.13x faster                                                           |
| comprehensions           | 24.6 us                                                      | 22.2 us: 1.11x faster                                                          |
| hexiom                   | 7.13 ms                                                      | 6.46 ms: 1.10x faster                                                          |
| xml_etree_parse          | 158 ms                                                       | 143 ms: 1.10x faster                                                           |
| logging_format           | 8.11 us                                                      | 7.46 us: 1.09x faster                                                          |
| fannkuch                 | 429 ms                                                       | 395 ms: 1.09x faster                                                           |
| mdp                      | 2.75 sec                                                     | 2.54 sec: 1.08x faster                                                         |
| deltablue                | 4.00 ms                                                      | 3.71 ms: 1.08x faster                                                          |
| sqlglot_parse            | 1.53 ms                                                      | 1.42 ms: 1.08x faster                                                          |
| json                     | 5.65 ms                                                      | 5.25 ms: 1.08x faster                                                          |
| sqlglot_normalize        | 126 ms                                                       | 118 ms: 1.07x faster                                                           |
| async_tree_memoization   | 630 ms                                                       | 589 ms: 1.07x faster                                                           |
| bench_thread_pool        | 1.01 ms                                                      | 946 us: 1.07x faster                                                           |
| mako                     | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                                          |
| regex_compile            | 158 ms                                                       | 148 ms: 1.07x faster                                                           |
| deepcopy                 | 399 us                                                       | 376 us: 1.06x faster                                                           |
| async_tree_none          | 519 ms                                                       | 491 ms: 1.06x faster                                                           |
| logging_simple           | 7.19 us                                                      | 6.82 us: 1.05x faster                                                          |
| deepcopy_memo            | 38.8 us                                                      | 37.2 us: 1.04x faster                                                          |
| sqlglot_transpile        | 1.92 ms                                                      | 1.84 ms: 1.04x faster                                                          |
| unpickle_pure_python     | 241 us                                                       | 232 us: 1.04x faster                                                           |
| async_tree_io            | 1.17 sec                                                     | 1.13 sec: 1.03x faster                                                         |
| nbody                    | 90.7 ms                                                      | 87.7 ms: 1.03x faster                                                          |
| logging_silent           | 101 ns                                                       | 98.3 ns: 1.03x faster                                                          |
| deepcopy_reduce          | 3.51 us                                                      | 3.43 us: 1.02x faster                                                          |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 735 ms: 1.02x faster                                                           |
| sqlglot_optimize         | 59.8 ms                                                      | 58.7 ms: 1.02x faster                                                          |
| pickle_pure_python       | 319 us                                                       | 318 us: 1.00x faster                                                           |
| regex_v8                 | 23.9 ms                                                      | 23.9 ms: 1.00x faster                                                          |
| richards_super           | 61.0 ms                                                      | 61.8 ms: 1.01x slower                                                          |
| pprint_pformat           | 1.63 sec                                                     | 1.65 sec: 1.01x slower                                                         |
| tomli_loads              | 2.26 sec                                                     | 2.29 sec: 1.01x slower                                                         |
| pathlib                  | 19.1 ms                                                      | 19.3 ms: 1.02x slower                                                          |
| dulwich_log              | 68.4 ms                                                      | 69.5 ms: 1.02x slower                                                          |
| scimark_monte_carlo      | 68.2 ms                                                      | 69.7 ms: 1.02x slower                                                          |
| pprint_safe_repr         | 784 ms                                                       | 809 ms: 1.03x slower                                                           |
| pidigits                 | 251 ms                                                       | 260 ms: 1.03x slower                                                           |
| spectral_norm            | 93.3 ms                                                      | 96.7 ms: 1.04x slower                                                          |
| pickle_dict              | 30.8 us                                                      | 31.9 us: 1.04x slower                                                          |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.21 ms: 1.04x slower                                                          |
| xml_etree_process        | 56.5 ms                                                      | 58.9 ms: 1.04x slower                                                          |
| docutils                 | 2.86 sec                                                     | 3.00 sec: 1.05x slower                                                         |
| pickle                   | 9.64 us                                                      | 10.1 us: 1.05x slower                                                          |
| coverage                 | 84.8 ms                                                      | 89.8 ms: 1.06x slower                                                          |
| go                       | 164 ms                                                       | 174 ms: 1.06x slower                                                           |
| xml_etree_generate       | 80.5 ms                                                      | 85.6 ms: 1.06x slower                                                          |
| scimark_fft              | 285 ms                                                       | 303 ms: 1.06x slower                                                           |
| unpickle_list            | 4.53 us                                                      | 4.83 us: 1.07x slower                                                          |
| regex_effbot             | 3.50 ms                                                      | 3.74 ms: 1.07x slower                                                          |
| create_gc_cycles         | 1.61 ms                                                      | 1.72 ms: 1.07x slower                                                          |
| python_startup           | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                                          |
| unpack_sequence          | 45.6 ns                                                      | 49.6 ns: 1.09x slower                                                          |
| sqlite_synth             | 2.50 us                                                      | 2.72 us: 1.09x slower                                                          |
| regex_dna                | 227 ms                                                       | 248 ms: 1.09x slower                                                           |
| float                    | 74.2 ms                                                      | 82.4 ms: 1.11x slower                                                          |
| python_startup_no_site   | 7.76 ms                                                      | 8.64 ms: 1.11x slower                                                          |
| unpickle                 | 13.4 us                                                      | 15.1 us: 1.12x slower                                                          |
| richards                 | 48.3 ms                                                      | 54.8 ms: 1.13x slower                                                          |
| pickle_list              | 3.83 us                                                      | 4.36 us: 1.14x slower                                                          |
| pyflate                  | 449 ms                                                       | 517 ms: 1.15x slower                                                           |
| telco                    | 6.86 ms                                                      | 8.06 ms: 1.18x slower                                                          |
| async_generators         | 316 ms                                                       | 404 ms: 1.28x slower                                                           |
| scimark_sor              | 111 ms                                                       | 149 ms: 1.34x slower                                                           |
| dask                     | 410 ms                                                       | 588 ms: 1.43x slower                                                           |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                                   |

Benchmark hidden because not significant (6): gc_traversal, pycparser, meteor_contest, xml_etree_iterparse, tornado_http, bench_mp_pool
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 74.65% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
