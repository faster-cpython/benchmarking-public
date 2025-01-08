# Results vs. 3.10.4

- fork: brandtbucher
- ref: nojit
- machine: linux-aarch64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.311x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 308 ms: 1.24x faster                                            |
| docutils       | 3.53 sec                                                              | 3.03 sec: 1.17x faster                                          |
| html5lib       | 86.5 ms                                                               | 64.9 ms: 1.33x faster                                           |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 890 ms: 2.57x faster                                            |
| async_tree_none         | 950 ms                                                                | 375 ms: 2.53x faster                                            |
| async_tree_memoization  | 1.13 sec                                                              | 490 ms: 2.31x faster                                            |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 672 ms: 1.89x faster                                            |
| Geometric mean          | (ref)                                                                 | 2.31x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.7 ms: 1.49x faster                                           |
| nbody          | 166 ms                                                                | 125 ms: 1.33x faster                                            |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.37x faster                                            |
| regex_dna      | 257 ms                                                                | 245 ms: 1.05x faster                                            |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                    |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 268 us: 1.37x faster                                            |
| pickle_pure_python   | 529 us                                                                | 400 us: 1.32x faster                                            |
| tomli_loads          | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                          |
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.18x faster                                            |
| xml_etree_process    | 99.5 ms                                                               | 85.6 ms: 1.16x faster                                           |
| json_dumps           | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                           |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                            |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.07x faster                                            |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                    |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.01 ms: 1.31x slower                                           |
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.38x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.3 ms: 1.33x faster                                           |
| django_template | 53.3 ms                                                               | 42.3 ms: 1.26x faster                                           |
| genshi_text     | 35.2 ms                                                               | 28.1 ms: 1.25x faster                                           |
| genshi_xml      | 69.8 ms                                                               | 62.8 ms: 1.11x faster                                           |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 203 us: 3.26x faster                                            |
| async_tree_io            | 2.28 sec                                                              | 890 ms: 2.57x faster                                            |
| async_tree_none          | 950 ms                                                                | 375 ms: 2.53x faster                                            |
| async_tree_memoization   | 1.13 sec                                                              | 490 ms: 2.31x faster                                            |
| deltablue                | 8.94 ms                                                               | 3.96 ms: 2.26x faster                                           |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 672 ms: 1.89x faster                                            |
| richards_super           | 107 ms                                                                | 58.1 ms: 1.85x faster                                           |
| generators               | 68.1 ms                                                               | 36.9 ms: 1.84x faster                                           |
| go                       | 264 ms                                                                | 144 ms: 1.83x faster                                            |
| richards                 | 91.7 ms                                                               | 51.6 ms: 1.78x faster                                           |
| raytrace                 | 573 ms                                                                | 329 ms: 1.74x faster                                            |
| chaos                    | 121 ms                                                                | 71.4 ms: 1.70x faster                                           |
| sqlglot_parse            | 2.40 ms                                                               | 1.46 ms: 1.65x faster                                           |
| scimark_lu               | 227 ms                                                                | 138 ms: 1.65x faster                                            |
| logging_silent           | 222 ns                                                                | 140 ns: 1.59x faster                                            |
| sqlglot_transpile        | 2.84 ms                                                               | 1.80 ms: 1.58x faster                                           |
| pylint                   | 485 ms                                                                | 307 ms: 1.58x faster                                            |
| comprehensions           | 33.1 us                                                               | 21.2 us: 1.56x faster                                           |
| crypto_pyaes             | 134 ms                                                                | 86.3 ms: 1.55x faster                                           |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.55x faster                                            |
| scimark_monte_carlo      | 128 ms                                                                | 85.3 ms: 1.50x faster                                           |
| deepcopy_memo            | 61.7 us                                                               | 41.2 us: 1.50x faster                                           |
| deepcopy                 | 511 us                                                                | 342 us: 1.49x faster                                            |
| float                    | 135 ms                                                                | 90.7 ms: 1.49x faster                                           |
| hexiom                   | 10.9 ms                                                               | 7.37 ms: 1.48x faster                                           |
| spectral_norm            | 186 ms                                                                | 130 ms: 1.44x faster                                            |
| pyflate                  | 795 ms                                                                | 569 ms: 1.40x faster                                            |
| regex_compile            | 177 ms                                                                | 129 ms: 1.37x faster                                            |
| unpickle_pure_python     | 366 us                                                                | 268 us: 1.37x faster                                            |
| logging_simple           | 9.78 us                                                               | 7.19 us: 1.36x faster                                           |
| html5lib                 | 86.5 ms                                                               | 64.9 ms: 1.33x faster                                           |
| mako                     | 18.9 ms                                                               | 14.3 ms: 1.33x faster                                           |
| nbody                    | 166 ms                                                                | 125 ms: 1.33x faster                                            |
| pickle_pure_python       | 529 us                                                                | 400 us: 1.32x faster                                            |
| sqlalchemy_declarative   | 197 ms                                                                | 151 ms: 1.31x faster                                            |
| pycparser                | 1.69 sec                                                              | 1.29 sec: 1.31x faster                                          |
| thrift                   | 1.26 ms                                                               | 972 us: 1.30x faster                                            |
| logging_format           | 10.6 us                                                               | 8.22 us: 1.29x faster                                           |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.9 ms: 1.29x faster                                           |
| tomli_loads              | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                          |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.29x faster                                            |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                           |
| django_template          | 53.3 ms                                                               | 42.3 ms: 1.26x faster                                           |
| deepcopy_reduce          | 4.60 us                                                               | 3.67 us: 1.25x faster                                           |
| genshi_text              | 35.2 ms                                                               | 28.1 ms: 1.25x faster                                           |
| 2to3                     | 381 ms                                                                | 308 ms: 1.24x faster                                            |
| bench_thread_pool        | 1.59 ms                                                               | 1.30 ms: 1.22x faster                                           |
| pathlib                  | 26.3 ms                                                               | 21.7 ms: 1.21x faster                                           |
| sqlglot_optimize         | 75.4 ms                                                               | 62.4 ms: 1.21x faster                                           |
| sympy_str                | 329 ms                                                                | 272 ms: 1.21x faster                                            |
| sympy_integrate          | 26.5 ms                                                               | 22.0 ms: 1.21x faster                                           |
| pprint_safe_repr         | 1.15 sec                                                              | 958 ms: 1.20x faster                                            |
| pprint_pformat           | 2.36 sec                                                              | 1.99 sec: 1.19x faster                                          |
| sqlglot_normalize        | 156 ms                                                                | 131 ms: 1.19x faster                                            |
| dulwich_log              | 73.5 ms                                                               | 62.4 ms: 1.18x faster                                           |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.18x faster                                            |
| docutils                 | 3.53 sec                                                              | 3.03 sec: 1.17x faster                                          |
| xml_etree_process        | 99.5 ms                                                               | 85.6 ms: 1.16x faster                                           |
| json_dumps               | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                           |
| scimark_fft              | 500 ms                                                                | 435 ms: 1.15x faster                                            |
| sympy_expand             | 543 ms                                                                | 474 ms: 1.14x faster                                            |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.67 ms: 1.14x faster                                           |
| fannkuch                 | 546 ms                                                                | 478 ms: 1.14x faster                                            |
| nqueens                  | 117 ms                                                                | 105 ms: 1.12x faster                                            |
| genshi_xml               | 69.8 ms                                                               | 62.8 ms: 1.11x faster                                           |
| meteor_contest           | 126 ms                                                                | 115 ms: 1.09x faster                                            |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                            |
| mdp                      | 3.70 sec                                                              | 3.41 sec: 1.08x faster                                          |
| json                     | 5.88 ms                                                               | 5.49 ms: 1.07x faster                                           |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.07x faster                                            |
| regex_dna                | 257 ms                                                                | 245 ms: 1.05x faster                                            |
| asyncio_websockets       | 657 ms                                                                | 678 ms: 1.03x slower                                            |
| async_generators         | 452 ms                                                                | 493 ms: 1.09x slower                                            |
| mypy2                    | 936 ms                                                                | 1.05 sec: 1.12x slower                                          |
| telco                    | 8.49 ms                                                               | 9.97 ms: 1.17x slower                                           |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                            |
| python_startup_no_site   | 6.89 ms                                                               | 9.01 ms: 1.31x slower                                           |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                           |
| create_gc_cycles         | 2.26 ms                                                               | 3.71 ms: 1.64x slower                                           |
| gc_traversal             | 4.15 ms                                                               | 6.91 ms: 1.66x slower                                           |
| bench_mp_pool            | 14.5 ms                                                               | 3.47 sec: 238.74x slower                                        |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                    |

Benchmark hidden because not significant (5): regex_effbot, regex_v8, sqlite_synth, pidigits, json_loads
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250107-3.14.0a3+-f098037/bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.311x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.31x