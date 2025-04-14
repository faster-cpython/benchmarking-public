# Results vs. 3.10.4

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-x86
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.057x faster
- HPT reliability: 90.51%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 283 ms: 1.07x slower                                                            |
| docutils       | 1.95 sec                                                        | 1.99 sec: 1.02x slower                                                          |
| html5lib       | 52.1 ms                                                         | 48.2 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 494 ms: 1.90x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 515 ms: 1.79x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 271 ms: 1.72x faster                                                            |
| async_tree_none         | 394 ms                                                          | 232 ms: 1.70x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| float          | 69.6 ms                                                         | 57.5 ms: 1.21x faster                                                           |
| nbody          | 79.1 ms                                                         | 112 ms: 1.42x slower                                                            |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 114 ms: 1.14x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 14.5 ms: 1.09x faster                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.58 ms: 1.05x faster                                                           |
| regex_compile  | 117 ms                                                          | 114 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.35 ms: 1.18x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 110 ms: 1.09x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.1 ms: 1.04x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.7 us: 1.03x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.87 sec: 1.02x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 2.94 us: 1.02x faster                                                           |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.04x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.75 us: 1.16x slower                                                           |
| pickle_pure_python   | 280 us                                                          | 326 us: 1.16x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 56.3 ms: 1.17x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 21.4 us: 1.17x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 72.6 ms: 1.18x slower                                                           |
| pickle               | 7.83 us                                                         | 9.49 us: 1.21x slower                                                           |
| unpickle_pure_python | 189 us                                                          | 239 us: 1.26x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.07x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 29.0 ms: 1.26x slower                                                           |
| python_startup_no_site | 18.1 ms                                                         | 22.9 ms: 1.27x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.27x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.18 ms: 1.11x faster                                                           |
| django_template | 36.0 ms                                                         | 35.7 ms: 1.01x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 23.6 ms: 1.12x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 54.3 ms: 1.17x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.04x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 180 us: 2.20x faster                                                            |
| pathlib                  | 81.2 ms                                                         | 37.5 ms: 2.16x faster                                                           |
| async_tree_io            | 940 ms                                                          | 494 ms: 1.90x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 515 ms: 1.79x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 271 ms: 1.72x faster                                                            |
| async_tree_none          | 394 ms                                                          | 232 ms: 1.70x faster                                                            |
| pylint                   | 384 ms                                                          | 235 ms: 1.63x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.13 sec: 1.61x faster                                                          |
| deltablue                | 4.04 ms                                                         | 3.10 ms: 1.30x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 75.3 ns: 1.30x faster                                                           |
| go                       | 146 ms                                                          | 114 ms: 1.28x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 23.3 us: 1.27x faster                                                           |
| chaos                    | 74.4 ms                                                         | 59.5 ms: 1.25x faster                                                           |
| deepcopy                 | 310 us                                                          | 254 us: 1.22x faster                                                            |
| float                    | 69.6 ms                                                         | 57.5 ms: 1.21x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.91 us: 1.20x faster                                                           |
| raytrace                 | 303 ms                                                          | 255 ms: 1.19x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 8.35 ms: 1.18x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 634 ms: 1.17x faster                                                            |
| generators               | 31.6 ms                                                         | 27.0 ms: 1.17x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 76.8 ms: 1.17x faster                                                           |
| regex_dna                | 131 ms                                                          | 114 ms: 1.14x faster                                                            |
| scimark_sor              | 115 ms                                                          | 101 ms: 1.14x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 54.7 ms: 1.13x faster                                                           |
| pyflate                  | 422 ms                                                          | 377 ms: 1.12x faster                                                            |
| mako                     | 9.10 ms                                                         | 8.18 ms: 1.11x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 53.0 ms: 1.10x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 110 ms: 1.09x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.5 ms: 1.09x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 48.2 ms: 1.08x faster                                                           |
| sympy_sum                | 122 ms                                                          | 114 ms: 1.07x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.58 ms: 1.05x faster                                                           |
| richards_super           | 49.9 ms                                                         | 47.5 ms: 1.05x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.1 ms: 1.04x faster                                                           |
| pycparser                | 1.04 sec                                                        | 1.01 sec: 1.04x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.14 ms: 1.03x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.7 us: 1.03x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.62 us: 1.02x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.87 sec: 1.02x faster                                                          |
| regex_compile            | 117 ms                                                          | 114 ms: 1.02x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 78.6 ms: 1.02x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.94 us: 1.02x faster                                                           |
| django_template          | 36.0 ms                                                         | 35.7 ms: 1.01x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.8 ms: 1.01x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 16.7 ms: 1.01x slower                                                           |
| docutils                 | 1.95 sec                                                        | 1.99 sec: 1.02x slower                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 83.3 ms: 1.03x slower                                                           |
| sympy_str                | 229 ms                                                          | 236 ms: 1.03x slower                                                            |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.04x slower                                                           |
| comprehensions           | 17.7 us                                                         | 18.6 us: 1.05x slower                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.8 sec: 1.05x slower                                                          |
| richards                 | 40.3 ms                                                         | 42.3 ms: 1.05x slower                                                           |
| 2to3                     | 265 ms                                                          | 283 ms: 1.07x slower                                                            |
| nqueens                  | 87.1 ms                                                         | 93.6 ms: 1.07x slower                                                           |
| sympy_expand             | 391 ms                                                          | 421 ms: 1.08x slower                                                            |
| hexiom                   | 6.13 ms                                                         | 6.75 ms: 1.10x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 23.6 ms: 1.12x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 92.2 ms: 1.15x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.75 us: 1.16x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 326 us: 1.16x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 54.3 ms: 1.17x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 56.3 ms: 1.17x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.61 sec: 1.17x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 21.4 us: 1.17x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 72.6 ms: 1.18x slower                                                           |
| coverage                 | 46.6 ms                                                         | 55.0 ms: 1.18x slower                                                           |
| fannkuch                 | 317 ms                                                          | 376 ms: 1.18x slower                                                            |
| logging_format           | 7.91 us                                                         | 9.45 us: 1.19x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 786 ms: 1.19x slower                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.34 ms: 1.20x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.76 us: 1.20x slower                                                           |
| pickle                   | 7.83 us                                                         | 9.49 us: 1.21x slower                                                           |
| scimark_fft              | 216 ms                                                          | 265 ms: 1.23x slower                                                            |
| unpickle_pure_python     | 189 us                                                          | 239 us: 1.26x slower                                                            |
| python_startup           | 22.9 ms                                                         | 29.0 ms: 1.26x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 22.9 ms: 1.27x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 51.7 ns: 1.29x slower                                                           |
| async_generators         | 241 ms                                                          | 338 ms: 1.40x slower                                                            |
| nbody                    | 79.1 ms                                                         | 112 ms: 1.42x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 95.6 ms: 1.44x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.87 ms: 1.46x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.07 ms: 1.54x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.75 ms: 1.61x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): json
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.057x faster

# HPT report

- Reliability score: 90.51% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown