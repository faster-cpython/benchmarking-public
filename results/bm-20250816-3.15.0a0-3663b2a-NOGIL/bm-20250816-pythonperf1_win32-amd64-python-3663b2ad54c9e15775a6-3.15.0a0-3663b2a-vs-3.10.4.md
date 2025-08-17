# Results vs. 3.10.4

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.305x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 223 ms: 1.19x faster                                                             |
| docutils       | 1.95 sec                                                        | 2.75 sec: 1.41x slower                                                           |
| html5lib       | 52.1 ms                                                         | 40.9 ms: 1.27x faster                                                            |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 329 ms: 2.80x faster                                                             |
| async_tree_io           | 940 ms                                                          | 347 ms: 2.71x faster                                                             |
| async_tree_none         | 394 ms                                                          | 169 ms: 2.34x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 209 ms: 2.23x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.51x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 135 ms: 3.73x faster                                                             |
| float          | 69.6 ms                                                         | 46.1 ms: 1.51x faster                                                            |
| nbody          | 79.1 ms                                                         | 82.1 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                           | 1.76x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 93.0 ms: 1.25x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.2 ms: 1.19x faster                                                            |
| regex_dna      | 131 ms                                                          | 115 ms: 1.14x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.56 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.81 ms: 1.69x faster                                                            |
| json_loads           | 22.4 us                                                         | 16.1 us: 1.39x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 89.7 ms: 1.34x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 157 us: 1.21x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 60.3 ms: 1.17x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 240 us: 1.17x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 44.4 ms: 1.08x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.10 us: 1.04x faster                                                            |
| pickle               | 7.83 us                                                         | 7.70 us: 1.02x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 62.4 ms: 1.01x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.53 sec: 1.32x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                     |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.6 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 26.7 ms: 1.35x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 40.5 ms: 1.15x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 19.6 ms: 1.07x faster                                                            |
| mako            | 9.10 ms                                                         | 9.93 ms: 1.09x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.11x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.91 sec: 8.87x faster                                                           |
| pidigits                 | 502 ms                                                          | 135 ms: 3.73x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 129 us: 3.07x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 28.6 ms: 2.84x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 329 ms: 2.80x faster                                                             |
| async_tree_io            | 940 ms                                                          | 347 ms: 2.71x faster                                                             |
| async_tree_none          | 394 ms                                                          | 169 ms: 2.34x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 209 ms: 2.23x faster                                                             |
| pylint                   | 384 ms                                                          | 199 ms: 1.93x faster                                                             |
| mdp                      | 1.83 sec                                                        | 1.03 sec: 1.78x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 429 ms: 1.74x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.34 us: 1.72x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 5.81 ms: 1.69x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.45 ms: 1.65x faster                                                            |
| chaos                    | 74.4 ms                                                         | 45.5 ms: 1.64x faster                                                            |
| thrift                   | 902 us                                                          | 562 us: 1.61x faster                                                             |
| go                       | 146 ms                                                          | 91.2 ms: 1.60x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 61.3 ns: 1.60x faster                                                            |
| json                     | 4.76 ms                                                         | 3.12 ms: 1.53x faster                                                            |
| float                    | 69.6 ms                                                         | 46.1 ms: 1.51x faster                                                            |
| deepcopy                 | 310 us                                                          | 206 us: 1.51x faster                                                             |
| comprehensions           | 17.7 us                                                         | 12.0 us: 1.48x faster                                                            |
| raytrace                 | 303 ms                                                          | 206 ms: 1.47x faster                                                             |
| pycparser                | 1.04 sec                                                        | 720 ms: 1.45x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 56.8 ms: 1.43x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 41.0 ms: 1.43x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 21.0 us: 1.41x faster                                                            |
| json_loads               | 22.4 us                                                         | 16.1 us: 1.39x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 65.5 ms: 1.37x faster                                                            |
| pyflate                  | 422 ms                                                          | 311 ms: 1.36x faster                                                             |
| generators               | 31.6 ms                                                         | 23.4 ms: 1.35x faster                                                            |
| django_template          | 36.0 ms                                                         | 26.7 ms: 1.35x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.56 ms: 1.35x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 89.7 ms: 1.34x faster                                                            |
| scimark_sor              | 115 ms                                                          | 88.7 ms: 1.30x faster                                                            |
| sympy_sum                | 122 ms                                                          | 95.9 ms: 1.28x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 40.9 ms: 1.27x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.13 us: 1.26x faster                                                            |
| regex_compile            | 117 ms                                                          | 93.0 ms: 1.25x faster                                                            |
| richards_super           | 49.9 ms                                                         | 40.0 ms: 1.25x faster                                                            |
| sympy_str                | 229 ms                                                          | 185 ms: 1.24x faster                                                             |
| sympy_expand             | 391 ms                                                          | 316 ms: 1.24x faster                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.6 ms: 1.22x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 157 us: 1.21x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 13.9 ms: 1.20x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.2 ms: 1.19x faster                                                            |
| 2to3                     | 265 ms                                                          | 223 ms: 1.19x faster                                                             |
| coroutines               | 17.9 ms                                                         | 15.1 ms: 1.19x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 60.3 ms: 1.17x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 74.3 ms: 1.17x faster                                                            |
| richards                 | 40.3 ms                                                         | 34.3 ms: 1.17x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 240 us: 1.17x faster                                                             |
| pprint_safe_repr         | 658 ms                                                          | 565 ms: 1.16x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 40.5 ms: 1.15x faster                                                            |
| regex_dna                | 131 ms                                                          | 115 ms: 1.14x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 72.3 ms: 1.11x faster                                                            |
| logging_format           | 7.91 us                                                         | 7.16 us: 1.10x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.68 us: 1.09x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 44.4 ms: 1.08x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 37.3 ns: 1.07x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 19.6 ms: 1.07x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.56 ms: 1.07x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.04 ms: 1.07x faster                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.22 ms: 1.05x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.08 ms: 1.04x faster                                                            |
| fannkuch                 | 317 ms                                                          | 306 ms: 1.04x faster                                                             |
| pickle_list              | 3.22 us                                                         | 3.10 us: 1.04x faster                                                            |
| pickle                   | 7.83 us                                                         | 7.70 us: 1.02x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.88 ms: 1.01x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 62.4 ms: 1.01x slower                                                            |
| nbody                    | 79.1 ms                                                         | 82.1 ms: 1.04x slower                                                            |
| async_generators         | 241 ms                                                          | 255 ms: 1.06x slower                                                             |
| meteor_contest           | 80.0 ms                                                         | 85.8 ms: 1.07x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.47 sec: 1.07x slower                                                           |
| mako                     | 9.10 ms                                                         | 9.93 ms: 1.09x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.6 ms: 1.12x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 77.7 ms: 1.17x slower                                                            |
| tomli_loads              | 1.91 sec                                                        | 2.53 sec: 1.32x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.75 sec: 1.41x slower                                                           |
| coverage                 | 46.6 ms                                                         | 66.3 ms: 1.42x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.04 ms: 1.49x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.30x faster                                                                     |

Benchmark hidden because not significant (3): scimark_fft, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250816-3.15.0a0-3663b2a-NOGIL/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.305x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown