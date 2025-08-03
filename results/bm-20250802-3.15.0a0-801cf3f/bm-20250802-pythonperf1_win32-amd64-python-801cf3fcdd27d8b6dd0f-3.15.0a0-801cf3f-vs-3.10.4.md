# Results vs. 3.10.4

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.414x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 227 ms: 1.17x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.61 sec: 1.21x faster                                                           |
| html5lib       | 52.1 ms                                                         | 39.5 ms: 1.32x faster                                                            |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 339 ms: 2.72x faster                                                             |
| async_tree_io           | 940 ms                                                          | 398 ms: 2.36x faster                                                             |
| async_tree_none         | 394 ms                                                          | 183 ms: 2.15x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 218 ms: 2.14x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.34x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 146 ms: 3.44x faster                                                             |
| float          | 69.6 ms                                                         | 43.5 ms: 1.60x faster                                                            |
| nbody          | 79.1 ms                                                         | 65.3 ms: 1.21x faster                                                            |
| Geometric mean | (ref)                                                           | 1.88x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 81.0 ms: 1.44x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 14.5 ms: 1.09x faster                                                            |
| regex_dna      | 131 ms                                                          | 121 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.35 ms: 1.55x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.6 us: 1.54x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 134 us: 1.41x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.42 sec: 1.34x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 212 us: 1.32x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 90.8 ms: 1.32x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 40.0 ms: 1.20x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.74 us: 1.12x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.1 ms: 1.07x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 58.0 ms: 1.06x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.83 us: 1.06x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.36 us: 1.05x slower                                                            |
| pickle               | 7.83 us                                                         | 8.36 us: 1.07x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.6 us: 1.13x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                            |
| python_startup         | 22.9 ms                                                         | 27.2 ms: 1.18x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.16x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 24.6 ms: 1.46x faster                                                            |
| mako            | 9.10 ms                                                         | 6.67 ms: 1.36x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.7 ms: 1.34x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 35.2 ms: 1.32x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.37x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.30 sec: 13.04x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 102 us: 3.88x faster                                                             |
| pidigits                 | 502 ms                                                          | 146 ms: 3.44x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 339 ms: 2.72x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 33.0 ms: 2.46x faster                                                            |
| async_tree_io            | 940 ms                                                          | 398 ms: 2.36x faster                                                             |
| mdp                      | 1.83 sec                                                        | 824 ms: 2.22x faster                                                             |
| async_tree_none          | 394 ms                                                          | 183 ms: 2.15x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 218 ms: 2.14x faster                                                             |
| pylint                   | 384 ms                                                          | 199 ms: 1.93x faster                                                             |
| go                       | 146 ms                                                          | 77.1 ms: 1.89x faster                                                            |
| chaos                    | 74.4 ms                                                         | 41.3 ms: 1.80x faster                                                            |
| thrift                   | 902 us                                                          | 504 us: 1.79x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.27 ms: 1.78x faster                                                            |
| deepcopy                 | 310 us                                                          | 175 us: 1.77x faster                                                             |
| raytrace                 | 303 ms                                                          | 181 ms: 1.67x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 58.6 ns: 1.67x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 448 ms: 1.66x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 49.2 ms: 1.65x faster                                                            |
| comprehensions           | 17.7 us                                                         | 10.8 us: 1.64x faster                                                            |
| generators               | 31.6 ms                                                         | 19.4 ms: 1.63x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 18.4 us: 1.61x faster                                                            |
| float                    | 69.6 ms                                                         | 43.5 ms: 1.60x faster                                                            |
| richards_super           | 49.9 ms                                                         | 32.1 ms: 1.55x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.35 ms: 1.55x faster                                                            |
| json                     | 4.76 ms                                                         | 3.09 ms: 1.54x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.6 us: 1.54x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 60.2 ms: 1.49x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.9 ms: 1.48x faster                                                            |
| scimark_sor              | 115 ms                                                          | 78.2 ms: 1.47x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.19 ms: 1.46x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.6 ms: 1.46x faster                                                            |
| pyflate                  | 422 ms                                                          | 289 ms: 1.46x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.58 us: 1.45x faster                                                            |
| regex_compile            | 117 ms                                                          | 81.0 ms: 1.44x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 41.1 ms: 1.42x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 134 us: 1.41x faster                                                             |
| pycparser                | 1.04 sec                                                        | 739 ms: 1.41x faster                                                             |
| deepcopy_reduce          | 2.68 us                                                         | 1.91 us: 1.41x faster                                                            |
| richards                 | 40.3 ms                                                         | 29.0 ms: 1.39x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 63.5 ms: 1.37x faster                                                            |
| sympy_sum                | 122 ms                                                          | 89.5 ms: 1.37x faster                                                            |
| mako                     | 9.10 ms                                                         | 6.67 ms: 1.36x faster                                                            |
| sympy_expand             | 391 ms                                                          | 288 ms: 1.36x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.42 sec: 1.34x faster                                                           |
| sympy_str                | 229 ms                                                          | 171 ms: 1.34x faster                                                             |
| genshi_text              | 21.0 ms                                                         | 15.7 ms: 1.34x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.03 sec: 1.33x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 212 us: 1.32x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.6 ms: 1.32x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 35.2 ms: 1.32x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 90.8 ms: 1.32x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 39.5 ms: 1.32x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 509 ms: 1.29x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 868 us: 1.29x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.60 ms: 1.25x faster                                                            |
| fannkuch                 | 317 ms                                                          | 256 ms: 1.24x faster                                                             |
| nbody                    | 79.1 ms                                                         | 65.3 ms: 1.21x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.61 sec: 1.21x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 40.0 ms: 1.20x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.9 ms: 1.20x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 67.2 ms: 1.19x faster                                                            |
| scimark_fft              | 216 ms                                                          | 184 ms: 1.17x faster                                                             |
| logging_format           | 7.91 us                                                         | 6.76 us: 1.17x faster                                                            |
| 2to3                     | 265 ms                                                          | 227 ms: 1.17x faster                                                             |
| logging_simple           | 7.29 us                                                         | 6.34 us: 1.15x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.74 us: 1.12x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 72.2 ms: 1.11x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.5 ms: 1.09x faster                                                            |
| regex_dna                | 131 ms                                                          | 121 ms: 1.08x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.1 ms: 1.07x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 37.5 ns: 1.07x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 58.0 ms: 1.06x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.83 us: 1.06x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.61 ms: 1.05x faster                                                            |
| async_generators         | 241 ms                                                          | 237 ms: 1.02x faster                                                             |
| pickle_list              | 3.22 us                                                         | 3.36 us: 1.05x slower                                                            |
| pickle                   | 7.83 us                                                         | 8.36 us: 1.07x slower                                                            |
| coverage                 | 46.6 ms                                                         | 51.3 ms: 1.10x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.6 us: 1.13x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                            |
| python_startup           | 22.9 ms                                                         | 27.2 ms: 1.18x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 96.9 ms: 1.46x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.10 ms: 1.64x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.33 ms: 1.91x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.40x faster                                                                     |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.414x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: unknown