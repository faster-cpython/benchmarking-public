# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-x86
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.284x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 240 ms: 1.11x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.73 sec: 1.13x faster                                                          |
| html5lib       | 52.1 ms                                                         | 42.4 ms: 1.23x faster                                                           |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 385 ms: 2.44x faster                                                            |
| async_tree_none         | 394 ms                                                          | 176 ms: 2.24x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 215 ms: 2.17x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 438 ms: 2.11x faster                                                            |
| Geometric mean          | (ref)                                                           | 2.23x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 217 ms: 2.32x faster                                                            |
| float          | 69.6 ms                                                         | 44.0 ms: 1.58x faster                                                           |
| nbody          | 79.1 ms                                                         | 64.5 ms: 1.23x faster                                                           |
| Geometric mean | (ref)                                                           | 1.65x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 90.0 ms: 1.30x faster                                                           |
| regex_dna      | 131 ms                                                          | 132 ms: 1.01x slower                                                            |
| regex_v8       | 15.8 ms                                                         | 17.4 ms: 1.10x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.97 ms: 1.19x slower                                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.39 sec: 1.37x faster                                                          |
| json_dumps           | 9.82 ms                                                         | 7.71 ms: 1.27x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 220 us: 1.27x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 151 us: 1.25x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 114 ms: 1.05x faster                                                            |
| json_loads           | 22.4 us                                                         | 21.5 us: 1.04x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 46.6 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 71.8 ms: 1.01x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 66.3 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 22.6 ms: 1.25x slower                                                           |
| python_startup         | 22.9 ms                                                         | 29.6 ms: 1.29x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.27x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 21.0 ms                                                         | 15.9 ms: 1.32x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 36.0 ms: 1.30x faster                                                           |
| django_template | 36.0 ms                                                         | 28.6 ms: 1.26x faster                                                           |
| mako            | 9.10 ms                                                         | 7.59 ms: 1.20x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.27x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 126 us: 3.14x faster                                                            |
| async_tree_io            | 940 ms                                                          | 385 ms: 2.44x faster                                                            |
| pidigits                 | 502 ms                                                          | 217 ms: 2.32x faster                                                            |
| async_tree_none          | 394 ms                                                          | 176 ms: 2.24x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 215 ms: 2.17x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 438 ms: 2.11x faster                                                            |
| deltablue                | 4.04 ms                                                         | 1.97 ms: 2.05x faster                                                           |
| go                       | 146 ms                                                          | 77.5 ms: 1.88x faster                                                           |
| pylint                   | 384 ms                                                          | 207 ms: 1.86x faster                                                            |
| generators               | 31.6 ms                                                         | 17.5 ms: 1.80x faster                                                           |
| chaos                    | 74.4 ms                                                         | 43.8 ms: 1.70x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 17.7 us: 1.67x faster                                                           |
| deepcopy                 | 310 us                                                          | 189 us: 1.64x faster                                                            |
| raytrace                 | 303 ms                                                          | 186 ms: 1.63x faster                                                            |
| scimark_sor              | 115 ms                                                          | 72.7 ms: 1.58x faster                                                           |
| float                    | 69.6 ms                                                         | 44.0 ms: 1.58x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 858 us: 1.55x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.6 ms: 1.49x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 54.9 ms: 1.48x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 66.4 ns: 1.47x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.08 ms: 1.47x faster                                                           |
| comprehensions           | 17.7 us                                                         | 12.1 us: 1.47x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.22 ms: 1.45x faster                                                           |
| pyflate                  | 422 ms                                                          | 293 ms: 1.44x faster                                                            |
| richards_super           | 49.9 ms                                                         | 34.8 ms: 1.43x faster                                                           |
| thrift                   | 902 us                                                          | 645 us: 1.40x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.39 sec: 1.37x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 58.6 ms: 1.37x faster                                                           |
| pycparser                | 1.04 sec                                                        | 765 ms: 1.36x faster                                                            |
| coroutines               | 17.9 ms                                                         | 13.2 ms: 1.36x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.01 us: 1.33x faster                                                           |
| genshi_text              | 21.0 ms                                                         | 15.9 ms: 1.32x faster                                                           |
| richards                 | 40.3 ms                                                         | 30.6 ms: 1.32x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 68.5 ms: 1.31x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 36.0 ms: 1.30x faster                                                           |
| regex_compile            | 117 ms                                                          | 90.0 ms: 1.30x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.07 sec: 1.28x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.71 ms: 1.27x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 68.4 ms: 1.27x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 220 us: 1.27x faster                                                            |
| django_template          | 36.0 ms                                                         | 28.6 ms: 1.26x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 524 ms: 1.26x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.58 ms: 1.26x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 151 us: 1.25x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 46.8 ms: 1.25x faster                                                           |
| sympy_sum                | 122 ms                                                          | 98.1 ms: 1.25x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.85 us: 1.24x faster                                                           |
| pathlib                  | 81.2 ms                                                         | 66.0 ms: 1.23x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 42.4 ms: 1.23x faster                                                           |
| nbody                    | 79.1 ms                                                         | 64.5 ms: 1.23x faster                                                           |
| sympy_str                | 229 ms                                                          | 190 ms: 1.20x faster                                                            |
| mako                     | 9.10 ms                                                         | 7.59 ms: 1.20x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 192 ms: 1.20x faster                                                            |
| sympy_expand             | 391 ms                                                          | 328 ms: 1.19x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 14.0 ms: 1.19x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 38.3 ms: 1.17x faster                                                           |
| fannkuch                 | 317 ms                                                          | 273 ms: 1.16x faster                                                            |
| json                     | 4.76 ms                                                         | 4.21 ms: 1.13x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.73 sec: 1.13x faster                                                          |
| scimark_fft              | 216 ms                                                          | 193 ms: 1.12x faster                                                            |
| 2to3                     | 265 ms                                                          | 240 ms: 1.11x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 74.9 ms: 1.07x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 114 ms: 1.05x faster                                                            |
| async_generators         | 241 ms                                                          | 231 ms: 1.04x faster                                                            |
| json_loads               | 22.4 us                                                         | 21.5 us: 1.04x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 46.6 ms: 1.03x faster                                                           |
| logging_format           | 7.91 us                                                         | 7.65 us: 1.03x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.77 sec: 1.03x faster                                                          |
| logging_simple           | 7.29 us                                                         | 7.17 us: 1.02x faster                                                           |
| regex_dna                | 131 ms                                                          | 132 ms: 1.01x slower                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 71.8 ms: 1.01x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 66.3 ms: 1.08x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 17.4 ms: 1.10x slower                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.31 ms: 1.17x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.97 ms: 1.19x slower                                                           |
| coverage                 | 46.6 ms                                                         | 55.7 ms: 1.20x slower                                                           |
| telco                    | 4.83 ms                                                         | 5.91 ms: 1.22x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 22.6 ms: 1.25x slower                                                           |
| python_startup           | 22.9 ms                                                         | 29.6 ms: 1.29x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 98.1 ms: 1.48x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.19 ms: 1.72x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 2.43 ms: 1.90x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.27x faster                                                                    |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.284x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown