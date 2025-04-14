# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: windows-x86
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.110x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 268 ms: 1.01x slower                                                            |
| docutils       | 1.95 sec                                                        | 1.91 sec: 1.02x faster                                                          |
| html5lib       | 52.1 ms                                                         | 49.1 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 464 ms: 2.03x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 486 ms: 1.90x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 255 ms: 1.83x faster                                                            |
| async_tree_none         | 394 ms                                                          | 219 ms: 1.80x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.89x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| float          | 69.6 ms                                                         | 54.1 ms: 1.29x faster                                                           |
| nbody          | 79.1 ms                                                         | 86.0 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.44x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                            |
| regex_compile  | 117 ms                                                          | 108 ms: 1.08x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.1 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.33 ms: 1.18x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 110 ms: 1.09x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.0 ms: 1.04x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.6 us: 1.03x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 272 us: 1.03x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 187 us: 1.01x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 3.18 us: 1.07x slower                                                           |
| xml_etree_process    | 48.1 ms                                                         | 53.2 ms: 1.11x slower                                                           |
| unpickle             | 9.82 us                                                         | 11.2 us: 1.14x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 21.0 us: 1.15x slower                                                           |
| pickle               | 7.83 us                                                         | 9.19 us: 1.17x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 72.6 ms: 1.18x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.85 us: 1.20x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 29.0 ms: 1.27x slower                                                           |
| python_startup_no_site | 18.1 ms                                                         | 22.9 ms: 1.27x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.27x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.37 ms: 1.09x faster                                                           |
| django_template | 36.0 ms                                                         | 35.6 ms: 1.01x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 23.5 ms: 1.12x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 53.9 ms: 1.16x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.04x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 153 us: 2.59x faster                                                            |
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| pathlib                  | 81.2 ms                                                         | 37.3 ms: 2.18x faster                                                           |
| async_tree_io            | 940 ms                                                          | 464 ms: 2.03x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 486 ms: 1.90x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 255 ms: 1.83x faster                                                            |
| async_tree_none          | 394 ms                                                          | 219 ms: 1.80x faster                                                            |
| pylint                   | 384 ms                                                          | 230 ms: 1.67x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.73 ms: 1.48x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 67.2 ns: 1.46x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 21.6 us: 1.37x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 67.7 ms: 1.33x faster                                                           |
| go                       | 146 ms                                                          | 111 ms: 1.31x faster                                                            |
| float                    | 69.6 ms                                                         | 54.1 ms: 1.29x faster                                                           |
| generators               | 31.6 ms                                                         | 25.2 ms: 1.25x faster                                                           |
| chaos                    | 74.4 ms                                                         | 59.7 ms: 1.25x faster                                                           |
| comprehensions           | 17.7 us                                                         | 14.5 us: 1.23x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.08 ms: 1.21x faster                                                           |
| raytrace                 | 303 ms                                                          | 253 ms: 1.20x faster                                                            |
| deepcopy                 | 310 us                                                          | 259 us: 1.20x faster                                                            |
| scimark_sor              | 115 ms                                                          | 96.7 ms: 1.19x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.18x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 68.8 ms: 1.18x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.33 ms: 1.18x faster                                                           |
| pyflate                  | 422 ms                                                          | 358 ms: 1.18x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 642 ms: 1.16x faster                                                            |
| richards_super           | 49.9 ms                                                         | 43.3 ms: 1.15x faster                                                           |
| thrift                   | 902 us                                                          | 786 us: 1.15x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 54.3 ms: 1.14x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 52.2 ms: 1.12x faster                                                           |
| pycparser                | 1.04 sec                                                        | 947 ms: 1.10x faster                                                            |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                            |
| mako                     | 9.10 ms                                                         | 8.37 ms: 1.09x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 110 ms: 1.09x faster                                                            |
| sympy_sum                | 122 ms                                                          | 113 ms: 1.09x faster                                                            |
| coroutines               | 17.9 ms                                                         | 16.5 ms: 1.08x faster                                                           |
| regex_compile            | 117 ms                                                          | 108 ms: 1.08x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 74.3 ms: 1.08x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 49.1 ms: 1.06x faster                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                           |
| richards                 | 40.3 ms                                                         | 38.5 ms: 1.05x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.9 ms: 1.05x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.1 ms: 1.04x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.0 ms: 1.04x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.6 us: 1.03x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 272 us: 1.03x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.91 sec: 1.02x faster                                                          |
| unpack_sequence          | 40.0 ns                                                         | 39.4 ns: 1.02x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 187 us: 1.01x faster                                                            |
| django_template          | 36.0 ms                                                         | 35.6 ms: 1.01x faster                                                           |
| sympy_str                | 229 ms                                                          | 228 ms: 1.01x faster                                                            |
| 2to3                     | 265 ms                                                          | 268 ms: 1.01x slower                                                            |
| pprint_safe_repr         | 658 ms                                                          | 670 ms: 1.02x slower                                                            |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.3 sec: 1.02x slower                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.75 us: 1.03x slower                                                           |
| mdp                      | 1.83 sec                                                        | 1.88 sec: 1.03x slower                                                          |
| sympy_expand             | 391 ms                                                          | 406 ms: 1.04x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 84.9 ms: 1.06x slower                                                           |
| unpickle_list            | 2.98 us                                                         | 3.18 us: 1.07x slower                                                           |
| scimark_fft              | 216 ms                                                          | 235 ms: 1.09x slower                                                            |
| nbody                    | 79.1 ms                                                         | 86.0 ms: 1.09x slower                                                           |
| fannkuch                 | 317 ms                                                          | 347 ms: 1.09x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 53.2 ms: 1.11x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 23.5 ms: 1.12x slower                                                           |
| unpickle                 | 9.82 us                                                         | 11.2 us: 1.14x slower                                                           |
| coverage                 | 46.6 ms                                                         | 53.2 ms: 1.14x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 21.0 us: 1.15x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 53.9 ms: 1.16x slower                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.30 ms: 1.16x slower                                                           |
| pickle                   | 7.83 us                                                         | 9.19 us: 1.17x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 72.6 ms: 1.18x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.85 us: 1.20x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.88 us: 1.22x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.75 us: 1.23x slower                                                           |
| python_startup           | 22.9 ms                                                         | 29.0 ms: 1.27x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 22.9 ms: 1.27x slower                                                           |
| async_generators         | 241 ms                                                          | 317 ms: 1.31x slower                                                            |
| telco                    | 4.83 ms                                                         | 6.82 ms: 1.41x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.82 ms: 1.42x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 95.7 ms: 1.44x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.07 ms: 1.54x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.08x faster                                                                    |

Benchmark hidden because not significant (4): json, pprint_pformat, scimark_sparse_mat_mult, nqueens
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.110x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown