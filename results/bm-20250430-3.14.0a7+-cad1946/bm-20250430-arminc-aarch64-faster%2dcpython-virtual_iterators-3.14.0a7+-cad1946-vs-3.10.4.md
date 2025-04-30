# Results vs. 3.10.4

- fork: faster-cpython
- ref: virtual_iterators
- machine: linux-aarch64
- commit hash: cad1946
- commit date: 2025-04-30
- overall geometric mean: 1.348x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 294 ms: 1.29x faster                                                            |
| docutils       | 3.53 sec                                                              | 2.91 sec: 1.21x faster                                                          |
| html5lib       | 86.5 ms                                                               | 63.2 ms: 1.37x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 882 ms: 2.59x faster                                                            |
| async_tree_none         | 950 ms                                                                | 381 ms: 2.49x faster                                                            |
| async_tree_memoization  | 1.13 sec                                                              | 459 ms: 2.47x faster                                                            |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 663 ms: 1.92x faster                                                            |
| Geometric mean          | (ref)                                                                 | 2.35x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.9 ms: 1.57x faster                                                           |
| nbody          | 166 ms                                                                | 124 ms: 1.34x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 120 ms: 1.47x faster                                                            |
| regex_v8       | 32.2 ms                                                               | 28.3 ms: 1.14x faster                                                           |
| regex_effbot   | 4.25 ms                                                               | 3.81 ms: 1.11x faster                                                           |
| regex_dna      | 257 ms                                                                | 241 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.19x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 382 us: 1.38x faster                                                            |
| tomli_loads          | 3.36 sec                                                              | 2.43 sec: 1.38x faster                                                          |
| unpickle_pure_python | 366 us                                                                | 267 us: 1.37x faster                                                            |
| xml_etree_process    | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                                           |
| json_dumps           | 16.7 ms                                                               | 14.2 ms: 1.17x faster                                                           |
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.16x faster                                                            |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                            |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.09x faster                                                            |
| json_loads           | 30.9 us                                                               | 35.4 us: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.19x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.68 ms: 1.26x slower                                                           |
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.35x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.3 ms: 1.32x faster                                                           |
| django_template | 53.3 ms                                                               | 40.4 ms: 1.32x faster                                                           |
| genshi_text     | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                           |
| genshi_xml      | 69.8 ms                                                               | 61.4 ms: 1.14x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 197 us: 3.35x faster                                                            |
| async_tree_io            | 2.28 sec                                                              | 882 ms: 2.59x faster                                                            |
| async_tree_none          | 950 ms                                                                | 381 ms: 2.49x faster                                                            |
| async_tree_memoization   | 1.13 sec                                                              | 459 ms: 2.47x faster                                                            |
| deltablue                | 8.94 ms                                                               | 3.92 ms: 2.28x faster                                                           |
| mdp                      | 3.70 sec                                                              | 1.64 sec: 2.26x faster                                                          |
| go                       | 264 ms                                                                | 128 ms: 2.06x faster                                                            |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 663 ms: 1.92x faster                                                            |
| generators               | 68.1 ms                                                               | 36.6 ms: 1.86x faster                                                           |
| richards_super           | 107 ms                                                                | 58.5 ms: 1.83x faster                                                           |
| raytrace                 | 573 ms                                                                | 326 ms: 1.76x faster                                                            |
| richards                 | 91.7 ms                                                               | 52.2 ms: 1.76x faster                                                           |
| chaos                    | 121 ms                                                                | 69.1 ms: 1.75x faster                                                           |
| logging_silent           | 222 ns                                                                | 131 ns: 1.70x faster                                                            |
| scimark_sor              | 246 ms                                                                | 148 ms: 1.66x faster                                                            |
| comprehensions           | 33.1 us                                                               | 20.2 us: 1.64x faster                                                           |
| deepcopy_memo            | 61.7 us                                                               | 37.6 us: 1.64x faster                                                           |
| scimark_monte_carlo      | 128 ms                                                                | 80.0 ms: 1.60x faster                                                           |
| hexiom                   | 10.9 ms                                                               | 6.87 ms: 1.59x faster                                                           |
| crypto_pyaes             | 134 ms                                                                | 85.0 ms: 1.58x faster                                                           |
| deepcopy                 | 511 us                                                                | 325 us: 1.57x faster                                                            |
| float                    | 135 ms                                                                | 85.9 ms: 1.57x faster                                                           |
| scimark_lu               | 227 ms                                                                | 146 ms: 1.56x faster                                                            |
| regex_compile            | 177 ms                                                                | 120 ms: 1.47x faster                                                            |
| pyflate                  | 795 ms                                                                | 549 ms: 1.45x faster                                                            |
| spectral_norm            | 186 ms                                                                | 130 ms: 1.43x faster                                                            |
| logging_simple           | 9.78 us                                                               | 6.92 us: 1.41x faster                                                           |
| logging_format           | 10.6 us                                                               | 7.62 us: 1.39x faster                                                           |
| pickle_pure_python       | 529 us                                                                | 382 us: 1.38x faster                                                            |
| tomli_loads              | 3.36 sec                                                              | 2.43 sec: 1.38x faster                                                          |
| unpickle_pure_python     | 366 us                                                                | 267 us: 1.37x faster                                                            |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.37x faster                                                          |
| html5lib                 | 86.5 ms                                                               | 63.2 ms: 1.37x faster                                                           |
| nbody                    | 166 ms                                                                | 124 ms: 1.34x faster                                                            |
| dulwich_log              | 73.5 ms                                                               | 54.9 ms: 1.34x faster                                                           |
| mako                     | 18.9 ms                                                               | 14.3 ms: 1.32x faster                                                           |
| django_template          | 53.3 ms                                                               | 40.4 ms: 1.32x faster                                                           |
| sqlalchemy_declarative   | 197 ms                                                                | 152 ms: 1.30x faster                                                            |
| deepcopy_reduce          | 4.60 us                                                               | 3.54 us: 1.30x faster                                                           |
| 2to3                     | 381 ms                                                                | 294 ms: 1.29x faster                                                            |
| pprint_pformat           | 2.36 sec                                                              | 1.84 sec: 1.28x faster                                                          |
| pprint_safe_repr         | 1.15 sec                                                              | 899 ms: 1.28x faster                                                            |
| genshi_text              | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                           |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.3 ms: 1.26x faster                                                           |
| xml_etree_process        | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                                           |
| coroutines               | 37.2 ms                                                               | 30.2 ms: 1.23x faster                                                           |
| docutils                 | 3.53 sec                                                              | 2.91 sec: 1.21x faster                                                          |
| pathlib                  | 26.3 ms                                                               | 21.8 ms: 1.20x faster                                                           |
| nqueens                  | 117 ms                                                                | 98.9 ms: 1.19x faster                                                           |
| json_dumps               | 16.7 ms                                                               | 14.2 ms: 1.17x faster                                                           |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.16x faster                                                            |
| bench_thread_pool        | 1.59 ms                                                               | 1.39 ms: 1.14x faster                                                           |
| regex_v8                 | 32.2 ms                                                               | 28.3 ms: 1.14x faster                                                           |
| genshi_xml               | 69.8 ms                                                               | 61.4 ms: 1.14x faster                                                           |
| scimark_fft              | 500 ms                                                                | 444 ms: 1.13x faster                                                            |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.12x faster                                                            |
| fannkuch                 | 546 ms                                                                | 488 ms: 1.12x faster                                                            |
| regex_effbot             | 4.25 ms                                                               | 3.81 ms: 1.11x faster                                                           |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                            |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.99 ms: 1.09x faster                                                           |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.09x faster                                                            |
| regex_dna                | 257 ms                                                                | 241 ms: 1.07x faster                                                            |
| sqlite_synth             | 4.12 us                                                               | 3.94 us: 1.04x faster                                                           |
| json                     | 5.88 ms                                                               | 6.00 ms: 1.02x slower                                                           |
| asyncio_websockets       | 657 ms                                                                | 671 ms: 1.02x slower                                                            |
| json_loads               | 30.9 us                                                               | 35.4 us: 1.14x slower                                                           |
| telco                    | 8.49 ms                                                               | 9.73 ms: 1.15x slower                                                           |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.23x slower                                                            |
| python_startup_no_site   | 6.89 ms                                                               | 8.68 ms: 1.26x slower                                                           |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                           |
| gc_traversal             | 4.15 ms                                                               | 6.53 ms: 1.57x slower                                                           |
| create_gc_cycles         | 2.26 ms                                                               | 3.59 ms: 1.59x slower                                                           |
| bench_mp_pool            | 14.5 ms                                                               | 1.87 sec: 128.34x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.25x faster                                                                    |

Benchmark hidden because not significant (2): async_generators, pidigits
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250430-3.14.0a7+-cad1946/bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.348x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.33x