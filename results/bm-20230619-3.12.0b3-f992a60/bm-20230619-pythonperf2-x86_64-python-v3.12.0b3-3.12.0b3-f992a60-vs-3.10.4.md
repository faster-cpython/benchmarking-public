
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0b3
- machine: linux-x86_64
- commit hash: f992a60
- commit date: 2023-06-19
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-pythonperf2-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                             |
| docutils       | 3.40 sec                                                     | 2.87 sec: 1.19x faster                                           |
| tornado_http   | 152 ms                                                       | 118 ms: 1.29x faster                                             |
| Geometric mean | (ref)                                                        | 1.24x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-pythonperf2-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 84.2 ms: 1.63x faster                                            |
| float          | 110 ms                                                       | 78.8 ms: 1.40x faster                                            |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                        | 1.33x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-pythonperf2-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 144 ms: 1.35x faster                                             |
| regex_v8       | 26.6 ms                                                      | 23.9 ms: 1.11x faster                                            |
| regex_dna      | 259 ms                                                       | 238 ms: 1.09x faster                                             |
| regex_effbot   | 2.99 ms                                                      | 3.48 ms: 1.16x slower                                            |
| Geometric mean | (ref)                                                        | 1.09x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-pythonperf2-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 209 us: 1.54x faster                                             |
| pickle_pure_python   | 457 us                                                       | 326 us: 1.40x faster                                             |
| tomli_loads          | 2.97 sec                                                     | 2.17 sec: 1.37x faster                                           |
| json_dumps           | 14.2 ms                                                      | 10.4 ms: 1.36x faster                                            |
| xml_etree_process    | 76.0 ms                                                      | 58.2 ms: 1.31x faster                                            |
| json_loads           | 30.0 us                                                      | 24.7 us: 1.21x faster                                            |
| xml_etree_generate   | 94.6 ms                                                      | 85.3 ms: 1.11x faster                                            |
| xml_etree_parse      | 162 ms                                                       | 150 ms: 1.08x faster                                             |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                             |
| unpickle             | 14.2 us                                                      | 14.6 us: 1.03x slower                                            |
| unpickle_list        | 4.49 us                                                      | 4.65 us: 1.03x slower                                            |
| pickle               | 9.94 us                                                      | 10.3 us: 1.04x slower                                            |
| pickle_list          | 4.11 us                                                      | 4.43 us: 1.08x slower                                            |
| pickle_dict          | 30.0 us                                                      | 33.6 us: 1.12x slower                                            |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-pythonperf2-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                            |
| python_startup_no_site | 7.32 ms                                                      | 8.43 ms: 1.15x slower                                            |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-pythonperf2-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.0 ms: 1.46x faster                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-pythonperf2-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 152 us: 3.44x faster                                             |
| deltablue                | 7.47 ms                                                      | 3.21 ms: 2.32x faster                                            |
| asyncio_tcp              | 782 ms                                                       | 377 ms: 2.08x faster                                             |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.56 sec: 1.98x faster                                           |
| logging_silent           | 166 ns                                                       | 91.8 ns: 1.81x faster                                            |
| richards_super           | 90.8 ms                                                      | 50.8 ms: 1.79x faster                                            |
| go                       | 259 ms                                                       | 145 ms: 1.78x faster                                             |
| scimark_lu               | 164 ms                                                       | 96.7 ms: 1.69x faster                                            |
| chaos                    | 107 ms                                                       | 63.4 ms: 1.69x faster                                            |
| richards                 | 74.1 ms                                                      | 44.7 ms: 1.66x faster                                            |
| scimark_sor              | 177 ms                                                       | 107 ms: 1.65x faster                                             |
| hexiom                   | 9.52 ms                                                      | 5.79 ms: 1.64x faster                                            |
| nbody                    | 137 ms                                                       | 84.2 ms: 1.63x faster                                            |
| raytrace                 | 488 ms                                                       | 300 ms: 1.63x faster                                             |
| sqlglot_parse            | 2.26 ms                                                      | 1.39 ms: 1.62x faster                                            |
| scimark_monte_carlo      | 109 ms                                                       | 67.8 ms: 1.62x faster                                            |
| pyflate                  | 697 ms                                                       | 439 ms: 1.59x faster                                             |
| generators               | 58.0 ms                                                      | 36.7 ms: 1.58x faster                                            |
| unpickle_pure_python     | 321 us                                                       | 209 us: 1.54x faster                                             |
| async_tree_none          | 700 ms                                                       | 457 ms: 1.53x faster                                             |
| async_tree_io            | 1.61 sec                                                     | 1.06 sec: 1.52x faster                                           |
| sqlglot_transpile        | 2.71 ms                                                      | 1.80 ms: 1.51x faster                                            |
| async_tree_memoization   | 824 ms                                                       | 551 ms: 1.50x faster                                             |
| mako                     | 14.7 ms                                                      | 10.0 ms: 1.46x faster                                            |
| crypto_pyaes             | 118 ms                                                       | 80.9 ms: 1.46x faster                                            |
| spectral_norm            | 136 ms                                                       | 93.4 ms: 1.46x faster                                            |
| fannkuch                 | 496 ms                                                       | 343 ms: 1.45x faster                                             |
| bench_mp_pool            | 7.18 ms                                                      | 5.05 ms: 1.42x faster                                            |
| pickle_pure_python       | 457 us                                                       | 326 us: 1.40x faster                                             |
| float                    | 110 ms                                                       | 78.8 ms: 1.40x faster                                            |
| logging_simple           | 8.90 us                                                      | 6.49 us: 1.37x faster                                            |
| tomli_loads              | 2.97 sec                                                     | 2.17 sec: 1.37x faster                                           |
| json_dumps               | 14.2 ms                                                      | 10.4 ms: 1.36x faster                                            |
| coroutines               | 30.4 ms                                                      | 22.4 ms: 1.36x faster                                            |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 704 ms: 1.35x faster                                             |
| regex_compile            | 194 ms                                                       | 144 ms: 1.35x faster                                             |
| logging_format           | 9.57 us                                                      | 7.13 us: 1.34x faster                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                           |
| pprint_safe_repr         | 1.05 sec                                                     | 799 ms: 1.31x faster                                             |
| deepcopy_memo            | 48.9 us                                                      | 37.4 us: 1.31x faster                                            |
| pycparser                | 1.66 sec                                                     | 1.27 sec: 1.31x faster                                           |
| xml_etree_process        | 76.0 ms                                                      | 58.2 ms: 1.31x faster                                            |
| tornado_http             | 152 ms                                                       | 118 ms: 1.29x faster                                             |
| nqueens                  | 112 ms                                                       | 90.2 ms: 1.25x faster                                            |
| comprehensions           | 26.9 us                                                      | 21.7 us: 1.24x faster                                            |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.24x faster                                             |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                             |
| sqlglot_optimize         | 70.3 ms                                                      | 57.4 ms: 1.22x faster                                            |
| mdp                      | 3.03 sec                                                     | 2.49 sec: 1.22x faster                                           |
| json_loads               | 30.0 us                                                      | 24.7 us: 1.21x faster                                            |
| dulwich_log              | 80.1 ms                                                      | 66.1 ms: 1.21x faster                                            |
| deepcopy                 | 454 us                                                       | 376 us: 1.21x faster                                             |
| unpack_sequence          | 59.5 ns                                                      | 49.4 ns: 1.21x faster                                            |
| bench_thread_pool        | 1.14 ms                                                      | 953 us: 1.19x faster                                             |
| docutils                 | 3.40 sec                                                     | 2.87 sec: 1.19x faster                                           |
| scimark_fft              | 359 ms                                                       | 304 ms: 1.18x faster                                             |
| deepcopy_reduce          | 4.03 us                                                      | 3.41 us: 1.18x faster                                            |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.43 ms: 1.17x faster                                            |
| json                     | 5.96 ms                                                      | 5.18 ms: 1.15x faster                                            |
| pathlib                  | 21.7 ms                                                      | 19.2 ms: 1.13x faster                                            |
| regex_v8                 | 26.6 ms                                                      | 23.9 ms: 1.11x faster                                            |
| create_gc_cycles         | 1.82 ms                                                      | 1.64 ms: 1.11x faster                                            |
| xml_etree_generate       | 94.6 ms                                                      | 85.3 ms: 1.11x faster                                            |
| async_generators         | 422 ms                                                       | 382 ms: 1.11x faster                                             |
| meteor_contest           | 137 ms                                                       | 125 ms: 1.09x faster                                             |
| sqlite_synth             | 2.97 us                                                      | 2.72 us: 1.09x faster                                            |
| regex_dna                | 259 ms                                                       | 238 ms: 1.09x faster                                             |
| xml_etree_parse          | 162 ms                                                       | 150 ms: 1.08x faster                                             |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.04x faster                                             |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                             |
| telco                    | 7.14 ms                                                      | 7.07 ms: 1.01x faster                                            |
| python_startup           | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                            |
| unpickle                 | 14.2 us                                                      | 14.6 us: 1.03x slower                                            |
| unpickle_list            | 4.49 us                                                      | 4.65 us: 1.03x slower                                            |
| pickle                   | 9.94 us                                                      | 10.3 us: 1.04x slower                                            |
| pickle_list              | 4.11 us                                                      | 4.43 us: 1.08x slower                                            |
| pickle_dict              | 30.0 us                                                      | 33.6 us: 1.12x slower                                            |
| python_startup_no_site   | 7.32 ms                                                      | 8.43 ms: 1.15x slower                                            |
| regex_effbot             | 2.99 ms                                                      | 3.48 ms: 1.16x slower                                            |
| gc_traversal             | 3.45 ms                                                      | 4.06 ms: 1.18x slower                                            |
| dask                     | 463 ms                                                       | 562 ms: 1.21x slower                                             |
| coverage                 | 64.0 ms                                                      | 89.0 ms: 1.39x slower                                            |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                     |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x
