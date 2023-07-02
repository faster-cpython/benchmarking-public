
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 730c873
- commit date: 2023-07-01
- overall geometric mean: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf2-x86_64-python-3.12-3.12.0b3+-730c873 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 285 ms: 1.01x faster                                         |
| docutils       | 2.86 sec                                                     | 2.88 sec: 1.01x slower                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf2-x86_64-python-3.12-3.12.0b3+-730c873 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 85.0 ms: 1.07x faster                                        |
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                         |
| float          | 74.2 ms                                                      | 78.4 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf2-x86_64-python-3.12-3.12.0b3+-730c873 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 143 ms: 1.10x faster                                         |
| regex_effbot   | 3.50 ms                                                      | 3.49 ms: 1.00x faster                                        |
| regex_v8       | 23.9 ms                                                      | 24.0 ms: 1.00x slower                                        |
| regex_dna      | 227 ms                                                       | 244 ms: 1.07x slower                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf2-x86_64-python-3.12-3.12.0b3+-730c873 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.32x faster                                        |
| unpickle_pure_python | 241 us                                                       | 205 us: 1.17x faster                                         |
| json_loads           | 28.7 us                                                      | 24.5 us: 1.17x faster                                        |
| xml_etree_parse      | 158 ms                                                       | 152 ms: 1.04x faster                                         |
| tomli_loads          | 2.26 sec                                                     | 2.19 sec: 1.03x faster                                       |
| xml_etree_iterparse  | 104 ms                                                       | 105 ms: 1.01x slower                                         |
| xml_etree_process    | 56.5 ms                                                      | 57.9 ms: 1.03x slower                                        |
| pickle               | 9.64 us                                                      | 10.1 us: 1.05x slower                                        |
| pickle_dict          | 30.8 us                                                      | 32.2 us: 1.05x slower                                        |
| xml_etree_generate   | 80.5 ms                                                      | 84.8 ms: 1.05x slower                                        |
| unpickle_list        | 4.53 us                                                      | 4.78 us: 1.05x slower                                        |
| unpickle             | 13.4 us                                                      | 14.2 us: 1.06x slower                                        |
| pickle_list          | 3.83 us                                                      | 4.46 us: 1.17x slower                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf2-x86_64-python-3.12-3.12.0b3+-730c873 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.46 ms: 1.09x slower                                        |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf2-x86_64-python-3.12-3.12.0b3+-730c873 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf2-x86_64-python-3.12-3.12.0b3+-730c873 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 152 us: 3.43x faster                                         |
| asyncio_tcp              | 753 ms                                                       | 377 ms: 2.00x faster                                         |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.56 sec: 1.97x faster                                       |
| generators               | 56.0 ms                                                      | 36.1 ms: 1.55x faster                                        |
| json_dumps               | 13.4 ms                                                      | 10.2 ms: 1.32x faster                                        |
| chaos                    | 80.9 ms                                                      | 62.9 ms: 1.29x faster                                        |
| fannkuch                 | 429 ms                                                       | 343 ms: 1.25x faster                                         |
| mypy2                    | 451 ms                                                       | 363 ms: 1.24x faster                                         |
| deltablue                | 4.00 ms                                                      | 3.24 ms: 1.24x faster                                        |
| hexiom                   | 7.13 ms                                                      | 5.79 ms: 1.23x faster                                        |
| coroutines               | 27.6 ms                                                      | 22.6 ms: 1.22x faster                                        |
| richards_super           | 61.0 ms                                                      | 50.5 ms: 1.21x faster                                        |
| scimark_lu               | 115 ms                                                       | 95.9 ms: 1.19x faster                                        |
| unpickle_pure_python     | 241 us                                                       | 205 us: 1.17x faster                                         |
| json_loads               | 28.7 us                                                      | 24.5 us: 1.17x faster                                        |
| nqueens                  | 103 ms                                                       | 89.7 ms: 1.15x faster                                        |
| async_tree_memoization   | 630 ms                                                       | 551 ms: 1.14x faster                                         |
| go                       | 164 ms                                                       | 144 ms: 1.14x faster                                         |
| async_tree_none          | 519 ms                                                       | 459 ms: 1.13x faster                                         |
| logging_format           | 8.11 us                                                      | 7.25 us: 1.12x faster                                        |
| comprehensions           | 24.6 us                                                      | 22.1 us: 1.11x faster                                        |
| async_tree_io            | 1.17 sec                                                     | 1.05 sec: 1.11x faster                                       |
| regex_compile            | 158 ms                                                       | 143 ms: 1.10x faster                                         |
| sqlglot_parse            | 1.53 ms                                                      | 1.39 ms: 1.10x faster                                        |
| json                     | 5.65 ms                                                      | 5.13 ms: 1.10x faster                                        |
| logging_simple           | 7.19 us                                                      | 6.56 us: 1.10x faster                                        |
| sqlglot_normalize        | 126 ms                                                       | 116 ms: 1.09x faster                                         |
| mako                     | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                        |
| richards                 | 48.3 ms                                                      | 44.6 ms: 1.08x faster                                        |
| deepcopy_memo            | 38.8 us                                                      | 36.1 us: 1.08x faster                                        |
| sqlglot_transpile        | 1.92 ms                                                      | 1.78 ms: 1.08x faster                                        |
| deepcopy                 | 399 us                                                       | 371 us: 1.08x faster                                         |
| mdp                      | 2.75 sec                                                     | 2.57 sec: 1.07x faster                                       |
| nbody                    | 90.7 ms                                                      | 85.0 ms: 1.07x faster                                        |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 704 ms: 1.06x faster                                         |
| logging_silent           | 101 ns                                                       | 95.0 ns: 1.06x faster                                        |
| spectral_norm            | 93.3 ms                                                      | 88.0 ms: 1.06x faster                                        |
| bench_thread_pool        | 1.01 ms                                                      | 954 us: 1.06x faster                                         |
| meteor_contest           | 131 ms                                                       | 124 ms: 1.05x faster                                         |
| pycparser                | 1.32 sec                                                     | 1.26 sec: 1.05x faster                                       |
| sqlglot_optimize         | 59.8 ms                                                      | 57.3 ms: 1.04x faster                                        |
| deepcopy_reduce          | 3.51 us                                                      | 3.38 us: 1.04x faster                                        |
| xml_etree_parse          | 158 ms                                                       | 152 ms: 1.04x faster                                         |
| scimark_sor              | 111 ms                                                       | 107 ms: 1.04x faster                                         |
| tomli_loads              | 2.26 sec                                                     | 2.19 sec: 1.03x faster                                       |
| raytrace                 | 317 ms                                                       | 306 ms: 1.03x faster                                         |
| pyflate                  | 449 ms                                                       | 435 ms: 1.03x faster                                         |
| crypto_pyaes             | 83.4 ms                                                      | 81.6 ms: 1.02x faster                                        |
| dulwich_log              | 68.4 ms                                                      | 67.1 ms: 1.02x faster                                        |
| 2to3                     | 288 ms                                                       | 285 ms: 1.01x faster                                         |
| scimark_monte_carlo      | 68.2 ms                                                      | 67.8 ms: 1.01x faster                                        |
| regex_effbot             | 3.50 ms                                                      | 3.49 ms: 1.00x faster                                        |
| regex_v8                 | 23.9 ms                                                      | 24.0 ms: 1.00x slower                                        |
| xml_etree_iterparse      | 104 ms                                                       | 105 ms: 1.01x slower                                         |
| docutils                 | 2.86 sec                                                     | 2.88 sec: 1.01x slower                                       |
| pathlib                  | 19.1 ms                                                      | 19.2 ms: 1.01x slower                                        |
| pprint_safe_repr         | 784 ms                                                       | 799 ms: 1.02x slower                                         |
| create_gc_cycles         | 1.61 ms                                                      | 1.64 ms: 1.02x slower                                        |
| xml_etree_process        | 56.5 ms                                                      | 57.9 ms: 1.03x slower                                        |
| pidigits                 | 251 ms                                                       | 260 ms: 1.03x slower                                         |
| telco                    | 6.86 ms                                                      | 7.14 ms: 1.04x slower                                        |
| pickle                   | 9.64 us                                                      | 10.1 us: 1.05x slower                                        |
| pickle_dict              | 30.8 us                                                      | 32.2 us: 1.05x slower                                        |
| xml_etree_generate       | 80.5 ms                                                      | 84.8 ms: 1.05x slower                                        |
| unpickle_list            | 4.53 us                                                      | 4.78 us: 1.05x slower                                        |
| unpickle                 | 13.4 us                                                      | 14.2 us: 1.06x slower                                        |
| float                    | 74.2 ms                                                      | 78.4 ms: 1.06x slower                                        |
| scimark_fft              | 285 ms                                                       | 301 ms: 1.06x slower                                         |
| python_startup           | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                        |
| coverage                 | 84.8 ms                                                      | 90.8 ms: 1.07x slower                                        |
| regex_dna                | 227 ms                                                       | 244 ms: 1.07x slower                                         |
| sqlite_synth             | 2.50 us                                                      | 2.70 us: 1.08x slower                                        |
| python_startup_no_site   | 7.76 ms                                                      | 8.46 ms: 1.09x slower                                        |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.46 ms: 1.10x slower                                        |
| pickle_list              | 3.83 us                                                      | 4.46 us: 1.17x slower                                        |
| bench_mp_pool            | 4.62 ms                                                      | 5.53 ms: 1.20x slower                                        |
| unpack_sequence          | 45.6 ns                                                      | 55.4 ns: 1.21x slower                                        |
| async_generators         | 316 ms                                                       | 388 ms: 1.23x slower                                         |
| dask                     | 410 ms                                                       | 559 ms: 1.36x slower                                         |
| Geometric mean           | (ref)                                                        | 1.07x faster                                                 |

Benchmark hidden because not significant (4): gc_traversal, tornado_http, pickle_pure_python, pprint_pformat
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
