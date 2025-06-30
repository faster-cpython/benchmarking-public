# Results vs. 3.10.4

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.271x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 229 ms: 1.16x faster                                                             |
| docutils       | 1.95 sec                                                        | 2.94 sec: 1.51x slower                                                           |
| html5lib       | 52.1 ms                                                         | 41.6 ms: 1.25x faster                                                            |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 337 ms: 2.74x faster                                                             |
| async_tree_io           | 940 ms                                                          | 354 ms: 2.65x faster                                                             |
| async_tree_none         | 394 ms                                                          | 175 ms: 2.26x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 215 ms: 2.17x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.44x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 137 ms: 3.67x faster                                                             |
| float          | 69.6 ms                                                         | 46.2 ms: 1.51x faster                                                            |
| nbody          | 79.1 ms                                                         | 85.9 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                           | 1.72x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 95.9 ms: 1.22x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.5 ms: 1.17x faster                                                            |
| regex_dna      | 131 ms                                                          | 114 ms: 1.14x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.62 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.67 ms: 1.47x faster                                                            |
| json_loads           | 22.4 us                                                         | 16.1 us: 1.39x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 90.4 ms: 1.33x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 156 us: 1.21x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 58.8 ms: 1.20x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 237 us: 1.18x faster                                                             |
| pickle_list          | 3.22 us                                                         | 3.03 us: 1.06x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 45.9 ms: 1.05x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 3.06 us: 1.03x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 63.3 ms: 1.03x slower                                                            |
| pickle               | 7.83 us                                                         | 8.22 us: 1.05x slower                                                            |
| unpickle             | 9.82 us                                                         | 10.5 us: 1.07x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.2 us: 1.11x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.72 sec: 1.42x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.6 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 28.2 ms: 1.28x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 41.8 ms: 1.12x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 20.0 ms: 1.05x faster                                                            |
| mako            | 9.10 ms                                                         | 9.89 ms: 1.09x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.45 sec: 6.92x faster                                                           |
| pidigits                 | 502 ms                                                          | 137 ms: 3.67x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 130 us: 3.05x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 337 ms: 2.74x faster                                                             |
| async_tree_io            | 940 ms                                                          | 354 ms: 2.65x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 32.3 ms: 2.51x faster                                                            |
| async_tree_none          | 394 ms                                                          | 175 ms: 2.26x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 215 ms: 2.17x faster                                                             |
| pylint                   | 384 ms                                                          | 215 ms: 1.78x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.34 us: 1.70x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.46 ms: 1.64x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 62.1 ns: 1.57x faster                                                            |
| go                       | 146 ms                                                          | 92.7 ms: 1.57x faster                                                            |
| thrift                   | 902 us                                                          | 575 us: 1.57x faster                                                             |
| chaos                    | 74.4 ms                                                         | 47.5 ms: 1.57x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.18 sec: 1.55x faster                                                           |
| json                     | 4.76 ms                                                         | 3.09 ms: 1.54x faster                                                            |
| deepcopy                 | 310 us                                                          | 204 us: 1.52x faster                                                             |
| float                    | 69.6 ms                                                         | 46.2 ms: 1.51x faster                                                            |
| comprehensions           | 17.7 us                                                         | 12.1 us: 1.47x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.67 ms: 1.47x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 57.5 ms: 1.41x faster                                                            |
| pycparser                | 1.04 sec                                                        | 739 ms: 1.41x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 21.1 us: 1.41x faster                                                            |
| raytrace                 | 303 ms                                                          | 216 ms: 1.40x faster                                                             |
| json_loads               | 22.4 us                                                         | 16.1 us: 1.39x faster                                                            |
| generators               | 31.6 ms                                                         | 23.0 ms: 1.37x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 43.1 ms: 1.36x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 556 ms: 1.34x faster                                                             |
| scimark_lu               | 89.8 ms                                                         | 67.4 ms: 1.33x faster                                                            |
| pyflate                  | 422 ms                                                          | 318 ms: 1.33x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 90.4 ms: 1.33x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.64 ms: 1.32x faster                                                            |
| scimark_sor              | 115 ms                                                          | 87.4 ms: 1.32x faster                                                            |
| django_template          | 36.0 ms                                                         | 28.2 ms: 1.28x faster                                                            |
| richards_super           | 49.9 ms                                                         | 39.6 ms: 1.26x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 41.6 ms: 1.25x faster                                                            |
| sympy_sum                | 122 ms                                                          | 98.7 ms: 1.24x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.5 ms: 1.23x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.19 us: 1.22x faster                                                            |
| regex_compile            | 117 ms                                                          | 95.9 ms: 1.22x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.8 ms: 1.21x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 156 us: 1.21x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 58.8 ms: 1.20x faster                                                            |
| sympy_str                | 229 ms                                                          | 191 ms: 1.20x faster                                                             |
| sympy_expand             | 391 ms                                                          | 328 ms: 1.19x faster                                                             |
| richards                 | 40.3 ms                                                         | 34.1 ms: 1.18x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 237 us: 1.18x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 73.9 ms: 1.18x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.5 ms: 1.17x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 14.3 ms: 1.16x faster                                                            |
| 2to3                     | 265 ms                                                          | 229 ms: 1.16x faster                                                             |
| pprint_safe_repr         | 658 ms                                                          | 573 ms: 1.15x faster                                                             |
| regex_dna                | 131 ms                                                          | 114 ms: 1.14x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 41.8 ms: 1.12x faster                                                            |
| logging_format           | 7.91 us                                                         | 7.31 us: 1.08x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 37.1 ns: 1.08x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 74.4 ms: 1.08x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.77 us: 1.08x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.03 us: 1.06x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 45.9 ms: 1.05x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 20.0 ms: 1.05x faster                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.23 ms: 1.04x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.14 ms: 1.03x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.62 ms: 1.03x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.09 ms: 1.03x faster                                                            |
| fannkuch                 | 317 ms                                                          | 310 ms: 1.02x faster                                                             |
| scimark_fft              | 216 ms                                                          | 212 ms: 1.02x faster                                                             |
| unpickle_list            | 2.98 us                                                         | 3.06 us: 1.03x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 63.3 ms: 1.03x slower                                                            |
| pickle                   | 7.83 us                                                         | 8.22 us: 1.05x slower                                                            |
| unpickle                 | 9.82 us                                                         | 10.5 us: 1.07x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 86.0 ms: 1.08x slower                                                            |
| async_generators         | 241 ms                                                          | 261 ms: 1.08x slower                                                             |
| nbody                    | 79.1 ms                                                         | 85.9 ms: 1.09x slower                                                            |
| mako                     | 9.10 ms                                                         | 9.89 ms: 1.09x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.2 us: 1.11x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.6 ms: 1.12x slower                                                            |
| telco                    | 4.83 ms                                                         | 5.47 ms: 1.13x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 79.8 ms: 1.20x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.74 sec: 1.27x slower                                                           |
| tomli_loads              | 1.91 sec                                                        | 2.72 sec: 1.42x slower                                                           |
| coverage                 | 46.6 ms                                                         | 66.9 ms: 1.44x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.94 sec: 1.51x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.53x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.27x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250630-3.15.0a0-75f4059-NOGIL/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.271x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown