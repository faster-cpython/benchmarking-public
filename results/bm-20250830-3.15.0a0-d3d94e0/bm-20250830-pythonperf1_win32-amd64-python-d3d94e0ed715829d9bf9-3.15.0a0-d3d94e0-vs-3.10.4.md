# Results vs. 3.10.4

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.439x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 218 ms: 1.22x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.62 sec: 1.21x faster                                                           |
| html5lib       | 52.1 ms                                                         | 38.0 ms: 1.37x faster                                                            |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 326 ms: 2.83x faster                                                             |
| async_tree_io           | 940 ms                                                          | 384 ms: 2.45x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| async_tree_none         | 394 ms                                                          | 174 ms: 2.26x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.45x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 145 ms: 3.47x faster                                                             |
| float          | 69.6 ms                                                         | 44.4 ms: 1.57x faster                                                            |
| nbody          | 79.1 ms                                                         | 65.5 ms: 1.21x faster                                                            |
| Geometric mean | (ref)                                                           | 1.87x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 80.8 ms: 1.44x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.3 ms: 1.18x faster                                                            |
| regex_dna      | 131 ms                                                          | 116 ms: 1.12x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.52 ms: 1.10x faster                                                            |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.45 ms: 1.80x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.3 us: 1.57x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 87.8 ms: 1.37x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.41 sec: 1.36x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 140 us: 1.35x faster                                                             |
| pickle_pure_python   | 280 us                                                          | 218 us: 1.28x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 39.8 ms: 1.21x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.53 us: 1.15x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.7 ms: 1.10x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 56.9 ms: 1.08x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.83 us: 1.05x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.32 us: 1.03x slower                                                            |
| pickle               | 7.83 us                                                         | 8.12 us: 1.04x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.7 us: 1.08x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.21x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.8 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 24.5 ms: 1.47x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 33.9 ms: 1.37x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.4 ms: 1.37x faster                                                            |
| mako            | 9.10 ms                                                         | 6.79 ms: 1.34x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.39x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.32 sec: 12.90x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 105 us: 3.79x faster                                                             |
| pidigits                 | 502 ms                                                          | 145 ms: 3.47x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 326 ms: 2.83x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 29.8 ms: 2.72x faster                                                            |
| async_tree_io            | 940 ms                                                          | 384 ms: 2.45x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| async_tree_none          | 394 ms                                                          | 174 ms: 2.26x faster                                                             |
| mdp                      | 1.83 sec                                                        | 815 ms: 2.24x faster                                                             |
| pylint                   | 384 ms                                                          | 197 ms: 1.95x faster                                                             |
| go                       | 146 ms                                                          | 77.5 ms: 1.88x faster                                                            |
| chaos                    | 74.4 ms                                                         | 41.0 ms: 1.82x faster                                                            |
| thrift                   | 902 us                                                          | 498 us: 1.81x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.23 ms: 1.81x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 5.45 ms: 1.80x faster                                                            |
| deepcopy                 | 310 us                                                          | 173 us: 1.79x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 47.4 ms: 1.71x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 57.3 ns: 1.71x faster                                                            |
| raytrace                 | 303 ms                                                          | 178 ms: 1.70x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 446 ms: 1.67x faster                                                             |
| generators               | 31.6 ms                                                         | 19.1 ms: 1.65x faster                                                            |
| comprehensions           | 17.7 us                                                         | 11.0 us: 1.61x faster                                                            |
| json                     | 4.76 ms                                                         | 2.99 ms: 1.59x faster                                                            |
| richards_super           | 49.9 ms                                                         | 31.4 ms: 1.59x faster                                                            |
| float                    | 69.6 ms                                                         | 44.4 ms: 1.57x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.3 us: 1.57x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 58.4 ms: 1.54x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 19.5 us: 1.52x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.0 ms: 1.51x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.14 ms: 1.48x faster                                                            |
| scimark_sor              | 115 ms                                                          | 78.0 ms: 1.48x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.5 ms: 1.47x faster                                                            |
| pycparser                | 1.04 sec                                                        | 711 ms: 1.47x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 40.1 ms: 1.46x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.84 us: 1.46x faster                                                            |
| regex_compile            | 117 ms                                                          | 80.8 ms: 1.44x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.60 us: 1.43x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 61.1 ms: 1.43x faster                                                            |
| pyflate                  | 422 ms                                                          | 298 ms: 1.42x faster                                                             |
| richards                 | 40.3 ms                                                         | 28.4 ms: 1.42x faster                                                            |
| sympy_sum                | 122 ms                                                          | 87.8 ms: 1.39x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 33.9 ms: 1.37x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 38.0 ms: 1.37x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 87.8 ms: 1.37x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.4 ms: 1.37x faster                                                            |
| sympy_expand             | 391 ms                                                          | 287 ms: 1.36x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.41 sec: 1.36x faster                                                           |
| sympy_str                | 229 ms                                                          | 169 ms: 1.36x faster                                                             |
| unpickle_pure_python     | 189 us                                                          | 140 us: 1.35x faster                                                             |
| mako                     | 9.10 ms                                                         | 6.79 ms: 1.34x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.03 sec: 1.33x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 12.6 ms: 1.32x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 856 us: 1.31x faster                                                             |
| pprint_safe_repr         | 658 ms                                                          | 506 ms: 1.30x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 218 us: 1.28x faster                                                             |
| coroutines               | 17.9 ms                                                         | 14.2 ms: 1.26x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.58 ms: 1.25x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 64.8 ms: 1.24x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.47 us: 1.22x faster                                                            |
| 2to3                     | 265 ms                                                          | 218 ms: 1.22x faster                                                             |
| unpack_sequence          | 40.0 ns                                                         | 33.0 ns: 1.21x faster                                                            |
| nbody                    | 79.1 ms                                                         | 65.5 ms: 1.21x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 39.8 ms: 1.21x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.62 sec: 1.21x faster                                                           |
| logging_simple           | 7.29 us                                                         | 6.10 us: 1.19x faster                                                            |
| scimark_fft              | 216 ms                                                          | 181 ms: 1.19x faster                                                             |
| fannkuch                 | 317 ms                                                          | 267 ms: 1.19x faster                                                             |
| regex_v8                 | 15.8 ms                                                         | 13.3 ms: 1.18x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.16 ms: 1.16x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.53 us: 1.15x faster                                                            |
| regex_dna                | 131 ms                                                          | 116 ms: 1.12x faster                                                             |
| meteor_contest           | 80.0 ms                                                         | 72.6 ms: 1.10x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.52 ms: 1.10x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.7 ms: 1.10x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 56.9 ms: 1.08x faster                                                            |
| async_generators         | 241 ms                                                          | 226 ms: 1.06x faster                                                             |
| unpickle_list            | 2.98 us                                                         | 2.83 us: 1.05x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.32 us: 1.03x slower                                                            |
| pickle                   | 7.83 us                                                         | 8.12 us: 1.04x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.7 ms: 1.07x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.7 us: 1.08x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.8 ms: 1.12x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 93.3 ms: 1.41x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.09 ms: 1.63x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.29 ms: 1.86x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.43x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.439x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: unknown