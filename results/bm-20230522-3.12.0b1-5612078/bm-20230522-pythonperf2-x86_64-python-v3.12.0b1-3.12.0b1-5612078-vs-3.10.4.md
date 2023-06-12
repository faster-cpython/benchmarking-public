
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0b1
- machine: linux-x86_64
- commit hash: 5612078
- commit date: 2023-05-22
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                             |
| docutils       | 3.40 sec                                                     | 2.87 sec: 1.19x faster                                           |
| tornado_http   | 152 ms                                                       | 114 ms: 1.34x faster                                             |
| Geometric mean | (ref)                                                        | 1.25x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 85.9 ms: 1.60x faster                                            |
| float          | 110 ms                                                       | 79.1 ms: 1.39x faster                                            |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                        | 1.32x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 144 ms: 1.35x faster                                             |
| regex_v8       | 26.6 ms                                                      | 23.6 ms: 1.13x faster                                            |
| regex_dna      | 259 ms                                                       | 238 ms: 1.09x faster                                             |
| regex_effbot   | 2.99 ms                                                      | 3.46 ms: 1.16x slower                                            |
| Geometric mean | (ref)                                                        | 1.09x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 206 us: 1.55x faster                                             |
| pickle_pure_python   | 457 us                                                       | 322 us: 1.42x faster                                             |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.40x faster                                            |
| tomli_loads          | 2.97 sec                                                     | 2.13 sec: 1.39x faster                                           |
| xml_etree_process    | 76.0 ms                                                      | 59.2 ms: 1.28x faster                                            |
| json_loads           | 30.0 us                                                      | 24.0 us: 1.25x faster                                            |
| xml_etree_parse      | 162 ms                                                       | 148 ms: 1.09x faster                                             |
| xml_etree_generate   | 94.6 ms                                                      | 87.5 ms: 1.08x faster                                            |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                             |
| unpickle             | 14.2 us                                                      | 14.3 us: 1.01x slower                                            |
| pickle               | 9.94 us                                                      | 10.1 us: 1.02x slower                                            |
| unpickle_list        | 4.49 us                                                      | 4.67 us: 1.04x slower                                            |
| pickle_list          | 4.11 us                                                      | 4.31 us: 1.05x slower                                            |
| pickle_dict          | 30.0 us                                                      | 31.6 us: 1.05x slower                                            |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.32 ms                                                      | 8.50 ms: 1.16x slower                                            |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                     |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.0 ms: 1.46x faster                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 144 us: 3.62x faster                                             |
| deltablue                | 7.47 ms                                                      | 3.20 ms: 2.34x faster                                            |
| asyncio_tcp              | 782 ms                                                       | 379 ms: 2.06x faster                                             |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                           |
| logging_silent           | 166 ns                                                       | 90.6 ns: 1.83x faster                                            |
| richards_super           | 90.8 ms                                                      | 50.8 ms: 1.79x faster                                            |
| go                       | 259 ms                                                       | 145 ms: 1.78x faster                                             |
| chaos                    | 107 ms                                                       | 63.5 ms: 1.69x faster                                            |
| hexiom                   | 9.52 ms                                                      | 5.76 ms: 1.65x faster                                            |
| scimark_lu               | 164 ms                                                       | 99.1 ms: 1.65x faster                                            |
| generators               | 58.0 ms                                                      | 35.2 ms: 1.65x faster                                            |
| scimark_sor              | 177 ms                                                       | 108 ms: 1.64x faster                                             |
| sqlglot_parse            | 2.26 ms                                                      | 1.37 ms: 1.64x faster                                            |
| richards                 | 74.1 ms                                                      | 45.3 ms: 1.64x faster                                            |
| raytrace                 | 488 ms                                                       | 303 ms: 1.61x faster                                             |
| scimark_monte_carlo      | 109 ms                                                       | 68.5 ms: 1.60x faster                                            |
| nbody                    | 137 ms                                                       | 85.9 ms: 1.60x faster                                            |
| pyflate                  | 697 ms                                                       | 441 ms: 1.58x faster                                             |
| unpickle_pure_python     | 321 us                                                       | 206 us: 1.55x faster                                             |
| sqlglot_transpile        | 2.71 ms                                                      | 1.77 ms: 1.53x faster                                            |
| async_tree_none          | 700 ms                                                       | 456 ms: 1.53x faster                                             |
| spectral_norm            | 136 ms                                                       | 89.0 ms: 1.53x faster                                            |
| async_tree_io            | 1.61 sec                                                     | 1.06 sec: 1.52x faster                                           |
| async_tree_memoization   | 824 ms                                                       | 550 ms: 1.50x faster                                             |
| mako                     | 14.7 ms                                                      | 10.0 ms: 1.46x faster                                            |
| crypto_pyaes             | 118 ms                                                       | 82.1 ms: 1.44x faster                                            |
| pickle_pure_python       | 457 us                                                       | 322 us: 1.42x faster                                             |
| json_dumps               | 14.2 ms                                                      | 10.2 ms: 1.40x faster                                            |
| float                    | 110 ms                                                       | 79.1 ms: 1.39x faster                                            |
| tomli_loads              | 2.97 sec                                                     | 2.13 sec: 1.39x faster                                           |
| fannkuch                 | 496 ms                                                       | 358 ms: 1.39x faster                                             |
| pycparser                | 1.66 sec                                                     | 1.22 sec: 1.36x faster                                           |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 702 ms: 1.36x faster                                             |
| regex_compile            | 194 ms                                                       | 144 ms: 1.35x faster                                             |
| deepcopy_memo            | 48.9 us                                                      | 36.3 us: 1.34x faster                                            |
| coroutines               | 30.4 ms                                                      | 22.6 ms: 1.34x faster                                            |
| tornado_http             | 152 ms                                                       | 114 ms: 1.34x faster                                             |
| logging_simple           | 8.90 us                                                      | 6.65 us: 1.34x faster                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                           |
| logging_format           | 9.57 us                                                      | 7.26 us: 1.32x faster                                            |
| pprint_safe_repr         | 1.05 sec                                                     | 801 ms: 1.31x faster                                             |
| xml_etree_process        | 76.0 ms                                                      | 59.2 ms: 1.28x faster                                            |
| sqlglot_normalize        | 144 ms                                                       | 114 ms: 1.26x faster                                             |
| nqueens                  | 112 ms                                                       | 89.6 ms: 1.26x faster                                            |
| json_loads               | 30.0 us                                                      | 24.0 us: 1.25x faster                                            |
| comprehensions           | 26.9 us                                                      | 21.7 us: 1.24x faster                                            |
| dulwich_log              | 80.1 ms                                                      | 64.9 ms: 1.23x faster                                            |
| 2to3                     | 350 ms                                                       | 284 ms: 1.23x faster                                             |
| deepcopy                 | 454 us                                                       | 369 us: 1.23x faster                                             |
| sqlglot_optimize         | 70.3 ms                                                      | 57.2 ms: 1.23x faster                                            |
| mdp                      | 3.03 sec                                                     | 2.52 sec: 1.20x faster                                           |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.35 ms: 1.19x faster                                            |
| scimark_fft              | 359 ms                                                       | 302 ms: 1.19x faster                                             |
| deepcopy_reduce          | 4.03 us                                                      | 3.38 us: 1.19x faster                                            |
| docutils                 | 3.40 sec                                                     | 2.87 sec: 1.19x faster                                           |
| json                     | 5.96 ms                                                      | 5.05 ms: 1.18x faster                                            |
| bench_thread_pool        | 1.14 ms                                                      | 973 us: 1.17x faster                                             |
| unpack_sequence          | 59.5 ns                                                      | 51.8 ns: 1.15x faster                                            |
| regex_v8                 | 26.6 ms                                                      | 23.6 ms: 1.13x faster                                            |
| pathlib                  | 21.7 ms                                                      | 19.3 ms: 1.12x faster                                            |
| async_generators         | 422 ms                                                       | 382 ms: 1.10x faster                                             |
| sqlite_synth             | 2.97 us                                                      | 2.69 us: 1.10x faster                                            |
| xml_etree_parse          | 162 ms                                                       | 148 ms: 1.09x faster                                             |
| regex_dna                | 259 ms                                                       | 238 ms: 1.09x faster                                             |
| xml_etree_generate       | 94.6 ms                                                      | 87.5 ms: 1.08x faster                                            |
| meteor_contest           | 137 ms                                                       | 127 ms: 1.08x faster                                             |
| create_gc_cycles         | 1.82 ms                                                      | 1.69 ms: 1.08x faster                                            |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.04x faster                                             |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                             |
| unpickle                 | 14.2 us                                                      | 14.3 us: 1.01x slower                                            |
| pickle                   | 9.94 us                                                      | 10.1 us: 1.02x slower                                            |
| telco                    | 7.14 ms                                                      | 7.30 ms: 1.02x slower                                            |
| unpickle_list            | 4.49 us                                                      | 4.67 us: 1.04x slower                                            |
| pickle_list              | 4.11 us                                                      | 4.31 us: 1.05x slower                                            |
| pickle_dict              | 30.0 us                                                      | 31.6 us: 1.05x slower                                            |
| regex_effbot             | 2.99 ms                                                      | 3.46 ms: 1.16x slower                                            |
| python_startup_no_site   | 7.32 ms                                                      | 8.50 ms: 1.16x slower                                            |
| dask                     | 463 ms                                                       | 554 ms: 1.20x slower                                             |
| gc_traversal             | 3.45 ms                                                      | 4.23 ms: 1.22x slower                                            |
| coverage                 | 64.0 ms                                                      | 89.3 ms: 1.40x slower                                            |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                     |

Benchmark hidden because not significant (3): bench_mp_pool, mypy2, python_startup
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
