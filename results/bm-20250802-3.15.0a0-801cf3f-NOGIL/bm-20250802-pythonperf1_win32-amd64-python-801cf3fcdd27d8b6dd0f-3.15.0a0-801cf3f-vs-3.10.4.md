# Results vs. 3.10.4

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.265x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 234 ms: 1.13x faster                                                             |
| docutils       | 1.95 sec                                                        | 3.03 sec: 1.55x slower                                                           |
| html5lib       | 52.1 ms                                                         | 41.9 ms: 1.24x faster                                                            |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 334 ms: 2.76x faster                                                             |
| async_tree_io           | 940 ms                                                          | 377 ms: 2.50x faster                                                             |
| async_tree_none         | 394 ms                                                          | 173 ms: 2.28x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 225 ms: 2.08x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.39x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 138 ms: 3.64x faster                                                             |
| float          | 69.6 ms                                                         | 47.7 ms: 1.46x faster                                                            |
| nbody          | 79.1 ms                                                         | 82.8 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                           | 1.72x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 13.4 ms: 1.18x faster                                                            |
| regex_compile  | 117 ms                                                          | 99.5 ms: 1.17x faster                                                            |
| regex_dna      | 131 ms                                                          | 117 ms: 1.11x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.63 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.75 ms: 1.45x faster                                                            |
| json_loads           | 22.4 us                                                         | 15.8 us: 1.41x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 92.1 ms: 1.30x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 58.6 ms: 1.21x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 160 us: 1.18x faster                                                             |
| pickle_pure_python   | 280 us                                                          | 240 us: 1.17x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 44.8 ms: 1.08x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.29 us: 1.02x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 64.0 ms: 1.04x slower                                                            |
| pickle               | 7.83 us                                                         | 8.23 us: 1.05x slower                                                            |
| unpickle_list        | 2.98 us                                                         | 3.19 us: 1.07x slower                                                            |
| unpickle             | 9.82 us                                                         | 10.6 us: 1.08x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 21.2 us: 1.16x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.75 sec: 1.44x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                            |
| python_startup         | 22.9 ms                                                         | 27.0 ms: 1.18x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 27.6 ms: 1.30x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 41.5 ms: 1.12x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 20.3 ms: 1.04x faster                                                            |
| mako            | 9.10 ms                                                         | 10.3 ms: 1.13x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.35 sec: 7.23x faster                                                           |
| pidigits                 | 502 ms                                                          | 138 ms: 3.64x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 129 us: 3.07x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 334 ms: 2.76x faster                                                             |
| async_tree_io            | 940 ms                                                          | 377 ms: 2.50x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 32.8 ms: 2.47x faster                                                            |
| async_tree_none          | 394 ms                                                          | 173 ms: 2.28x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 225 ms: 2.08x faster                                                             |
| pylint                   | 384 ms                                                          | 217 ms: 1.77x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.39 us: 1.65x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.47 ms: 1.63x faster                                                            |
| chaos                    | 74.4 ms                                                         | 46.1 ms: 1.61x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 463 ms: 1.61x faster                                                             |
| thrift                   | 902 us                                                          | 574 us: 1.57x faster                                                             |
| go                       | 146 ms                                                          | 93.8 ms: 1.55x faster                                                            |
| json                     | 4.76 ms                                                         | 3.07 ms: 1.55x faster                                                            |
| deepcopy                 | 310 us                                                          | 205 us: 1.52x faster                                                             |
| mdp                      | 1.83 sec                                                        | 1.24 sec: 1.48x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 66.7 ns: 1.47x faster                                                            |
| comprehensions           | 17.7 us                                                         | 12.1 us: 1.46x faster                                                            |
| float                    | 69.6 ms                                                         | 47.7 ms: 1.46x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.75 ms: 1.45x faster                                                            |
| json_loads               | 22.4 us                                                         | 15.8 us: 1.41x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 57.6 ms: 1.41x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 21.1 us: 1.40x faster                                                            |
| raytrace                 | 303 ms                                                          | 220 ms: 1.38x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 42.8 ms: 1.37x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 65.6 ms: 1.37x faster                                                            |
| pyflate                  | 422 ms                                                          | 316 ms: 1.33x faster                                                             |
| generators               | 31.6 ms                                                         | 23.7 ms: 1.33x faster                                                            |
| scimark_sor              | 115 ms                                                          | 87.8 ms: 1.31x faster                                                            |
| django_template          | 36.0 ms                                                         | 27.6 ms: 1.30x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 92.1 ms: 1.30x faster                                                            |
| pycparser                | 1.04 sec                                                        | 811 ms: 1.28x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 4.78 ms: 1.28x faster                                                            |
| richards_super           | 49.9 ms                                                         | 39.3 ms: 1.27x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 49.6 ms: 1.25x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.15 us: 1.25x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 41.9 ms: 1.24x faster                                                            |
| sympy_sum                | 122 ms                                                          | 98.8 ms: 1.24x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 58.6 ms: 1.21x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.9 ms: 1.21x faster                                                            |
| sympy_str                | 229 ms                                                          | 192 ms: 1.20x faster                                                             |
| richards                 | 40.3 ms                                                         | 33.8 ms: 1.19x faster                                                            |
| sympy_expand             | 391 ms                                                          | 328 ms: 1.19x faster                                                             |
| unpickle_pure_python     | 189 us                                                          | 160 us: 1.18x faster                                                             |
| regex_v8                 | 15.8 ms                                                         | 13.4 ms: 1.18x faster                                                            |
| regex_compile            | 117 ms                                                          | 99.5 ms: 1.17x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 74.5 ms: 1.17x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 240 us: 1.17x faster                                                             |
| pprint_safe_repr         | 658 ms                                                          | 566 ms: 1.16x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 14.3 ms: 1.16x faster                                                            |
| 2to3                     | 265 ms                                                          | 234 ms: 1.13x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 41.5 ms: 1.12x faster                                                            |
| regex_dna                | 131 ms                                                          | 117 ms: 1.11x faster                                                             |
| logging_format           | 7.91 us                                                         | 7.30 us: 1.08x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 44.8 ms: 1.08x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 75.9 ms: 1.06x faster                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.21 ms: 1.06x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.09 ms: 1.05x faster                                                            |
| fannkuch                 | 317 ms                                                          | 306 ms: 1.04x faster                                                             |
| genshi_text              | 21.0 ms                                                         | 20.3 ms: 1.04x faster                                                            |
| logging_simple           | 7.29 us                                                         | 7.08 us: 1.03x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.63 ms: 1.02x faster                                                            |
| scimark_fft              | 216 ms                                                          | 213 ms: 1.02x faster                                                             |
| pickle_list              | 3.22 us                                                         | 3.29 us: 1.02x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 64.0 ms: 1.04x slower                                                            |
| nbody                    | 79.1 ms                                                         | 82.8 ms: 1.05x slower                                                            |
| pickle                   | 7.83 us                                                         | 8.23 us: 1.05x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.19 us: 1.07x slower                                                            |
| unpickle                 | 9.82 us                                                         | 10.6 us: 1.08x slower                                                            |
| telco                    | 4.83 ms                                                         | 5.25 ms: 1.09x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 87.3 ms: 1.09x slower                                                            |
| async_generators         | 241 ms                                                          | 268 ms: 1.11x slower                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                            |
| mako                     | 9.10 ms                                                         | 10.3 ms: 1.13x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 21.2 us: 1.16x slower                                                            |
| python_startup           | 22.9 ms                                                         | 27.0 ms: 1.18x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 80.3 ms: 1.21x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.76 sec: 1.28x slower                                                           |
| tomli_loads              | 1.91 sec                                                        | 2.75 sec: 1.44x slower                                                           |
| coverage                 | 46.6 ms                                                         | 67.7 ms: 1.45x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.01 ms: 1.46x slower                                                            |
| docutils                 | 1.95 sec                                                        | 3.03 sec: 1.55x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.26x faster                                                                     |

Benchmark hidden because not significant (2): bench_thread_pool, unpack_sequence
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.265x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown