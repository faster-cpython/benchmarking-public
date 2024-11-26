# Results vs. 3.10.4

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: windows-x86
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.121x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 251 ms: 1.06x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.84 sec: 1.06x faster                                                          |
| html5lib       | 52.1 ms                                                         | 46.0 ms: 1.13x faster                                                           |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 469 ms: 1.96x faster                                                            |
| async_tree_io           | 940 ms                                                          | 519 ms: 1.81x faster                                                            |
| async_tree_none         | 394 ms                                                          | 219 ms: 1.80x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 275 ms: 1.70x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.82x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.51x faster                                                            |
| float          | 69.6 ms                                                         | 61.7 ms: 1.13x faster                                                           |
| nbody          | 79.1 ms                                                         | 95.8 ms: 1.21x slower                                                           |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 105 ms: 1.11x faster                                                            |
| regex_dna      | 131 ms                                                          | 122 ms: 1.07x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.88 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.75 ms: 1.12x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 113 ms: 1.07x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 178 us: 1.07x faster                                                            |
| json_loads           | 22.4 us                                                         | 21.2 us: 1.06x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.81 sec: 1.05x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 267 us: 1.05x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.5 ms: 1.03x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 50.5 ms: 1.05x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 68.8 ms: 1.12x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.62 ms: 1.19x faster                                                           |
| django_template | 36.0 ms                                                         | 32.7 ms: 1.10x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 20.7 ms: 1.01x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 46.1 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 147 us: 2.69x faster                                                            |
| pidigits                 | 502 ms                                                          | 201 ms: 2.51x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 469 ms: 1.96x faster                                                            |
| async_tree_io            | 940 ms                                                          | 519 ms: 1.81x faster                                                            |
| async_tree_none          | 394 ms                                                          | 219 ms: 1.80x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 275 ms: 1.70x faster                                                            |
| pylint                   | 384 ms                                                          | 232 ms: 1.65x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.67 ms: 1.51x faster                                                           |
| go                       | 146 ms                                                          | 101 ms: 1.45x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 70.5 ns: 1.39x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 59.8 ms: 1.36x faster                                                           |
| deepcopy                 | 310 us                                                          | 235 us: 1.32x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 22.5 us: 1.31x faster                                                           |
| generators               | 31.6 ms                                                         | 24.4 ms: 1.29x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 69.5 ms: 1.29x faster                                                           |
| pycparser                | 1.04 sec                                                        | 823 ms: 1.27x faster                                                            |
| chaos                    | 74.4 ms                                                         | 58.8 ms: 1.27x faster                                                           |
| comprehensions           | 17.7 us                                                         | 14.3 us: 1.24x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.08 ms: 1.23x faster                                                           |
| raytrace                 | 303 ms                                                          | 249 ms: 1.22x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 5.11 ms: 1.20x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.32 ms: 1.20x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.62 ms: 1.19x faster                                                           |
| thrift                   | 902 us                                                          | 757 us: 1.19x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.94 us: 1.18x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 74.0 ms: 1.18x faster                                                           |
| sympy_sum                | 122 ms                                                          | 105 ms: 1.16x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 46.0 ms: 1.13x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 51.8 ms: 1.13x faster                                                           |
| pyflate                  | 422 ms                                                          | 373 ms: 1.13x faster                                                            |
| float                    | 69.6 ms                                                         | 61.7 ms: 1.13x faster                                                           |
| richards_super           | 49.9 ms                                                         | 44.3 ms: 1.13x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.75 ms: 1.12x faster                                                           |
| regex_compile            | 117 ms                                                          | 105 ms: 1.11x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 56.2 ms: 1.10x faster                                                           |
| django_template          | 36.0 ms                                                         | 32.7 ms: 1.10x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.3 ms: 1.10x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.03 ms: 1.09x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.68 sec: 1.08x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.50 us: 1.08x faster                                                           |
| regex_dna                | 131 ms                                                          | 122 ms: 1.07x faster                                                            |
| sympy_str                | 229 ms                                                          | 214 ms: 1.07x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 113 ms: 1.07x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 178 us: 1.07x faster                                                            |
| json                     | 4.76 ms                                                         | 4.49 ms: 1.06x faster                                                           |
| 2to3                     | 265 ms                                                          | 251 ms: 1.06x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.84 sec: 1.06x faster                                                          |
| scimark_sor              | 115 ms                                                          | 109 ms: 1.06x faster                                                            |
| json_loads               | 22.4 us                                                         | 21.2 us: 1.06x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.81 sec: 1.05x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 267 us: 1.05x faster                                                            |
| richards                 | 40.3 ms                                                         | 38.4 ms: 1.05x faster                                                           |
| sympy_expand             | 391 ms                                                          | 376 ms: 1.04x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.5 ms: 1.03x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 77.7 ms: 1.03x faster                                                           |
| genshi_text              | 21.0 ms                                                         | 20.7 ms: 1.01x faster                                                           |
| fannkuch                 | 317 ms                                                          | 314 ms: 1.01x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 46.1 ms: 1.01x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 234 ms: 1.01x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 81.4 ms: 1.02x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.40 sec: 1.02x slower                                                          |
| pprint_safe_repr         | 658 ms                                                          | 677 ms: 1.03x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 50.5 ms: 1.05x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 86.7 ms: 1.07x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.81 us: 1.07x slower                                                           |
| scimark_fft              | 216 ms                                                          | 233 ms: 1.08x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.54 us: 1.08x slower                                                           |
| coverage                 | 46.6 ms                                                         | 51.7 ms: 1.11x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 68.8 ms: 1.12x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.88 ms: 1.13x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                           |
| nbody                    | 79.1 ms                                                         | 95.8 ms: 1.21x slower                                                           |
| async_generators         | 241 ms                                                          | 300 ms: 1.25x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 88.7 ms: 1.34x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.59 ms: 1.36x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.78 ms: 1.39x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.16 ms: 1.67x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.12x faster                                                                    |

Benchmark hidden because not significant (2): scimark_sparse_mat_mult, sqlglot_optimize
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.121x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown