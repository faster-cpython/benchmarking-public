# Results vs. 3.10.4

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.291x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 227 ms: 1.17x faster                                                             |
| docutils       | 1.95 sec                                                        | 2.84 sec: 1.46x slower                                                           |
| html5lib       | 52.1 ms                                                         | 41.3 ms: 1.26x faster                                                            |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 335 ms: 2.75x faster                                                             |
| async_tree_io           | 940 ms                                                          | 356 ms: 2.64x faster                                                             |
| async_tree_none         | 394 ms                                                          | 172 ms: 2.29x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 216 ms: 2.16x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.45x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 138 ms: 3.64x faster                                                             |
| float          | 69.6 ms                                                         | 46.3 ms: 1.50x faster                                                            |
| nbody          | 79.1 ms                                                         | 81.4 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                           | 1.74x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 94.7 ms: 1.23x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.3 ms: 1.19x faster                                                            |
| regex_dna      | 131 ms                                                          | 116 ms: 1.13x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.59 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.11 ms: 1.61x faster                                                            |
| json_loads           | 22.4 us                                                         | 16.0 us: 1.40x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 92.9 ms: 1.29x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 157 us: 1.21x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 59.6 ms: 1.19x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 238 us: 1.18x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 44.8 ms: 1.07x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.07 us: 1.05x faster                                                            |
| pickle               | 7.83 us                                                         | 7.91 us: 1.01x slower                                                            |
| unpickle             | 9.82 us                                                         | 10.0 us: 1.02x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 64.1 ms: 1.04x slower                                                            |
| unpickle_list        | 2.98 us                                                         | 3.20 us: 1.07x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.3 us: 1.11x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.41 sec: 1.26x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 18.9 ms: 1.05x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.2 ms: 1.10x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 27.3 ms: 1.32x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 41.0 ms: 1.14x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 20.1 ms: 1.05x faster                                                            |
| mako            | 9.10 ms                                                         | 9.98 ms: 1.10x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.09x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.21 sec: 7.67x faster                                                           |
| pidigits                 | 502 ms                                                          | 138 ms: 3.64x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 132 us: 3.01x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 29.0 ms: 2.80x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 335 ms: 2.75x faster                                                             |
| async_tree_io            | 940 ms                                                          | 356 ms: 2.64x faster                                                             |
| async_tree_none          | 394 ms                                                          | 172 ms: 2.29x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 216 ms: 2.16x faster                                                             |
| pylint                   | 384 ms                                                          | 208 ms: 1.84x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.35 us: 1.70x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 441 ms: 1.69x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.42 ms: 1.67x faster                                                            |
| deepcopy                 | 310 us                                                          | 190 us: 1.63x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 6.11 ms: 1.61x faster                                                            |
| go                       | 146 ms                                                          | 91.4 ms: 1.59x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 61.5 ns: 1.59x faster                                                            |
| thrift                   | 902 us                                                          | 568 us: 1.59x faster                                                             |
| mdp                      | 1.83 sec                                                        | 1.16 sec: 1.57x faster                                                           |
| chaos                    | 74.4 ms                                                         | 47.8 ms: 1.56x faster                                                            |
| json                     | 4.76 ms                                                         | 3.09 ms: 1.54x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 19.5 us: 1.52x faster                                                            |
| float                    | 69.6 ms                                                         | 46.3 ms: 1.50x faster                                                            |
| comprehensions           | 17.7 us                                                         | 12.5 us: 1.42x faster                                                            |
| raytrace                 | 303 ms                                                          | 214 ms: 1.42x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 57.6 ms: 1.41x faster                                                            |
| json_loads               | 22.4 us                                                         | 16.0 us: 1.40x faster                                                            |
| generators               | 31.6 ms                                                         | 22.7 ms: 1.39x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 65.4 ms: 1.37x faster                                                            |
| pycparser                | 1.04 sec                                                        | 761 ms: 1.37x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 42.9 ms: 1.36x faster                                                            |
| pyflate                  | 422 ms                                                          | 316 ms: 1.34x faster                                                             |
| scimark_sor              | 115 ms                                                          | 87.1 ms: 1.32x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.65 ms: 1.32x faster                                                            |
| django_template          | 36.0 ms                                                         | 27.3 ms: 1.32x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.05 us: 1.31x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 92.9 ms: 1.29x faster                                                            |
| richards_super           | 49.9 ms                                                         | 39.1 ms: 1.28x faster                                                            |
| sympy_sum                | 122 ms                                                          | 97.0 ms: 1.26x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 41.3 ms: 1.26x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.3 ms: 1.25x faster                                                            |
| regex_compile            | 117 ms                                                          | 94.7 ms: 1.23x faster                                                            |
| sympy_expand             | 391 ms                                                          | 319 ms: 1.22x faster                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.9 ms: 1.22x faster                                                            |
| richards                 | 40.3 ms                                                         | 33.2 ms: 1.21x faster                                                            |
| sympy_str                | 229 ms                                                          | 189 ms: 1.21x faster                                                             |
| unpickle_pure_python     | 189 us                                                          | 157 us: 1.21x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 73.2 ms: 1.19x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 59.6 ms: 1.19x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.3 ms: 1.19x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 14.1 ms: 1.18x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 238 us: 1.18x faster                                                             |
| 2to3                     | 265 ms                                                          | 227 ms: 1.17x faster                                                             |
| pprint_safe_repr         | 658 ms                                                          | 565 ms: 1.17x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 70.1 ms: 1.14x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 41.0 ms: 1.14x faster                                                            |
| regex_dna                | 131 ms                                                          | 116 ms: 1.13x faster                                                             |
| logging_format           | 7.91 us                                                         | 7.22 us: 1.10x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.72 us: 1.08x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 44.8 ms: 1.07x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.59 ms: 1.05x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.07 us: 1.05x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.09 ms: 1.05x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 20.1 ms: 1.05x faster                                                            |
| fannkuch                 | 317 ms                                                          | 309 ms: 1.03x faster                                                             |
| scimark_fft              | 216 ms                                                          | 212 ms: 1.02x faster                                                             |
| telco                    | 4.83 ms                                                         | 4.80 ms: 1.01x faster                                                            |
| pickle                   | 7.83 us                                                         | 7.91 us: 1.01x slower                                                            |
| unpickle                 | 9.82 us                                                         | 10.0 us: 1.02x slower                                                            |
| nbody                    | 79.1 ms                                                         | 81.4 ms: 1.03x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 64.1 ms: 1.04x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 18.9 ms: 1.05x slower                                                            |
| unpack_sequence          | 40.0 ns                                                         | 42.1 ns: 1.05x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.20 us: 1.07x slower                                                            |
| mako                     | 9.10 ms                                                         | 9.98 ms: 1.10x slower                                                            |
| async_generators         | 241 ms                                                          | 265 ms: 1.10x slower                                                             |
| python_startup           | 22.9 ms                                                         | 25.2 ms: 1.10x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 88.2 ms: 1.10x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.3 us: 1.11x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 75.1 ms: 1.13x slower                                                            |
| tomli_loads              | 1.91 sec                                                        | 2.41 sec: 1.26x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.73 sec: 1.27x slower                                                           |
| coverage                 | 46.6 ms                                                         | 67.6 ms: 1.45x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.84 sec: 1.46x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.01 ms: 1.46x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.29x faster                                                                     |

Benchmark hidden because not significant (2): gc_traversal, bench_thread_pool
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250913-3.15.0a0-7168e98-NOGIL/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.291x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown