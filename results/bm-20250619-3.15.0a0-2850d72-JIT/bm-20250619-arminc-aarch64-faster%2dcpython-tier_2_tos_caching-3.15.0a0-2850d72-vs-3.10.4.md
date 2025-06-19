# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-aarch64
- commit hash: 2850d72
- commit date: 2025-06-19
- overall geometric mean: 1.331x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 311 ms: 1.23x faster                                                            |
| docutils       | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                          |
| html5lib       | 86.5 ms                                                               | 63.7 ms: 1.36x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 910 ms: 2.51x faster                                                            |
| async_tree_memoization  | 1.13 sec                                                              | 476 ms: 2.38x faster                                                            |
| async_tree_none         | 950 ms                                                                | 402 ms: 2.37x faster                                                            |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 668 ms: 1.90x faster                                                            |
| Geometric mean          | (ref)                                                                 | 2.28x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 77.3 ms: 1.74x faster                                                           |
| nbody          | 166 ms                                                                | 105 ms: 1.57x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.39x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.45x faster                                                            |
| regex_v8       | 32.2 ms                                                               | 27.0 ms: 1.19x faster                                                           |
| regex_dna      | 257 ms                                                                | 216 ms: 1.19x faster                                                            |
| regex_effbot   | 4.25 ms                                                               | 3.89 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.22x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.29 sec: 1.47x faster                                                          |
| unpickle_pure_python | 366 us                                                                | 253 us: 1.44x faster                                                            |
| pickle_pure_python   | 529 us                                                                | 391 us: 1.35x faster                                                            |
| xml_etree_process    | 99.5 ms                                                               | 77.2 ms: 1.29x faster                                                           |
| json_dumps           | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                           |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.19x faster                                                            |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.12x faster                                                            |
| xml_etree_iterparse  | 156 ms                                                                | 142 ms: 1.10x faster                                                            |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.22x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.58 ms: 1.25x slower                                                           |
| python_startup         | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.43x faster                                                           |
| genshi_text     | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                                           |
| django_template | 53.3 ms                                                               | 41.4 ms: 1.29x faster                                                           |
| genshi_xml      | 69.8 ms                                                               | 64.3 ms: 1.09x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.19x faster                                                            |
| async_tree_io            | 2.28 sec                                                              | 910 ms: 2.51x faster                                                            |
| deltablue                | 8.94 ms                                                               | 3.73 ms: 2.40x faster                                                           |
| async_tree_memoization   | 1.13 sec                                                              | 476 ms: 2.38x faster                                                            |
| async_tree_none          | 950 ms                                                                | 402 ms: 2.37x faster                                                            |
| mdp                      | 3.70 sec                                                              | 1.69 sec: 2.19x faster                                                          |
| richards_super           | 107 ms                                                                | 52.4 ms: 2.05x faster                                                           |
| richards                 | 91.7 ms                                                               | 45.6 ms: 2.01x faster                                                           |
| generators               | 68.1 ms                                                               | 35.2 ms: 1.93x faster                                                           |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 668 ms: 1.90x faster                                                            |
| float                    | 135 ms                                                                | 77.3 ms: 1.74x faster                                                           |
| scimark_sor              | 246 ms                                                                | 141 ms: 1.74x faster                                                            |
| raytrace                 | 573 ms                                                                | 332 ms: 1.73x faster                                                            |
| chaos                    | 121 ms                                                                | 70.4 ms: 1.72x faster                                                           |
| go                       | 264 ms                                                                | 159 ms: 1.66x faster                                                            |
| deepcopy_memo            | 61.7 us                                                               | 38.2 us: 1.61x faster                                                           |
| scimark_monte_carlo      | 128 ms                                                                | 80.3 ms: 1.59x faster                                                           |
| spectral_norm            | 186 ms                                                                | 118 ms: 1.58x faster                                                            |
| nbody                    | 166 ms                                                                | 105 ms: 1.57x faster                                                            |
| pyflate                  | 795 ms                                                                | 522 ms: 1.52x faster                                                            |
| deepcopy                 | 511 us                                                                | 339 us: 1.51x faster                                                            |
| pylint                   | 485 ms                                                                | 325 ms: 1.49x faster                                                            |
| crypto_pyaes             | 134 ms                                                                | 90.0 ms: 1.49x faster                                                           |
| comprehensions           | 33.1 us                                                               | 22.3 us: 1.48x faster                                                           |
| hexiom                   | 10.9 ms                                                               | 7.40 ms: 1.47x faster                                                           |
| tomli_loads              | 3.36 sec                                                              | 2.29 sec: 1.47x faster                                                          |
| scimark_lu               | 227 ms                                                                | 156 ms: 1.45x faster                                                            |
| regex_compile            | 177 ms                                                                | 122 ms: 1.45x faster                                                            |
| unpickle_pure_python     | 366 us                                                                | 253 us: 1.44x faster                                                            |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.43x faster                                                           |
| dulwich_log              | 73.5 ms                                                               | 53.9 ms: 1.36x faster                                                           |
| html5lib                 | 86.5 ms                                                               | 63.7 ms: 1.36x faster                                                           |
| pickle_pure_python       | 529 us                                                                | 391 us: 1.35x faster                                                            |
| xml_etree_process        | 99.5 ms                                                               | 77.2 ms: 1.29x faster                                                           |
| genshi_text              | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                                           |
| django_template          | 53.3 ms                                                               | 41.4 ms: 1.29x faster                                                           |
| scimark_fft              | 500 ms                                                                | 391 ms: 1.28x faster                                                            |
| sympy_integrate          | 26.5 ms                                                               | 20.8 ms: 1.28x faster                                                           |
| thrift                   | 1.26 ms                                                               | 1.00 ms: 1.26x faster                                                           |
| logging_simple           | 9.78 us                                                               | 7.85 us: 1.25x faster                                                           |
| coroutines               | 37.2 ms                                                               | 29.8 ms: 1.25x faster                                                           |
| deepcopy_reduce          | 4.60 us                                                               | 3.69 us: 1.24x faster                                                           |
| logging_format           | 10.6 us                                                               | 8.59 us: 1.23x faster                                                           |
| pycparser                | 1.69 sec                                                              | 1.38 sec: 1.23x faster                                                          |
| 2to3                     | 381 ms                                                                | 311 ms: 1.23x faster                                                            |
| sympy_sum                | 184 ms                                                                | 150 ms: 1.22x faster                                                            |
| json_dumps               | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                           |
| regex_v8                 | 32.2 ms                                                               | 27.0 ms: 1.19x faster                                                           |
| regex_dna                | 257 ms                                                                | 216 ms: 1.19x faster                                                            |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.19x faster                                                            |
| sympy_str                | 329 ms                                                                | 279 ms: 1.18x faster                                                            |
| nqueens                  | 117 ms                                                                | 99.8 ms: 1.18x faster                                                           |
| pathlib                  | 26.3 ms                                                               | 22.6 ms: 1.16x faster                                                           |
| docutils                 | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                          |
| fannkuch                 | 546 ms                                                                | 480 ms: 1.14x faster                                                            |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                            |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.12x faster                                                            |
| sympy_expand             | 543 ms                                                                | 493 ms: 1.10x faster                                                            |
| xml_etree_iterparse      | 156 ms                                                                | 142 ms: 1.10x faster                                                            |
| sqlite_synth             | 4.12 us                                                               | 3.77 us: 1.09x faster                                                           |
| regex_effbot             | 4.25 ms                                                               | 3.89 ms: 1.09x faster                                                           |
| genshi_xml               | 69.8 ms                                                               | 64.3 ms: 1.09x faster                                                           |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.02 ms: 1.09x faster                                                           |
| json                     | 5.88 ms                                                               | 5.63 ms: 1.04x faster                                                           |
| asyncio_websockets       | 657 ms                                                                | 671 ms: 1.02x slower                                                            |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.04x slower                                                           |
| async_generators         | 452 ms                                                                | 480 ms: 1.06x slower                                                            |
| pprint_pformat           | 2.36 sec                                                              | 2.60 sec: 1.10x slower                                                          |
| pprint_safe_repr         | 1.15 sec                                                              | 1.26 sec: 1.10x slower                                                          |
| telco                    | 8.49 ms                                                               | 9.58 ms: 1.13x slower                                                           |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.23x slower                                                            |
| python_startup_no_site   | 6.89 ms                                                               | 8.58 ms: 1.25x slower                                                           |
| python_startup           | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                                           |
| create_gc_cycles         | 2.26 ms                                                               | 3.69 ms: 1.63x slower                                                           |
| gc_traversal             | 4.15 ms                                                               | 6.98 ms: 1.68x slower                                                           |
| logging_silent           | 222 ns                                                                | 630 ns: 2.83x slower                                                            |
| Geometric mean           | (ref)                                                                 | 1.29x faster                                                                    |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250619-3.15.0a0-2850d72-JIT/bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.331x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.40x