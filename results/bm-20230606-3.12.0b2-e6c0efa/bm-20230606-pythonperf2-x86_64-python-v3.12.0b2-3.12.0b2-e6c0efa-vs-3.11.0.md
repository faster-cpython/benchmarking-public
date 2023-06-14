
# Results vs. 3.11.0

- fork: python
- ref: v3.12.0b2
- machine: linux-x86_64
- commit hash: e6c0efa
- commit date: 2023-06-06
- overall geometric mean: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf2-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 285 ms: 1.01x faster                                             |
| docutils       | 2.86 sec                                                     | 2.88 sec: 1.01x slower                                           |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf2-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 83.7 ms: 1.08x faster                                            |
| pidigits       | 251 ms                                                       | 259 ms: 1.03x slower                                             |
| float          | 74.2 ms                                                      | 77.3 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf2-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 144 ms: 1.09x faster                                             |
| regex_v8       | 23.9 ms                                                      | 23.6 ms: 1.01x faster                                            |
| regex_effbot   | 3.50 ms                                                      | 3.55 ms: 1.01x slower                                            |
| regex_dna      | 227 ms                                                       | 245 ms: 1.08x slower                                             |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf2-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                            |
| unpickle_pure_python | 241 us                                                       | 205 us: 1.18x faster                                             |
| json_loads           | 28.7 us                                                      | 24.5 us: 1.17x faster                                            |
| xml_etree_parse      | 158 ms                                                       | 148 ms: 1.06x faster                                             |
| tomli_loads          | 2.26 sec                                                     | 2.19 sec: 1.03x faster                                           |
| pickle_dict          | 30.8 us                                                      | 31.2 us: 1.01x slower                                            |
| pickle_pure_python   | 319 us                                                       | 324 us: 1.01x slower                                             |
| unpickle_list        | 4.53 us                                                      | 4.71 us: 1.04x slower                                            |
| xml_etree_process    | 56.5 ms                                                      | 58.8 ms: 1.04x slower                                            |
| pickle               | 9.64 us                                                      | 10.0 us: 1.04x slower                                            |
| xml_etree_generate   | 80.5 ms                                                      | 85.6 ms: 1.06x slower                                            |
| unpickle             | 13.4 us                                                      | 14.6 us: 1.09x slower                                            |
| pickle_list          | 3.83 us                                                      | 4.27 us: 1.12x slower                                            |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf2-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                            |
| python_startup_no_site | 7.76 ms                                                      | 8.45 ms: 1.09x slower                                            |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf2-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 9.93 ms: 1.11x faster                                            |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf2-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 150 us: 3.48x faster                                             |
| asyncio_tcp              | 753 ms                                                       | 379 ms: 1.99x faster                                             |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.97x faster                                           |
| generators               | 56.0 ms                                                      | 35.5 ms: 1.58x faster                                            |
| json_dumps               | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                            |
| chaos                    | 80.9 ms                                                      | 63.6 ms: 1.27x faster                                            |
| fannkuch                 | 429 ms                                                       | 343 ms: 1.25x faster                                             |
| coroutines               | 27.6 ms                                                      | 22.3 ms: 1.23x faster                                            |
| deltablue                | 4.00 ms                                                      | 3.25 ms: 1.23x faster                                            |
| hexiom                   | 7.13 ms                                                      | 5.95 ms: 1.20x faster                                            |
| richards_super           | 61.0 ms                                                      | 51.0 ms: 1.20x faster                                            |
| scimark_lu               | 115 ms                                                       | 96.3 ms: 1.19x faster                                            |
| unpickle_pure_python     | 241 us                                                       | 205 us: 1.18x faster                                             |
| json_loads               | 28.7 us                                                      | 24.5 us: 1.17x faster                                            |
| async_tree_memoization   | 630 ms                                                       | 546 ms: 1.15x faster                                             |
| async_tree_none          | 519 ms                                                       | 452 ms: 1.15x faster                                             |
| nqueens                  | 103 ms                                                       | 89.5 ms: 1.15x faster                                            |
| comprehensions           | 24.6 us                                                      | 21.6 us: 1.14x faster                                            |
| async_tree_io            | 1.17 sec                                                     | 1.04 sec: 1.12x faster                                           |
| go                       | 164 ms                                                       | 147 ms: 1.12x faster                                             |
| mako                     | 11.0 ms                                                      | 9.93 ms: 1.11x faster                                            |
| logging_format           | 8.11 us                                                      | 7.35 us: 1.10x faster                                            |
| sqlglot_parse            | 1.53 ms                                                      | 1.40 ms: 1.10x faster                                            |
| mdp                      | 2.75 sec                                                     | 2.51 sec: 1.09x faster                                           |
| regex_compile            | 158 ms                                                       | 144 ms: 1.09x faster                                             |
| json                     | 5.65 ms                                                      | 5.19 ms: 1.09x faster                                            |
| sqlglot_normalize        | 126 ms                                                       | 116 ms: 1.09x faster                                             |
| nbody                    | 90.7 ms                                                      | 83.7 ms: 1.08x faster                                            |
| deepcopy                 | 399 us                                                       | 369 us: 1.08x faster                                             |
| deepcopy_memo            | 38.8 us                                                      | 36.0 us: 1.08x faster                                            |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 697 ms: 1.08x faster                                             |
| logging_silent           | 101 ns                                                       | 93.8 ns: 1.08x faster                                            |
| logging_simple           | 7.19 us                                                      | 6.73 us: 1.07x faster                                            |
| sqlglot_transpile        | 1.92 ms                                                      | 1.80 ms: 1.07x faster                                            |
| pycparser                | 1.32 sec                                                     | 1.24 sec: 1.07x faster                                           |
| xml_etree_parse          | 158 ms                                                       | 148 ms: 1.06x faster                                             |
| richards                 | 48.3 ms                                                      | 45.5 ms: 1.06x faster                                            |
| bench_thread_pool        | 1.01 ms                                                      | 960 us: 1.05x faster                                             |
| scimark_sor              | 111 ms                                                       | 107 ms: 1.04x faster                                             |
| sqlglot_optimize         | 59.8 ms                                                      | 57.5 ms: 1.04x faster                                            |
| dulwich_log              | 68.4 ms                                                      | 65.9 ms: 1.04x faster                                            |
| tomli_loads              | 2.26 sec                                                     | 2.19 sec: 1.03x faster                                           |
| deepcopy_reduce          | 3.51 us                                                      | 3.40 us: 1.03x faster                                            |
| raytrace                 | 317 ms                                                       | 307 ms: 1.03x faster                                             |
| crypto_pyaes             | 83.4 ms                                                      | 81.2 ms: 1.03x faster                                            |
| meteor_contest           | 131 ms                                                       | 127 ms: 1.03x faster                                             |
| spectral_norm            | 93.3 ms                                                      | 91.6 ms: 1.02x faster                                            |
| pyflate                  | 449 ms                                                       | 441 ms: 1.02x faster                                             |
| gc_traversal             | 3.85 ms                                                      | 3.79 ms: 1.01x faster                                            |
| regex_v8                 | 23.9 ms                                                      | 23.6 ms: 1.01x faster                                            |
| 2to3                     | 288 ms                                                       | 285 ms: 1.01x faster                                             |
| pprint_pformat           | 1.63 sec                                                     | 1.62 sec: 1.01x faster                                           |
| docutils                 | 2.86 sec                                                     | 2.88 sec: 1.01x slower                                           |
| pprint_safe_repr         | 784 ms                                                       | 792 ms: 1.01x slower                                             |
| pathlib                  | 19.1 ms                                                      | 19.3 ms: 1.01x slower                                            |
| pickle_dict              | 30.8 us                                                      | 31.2 us: 1.01x slower                                            |
| regex_effbot             | 3.50 ms                                                      | 3.55 ms: 1.01x slower                                            |
| scimark_monte_carlo      | 68.2 ms                                                      | 69.2 ms: 1.01x slower                                            |
| pickle_pure_python       | 319 us                                                       | 324 us: 1.01x slower                                             |
| pidigits                 | 251 ms                                                       | 259 ms: 1.03x slower                                             |
| telco                    | 6.86 ms                                                      | 7.08 ms: 1.03x slower                                            |
| unpickle_list            | 4.53 us                                                      | 4.71 us: 1.04x slower                                            |
| scimark_fft              | 285 ms                                                       | 296 ms: 1.04x slower                                             |
| xml_etree_process        | 56.5 ms                                                      | 58.8 ms: 1.04x slower                                            |
| pickle                   | 9.64 us                                                      | 10.0 us: 1.04x slower                                            |
| float                    | 74.2 ms                                                      | 77.3 ms: 1.04x slower                                            |
| coverage                 | 84.8 ms                                                      | 88.5 ms: 1.04x slower                                            |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.29 ms: 1.06x slower                                            |
| python_startup           | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                            |
| xml_etree_generate       | 80.5 ms                                                      | 85.6 ms: 1.06x slower                                            |
| regex_dna                | 227 ms                                                       | 245 ms: 1.08x slower                                             |
| sqlite_synth             | 2.50 us                                                      | 2.71 us: 1.09x slower                                            |
| unpickle                 | 13.4 us                                                      | 14.6 us: 1.09x slower                                            |
| python_startup_no_site   | 7.76 ms                                                      | 8.45 ms: 1.09x slower                                            |
| unpack_sequence          | 45.6 ns                                                      | 49.8 ns: 1.09x slower                                            |
| pickle_list              | 3.83 us                                                      | 4.27 us: 1.12x slower                                            |
| bench_mp_pool            | 4.62 ms                                                      | 5.41 ms: 1.17x slower                                            |
| async_generators         | 316 ms                                                       | 389 ms: 1.23x slower                                             |
| dask                     | 410 ms                                                       | 563 ms: 1.37x slower                                             |
| Geometric mean           | (ref)                                                        | 1.07x faster                                                     |

Benchmark hidden because not significant (4): tornado_http, xml_etree_iterparse, mypy2, create_gc_cycles
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
