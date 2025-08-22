# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-aarch64
- commit hash: efe4628
- commit date: 2025-08-22
- overall geometric mean: 1.304x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 309 ms: 1.23x faster                                                            |
| docutils       | 3.53 sec                                                              | 3.08 sec: 1.15x faster                                                          |
| html5lib       | 86.5 ms                                                               | 61.7 ms: 1.40x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 879 ms: 2.60x faster                                                            |
| async_tree_none         | 950 ms                                                                | 381 ms: 2.50x faster                                                            |
| async_tree_memoization  | 1.13 sec                                                              | 472 ms: 2.40x faster                                                            |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 660 ms: 1.93x faster                                                            |
| Geometric mean          | (ref)                                                                 | 2.34x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 76.3 ms: 1.77x faster                                                           |
| nbody          | 166 ms                                                                | 106 ms: 1.57x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.40x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.45x faster                                                            |
| regex_v8       | 32.2 ms                                                               | 26.9 ms: 1.19x faster                                                           |
| regex_dna      | 257 ms                                                                | 226 ms: 1.14x faster                                                            |
| regex_effbot   | 4.25 ms                                                               | 3.91 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.24 sec: 1.50x faster                                                          |
| unpickle_pure_python | 366 us                                                                | 249 us: 1.47x faster                                                            |
| json_dumps           | 16.7 ms                                                               | 11.9 ms: 1.40x faster                                                           |
| pickle_pure_python   | 529 us                                                                | 389 us: 1.36x faster                                                            |
| xml_etree_process    | 99.5 ms                                                               | 76.3 ms: 1.30x faster                                                           |
| xml_etree_parse      | 212 ms                                                                | 183 ms: 1.16x faster                                                            |
| xml_etree_generate   | 123 ms                                                                | 108 ms: 1.14x faster                                                            |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.08x faster                                                            |
| json_loads           | 30.9 us                                                               | 33.0 us: 1.07x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.25x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.61 ms: 1.25x slower                                                           |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.8 ms: 1.48x faster                                                           |
| django_template | 53.3 ms                                                               | 38.6 ms: 1.38x faster                                                           |
| genshi_text     | 35.2 ms                                                               | 27.0 ms: 1.30x faster                                                           |
| genshi_xml      | 69.8 ms                                                               | 64.1 ms: 1.09x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.30x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 209 us: 3.16x faster                                                            |
| async_tree_io            | 2.28 sec                                                              | 879 ms: 2.60x faster                                                            |
| async_tree_none          | 950 ms                                                                | 381 ms: 2.50x faster                                                            |
| async_tree_memoization   | 1.13 sec                                                              | 472 ms: 2.40x faster                                                            |
| deltablue                | 8.94 ms                                                               | 3.82 ms: 2.34x faster                                                           |
| mdp                      | 3.70 sec                                                              | 1.66 sec: 2.23x faster                                                          |
| richards_super           | 107 ms                                                                | 49.9 ms: 2.15x faster                                                           |
| richards                 | 91.7 ms                                                               | 44.6 ms: 2.06x faster                                                           |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 660 ms: 1.93x faster                                                            |
| generators               | 68.1 ms                                                               | 36.2 ms: 1.88x faster                                                           |
| go                       | 264 ms                                                                | 147 ms: 1.79x faster                                                            |
| float                    | 135 ms                                                                | 76.3 ms: 1.77x faster                                                           |
| chaos                    | 121 ms                                                                | 68.7 ms: 1.76x faster                                                           |
| scimark_sor              | 246 ms                                                                | 143 ms: 1.72x faster                                                            |
| raytrace                 | 573 ms                                                                | 336 ms: 1.71x faster                                                            |
| logging_silent           | 222 ns                                                                | 131 ns: 1.70x faster                                                            |
| spectral_norm            | 186 ms                                                                | 111 ms: 1.69x faster                                                            |
| deepcopy_memo            | 61.7 us                                                               | 36.8 us: 1.68x faster                                                           |
| scimark_monte_carlo      | 128 ms                                                                | 81.4 ms: 1.57x faster                                                           |
| nbody                    | 166 ms                                                                | 106 ms: 1.57x faster                                                            |
| hexiom                   | 10.9 ms                                                               | 7.03 ms: 1.55x faster                                                           |
| pyflate                  | 795 ms                                                                | 524 ms: 1.52x faster                                                            |
| scimark_lu               | 227 ms                                                                | 149 ms: 1.52x faster                                                            |
| deepcopy                 | 511 us                                                                | 338 us: 1.51x faster                                                            |
| comprehensions           | 33.1 us                                                               | 22.1 us: 1.50x faster                                                           |
| tomli_loads              | 3.36 sec                                                              | 2.24 sec: 1.50x faster                                                          |
| crypto_pyaes             | 134 ms                                                                | 90.3 ms: 1.48x faster                                                           |
| pylint                   | 485 ms                                                                | 328 ms: 1.48x faster                                                            |
| mako                     | 18.9 ms                                                               | 12.8 ms: 1.48x faster                                                           |
| logging_simple           | 9.78 us                                                               | 6.63 us: 1.48x faster                                                           |
| unpickle_pure_python     | 366 us                                                                | 249 us: 1.47x faster                                                            |
| logging_format           | 10.6 us                                                               | 7.32 us: 1.45x faster                                                           |
| regex_compile            | 177 ms                                                                | 122 ms: 1.45x faster                                                            |
| html5lib                 | 86.5 ms                                                               | 61.7 ms: 1.40x faster                                                           |
| json_dumps               | 16.7 ms                                                               | 11.9 ms: 1.40x faster                                                           |
| django_template          | 53.3 ms                                                               | 38.6 ms: 1.38x faster                                                           |
| pickle_pure_python       | 529 us                                                                | 389 us: 1.36x faster                                                            |
| dulwich_log              | 73.5 ms                                                               | 55.6 ms: 1.32x faster                                                           |
| scimark_fft              | 500 ms                                                                | 382 ms: 1.31x faster                                                            |
| xml_etree_process        | 99.5 ms                                                               | 76.3 ms: 1.30x faster                                                           |
| genshi_text              | 35.2 ms                                                               | 27.0 ms: 1.30x faster                                                           |
| thrift                   | 1.26 ms                                                               | 989 us: 1.27x faster                                                            |
| pycparser                | 1.69 sec                                                              | 1.35 sec: 1.26x faster                                                          |
| deepcopy_reduce          | 4.60 us                                                               | 3.70 us: 1.24x faster                                                           |
| sympy_sum                | 184 ms                                                                | 149 ms: 1.24x faster                                                            |
| 2to3                     | 381 ms                                                                | 309 ms: 1.23x faster                                                            |
| sympy_integrate          | 26.5 ms                                                               | 21.6 ms: 1.23x faster                                                           |
| coroutines               | 37.2 ms                                                               | 31.1 ms: 1.20x faster                                                           |
| regex_v8                 | 32.2 ms                                                               | 26.9 ms: 1.19x faster                                                           |
| fannkuch                 | 546 ms                                                                | 464 ms: 1.18x faster                                                            |
| sympy_str                | 329 ms                                                                | 280 ms: 1.17x faster                                                            |
| nqueens                  | 117 ms                                                                | 101 ms: 1.16x faster                                                            |
| xml_etree_parse          | 212 ms                                                                | 183 ms: 1.16x faster                                                            |
| docutils                 | 3.53 sec                                                              | 3.08 sec: 1.15x faster                                                          |
| regex_dna                | 257 ms                                                                | 226 ms: 1.14x faster                                                            |
| xml_etree_generate       | 123 ms                                                                | 108 ms: 1.14x faster                                                            |
| pathlib                  | 26.3 ms                                                               | 23.2 ms: 1.14x faster                                                           |
| sqlite_synth             | 4.12 us                                                               | 3.65 us: 1.13x faster                                                           |
| sympy_expand             | 543 ms                                                                | 486 ms: 1.12x faster                                                            |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.11x faster                                                            |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.95 ms: 1.10x faster                                                           |
| genshi_xml               | 69.8 ms                                                               | 64.1 ms: 1.09x faster                                                           |
| regex_effbot             | 4.25 ms                                                               | 3.91 ms: 1.09x faster                                                           |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.08x faster                                                            |
| pprint_pformat           | 2.36 sec                                                              | 2.30 sec: 1.02x faster                                                          |
| json                     | 5.88 ms                                                               | 5.77 ms: 1.02x faster                                                           |
| pprint_safe_repr         | 1.15 sec                                                              | 1.13 sec: 1.01x faster                                                          |
| asyncio_websockets       | 657 ms                                                                | 671 ms: 1.02x slower                                                            |
| json_loads               | 30.9 us                                                               | 33.0 us: 1.07x slower                                                           |
| async_generators         | 452 ms                                                                | 494 ms: 1.09x slower                                                            |
| coverage                 | 83.6 ms                                                               | 104 ms: 1.24x slower                                                            |
| python_startup_no_site   | 6.89 ms                                                               | 8.61 ms: 1.25x slower                                                           |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                           |
| gc_traversal             | 4.15 ms                                                               | 6.96 ms: 1.68x slower                                                           |
| create_gc_cycles         | 2.26 ms                                                               | 3.86 ms: 1.71x slower                                                           |
| telco                    | 8.49 ms                                                               | 166 ms: 19.51x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.29x faster                                                                    |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250822-3.15.0a0-efe4628-JIT/bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.304x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.41x