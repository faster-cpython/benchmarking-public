
# Results vs. 3.11.0

- fork: python
- ref: v3.12.0b1
- machine: linux-x86_64
- commit hash: 5612078
- commit date: 2023-05-22
- overall geometric mean: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 284 ms: 1.01x faster                                             |
| docutils       | 2.86 sec                                                     | 2.87 sec: 1.01x slower                                           |
| tornado_http   | 122 ms                                                       | 115 ms: 1.05x faster                                             |
| Geometric mean | (ref)                                                        | 1.02x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 84.7 ms: 1.07x faster                                            |
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                             |
| float          | 74.2 ms                                                      | 78.6 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 143 ms: 1.10x faster                                             |
| regex_v8       | 23.9 ms                                                      | 22.8 ms: 1.05x faster                                            |
| regex_dna      | 227 ms                                                       | 237 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                        | 1.02x faster                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.32x faster                                            |
| json_loads           | 28.7 us                                                      | 24.2 us: 1.18x faster                                            |
| unpickle_pure_python | 241 us                                                       | 204 us: 1.18x faster                                             |
| xml_etree_parse      | 158 ms                                                       | 147 ms: 1.08x faster                                             |
| tomli_loads          | 2.26 sec                                                     | 2.12 sec: 1.07x faster                                           |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.02x slower                                             |
| pickle_pure_python   | 319 us                                                       | 325 us: 1.02x slower                                             |
| unpickle_list        | 4.53 us                                                      | 4.72 us: 1.04x slower                                            |
| pickle               | 9.64 us                                                      | 10.1 us: 1.04x slower                                            |
| xml_etree_process    | 56.5 ms                                                      | 59.0 ms: 1.04x slower                                            |
| unpickle             | 13.4 us                                                      | 14.4 us: 1.08x slower                                            |
| xml_etree_generate   | 80.5 ms                                                      | 86.8 ms: 1.08x slower                                            |
| pickle_dict          | 30.8 us                                                      | 33.2 us: 1.08x slower                                            |
| pickle_list          | 3.83 us                                                      | 4.37 us: 1.14x slower                                            |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                            |
| python_startup_no_site | 7.76 ms                                                      | 8.50 ms: 1.10x slower                                            |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 9.94 ms: 1.11x faster                                            |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 149 us: 3.51x faster                                             |
| asyncio_tcp              | 753 ms                                                       | 380 ms: 1.98x faster                                             |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                           |
| generators               | 56.0 ms                                                      | 35.1 ms: 1.60x faster                                            |
| json_dumps               | 13.4 ms                                                      | 10.2 ms: 1.32x faster                                            |
| chaos                    | 80.9 ms                                                      | 64.0 ms: 1.26x faster                                            |
| deltablue                | 4.00 ms                                                      | 3.22 ms: 1.24x faster                                            |
| coroutines               | 27.6 ms                                                      | 22.3 ms: 1.23x faster                                            |
| hexiom                   | 7.13 ms                                                      | 5.88 ms: 1.21x faster                                            |
| fannkuch                 | 429 ms                                                       | 355 ms: 1.21x faster                                             |
| richards_super           | 61.0 ms                                                      | 51.1 ms: 1.19x faster                                            |
| json_loads               | 28.7 us                                                      | 24.2 us: 1.18x faster                                            |
| unpickle_pure_python     | 241 us                                                       | 204 us: 1.18x faster                                             |
| scimark_lu               | 115 ms                                                       | 98.0 ms: 1.17x faster                                            |
| async_tree_memoization   | 630 ms                                                       | 544 ms: 1.16x faster                                             |
| async_tree_none          | 519 ms                                                       | 453 ms: 1.15x faster                                             |
| comprehensions           | 24.6 us                                                      | 21.6 us: 1.14x faster                                            |
| nqueens                  | 103 ms                                                       | 90.2 ms: 1.14x faster                                            |
| logging_format           | 8.11 us                                                      | 7.14 us: 1.14x faster                                            |
| async_tree_io            | 1.17 sec                                                     | 1.05 sec: 1.12x faster                                           |
| go                       | 164 ms                                                       | 148 ms: 1.11x faster                                             |
| sqlglot_parse            | 1.53 ms                                                      | 1.38 ms: 1.11x faster                                            |
| mako                     | 11.0 ms                                                      | 9.94 ms: 1.11x faster                                            |
| regex_compile            | 158 ms                                                       | 143 ms: 1.10x faster                                             |
| sqlglot_normalize        | 126 ms                                                       | 115 ms: 1.10x faster                                             |
| json                     | 5.65 ms                                                      | 5.16 ms: 1.09x faster                                            |
| logging_simple           | 7.19 us                                                      | 6.60 us: 1.09x faster                                            |
| mdp                      | 2.75 sec                                                     | 2.53 sec: 1.09x faster                                           |
| logging_silent           | 101 ns                                                       | 93.0 ns: 1.08x faster                                            |
| deepcopy                 | 399 us                                                       | 370 us: 1.08x faster                                             |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 696 ms: 1.08x faster                                             |
| xml_etree_parse          | 158 ms                                                       | 147 ms: 1.08x faster                                             |
| sqlglot_transpile        | 1.92 ms                                                      | 1.79 ms: 1.07x faster                                            |
| richards                 | 48.3 ms                                                      | 45.0 ms: 1.07x faster                                            |
| bench_thread_pool        | 1.01 ms                                                      | 943 us: 1.07x faster                                             |
| nbody                    | 90.7 ms                                                      | 84.7 ms: 1.07x faster                                            |
| raytrace                 | 317 ms                                                       | 297 ms: 1.07x faster                                             |
| tomli_loads              | 2.26 sec                                                     | 2.12 sec: 1.07x faster                                           |
| deepcopy_memo            | 38.8 us                                                      | 36.5 us: 1.06x faster                                            |
| tornado_http             | 122 ms                                                       | 115 ms: 1.05x faster                                             |
| regex_v8                 | 23.9 ms                                                      | 22.8 ms: 1.05x faster                                            |
| sqlglot_optimize         | 59.8 ms                                                      | 57.2 ms: 1.05x faster                                            |
| pycparser                | 1.32 sec                                                     | 1.27 sec: 1.05x faster                                           |
| deepcopy_reduce          | 3.51 us                                                      | 3.37 us: 1.04x faster                                            |
| dulwich_log              | 68.4 ms                                                      | 66.1 ms: 1.04x faster                                            |
| meteor_contest           | 131 ms                                                       | 127 ms: 1.03x faster                                             |
| scimark_sor              | 111 ms                                                       | 109 ms: 1.02x faster                                             |
| gc_traversal             | 3.85 ms                                                      | 3.79 ms: 1.02x faster                                            |
| 2to3                     | 288 ms                                                       | 284 ms: 1.01x faster                                             |
| pyflate                  | 449 ms                                                       | 443 ms: 1.01x faster                                             |
| crypto_pyaes             | 83.4 ms                                                      | 82.5 ms: 1.01x faster                                            |
| docutils                 | 2.86 sec                                                     | 2.87 sec: 1.01x slower                                           |
| pathlib                  | 19.1 ms                                                      | 19.3 ms: 1.01x slower                                            |
| pprint_pformat           | 1.63 sec                                                     | 1.65 sec: 1.01x slower                                           |
| spectral_norm            | 93.3 ms                                                      | 94.5 ms: 1.01x slower                                            |
| xml_etree_iterparse      | 104 ms                                                       | 106 ms: 1.02x slower                                             |
| pickle_pure_python       | 319 us                                                       | 325 us: 1.02x slower                                             |
| pprint_safe_repr         | 784 ms                                                       | 809 ms: 1.03x slower                                             |
| telco                    | 6.86 ms                                                      | 7.11 ms: 1.04x slower                                            |
| coverage                 | 84.8 ms                                                      | 88.0 ms: 1.04x slower                                            |
| pidigits                 | 251 ms                                                       | 261 ms: 1.04x slower                                             |
| unpickle_list            | 4.53 us                                                      | 4.72 us: 1.04x slower                                            |
| create_gc_cycles         | 1.61 ms                                                      | 1.68 ms: 1.04x slower                                            |
| pickle                   | 9.64 us                                                      | 10.1 us: 1.04x slower                                            |
| xml_etree_process        | 56.5 ms                                                      | 59.0 ms: 1.04x slower                                            |
| regex_dna                | 227 ms                                                       | 237 ms: 1.05x slower                                             |
| unpack_sequence          | 45.6 ns                                                      | 48.1 ns: 1.05x slower                                            |
| float                    | 74.2 ms                                                      | 78.6 ms: 1.06x slower                                            |
| scimark_fft              | 285 ms                                                       | 305 ms: 1.07x slower                                             |
| python_startup           | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                            |
| sqlite_synth             | 2.50 us                                                      | 2.68 us: 1.07x slower                                            |
| unpickle                 | 13.4 us                                                      | 14.4 us: 1.08x slower                                            |
| xml_etree_generate       | 80.5 ms                                                      | 86.8 ms: 1.08x slower                                            |
| pickle_dict              | 30.8 us                                                      | 33.2 us: 1.08x slower                                            |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.38 ms: 1.08x slower                                            |
| python_startup_no_site   | 7.76 ms                                                      | 8.50 ms: 1.10x slower                                            |
| pickle_list              | 3.83 us                                                      | 4.37 us: 1.14x slower                                            |
| async_generators         | 316 ms                                                       | 379 ms: 1.20x slower                                             |
| dask                     | 410 ms                                                       | 551 ms: 1.34x slower                                             |
| bench_mp_pool            | 4.62 ms                                                      | 8.65 ms: 1.87x slower                                            |
| Geometric mean           | (ref)                                                        | 1.07x faster                                                     |

Benchmark hidden because not significant (3): regex_effbot, scimark_monte_carlo, mypy2
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
