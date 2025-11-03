# Results vs. 3.10.4

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.467x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 216 ms: 1.23x faster                                                              |
| docutils       | 1.95 sec                                                        | 1.59 sec: 1.23x faster                                                            |
| html5lib       | 52.1 ms                                                         | 36.6 ms: 1.42x faster                                                             |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 322 ms: 2.86x faster                                                              |
| async_tree_io           | 940 ms                                                          | 366 ms: 2.57x faster                                                              |
| async_tree_memoization  | 467 ms                                                          | 195 ms: 2.40x faster                                                              |
| async_tree_none         | 394 ms                                                          | 167 ms: 2.36x faster                                                              |
| Geometric mean          | (ref)                                                           | 2.54x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 145 ms: 3.46x faster                                                              |
| float          | 69.6 ms                                                         | 43.3 ms: 1.61x faster                                                             |
| nbody          | 79.1 ms                                                         | 65.6 ms: 1.21x faster                                                             |
| Geometric mean | (ref)                                                           | 1.89x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 79.9 ms: 1.46x faster                                                             |
| regex_v8       | 15.8 ms                                                         | 13.7 ms: 1.15x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.46 ms: 1.14x faster                                                             |
| regex_dna      | 131 ms                                                          | 116 ms: 1.13x faster                                                              |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.43 ms: 1.81x faster                                                             |
| json_loads           | 22.4 us                                                         | 14.0 us: 1.60x faster                                                             |
| unpickle_pure_python | 189 us                                                          | 134 us: 1.41x faster                                                              |
| tomli_loads          | 1.91 sec                                                        | 1.37 sec: 1.40x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 86.6 ms: 1.39x faster                                                             |
| pickle_pure_python   | 280 us                                                          | 210 us: 1.33x faster                                                              |
| xml_etree_process    | 48.1 ms                                                         | 38.6 ms: 1.25x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 58.6 ms: 1.21x faster                                                             |
| unpickle             | 9.82 us                                                         | 8.28 us: 1.19x faster                                                             |
| xml_etree_generate   | 61.6 ms                                                         | 55.3 ms: 1.12x faster                                                             |
| unpickle_list        | 2.98 us                                                         | 2.78 us: 1.07x faster                                                             |
| pickle_dict          | 18.2 us                                                         | 19.4 us: 1.06x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.24x faster                                                                      |

Benchmark hidden because not significant (2): pickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                             |
| python_startup         | 22.9 ms                                                         | 25.3 ms: 1.10x slower                                                             |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 23.4 ms: 1.54x faster                                                             |
| genshi_xml      | 46.6 ms                                                         | 34.3 ms: 1.36x faster                                                             |
| mako            | 9.10 ms                                                         | 6.72 ms: 1.35x faster                                                             |
| genshi_text     | 21.0 ms                                                         | 15.5 ms: 1.35x faster                                                             |
| Geometric mean  | (ref)                                                           | 1.40x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.36 sec: 12.49x faster                                                           |
| typing_runtime_protocols | 396 us                                                          | 103 us: 3.85x faster                                                              |
| pidigits                 | 502 ms                                                          | 145 ms: 3.46x faster                                                              |
| pathlib                  | 81.2 ms                                                         | 28.3 ms: 2.87x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 322 ms: 2.86x faster                                                              |
| async_tree_io            | 940 ms                                                          | 366 ms: 2.57x faster                                                              |
| async_tree_memoization   | 467 ms                                                          | 195 ms: 2.40x faster                                                              |
| async_tree_none          | 394 ms                                                          | 167 ms: 2.36x faster                                                              |
| mdp                      | 1.83 sec                                                        | 812 ms: 2.25x faster                                                              |
| pylint                   | 384 ms                                                          | 196 ms: 1.96x faster                                                              |
| go                       | 146 ms                                                          | 76.6 ms: 1.90x faster                                                             |
| deepcopy                 | 310 us                                                          | 165 us: 1.88x faster                                                              |
| thrift                   | 902 us                                                          | 494 us: 1.83x faster                                                              |
| chaos                    | 74.4 ms                                                         | 41.1 ms: 1.81x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.23 ms: 1.81x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 5.43 ms: 1.81x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 55.2 ns: 1.77x faster                                                             |
| raytrace                 | 303 ms                                                          | 178 ms: 1.70x faster                                                              |
| crypto_pyaes             | 81.3 ms                                                         | 47.9 ms: 1.70x faster                                                             |
| json                     | 4.76 ms                                                         | 2.83 ms: 1.68x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 17.8 us: 1.66x faster                                                             |
| generators               | 31.6 ms                                                         | 19.2 ms: 1.65x faster                                                             |
| float                    | 69.6 ms                                                         | 43.3 ms: 1.61x faster                                                             |
| json_loads               | 22.4 us                                                         | 14.0 us: 1.60x faster                                                             |
| scimark_lu               | 89.8 ms                                                         | 56.2 ms: 1.60x faster                                                             |
| richards_super           | 49.9 ms                                                         | 31.4 ms: 1.59x faster                                                             |
| comprehensions           | 17.7 us                                                         | 11.2 us: 1.58x faster                                                             |
| django_template          | 36.0 ms                                                         | 23.4 ms: 1.54x faster                                                             |
| pycparser                | 1.04 sec                                                        | 684 ms: 1.52x faster                                                              |
| deepcopy_reduce          | 2.68 us                                                         | 1.77 us: 1.51x faster                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.0 ms: 1.51x faster                                                             |
| scimark_sor              | 115 ms                                                          | 76.6 ms: 1.50x faster                                                             |
| pyflate                  | 422 ms                                                          | 283 ms: 1.49x faster                                                              |
| hexiom                   | 6.13 ms                                                         | 4.12 ms: 1.49x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 39.3 ms: 1.49x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 504 ms: 1.48x faster                                                              |
| sqlite_synth             | 2.29 us                                                         | 1.57 us: 1.46x faster                                                             |
| regex_compile            | 117 ms                                                          | 79.9 ms: 1.46x faster                                                             |
| richards                 | 40.3 ms                                                         | 27.7 ms: 1.45x faster                                                             |
| sympy_sum                | 122 ms                                                          | 85.3 ms: 1.44x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 36.6 ms: 1.42x faster                                                             |
| unpickle_pure_python     | 189 us                                                          | 134 us: 1.41x faster                                                              |
| tomli_loads              | 1.91 sec                                                        | 1.37 sec: 1.40x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 86.6 ms: 1.39x faster                                                             |
| sympy_expand             | 391 ms                                                          | 283 ms: 1.38x faster                                                              |
| nqueens                  | 87.1 ms                                                         | 63.3 ms: 1.38x faster                                                             |
| sympy_str                | 229 ms                                                          | 167 ms: 1.37x faster                                                              |
| pprint_pformat           | 1.37 sec                                                        | 1.00 sec: 1.37x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 12.2 ms: 1.36x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 34.3 ms: 1.36x faster                                                             |
| mako                     | 9.10 ms                                                         | 6.72 ms: 1.35x faster                                                             |
| genshi_text              | 21.0 ms                                                         | 15.5 ms: 1.35x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 833 us: 1.34x faster                                                              |
| pickle_pure_python       | 280 us                                                          | 210 us: 1.33x faster                                                              |
| pprint_safe_repr         | 658 ms                                                          | 497 ms: 1.32x faster                                                              |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.47 ms: 1.31x faster                                                             |
| scimark_fft              | 216 ms                                                          | 169 ms: 1.28x faster                                                              |
| coroutines               | 17.9 ms                                                         | 14.1 ms: 1.27x faster                                                             |
| xml_etree_process        | 48.1 ms                                                         | 38.6 ms: 1.25x faster                                                             |
| logging_format           | 7.91 us                                                         | 6.39 us: 1.24x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 65.1 ms: 1.23x faster                                                             |
| 2to3                     | 265 ms                                                          | 216 ms: 1.23x faster                                                              |
| unpack_sequence          | 40.0 ns                                                         | 32.6 ns: 1.23x faster                                                             |
| docutils                 | 1.95 sec                                                        | 1.59 sec: 1.23x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.01 us: 1.21x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 58.6 ms: 1.21x faster                                                             |
| nbody                    | 79.1 ms                                                         | 65.6 ms: 1.21x faster                                                             |
| unpickle                 | 9.82 us                                                         | 8.28 us: 1.19x faster                                                             |
| fannkuch                 | 317 ms                                                          | 267 ms: 1.19x faster                                                              |
| telco                    | 4.83 ms                                                         | 4.17 ms: 1.16x faster                                                             |
| regex_v8                 | 15.8 ms                                                         | 13.7 ms: 1.15x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.46 ms: 1.14x faster                                                             |
| regex_dna                | 131 ms                                                          | 116 ms: 1.13x faster                                                              |
| xml_etree_generate       | 61.6 ms                                                         | 55.3 ms: 1.12x faster                                                             |
| meteor_contest           | 80.0 ms                                                         | 72.0 ms: 1.11x faster                                                             |
| unpickle_list            | 2.98 us                                                         | 2.78 us: 1.07x faster                                                             |
| async_generators         | 241 ms                                                          | 229 ms: 1.05x faster                                                              |
| coverage                 | 46.6 ms                                                         | 48.0 ms: 1.03x slower                                                             |
| pickle_dict              | 18.2 us                                                         | 19.4 us: 1.06x slower                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                             |
| python_startup           | 22.9 ms                                                         | 25.3 ms: 1.10x slower                                                             |
| bench_mp_pool            | 66.4 ms                                                         | 88.7 ms: 1.34x slower                                                             |
| gc_traversal             | 1.28 ms                                                         | 2.05 ms: 1.60x slower                                                             |
| create_gc_cycles         | 694 us                                                          | 1.28 ms: 1.85x slower                                                             |
| Geometric mean           | (ref)                                                           | 1.46x faster                                                                      |

Benchmark hidden because not significant (2): pickle_list, pickle
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.467x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: unknown