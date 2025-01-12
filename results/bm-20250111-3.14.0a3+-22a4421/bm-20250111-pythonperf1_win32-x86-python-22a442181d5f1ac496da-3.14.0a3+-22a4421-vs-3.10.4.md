# Results vs. 3.10.4

- fork: python
- ref: 22a442181d5f1ac496da
- machine: windows-x86
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.156x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 248 ms: 1.07x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.81 sec: 1.08x faster                                                          |
| html5lib       | 52.1 ms                                                         | 44.1 ms: 1.18x faster                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 428 ms: 2.20x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 438 ms: 2.11x faster                                                            |
| async_tree_none         | 394 ms                                                          | 199 ms: 1.98x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 242 ms: 1.93x faster                                                            |
| Geometric mean          | (ref)                                                           | 2.05x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.51x faster                                                            |
| float          | 69.6 ms                                                         | 56.2 ms: 1.24x faster                                                           |
| nbody          | 79.1 ms                                                         | 89.4 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                           | 1.40x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 99.9 ms: 1.17x faster                                                           |
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.64 sec: 1.17x faster                                                          |
| json_dumps           | 9.82 ms                                                         | 8.72 ms: 1.13x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 169 us: 1.12x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 261 us: 1.07x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.2 ms: 1.07x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.3 us: 1.05x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 49.9 ms: 1.04x slower                                                           |
| unpickle_list        | 2.98 us                                                         | 3.11 us: 1.04x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.9 us: 1.10x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 70.2 ms: 1.14x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.74 us: 1.16x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 21.4 us: 1.17x slower                                                           |
| pickle               | 7.83 us                                                         | 10.5 us: 1.34x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.3 ms: 1.15x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.54 ms: 1.21x faster                                                           |
| django_template | 36.0 ms                                                         | 31.9 ms: 1.13x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 43.8 ms: 1.07x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 19.8 ms: 1.06x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.11x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 141 us: 2.80x faster                                                            |
| pidigits                 | 502 ms                                                          | 201 ms: 2.51x faster                                                            |
| async_tree_io            | 940 ms                                                          | 428 ms: 2.20x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 438 ms: 2.11x faster                                                            |
| async_tree_none          | 394 ms                                                          | 199 ms: 1.98x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 242 ms: 1.93x faster                                                            |
| pylint                   | 384 ms                                                          | 216 ms: 1.77x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.53 ms: 1.59x faster                                                           |
| go                       | 146 ms                                                          | 96.2 ms: 1.51x faster                                                           |
| chaos                    | 74.4 ms                                                         | 53.8 ms: 1.38x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 21.9 us: 1.35x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 66.9 ms: 1.34x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 73.1 ns: 1.34x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.4 us: 1.32x faster                                                           |
| deepcopy                 | 310 us                                                          | 235 us: 1.32x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 61.7 ms: 1.32x faster                                                           |
| generators               | 31.6 ms                                                         | 24.2 ms: 1.30x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.03 ms: 1.29x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.78 ms: 1.28x faster                                                           |
| pycparser                | 1.04 sec                                                        | 827 ms: 1.26x faster                                                            |
| raytrace                 | 303 ms                                                          | 243 ms: 1.25x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.27 ms: 1.24x faster                                                           |
| float                    | 69.6 ms                                                         | 56.2 ms: 1.24x faster                                                           |
| thrift                   | 902 us                                                          | 734 us: 1.23x faster                                                            |
| richards_super           | 49.9 ms                                                         | 40.6 ms: 1.23x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.54 ms: 1.21x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 44.1 ms: 1.18x faster                                                           |
| regex_compile            | 117 ms                                                          | 99.9 ms: 1.17x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.64 sec: 1.17x faster                                                          |
| sympy_sum                | 122 ms                                                          | 105 ms: 1.17x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 50.4 ms: 1.16x faster                                                           |
| pyflate                  | 422 ms                                                          | 364 ms: 1.16x faster                                                            |
| scimark_sor              | 115 ms                                                          | 99.4 ms: 1.16x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 75.9 ms: 1.15x faster                                                           |
| richards                 | 40.3 ms                                                         | 35.4 ms: 1.14x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.37 us: 1.13x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 2.03 us: 1.13x faster                                                           |
| django_template          | 36.0 ms                                                         | 31.9 ms: 1.13x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.72 ms: 1.13x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 71.4 ms: 1.12x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 169 us: 1.12x faster                                                            |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                            |
| json                     | 4.76 ms                                                         | 4.31 ms: 1.10x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 57.2 ms: 1.08x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 213 ms: 1.08x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 41.4 ms: 1.08x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.81 sec: 1.08x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 261 us: 1.07x faster                                                            |
| 2to3                     | 265 ms                                                          | 248 ms: 1.07x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.2 ms: 1.07x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 43.8 ms: 1.07x faster                                                           |
| sympy_str                | 229 ms                                                          | 216 ms: 1.06x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.73 sec: 1.06x faster                                                          |
| genshi_text              | 21.0 ms                                                         | 19.8 ms: 1.06x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.0 ms: 1.06x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.3 us: 1.05x faster                                                           |
| fannkuch                 | 317 ms                                                          | 304 ms: 1.04x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.11 ms: 1.04x faster                                                           |
| sympy_expand             | 391 ms                                                          | 377 ms: 1.04x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 662 ms: 1.01x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 80.8 ms: 1.01x slower                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.2 sec: 1.01x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 49.9 ms: 1.04x slower                                                           |
| unpickle_list            | 2.98 us                                                         | 3.11 us: 1.04x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 42.1 ns: 1.05x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 87.3 ms: 1.08x slower                                                           |
| scimark_fft              | 216 ms                                                          | 233 ms: 1.08x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.9 us: 1.10x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.20 us: 1.12x slower                                                           |
| nbody                    | 79.1 ms                                                         | 89.4 ms: 1.13x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.97 us: 1.13x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 70.2 ms: 1.14x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.3 ms: 1.15x slower                                                           |
| coverage                 | 46.6 ms                                                         | 54.1 ms: 1.16x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.74 us: 1.16x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 21.4 us: 1.17x slower                                                           |
| async_generators         | 241 ms                                                          | 306 ms: 1.27x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 88.4 ms: 1.33x slower                                                           |
| pickle                   | 7.83 us                                                         | 10.5 us: 1.34x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.67 ms: 1.38x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.80 ms: 1.40x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.53x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.13x faster                                                                    |

Benchmark hidden because not significant (2): pprint_pformat, asyncio_tcp
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.156x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown