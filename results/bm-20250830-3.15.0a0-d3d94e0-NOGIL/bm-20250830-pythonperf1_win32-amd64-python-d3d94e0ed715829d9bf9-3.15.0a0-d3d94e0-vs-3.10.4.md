# Results vs. 3.10.4

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.283x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 228 ms: 1.16x faster                                                             |
| docutils       | 1.95 sec                                                        | 2.88 sec: 1.48x slower                                                           |
| html5lib       | 52.1 ms                                                         | 41.8 ms: 1.25x faster                                                            |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 334 ms: 2.76x faster                                                             |
| async_tree_io           | 940 ms                                                          | 355 ms: 2.65x faster                                                             |
| async_tree_none         | 394 ms                                                          | 173 ms: 2.27x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 211 ms: 2.22x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.46x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 136 ms: 3.69x faster                                                             |
| float          | 69.6 ms                                                         | 45.7 ms: 1.52x faster                                                            |
| nbody          | 79.1 ms                                                         | 80.8 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.77x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 95.4 ms: 1.22x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.7 ms: 1.15x faster                                                            |
| regex_dna      | 131 ms                                                          | 116 ms: 1.12x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.63 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.95 ms: 1.65x faster                                                            |
| json_loads           | 22.4 us                                                         | 16.0 us: 1.40x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 239 us: 1.17x faster                                                             |
| unpickle_pure_python | 189 us                                                          | 163 us: 1.16x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.1 ms: 1.14x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 105 ms: 1.14x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 45.5 ms: 1.06x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.09 us: 1.04x faster                                                            |
| pickle               | 7.83 us                                                         | 8.00 us: 1.02x slower                                                            |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.03x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 63.8 ms: 1.04x slower                                                            |
| unpickle_list        | 2.98 us                                                         | 3.12 us: 1.04x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.4 us: 1.12x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.36 sec: 1.23x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 27.5 ms: 1.31x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 40.7 ms: 1.15x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 19.9 ms: 1.06x faster                                                            |
| mako            | 9.10 ms                                                         | 10.1 ms: 1.11x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.09x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.16 sec: 7.86x faster                                                           |
| pidigits                 | 502 ms                                                          | 136 ms: 3.69x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 131 us: 3.03x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 334 ms: 2.76x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 29.8 ms: 2.73x faster                                                            |
| async_tree_io            | 940 ms                                                          | 355 ms: 2.65x faster                                                             |
| async_tree_none          | 394 ms                                                          | 173 ms: 2.27x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 211 ms: 2.22x faster                                                             |
| pylint                   | 384 ms                                                          | 202 ms: 1.90x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 412 ms: 1.81x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.39 ms: 1.69x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.37 us: 1.68x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 5.95 ms: 1.65x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.13 sec: 1.62x faster                                                           |
| chaos                    | 74.4 ms                                                         | 46.0 ms: 1.62x faster                                                            |
| thrift                   | 902 us                                                          | 567 us: 1.59x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 61.9 ns: 1.58x faster                                                            |
| go                       | 146 ms                                                          | 93.5 ms: 1.56x faster                                                            |
| json                     | 4.76 ms                                                         | 3.12 ms: 1.53x faster                                                            |
| float                    | 69.6 ms                                                         | 45.7 ms: 1.52x faster                                                            |
| deepcopy                 | 310 us                                                          | 205 us: 1.51x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 56.1 ms: 1.45x faster                                                            |
| comprehensions           | 17.7 us                                                         | 12.2 us: 1.45x faster                                                            |
| raytrace                 | 303 ms                                                          | 211 ms: 1.43x faster                                                             |
| pycparser                | 1.04 sec                                                        | 728 ms: 1.43x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 41.6 ms: 1.41x faster                                                            |
| json_loads               | 22.4 us                                                         | 16.0 us: 1.40x faster                                                            |
| generators               | 31.6 ms                                                         | 22.8 ms: 1.39x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 21.3 us: 1.39x faster                                                            |
| pyflate                  | 422 ms                                                          | 311 ms: 1.36x faster                                                             |
| scimark_lu               | 89.8 ms                                                         | 66.7 ms: 1.35x faster                                                            |
| django_template          | 36.0 ms                                                         | 27.5 ms: 1.31x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.80 ms: 1.28x faster                                                            |
| scimark_sor              | 115 ms                                                          | 90.5 ms: 1.27x faster                                                            |
| richards_super           | 49.9 ms                                                         | 39.5 ms: 1.26x faster                                                            |
| sympy_sum                | 122 ms                                                          | 97.5 ms: 1.26x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 41.8 ms: 1.25x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.19 us: 1.23x faster                                                            |
| regex_compile            | 117 ms                                                          | 95.4 ms: 1.22x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 51.0 ms: 1.21x faster                                                            |
| sympy_str                | 229 ms                                                          | 190 ms: 1.21x faster                                                             |
| sympy_expand             | 391 ms                                                          | 324 ms: 1.21x faster                                                             |
| coroutines               | 17.9 ms                                                         | 14.9 ms: 1.20x faster                                                            |
| richards                 | 40.3 ms                                                         | 33.6 ms: 1.20x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 72.9 ms: 1.20x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 239 us: 1.17x faster                                                             |
| unpickle_pure_python     | 189 us                                                          | 163 us: 1.16x faster                                                             |
| 2to3                     | 265 ms                                                          | 228 ms: 1.16x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 14.4 ms: 1.16x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 571 ms: 1.15x faster                                                             |
| regex_v8                 | 15.8 ms                                                         | 13.7 ms: 1.15x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 40.7 ms: 1.15x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.1 ms: 1.14x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 105 ms: 1.14x faster                                                             |
| regex_dna                | 131 ms                                                          | 116 ms: 1.12x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 71.7 ms: 1.12x faster                                                            |
| logging_format           | 7.91 us                                                         | 7.10 us: 1.11x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.60 us: 1.10x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 45.5 ms: 1.06x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 19.9 ms: 1.06x faster                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.23 ms: 1.04x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.09 us: 1.04x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 38.6 ns: 1.04x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.08 ms: 1.04x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.13 ms: 1.03x faster                                                            |
| fannkuch                 | 317 ms                                                          | 309 ms: 1.03x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.63 ms: 1.02x faster                                                            |
| nbody                    | 79.1 ms                                                         | 80.8 ms: 1.02x slower                                                            |
| pickle                   | 7.83 us                                                         | 8.00 us: 1.02x slower                                                            |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.03x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 63.8 ms: 1.04x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.12 us: 1.04x slower                                                            |
| async_generators         | 241 ms                                                          | 254 ms: 1.05x slower                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 86.7 ms: 1.08x slower                                                            |
| telco                    | 4.83 ms                                                         | 5.27 ms: 1.09x slower                                                            |
| mako                     | 9.10 ms                                                         | 10.1 ms: 1.11x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.4 us: 1.12x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 79.2 ms: 1.19x slower                                                            |
| tomli_loads              | 1.91 sec                                                        | 2.36 sec: 1.23x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.70 sec: 1.24x slower                                                           |
| coverage                 | 46.6 ms                                                         | 68.2 ms: 1.47x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.02 ms: 1.47x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.88 sec: 1.48x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.28x faster                                                                     |

Benchmark hidden because not significant (1): scimark_fft
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250830-3.15.0a0-d3d94e0-NOGIL/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.283x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown