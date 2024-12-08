# Results vs. 3.10.4

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: windows-x86
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.156x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 247 ms: 1.08x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.79 sec: 1.09x faster                                                          |
| html5lib       | 52.1 ms                                                         | 44.7 ms: 1.16x faster                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 432 ms: 2.18x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 449 ms: 2.06x faster                                                            |
| async_tree_none         | 394 ms                                                          | 201 ms: 1.96x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 250 ms: 1.87x faster                                                            |
| Geometric mean          | (ref)                                                           | 2.01x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| float          | 69.6 ms                                                         | 60.8 ms: 1.15x faster                                                           |
| nbody          | 79.1 ms                                                         | 86.7 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                           | 1.38x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 115 ms: 1.14x faster                                                            |
| regex_compile  | 117 ms                                                          | 105 ms: 1.11x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.56 ms: 1.07x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.3 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.15x faster                                                            |
| json_dumps           | 9.82 ms                                                         | 8.57 ms: 1.15x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 170 us: 1.11x faster                                                            |
| json_loads           | 22.4 us                                                         | 20.3 us: 1.10x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.9 ms: 1.09x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.80 sec: 1.06x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 274 us: 1.02x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 67.3 ms: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.8 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.50 ms: 1.21x faster                                                           |
| django_template | 36.0 ms                                                         | 32.5 ms: 1.11x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 45.7 ms: 1.02x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 139 us: 2.84x faster                                                            |
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| async_tree_io            | 940 ms                                                          | 432 ms: 2.18x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 449 ms: 2.06x faster                                                            |
| async_tree_none          | 394 ms                                                          | 201 ms: 1.96x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 250 ms: 1.87x faster                                                            |
| pylint                   | 384 ms                                                          | 210 ms: 1.83x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.65 ms: 1.52x faster                                                           |
| go                       | 146 ms                                                          | 98.3 ms: 1.48x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 21.4 us: 1.38x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 59.2 ms: 1.37x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 65.7 ms: 1.37x faster                                                           |
| chaos                    | 74.4 ms                                                         | 55.2 ms: 1.35x faster                                                           |
| deepcopy                 | 310 us                                                          | 230 us: 1.35x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 73.1 ns: 1.34x faster                                                           |
| generators               | 31.6 ms                                                         | 23.9 ms: 1.32x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.9 us: 1.28x faster                                                           |
| pycparser                | 1.04 sec                                                        | 816 ms: 1.28x faster                                                            |
| raytrace                 | 303 ms                                                          | 239 ms: 1.26x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.06 ms: 1.26x faster                                                           |
| thrift                   | 902 us                                                          | 736 us: 1.23x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 5.01 ms: 1.23x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.30 ms: 1.22x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.50 ms: 1.21x faster                                                           |
| pyflate                  | 422 ms                                                          | 349 ms: 1.21x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.95 us: 1.18x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 44.7 ms: 1.16x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 50.5 ms: 1.16x faster                                                           |
| richards_super           | 49.9 ms                                                         | 43.4 ms: 1.15x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.15x faster                                                            |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.15x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 8.57 ms: 1.15x faster                                                           |
| float                    | 69.6 ms                                                         | 60.8 ms: 1.15x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 983 us: 1.14x faster                                                            |
| json                     | 4.76 ms                                                         | 4.18 ms: 1.14x faster                                                           |
| regex_dna                | 131 ms                                                          | 115 ms: 1.14x faster                                                            |
| scimark_sor              | 115 ms                                                          | 102 ms: 1.13x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 170 us: 1.11x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 55.7 ms: 1.11x faster                                                           |
| regex_compile            | 117 ms                                                          | 105 ms: 1.11x faster                                                            |
| django_template          | 36.0 ms                                                         | 32.5 ms: 1.11x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.3 us: 1.10x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 72.9 ms: 1.10x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 79.4 ms: 1.10x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.45 us: 1.10x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.9 ms: 1.09x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.79 sec: 1.09x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.69 sec: 1.08x faster                                                          |
| 2to3                     | 265 ms                                                          | 247 ms: 1.08x faster                                                            |
| sympy_str                | 229 ms                                                          | 215 ms: 1.07x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.56 ms: 1.07x faster                                                           |
| richards                 | 40.3 ms                                                         | 37.9 ms: 1.06x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.80 sec: 1.06x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 218 ms: 1.06x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 42.3 ms: 1.06x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.0 ms: 1.05x faster                                                           |
| fannkuch                 | 317 ms                                                          | 305 ms: 1.04x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 634 ms: 1.04x faster                                                            |
| sympy_expand             | 391 ms                                                          | 377 ms: 1.03x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 15.3 ms: 1.03x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.33 sec: 1.03x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 274 us: 1.02x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 45.7 ms: 1.02x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 80.6 ms: 1.01x slower                                                           |
| scimark_fft              | 216 ms                                                          | 229 ms: 1.06x slower                                                            |
| logging_format           | 7.91 us                                                         | 8.44 us: 1.07x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.78 us: 1.07x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 67.3 ms: 1.09x slower                                                           |
| nbody                    | 79.1 ms                                                         | 86.7 ms: 1.10x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                           |
| coverage                 | 46.6 ms                                                         | 52.9 ms: 1.14x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.8 ms: 1.17x slower                                                           |
| async_generators         | 241 ms                                                          | 296 ms: 1.23x slower                                                            |
| telco                    | 4.83 ms                                                         | 6.51 ms: 1.35x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 92.1 ms: 1.39x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.78 ms: 1.39x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 972 us: 1.40x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                                    |

Benchmark hidden because not significant (4): scimark_sparse_mat_mult, genshi_text, xml_etree_process, pathlib
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.156x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown