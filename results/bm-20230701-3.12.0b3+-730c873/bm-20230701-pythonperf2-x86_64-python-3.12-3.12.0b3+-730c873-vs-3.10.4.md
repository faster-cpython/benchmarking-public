
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 730c873
- commit date: 2023-07-01
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf2-x86_64-python-3.12-3.12.0b3+-730c873 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                         |
| docutils       | 3.40 sec                                                     | 2.88 sec: 1.18x faster                                       |
| tornado_http   | 152 ms                                                       | 121 ms: 1.26x faster                                         |
| Geometric mean | (ref)                                                        | 1.22x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf2-x86_64-python-3.12-3.12.0b3+-730c873 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 85.0 ms: 1.61x faster                                        |
| float          | 110 ms                                                       | 78.4 ms: 1.41x faster                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.33x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf2-x86_64-python-3.12-3.12.0b3+-730c873 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 143 ms: 1.35x faster                                         |
| regex_v8       | 26.6 ms                                                      | 24.0 ms: 1.11x faster                                        |
| regex_dna      | 259 ms                                                       | 244 ms: 1.07x faster                                         |
| regex_effbot   | 2.99 ms                                                      | 3.49 ms: 1.17x slower                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf2-x86_64-python-3.12-3.12.0b3+-730c873 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 205 us: 1.56x faster                                         |
| pickle_pure_python   | 457 us                                                       | 319 us: 1.43x faster                                         |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.40x faster                                        |
| tomli_loads          | 2.97 sec                                                     | 2.19 sec: 1.36x faster                                       |
| xml_etree_process    | 76.0 ms                                                      | 57.9 ms: 1.31x faster                                        |
| json_loads           | 30.0 us                                                      | 24.5 us: 1.22x faster                                        |
| xml_etree_generate   | 94.6 ms                                                      | 84.8 ms: 1.12x faster                                        |
| xml_etree_parse      | 162 ms                                                       | 152 ms: 1.06x faster                                         |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                         |
| pickle               | 9.94 us                                                      | 10.1 us: 1.01x slower                                        |
| unpickle_list        | 4.49 us                                                      | 4.78 us: 1.06x slower                                        |
| pickle_dict          | 30.0 us                                                      | 32.2 us: 1.07x slower                                        |
| pickle_list          | 4.11 us                                                      | 4.46 us: 1.09x slower                                        |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf2-x86_64-python-3.12-3.12.0b3+-730c873 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.46 ms: 1.16x slower                                        |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf2-x86_64-python-3.12-3.12.0b3+-730c873 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf2-x86_64-python-3.12-3.12.0b3+-730c873 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 152 us: 3.43x faster                                         |
| deltablue                | 7.47 ms                                                      | 3.24 ms: 2.31x faster                                        |
| asyncio_tcp              | 782 ms                                                       | 377 ms: 2.08x faster                                         |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.56 sec: 1.98x faster                                       |
| richards_super           | 90.8 ms                                                      | 50.5 ms: 1.80x faster                                        |
| go                       | 259 ms                                                       | 144 ms: 1.79x faster                                         |
| logging_silent           | 166 ns                                                       | 95.0 ns: 1.74x faster                                        |
| scimark_lu               | 164 ms                                                       | 95.9 ms: 1.71x faster                                        |
| chaos                    | 107 ms                                                       | 62.9 ms: 1.70x faster                                        |
| richards                 | 74.1 ms                                                      | 44.6 ms: 1.66x faster                                        |
| scimark_sor              | 177 ms                                                       | 107 ms: 1.65x faster                                         |
| hexiom                   | 9.52 ms                                                      | 5.79 ms: 1.64x faster                                        |
| sqlglot_parse            | 2.26 ms                                                      | 1.39 ms: 1.62x faster                                        |
| scimark_monte_carlo      | 109 ms                                                       | 67.8 ms: 1.62x faster                                        |
| nbody                    | 137 ms                                                       | 85.0 ms: 1.61x faster                                        |
| generators               | 58.0 ms                                                      | 36.1 ms: 1.61x faster                                        |
| pyflate                  | 697 ms                                                       | 435 ms: 1.60x faster                                         |
| raytrace                 | 488 ms                                                       | 306 ms: 1.59x faster                                         |
| unpickle_pure_python     | 321 us                                                       | 205 us: 1.56x faster                                         |
| spectral_norm            | 136 ms                                                       | 88.0 ms: 1.55x faster                                        |
| async_tree_io            | 1.61 sec                                                     | 1.05 sec: 1.52x faster                                       |
| async_tree_none          | 700 ms                                                       | 459 ms: 1.52x faster                                         |
| sqlglot_transpile        | 2.71 ms                                                      | 1.78 ms: 1.52x faster                                        |
| async_tree_memoization   | 824 ms                                                       | 551 ms: 1.50x faster                                         |
| mako                     | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                        |
| crypto_pyaes             | 118 ms                                                       | 81.6 ms: 1.45x faster                                        |
| fannkuch                 | 496 ms                                                       | 343 ms: 1.45x faster                                         |
| pickle_pure_python       | 457 us                                                       | 319 us: 1.43x faster                                         |
| float                    | 110 ms                                                       | 78.4 ms: 1.41x faster                                        |
| json_dumps               | 14.2 ms                                                      | 10.2 ms: 1.40x faster                                        |
| tomli_loads              | 2.97 sec                                                     | 2.19 sec: 1.36x faster                                       |
| logging_simple           | 8.90 us                                                      | 6.56 us: 1.36x faster                                        |
| deepcopy_memo            | 48.9 us                                                      | 36.1 us: 1.36x faster                                        |
| regex_compile            | 194 ms                                                       | 143 ms: 1.35x faster                                         |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 704 ms: 1.35x faster                                         |
| coroutines               | 30.4 ms                                                      | 22.6 ms: 1.34x faster                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                       |
| logging_format           | 9.57 us                                                      | 7.25 us: 1.32x faster                                        |
| pycparser                | 1.66 sec                                                     | 1.26 sec: 1.32x faster                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 799 ms: 1.31x faster                                         |
| xml_etree_process        | 76.0 ms                                                      | 57.9 ms: 1.31x faster                                        |
| bench_mp_pool            | 7.18 ms                                                      | 5.53 ms: 1.30x faster                                        |
| mypy2                    | 466 ms                                                       | 363 ms: 1.28x faster                                         |
| tornado_http             | 152 ms                                                       | 121 ms: 1.26x faster                                         |
| nqueens                  | 112 ms                                                       | 89.7 ms: 1.25x faster                                        |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.25x faster                                         |
| sqlglot_optimize         | 70.3 ms                                                      | 57.3 ms: 1.23x faster                                        |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                         |
| deepcopy                 | 454 us                                                       | 371 us: 1.22x faster                                         |
| json_loads               | 30.0 us                                                      | 24.5 us: 1.22x faster                                        |
| comprehensions           | 26.9 us                                                      | 22.1 us: 1.22x faster                                        |
| deepcopy_reduce          | 4.03 us                                                      | 3.38 us: 1.19x faster                                        |
| dulwich_log              | 80.1 ms                                                      | 67.1 ms: 1.19x faster                                        |
| scimark_fft              | 359 ms                                                       | 301 ms: 1.19x faster                                         |
| bench_thread_pool        | 1.14 ms                                                      | 954 us: 1.19x faster                                         |
| docutils                 | 3.40 sec                                                     | 2.88 sec: 1.18x faster                                       |
| mdp                      | 3.03 sec                                                     | 2.57 sec: 1.18x faster                                       |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.46 ms: 1.17x faster                                        |
| json                     | 5.96 ms                                                      | 5.13 ms: 1.16x faster                                        |
| pathlib                  | 21.7 ms                                                      | 19.2 ms: 1.13x faster                                        |
| xml_etree_generate       | 94.6 ms                                                      | 84.8 ms: 1.12x faster                                        |
| regex_v8                 | 26.6 ms                                                      | 24.0 ms: 1.11x faster                                        |
| create_gc_cycles         | 1.82 ms                                                      | 1.64 ms: 1.11x faster                                        |
| sqlite_synth             | 2.97 us                                                      | 2.70 us: 1.10x faster                                        |
| meteor_contest           | 137 ms                                                       | 124 ms: 1.10x faster                                         |
| async_generators         | 422 ms                                                       | 388 ms: 1.09x faster                                         |
| unpack_sequence          | 59.5 ns                                                      | 55.4 ns: 1.07x faster                                        |
| regex_dna                | 259 ms                                                       | 244 ms: 1.07x faster                                         |
| xml_etree_parse          | 162 ms                                                       | 152 ms: 1.06x faster                                         |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                         |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| python_startup           | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                        |
| pickle                   | 9.94 us                                                      | 10.1 us: 1.01x slower                                        |
| unpickle_list            | 4.49 us                                                      | 4.78 us: 1.06x slower                                        |
| pickle_dict              | 30.0 us                                                      | 32.2 us: 1.07x slower                                        |
| pickle_list              | 4.11 us                                                      | 4.46 us: 1.09x slower                                        |
| gc_traversal             | 3.45 ms                                                      | 3.81 ms: 1.10x slower                                        |
| python_startup_no_site   | 7.32 ms                                                      | 8.46 ms: 1.16x slower                                        |
| regex_effbot             | 2.99 ms                                                      | 3.49 ms: 1.17x slower                                        |
| dask                     | 463 ms                                                       | 559 ms: 1.21x slower                                         |
| coverage                 | 64.0 ms                                                      | 90.8 ms: 1.42x slower                                        |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                 |

Benchmark hidden because not significant (2): telco, unpickle
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x
