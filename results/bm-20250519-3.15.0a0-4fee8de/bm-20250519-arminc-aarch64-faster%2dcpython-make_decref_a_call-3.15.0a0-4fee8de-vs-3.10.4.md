# Results vs. 3.10.4

- fork: faster-cpython
- ref: make_decref_a_call
- machine: linux-aarch64
- commit hash: 4fee8de
- commit date: 2025-05-19
- overall geometric mean: 1.302x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 319 ms: 1.19x faster                                                            |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                          |
| html5lib       | 86.5 ms                                                               | 63.7 ms: 1.36x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 907 ms: 2.52x faster                                                            |
| async_tree_memoization  | 1.13 sec                                                              | 473 ms: 2.39x faster                                                            |
| async_tree_none         | 950 ms                                                                | 399 ms: 2.38x faster                                                            |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 668 ms: 1.90x faster                                                            |
| Geometric mean          | (ref)                                                                 | 2.29x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.0 ms: 1.53x faster                                                           |
| nbody          | 166 ms                                                                | 121 ms: 1.37x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                                            |
| regex_v8       | 32.2 ms                                                               | 28.2 ms: 1.14x faster                                                           |
| regex_effbot   | 4.25 ms                                                               | 3.81 ms: 1.11x faster                                                           |
| regex_dna      | 257 ms                                                                | 232 ms: 1.11x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.18x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 267 us: 1.37x faster                                                            |
| tomli_loads          | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                          |
| pickle_pure_python   | 529 us                                                                | 418 us: 1.27x faster                                                            |
| json_dumps           | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                           |
| xml_etree_process    | 99.5 ms                                                               | 82.8 ms: 1.20x faster                                                           |
| xml_etree_parse      | 212 ms                                                                | 191 ms: 1.11x faster                                                            |
| xml_etree_generate   | 123 ms                                                                | 116 ms: 1.06x faster                                                            |
| xml_etree_iterparse  | 156 ms                                                                | 152 ms: 1.03x faster                                                            |
| json_loads           | 30.9 us                                                               | 36.0 us: 1.17x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.15x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.70 ms: 1.26x slower                                                           |
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.5 ms: 1.31x faster                                                           |
| django_template | 53.3 ms                                                               | 42.5 ms: 1.25x faster                                                           |
| genshi_text     | 35.2 ms                                                               | 28.4 ms: 1.24x faster                                                           |
| genshi_xml      | 69.8 ms                                                               | 63.1 ms: 1.11x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.22x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 209 us: 3.16x faster                                                            |
| async_tree_io            | 2.28 sec                                                              | 907 ms: 2.52x faster                                                            |
| async_tree_memoization   | 1.13 sec                                                              | 473 ms: 2.39x faster                                                            |
| async_tree_none          | 950 ms                                                                | 399 ms: 2.38x faster                                                            |
| deltablue                | 8.94 ms                                                               | 3.82 ms: 2.34x faster                                                           |
| mdp                      | 3.70 sec                                                              | 1.73 sec: 2.14x faster                                                          |
| go                       | 264 ms                                                                | 130 ms: 2.03x faster                                                            |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 668 ms: 1.90x faster                                                            |
| generators               | 68.1 ms                                                               | 36.9 ms: 1.84x faster                                                           |
| richards_super           | 107 ms                                                                | 59.2 ms: 1.81x faster                                                           |
| richards                 | 91.7 ms                                                               | 51.9 ms: 1.77x faster                                                           |
| chaos                    | 121 ms                                                                | 71.8 ms: 1.69x faster                                                           |
| raytrace                 | 573 ms                                                                | 340 ms: 1.68x faster                                                            |
| scimark_sor              | 246 ms                                                                | 152 ms: 1.62x faster                                                            |
| deepcopy_memo            | 61.7 us                                                               | 39.1 us: 1.58x faster                                                           |
| pylint                   | 485 ms                                                                | 315 ms: 1.54x faster                                                            |
| float                    | 135 ms                                                                | 88.0 ms: 1.53x faster                                                           |
| crypto_pyaes             | 134 ms                                                                | 88.0 ms: 1.52x faster                                                           |
| scimark_monte_carlo      | 128 ms                                                                | 84.3 ms: 1.52x faster                                                           |
| hexiom                   | 10.9 ms                                                               | 7.20 ms: 1.52x faster                                                           |
| deepcopy                 | 511 us                                                                | 342 us: 1.49x faster                                                            |
| comprehensions           | 33.1 us                                                               | 22.5 us: 1.47x faster                                                           |
| scimark_lu               | 227 ms                                                                | 157 ms: 1.44x faster                                                            |
| spectral_norm            | 186 ms                                                                | 131 ms: 1.42x faster                                                            |
| pyflate                  | 795 ms                                                                | 560 ms: 1.42x faster                                                            |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                                            |
| dulwich_log              | 73.5 ms                                                               | 53.5 ms: 1.37x faster                                                           |
| nbody                    | 166 ms                                                                | 121 ms: 1.37x faster                                                            |
| unpickle_pure_python     | 366 us                                                                | 267 us: 1.37x faster                                                            |
| html5lib                 | 86.5 ms                                                               | 63.7 ms: 1.36x faster                                                           |
| tomli_loads              | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                          |
| pycparser                | 1.69 sec                                                              | 1.29 sec: 1.31x faster                                                          |
| mako                     | 18.9 ms                                                               | 14.5 ms: 1.31x faster                                                           |
| sympy_integrate          | 26.5 ms                                                               | 20.5 ms: 1.29x faster                                                           |
| pickle_pure_python       | 529 us                                                                | 418 us: 1.27x faster                                                            |
| django_template          | 53.3 ms                                                               | 42.5 ms: 1.25x faster                                                           |
| deepcopy_reduce          | 4.60 us                                                               | 3.69 us: 1.25x faster                                                           |
| logging_simple           | 9.78 us                                                               | 7.88 us: 1.24x faster                                                           |
| thrift                   | 1.26 ms                                                               | 1.02 ms: 1.24x faster                                                           |
| genshi_text              | 35.2 ms                                                               | 28.4 ms: 1.24x faster                                                           |
| pprint_pformat           | 2.36 sec                                                              | 1.93 sec: 1.22x faster                                                          |
| json_dumps               | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                           |
| pprint_safe_repr         | 1.15 sec                                                              | 947 ms: 1.21x faster                                                            |
| sympy_sum                | 184 ms                                                                | 152 ms: 1.21x faster                                                            |
| logging_format           | 10.6 us                                                               | 8.79 us: 1.21x faster                                                           |
| xml_etree_process        | 99.5 ms                                                               | 82.8 ms: 1.20x faster                                                           |
| coroutines               | 37.2 ms                                                               | 31.0 ms: 1.20x faster                                                           |
| 2to3                     | 381 ms                                                                | 319 ms: 1.19x faster                                                            |
| sympy_str                | 329 ms                                                                | 276 ms: 1.19x faster                                                            |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                          |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                           |
| pathlib                  | 26.3 ms                                                               | 23.0 ms: 1.14x faster                                                           |
| regex_v8                 | 32.2 ms                                                               | 28.2 ms: 1.14x faster                                                           |
| scimark_fft              | 500 ms                                                                | 446 ms: 1.12x faster                                                            |
| nqueens                  | 117 ms                                                                | 105 ms: 1.12x faster                                                            |
| regex_effbot             | 4.25 ms                                                               | 3.81 ms: 1.11x faster                                                           |
| sympy_expand             | 543 ms                                                                | 489 ms: 1.11x faster                                                            |
| regex_dna                | 257 ms                                                                | 232 ms: 1.11x faster                                                            |
| genshi_xml               | 69.8 ms                                                               | 63.1 ms: 1.11x faster                                                           |
| xml_etree_parse          | 212 ms                                                                | 191 ms: 1.11x faster                                                            |
| fannkuch                 | 546 ms                                                                | 510 ms: 1.07x faster                                                            |
| xml_etree_generate       | 123 ms                                                                | 116 ms: 1.06x faster                                                            |
| meteor_contest           | 126 ms                                                                | 120 ms: 1.05x faster                                                            |
| sqlite_synth             | 4.12 us                                                               | 3.94 us: 1.04x faster                                                           |
| xml_etree_iterparse      | 156 ms                                                                | 152 ms: 1.03x faster                                                            |
| asyncio_websockets       | 657 ms                                                                | 670 ms: 1.02x slower                                                            |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.86 ms: 1.03x slower                                                           |
| json                     | 5.88 ms                                                               | 6.22 ms: 1.06x slower                                                           |
| async_generators         | 452 ms                                                                | 480 ms: 1.06x slower                                                            |
| json_loads               | 30.9 us                                                               | 36.0 us: 1.17x slower                                                           |
| telco                    | 8.49 ms                                                               | 9.94 ms: 1.17x slower                                                           |
| python_startup_no_site   | 6.89 ms                                                               | 8.70 ms: 1.26x slower                                                           |
| coverage                 | 83.6 ms                                                               | 113 ms: 1.35x slower                                                            |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                           |
| gc_traversal             | 4.15 ms                                                               | 6.92 ms: 1.66x slower                                                           |
| create_gc_cycles         | 2.26 ms                                                               | 3.80 ms: 1.68x slower                                                           |
| logging_silent           | 222 ns                                                                | 629 ns: 2.83x slower                                                            |
| bench_mp_pool            | 14.5 ms                                                               | 4.80 sec: 330.47x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.17x faster                                                                    |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250519-3.15.0a0-4fee8de/bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.302x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.33x