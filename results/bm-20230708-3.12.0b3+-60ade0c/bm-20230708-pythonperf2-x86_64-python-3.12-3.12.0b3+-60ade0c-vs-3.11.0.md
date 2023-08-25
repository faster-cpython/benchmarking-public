
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 60ade0c
- commit date: 2023-07-08
- overall geometric mean: 1.07x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf2-x86_64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 285 ms: 1.01x faster                                         |
| docutils       | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf2-x86_64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 85.3 ms: 1.06x faster                                        |
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                         |
| float          | 74.2 ms                                                      | 79.1 ms: 1.07x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf2-x86_64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 145 ms: 1.09x faster                                         |
| regex_v8       | 23.9 ms                                                      | 23.6 ms: 1.02x faster                                        |
| regex_effbot   | 3.50 ms                                                      | 3.51 ms: 1.00x slower                                        |
| regex_dna      | 227 ms                                                       | 240 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf2-x86_64-python-3.12-3.12.0b3+-60ade0c |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                        |
| unpickle_pure_python | 241 us                                                       | 211 us: 1.14x faster                                         |
| json_loads           | 28.7 us                                                      | 25.3 us: 1.13x faster                                        |
| xml_etree_parse      | 158 ms                                                       | 153 ms: 1.03x faster                                         |
| tomli_loads          | 2.26 sec                                                     | 2.22 sec: 1.02x faster                                       |
| pickle_pure_python   | 319 us                                                       | 324 us: 1.02x slower                                         |
| xml_etree_iterparse  | 104 ms                                                       | 107 ms: 1.02x slower                                         |
| xml_etree_process    | 56.5 ms                                                      | 58.7 ms: 1.04x slower                                        |
| unpickle_list        | 4.53 us                                                      | 4.72 us: 1.04x slower                                        |
| xml_etree_generate   | 80.5 ms                                                      | 85.8 ms: 1.07x slower                                        |
| pickle_dict          | 30.8 us                                                      | 33.1 us: 1.08x slower                                        |
| pickle               | 9.64 us                                                      | 10.4 us: 1.08x slower                                        |
| unpickle             | 13.4 us                                                      | 14.8 us: 1.10x slower                                        |
| pickle_list          | 3.83 us                                                      | 4.47 us: 1.17x slower                                        |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf2-x86_64-python-3.12-3.12.0b3+-60ade0c |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.46 ms: 1.09x slower                                        |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf2-x86_64-python-3.12-3.12.0b3+-60ade0c |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 9.98 ms: 1.10x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf2-x86_64-python-3.12-3.12.0b3+-60ade0c |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 153 us: 3.41x faster                                         |
| asyncio_tcp              | 753 ms                                                       | 379 ms: 1.99x faster                                         |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.97x faster                                       |
| generators               | 56.0 ms                                                      | 36.1 ms: 1.55x faster                                        |
| json_dumps               | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                        |
| chaos                    | 80.9 ms                                                      | 63.7 ms: 1.27x faster                                        |
| deltablue                | 4.00 ms                                                      | 3.22 ms: 1.24x faster                                        |
| mypy2                    | 451 ms                                                       | 366 ms: 1.23x faster                                         |
| richards_super           | 61.0 ms                                                      | 49.8 ms: 1.23x faster                                        |
| fannkuch                 | 429 ms                                                       | 350 ms: 1.23x faster                                         |
| hexiom                   | 7.13 ms                                                      | 5.83 ms: 1.22x faster                                        |
| coroutines               | 27.6 ms                                                      | 22.9 ms: 1.21x faster                                        |
| scimark_lu               | 115 ms                                                       | 97.4 ms: 1.18x faster                                        |
| async_tree_memoization   | 630 ms                                                       | 547 ms: 1.15x faster                                         |
| async_tree_none          | 519 ms                                                       | 454 ms: 1.14x faster                                         |
| unpickle_pure_python     | 241 us                                                       | 211 us: 1.14x faster                                         |
| nqueens                  | 103 ms                                                       | 90.5 ms: 1.14x faster                                        |
| json_loads               | 28.7 us                                                      | 25.3 us: 1.13x faster                                        |
| go                       | 164 ms                                                       | 146 ms: 1.13x faster                                         |
| comprehensions           | 24.6 us                                                      | 22.0 us: 1.12x faster                                        |
| async_tree_io            | 1.17 sec                                                     | 1.05 sec: 1.12x faster                                       |
| sqlglot_parse            | 1.53 ms                                                      | 1.39 ms: 1.11x faster                                        |
| json                     | 5.65 ms                                                      | 5.12 ms: 1.10x faster                                        |
| mako                     | 11.0 ms                                                      | 9.98 ms: 1.10x faster                                        |
| richards                 | 48.3 ms                                                      | 44.2 ms: 1.09x faster                                        |
| regex_compile            | 158 ms                                                       | 145 ms: 1.09x faster                                         |
| mdp                      | 2.75 sec                                                     | 2.53 sec: 1.09x faster                                       |
| logging_silent           | 101 ns                                                       | 93.2 ns: 1.08x faster                                        |
| sqlglot_normalize        | 126 ms                                                       | 117 ms: 1.08x faster                                         |
| sqlglot_transpile        | 1.92 ms                                                      | 1.79 ms: 1.07x faster                                        |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 697 ms: 1.07x faster                                         |
| pycparser                | 1.32 sec                                                     | 1.24 sec: 1.06x faster                                       |
| nbody                    | 90.7 ms                                                      | 85.3 ms: 1.06x faster                                        |
| logging_format           | 8.11 us                                                      | 7.64 us: 1.06x faster                                        |
| bench_thread_pool        | 1.01 ms                                                      | 957 us: 1.06x faster                                         |
| logging_simple           | 7.19 us                                                      | 6.83 us: 1.05x faster                                        |
| raytrace                 | 317 ms                                                       | 301 ms: 1.05x faster                                         |
| deepcopy                 | 399 us                                                       | 383 us: 1.04x faster                                         |
| sqlglot_optimize         | 59.8 ms                                                      | 57.8 ms: 1.04x faster                                        |
| meteor_contest           | 131 ms                                                       | 126 ms: 1.03x faster                                         |
| deepcopy_memo            | 38.8 us                                                      | 37.5 us: 1.03x faster                                        |
| xml_etree_parse          | 158 ms                                                       | 153 ms: 1.03x faster                                         |
| dulwich_log              | 68.4 ms                                                      | 66.8 ms: 1.02x faster                                        |
| deepcopy_reduce          | 3.51 us                                                      | 3.44 us: 1.02x faster                                        |
| gc_traversal             | 3.85 ms                                                      | 3.76 ms: 1.02x faster                                        |
| pyflate                  | 449 ms                                                       | 439 ms: 1.02x faster                                         |
| scimark_monte_carlo      | 68.2 ms                                                      | 66.9 ms: 1.02x faster                                        |
| tomli_loads              | 2.26 sec                                                     | 2.22 sec: 1.02x faster                                       |
| scimark_sor              | 111 ms                                                       | 109 ms: 1.02x faster                                         |
| regex_v8                 | 23.9 ms                                                      | 23.6 ms: 1.02x faster                                        |
| crypto_pyaes             | 83.4 ms                                                      | 82.1 ms: 1.02x faster                                        |
| 2to3                     | 288 ms                                                       | 285 ms: 1.01x faster                                         |
| regex_effbot             | 3.50 ms                                                      | 3.51 ms: 1.00x slower                                        |
| docutils                 | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                       |
| pickle_pure_python       | 319 us                                                       | 324 us: 1.02x slower                                         |
| create_gc_cycles         | 1.61 ms                                                      | 1.64 ms: 1.02x slower                                        |
| pprint_safe_repr         | 784 ms                                                       | 801 ms: 1.02x slower                                         |
| xml_etree_iterparse      | 104 ms                                                       | 107 ms: 1.02x slower                                         |
| pathlib                  | 19.1 ms                                                      | 19.7 ms: 1.03x slower                                        |
| telco                    | 6.86 ms                                                      | 7.08 ms: 1.03x slower                                        |
| pidigits                 | 251 ms                                                       | 261 ms: 1.04x slower                                         |
| xml_etree_process        | 56.5 ms                                                      | 58.7 ms: 1.04x slower                                        |
| unpickle_list            | 4.53 us                                                      | 4.72 us: 1.04x slower                                        |
| coverage                 | 84.8 ms                                                      | 89.2 ms: 1.05x slower                                        |
| regex_dna                | 227 ms                                                       | 240 ms: 1.06x slower                                         |
| scimark_fft              | 285 ms                                                       | 302 ms: 1.06x slower                                         |
| python_startup           | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                        |
| xml_etree_generate       | 80.5 ms                                                      | 85.8 ms: 1.07x slower                                        |
| float                    | 74.2 ms                                                      | 79.1 ms: 1.07x slower                                        |
| unpack_sequence          | 45.6 ns                                                      | 49.1 ns: 1.08x slower                                        |
| pickle_dict              | 30.8 us                                                      | 33.1 us: 1.08x slower                                        |
| pickle                   | 9.64 us                                                      | 10.4 us: 1.08x slower                                        |
| python_startup_no_site   | 7.76 ms                                                      | 8.46 ms: 1.09x slower                                        |
| sqlite_synth             | 2.50 us                                                      | 2.74 us: 1.10x slower                                        |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.45 ms: 1.10x slower                                        |
| unpickle                 | 13.4 us                                                      | 14.8 us: 1.10x slower                                        |
| bench_mp_pool            | 4.62 ms                                                      | 5.24 ms: 1.13x slower                                        |
| pickle_list              | 3.83 us                                                      | 4.47 us: 1.17x slower                                        |
| async_generators         | 316 ms                                                       | 397 ms: 1.26x slower                                         |
| dask                     | 410 ms                                                       | 563 ms: 1.37x slower                                         |
| Geometric mean           | (ref)                                                        | 1.07x faster                                                 |

Benchmark hidden because not significant (3): tornado_http, spectral_norm, pprint_pformat
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 99.89% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
