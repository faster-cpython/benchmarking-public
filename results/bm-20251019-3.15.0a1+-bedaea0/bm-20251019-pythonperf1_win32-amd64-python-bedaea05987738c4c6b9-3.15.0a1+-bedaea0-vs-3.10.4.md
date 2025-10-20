# Results vs. 3.10.4

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.434x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 219 ms: 1.21x faster                                                              |
| docutils       | 1.95 sec                                                        | 1.63 sec: 1.20x faster                                                            |
| html5lib       | 52.1 ms                                                         | 39.0 ms: 1.33x faster                                                             |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 326 ms: 2.83x faster                                                              |
| async_tree_io           | 940 ms                                                          | 382 ms: 2.46x faster                                                              |
| async_tree_memoization  | 467 ms                                                          | 203 ms: 2.30x faster                                                              |
| async_tree_none         | 394 ms                                                          | 177 ms: 2.22x faster                                                              |
| Geometric mean          | (ref)                                                           | 2.44x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 148 ms: 3.40x faster                                                              |
| float          | 69.6 ms                                                         | 44.8 ms: 1.56x faster                                                             |
| nbody          | 79.1 ms                                                         | 67.9 ms: 1.17x faster                                                             |
| Geometric mean | (ref)                                                           | 1.83x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 81.0 ms: 1.44x faster                                                             |
| regex_v8       | 15.8 ms                                                         | 13.5 ms: 1.17x faster                                                             |
| regex_dna      | 131 ms                                                          | 115 ms: 1.14x faster                                                              |
| regex_effbot   | 1.66 ms                                                         | 1.50 ms: 1.11x faster                                                             |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.53 ms: 1.78x faster                                                             |
| json_loads           | 22.4 us                                                         | 14.5 us: 1.54x faster                                                             |
| unpickle_pure_python | 189 us                                                          | 138 us: 1.37x faster                                                              |
| xml_etree_parse      | 120 ms                                                          | 87.5 ms: 1.37x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.42 sec: 1.35x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 218 us: 1.29x faster                                                              |
| xml_etree_process    | 48.1 ms                                                         | 39.3 ms: 1.23x faster                                                             |
| unpickle             | 9.82 us                                                         | 8.59 us: 1.14x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.1 ms: 1.09x faster                                                             |
| xml_etree_generate   | 61.6 ms                                                         | 57.1 ms: 1.08x faster                                                             |
| unpickle_list        | 2.98 us                                                         | 2.79 us: 1.07x faster                                                             |
| pickle               | 7.83 us                                                         | 8.04 us: 1.03x slower                                                             |
| pickle_list          | 3.22 us                                                         | 3.31 us: 1.03x slower                                                             |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.21x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                             |
| python_startup         | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                             |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 25.2 ms: 1.43x faster                                                             |
| mako            | 9.10 ms                                                         | 6.61 ms: 1.38x faster                                                             |
| genshi_xml      | 46.6 ms                                                         | 35.0 ms: 1.33x faster                                                             |
| genshi_text     | 21.0 ms                                                         | 15.9 ms: 1.32x faster                                                             |
| Geometric mean  | (ref)                                                           | 1.36x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.27 sec: 13.32x faster                                                           |
| typing_runtime_protocols | 396 us                                                          | 103 us: 3.83x faster                                                              |
| pidigits                 | 502 ms                                                          | 148 ms: 3.40x faster                                                              |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 326 ms: 2.83x faster                                                              |
| pathlib                  | 81.2 ms                                                         | 29.4 ms: 2.76x faster                                                             |
| async_tree_io            | 940 ms                                                          | 382 ms: 2.46x faster                                                              |
| async_tree_memoization   | 467 ms                                                          | 203 ms: 2.30x faster                                                              |
| async_tree_none          | 394 ms                                                          | 177 ms: 2.22x faster                                                              |
| mdp                      | 1.83 sec                                                        | 823 ms: 2.22x faster                                                              |
| pylint                   | 384 ms                                                          | 200 ms: 1.92x faster                                                              |
| asyncio_tcp              | 744 ms                                                          | 398 ms: 1.87x faster                                                              |
| go                       | 146 ms                                                          | 78.8 ms: 1.85x faster                                                             |
| deepcopy                 | 310 us                                                          | 168 us: 1.85x faster                                                              |
| deltablue                | 4.04 ms                                                         | 2.22 ms: 1.81x faster                                                             |
| thrift                   | 902 us                                                          | 501 us: 1.80x faster                                                              |
| chaos                    | 74.4 ms                                                         | 41.7 ms: 1.78x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 5.53 ms: 1.78x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 17.3 us: 1.71x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 57.7 ns: 1.69x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 48.0 ms: 1.69x faster                                                             |
| raytrace                 | 303 ms                                                          | 183 ms: 1.66x faster                                                              |
| generators               | 31.6 ms                                                         | 19.6 ms: 1.61x faster                                                             |
| json                     | 4.76 ms                                                         | 2.98 ms: 1.60x faster                                                             |
| comprehensions           | 17.7 us                                                         | 11.2 us: 1.58x faster                                                             |
| richards_super           | 49.9 ms                                                         | 31.7 ms: 1.57x faster                                                             |
| float                    | 69.6 ms                                                         | 44.8 ms: 1.56x faster                                                             |
| json_loads               | 22.4 us                                                         | 14.5 us: 1.54x faster                                                             |
| scimark_lu               | 89.8 ms                                                         | 59.0 ms: 1.52x faster                                                             |
| pycparser                | 1.04 sec                                                        | 702 ms: 1.48x faster                                                              |
| deepcopy_reduce          | 2.68 us                                                         | 1.81 us: 1.48x faster                                                             |
| scimark_sor              | 115 ms                                                          | 78.0 ms: 1.48x faster                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 42.2 ms: 1.47x faster                                                             |
| pyflate                  | 422 ms                                                          | 289 ms: 1.46x faster                                                              |
| dulwich_log              | 58.5 ms                                                         | 40.3 ms: 1.45x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 4.23 ms: 1.45x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.59 us: 1.44x faster                                                             |
| regex_compile            | 117 ms                                                          | 81.0 ms: 1.44x faster                                                             |
| django_template          | 36.0 ms                                                         | 25.2 ms: 1.43x faster                                                             |
| richards                 | 40.3 ms                                                         | 28.1 ms: 1.43x faster                                                             |
| sympy_sum                | 122 ms                                                          | 87.5 ms: 1.40x faster                                                             |
| mako                     | 9.10 ms                                                         | 6.61 ms: 1.38x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 63.3 ms: 1.38x faster                                                             |
| unpickle_pure_python     | 189 us                                                          | 138 us: 1.37x faster                                                              |
| xml_etree_parse          | 120 ms                                                          | 87.5 ms: 1.37x faster                                                             |
| sympy_str                | 229 ms                                                          | 169 ms: 1.36x faster                                                              |
| sympy_expand             | 391 ms                                                          | 289 ms: 1.35x faster                                                              |
| pprint_pformat           | 1.37 sec                                                        | 1.01 sec: 1.35x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.42 sec: 1.35x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 493 ms: 1.34x faster                                                              |
| html5lib                 | 52.1 ms                                                         | 39.0 ms: 1.33x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 35.0 ms: 1.33x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.5 ms: 1.33x faster                                                             |
| genshi_text              | 21.0 ms                                                         | 15.9 ms: 1.32x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 863 us: 1.30x faster                                                              |
| pickle_pure_python       | 280 us                                                          | 218 us: 1.29x faster                                                              |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.60 ms: 1.25x faster                                                             |
| scimark_fft              | 216 ms                                                          | 175 ms: 1.23x faster                                                              |
| xml_etree_process        | 48.1 ms                                                         | 39.3 ms: 1.23x faster                                                             |
| unpack_sequence          | 40.0 ns                                                         | 32.8 ns: 1.22x faster                                                             |
| coroutines               | 17.9 ms                                                         | 14.8 ms: 1.22x faster                                                             |
| 2to3                     | 265 ms                                                          | 219 ms: 1.21x faster                                                              |
| logging_format           | 7.91 us                                                         | 6.57 us: 1.20x faster                                                             |
| logging_simple           | 7.29 us                                                         | 6.08 us: 1.20x faster                                                             |
| docutils                 | 1.95 sec                                                        | 1.63 sec: 1.20x faster                                                            |
| fannkuch                 | 317 ms                                                          | 269 ms: 1.18x faster                                                              |
| regex_v8                 | 15.8 ms                                                         | 13.5 ms: 1.17x faster                                                             |
| nbody                    | 79.1 ms                                                         | 67.9 ms: 1.17x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 69.6 ms: 1.15x faster                                                             |
| unpickle                 | 9.82 us                                                         | 8.59 us: 1.14x faster                                                             |
| regex_dna                | 131 ms                                                          | 115 ms: 1.14x faster                                                              |
| telco                    | 4.83 ms                                                         | 4.26 ms: 1.13x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.50 ms: 1.11x faster                                                             |
| meteor_contest           | 80.0 ms                                                         | 73.4 ms: 1.09x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.1 ms: 1.09x faster                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 57.1 ms: 1.08x faster                                                             |
| unpickle_list            | 2.98 us                                                         | 2.79 us: 1.07x faster                                                             |
| async_generators         | 241 ms                                                          | 237 ms: 1.02x faster                                                              |
| pickle                   | 7.83 us                                                         | 8.04 us: 1.03x slower                                                             |
| pickle_list              | 3.22 us                                                         | 3.31 us: 1.03x slower                                                             |
| coverage                 | 46.6 ms                                                         | 49.4 ms: 1.06x slower                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                             |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                                             |
| python_startup           | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                             |
| bench_mp_pool            | 66.4 ms                                                         | 90.2 ms: 1.36x slower                                                             |
| gc_traversal             | 1.28 ms                                                         | 2.11 ms: 1.65x slower                                                             |
| create_gc_cycles         | 694 us                                                          | 1.28 ms: 1.85x slower                                                             |
| Geometric mean           | (ref)                                                           | 1.43x faster                                                                      |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.434x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: unknown