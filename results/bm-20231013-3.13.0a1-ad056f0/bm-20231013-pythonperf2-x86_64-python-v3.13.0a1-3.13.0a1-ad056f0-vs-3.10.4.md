
# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a1
- machine: linux-x86_64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.26x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 297 ms: 1.18x faster                                             |
| chameleon      | 9.44 ms                                                      | 7.78 ms: 1.21x faster                                            |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                           |
| tornado_http   | 157 ms                                                       | 121 ms: 1.29x faster                                             |
| Geometric mean | (ref)                                                        | 1.22x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 439 ms: 1.57x faster                                             |
| async_tree_memoization  | 819 ms                                                       | 557 ms: 1.47x faster                                             |
| async_tree_io           | 1.60 sec                                                     | 1.09 sec: 1.46x faster                                           |
| async_tree_cpu_io_mixed | 936 ms                                                       | 713 ms: 1.31x faster                                             |
| Geometric mean          | (ref)                                                        | 1.45x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 87.7 ms: 1.53x faster                                            |
| float          | 111 ms                                                       | 81.5 ms: 1.36x faster                                            |
| pidigits       | 271 ms                                                       | 264 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                        | 1.29x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 150 ms: 1.26x faster                                             |
| regex_dna      | 261 ms                                                       | 241 ms: 1.09x faster                                             |
| regex_v8       | 27.2 ms                                                      | 26.2 ms: 1.04x faster                                            |
| regex_effbot   | 3.09 ms                                                      | 3.55 ms: 1.15x slower                                            |
| Geometric mean | (ref)                                                        | 1.06x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 314 us: 1.45x faster                                             |
| unpickle_pure_python | 312 us                                                       | 220 us: 1.42x faster                                             |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                            |
| tomli_loads          | 2.92 sec                                                     | 2.24 sec: 1.30x faster                                           |
| xml_etree_process    | 75.9 ms                                                      | 59.9 ms: 1.27x faster                                            |
| json_loads           | 30.3 us                                                      | 24.3 us: 1.25x faster                                            |
| xml_etree_generate   | 92.3 ms                                                      | 87.3 ms: 1.06x faster                                            |
| xml_etree_parse      | 160 ms                                                       | 152 ms: 1.05x faster                                             |
| unpickle_list        | 4.65 us                                                      | 4.61 us: 1.01x faster                                            |
| pickle               | 9.89 us                                                      | 10.1 us: 1.02x slower                                            |
| unpickle             | 13.5 us                                                      | 14.3 us: 1.06x slower                                            |
| pickle_list          | 4.12 us                                                      | 4.45 us: 1.08x slower                                            |
| pickle_dict          | 29.5 us                                                      | 32.9 us: 1.12x slower                                            |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 12.6 ms: 1.10x slower                                            |
| python_startup_no_site | 7.33 ms                                                      | 8.70 ms: 1.19x slower                                            |
| Geometric mean         | (ref)                                                        | 1.14x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 155 us: 3.47x faster                                             |
| asyncio_tcp              | 779 ms                                                       | 367 ms: 2.13x faster                                             |
| deltablue                | 7.50 ms                                                      | 3.66 ms: 2.05x faster                                            |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                           |
| raytrace                 | 489 ms                                                       | 276 ms: 1.77x faster                                             |
| chaos                    | 109 ms                                                       | 62.7 ms: 1.73x faster                                            |
| logging_silent           | 167 ns                                                       | 98.3 ns: 1.70x faster                                            |
| scimark_lu               | 167 ms                                                       | 103 ms: 1.63x faster                                             |
| crypto_pyaes             | 119 ms                                                       | 73.4 ms: 1.62x faster                                            |
| generators               | 57.3 ms                                                      | 35.4 ms: 1.62x faster                                            |
| async_tree_none          | 692 ms                                                       | 439 ms: 1.57x faster                                             |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.57x faster                                            |
| nbody                    | 134 ms                                                       | 87.7 ms: 1.53x faster                                            |
| go                       | 262 ms                                                       | 172 ms: 1.52x faster                                             |
| scimark_monte_carlo      | 107 ms                                                       | 71.0 ms: 1.51x faster                                            |
| spectral_norm            | 139 ms                                                       | 92.3 ms: 1.51x faster                                            |
| async_tree_memoization   | 819 ms                                                       | 557 ms: 1.47x faster                                             |
| richards_super           | 90.6 ms                                                      | 61.7 ms: 1.47x faster                                            |
| sqlglot_transpile        | 2.68 ms                                                      | 1.83 ms: 1.46x faster                                            |
| async_tree_io            | 1.60 sec                                                     | 1.09 sec: 1.46x faster                                           |
| pickle_pure_python       | 455 us                                                       | 314 us: 1.45x faster                                             |
| hexiom                   | 9.42 ms                                                      | 6.54 ms: 1.44x faster                                            |
| pyflate                  | 733 ms                                                       | 513 ms: 1.43x faster                                             |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                            |
| unpickle_pure_python     | 312 us                                                       | 220 us: 1.42x faster                                             |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                            |
| float                    | 111 ms                                                       | 81.5 ms: 1.36x faster                                            |
| richards                 | 75.1 ms                                                      | 55.4 ms: 1.36x faster                                            |
| bench_mp_pool            | 6.37 ms                                                      | 4.72 ms: 1.35x faster                                            |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 713 ms: 1.31x faster                                             |
| logging_simple           | 8.88 us                                                      | 6.79 us: 1.31x faster                                            |
| tomli_loads              | 2.92 sec                                                     | 2.24 sec: 1.30x faster                                           |
| logging_format           | 9.64 us                                                      | 7.44 us: 1.30x faster                                            |
| tornado_http             | 157 ms                                                       | 121 ms: 1.29x faster                                             |
| deepcopy_memo            | 49.8 us                                                      | 38.6 us: 1.29x faster                                            |
| nqueens                  | 115 ms                                                       | 89.2 ms: 1.29x faster                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                           |
| xml_etree_process        | 75.9 ms                                                      | 59.9 ms: 1.27x faster                                            |
| pprint_safe_repr         | 1.05 sec                                                     | 829 ms: 1.27x faster                                             |
| regex_compile            | 190 ms                                                       | 150 ms: 1.26x faster                                             |
| pycparser                | 1.67 sec                                                     | 1.33 sec: 1.26x faster                                           |
| json_loads               | 30.3 us                                                      | 24.3 us: 1.25x faster                                            |
| comprehensions           | 26.7 us                                                      | 21.5 us: 1.24x faster                                            |
| deepcopy                 | 468 us                                                       | 379 us: 1.24x faster                                             |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                             |
| fannkuch                 | 483 ms                                                       | 396 ms: 1.22x faster                                             |
| sympy_expand             | 600 ms                                                       | 494 ms: 1.21x faster                                             |
| chameleon                | 9.44 ms                                                      | 7.78 ms: 1.21x faster                                            |
| scimark_sor              | 180 ms                                                       | 149 ms: 1.21x faster                                             |
| sympy_sum                | 193 ms                                                       | 161 ms: 1.20x faster                                             |
| mdp                      | 3.01 sec                                                     | 2.52 sec: 1.19x faster                                           |
| sqlglot_optimize         | 70.1 ms                                                      | 58.8 ms: 1.19x faster                                            |
| bench_thread_pool        | 1.14 ms                                                      | 961 us: 1.19x faster                                             |
| docutils                 | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                           |
| deepcopy_reduce          | 4.01 us                                                      | 3.39 us: 1.18x faster                                            |
| unpack_sequence          | 59.9 ns                                                      | 50.9 ns: 1.18x faster                                            |
| 2to3                     | 350 ms                                                       | 297 ms: 1.18x faster                                             |
| sympy_str                | 360 ms                                                       | 307 ms: 1.17x faster                                             |
| dulwich_log              | 81.1 ms                                                      | 69.2 ms: 1.17x faster                                            |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.34 ms: 1.17x faster                                            |
| sympy_integrate          | 28.2 ms                                                      | 24.2 ms: 1.16x faster                                            |
| json                     | 5.86 ms                                                      | 5.12 ms: 1.15x faster                                            |
| scimark_fft              | 361 ms                                                       | 315 ms: 1.15x faster                                             |
| create_gc_cycles         | 1.76 ms                                                      | 1.58 ms: 1.12x faster                                            |
| sqlite_synth             | 2.99 us                                                      | 2.70 us: 1.11x faster                                            |
| pathlib                  | 21.4 ms                                                      | 19.3 ms: 1.10x faster                                            |
| regex_dna                | 261 ms                                                       | 241 ms: 1.09x faster                                             |
| xml_etree_generate       | 92.3 ms                                                      | 87.3 ms: 1.06x faster                                            |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.06x faster                                             |
| async_generators         | 421 ms                                                       | 399 ms: 1.06x faster                                             |
| xml_etree_parse          | 160 ms                                                       | 152 ms: 1.05x faster                                             |
| regex_v8                 | 27.2 ms                                                      | 26.2 ms: 1.04x faster                                            |
| pidigits                 | 271 ms                                                       | 264 ms: 1.03x faster                                             |
| unpickle_list            | 4.65 us                                                      | 4.61 us: 1.01x faster                                            |
| pickle                   | 9.89 us                                                      | 10.1 us: 1.02x slower                                            |
| unpickle                 | 13.5 us                                                      | 14.3 us: 1.06x slower                                            |
| pickle_list              | 4.12 us                                                      | 4.45 us: 1.08x slower                                            |
| python_startup           | 11.5 ms                                                      | 12.6 ms: 1.10x slower                                            |
| pickle_dict              | 29.5 us                                                      | 32.9 us: 1.12x slower                                            |
| telco                    | 7.23 ms                                                      | 8.25 ms: 1.14x slower                                            |
| regex_effbot             | 3.09 ms                                                      | 3.55 ms: 1.15x slower                                            |
| gc_traversal             | 3.42 ms                                                      | 3.95 ms: 1.16x slower                                            |
| python_startup_no_site   | 7.33 ms                                                      | 8.70 ms: 1.19x slower                                            |
| coverage                 | 63.3 ms                                                      | 83.6 ms: 1.32x slower                                            |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                     |

Benchmark hidden because not significant (2): asyncio_websockets, xml_etree_iterparse
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x


# Memory

- memory change: 1.05x