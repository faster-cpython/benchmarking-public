# Results vs. 3.10.4

- fork: faster-cpython
- ref: virtual_iterators
- machine: linux-aarch64
- commit hash: a4b740d
- commit date: 2025-04-16
- overall geometric mean: 1.367x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 290 ms: 1.31x faster                                                            |
| docutils       | 3.53 sec                                                              | 2.89 sec: 1.22x faster                                                          |
| html5lib       | 86.5 ms                                                               | 62.2 ms: 1.39x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 884 ms: 2.58x faster                                                            |
| async_tree_memoization  | 1.13 sec                                                              | 457 ms: 2.48x faster                                                            |
| async_tree_none         | 950 ms                                                                | 387 ms: 2.45x faster                                                            |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 657 ms: 1.94x faster                                                            |
| Geometric mean          | (ref)                                                                 | 2.35x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 83.0 ms: 1.62x faster                                                           |
| nbody          | 166 ms                                                                | 119 ms: 1.40x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 121 ms: 1.46x faster                                                            |
| regex_v8       | 32.2 ms                                                               | 28.1 ms: 1.14x faster                                                           |
| regex_effbot   | 4.25 ms                                                               | 3.83 ms: 1.11x faster                                                           |
| regex_dna      | 257 ms                                                                | 241 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.19x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 374 us: 1.42x faster                                                            |
| unpickle_pure_python | 366 us                                                                | 261 us: 1.40x faster                                                            |
| tomli_loads          | 3.36 sec                                                              | 2.41 sec: 1.39x faster                                                          |
| xml_etree_process    | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                                           |
| json_dumps           | 16.7 ms                                                               | 14.1 ms: 1.19x faster                                                           |
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                            |
| xml_etree_iterparse  | 156 ms                                                                | 142 ms: 1.10x faster                                                            |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                            |
| json_loads           | 30.9 us                                                               | 34.8 us: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                           |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                           |
| django_template | 53.3 ms                                                               | 39.5 ms: 1.35x faster                                                           |
| genshi_text     | 35.2 ms                                                               | 26.3 ms: 1.34x faster                                                           |
| genshi_xml      | 69.8 ms                                                               | 59.2 ms: 1.18x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.31x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 186 us: 3.55x faster                                                            |
| async_tree_io            | 2.28 sec                                                              | 884 ms: 2.58x faster                                                            |
| async_tree_memoization   | 1.13 sec                                                              | 457 ms: 2.48x faster                                                            |
| async_tree_none          | 950 ms                                                                | 387 ms: 2.45x faster                                                            |
| deltablue                | 8.94 ms                                                               | 3.84 ms: 2.33x faster                                                           |
| mdp                      | 3.70 sec                                                              | 1.60 sec: 2.30x faster                                                          |
| go                       | 264 ms                                                                | 130 ms: 2.03x faster                                                            |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 657 ms: 1.94x faster                                                            |
| generators               | 68.1 ms                                                               | 36.6 ms: 1.86x faster                                                           |
| richards_super           | 107 ms                                                                | 58.7 ms: 1.83x faster                                                           |
| chaos                    | 121 ms                                                                | 66.3 ms: 1.83x faster                                                           |
| raytrace                 | 573 ms                                                                | 315 ms: 1.82x faster                                                            |
| richards                 | 91.7 ms                                                               | 52.0 ms: 1.76x faster                                                           |
| logging_silent           | 222 ns                                                                | 127 ns: 1.75x faster                                                            |
| deepcopy_memo            | 61.7 us                                                               | 36.6 us: 1.69x faster                                                           |
| scimark_sor              | 246 ms                                                                | 147 ms: 1.68x faster                                                            |
| scimark_monte_carlo      | 128 ms                                                                | 77.6 ms: 1.65x faster                                                           |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.63x faster                                                           |
| float                    | 135 ms                                                                | 83.0 ms: 1.62x faster                                                           |
| crypto_pyaes             | 134 ms                                                                | 83.0 ms: 1.61x faster                                                           |
| deepcopy                 | 511 us                                                                | 326 us: 1.57x faster                                                            |
| hexiom                   | 10.9 ms                                                               | 6.97 ms: 1.56x faster                                                           |
| scimark_lu               | 227 ms                                                                | 146 ms: 1.55x faster                                                            |
| pyflate                  | 795 ms                                                                | 536 ms: 1.48x faster                                                            |
| spectral_norm            | 186 ms                                                                | 127 ms: 1.46x faster                                                            |
| regex_compile            | 177 ms                                                                | 121 ms: 1.46x faster                                                            |
| logging_simple           | 9.78 us                                                               | 6.82 us: 1.43x faster                                                           |
| pickle_pure_python       | 529 us                                                                | 374 us: 1.42x faster                                                            |
| logging_format           | 10.6 us                                                               | 7.53 us: 1.41x faster                                                           |
| unpickle_pure_python     | 366 us                                                                | 261 us: 1.40x faster                                                            |
| nbody                    | 166 ms                                                                | 119 ms: 1.40x faster                                                            |
| dulwich_log              | 73.5 ms                                                               | 52.7 ms: 1.40x faster                                                           |
| tomli_loads              | 3.36 sec                                                              | 2.41 sec: 1.39x faster                                                          |
| html5lib                 | 86.5 ms                                                               | 62.2 ms: 1.39x faster                                                           |
| mako                     | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                           |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.37x faster                                                          |
| django_template          | 53.3 ms                                                               | 39.5 ms: 1.35x faster                                                           |
| genshi_text              | 35.2 ms                                                               | 26.3 ms: 1.34x faster                                                           |
| sqlalchemy_declarative   | 197 ms                                                                | 149 ms: 1.33x faster                                                            |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.6 ms: 1.32x faster                                                           |
| 2to3                     | 381 ms                                                                | 290 ms: 1.31x faster                                                            |
| pprint_pformat           | 2.36 sec                                                              | 1.82 sec: 1.30x faster                                                          |
| pprint_safe_repr         | 1.15 sec                                                              | 888 ms: 1.29x faster                                                            |
| deepcopy_reduce          | 4.60 us                                                               | 3.58 us: 1.28x faster                                                           |
| xml_etree_process        | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                                           |
| coroutines               | 37.2 ms                                                               | 29.8 ms: 1.25x faster                                                           |
| docutils                 | 3.53 sec                                                              | 2.89 sec: 1.22x faster                                                          |
| nqueens                  | 117 ms                                                                | 97.4 ms: 1.21x faster                                                           |
| scimark_fft              | 500 ms                                                                | 416 ms: 1.20x faster                                                            |
| pathlib                  | 26.3 ms                                                               | 22.2 ms: 1.19x faster                                                           |
| json_dumps               | 16.7 ms                                                               | 14.1 ms: 1.19x faster                                                           |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                           |
| genshi_xml               | 69.8 ms                                                               | 59.2 ms: 1.18x faster                                                           |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                            |
| meteor_contest           | 126 ms                                                                | 109 ms: 1.16x faster                                                            |
| fannkuch                 | 546 ms                                                                | 471 ms: 1.16x faster                                                            |
| regex_v8                 | 32.2 ms                                                               | 28.1 ms: 1.14x faster                                                           |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.79 ms: 1.12x faster                                                           |
| regex_effbot             | 4.25 ms                                                               | 3.83 ms: 1.11x faster                                                           |
| xml_etree_iterparse      | 156 ms                                                                | 142 ms: 1.10x faster                                                            |
| sqlite_synth             | 4.12 us                                                               | 3.77 us: 1.09x faster                                                           |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                            |
| regex_dna                | 257 ms                                                                | 241 ms: 1.07x faster                                                            |
| asyncio_websockets       | 657 ms                                                                | 669 ms: 1.02x slower                                                            |
| telco                    | 8.49 ms                                                               | 9.44 ms: 1.11x slower                                                           |
| json_loads               | 30.9 us                                                               | 34.8 us: 1.13x slower                                                           |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                            |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                           |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                           |
| gc_traversal             | 4.15 ms                                                               | 6.54 ms: 1.57x slower                                                           |
| create_gc_cycles         | 2.26 ms                                                               | 3.59 ms: 1.59x slower                                                           |
| bench_mp_pool            | 14.5 ms                                                               | 6.60 sec: 454.06x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.24x faster                                                                    |

Benchmark hidden because not significant (3): async_generators, json, pidigits
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250416-3.14.0a7+-a4b740d/bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.367x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.33x