# Results vs. 3.10.4

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.408x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 227 ms: 1.17x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.64 sec: 1.19x faster                                                           |
| html5lib       | 52.1 ms                                                         | 38.9 ms: 1.34x faster                                                            |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 338 ms: 2.73x faster                                                             |
| async_tree_io           | 940 ms                                                          | 394 ms: 2.39x faster                                                             |
| async_tree_none         | 394 ms                                                          | 179 ms: 2.20x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 213 ms: 2.19x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.37x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 150 ms: 3.35x faster                                                             |
| float          | 69.6 ms                                                         | 44.9 ms: 1.55x faster                                                            |
| nbody          | 79.1 ms                                                         | 67.9 ms: 1.16x faster                                                            |
| Geometric mean | (ref)                                                           | 1.82x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 81.5 ms: 1.43x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 14.6 ms: 1.08x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.55 ms: 1.08x faster                                                            |
| regex_dna      | 131 ms                                                          | 126 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.52 ms: 1.51x faster                                                            |
| json_loads           | 22.4 us                                                         | 15.0 us: 1.49x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 136 us: 1.39x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 89.6 ms: 1.34x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.44 sec: 1.32x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 223 us: 1.26x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 40.2 ms: 1.20x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.80 us: 1.12x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 57.8 ms: 1.07x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.7 ms: 1.06x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.95 us: 1.01x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.39 us: 1.05x slower                                                            |
| pickle               | 7.83 us                                                         | 8.31 us: 1.06x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.3 us: 1.11x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                            |
| python_startup         | 22.9 ms                                                         | 26.6 ms: 1.16x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 25.4 ms: 1.42x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.6 ms: 1.35x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.9 ms: 1.33x faster                                                            |
| mako            | 9.10 ms                                                         | 6.84 ms: 1.33x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.36x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.31 sec: 12.99x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 104 us: 3.82x faster                                                             |
| pidigits                 | 502 ms                                                          | 150 ms: 3.35x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 338 ms: 2.73x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 33.5 ms: 2.42x faster                                                            |
| async_tree_io            | 940 ms                                                          | 394 ms: 2.39x faster                                                             |
| mdp                      | 1.83 sec                                                        | 819 ms: 2.23x faster                                                             |
| async_tree_none          | 394 ms                                                          | 179 ms: 2.20x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 213 ms: 2.19x faster                                                             |
| pylint                   | 384 ms                                                          | 201 ms: 1.91x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 396 ms: 1.88x faster                                                             |
| go                       | 146 ms                                                          | 77.6 ms: 1.88x faster                                                            |
| deepcopy                 | 310 us                                                          | 173 us: 1.79x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.29 ms: 1.76x faster                                                            |
| thrift                   | 902 us                                                          | 514 us: 1.76x faster                                                             |
| chaos                    | 74.4 ms                                                         | 42.7 ms: 1.74x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 47.8 ms: 1.70x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 57.9 ns: 1.69x faster                                                            |
| raytrace                 | 303 ms                                                          | 181 ms: 1.67x faster                                                             |
| generators               | 31.6 ms                                                         | 19.7 ms: 1.60x faster                                                            |
| richards_super           | 49.9 ms                                                         | 31.8 ms: 1.57x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 19.0 us: 1.56x faster                                                            |
| json                     | 4.76 ms                                                         | 3.07 ms: 1.55x faster                                                            |
| float                    | 69.6 ms                                                         | 44.9 ms: 1.55x faster                                                            |
| comprehensions           | 17.7 us                                                         | 11.5 us: 1.55x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.52 ms: 1.51x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.2 ms: 1.50x faster                                                            |
| json_loads               | 22.4 us                                                         | 15.0 us: 1.49x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.13 ms: 1.48x faster                                                            |
| pyflate                  | 422 ms                                                          | 286 ms: 1.47x faster                                                             |
| scimark_sor              | 115 ms                                                          | 78.6 ms: 1.46x faster                                                            |
| pycparser                | 1.04 sec                                                        | 717 ms: 1.45x faster                                                             |
| richards                 | 40.3 ms                                                         | 27.8 ms: 1.45x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.58 us: 1.45x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.87 us: 1.44x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 40.8 ms: 1.43x faster                                                            |
| regex_compile            | 117 ms                                                          | 81.5 ms: 1.43x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 63.2 ms: 1.42x faster                                                            |
| django_template          | 36.0 ms                                                         | 25.4 ms: 1.42x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 136 us: 1.39x faster                                                             |
| sympy_sum                | 122 ms                                                          | 87.9 ms: 1.39x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 63.8 ms: 1.37x faster                                                            |
| sympy_expand             | 391 ms                                                          | 287 ms: 1.36x faster                                                             |
| pprint_pformat           | 1.37 sec                                                        | 1.01 sec: 1.35x faster                                                           |
| genshi_text              | 21.0 ms                                                         | 15.6 ms: 1.35x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 89.6 ms: 1.34x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 38.9 ms: 1.34x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 34.9 ms: 1.33x faster                                                            |
| mako                     | 9.10 ms                                                         | 6.84 ms: 1.33x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 496 ms: 1.33x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.44 sec: 1.32x faster                                                           |
| sympy_str                | 229 ms                                                          | 173 ms: 1.32x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.6 ms: 1.32x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 861 us: 1.30x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 223 us: 1.26x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 63.9 ms: 1.25x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.59 ms: 1.25x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.6 ms: 1.23x faster                                                            |
| fannkuch                 | 317 ms                                                          | 261 ms: 1.21x faster                                                             |
| xml_etree_process        | 48.1 ms                                                         | 40.2 ms: 1.20x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.64 sec: 1.19x faster                                                           |
| 2to3                     | 265 ms                                                          | 227 ms: 1.17x faster                                                             |
| nbody                    | 79.1 ms                                                         | 67.9 ms: 1.16x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.79 us: 1.16x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.27 us: 1.16x faster                                                            |
| scimark_fft              | 216 ms                                                          | 190 ms: 1.14x faster                                                             |
| unpickle                 | 9.82 us                                                         | 8.80 us: 1.12x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.6 ms: 1.08x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.55 ms: 1.08x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 57.8 ms: 1.07x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 37.6 ns: 1.06x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.7 ms: 1.06x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 75.5 ms: 1.06x faster                                                            |
| regex_dna                | 131 ms                                                          | 126 ms: 1.04x faster                                                             |
| unpickle_list            | 2.98 us                                                         | 2.95 us: 1.01x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.39 us: 1.05x slower                                                            |
| pickle                   | 7.83 us                                                         | 8.31 us: 1.06x slower                                                            |
| coverage                 | 46.6 ms                                                         | 50.5 ms: 1.08x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.3 us: 1.11x slower                                                            |
| python_startup           | 22.9 ms                                                         | 26.6 ms: 1.16x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 96.1 ms: 1.45x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.20 ms: 1.72x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.32 ms: 1.90x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.40x faster                                                                     |

Benchmark hidden because not significant (2): telco, async_generators
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.408x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: unknown