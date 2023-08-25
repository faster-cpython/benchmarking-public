
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 0e5eee0
- commit date: 2023-08-20
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-pythonperf2-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.22x faster                                          |
| docutils       | 3.40 sec                                                     | 2.90 sec: 1.17x faster                                        |
| tornado_http   | 152 ms                                                       | 121 ms: 1.26x faster                                          |
| Geometric mean | (ref)                                                        | 1.22x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-pythonperf2-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 87.5 ms: 1.57x faster                                         |
| float          | 110 ms                                                       | 78.5 ms: 1.41x faster                                         |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                          |
| Geometric mean | (ref)                                                        | 1.32x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-pythonperf2-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 144 ms: 1.34x faster                                          |
| regex_v8       | 26.6 ms                                                      | 23.9 ms: 1.11x faster                                         |
| regex_dna      | 259 ms                                                       | 242 ms: 1.07x faster                                          |
| regex_effbot   | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                         |
| Geometric mean | (ref)                                                        | 1.08x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-pythonperf2-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 205 us: 1.56x faster                                          |
| pickle_pure_python   | 457 us                                                       | 322 us: 1.42x faster                                          |
| tomli_loads          | 2.97 sec                                                     | 2.18 sec: 1.36x faster                                        |
| json_dumps           | 14.2 ms                                                      | 10.4 ms: 1.36x faster                                         |
| xml_etree_process    | 76.0 ms                                                      | 59.1 ms: 1.29x faster                                         |
| json_loads           | 30.0 us                                                      | 24.5 us: 1.22x faster                                         |
| xml_etree_parse      | 162 ms                                                       | 146 ms: 1.11x faster                                          |
| xml_etree_generate   | 94.6 ms                                                      | 86.3 ms: 1.10x faster                                         |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                          |
| unpickle             | 14.2 us                                                      | 14.3 us: 1.01x slower                                         |
| pickle               | 9.94 us                                                      | 10.0 us: 1.01x slower                                         |
| pickle_list          | 4.11 us                                                      | 4.23 us: 1.03x slower                                         |
| unpickle_list        | 4.49 us                                                      | 4.69 us: 1.04x slower                                         |
| pickle_dict          | 30.0 us                                                      | 31.5 us: 1.05x slower                                         |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-pythonperf2-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 7.32 ms                                                      | 8.49 ms: 1.16x slower                                         |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                  |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-pythonperf2-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 9.99 ms: 1.47x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-pythonperf2-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 150 us: 3.49x faster                                          |
| deltablue                | 7.47 ms                                                      | 3.18 ms: 2.35x faster                                         |
| asyncio_tcp              | 782 ms                                                       | 383 ms: 2.05x faster                                          |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                        |
| go                       | 259 ms                                                       | 145 ms: 1.79x faster                                          |
| richards_super           | 90.8 ms                                                      | 51.5 ms: 1.76x faster                                         |
| logging_silent           | 166 ns                                                       | 95.7 ns: 1.73x faster                                         |
| chaos                    | 107 ms                                                       | 62.7 ms: 1.71x faster                                         |
| scimark_lu               | 164 ms                                                       | 97.9 ms: 1.67x faster                                         |
| richards                 | 74.1 ms                                                      | 44.4 ms: 1.67x faster                                         |
| hexiom                   | 9.52 ms                                                      | 5.79 ms: 1.64x faster                                         |
| raytrace                 | 488 ms                                                       | 299 ms: 1.63x faster                                          |
| sqlglot_parse            | 2.26 ms                                                      | 1.38 ms: 1.63x faster                                         |
| scimark_sor              | 177 ms                                                       | 109 ms: 1.63x faster                                          |
| generators               | 58.0 ms                                                      | 36.5 ms: 1.59x faster                                         |
| scimark_monte_carlo      | 109 ms                                                       | 68.9 ms: 1.59x faster                                         |
| pyflate                  | 697 ms                                                       | 442 ms: 1.58x faster                                          |
| nbody                    | 137 ms                                                       | 87.5 ms: 1.57x faster                                         |
| unpickle_pure_python     | 321 us                                                       | 205 us: 1.56x faster                                          |
| async_tree_none          | 700 ms                                                       | 459 ms: 1.52x faster                                          |
| sqlglot_transpile        | 2.71 ms                                                      | 1.78 ms: 1.52x faster                                         |
| async_tree_io            | 1.61 sec                                                     | 1.06 sec: 1.52x faster                                        |
| async_tree_memoization   | 824 ms                                                       | 553 ms: 1.49x faster                                          |
| spectral_norm            | 136 ms                                                       | 92.6 ms: 1.47x faster                                         |
| mako                     | 14.7 ms                                                      | 9.99 ms: 1.47x faster                                         |
| fannkuch                 | 496 ms                                                       | 342 ms: 1.45x faster                                          |
| crypto_pyaes             | 118 ms                                                       | 81.7 ms: 1.45x faster                                         |
| bench_mp_pool            | 7.18 ms                                                      | 4.98 ms: 1.44x faster                                         |
| pickle_pure_python       | 457 us                                                       | 322 us: 1.42x faster                                          |
| float                    | 110 ms                                                       | 78.5 ms: 1.41x faster                                         |
| tomli_loads              | 2.97 sec                                                     | 2.18 sec: 1.36x faster                                        |
| json_dumps               | 14.2 ms                                                      | 10.4 ms: 1.36x faster                                         |
| coroutines               | 30.4 ms                                                      | 22.4 ms: 1.36x faster                                         |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 704 ms: 1.35x faster                                          |
| regex_compile            | 194 ms                                                       | 144 ms: 1.34x faster                                          |
| logging_simple           | 8.90 us                                                      | 6.67 us: 1.33x faster                                         |
| pycparser                | 1.66 sec                                                     | 1.26 sec: 1.32x faster                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.31x faster                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 807 ms: 1.30x faster                                          |
| logging_format           | 9.57 us                                                      | 7.42 us: 1.29x faster                                         |
| deepcopy_memo            | 48.9 us                                                      | 38.0 us: 1.29x faster                                         |
| xml_etree_process        | 76.0 ms                                                      | 59.1 ms: 1.29x faster                                         |
| mypy2                    | 466 ms                                                       | 366 ms: 1.28x faster                                          |
| tornado_http             | 152 ms                                                       | 121 ms: 1.26x faster                                          |
| comprehensions           | 26.9 us                                                      | 21.6 us: 1.25x faster                                         |
| nqueens                  | 112 ms                                                       | 90.1 ms: 1.25x faster                                         |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                          |
| json_loads               | 30.0 us                                                      | 24.5 us: 1.22x faster                                         |
| 2to3                     | 350 ms                                                       | 286 ms: 1.22x faster                                          |
| sqlglot_optimize         | 70.3 ms                                                      | 57.8 ms: 1.22x faster                                         |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.32 ms: 1.20x faster                                         |
| scimark_fft              | 359 ms                                                       | 299 ms: 1.20x faster                                          |
| mdp                      | 3.03 sec                                                     | 2.52 sec: 1.20x faster                                        |
| dulwich_log              | 80.1 ms                                                      | 66.6 ms: 1.20x faster                                         |
| deepcopy                 | 454 us                                                       | 379 us: 1.20x faster                                          |
| bench_thread_pool        | 1.14 ms                                                      | 957 us: 1.19x faster                                          |
| docutils                 | 3.40 sec                                                     | 2.90 sec: 1.17x faster                                        |
| json                     | 5.96 ms                                                      | 5.08 ms: 1.17x faster                                         |
| deepcopy_reduce          | 4.03 us                                                      | 3.49 us: 1.15x faster                                         |
| pathlib                  | 21.7 ms                                                      | 19.2 ms: 1.13x faster                                         |
| create_gc_cycles         | 1.82 ms                                                      | 1.62 ms: 1.12x faster                                         |
| regex_v8                 | 26.6 ms                                                      | 23.9 ms: 1.11x faster                                         |
| xml_etree_parse          | 162 ms                                                       | 146 ms: 1.11x faster                                          |
| xml_etree_generate       | 94.6 ms                                                      | 86.3 ms: 1.10x faster                                         |
| unpack_sequence          | 59.5 ns                                                      | 54.5 ns: 1.09x faster                                         |
| sqlite_synth             | 2.97 us                                                      | 2.72 us: 1.09x faster                                         |
| meteor_contest           | 137 ms                                                       | 126 ms: 1.09x faster                                          |
| async_generators         | 422 ms                                                       | 391 ms: 1.08x faster                                          |
| regex_dna                | 259 ms                                                       | 242 ms: 1.07x faster                                          |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.06x faster                                          |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                          |
| telco                    | 7.14 ms                                                      | 7.09 ms: 1.01x faster                                         |
| unpickle                 | 14.2 us                                                      | 14.3 us: 1.01x slower                                         |
| pickle                   | 9.94 us                                                      | 10.0 us: 1.01x slower                                         |
| pickle_list              | 4.11 us                                                      | 4.23 us: 1.03x slower                                         |
| gc_traversal             | 3.45 ms                                                      | 3.59 ms: 1.04x slower                                         |
| unpickle_list            | 4.49 us                                                      | 4.69 us: 1.04x slower                                         |
| pickle_dict              | 30.0 us                                                      | 31.5 us: 1.05x slower                                         |
| python_startup_no_site   | 7.32 ms                                                      | 8.49 ms: 1.16x slower                                         |
| regex_effbot             | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                         |
| dask                     | 463 ms                                                       | 569 ms: 1.23x slower                                          |
| coverage                 | 64.0 ms                                                      | 89.2 ms: 1.40x slower                                         |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                  |

Benchmark hidden because not significant (1): python_startup
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.22x
