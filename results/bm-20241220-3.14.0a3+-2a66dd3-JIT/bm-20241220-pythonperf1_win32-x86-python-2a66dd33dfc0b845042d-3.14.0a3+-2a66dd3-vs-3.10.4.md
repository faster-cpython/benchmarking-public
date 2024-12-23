# Results vs. 3.10.4

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: windows-x86
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.054x faster
- HPT reliability: 75.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| html5lib       | 52.1 ms                                                         | 48.9 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 481 ms: 1.92x faster                                                            |
| async_tree_io           | 940 ms                                                          | 497 ms: 1.89x faster                                                            |
| async_tree_none         | 394 ms                                                          | 238 ms: 1.65x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 290 ms: 1.61x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.76x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 203 ms: 2.48x faster                                                            |
| float          | 69.6 ms                                                         | 57.3 ms: 1.21x faster                                                           |
| nbody          | 79.1 ms                                                         | 96.3 ms: 1.22x slower                                                           |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 114 ms: 1.15x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                           |
| regex_compile  | 117 ms                                                          | 114 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.75 sec: 1.09x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.6 ms: 1.06x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.1 us: 1.06x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 9.55 ms: 1.03x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 205 us: 1.08x slower                                                            |
| pickle_pure_python   | 280 us                                                          | 303 us: 1.08x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 52.5 ms: 1.09x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 70.0 ms: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.00x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.08x slower                                                           |
| python_startup         | 22.9 ms                                                         | 25.8 ms: 1.12x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.33 ms: 1.24x faster                                                           |
| django_template | 36.0 ms                                                         | 37.6 ms: 1.04x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 55.9 ms: 1.20x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 25.3 ms: 1.21x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.05x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 203 ms: 2.48x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 170 us: 2.33x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 108 ms: 2.13x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 481 ms: 1.92x faster                                                            |
| async_tree_io            | 940 ms                                                          | 497 ms: 1.89x faster                                                            |
| async_tree_none          | 394 ms                                                          | 238 ms: 1.65x faster                                                            |
| pylint                   | 384 ms                                                          | 234 ms: 1.64x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 290 ms: 1.61x faster                                                            |
| deltablue                | 4.04 ms                                                         | 3.23 ms: 1.25x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.33 ms: 1.24x faster                                                           |
| float                    | 69.6 ms                                                         | 57.3 ms: 1.21x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 74.3 ms: 1.21x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 24.8 us: 1.19x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 68.8 ms: 1.18x faster                                                           |
| go                       | 146 ms                                                          | 123 ms: 1.18x faster                                                            |
| thrift                   | 902 us                                                          | 776 us: 1.16x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.98 us: 1.16x faster                                                           |
| scimark_sor              | 115 ms                                                          | 100 ms: 1.15x faster                                                            |
| regex_dna                | 131 ms                                                          | 114 ms: 1.15x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 51.3 ms: 1.14x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.17 ms: 1.14x faster                                                           |
| pyflate                  | 422 ms                                                          | 372 ms: 1.13x faster                                                            |
| chaos                    | 74.4 ms                                                         | 65.6 ms: 1.13x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 86.6 ns: 1.13x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                            |
| deepcopy                 | 310 us                                                          | 282 us: 1.10x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 73.1 ms: 1.10x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.45 ms: 1.09x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.75 sec: 1.09x faster                                                          |
| pycparser                | 1.04 sec                                                        | 958 ms: 1.09x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.04 ms: 1.08x faster                                                           |
| json                     | 4.76 ms                                                         | 4.43 ms: 1.07x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 48.9 ms: 1.07x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.6 ms: 1.06x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.1 us: 1.06x faster                                                           |
| sympy_sum                | 122 ms                                                          | 116 ms: 1.06x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.06 ms: 1.06x faster                                                           |
| richards_super           | 49.9 ms                                                         | 48.0 ms: 1.04x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.3 ms: 1.04x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 9.55 ms: 1.03x faster                                                           |
| regex_compile            | 117 ms                                                          | 114 ms: 1.02x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 62.9 ms: 1.02x slower                                                           |
| sympy_str                | 229 ms                                                          | 236 ms: 1.03x slower                                                            |
| pathlib                  | 81.2 ms                                                         | 83.8 ms: 1.03x slower                                                           |
| mdp                      | 1.83 sec                                                        | 1.90 sec: 1.04x slower                                                          |
| django_template          | 36.0 ms                                                         | 37.6 ms: 1.04x slower                                                           |
| comprehensions           | 17.7 us                                                         | 18.6 us: 1.05x slower                                                           |
| fannkuch                 | 317 ms                                                          | 333 ms: 1.05x slower                                                            |
| sympy_expand             | 391 ms                                                          | 411 ms: 1.05x slower                                                            |
| sympy_integrate          | 16.6 ms                                                         | 17.7 ms: 1.06x slower                                                           |
| raytrace                 | 303 ms                                                          | 322 ms: 1.07x slower                                                            |
| richards                 | 40.3 ms                                                         | 43.0 ms: 1.07x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.08x slower                                                           |
| unpickle_pure_python     | 189 us                                                          | 205 us: 1.08x slower                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.90 us: 1.08x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 303 us: 1.08x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 52.5 ms: 1.09x slower                                                           |
| scimark_fft              | 216 ms                                                          | 237 ms: 1.10x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.52 sec: 1.11x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 88.7 ms: 1.11x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 97.7 ms: 1.12x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 739 ms: 1.12x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.8 ms: 1.12x slower                                                           |
| coverage                 | 46.6 ms                                                         | 52.7 ms: 1.13x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 70.0 ms: 1.13x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 51.3 ms: 1.15x slower                                                           |
| generators               | 31.6 ms                                                         | 36.5 ms: 1.16x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.17 us: 1.16x slower                                                           |
| hexiom                   | 6.13 ms                                                         | 7.12 ms: 1.16x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.53 us: 1.17x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 55.9 ms: 1.20x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 25.3 ms: 1.21x slower                                                           |
| nbody                    | 79.1 ms                                                         | 96.3 ms: 1.22x slower                                                           |
| mypy2                    | 590 ms                                                          | 736 ms: 1.25x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 87.3 ms: 1.32x slower                                                           |
| async_generators         | 241 ms                                                          | 323 ms: 1.34x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.82 ms: 1.42x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.19 ms: 1.49x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.53x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (3): 2to3, regex_v8, docutils
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.054x faster

# HPT report

- Reliability score: 75.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown