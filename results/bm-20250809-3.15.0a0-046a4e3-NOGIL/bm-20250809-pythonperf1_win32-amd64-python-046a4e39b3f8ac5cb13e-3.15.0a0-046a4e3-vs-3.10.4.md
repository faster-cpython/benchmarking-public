# Results vs. 3.10.4

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.271x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 229 ms: 1.16x faster                                                             |
| docutils       | 1.95 sec                                                        | 2.92 sec: 1.50x slower                                                           |
| html5lib       | 52.1 ms                                                         | 41.0 ms: 1.27x faster                                                            |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 336 ms: 2.75x faster                                                             |
| async_tree_io           | 940 ms                                                          | 354 ms: 2.66x faster                                                             |
| async_tree_none         | 394 ms                                                          | 173 ms: 2.27x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 210 ms: 2.22x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.46x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 137 ms: 3.66x faster                                                             |
| float          | 69.6 ms                                                         | 47.1 ms: 1.48x faster                                                            |
| nbody          | 79.1 ms                                                         | 86.2 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                           | 1.71x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 12.8 ms: 1.23x faster                                                            |
| regex_compile  | 117 ms                                                          | 95.1 ms: 1.23x faster                                                            |
| regex_dna      | 131 ms                                                          | 112 ms: 1.16x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.53 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.96 ms: 1.65x faster                                                            |
| json_loads           | 22.4 us                                                         | 15.7 us: 1.43x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 90.5 ms: 1.33x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 58.3 ms: 1.22x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 235 us: 1.19x faster                                                             |
| unpickle_pure_python | 189 us                                                          | 160 us: 1.19x faster                                                             |
| pickle_list          | 3.22 us                                                         | 2.98 us: 1.08x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 44.7 ms: 1.08x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 63.0 ms: 1.02x slower                                                            |
| unpickle             | 9.82 us                                                         | 10.1 us: 1.03x slower                                                            |
| unpickle_list        | 2.98 us                                                         | 3.07 us: 1.03x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.8 us: 1.09x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.75 sec: 1.44x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                            |
| python_startup         | 22.9 ms                                                         | 27.1 ms: 1.18x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 27.3 ms: 1.32x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 41.6 ms: 1.12x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 20.5 ms: 1.02x faster                                                            |
| mako            | 9.10 ms                                                         | 10.1 ms: 1.11x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.50 sec: 6.78x faster                                                           |
| pidigits                 | 502 ms                                                          | 137 ms: 3.66x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 132 us: 2.99x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 336 ms: 2.75x faster                                                             |
| async_tree_io            | 940 ms                                                          | 354 ms: 2.66x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 32.7 ms: 2.49x faster                                                            |
| async_tree_none          | 394 ms                                                          | 173 ms: 2.27x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 210 ms: 2.22x faster                                                             |
| pylint                   | 384 ms                                                          | 207 ms: 1.86x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 5.96 ms: 1.65x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.40 us: 1.64x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.50 ms: 1.61x faster                                                            |
| json                     | 4.76 ms                                                         | 3.04 ms: 1.57x faster                                                            |
| chaos                    | 74.4 ms                                                         | 47.5 ms: 1.57x faster                                                            |
| thrift                   | 902 us                                                          | 577 us: 1.56x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 62.9 ns: 1.56x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.18 sec: 1.55x faster                                                           |
| go                       | 146 ms                                                          | 94.6 ms: 1.54x faster                                                            |
| deepcopy                 | 310 us                                                          | 207 us: 1.50x faster                                                             |
| float                    | 69.6 ms                                                         | 47.1 ms: 1.48x faster                                                            |
| comprehensions           | 17.7 us                                                         | 12.3 us: 1.44x faster                                                            |
| raytrace                 | 303 ms                                                          | 211 ms: 1.43x faster                                                             |
| json_loads               | 22.4 us                                                         | 15.7 us: 1.43x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 58.0 ms: 1.40x faster                                                            |
| pycparser                | 1.04 sec                                                        | 752 ms: 1.39x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 42.8 ms: 1.37x faster                                                            |
| generators               | 31.6 ms                                                         | 23.3 ms: 1.36x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 21.8 us: 1.35x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 67.4 ms: 1.33x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 90.5 ms: 1.33x faster                                                            |
| django_template          | 36.0 ms                                                         | 27.3 ms: 1.32x faster                                                            |
| pyflate                  | 422 ms                                                          | 320 ms: 1.32x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 565 ms: 1.32x faster                                                             |
| scimark_sor              | 115 ms                                                          | 87.7 ms: 1.31x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.74 ms: 1.29x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 41.0 ms: 1.27x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 49.0 ms: 1.26x faster                                                            |
| richards_super           | 49.9 ms                                                         | 39.8 ms: 1.25x faster                                                            |
| sympy_sum                | 122 ms                                                          | 99.1 ms: 1.24x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.18 us: 1.23x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 12.8 ms: 1.23x faster                                                            |
| regex_compile            | 117 ms                                                          | 95.1 ms: 1.23x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 58.3 ms: 1.22x faster                                                            |
| sympy_str                | 229 ms                                                          | 191 ms: 1.20x faster                                                             |
| sympy_expand             | 391 ms                                                          | 326 ms: 1.20x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 235 us: 1.19x faster                                                             |
| unpickle_pure_python     | 189 us                                                          | 160 us: 1.19x faster                                                             |
| richards                 | 40.3 ms                                                         | 34.3 ms: 1.17x faster                                                            |
| coroutines               | 17.9 ms                                                         | 15.4 ms: 1.17x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 565 ms: 1.17x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 14.3 ms: 1.16x faster                                                            |
| regex_dna                | 131 ms                                                          | 112 ms: 1.16x faster                                                             |
| 2to3                     | 265 ms                                                          | 229 ms: 1.16x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 76.0 ms: 1.15x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 41.6 ms: 1.12x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.53 ms: 1.09x faster                                                            |
| logging_format           | 7.91 us                                                         | 7.32 us: 1.08x faster                                                            |
| pickle_list              | 3.22 us                                                         | 2.98 us: 1.08x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 44.7 ms: 1.08x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 37.7 ns: 1.06x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 75.8 ms: 1.06x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.92 us: 1.05x faster                                                            |
| fannkuch                 | 317 ms                                                          | 310 ms: 1.02x faster                                                             |
| genshi_text              | 21.0 ms                                                         | 20.5 ms: 1.02x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.17 ms: 1.02x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.10 ms: 1.02x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 63.0 ms: 1.02x slower                                                            |
| unpickle                 | 9.82 us                                                         | 10.1 us: 1.03x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.07 us: 1.03x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.8 us: 1.09x slower                                                            |
| nbody                    | 79.1 ms                                                         | 86.2 ms: 1.09x slower                                                            |
| telco                    | 4.83 ms                                                         | 5.29 ms: 1.10x slower                                                            |
| async_generators         | 241 ms                                                          | 266 ms: 1.10x slower                                                             |
| meteor_contest           | 80.0 ms                                                         | 88.2 ms: 1.10x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                            |
| mako                     | 9.10 ms                                                         | 10.1 ms: 1.11x slower                                                            |
| python_startup           | 22.9 ms                                                         | 27.1 ms: 1.18x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 80.9 ms: 1.22x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.76 sec: 1.29x slower                                                           |
| tomli_loads              | 1.91 sec                                                        | 2.75 sec: 1.44x slower                                                           |
| coverage                 | 46.6 ms                                                         | 69.4 ms: 1.49x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.92 sec: 1.50x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.52x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.26x faster                                                                     |

Benchmark hidden because not significant (3): gc_traversal, pickle, scimark_fft
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.271x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown