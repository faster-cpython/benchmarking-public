
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
| docutils       | 2.86 sec                                                     | 2.87 sec: 1.00x slower                                           |
| tornado_http   | 122 ms                                                       | 114 ms: 1.07x faster                                             |
| Geometric mean | (ref)                                                        | 1.03x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 85.9 ms: 1.06x faster                                            |
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                             |
| float          | 74.2 ms                                                      | 79.1 ms: 1.07x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 144 ms: 1.10x faster                                             |
| regex_v8       | 23.9 ms                                                      | 23.6 ms: 1.01x faster                                            |
| regex_effbot   | 3.50 ms                                                      | 3.46 ms: 1.01x faster                                            |
| regex_dna      | 227 ms                                                       | 238 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                        | 1.02x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.32x faster                                            |
| json_loads           | 28.7 us                                                      | 24.0 us: 1.20x faster                                            |
| unpickle_pure_python | 241 us                                                       | 206 us: 1.17x faster                                             |
| xml_etree_parse      | 158 ms                                                       | 148 ms: 1.07x faster                                             |
| tomli_loads          | 2.26 sec                                                     | 2.13 sec: 1.06x faster                                           |
| pickle_pure_python   | 319 us                                                       | 322 us: 1.01x slower                                             |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.02x slower                                             |
| pickle_dict          | 30.8 us                                                      | 31.6 us: 1.03x slower                                            |
| unpickle_list        | 4.53 us                                                      | 4.67 us: 1.03x slower                                            |
| xml_etree_process    | 56.5 ms                                                      | 59.2 ms: 1.05x slower                                            |
| pickle               | 9.64 us                                                      | 10.1 us: 1.05x slower                                            |
| unpickle             | 13.4 us                                                      | 14.3 us: 1.06x slower                                            |
| xml_etree_generate   | 80.5 ms                                                      | 87.5 ms: 1.09x slower                                            |
| pickle_list          | 3.83 us                                                      | 4.31 us: 1.13x slower                                            |
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
| mako      | 11.0 ms                                                      | 10.0 ms: 1.09x faster                                            |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 144 us: 3.62x faster                                             |
| asyncio_tcp              | 753 ms                                                       | 379 ms: 1.99x faster                                             |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.97x faster                                           |
| generators               | 56.0 ms                                                      | 35.2 ms: 1.59x faster                                            |
| json_dumps               | 13.4 ms                                                      | 10.2 ms: 1.32x faster                                            |
| chaos                    | 80.9 ms                                                      | 63.5 ms: 1.27x faster                                            |
| deltablue                | 4.00 ms                                                      | 3.20 ms: 1.25x faster                                            |
| hexiom                   | 7.13 ms                                                      | 5.76 ms: 1.24x faster                                            |
| coroutines               | 27.6 ms                                                      | 22.6 ms: 1.22x faster                                            |
| richards_super           | 61.0 ms                                                      | 50.8 ms: 1.20x faster                                            |
| fannkuch                 | 429 ms                                                       | 358 ms: 1.20x faster                                             |
| json_loads               | 28.7 us                                                      | 24.0 us: 1.20x faster                                            |
| unpickle_pure_python     | 241 us                                                       | 206 us: 1.17x faster                                             |
| scimark_lu               | 115 ms                                                       | 99.1 ms: 1.16x faster                                            |
| nqueens                  | 103 ms                                                       | 89.6 ms: 1.15x faster                                            |
| async_tree_memoization   | 630 ms                                                       | 550 ms: 1.15x faster                                             |
| async_tree_none          | 519 ms                                                       | 456 ms: 1.14x faster                                             |
| comprehensions           | 24.6 us                                                      | 21.7 us: 1.14x faster                                            |
| go                       | 164 ms                                                       | 145 ms: 1.13x faster                                             |
| json                     | 5.65 ms                                                      | 5.05 ms: 1.12x faster                                            |
| logging_format           | 8.11 us                                                      | 7.26 us: 1.12x faster                                            |
| sqlglot_parse            | 1.53 ms                                                      | 1.37 ms: 1.11x faster                                            |
| logging_silent           | 101 ns                                                       | 90.6 ns: 1.11x faster                                            |
| async_tree_io            | 1.17 sec                                                     | 1.06 sec: 1.11x faster                                           |
| sqlglot_normalize        | 126 ms                                                       | 114 ms: 1.10x faster                                             |
| regex_compile            | 158 ms                                                       | 144 ms: 1.10x faster                                             |
| mako                     | 11.0 ms                                                      | 10.0 ms: 1.09x faster                                            |
| mdp                      | 2.75 sec                                                     | 2.52 sec: 1.09x faster                                           |
| sqlglot_transpile        | 1.92 ms                                                      | 1.77 ms: 1.09x faster                                            |
| pycparser                | 1.32 sec                                                     | 1.22 sec: 1.09x faster                                           |
| deepcopy                 | 399 us                                                       | 369 us: 1.08x faster                                             |
| logging_simple           | 7.19 us                                                      | 6.65 us: 1.08x faster                                            |
| tornado_http             | 122 ms                                                       | 114 ms: 1.07x faster                                             |
| deepcopy_memo            | 38.8 us                                                      | 36.3 us: 1.07x faster                                            |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 702 ms: 1.07x faster                                             |
| xml_etree_parse          | 158 ms                                                       | 148 ms: 1.07x faster                                             |
| richards                 | 48.3 ms                                                      | 45.3 ms: 1.07x faster                                            |
| tomli_loads              | 2.26 sec                                                     | 2.13 sec: 1.06x faster                                           |
| nbody                    | 90.7 ms                                                      | 85.9 ms: 1.06x faster                                            |
| dulwich_log              | 68.4 ms                                                      | 64.9 ms: 1.05x faster                                            |
| spectral_norm            | 93.3 ms                                                      | 89.0 ms: 1.05x faster                                            |
| sqlglot_optimize         | 59.8 ms                                                      | 57.2 ms: 1.05x faster                                            |
| raytrace                 | 317 ms                                                       | 303 ms: 1.05x faster                                             |
| bench_thread_pool        | 1.01 ms                                                      | 973 us: 1.04x faster                                             |
| deepcopy_reduce          | 3.51 us                                                      | 3.38 us: 1.04x faster                                            |
| scimark_sor              | 111 ms                                                       | 108 ms: 1.03x faster                                             |
| meteor_contest           | 131 ms                                                       | 127 ms: 1.03x faster                                             |
| crypto_pyaes             | 83.4 ms                                                      | 82.1 ms: 1.02x faster                                            |
| pyflate                  | 449 ms                                                       | 441 ms: 1.02x faster                                             |
| regex_v8                 | 23.9 ms                                                      | 23.6 ms: 1.01x faster                                            |
| 2to3                     | 288 ms                                                       | 284 ms: 1.01x faster                                             |
| regex_effbot             | 3.50 ms                                                      | 3.46 ms: 1.01x faster                                            |
| scimark_monte_carlo      | 68.2 ms                                                      | 68.5 ms: 1.00x slower                                            |
| docutils                 | 2.86 sec                                                     | 2.87 sec: 1.00x slower                                           |
| pickle_pure_python       | 319 us                                                       | 322 us: 1.01x slower                                             |
| pathlib                  | 19.1 ms                                                      | 19.3 ms: 1.01x slower                                            |
| xml_etree_iterparse      | 104 ms                                                       | 106 ms: 1.02x slower                                             |
| pprint_safe_repr         | 784 ms                                                       | 801 ms: 1.02x slower                                             |
| pickle_dict              | 30.8 us                                                      | 31.6 us: 1.03x slower                                            |
| unpickle_list            | 4.53 us                                                      | 4.67 us: 1.03x slower                                            |
| pidigits                 | 251 ms                                                       | 261 ms: 1.04x slower                                             |
| xml_etree_process        | 56.5 ms                                                      | 59.2 ms: 1.05x slower                                            |
| regex_dna                | 227 ms                                                       | 238 ms: 1.05x slower                                             |
| pickle                   | 9.64 us                                                      | 10.1 us: 1.05x slower                                            |
| create_gc_cycles         | 1.61 ms                                                      | 1.69 ms: 1.05x slower                                            |
| coverage                 | 84.8 ms                                                      | 89.3 ms: 1.05x slower                                            |
| scimark_fft              | 285 ms                                                       | 302 ms: 1.06x slower                                             |
| telco                    | 6.86 ms                                                      | 7.30 ms: 1.06x slower                                            |
| unpickle                 | 13.4 us                                                      | 14.3 us: 1.06x slower                                            |
| float                    | 74.2 ms                                                      | 79.1 ms: 1.07x slower                                            |
| python_startup           | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                            |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.35 ms: 1.07x slower                                            |
| sqlite_synth             | 2.50 us                                                      | 2.69 us: 1.08x slower                                            |
| xml_etree_generate       | 80.5 ms                                                      | 87.5 ms: 1.09x slower                                            |
| python_startup_no_site   | 7.76 ms                                                      | 8.50 ms: 1.10x slower                                            |
| gc_traversal             | 3.85 ms                                                      | 4.23 ms: 1.10x slower                                            |
| pickle_list              | 3.83 us                                                      | 4.31 us: 1.13x slower                                            |
| unpack_sequence          | 45.6 ns                                                      | 51.8 ns: 1.14x slower                                            |
| async_generators         | 316 ms                                                       | 382 ms: 1.21x slower                                             |
| dask                     | 410 ms                                                       | 554 ms: 1.35x slower                                             |
| bench_mp_pool            | 4.62 ms                                                      | 6.56 ms: 1.42x slower                                            |
| Geometric mean           | (ref)                                                        | 1.07x faster                                                     |

Benchmark hidden because not significant (2): pprint_pformat, mypy2
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
