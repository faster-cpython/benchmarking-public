# Results vs. 3.10.4

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.460x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.37x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 221 ms: 1.20x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.67 sec: 1.16x faster                                                           |
| html5lib       | 52.1 ms                                                         | 38.7 ms: 1.34x faster                                                            |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 333 ms: 2.77x faster                                                             |
| async_tree_io           | 940 ms                                                          | 397 ms: 2.37x faster                                                             |
| async_tree_none         | 394 ms                                                          | 170 ms: 2.31x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 207 ms: 2.25x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.42x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 146 ms: 3.43x faster                                                             |
| float          | 69.6 ms                                                         | 44.5 ms: 1.56x faster                                                            |
| nbody          | 79.1 ms                                                         | 56.8 ms: 1.39x faster                                                            |
| Geometric mean | (ref)                                                           | 1.96x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 78.1 ms: 1.49x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 14.2 ms: 1.11x faster                                                            |
| regex_dna      | 131 ms                                                          | 122 ms: 1.07x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                          | 109 us: 1.74x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.14 sec: 1.68x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 6.25 ms: 1.57x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.6 us: 1.54x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 204 us: 1.37x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 87.6 ms: 1.37x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 35.5 ms: 1.36x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 51.8 ms: 1.19x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.84 us: 1.11x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.0 ms: 1.11x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.85 us: 1.05x faster                                                            |
| pickle               | 7.83 us                                                         | 7.71 us: 1.02x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.36 us: 1.04x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.6 us: 1.08x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.6 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.47 ms: 1.66x faster                                                            |
| django_template | 36.0 ms                                                         | 23.9 ms: 1.51x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.3 ms: 1.37x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.7 ms: 1.34x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.44 sec: 11.78x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 103 us: 3.84x faster                                                             |
| pidigits                 | 502 ms                                                          | 146 ms: 3.43x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 333 ms: 2.77x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 31.9 ms: 2.55x faster                                                            |
| async_tree_io            | 940 ms                                                          | 397 ms: 2.37x faster                                                             |
| async_tree_none          | 394 ms                                                          | 170 ms: 2.31x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 207 ms: 2.25x faster                                                             |
| mdp                      | 1.83 sec                                                        | 824 ms: 2.22x faster                                                             |
| pylint                   | 384 ms                                                          | 201 ms: 1.91x faster                                                             |
| go                       | 146 ms                                                          | 77.0 ms: 1.89x faster                                                            |
| thrift                   | 902 us                                                          | 488 us: 1.85x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.23 ms: 1.81x faster                                                            |
| deepcopy                 | 310 us                                                          | 172 us: 1.80x faster                                                             |
| chaos                    | 74.4 ms                                                         | 41.7 ms: 1.79x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 54.9 ns: 1.78x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 46.2 ms: 1.76x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 109 us: 1.74x faster                                                             |
| raytrace                 | 303 ms                                                          | 177 ms: 1.71x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.14 sec: 1.68x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.47 ms: 1.66x faster                                                            |
| comprehensions           | 17.7 us                                                         | 10.7 us: 1.65x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 18.1 us: 1.64x faster                                                            |
| pyflate                  | 422 ms                                                          | 259 ms: 1.63x faster                                                             |
| richards_super           | 49.9 ms                                                         | 30.6 ms: 1.63x faster                                                            |
| generators               | 31.6 ms                                                         | 19.9 ms: 1.59x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.25 ms: 1.57x faster                                                            |
| float                    | 69.6 ms                                                         | 44.5 ms: 1.56x faster                                                            |
| json                     | 4.76 ms                                                         | 3.05 ms: 1.56x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.6 us: 1.54x faster                                                            |
| django_template          | 36.0 ms                                                         | 23.9 ms: 1.51x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.1 ms: 1.51x faster                                                            |
| regex_compile            | 117 ms                                                          | 78.1 ms: 1.49x faster                                                            |
| richards                 | 40.3 ms                                                         | 27.1 ms: 1.49x faster                                                            |
| pycparser                | 1.04 sec                                                        | 703 ms: 1.48x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 4.16 ms: 1.48x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.56 us: 1.47x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 40.4 ms: 1.45x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.87 us: 1.44x faster                                                            |
| scimark_sor              | 115 ms                                                          | 80.2 ms: 1.44x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 62.8 ms: 1.43x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 959 ms: 1.43x faster                                                             |
| pprint_safe_repr         | 658 ms                                                          | 465 ms: 1.42x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.29 ms: 1.41x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 61.7 ms: 1.41x faster                                                            |
| scimark_fft              | 216 ms                                                          | 153 ms: 1.41x faster                                                             |
| fannkuch                 | 317 ms                                                          | 225 ms: 1.41x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 531 ms: 1.40x faster                                                             |
| nbody                    | 79.1 ms                                                         | 56.8 ms: 1.39x faster                                                            |
| sympy_sum                | 122 ms                                                          | 88.3 ms: 1.39x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 204 us: 1.37x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 87.6 ms: 1.37x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.3 ms: 1.37x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 35.5 ms: 1.36x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 34.7 ms: 1.34x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 38.7 ms: 1.34x faster                                                            |
| sympy_str                | 229 ms                                                          | 172 ms: 1.33x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 850 us: 1.32x faster                                                             |
| sympy_expand             | 391 ms                                                          | 298 ms: 1.31x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.8 ms: 1.30x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.8 ms: 1.21x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.59 us: 1.20x faster                                                            |
| 2to3                     | 265 ms                                                          | 221 ms: 1.20x faster                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 51.8 ms: 1.19x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.13 us: 1.19x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 68.7 ms: 1.17x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.67 sec: 1.16x faster                                                           |
| telco                    | 4.83 ms                                                         | 4.25 ms: 1.14x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 70.7 ms: 1.13x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.84 us: 1.11x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.2 ms: 1.11x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.0 ms: 1.11x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 37.3 ns: 1.07x faster                                                            |
| regex_dna                | 131 ms                                                          | 122 ms: 1.07x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.85 us: 1.05x faster                                                            |
| pickle                   | 7.83 us                                                         | 7.71 us: 1.02x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.36 us: 1.04x slower                                                            |
| async_generators         | 241 ms                                                          | 253 ms: 1.05x slower                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.6 us: 1.08x slower                                                            |
| coverage                 | 46.6 ms                                                         | 50.4 ms: 1.08x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.6 ms: 1.12x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 95.3 ms: 1.44x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.14 ms: 1.67x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.33 ms: 1.92x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.45x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.460x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.40x
- 95% likely to have a speedup of 1.39x
- 99% likely to have a speedup of 1.37x

# Memory
- memory change: unknown