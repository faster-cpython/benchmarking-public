# Results vs. 3.10.4

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.524x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.42x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 214 ms: 1.24x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.61 sec: 1.21x faster                                                           |
| html5lib       | 52.1 ms                                                         | 38.0 ms: 1.37x faster                                                            |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 327 ms: 2.82x faster                                                             |
| async_tree_io           | 940 ms                                                          | 380 ms: 2.48x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 198 ms: 2.35x faster                                                             |
| async_tree_none         | 394 ms                                                          | 168 ms: 2.34x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.49x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 149 ms: 3.38x faster                                                             |
| float          | 69.6 ms                                                         | 43.5 ms: 1.60x faster                                                            |
| nbody          | 79.1 ms                                                         | 53.1 ms: 1.49x faster                                                            |
| Geometric mean | (ref)                                                           | 2.01x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 76.9 ms: 1.52x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.3 ms: 1.19x faster                                                            |
| regex_dna      | 131 ms                                                          | 115 ms: 1.13x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.55 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                          | 103 us: 1.84x faster                                                             |
| json_dumps           | 9.82 ms                                                         | 5.35 ms: 1.84x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.08 sec: 1.77x faster                                                           |
| json_loads           | 22.4 us                                                         | 13.7 us: 1.63x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 196 us: 1.43x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 84.5 ms: 1.42x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 34.6 ms: 1.39x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 50.8 ms: 1.21x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.5 ms: 1.15x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.65 us: 1.14x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.69 us: 1.11x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.26 us: 1.02x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.2 us: 1.11x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.31x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 18.8 ms: 1.04x slower                                                            |
| python_startup         | 22.9 ms                                                         | 24.8 ms: 1.08x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.27 ms: 1.73x faster                                                            |
| django_template | 36.0 ms                                                         | 24.7 ms: 1.46x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 33.9 ms: 1.37x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.5 ms: 1.35x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.37 sec: 12.39x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 103 us: 3.86x faster                                                             |
| pidigits                 | 502 ms                                                          | 149 ms: 3.38x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 28.6 ms: 2.84x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 327 ms: 2.82x faster                                                             |
| async_tree_io            | 940 ms                                                          | 380 ms: 2.48x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 198 ms: 2.35x faster                                                             |
| async_tree_none          | 394 ms                                                          | 168 ms: 2.34x faster                                                             |
| mdp                      | 1.83 sec                                                        | 789 ms: 2.31x faster                                                             |
| pylint                   | 384 ms                                                          | 193 ms: 1.99x faster                                                             |
| go                       | 146 ms                                                          | 74.7 ms: 1.95x faster                                                            |
| richards_super           | 49.9 ms                                                         | 26.2 ms: 1.91x faster                                                            |
| deepcopy                 | 310 us                                                          | 163 us: 1.90x faster                                                             |
| chaos                    | 74.4 ms                                                         | 39.7 ms: 1.87x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.15 ms: 1.87x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 103 us: 1.84x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 5.35 ms: 1.84x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 53.4 ns: 1.83x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 44.7 ms: 1.82x faster                                                            |
| richards                 | 40.3 ms                                                         | 22.2 ms: 1.82x faster                                                            |
| thrift                   | 902 us                                                          | 498 us: 1.81x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 16.4 us: 1.80x faster                                                            |
| raytrace                 | 303 ms                                                          | 170 ms: 1.78x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.08 sec: 1.77x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.27 ms: 1.73x faster                                                            |
| comprehensions           | 17.7 us                                                         | 10.6 us: 1.68x faster                                                            |
| pyflate                  | 422 ms                                                          | 253 ms: 1.67x faster                                                             |
| generators               | 31.6 ms                                                         | 19.1 ms: 1.66x faster                                                            |
| json                     | 4.76 ms                                                         | 2.90 ms: 1.64x faster                                                            |
| json_loads               | 22.4 us                                                         | 13.7 us: 1.63x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 841 ms: 1.63x faster                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 38.5 ms: 1.61x faster                                                            |
| float                    | 69.6 ms                                                         | 43.5 ms: 1.60x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 412 ms: 1.60x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 484 ms: 1.54x faster                                                             |
| deepcopy_reduce          | 2.68 us                                                         | 1.76 us: 1.52x faster                                                            |
| scimark_sor              | 115 ms                                                          | 75.8 ms: 1.52x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 59.1 ms: 1.52x faster                                                            |
| regex_compile            | 117 ms                                                          | 76.9 ms: 1.52x faster                                                            |
| pycparser                | 1.04 sec                                                        | 687 ms: 1.52x faster                                                             |
| fannkuch                 | 317 ms                                                          | 209 ms: 1.52x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.51 us: 1.51x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.07 ms: 1.51x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 38.8 ms: 1.51x faster                                                            |
| nbody                    | 79.1 ms                                                         | 53.1 ms: 1.49x faster                                                            |
| scimark_fft              | 216 ms                                                          | 146 ms: 1.48x faster                                                             |
| django_template          | 36.0 ms                                                         | 24.7 ms: 1.46x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 60.6 ms: 1.44x faster                                                            |
| sympy_sum                | 122 ms                                                          | 85.2 ms: 1.44x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 196 us: 1.43x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.28 ms: 1.42x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 84.5 ms: 1.42x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 34.6 ms: 1.39x faster                                                            |
| sympy_str                | 229 ms                                                          | 166 ms: 1.38x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 33.9 ms: 1.37x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 38.0 ms: 1.37x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.5 ms: 1.35x faster                                                            |
| sympy_expand             | 391 ms                                                          | 289 ms: 1.35x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.4 ms: 1.34x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 843 us: 1.33x faster                                                             |
| telco                    | 4.83 ms                                                         | 3.74 ms: 1.29x faster                                                            |
| 2to3                     | 265 ms                                                          | 214 ms: 1.24x faster                                                             |
| logging_format           | 7.91 us                                                         | 6.43 us: 1.23x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 32.8 ns: 1.22x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 66.0 ms: 1.21x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 50.8 ms: 1.21x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.61 sec: 1.21x faster                                                           |
| logging_simple           | 7.29 us                                                         | 6.01 us: 1.21x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.3 ms: 1.19x faster                                                            |
| coroutines               | 17.9 ms                                                         | 15.3 ms: 1.18x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.5 ms: 1.15x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.65 us: 1.14x faster                                                            |
| regex_dna                | 131 ms                                                          | 115 ms: 1.13x faster                                                             |
| meteor_contest           | 80.0 ms                                                         | 71.8 ms: 1.12x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.69 us: 1.11x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.55 ms: 1.08x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.26 us: 1.02x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 18.8 ms: 1.04x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.5 ms: 1.06x slower                                                            |
| python_startup           | 22.9 ms                                                         | 24.8 ms: 1.08x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.2 us: 1.11x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 87.9 ms: 1.33x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.09 ms: 1.63x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.27 ms: 1.84x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.51x faster                                                                     |

Benchmark hidden because not significant (2): pickle, async_generators
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.524x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.47x
- 95% likely to have a speedup of 1.45x
- 99% likely to have a speedup of 1.42x

# Memory
- memory change: unknown