# Results vs. 3.10.4

- fork: mdboom
- ref: aa_test_2025
- machine: linux-aarch64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.319x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 309 ms: 1.23x faster                                             |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                           |
| html5lib       | 86.5 ms                                                               | 63.0 ms: 1.37x faster                                            |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 887 ms: 2.58x faster                                             |
| async_tree_none         | 950 ms                                                                | 379 ms: 2.50x faster                                             |
| async_tree_memoization  | 1.13 sec                                                              | 483 ms: 2.35x faster                                             |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 672 ms: 1.89x faster                                             |
| Geometric mean          | (ref)                                                                 | 2.31x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.7 ms: 1.57x faster                                            |
| nbody          | 166 ms                                                                | 122 ms: 1.36x faster                                             |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                             |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                     |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.59 sec: 1.30x faster                                           |
| pickle_pure_python   | 529 us                                                                | 410 us: 1.29x faster                                             |
| unpickle_pure_python | 366 us                                                                | 285 us: 1.28x faster                                             |
| xml_etree_process    | 99.5 ms                                                               | 85.8 ms: 1.16x faster                                            |
| xml_etree_parse      | 212 ms                                                                | 183 ms: 1.16x faster                                             |
| json_dumps           | 16.7 ms                                                               | 14.6 ms: 1.14x faster                                            |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                             |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.08x faster                                             |
| json_loads           | 30.9 us                                                               | 33.0 us: 1.07x slower                                            |
| Geometric mean       | (ref)                                                                 | 1.15x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.06 ms: 1.32x slower                                            |
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.38x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 40.1 ms: 1.33x faster                                            |
| mako            | 18.9 ms                                                               | 14.3 ms: 1.32x faster                                            |
| genshi_text     | 35.2 ms                                                               | 28.9 ms: 1.22x faster                                            |
| genshi_xml      | 69.8 ms                                                               | 62.4 ms: 1.12x faster                                            |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.20x faster                                             |
| async_tree_io            | 2.28 sec                                                              | 887 ms: 2.58x faster                                             |
| async_tree_none          | 950 ms                                                                | 379 ms: 2.50x faster                                             |
| async_tree_memoization   | 1.13 sec                                                              | 483 ms: 2.35x faster                                             |
| deltablue                | 8.94 ms                                                               | 3.87 ms: 2.31x faster                                            |
| generators               | 68.1 ms                                                               | 35.9 ms: 1.90x faster                                            |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 672 ms: 1.89x faster                                             |
| go                       | 264 ms                                                                | 144 ms: 1.84x faster                                             |
| richards_super           | 107 ms                                                                | 58.5 ms: 1.83x faster                                            |
| raytrace                 | 573 ms                                                                | 316 ms: 1.81x faster                                             |
| richards                 | 91.7 ms                                                               | 51.6 ms: 1.78x faster                                            |
| chaos                    | 121 ms                                                                | 69.4 ms: 1.75x faster                                            |
| sqlglot_parse            | 2.40 ms                                                               | 1.47 ms: 1.64x faster                                            |
| logging_silent           | 222 ns                                                                | 136 ns: 1.64x faster                                             |
| scimark_sor              | 246 ms                                                                | 152 ms: 1.62x faster                                             |
| scimark_lu               | 227 ms                                                                | 141 ms: 1.61x faster                                             |
| sqlglot_transpile        | 2.84 ms                                                               | 1.79 ms: 1.58x faster                                            |
| crypto_pyaes             | 134 ms                                                                | 85.0 ms: 1.58x faster                                            |
| comprehensions           | 33.1 us                                                               | 21.0 us: 1.57x faster                                            |
| float                    | 135 ms                                                                | 85.7 ms: 1.57x faster                                            |
| spectral_norm            | 186 ms                                                                | 125 ms: 1.50x faster                                             |
| deepcopy_memo            | 61.7 us                                                               | 41.3 us: 1.49x faster                                            |
| pylint                   | 485 ms                                                                | 326 ms: 1.49x faster                                             |
| scimark_monte_carlo      | 128 ms                                                                | 86.7 ms: 1.47x faster                                            |
| hexiom                   | 10.9 ms                                                               | 7.44 ms: 1.47x faster                                            |
| deepcopy                 | 511 us                                                                | 356 us: 1.43x faster                                             |
| pyflate                  | 795 ms                                                                | 566 ms: 1.40x faster                                             |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                             |
| html5lib                 | 86.5 ms                                                               | 63.0 ms: 1.37x faster                                            |
| nbody                    | 166 ms                                                                | 122 ms: 1.36x faster                                             |
| sqlalchemy_declarative   | 197 ms                                                                | 147 ms: 1.34x faster                                             |
| django_template          | 53.3 ms                                                               | 40.1 ms: 1.33x faster                                            |
| mako                     | 18.9 ms                                                               | 14.3 ms: 1.32x faster                                            |
| logging_simple           | 9.78 us                                                               | 7.44 us: 1.31x faster                                            |
| pycparser                | 1.69 sec                                                              | 1.29 sec: 1.31x faster                                           |
| logging_format           | 10.6 us                                                               | 8.12 us: 1.31x faster                                            |
| tomli_loads              | 3.36 sec                                                              | 2.59 sec: 1.30x faster                                           |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.29x faster                                             |
| pickle_pure_python       | 529 us                                                                | 410 us: 1.29x faster                                             |
| thrift                   | 1.26 ms                                                               | 978 us: 1.29x faster                                             |
| unpickle_pure_python     | 366 us                                                                | 285 us: 1.28x faster                                             |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.1 ms: 1.28x faster                                            |
| deepcopy_reduce          | 4.60 us                                                               | 3.66 us: 1.26x faster                                            |
| coroutines               | 37.2 ms                                                               | 30.0 ms: 1.24x faster                                            |
| 2to3                     | 381 ms                                                                | 309 ms: 1.23x faster                                             |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                             |
| genshi_text              | 35.2 ms                                                               | 28.9 ms: 1.22x faster                                            |
| sympy_integrate          | 26.5 ms                                                               | 21.9 ms: 1.21x faster                                            |
| dulwich_log              | 73.5 ms                                                               | 61.3 ms: 1.20x faster                                            |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.19x faster                                            |
| scimark_fft              | 500 ms                                                                | 421 ms: 1.19x faster                                             |
| sympy_str                | 329 ms                                                                | 279 ms: 1.18x faster                                             |
| pprint_safe_repr         | 1.15 sec                                                              | 976 ms: 1.18x faster                                             |
| pprint_pformat           | 2.36 sec                                                              | 2.01 sec: 1.18x faster                                           |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                           |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.53 ms: 1.17x faster                                            |
| pathlib                  | 26.3 ms                                                               | 22.6 ms: 1.16x faster                                            |
| sqlglot_optimize         | 75.4 ms                                                               | 64.9 ms: 1.16x faster                                            |
| xml_etree_process        | 99.5 ms                                                               | 85.8 ms: 1.16x faster                                            |
| xml_etree_parse          | 212 ms                                                                | 183 ms: 1.16x faster                                             |
| json_dumps               | 16.7 ms                                                               | 14.6 ms: 1.14x faster                                            |
| sympy_expand             | 543 ms                                                                | 478 ms: 1.14x faster                                             |
| nqueens                  | 117 ms                                                                | 105 ms: 1.12x faster                                             |
| genshi_xml               | 69.8 ms                                                               | 62.4 ms: 1.12x faster                                            |
| fannkuch                 | 546 ms                                                                | 492 ms: 1.11x faster                                             |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                             |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.08x faster                                             |
| mdp                      | 3.70 sec                                                              | 3.44 sec: 1.08x faster                                           |
| meteor_contest           | 126 ms                                                                | 117 ms: 1.07x faster                                             |
| asyncio_websockets       | 657 ms                                                                | 669 ms: 1.02x slower                                             |
| json_loads               | 30.9 us                                                               | 33.0 us: 1.07x slower                                            |
| telco                    | 8.49 ms                                                               | 9.64 ms: 1.14x slower                                            |
| coverage                 | 83.6 ms                                                               | 99.6 ms: 1.19x slower                                            |
| python_startup_no_site   | 6.89 ms                                                               | 9.06 ms: 1.32x slower                                            |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                            |
| create_gc_cycles         | 2.26 ms                                                               | 3.64 ms: 1.61x slower                                            |
| gc_traversal             | 4.15 ms                                                               | 6.74 ms: 1.62x slower                                            |
| bench_mp_pool            | 14.5 ms                                                               | 4.70 sec: 323.60x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                     |

Benchmark hidden because not significant (7): regex_effbot, regex_dna, async_generators, sqlite_synth, json, regex_v8, pidigits
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250121-3.14.0a4+-4844db8/bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.319x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.30x