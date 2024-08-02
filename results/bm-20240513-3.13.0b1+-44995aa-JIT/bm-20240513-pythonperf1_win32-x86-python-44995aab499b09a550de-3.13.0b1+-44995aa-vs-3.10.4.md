# Results vs. 3.10.4

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-x86
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 244 ms: 1.09x faster                                                            |
| chameleon      | 6.42 ms                                                         | 5.95 ms: 1.08x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                          |
| html5lib       | 52.1 ms                                                         | 45.2 ms: 1.15x faster                                                           |
| tornado_http   | 118 ms                                                          | 97.4 ms: 1.21x faster                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 479 ms: 1.92x faster                                                            |
| async_tree_io           | 940 ms                                                          | 531 ms: 1.77x faster                                                            |
| async_tree_none         | 394 ms                                                          | 230 ms: 1.71x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 281 ms: 1.66x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.76x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.56x faster                                                            |
| float          | 69.6 ms                                                         | 41.3 ms: 1.68x faster                                                           |
| nbody          | 79.1 ms                                                         | 53.7 ms: 1.48x faster                                                           |
| Geometric mean | (ref)                                                           | 1.85x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 92.7 ms: 1.26x faster                                                           |
| regex_dna      | 131 ms                                                          | 117 ms: 1.12x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.94 ms: 1.17x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.69 ms: 1.47x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 198 us: 1.42x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 136 us: 1.40x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.38 sec: 1.38x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 40.5 ms: 1.19x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 60.0 ms: 1.18x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 102 ms: 1.17x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 56.0 ms: 1.10x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.89 us: 1.03x faster                                                           |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.03x slower                                                           |
| pickle               | 7.83 us                                                         | 8.21 us: 1.05x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.64 us: 1.13x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.8 us: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 25.2 ms: 1.10x slower                                                           |
| python_startup_no_site | 18.1 ms                                                         | 21.3 ms: 1.18x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.31 ms: 1.71x faster                                                           |
| django_template | 36.0 ms                                                         | 32.2 ms: 1.12x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 50.9 ms: 1.09x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 140 us: 2.82x faster                                                            |
| pidigits                 | 502 ms                                                          | 196 ms: 2.56x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 479 ms: 1.92x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 54.6 ns: 1.79x faster                                                           |
| async_tree_io            | 940 ms                                                          | 531 ms: 1.77x faster                                                            |
| mako                     | 9.10 ms                                                         | 5.31 ms: 1.71x faster                                                           |
| async_tree_none          | 394 ms                                                          | 230 ms: 1.71x faster                                                            |
| float                    | 69.6 ms                                                         | 41.3 ms: 1.68x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 47.9 ms: 1.67x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 281 ms: 1.66x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 49.2 ms: 1.65x faster                                                           |
| pylint                   | 384 ms                                                          | 238 ms: 1.61x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.51 ms: 1.61x faster                                                           |
| comprehensions           | 17.7 us                                                         | 11.1 us: 1.60x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.9 ms: 1.55x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 887 us: 1.50x faster                                                            |
| chaos                    | 74.4 ms                                                         | 50.2 ms: 1.48x faster                                                           |
| nbody                    | 79.1 ms                                                         | 53.7 ms: 1.48x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 6.69 ms: 1.47x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 20.2 us: 1.47x faster                                                           |
| raytrace                 | 303 ms                                                          | 208 ms: 1.46x faster                                                            |
| fannkuch                 | 317 ms                                                          | 219 ms: 1.45x faster                                                            |
| richards_super           | 49.9 ms                                                         | 34.7 ms: 1.44x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 198 us: 1.42x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 136 us: 1.40x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.14 ms: 1.38x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.38 sec: 1.38x faster                                                          |
| pyflate                  | 422 ms                                                          | 305 ms: 1.38x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.49 ms: 1.37x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.38 ms: 1.36x faster                                                           |
| generators               | 31.6 ms                                                         | 23.3 ms: 1.36x faster                                                           |
| go                       | 146 ms                                                          | 108 ms: 1.35x faster                                                            |
| pycparser                | 1.04 sec                                                        | 778 ms: 1.34x faster                                                            |
| richards                 | 40.3 ms                                                         | 30.5 ms: 1.32x faster                                                           |
| scimark_sor              | 115 ms                                                          | 88.1 ms: 1.31x faster                                                           |
| regex_compile            | 117 ms                                                          | 92.7 ms: 1.26x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 70.6 ms: 1.23x faster                                                           |
| scimark_fft              | 216 ms                                                          | 176 ms: 1.23x faster                                                            |
| tornado_http             | 118 ms                                                          | 97.4 ms: 1.21x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 74.7 ms: 1.20x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.92 us: 1.19x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.15 sec: 1.19x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 40.5 ms: 1.19x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 555 ms: 1.19x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 60.0 ms: 1.18x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 102 ms: 1.17x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 45.2 ms: 1.15x faster                                                           |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.15x faster                                                            |
| coroutines               | 17.9 ms                                                         | 15.8 ms: 1.14x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 990 us: 1.13x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 71.4 ms: 1.12x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.63 sec: 1.12x faster                                                          |
| json                     | 4.76 ms                                                         | 4.25 ms: 1.12x faster                                                           |
| django_template          | 36.0 ms                                                         | 32.2 ms: 1.12x faster                                                           |
| regex_dna                | 131 ms                                                          | 117 ms: 1.12x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 56.0 ms: 1.10x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 40.7 ms: 1.10x faster                                                           |
| sympy_str                | 229 ms                                                          | 209 ms: 1.10x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 211 ms: 1.09x faster                                                            |
| 2to3                     | 265 ms                                                          | 244 ms: 1.09x faster                                                            |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                           |
| chameleon                | 6.42 ms                                                         | 5.95 ms: 1.08x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.6 ms: 1.07x faster                                                           |
| sympy_expand             | 391 ms                                                          | 370 ms: 1.06x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 705 ms: 1.06x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                          |
| deepcopy                 | 310 us                                                          | 299 us: 1.04x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.89 us: 1.03x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.66 us: 1.01x faster                                                           |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                                          |
| logging_format           | 7.91 us                                                         | 7.97 us: 1.01x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.36 us: 1.01x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.03x slower                                                           |
| pickle                   | 7.83 us                                                         | 8.21 us: 1.05x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 86.9 ms: 1.07x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 755 us: 1.09x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 50.9 ms: 1.09x slower                                                           |
| python_startup           | 22.9 ms                                                         | 25.2 ms: 1.10x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.64 us: 1.13x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 75.3 ms: 1.14x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 20.8 us: 1.14x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.94 ms: 1.17x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 21.3 ms: 1.18x slower                                                           |
| telco                    | 4.83 ms                                                         | 5.76 ms: 1.19x slower                                                           |
| async_generators         | 241 ms                                                          | 297 ms: 1.23x slower                                                            |
| coverage                 | 46.6 ms                                                         | 325 ms: 6.97x slower                                                            |
| thrift                   | 902 us                                                          | 10.6 ms: 11.70x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.16x faster                                                                    |

Benchmark hidden because not significant (3): regex_v8, genshi_text, asyncio_tcp_ssl
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown