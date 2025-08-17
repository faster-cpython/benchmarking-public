# Results vs. 3.10.4

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.502x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 216 ms: 1.23x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.62 sec: 1.20x faster                                                           |
| html5lib       | 52.1 ms                                                         | 37.8 ms: 1.38x faster                                                            |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 330 ms: 2.79x faster                                                             |
| async_tree_io           | 940 ms                                                          | 389 ms: 2.42x faster                                                             |
| async_tree_none         | 394 ms                                                          | 172 ms: 2.29x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.44x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 145 ms: 3.47x faster                                                             |
| float          | 69.6 ms                                                         | 43.9 ms: 1.59x faster                                                            |
| nbody          | 79.1 ms                                                         | 54.6 ms: 1.45x faster                                                            |
| Geometric mean | (ref)                                                           | 2.00x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 78.0 ms: 1.50x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.1 ms: 1.21x faster                                                            |
| regex_dna      | 131 ms                                                          | 114 ms: 1.15x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.52 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.39 ms: 1.82x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 105 us: 1.80x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.10 sec: 1.73x faster                                                           |
| json_loads           | 22.4 us                                                         | 14.2 us: 1.58x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 199 us: 1.40x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 87.7 ms: 1.37x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 35.2 ms: 1.37x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 50.2 ms: 1.23x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.39 us: 1.17x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.1 ms: 1.16x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.75 us: 1.09x faster                                                            |
| pickle               | 7.83 us                                                         | 7.43 us: 1.05x faster                                                            |
| pickle_dict          | 18.2 us                                                         | 20.0 us: 1.10x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.30x faster                                                                     |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.3 ms: 1.10x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.20 ms: 1.75x faster                                                            |
| django_template | 36.0 ms                                                         | 23.9 ms: 1.51x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.7 ms: 1.34x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.9 ms: 1.34x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.25 sec: 13.62x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 104 us: 3.79x faster                                                             |
| pidigits                 | 502 ms                                                          | 145 ms: 3.47x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 330 ms: 2.79x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 29.1 ms: 2.79x faster                                                            |
| async_tree_io            | 940 ms                                                          | 389 ms: 2.42x faster                                                             |
| async_tree_none          | 394 ms                                                          | 172 ms: 2.29x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| mdp                      | 1.83 sec                                                        | 801 ms: 2.28x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 373 ms: 2.00x faster                                                             |
| pylint                   | 384 ms                                                          | 194 ms: 1.98x faster                                                             |
| go                       | 146 ms                                                          | 77.2 ms: 1.89x faster                                                            |
| chaos                    | 74.4 ms                                                         | 40.2 ms: 1.85x faster                                                            |
| deepcopy                 | 310 us                                                          | 168 us: 1.85x faster                                                             |
| thrift                   | 902 us                                                          | 495 us: 1.82x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 5.39 ms: 1.82x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 44.8 ms: 1.82x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.22 ms: 1.81x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 105 us: 1.80x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 55.2 ns: 1.77x faster                                                            |
| mako                     | 9.10 ms                                                         | 5.20 ms: 1.75x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.10 sec: 1.73x faster                                                           |
| raytrace                 | 303 ms                                                          | 178 ms: 1.70x faster                                                             |
| comprehensions           | 17.7 us                                                         | 10.5 us: 1.68x faster                                                            |
| generators               | 31.6 ms                                                         | 18.9 ms: 1.67x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 17.8 us: 1.67x faster                                                            |
| json                     | 4.76 ms                                                         | 2.89 ms: 1.65x faster                                                            |
| richards_super           | 49.9 ms                                                         | 30.6 ms: 1.63x faster                                                            |
| pyflate                  | 422 ms                                                          | 260 ms: 1.62x faster                                                             |
| float                    | 69.6 ms                                                         | 43.9 ms: 1.59x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.2 us: 1.58x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 3.99 ms: 1.54x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 891 ms: 1.54x faster                                                             |
| scimark_lu               | 89.8 ms                                                         | 58.6 ms: 1.53x faster                                                            |
| fannkuch                 | 317 ms                                                          | 207 ms: 1.53x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.51 us: 1.52x faster                                                            |
| pycparser                | 1.04 sec                                                        | 688 ms: 1.52x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 38.7 ms: 1.51x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 436 ms: 1.51x faster                                                             |
| django_template          | 36.0 ms                                                         | 23.9 ms: 1.51x faster                                                            |
| regex_compile            | 117 ms                                                          | 78.0 ms: 1.50x faster                                                            |
| richards                 | 40.3 ms                                                         | 26.9 ms: 1.49x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 42.1 ms: 1.47x faster                                                            |
| scimark_sor              | 115 ms                                                          | 78.2 ms: 1.47x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.83 us: 1.47x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.21 ms: 1.46x faster                                                            |
| scimark_fft              | 216 ms                                                          | 149 ms: 1.45x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 60.0 ms: 1.45x faster                                                            |
| nbody                    | 79.1 ms                                                         | 54.6 ms: 1.45x faster                                                            |
| sympy_sum                | 122 ms                                                          | 85.7 ms: 1.43x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 199 us: 1.40x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 37.8 ms: 1.38x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 87.7 ms: 1.37x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 35.2 ms: 1.37x faster                                                            |
| sympy_str                | 229 ms                                                          | 168 ms: 1.36x faster                                                             |
| sympy_expand             | 391 ms                                                          | 290 ms: 1.35x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 833 us: 1.34x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.4 ms: 1.34x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.7 ms: 1.34x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 34.9 ms: 1.34x faster                                                            |
| coroutines               | 17.9 ms                                                         | 13.8 ms: 1.30x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 32.5 ns: 1.23x faster                                                            |
| 2to3                     | 265 ms                                                          | 216 ms: 1.23x faster                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 50.2 ms: 1.23x faster                                                            |
| telco                    | 4.83 ms                                                         | 3.94 ms: 1.23x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.47 us: 1.22x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 65.7 ms: 1.22x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.04 us: 1.21x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.1 ms: 1.21x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.62 sec: 1.20x faster                                                           |
| unpickle                 | 9.82 us                                                         | 8.39 us: 1.17x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.1 ms: 1.16x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 69.1 ms: 1.16x faster                                                            |
| regex_dna                | 131 ms                                                          | 114 ms: 1.15x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.52 ms: 1.09x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.75 us: 1.09x faster                                                            |
| pickle                   | 7.83 us                                                         | 7.43 us: 1.05x faster                                                            |
| async_generators         | 241 ms                                                          | 238 ms: 1.01x faster                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.7 ms: 1.07x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.0 us: 1.10x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.3 ms: 1.10x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 92.8 ms: 1.40x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.20 ms: 1.72x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.31 ms: 1.89x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.50x faster                                                                     |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.502x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.46x
- 95% likely to have a speedup of 1.44x
- 99% likely to have a speedup of 1.41x

# Memory
- memory change: unknown