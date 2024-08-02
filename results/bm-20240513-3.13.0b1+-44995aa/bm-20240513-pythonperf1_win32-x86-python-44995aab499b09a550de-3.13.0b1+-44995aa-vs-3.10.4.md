# Results vs. 3.10.4

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-x86
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.14x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 236 ms: 1.12x faster                                                            |
| chameleon      | 6.42 ms                                                         | 5.72 ms: 1.12x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.81 sec: 1.08x faster                                                          |
| html5lib       | 52.1 ms                                                         | 44.9 ms: 1.16x faster                                                           |
| tornado_http   | 118 ms                                                          | 94.6 ms: 1.24x faster                                                           |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 468 ms: 1.97x faster                                                            |
| async_tree_io           | 940 ms                                                          | 533 ms: 1.77x faster                                                            |
| async_tree_none         | 394 ms                                                          | 227 ms: 1.73x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 276 ms: 1.69x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.79x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.56x faster                                                            |
| float          | 69.6 ms                                                         | 52.4 ms: 1.33x faster                                                           |
| nbody          | 79.1 ms                                                         | 76.2 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                           | 1.52x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 101 ms: 1.15x faster                                                            |
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.87 ms: 1.43x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 218 us: 1.29x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 151 us: 1.25x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.62 sec: 1.18x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 102 ms: 1.17x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 41.4 ms: 1.16x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.2 ms: 1.12x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.6 us: 1.09x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 58.5 ms: 1.05x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 3.07 us: 1.03x slower                                                           |
| pickle               | 7.83 us                                                         | 8.12 us: 1.04x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.6 us: 1.08x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.52 us: 1.10x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.7 us: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.1 ms: 1.04x faster                                                           |
| python_startup_no_site | 18.1 ms                                                         | 18.2 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.99 ms: 1.30x faster                                                           |
| django_template | 36.0 ms                                                         | 31.0 ms: 1.16x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 44.3 ms: 1.05x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 20.3 ms: 1.04x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.13x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 138 us: 2.87x faster                                                            |
| pidigits                 | 502 ms                                                          | 196 ms: 2.56x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 468 ms: 1.97x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.22 ms: 1.82x faster                                                           |
| async_tree_io            | 940 ms                                                          | 533 ms: 1.77x faster                                                            |
| pylint                   | 384 ms                                                          | 220 ms: 1.74x faster                                                            |
| async_tree_none          | 394 ms                                                          | 227 ms: 1.73x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 276 ms: 1.69x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 58.0 ns: 1.69x faster                                                           |
| raytrace                 | 303 ms                                                          | 182 ms: 1.66x faster                                                            |
| comprehensions           | 17.7 us                                                         | 11.7 us: 1.52x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 59.2 ms: 1.52x faster                                                           |
| chaos                    | 74.4 ms                                                         | 49.2 ms: 1.51x faster                                                           |
| generators               | 31.6 ms                                                         | 21.2 ms: 1.49x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 54.9 ms: 1.48x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 6.87 ms: 1.43x faster                                                           |
| go                       | 146 ms                                                          | 104 ms: 1.41x faster                                                            |
| richards_super           | 49.9 ms                                                         | 35.7 ms: 1.40x faster                                                           |
| scimark_sor              | 115 ms                                                          | 82.6 ms: 1.39x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 959 us: 1.39x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.43 ms: 1.38x faster                                                           |
| pyflate                  | 422 ms                                                          | 307 ms: 1.38x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 45.6 ms: 1.36x faster                                                           |
| float                    | 69.6 ms                                                         | 52.4 ms: 1.33x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.19 ms: 1.33x faster                                                           |
| pycparser                | 1.04 sec                                                        | 798 ms: 1.31x faster                                                            |
| mako                     | 9.10 ms                                                         | 6.99 ms: 1.30x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 218 us: 1.29x faster                                                            |
| richards                 | 40.3 ms                                                         | 31.7 ms: 1.27x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 69.2 ms: 1.26x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 23.5 us: 1.26x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 151 us: 1.25x faster                                                            |
| tornado_http             | 118 ms                                                          | 94.6 ms: 1.24x faster                                                           |
| fannkuch                 | 317 ms                                                          | 265 ms: 1.20x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 68.0 ms: 1.18x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.62 sec: 1.18x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 102 ms: 1.17x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.96 us: 1.17x faster                                                           |
| sympy_sum                | 122 ms                                                          | 105 ms: 1.17x faster                                                            |
| django_template          | 36.0 ms                                                         | 31.0 ms: 1.16x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 41.4 ms: 1.16x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 44.9 ms: 1.16x faster                                                           |
| regex_compile            | 117 ms                                                          | 101 ms: 1.15x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.82 ms: 1.15x faster                                                           |
| json                     | 4.76 ms                                                         | 4.17 ms: 1.14x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 14.7 ms: 1.13x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 987 us: 1.13x faster                                                            |
| chameleon                | 6.42 ms                                                         | 5.72 ms: 1.12x faster                                                           |
| 2to3                     | 265 ms                                                          | 236 ms: 1.12x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.2 ms: 1.12x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.0 ms: 1.12x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 40.2 ms: 1.11x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.65 sec: 1.11x faster                                                          |
| sympy_str                | 229 ms                                                          | 208 ms: 1.10x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 209 ms: 1.10x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.24 sec: 1.10x faster                                                          |
| deepcopy                 | 310 us                                                          | 282 us: 1.10x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 73.3 ms: 1.09x faster                                                           |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                            |
| json_loads               | 22.4 us                                                         | 20.6 us: 1.09x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 610 ms: 1.08x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.81 sec: 1.08x faster                                                          |
| sympy_expand             | 391 ms                                                          | 370 ms: 1.06x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 58.5 ms: 1.05x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 44.3 ms: 1.05x faster                                                           |
| scimark_fft              | 216 ms                                                          | 207 ms: 1.05x faster                                                            |
| nbody                    | 79.1 ms                                                         | 76.2 ms: 1.04x faster                                                           |
| python_startup           | 22.9 ms                                                         | 22.1 ms: 1.04x faster                                                           |
| genshi_text              | 21.0 ms                                                         | 20.3 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.9 sec: 1.01x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.70 us: 1.01x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 18.2 ms: 1.01x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                           |
| unpickle_list            | 2.98 us                                                         | 3.07 us: 1.03x slower                                                           |
| pickle                   | 7.83 us                                                         | 8.12 us: 1.04x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.63 us: 1.05x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.30 us: 1.05x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 737 us: 1.06x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 71.2 ms: 1.07x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.6 us: 1.08x slower                                                           |
| async_generators         | 241 ms                                                          | 261 ms: 1.08x slower                                                            |
| pathlib                  | 81.2 ms                                                         | 88.7 ms: 1.09x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.52 us: 1.10x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.45 ms: 1.13x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 20.7 us: 1.13x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.01 ms: 1.24x slower                                                           |
| coverage                 | 46.6 ms                                                         | 310 ms: 6.65x slower                                                            |
| thrift                   | 902 us                                                          | 10.1 ms: 11.19x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.14x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_tcp, flaskblogging
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown