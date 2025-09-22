# Results vs. 3.10.4

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.288x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 228 ms: 1.17x faster                                                             |
| docutils       | 1.95 sec                                                        | 2.90 sec: 1.49x slower                                                           |
| html5lib       | 52.1 ms                                                         | 40.7 ms: 1.28x faster                                                            |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 333 ms: 2.77x faster                                                             |
| async_tree_io           | 940 ms                                                          | 359 ms: 2.62x faster                                                             |
| async_tree_none         | 394 ms                                                          | 172 ms: 2.29x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 214 ms: 2.18x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.45x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 136 ms: 3.69x faster                                                             |
| float          | 69.6 ms                                                         | 46.5 ms: 1.50x faster                                                            |
| nbody          | 79.1 ms                                                         | 82.1 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                           | 1.75x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 93.9 ms: 1.24x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.4 ms: 1.17x faster                                                            |
| regex_dna      | 131 ms                                                          | 112 ms: 1.16x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.65 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.28 ms: 1.57x faster                                                            |
| json_loads           | 22.4 us                                                         | 15.9 us: 1.40x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 91.3 ms: 1.31x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 158 us: 1.20x faster                                                             |
| pickle_pure_python   | 280 us                                                          | 236 us: 1.19x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.7 ms: 1.15x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.03 us: 1.06x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 45.9 ms: 1.05x faster                                                            |
| pickle               | 7.83 us                                                         | 7.94 us: 1.01x slower                                                            |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.04x slower                                                            |
| unpickle_list        | 2.98 us                                                         | 3.10 us: 1.04x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 64.0 ms: 1.04x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.4 us: 1.12x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.41 sec: 1.26x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.8 ms: 1.13x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 27.2 ms: 1.32x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 40.4 ms: 1.15x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 19.9 ms: 1.05x faster                                                            |
| mako            | 9.10 ms                                                         | 10.1 ms: 1.10x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.10x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.17 sec: 7.84x faster                                                           |
| pidigits                 | 502 ms                                                          | 136 ms: 3.69x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 132 us: 3.00x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 333 ms: 2.77x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 29.7 ms: 2.73x faster                                                            |
| async_tree_io            | 940 ms                                                          | 359 ms: 2.62x faster                                                             |
| async_tree_none          | 394 ms                                                          | 172 ms: 2.29x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 214 ms: 2.18x faster                                                             |
| pylint                   | 384 ms                                                          | 202 ms: 1.90x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.36 us: 1.68x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 451 ms: 1.65x faster                                                             |
| deepcopy                 | 310 us                                                          | 190 us: 1.63x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.49 ms: 1.62x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.13 sec: 1.61x faster                                                           |
| chaos                    | 74.4 ms                                                         | 46.4 ms: 1.60x faster                                                            |
| go                       | 146 ms                                                          | 91.2 ms: 1.60x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 61.9 ns: 1.58x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.28 ms: 1.57x faster                                                            |
| thrift                   | 902 us                                                          | 579 us: 1.56x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 19.4 us: 1.53x faster                                                            |
| json                     | 4.76 ms                                                         | 3.13 ms: 1.52x faster                                                            |
| float                    | 69.6 ms                                                         | 46.5 ms: 1.50x faster                                                            |
| comprehensions           | 17.7 us                                                         | 12.0 us: 1.48x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 56.6 ms: 1.44x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 62.8 ms: 1.43x faster                                                            |
| raytrace                 | 303 ms                                                          | 213 ms: 1.42x faster                                                             |
| pycparser                | 1.04 sec                                                        | 741 ms: 1.41x faster                                                             |
| json_loads               | 22.4 us                                                         | 15.9 us: 1.40x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 42.2 ms: 1.39x faster                                                            |
| pyflate                  | 422 ms                                                          | 311 ms: 1.35x faster                                                             |
| generators               | 31.6 ms                                                         | 23.6 ms: 1.33x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.63 ms: 1.32x faster                                                            |
| django_template          | 36.0 ms                                                         | 27.2 ms: 1.32x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 91.3 ms: 1.31x faster                                                            |
| scimark_sor              | 115 ms                                                          | 88.0 ms: 1.31x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.08 us: 1.29x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 40.7 ms: 1.28x faster                                                            |
| sympy_sum                | 122 ms                                                          | 97.2 ms: 1.26x faster                                                            |
| richards_super           | 49.9 ms                                                         | 39.8 ms: 1.25x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 49.6 ms: 1.25x faster                                                            |
| regex_compile            | 117 ms                                                          | 93.9 ms: 1.24x faster                                                            |
| sympy_str                | 229 ms                                                          | 189 ms: 1.21x faster                                                             |
| sympy_expand             | 391 ms                                                          | 324 ms: 1.20x faster                                                             |
| unpickle_pure_python     | 189 us                                                          | 158 us: 1.20x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 73.0 ms: 1.19x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 236 us: 1.19x faster                                                             |
| coroutines               | 17.9 ms                                                         | 15.1 ms: 1.18x faster                                                            |
| richards                 | 40.3 ms                                                         | 34.1 ms: 1.18x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 558 ms: 1.18x faster                                                             |
| regex_v8                 | 15.8 ms                                                         | 13.4 ms: 1.17x faster                                                            |
| 2to3                     | 265 ms                                                          | 228 ms: 1.17x faster                                                             |
| regex_dna                | 131 ms                                                          | 112 ms: 1.16x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 14.3 ms: 1.16x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 40.4 ms: 1.15x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.7 ms: 1.15x faster                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.16 ms: 1.11x faster                                                            |
| logging_format           | 7.91 us                                                         | 7.27 us: 1.09x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.78 us: 1.08x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.03 us: 1.06x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 75.5 ms: 1.06x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 19.9 ms: 1.05x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 45.9 ms: 1.05x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.16 ms: 1.03x faster                                                            |
| fannkuch                 | 317 ms                                                          | 310 ms: 1.02x faster                                                             |
| scimark_fft              | 216 ms                                                          | 213 ms: 1.01x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.65 ms: 1.01x faster                                                            |
| pickle                   | 7.83 us                                                         | 7.94 us: 1.01x slower                                                            |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.04x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.10 us: 1.04x slower                                                            |
| nbody                    | 79.1 ms                                                         | 82.1 ms: 1.04x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 64.0 ms: 1.04x slower                                                            |
| telco                    | 4.83 ms                                                         | 5.03 ms: 1.04x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 85.6 ms: 1.07x slower                                                            |
| async_generators         | 241 ms                                                          | 264 ms: 1.10x slower                                                             |
| mako                     | 9.10 ms                                                         | 10.1 ms: 1.10x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.4 us: 1.12x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.8 ms: 1.13x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 75.1 ms: 1.13x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.69 sec: 1.23x slower                                                           |
| tomli_loads              | 1.91 sec                                                        | 2.41 sec: 1.26x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.02 ms: 1.46x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.90 sec: 1.49x slower                                                           |
| coverage                 | 46.6 ms                                                         | 70.4 ms: 1.51x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.29x faster                                                                     |

Benchmark hidden because not significant (2): bench_thread_pool, unpack_sequence
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250920-3.15.0a0-20d5494-NOGIL/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.288x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown