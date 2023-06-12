
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
| docutils       | 3.40 sec                                                     | 2.87 sec: 1.18x faster                                           |
| tornado_http   | 152 ms                                                       | 115 ms: 1.32x faster                                             |
| Geometric mean | (ref)                                                        | 1.24x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 84.7 ms: 1.62x faster                                            |
| float          | 110 ms                                                       | 78.6 ms: 1.40x faster                                            |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                        | 1.33x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 143 ms: 1.35x faster                                             |
| regex_v8       | 26.6 ms                                                      | 22.8 ms: 1.17x faster                                            |
| regex_dna      | 259 ms                                                       | 237 ms: 1.09x faster                                             |
| regex_effbot   | 2.99 ms                                                      | 3.49 ms: 1.17x slower                                            |
| Geometric mean | (ref)                                                        | 1.10x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 204 us: 1.58x faster                                             |
| pickle_pure_python   | 457 us                                                       | 325 us: 1.41x faster                                             |
| tomli_loads          | 2.97 sec                                                     | 2.12 sec: 1.40x faster                                           |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.40x faster                                            |
| xml_etree_process    | 76.0 ms                                                      | 59.0 ms: 1.29x faster                                            |
| json_loads           | 30.0 us                                                      | 24.2 us: 1.24x faster                                            |
| xml_etree_parse      | 162 ms                                                       | 147 ms: 1.10x faster                                             |
| xml_etree_generate   | 94.6 ms                                                      | 86.8 ms: 1.09x faster                                            |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                             |
| pickle               | 9.94 us                                                      | 10.1 us: 1.01x slower                                            |
| unpickle             | 14.2 us                                                      | 14.4 us: 1.02x slower                                            |
| unpickle_list        | 4.49 us                                                      | 4.72 us: 1.05x slower                                            |
| pickle_list          | 4.11 us                                                      | 4.37 us: 1.06x slower                                            |
| pickle_dict          | 30.0 us                                                      | 33.2 us: 1.11x slower                                            |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.5 ms: 1.00x slower                                            |
| python_startup_no_site | 7.32 ms                                                      | 8.50 ms: 1.16x slower                                            |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 9.94 ms: 1.48x faster                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 149 us: 3.51x faster                                             |
| deltablue                | 7.47 ms                                                      | 3.22 ms: 2.32x faster                                            |
| asyncio_tcp              | 782 ms                                                       | 380 ms: 2.06x faster                                             |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                           |
| logging_silent           | 166 ns                                                       | 93.0 ns: 1.78x faster                                            |
| richards_super           | 90.8 ms                                                      | 51.1 ms: 1.78x faster                                            |
| go                       | 259 ms                                                       | 148 ms: 1.75x faster                                             |
| chaos                    | 107 ms                                                       | 64.0 ms: 1.67x faster                                            |
| scimark_lu               | 164 ms                                                       | 98.0 ms: 1.67x faster                                            |
| generators               | 58.0 ms                                                      | 35.1 ms: 1.65x faster                                            |
| raytrace                 | 488 ms                                                       | 297 ms: 1.65x faster                                             |
| richards                 | 74.1 ms                                                      | 45.0 ms: 1.64x faster                                            |
| sqlglot_parse            | 2.26 ms                                                      | 1.38 ms: 1.63x faster                                            |
| scimark_sor              | 177 ms                                                       | 109 ms: 1.62x faster                                             |
| nbody                    | 137 ms                                                       | 84.7 ms: 1.62x faster                                            |
| hexiom                   | 9.52 ms                                                      | 5.88 ms: 1.62x faster                                            |
| scimark_monte_carlo      | 109 ms                                                       | 68.2 ms: 1.60x faster                                            |
| unpickle_pure_python     | 321 us                                                       | 204 us: 1.58x faster                                             |
| pyflate                  | 697 ms                                                       | 443 ms: 1.57x faster                                             |
| async_tree_none          | 700 ms                                                       | 453 ms: 1.55x faster                                             |
| async_tree_io            | 1.61 sec                                                     | 1.05 sec: 1.54x faster                                           |
| sqlglot_transpile        | 2.71 ms                                                      | 1.79 ms: 1.52x faster                                            |
| async_tree_memoization   | 824 ms                                                       | 544 ms: 1.51x faster                                             |
| mako                     | 14.7 ms                                                      | 9.94 ms: 1.48x faster                                            |
| spectral_norm            | 136 ms                                                       | 94.5 ms: 1.44x faster                                            |
| crypto_pyaes             | 118 ms                                                       | 82.5 ms: 1.43x faster                                            |
| pickle_pure_python       | 457 us                                                       | 325 us: 1.41x faster                                             |
| float                    | 110 ms                                                       | 78.6 ms: 1.40x faster                                            |
| tomli_loads              | 2.97 sec                                                     | 2.12 sec: 1.40x faster                                           |
| json_dumps               | 14.2 ms                                                      | 10.2 ms: 1.40x faster                                            |
| fannkuch                 | 496 ms                                                       | 355 ms: 1.40x faster                                             |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 696 ms: 1.37x faster                                             |
| coroutines               | 30.4 ms                                                      | 22.3 ms: 1.36x faster                                            |
| regex_compile            | 194 ms                                                       | 143 ms: 1.35x faster                                             |
| logging_simple           | 8.90 us                                                      | 6.60 us: 1.35x faster                                            |
| logging_format           | 9.57 us                                                      | 7.14 us: 1.34x faster                                            |
| deepcopy_memo            | 48.9 us                                                      | 36.5 us: 1.34x faster                                            |
| tornado_http             | 152 ms                                                       | 115 ms: 1.32x faster                                             |
| pycparser                | 1.66 sec                                                     | 1.27 sec: 1.31x faster                                           |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                           |
| pprint_safe_repr         | 1.05 sec                                                     | 809 ms: 1.30x faster                                             |
| xml_etree_process        | 76.0 ms                                                      | 59.0 ms: 1.29x faster                                            |
| sqlglot_normalize        | 144 ms                                                       | 115 ms: 1.26x faster                                             |
| comprehensions           | 26.9 us                                                      | 21.6 us: 1.25x faster                                            |
| nqueens                  | 112 ms                                                       | 90.2 ms: 1.25x faster                                            |
| unpack_sequence          | 59.5 ns                                                      | 48.1 ns: 1.24x faster                                            |
| json_loads               | 30.0 us                                                      | 24.2 us: 1.24x faster                                            |
| 2to3                     | 350 ms                                                       | 284 ms: 1.23x faster                                             |
| sqlglot_optimize         | 70.3 ms                                                      | 57.2 ms: 1.23x faster                                            |
| deepcopy                 | 454 us                                                       | 370 us: 1.23x faster                                             |
| dulwich_log              | 80.1 ms                                                      | 66.1 ms: 1.21x faster                                            |
| bench_thread_pool        | 1.14 ms                                                      | 943 us: 1.20x faster                                             |
| mdp                      | 3.03 sec                                                     | 2.53 sec: 1.20x faster                                           |
| deepcopy_reduce          | 4.03 us                                                      | 3.37 us: 1.19x faster                                            |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.38 ms: 1.19x faster                                            |
| docutils                 | 3.40 sec                                                     | 2.87 sec: 1.18x faster                                           |
| scimark_fft              | 359 ms                                                       | 305 ms: 1.18x faster                                             |
| regex_v8                 | 26.6 ms                                                      | 22.8 ms: 1.17x faster                                            |
| json                     | 5.96 ms                                                      | 5.16 ms: 1.15x faster                                            |
| pathlib                  | 21.7 ms                                                      | 19.3 ms: 1.13x faster                                            |
| async_generators         | 422 ms                                                       | 379 ms: 1.11x faster                                             |
| sqlite_synth             | 2.97 us                                                      | 2.68 us: 1.11x faster                                            |
| xml_etree_parse          | 162 ms                                                       | 147 ms: 1.10x faster                                             |
| regex_dna                | 259 ms                                                       | 237 ms: 1.09x faster                                             |
| xml_etree_generate       | 94.6 ms                                                      | 86.8 ms: 1.09x faster                                            |
| create_gc_cycles         | 1.82 ms                                                      | 1.68 ms: 1.09x faster                                            |
| meteor_contest           | 137 ms                                                       | 127 ms: 1.08x faster                                             |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.04x faster                                             |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                             |
| python_startup           | 11.5 ms                                                      | 11.5 ms: 1.00x slower                                            |
| pickle                   | 9.94 us                                                      | 10.1 us: 1.01x slower                                            |
| unpickle                 | 14.2 us                                                      | 14.4 us: 1.02x slower                                            |
| unpickle_list            | 4.49 us                                                      | 4.72 us: 1.05x slower                                            |
| pickle_list              | 4.11 us                                                      | 4.37 us: 1.06x slower                                            |
| gc_traversal             | 3.45 ms                                                      | 3.79 ms: 1.10x slower                                            |
| pickle_dict              | 30.0 us                                                      | 33.2 us: 1.11x slower                                            |
| python_startup_no_site   | 7.32 ms                                                      | 8.50 ms: 1.16x slower                                            |
| regex_effbot             | 2.99 ms                                                      | 3.49 ms: 1.17x slower                                            |
| dask                     | 463 ms                                                       | 551 ms: 1.19x slower                                             |
| bench_mp_pool            | 7.18 ms                                                      | 8.65 ms: 1.20x slower                                            |
| coverage                 | 64.0 ms                                                      | 88.0 ms: 1.38x slower                                            |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                     |

Benchmark hidden because not significant (2): mypy2, telco
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
