# Results vs. 3.13.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-aarch64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.033x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 299 ms: 1.04x faster                                                    |
| docutils       | 2.96 sec                                                 | 2.90 sec: 1.02x faster                                                  |
| sphinx         | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                  |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 453 ms: 1.46x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 461 ms: 1.44x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 866 ms: 1.32x faster                                                    |
| async_tree_none            | 504 ms                                                   | 384 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 372 ms: 1.30x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 902 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 645 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 646 ms: 1.22x faster                                                    |
| async_generators           | 500 ms                                                   | 454 ms: 1.10x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 84.5 ms: 1.13x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.89 ms: 1.31x faster                                                   |
| regex_dna      | 263 ms                                                   | 222 ms: 1.19x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 27.5 ms: 1.18x faster                                                   |
| regex_compile  | 134 ms                                                   | 124 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                    | 1.19x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps          | 14.2 ms                                                  | 12.0 ms: 1.18x faster                                                   |
| xml_etree_parse     | 203 ms                                                   | 177 ms: 1.15x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| tomli_loads         | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                  |
| Geometric mean      | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, unpickle_pure_python, xml_etree_process, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.56 ms: 1.03x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 13.5 ms: 1.04x faster                                                   |
| genshi_xml     | 61.6 ms                                                  | 60.0 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.66 sec: 2.07x faster                                                  |
| deepcopy                   | 479 us                                                   | 326 us: 1.47x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 453 ms: 1.46x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 36.5 us: 1.45x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 461 ms: 1.44x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 866 ms: 1.32x faster                                                    |
| async_tree_none            | 504 ms                                                   | 384 ms: 1.31x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.89 ms: 1.31x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 372 ms: 1.30x faster                                                    |
| go                         | 164 ms                                                   | 127 ms: 1.29x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 902 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 645 ms: 1.24x faster                                                    |
| spectral_norm              | 143 ms                                                   | 116 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 646 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.51 us: 1.21x faster                                                   |
| regex_dna                  | 263 ms                                                   | 222 ms: 1.19x faster                                                    |
| json_dumps                 | 14.2 ms                                                  | 12.0 ms: 1.18x faster                                                   |
| regex_v8                   | 32.5 ms                                                  | 27.5 ms: 1.18x faster                                                   |
| xml_etree_parse            | 203 ms                                                   | 177 ms: 1.15x faster                                                    |
| scimark_sor                | 164 ms                                                   | 144 ms: 1.14x faster                                                    |
| float                      | 95.8 ms                                                  | 84.5 ms: 1.13x faster                                                   |
| generators                 | 40.3 ms                                                  | 35.9 ms: 1.12x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| pylint                     | 345 ms                                                   | 311 ms: 1.11x faster                                                    |
| async_generators           | 500 ms                                                   | 454 ms: 1.10x faster                                                    |
| pprint_pformat             | 1.99 sec                                                 | 1.80 sec: 1.10x faster                                                  |
| pycparser                  | 1.34 sec                                                 | 1.22 sec: 1.10x faster                                                  |
| bpe_tokeniser              | 6.02 sec                                                 | 5.51 sec: 1.09x faster                                                  |
| pprint_safe_repr           | 962 ms                                                   | 881 ms: 1.09x faster                                                    |
| scimark_fft                | 463 ms                                                   | 424 ms: 1.09x faster                                                    |
| meteor_contest             | 117 ms                                                   | 107 ms: 1.09x faster                                                    |
| pyflate                    | 582 ms                                                   | 534 ms: 1.09x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.7 ms: 1.09x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                  |
| pathlib                    | 24.3 ms                                                  | 22.4 ms: 1.08x faster                                                   |
| chaos                      | 70.7 ms                                                  | 65.3 ms: 1.08x faster                                                   |
| logging_format             | 8.10 us                                                  | 7.49 us: 1.08x faster                                                   |
| regex_compile              | 134 ms                                                   | 124 ms: 1.08x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.79 us: 1.08x faster                                                   |
| thrift                     | 1.01 ms                                                  | 940 us: 1.07x faster                                                    |
| logging_simple             | 7.25 us                                                  | 6.75 us: 1.07x faster                                                   |
| sympy_sum                  | 151 ms                                                   | 141 ms: 1.07x faster                                                    |
| sympy_integrate            | 21.4 ms                                                  | 20.1 ms: 1.07x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                  |
| hexiom                     | 7.34 ms                                                  | 6.90 ms: 1.06x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.81 sec: 1.06x faster                                                  |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| nqueens                    | 105 ms                                                   | 99.5 ms: 1.06x faster                                                   |
| 2to3                       | 313 ms                                                   | 299 ms: 1.04x faster                                                    |
| comprehensions             | 20.8 us                                                  | 20.0 us: 1.04x faster                                                   |
| mako                       | 14.0 ms                                                  | 13.5 ms: 1.04x faster                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 8.56 ms: 1.03x faster                                                   |
| genshi_xml                 | 61.6 ms                                                  | 60.0 ms: 1.03x faster                                                   |
| docutils                   | 2.96 sec                                                 | 2.90 sec: 1.02x faster                                                  |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| connected_components       | 547 ms                                                   | 559 ms: 1.02x slower                                                    |
| shortest_path              | 565 ms                                                   | 589 ms: 1.04x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.90 ms: 1.15x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 7.01 ms: 1.18x slower                                                   |
| many_optionals             | 626 us                                                   | 932 us: 1.49x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 48.1 ms: 2.36x slower                                                   |
| telco                      | 10.5 ms                                                  | 162 ms: 15.53x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 5.71 sec: 708.09x slower                                                |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (27): genshi_text, xml_etree_generate, logging_silent, richards, coverage, fannkuch, unpickle_pure_python, deltablue, html5lib, richards_super, json, sympy_expand, typing_runtime_protocols, xml_etree_process, json_loads, asyncio_websockets, crypto_pyaes, scimark_lu, django_template, pidigits, nbody, sympy_str, coroutines, bench_thread_pool, scimark_sparse_mat_mult, pickle_pure_python, raytrace
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x