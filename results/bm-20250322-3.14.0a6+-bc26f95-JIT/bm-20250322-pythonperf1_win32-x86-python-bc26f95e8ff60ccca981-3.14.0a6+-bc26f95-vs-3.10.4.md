# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: windows-x86
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.021x faster
- HPT reliability: 58.85%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 287 ms: 1.08x slower                                                            |
| docutils       | 1.95 sec                                                        | 2.03 sec: 1.04x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 513 ms: 1.83x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 506 ms: 1.82x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 281 ms: 1.66x faster                                                            |
| async_tree_none         | 394 ms                                                          | 241 ms: 1.63x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.74x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.49x faster                                                            |
| float          | 69.6 ms                                                         | 59.0 ms: 1.18x faster                                                           |
| nbody          | 79.1 ms                                                         | 130 ms: 1.64x slower                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 115 ms: 1.14x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 15.0 ms: 1.05x faster                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.59 ms: 1.05x faster                                                           |
| regex_compile  | 117 ms                                                          | 120 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.55 ms: 1.15x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 112 ms: 1.07x faster                                                            |
| json_loads           | 22.4 us                                                         | 22.0 us: 1.02x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 71.2 ms: 1.00x slower                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.96 sec: 1.03x slower                                                          |
| unpickle_list        | 2.98 us                                                         | 3.19 us: 1.07x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.5 us: 1.07x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 21.4 us: 1.17x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.85 us: 1.20x slower                                                           |
| pickle               | 7.83 us                                                         | 9.50 us: 1.21x slower                                                           |
| xml_etree_process    | 48.1 ms                                                         | 58.9 ms: 1.22x slower                                                           |
| pickle_pure_python   | 280 us                                                          | 350 us: 1.25x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 78.0 ms: 1.27x slower                                                           |
| unpickle_pure_python | 189 us                                                          | 254 us: 1.34x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.11x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 28.7 ms: 1.25x slower                                                           |
| python_startup_no_site | 18.1 ms                                                         | 22.8 ms: 1.26x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.26x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.05 ms: 1.13x faster                                                           |
| django_template | 36.0 ms                                                         | 37.2 ms: 1.03x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 55.4 ms: 1.19x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 25.1 ms: 1.20x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.07x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 201 ms: 2.49x faster                                                            |
| pathlib                  | 81.2 ms                                                         | 38.1 ms: 2.13x faster                                                           |
| typing_runtime_protocols | 396 us                                                          | 186 us: 2.13x faster                                                            |
| async_tree_io            | 940 ms                                                          | 513 ms: 1.83x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 506 ms: 1.82x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 281 ms: 1.66x faster                                                            |
| async_tree_none          | 394 ms                                                          | 241 ms: 1.63x faster                                                            |
| pylint                   | 384 ms                                                          | 239 ms: 1.61x faster                                                            |
| deltablue                | 4.04 ms                                                         | 3.23 ms: 1.25x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 23.8 us: 1.24x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.90 us: 1.21x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 82.6 ns: 1.18x faster                                                           |
| go                       | 146 ms                                                          | 123 ms: 1.18x faster                                                            |
| float                    | 69.6 ms                                                         | 59.0 ms: 1.18x faster                                                           |
| chaos                    | 74.4 ms                                                         | 63.2 ms: 1.18x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.55 ms: 1.15x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 78.1 ms: 1.15x faster                                                           |
| raytrace                 | 303 ms                                                          | 266 ms: 1.14x faster                                                            |
| regex_dna                | 131 ms                                                          | 115 ms: 1.14x faster                                                            |
| thrift                   | 902 us                                                          | 794 us: 1.14x faster                                                            |
| mako                     | 9.10 ms                                                         | 8.05 ms: 1.13x faster                                                           |
| deepcopy                 | 310 us                                                          | 275 us: 1.13x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 53.9 ms: 1.09x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 691 ms: 1.08x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 112 ms: 1.07x faster                                                            |
| scimark_sor              | 115 ms                                                          | 108 ms: 1.06x faster                                                            |
| richards_super           | 49.9 ms                                                         | 47.1 ms: 1.06x faster                                                           |
| pyflate                  | 422 ms                                                          | 399 ms: 1.06x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 58.8 ms: 1.05x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.0 ms: 1.05x faster                                                           |
| generators               | 31.6 ms                                                         | 30.0 ms: 1.05x faster                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.59 ms: 1.05x faster                                                           |
| sympy_sum                | 122 ms                                                          | 117 ms: 1.04x faster                                                            |
| json_loads               | 22.4 us                                                         | 22.0 us: 1.02x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.19 ms: 1.02x faster                                                           |
| pycparser                | 1.04 sec                                                        | 1.03 sec: 1.01x faster                                                          |
| coroutines               | 17.9 ms                                                         | 17.8 ms: 1.01x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 71.2 ms: 1.00x slower                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.2 sec: 1.01x slower                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.96 sec: 1.03x slower                                                          |
| regex_compile            | 117 ms                                                          | 120 ms: 1.03x slower                                                            |
| sympy_integrate          | 16.6 ms                                                         | 17.1 ms: 1.03x slower                                                           |
| django_template          | 36.0 ms                                                         | 37.2 ms: 1.03x slower                                                           |
| spectral_norm            | 80.2 ms                                                         | 82.8 ms: 1.03x slower                                                           |
| richards                 | 40.3 ms                                                         | 41.6 ms: 1.03x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.03 sec: 1.04x slower                                                          |
| sympy_str                | 229 ms                                                          | 239 ms: 1.04x slower                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.80 us: 1.04x slower                                                           |
| unpickle_list            | 2.98 us                                                         | 3.19 us: 1.07x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.5 us: 1.07x slower                                                           |
| sympy_expand             | 391 ms                                                          | 421 ms: 1.08x slower                                                            |
| 2to3                     | 265 ms                                                          | 287 ms: 1.08x slower                                                            |
| comprehensions           | 17.7 us                                                         | 19.3 us: 1.09x slower                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 88.6 ms: 1.09x slower                                                           |
| hexiom                   | 6.13 ms                                                         | 6.92 ms: 1.13x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 102 ms: 1.17x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 21.4 us: 1.17x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.61 sec: 1.18x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 55.4 ms: 1.19x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.85 us: 1.20x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 25.1 ms: 1.20x slower                                                           |
| coverage                 | 46.6 ms                                                         | 55.9 ms: 1.20x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 96.1 ms: 1.20x slower                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.35 ms: 1.20x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 793 ms: 1.21x slower                                                            |
| pickle                   | 7.83 us                                                         | 9.50 us: 1.21x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 58.9 ms: 1.22x slower                                                           |
| fannkuch                 | 317 ms                                                          | 391 ms: 1.23x slower                                                            |
| scimark_fft              | 216 ms                                                          | 268 ms: 1.24x slower                                                            |
| pickle_pure_python       | 280 us                                                          | 350 us: 1.25x slower                                                            |
| python_startup           | 22.9 ms                                                         | 28.7 ms: 1.25x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.92 us: 1.25x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 22.8 ms: 1.26x slower                                                           |
| logging_simple           | 7.29 us                                                         | 9.20 us: 1.26x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 78.0 ms: 1.27x slower                                                           |
| unpickle_pure_python     | 189 us                                                          | 254 us: 1.34x slower                                                            |
| unpack_sequence          | 40.0 ns                                                         | 56.0 ns: 1.40x slower                                                           |
| async_generators         | 241 ms                                                          | 340 ms: 1.41x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.85 ms: 1.45x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 96.2 ms: 1.45x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.53x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.56 ms: 1.56x slower                                                           |
| nbody                    | 79.1 ms                                                         | 130 ms: 1.64x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): json, html5lib, mdp
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.021x faster

# HPT report

- Reliability score: 58.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown