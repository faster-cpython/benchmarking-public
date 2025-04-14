# Results vs. 3.10.4

- fork: faster-cpython
- ref: c_recursion_limit
- machine: linux-aarch64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.315x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 309 ms: 1.23x faster                                                            |
| docutils       | 3.53 sec                                                              | 3.03 sec: 1.17x faster                                                          |
| html5lib       | 86.5 ms                                                               | 64.1 ms: 1.35x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 936 ms: 2.44x faster                                                            |
| async_tree_none         | 950 ms                                                                | 403 ms: 2.35x faster                                                            |
| async_tree_memoization  | 1.13 sec                                                              | 504 ms: 2.25x faster                                                            |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 690 ms: 1.84x faster                                                            |
| Geometric mean          | (ref)                                                                 | 2.21x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.2 ms: 1.56x faster                                                           |
| nbody          | 166 ms                                                                | 120 ms: 1.38x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                                            |
| regex_dna      | 257 ms                                                                | 244 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                                    |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 268 us: 1.36x faster                                                            |
| pickle_pure_python   | 529 us                                                                | 393 us: 1.35x faster                                                            |
| tomli_loads          | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                          |
| xml_etree_process    | 99.5 ms                                                               | 83.0 ms: 1.20x faster                                                           |
| json_dumps           | 16.7 ms                                                               | 15.0 ms: 1.12x faster                                                           |
| xml_etree_parse      | 212 ms                                                                | 190 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.04x faster                                                            |
| json_loads           | 30.9 us                                                               | 34.6 us: 1.12x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.15x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.12 ms: 1.32x slower                                                           |
| python_startup         | 11.2 ms                                                               | 16.6 ms: 1.48x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.40x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                           |
| genshi_text     | 35.2 ms                                                               | 26.9 ms: 1.31x faster                                                           |
| django_template | 53.3 ms                                                               | 41.5 ms: 1.29x faster                                                           |
| genshi_xml      | 69.8 ms                                                               | 63.3 ms: 1.10x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 204 us: 3.24x faster                                                            |
| async_tree_io            | 2.28 sec                                                              | 936 ms: 2.44x faster                                                            |
| async_tree_none          | 950 ms                                                                | 403 ms: 2.35x faster                                                            |
| deltablue                | 8.94 ms                                                               | 3.96 ms: 2.26x faster                                                           |
| async_tree_memoization   | 1.13 sec                                                              | 504 ms: 2.25x faster                                                            |
| generators               | 68.1 ms                                                               | 36.3 ms: 1.87x faster                                                           |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 690 ms: 1.84x faster                                                            |
| go                       | 264 ms                                                                | 146 ms: 1.81x faster                                                            |
| chaos                    | 121 ms                                                                | 68.3 ms: 1.77x faster                                                           |
| richards_super           | 107 ms                                                                | 60.8 ms: 1.76x faster                                                           |
| raytrace                 | 573 ms                                                                | 328 ms: 1.75x faster                                                            |
| richards                 | 91.7 ms                                                               | 52.8 ms: 1.74x faster                                                           |
| sqlglot_parse            | 2.40 ms                                                               | 1.45 ms: 1.66x faster                                                           |
| scimark_lu               | 227 ms                                                                | 144 ms: 1.57x faster                                                            |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.56x faster                                                            |
| float                    | 135 ms                                                                | 86.2 ms: 1.56x faster                                                           |
| logging_silent           | 222 ns                                                                | 142 ns: 1.56x faster                                                            |
| spectral_norm            | 186 ms                                                                | 121 ms: 1.54x faster                                                            |
| sqlglot_transpile        | 2.84 ms                                                               | 1.84 ms: 1.54x faster                                                           |
| comprehensions           | 33.1 us                                                               | 21.6 us: 1.54x faster                                                           |
| deepcopy_memo            | 61.7 us                                                               | 40.5 us: 1.52x faster                                                           |
| crypto_pyaes             | 134 ms                                                                | 89.4 ms: 1.50x faster                                                           |
| scimark_monte_carlo      | 128 ms                                                                | 85.9 ms: 1.49x faster                                                           |
| pylint                   | 485 ms                                                                | 329 ms: 1.48x faster                                                            |
| deepcopy                 | 511 us                                                                | 346 us: 1.48x faster                                                            |
| hexiom                   | 10.9 ms                                                               | 7.62 ms: 1.43x faster                                                           |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                                            |
| pyflate                  | 795 ms                                                                | 566 ms: 1.41x faster                                                            |
| nbody                    | 166 ms                                                                | 120 ms: 1.38x faster                                                            |
| mako                     | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                           |
| unpickle_pure_python     | 366 us                                                                | 268 us: 1.36x faster                                                            |
| logging_format           | 10.6 us                                                               | 7.83 us: 1.35x faster                                                           |
| logging_simple           | 9.78 us                                                               | 7.22 us: 1.35x faster                                                           |
| html5lib                 | 86.5 ms                                                               | 64.1 ms: 1.35x faster                                                           |
| pickle_pure_python       | 529 us                                                                | 393 us: 1.35x faster                                                            |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.5 ms: 1.33x faster                                                           |
| sqlalchemy_declarative   | 197 ms                                                                | 150 ms: 1.32x faster                                                            |
| genshi_text              | 35.2 ms                                                               | 26.9 ms: 1.31x faster                                                           |
| tomli_loads              | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                          |
| pycparser                | 1.69 sec                                                              | 1.30 sec: 1.30x faster                                                          |
| django_template          | 53.3 ms                                                               | 41.5 ms: 1.29x faster                                                           |
| coroutines               | 37.2 ms                                                               | 29.0 ms: 1.28x faster                                                           |
| thrift                   | 1.26 ms                                                               | 986 us: 1.28x faster                                                            |
| deepcopy_reduce          | 4.60 us                                                               | 3.66 us: 1.26x faster                                                           |
| sympy_sum                | 184 ms                                                                | 147 ms: 1.25x faster                                                            |
| 2to3                     | 381 ms                                                                | 309 ms: 1.23x faster                                                            |
| bench_thread_pool        | 1.59 ms                                                               | 1.30 ms: 1.23x faster                                                           |
| dulwich_log              | 73.5 ms                                                               | 60.6 ms: 1.21x faster                                                           |
| sympy_integrate          | 26.5 ms                                                               | 21.9 ms: 1.21x faster                                                           |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.30 ms: 1.21x faster                                                           |
| xml_etree_process        | 99.5 ms                                                               | 83.0 ms: 1.20x faster                                                           |
| sqlglot_normalize        | 156 ms                                                                | 131 ms: 1.19x faster                                                            |
| sqlglot_optimize         | 75.4 ms                                                               | 63.8 ms: 1.18x faster                                                           |
| pprint_safe_repr         | 1.15 sec                                                              | 974 ms: 1.18x faster                                                            |
| pprint_pformat           | 2.36 sec                                                              | 2.01 sec: 1.18x faster                                                          |
| scimark_fft              | 500 ms                                                                | 426 ms: 1.17x faster                                                            |
| pathlib                  | 26.3 ms                                                               | 22.5 ms: 1.17x faster                                                           |
| sympy_str                | 329 ms                                                                | 281 ms: 1.17x faster                                                            |
| docutils                 | 3.53 sec                                                              | 3.03 sec: 1.17x faster                                                          |
| sympy_expand             | 543 ms                                                                | 478 ms: 1.13x faster                                                            |
| nqueens                  | 117 ms                                                                | 104 ms: 1.12x faster                                                            |
| json_dumps               | 16.7 ms                                                               | 15.0 ms: 1.12x faster                                                           |
| xml_etree_parse          | 212 ms                                                                | 190 ms: 1.11x faster                                                            |
| genshi_xml               | 69.8 ms                                                               | 63.3 ms: 1.10x faster                                                           |
| meteor_contest           | 126 ms                                                                | 115 ms: 1.10x faster                                                            |
| fannkuch                 | 546 ms                                                                | 496 ms: 1.10x faster                                                            |
| mdp                      | 3.70 sec                                                              | 3.47 sec: 1.07x faster                                                          |
| regex_dna                | 257 ms                                                                | 244 ms: 1.05x faster                                                            |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.04x faster                                                            |
| asyncio_websockets       | 657 ms                                                                | 675 ms: 1.03x slower                                                            |
| json_loads               | 30.9 us                                                               | 34.6 us: 1.12x slower                                                           |
| telco                    | 8.49 ms                                                               | 10.1 ms: 1.19x slower                                                           |
| coverage                 | 83.6 ms                                                               | 104 ms: 1.24x slower                                                            |
| python_startup_no_site   | 6.89 ms                                                               | 9.12 ms: 1.32x slower                                                           |
| python_startup           | 11.2 ms                                                               | 16.6 ms: 1.48x slower                                                           |
| create_gc_cycles         | 2.26 ms                                                               | 3.57 ms: 1.58x slower                                                           |
| gc_traversal             | 4.15 ms                                                               | 6.89 ms: 1.66x slower                                                           |
| bench_mp_pool            | 14.5 ms                                                               | 7.19 sec: 494.60x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                                    |

Benchmark hidden because not significant (7): regex_effbot, xml_etree_generate, regex_v8, sqlite_synth, async_generators, pidigits, json
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250217-3.14.0a5+-21366c3/bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.315x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.30x