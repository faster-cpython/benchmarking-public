# Results vs. 3.10.4

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.462x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 218 ms: 1.22x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.59 sec: 1.23x faster                                                           |
| html5lib       | 52.1 ms                                                         | 37.3 ms: 1.39x faster                                                            |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 328 ms: 2.81x faster                                                             |
| async_tree_io           | 940 ms                                                          | 383 ms: 2.45x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| async_tree_none         | 394 ms                                                          | 172 ms: 2.28x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.45x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 144 ms: 3.49x faster                                                             |
| float          | 69.6 ms                                                         | 42.6 ms: 1.63x faster                                                            |
| nbody          | 79.1 ms                                                         | 63.5 ms: 1.25x faster                                                            |
| Geometric mean | (ref)                                                           | 1.92x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 79.0 ms: 1.48x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.9 ms: 1.14x faster                                                            |
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.52 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.43 ms: 1.81x faster                                                            |
| json_loads           | 22.4 us                                                         | 13.9 us: 1.61x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 133 us: 1.43x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 87.6 ms: 1.37x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.42 sec: 1.35x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 212 us: 1.32x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 38.8 ms: 1.24x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.50 us: 1.16x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.3 ms: 1.10x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 56.6 ms: 1.09x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.88 us: 1.04x faster                                                            |
| pickle               | 7.83 us                                                         | 7.93 us: 1.01x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.27 us: 1.02x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.22x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.3 ms: 1.10x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 24.5 ms: 1.47x faster                                                            |
| mako            | 9.10 ms                                                         | 6.58 ms: 1.38x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.3 ms: 1.37x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.5 ms: 1.35x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.39x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.23 sec: 13.75x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 105 us: 3.78x faster                                                             |
| pidigits                 | 502 ms                                                          | 144 ms: 3.49x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 28.5 ms: 2.85x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 328 ms: 2.81x faster                                                             |
| async_tree_io            | 940 ms                                                          | 383 ms: 2.45x faster                                                             |
| mdp                      | 1.83 sec                                                        | 794 ms: 2.30x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| async_tree_none          | 394 ms                                                          | 172 ms: 2.28x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 369 ms: 2.02x faster                                                             |
| pylint                   | 384 ms                                                          | 193 ms: 1.99x faster                                                             |
| go                       | 146 ms                                                          | 76.6 ms: 1.90x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.18 ms: 1.86x faster                                                            |
| chaos                    | 74.4 ms                                                         | 40.3 ms: 1.85x faster                                                            |
| deepcopy                 | 310 us                                                          | 169 us: 1.84x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 5.43 ms: 1.81x faster                                                            |
| thrift                   | 902 us                                                          | 499 us: 1.81x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 55.0 ns: 1.78x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 46.0 ms: 1.77x faster                                                            |
| raytrace                 | 303 ms                                                          | 174 ms: 1.74x faster                                                             |
| richards_super           | 49.9 ms                                                         | 30.5 ms: 1.63x faster                                                            |
| float                    | 69.6 ms                                                         | 42.6 ms: 1.63x faster                                                            |
| generators               | 31.6 ms                                                         | 19.3 ms: 1.63x faster                                                            |
| json                     | 4.76 ms                                                         | 2.93 ms: 1.63x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 18.3 us: 1.62x faster                                                            |
| json_loads               | 22.4 us                                                         | 13.9 us: 1.61x faster                                                            |
| comprehensions           | 17.7 us                                                         | 11.1 us: 1.60x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 57.6 ms: 1.56x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.8 ms: 1.56x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.02 ms: 1.53x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 38.5 ms: 1.52x faster                                                            |
| scimark_sor              | 115 ms                                                          | 76.0 ms: 1.51x faster                                                            |
| richards                 | 40.3 ms                                                         | 26.7 ms: 1.51x faster                                                            |
| pycparser                | 1.04 sec                                                        | 694 ms: 1.50x faster                                                             |
| regex_compile            | 117 ms                                                          | 79.0 ms: 1.48x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.5 ms: 1.47x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.83 us: 1.47x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.57 us: 1.46x faster                                                            |
| pyflate                  | 422 ms                                                          | 289 ms: 1.46x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 60.6 ms: 1.44x faster                                                            |
| sympy_sum                | 122 ms                                                          | 85.6 ms: 1.43x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 133 us: 1.43x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 37.3 ms: 1.39x faster                                                            |
| sympy_expand             | 391 ms                                                          | 282 ms: 1.39x faster                                                             |
| mako                     | 9.10 ms                                                         | 6.58 ms: 1.38x faster                                                            |
| sympy_str                | 229 ms                                                          | 167 ms: 1.37x faster                                                             |
| pprint_pformat           | 1.37 sec                                                        | 998 ms: 1.37x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 87.6 ms: 1.37x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.3 ms: 1.37x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 12.2 ms: 1.37x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.42 sec: 1.35x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 34.5 ms: 1.35x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 489 ms: 1.35x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 839 us: 1.33x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 212 us: 1.32x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.47 ms: 1.31x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.26 us: 1.26x faster                                                            |
| logging_simple           | 7.29 us                                                         | 5.83 us: 1.25x faster                                                            |
| nbody                    | 79.1 ms                                                         | 63.5 ms: 1.25x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 32.1 ns: 1.25x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 64.6 ms: 1.24x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 38.8 ms: 1.24x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.59 sec: 1.23x faster                                                           |
| coroutines               | 17.9 ms                                                         | 14.6 ms: 1.23x faster                                                            |
| 2to3                     | 265 ms                                                          | 218 ms: 1.22x faster                                                             |
| scimark_fft              | 216 ms                                                          | 179 ms: 1.21x faster                                                             |
| fannkuch                 | 317 ms                                                          | 262 ms: 1.21x faster                                                             |
| unpickle                 | 9.82 us                                                         | 8.50 us: 1.16x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.9 ms: 1.14x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 70.9 ms: 1.13x faster                                                            |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.3 ms: 1.10x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.40 ms: 1.10x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.52 ms: 1.09x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 56.6 ms: 1.09x faster                                                            |
| async_generators         | 241 ms                                                          | 227 ms: 1.06x faster                                                             |
| unpickle_list            | 2.98 us                                                         | 2.88 us: 1.04x faster                                                            |
| pickle                   | 7.83 us                                                         | 7.93 us: 1.01x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.27 us: 1.02x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.7 ms: 1.07x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.3 ms: 1.10x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 91.7 ms: 1.38x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.06 ms: 1.61x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.26 ms: 1.81x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.46x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.462x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: unknown