# Results vs. 3.10.4

- fork: python
- ref: dcaf33a41d5d220523d7
- machine: windows-x86
- commit hash: dcaf33a
- commit date: 2024-03-20
- overall geometric mean: 1.04x slower
- HPT reliability: 66.40%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| chameleon      | 6.42 ms                                                         | 5.84 ms: 1.10x faster                                                           |
| docutils       | 1.95 sec                                                        | 2.45 sec: 1.26x slower                                                          |
| html5lib       | 52.1 ms                                                         | 50.2 ms: 1.04x faster                                                           |
| tornado_http   | 118 ms                                                          | 97.2 ms: 1.21x faster                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 1.57 sec: 1.70x slower                                                          |
| async_tree_none         | 394 ms                                                          | 1.20 sec: 3.05x slower                                                          |
| async_tree_memoization  | 467 ms                                                          | 1.47 sec: 3.14x slower                                                          |
| async_tree_io           | 940 ms                                                          | 4.63 sec: 4.93x slower                                                          |
| Geometric mean          | (ref)                                                           | 2.99x slower                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.53x faster                                                            |
| float          | 69.6 ms                                                         | 82.2 ms: 1.18x slower                                                           |
| nbody          | 79.1 ms                                                         | 100 ms: 1.27x slower                                                            |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 110 ms: 1.06x faster                                                            |
| regex_dna      | 131 ms                                                          | 124 ms: 1.05x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.95 ms: 1.17x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.93 ms: 1.42x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 215 us: 1.30x faster                                                            |
| json_loads           | 22.4 us                                                         | 20.1 us: 1.11x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.72 sec: 1.11x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 174 us: 1.09x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 47.6 ms: 1.01x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 3.04 us: 1.02x slower                                                           |
| pickle               | 7.83 us                                                         | 8.00 us: 1.02x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.5 us: 1.07x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.46 us: 1.08x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.0 us: 1.10x slower                                                           |
| xml_etree_parse      | 120 ms                                                          | 133 ms: 1.11x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 69.1 ms: 1.12x slower                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 93.8 ms: 1.32x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 26.6 ms: 1.16x slower                                                           |
| python_startup_no_site | 18.1 ms                                                         | 24.2 ms: 1.34x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.25x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.15 ms: 1.27x faster                                                           |
| django_template | 36.0 ms                                                         | 31.1 ms: 1.16x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 50.0 ms: 1.07x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 22.8 ms: 1.08x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.06x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 98.8 us: 4.00x faster                                                           |
| pidigits                 | 502 ms                                                          | 199 ms: 2.53x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 60.6 ns: 1.62x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.67 ms: 1.51x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 6.93 ms: 1.42x faster                                                           |
| generators               | 31.6 ms                                                         | 22.4 ms: 1.41x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 61.5 ms: 1.32x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 215 us: 1.30x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.03 ms: 1.29x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.15 ms: 1.27x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.29 ms: 1.23x faster                                                           |
| comprehensions           | 17.7 us                                                         | 14.4 us: 1.23x faster                                                           |
| chaos                    | 74.4 ms                                                         | 60.9 ms: 1.22x faster                                                           |
| richards_super           | 49.9 ms                                                         | 40.9 ms: 1.22x faster                                                           |
| tornado_http             | 118 ms                                                          | 97.2 ms: 1.21x faster                                                           |
| coroutines               | 17.9 ms                                                         | 14.9 ms: 1.20x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 629 ms: 1.18x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.95 us: 1.17x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 25.2 us: 1.17x faster                                                           |
| sympy_sum                | 122 ms                                                          | 105 ms: 1.16x faster                                                            |
| django_template          | 36.0 ms                                                         | 31.1 ms: 1.16x faster                                                           |
| scimark_sor              | 115 ms                                                          | 99.3 ms: 1.16x faster                                                           |
| go                       | 146 ms                                                          | 126 ms: 1.15x faster                                                            |
| raytrace                 | 303 ms                                                          | 264 ms: 1.15x faster                                                            |
| richards                 | 40.3 ms                                                         | 35.7 ms: 1.13x faster                                                           |
| pyflate                  | 422 ms                                                          | 376 ms: 1.12x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 71.6 ms: 1.12x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.1 us: 1.11x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.72 sec: 1.11x faster                                                          |
| json                     | 4.76 ms                                                         | 4.30 ms: 1.11x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                           |
| chameleon                | 6.42 ms                                                         | 5.84 ms: 1.10x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 174 us: 1.09x faster                                                            |
| sympy_str                | 229 ms                                                          | 211 ms: 1.09x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 15.3 ms: 1.09x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 83.3 ms: 1.08x faster                                                           |
| deepcopy                 | 310 us                                                          | 289 us: 1.07x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.51 us: 1.07x faster                                                           |
| regex_compile            | 117 ms                                                          | 110 ms: 1.06x faster                                                            |
| pycparser                | 1.04 sec                                                        | 989 ms: 1.05x faster                                                            |
| regex_dna                | 131 ms                                                          | 124 ms: 1.05x faster                                                            |
| sympy_expand             | 391 ms                                                          | 371 ms: 1.05x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.74 sec: 1.05x faster                                                          |
| create_gc_cycles         | 694 us                                                          | 664 us: 1.05x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 221 ms: 1.04x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 50.2 ms: 1.04x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.13 ms: 1.03x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.98 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.7 sec: 1.02x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 47.6 ms: 1.01x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                           |
| unpickle_list            | 2.98 us                                                         | 3.04 us: 1.02x slower                                                           |
| pickle                   | 7.83 us                                                         | 8.00 us: 1.02x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 45.8 ms: 1.03x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 90.2 ms: 1.04x slower                                                           |
| fannkuch                 | 317 ms                                                          | 329 ms: 1.04x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 83.4 ms: 1.04x slower                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 64.6 ms: 1.04x slower                                                           |
| pylint                   | 384 ms                                                          | 405 ms: 1.06x slower                                                            |
| pathlib                  | 81.2 ms                                                         | 86.3 ms: 1.06x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.5 us: 1.07x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.46 sec: 1.07x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 50.0 ms: 1.07x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.46 us: 1.08x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 43.1 ns: 1.08x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 22.8 ms: 1.08x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 715 ms: 1.09x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.0 us: 1.10x slower                                                           |
| scimark_fft              | 216 ms                                                          | 239 ms: 1.10x slower                                                            |
| xml_etree_parse          | 120 ms                                                          | 133 ms: 1.11x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 69.1 ms: 1.12x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 75.6 ms: 1.14x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.02 us: 1.14x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.38 us: 1.15x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.6 ms: 1.16x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.95 ms: 1.17x slower                                                           |
| float                    | 69.6 ms                                                         | 82.2 ms: 1.18x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.45 sec: 1.26x slower                                                          |
| nbody                    | 79.1 ms                                                         | 100 ms: 1.27x slower                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 93.8 ms: 1.32x slower                                                           |
| async_generators         | 241 ms                                                          | 322 ms: 1.34x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 24.2 ms: 1.34x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.53 ms: 1.35x slower                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 1.57 sec: 1.70x slower                                                          |
| async_tree_none          | 394 ms                                                          | 1.20 sec: 3.05x slower                                                          |
| async_tree_memoization   | 467 ms                                                          | 1.47 sec: 3.14x slower                                                          |
| async_tree_io            | 940 ms                                                          | 4.63 sec: 4.93x slower                                                          |
| coverage                 | 46.6 ms                                                         | 508 ms: 10.90x slower                                                           |
| thrift                   | 902 us                                                          | 10.8 ms: 12.02x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.04x slower                                                                    |

Benchmark hidden because not significant (2): gc_traversal, 2to3
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240320-3.13.0a5+-dcaf33a-JIT/bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 66.40% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: unknown