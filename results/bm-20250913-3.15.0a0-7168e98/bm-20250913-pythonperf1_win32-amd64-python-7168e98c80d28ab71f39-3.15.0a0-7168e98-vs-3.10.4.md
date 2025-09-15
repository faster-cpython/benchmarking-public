# Results vs. 3.10.4

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.454x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 216 ms: 1.23x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.61 sec: 1.21x faster                                                           |
| html5lib       | 52.1 ms                                                         | 38.5 ms: 1.35x faster                                                            |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 324 ms: 2.84x faster                                                             |
| async_tree_io           | 940 ms                                                          | 388 ms: 2.42x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 199 ms: 2.34x faster                                                             |
| async_tree_none         | 394 ms                                                          | 172 ms: 2.29x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.47x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 148 ms: 3.39x faster                                                             |
| float          | 69.6 ms                                                         | 42.7 ms: 1.63x faster                                                            |
| nbody          | 79.1 ms                                                         | 65.3 ms: 1.21x faster                                                            |
| Geometric mean | (ref)                                                           | 1.89x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 79.8 ms: 1.46x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 14.4 ms: 1.10x faster                                                            |
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.61 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.46 ms: 1.80x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.3 us: 1.57x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.35 sec: 1.42x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 135 us: 1.40x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 88.9 ms: 1.35x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 212 us: 1.32x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 38.7 ms: 1.24x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.52 us: 1.15x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 55.4 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.9 ms: 1.11x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.84 us: 1.05x faster                                                            |
| pickle               | 7.83 us                                                         | 7.76 us: 1.01x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.27 us: 1.02x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.7 us: 1.08x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 18.9 ms: 1.04x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.5 ms: 1.11x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 24.5 ms: 1.47x faster                                                            |
| mako            | 9.10 ms                                                         | 6.51 ms: 1.40x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.8 ms: 1.33x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 35.2 ms: 1.32x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.38x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.32 sec: 12.84x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 104 us: 3.79x faster                                                             |
| pidigits                 | 502 ms                                                          | 148 ms: 3.39x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 324 ms: 2.84x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 28.8 ms: 2.82x faster                                                            |
| async_tree_io            | 940 ms                                                          | 388 ms: 2.42x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 199 ms: 2.34x faster                                                             |
| async_tree_none          | 394 ms                                                          | 172 ms: 2.29x faster                                                             |
| mdp                      | 1.83 sec                                                        | 810 ms: 2.25x faster                                                             |
| pylint                   | 384 ms                                                          | 195 ms: 1.97x faster                                                             |
| go                       | 146 ms                                                          | 75.7 ms: 1.92x faster                                                            |
| deepcopy                 | 310 us                                                          | 165 us: 1.88x faster                                                             |
| chaos                    | 74.4 ms                                                         | 40.4 ms: 1.84x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.21 ms: 1.83x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 5.46 ms: 1.80x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 16.5 us: 1.80x faster                                                            |
| thrift                   | 902 us                                                          | 503 us: 1.79x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 56.5 ns: 1.73x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 47.6 ms: 1.71x faster                                                            |
| raytrace                 | 303 ms                                                          | 178 ms: 1.70x faster                                                             |
| generators               | 31.6 ms                                                         | 19.3 ms: 1.64x faster                                                            |
| json                     | 4.76 ms                                                         | 2.91 ms: 1.63x faster                                                            |
| float                    | 69.6 ms                                                         | 42.7 ms: 1.63x faster                                                            |
| comprehensions           | 17.7 us                                                         | 10.9 us: 1.62x faster                                                            |
| richards_super           | 49.9 ms                                                         | 31.0 ms: 1.61x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.3 ms: 1.58x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.3 us: 1.57x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 57.7 ms: 1.56x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.00 ms: 1.53x faster                                                            |
| scimark_sor              | 115 ms                                                          | 76.1 ms: 1.51x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 494 ms: 1.50x faster                                                             |
| pyflate                  | 422 ms                                                          | 282 ms: 1.50x faster                                                             |
| richards                 | 40.3 ms                                                         | 27.0 ms: 1.49x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.80 us: 1.49x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.5 ms: 1.47x faster                                                            |
| pycparser                | 1.04 sec                                                        | 710 ms: 1.47x faster                                                             |
| regex_compile            | 117 ms                                                          | 79.8 ms: 1.46x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.57 us: 1.46x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 40.4 ms: 1.45x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.35 sec: 1.42x faster                                                           |
| sympy_sum                | 122 ms                                                          | 86.8 ms: 1.41x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 61.8 ms: 1.41x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 135 us: 1.40x faster                                                             |
| mako                     | 9.10 ms                                                         | 6.51 ms: 1.40x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 992 ms: 1.38x faster                                                             |
| sympy_str                | 229 ms                                                          | 168 ms: 1.37x faster                                                             |
| sympy_expand             | 391 ms                                                          | 286 ms: 1.37x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 38.5 ms: 1.35x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 88.9 ms: 1.35x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 488 ms: 1.35x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.4 ms: 1.35x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.8 ms: 1.33x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 35.2 ms: 1.32x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 212 us: 1.32x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 861 us: 1.30x faster                                                             |
| unpack_sequence          | 40.0 ns                                                         | 31.1 ns: 1.29x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.55 ms: 1.27x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 63.4 ms: 1.26x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 38.7 ms: 1.24x faster                                                            |
| 2to3                     | 265 ms                                                          | 216 ms: 1.23x faster                                                             |
| coroutines               | 17.9 ms                                                         | 14.7 ms: 1.22x faster                                                            |
| scimark_fft              | 216 ms                                                          | 178 ms: 1.21x faster                                                             |
| nbody                    | 79.1 ms                                                         | 65.3 ms: 1.21x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.61 sec: 1.21x faster                                                           |
| logging_format           | 7.91 us                                                         | 6.55 us: 1.21x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.08 us: 1.20x faster                                                            |
| fannkuch                 | 317 ms                                                          | 268 ms: 1.18x faster                                                             |
| unpickle                 | 9.82 us                                                         | 8.52 us: 1.15x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.23 ms: 1.14x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 55.4 ms: 1.11x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 72.2 ms: 1.11x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.9 ms: 1.11x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.4 ms: 1.10x faster                                                            |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                             |
| async_generators         | 241 ms                                                          | 227 ms: 1.06x faster                                                             |
| unpickle_list            | 2.98 us                                                         | 2.84 us: 1.05x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.61 ms: 1.03x faster                                                            |
| pickle                   | 7.83 us                                                         | 7.76 us: 1.01x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.27 us: 1.02x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 18.9 ms: 1.04x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.7 us: 1.08x slower                                                            |
| coverage                 | 46.6 ms                                                         | 50.8 ms: 1.09x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.5 ms: 1.11x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 89.9 ms: 1.35x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.06 ms: 1.61x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.29 ms: 1.85x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.45x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.454x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: unknown