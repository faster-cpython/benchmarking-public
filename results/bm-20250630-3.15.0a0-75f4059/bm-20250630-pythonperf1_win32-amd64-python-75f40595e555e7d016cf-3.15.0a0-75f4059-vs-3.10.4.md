# Results vs. 3.10.4

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.449x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 220 ms: 1.20x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.60 sec: 1.22x faster                                                           |
| html5lib       | 52.1 ms                                                         | 38.0 ms: 1.37x faster                                                            |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 328 ms: 2.81x faster                                                             |
| async_tree_io           | 940 ms                                                          | 397 ms: 2.37x faster                                                             |
| async_tree_none         | 394 ms                                                          | 170 ms: 2.32x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 208 ms: 2.25x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.42x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 146 ms: 3.43x faster                                                             |
| float          | 69.6 ms                                                         | 43.1 ms: 1.62x faster                                                            |
| nbody          | 79.1 ms                                                         | 63.0 ms: 1.26x faster                                                            |
| Geometric mean | (ref)                                                           | 1.91x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 79.4 ms: 1.47x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.3 ms: 1.18x faster                                                            |
| regex_dna      | 131 ms                                                          | 115 ms: 1.13x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.50 ms: 1.11x faster                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.19 ms: 1.59x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.3 us: 1.57x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 135 us: 1.41x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.38 sec: 1.39x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 208 us: 1.35x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 89.2 ms: 1.35x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 39.1 ms: 1.23x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.57 us: 1.15x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 56.1 ms: 1.10x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.78 us: 1.08x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.3 ms: 1.07x faster                                                            |
| pickle               | 7.83 us                                                         | 7.96 us: 1.02x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.40 us: 1.06x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.7 us: 1.08x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.20x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.08x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 24.3 ms: 1.48x faster                                                            |
| mako            | 9.10 ms                                                         | 6.55 ms: 1.39x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.3 ms: 1.37x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.3 ms: 1.36x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.40x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.33 sec: 12.79x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 101 us: 3.91x faster                                                             |
| pidigits                 | 502 ms                                                          | 146 ms: 3.43x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 328 ms: 2.81x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 31.7 ms: 2.56x faster                                                            |
| async_tree_io            | 940 ms                                                          | 397 ms: 2.37x faster                                                             |
| async_tree_none          | 394 ms                                                          | 170 ms: 2.32x faster                                                             |
| mdp                      | 1.83 sec                                                        | 801 ms: 2.28x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 208 ms: 2.25x faster                                                             |
| pylint                   | 384 ms                                                          | 198 ms: 1.94x faster                                                             |
| go                       | 146 ms                                                          | 75.5 ms: 1.93x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.15 ms: 1.88x faster                                                            |
| deepcopy                 | 310 us                                                          | 168 us: 1.84x faster                                                             |
| chaos                    | 74.4 ms                                                         | 40.6 ms: 1.83x faster                                                            |
| thrift                   | 902 us                                                          | 494 us: 1.83x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 55.2 ns: 1.77x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 433 ms: 1.72x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 47.8 ms: 1.70x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 17.6 us: 1.68x faster                                                            |
| raytrace                 | 303 ms                                                          | 180 ms: 1.68x faster                                                             |
| comprehensions           | 17.7 us                                                         | 10.9 us: 1.63x faster                                                            |
| richards_super           | 49.9 ms                                                         | 30.6 ms: 1.63x faster                                                            |
| generators               | 31.6 ms                                                         | 19.4 ms: 1.62x faster                                                            |
| float                    | 69.6 ms                                                         | 43.1 ms: 1.62x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.19 ms: 1.59x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 56.6 ms: 1.59x faster                                                            |
| json                     | 4.76 ms                                                         | 3.03 ms: 1.57x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.3 us: 1.57x faster                                                            |
| scimark_sor              | 115 ms                                                          | 74.0 ms: 1.56x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.1 ms: 1.55x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.03 ms: 1.52x faster                                                            |
| pycparser                | 1.04 sec                                                        | 699 ms: 1.49x faster                                                             |
| richards                 | 40.3 ms                                                         | 27.0 ms: 1.49x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.3 ms: 1.48x faster                                                            |
| pyflate                  | 422 ms                                                          | 285 ms: 1.48x faster                                                             |
| regex_compile            | 117 ms                                                          | 79.4 ms: 1.47x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.84 us: 1.45x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 60.5 ms: 1.44x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.59 us: 1.44x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 40.9 ms: 1.43x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 135 us: 1.41x faster                                                             |
| sympy_sum                | 122 ms                                                          | 87.3 ms: 1.40x faster                                                            |
| mako                     | 9.10 ms                                                         | 6.55 ms: 1.39x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.38 sec: 1.39x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 38.0 ms: 1.37x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.3 ms: 1.37x faster                                                            |
| sympy_expand             | 391 ms                                                          | 287 ms: 1.36x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 34.3 ms: 1.36x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.01 sec: 1.35x faster                                                           |
| sympy_str                | 229 ms                                                          | 170 ms: 1.35x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 208 us: 1.35x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 89.2 ms: 1.35x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 490 ms: 1.34x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.4 ms: 1.34x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 843 us: 1.33x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.49 ms: 1.30x faster                                                            |
| nbody                    | 79.1 ms                                                         | 63.0 ms: 1.26x faster                                                            |
| fannkuch                 | 317 ms                                                          | 255 ms: 1.24x faster                                                             |
| coroutines               | 17.9 ms                                                         | 14.4 ms: 1.24x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 64.7 ms: 1.24x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 39.1 ms: 1.23x faster                                                            |
| scimark_fft              | 216 ms                                                          | 176 ms: 1.23x faster                                                             |
| logging_format           | 7.91 us                                                         | 6.49 us: 1.22x faster                                                            |
| logging_simple           | 7.29 us                                                         | 5.99 us: 1.22x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.60 sec: 1.22x faster                                                           |
| 2to3                     | 265 ms                                                          | 220 ms: 1.20x faster                                                             |
| regex_v8                 | 15.8 ms                                                         | 13.3 ms: 1.18x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.57 us: 1.15x faster                                                            |
| regex_dna                | 131 ms                                                          | 115 ms: 1.13x faster                                                             |
| meteor_contest           | 80.0 ms                                                         | 71.8 ms: 1.11x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.50 ms: 1.11x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 36.2 ns: 1.10x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 56.1 ms: 1.10x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.78 us: 1.08x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.3 ms: 1.07x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.60 ms: 1.05x faster                                                            |
| async_generators         | 241 ms                                                          | 230 ms: 1.05x faster                                                             |
| pickle                   | 7.83 us                                                         | 7.96 us: 1.02x slower                                                            |
| coverage                 | 46.6 ms                                                         | 47.6 ms: 1.02x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.40 us: 1.06x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.08x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.7 us: 1.08x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 95.7 ms: 1.44x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.14 ms: 1.67x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.33 ms: 1.92x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.44x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.449x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: unknown