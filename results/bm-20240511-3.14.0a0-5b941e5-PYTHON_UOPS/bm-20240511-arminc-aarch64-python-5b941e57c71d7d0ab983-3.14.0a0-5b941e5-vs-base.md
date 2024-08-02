# Results vs. base

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: linux-aarch64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.13x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-PYTHON_UOPS/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                                                            | 354 ms: 1.16x slower                                                                                                          |
| chameleon      | 8.99 ms                                                                                                           | 9.96 ms: 1.11x slower                                                                                                         |
| docutils       | 3.09 sec                                                                                                          | 3.54 sec: 1.14x slower                                                                                                        |
| html5lib       | 67.1 ms                                                                                                           | 74.8 ms: 1.11x slower                                                                                                         |
| Geometric mean | (ref)                                                                                                             | 1.11x slower                                                                                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-PYTHON_UOPS/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|-------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg        | 1.23 sec                                                                                                          | 1.26 sec: 1.03x slower                                                                                                        |
| async_tree_none_tg      | 465 ms                                                                                                            | 478 ms: 1.03x slower                                                                                                          |
| async_tree_cpu_io_mixed | 792 ms                                                                                                            | 816 ms: 1.03x slower                                                                                                          |
| async_tree_memoization  | 644 ms                                                                                                            | 670 ms: 1.04x slower                                                                                                          |
| async_tree_none         | 487 ms                                                                                                            | 517 ms: 1.06x slower                                                                                                          |
| Geometric mean          | (ref)                                                                                                             | 1.03x slower                                                                                                                  |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-PYTHON_UOPS/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 112 ms                                                                                                            | 138 ms: 1.23x slower                                                                                                          |
| float          | 90.2 ms                                                                                                           | 114 ms: 1.26x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                             | 1.16x slower                                                                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-PYTHON_UOPS/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 30.7 ms                                                                                                           | 31.1 ms: 1.01x slower                                                                                                         |
| regex_dna      | 254 ms                                                                                                            | 261 ms: 1.03x slower                                                                                                          |
| regex_compile  | 130 ms                                                                                                            | 167 ms: 1.28x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                             | 1.08x slower                                                                                                                  |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-PYTHON_UOPS/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list        | 6.59 us                                                                                                           | 6.51 us: 1.01x faster                                                                                                         |
| json_dumps           | 13.3 ms                                                                                                           | 14.0 ms: 1.05x slower                                                                                                         |
| xml_etree_iterparse  | 149 ms                                                                                                            | 162 ms: 1.09x slower                                                                                                          |
| xml_etree_process    | 79.3 ms                                                                                                           | 88.5 ms: 1.12x slower                                                                                                         |
| xml_etree_generate   | 112 ms                                                                                                            | 125 ms: 1.12x slower                                                                                                          |
| tomli_loads          | 2.58 sec                                                                                                          | 3.08 sec: 1.19x slower                                                                                                        |
| pickle_pure_python   | 360 us                                                                                                            | 449 us: 1.25x slower                                                                                                          |
| unpickle_pure_python | 252 us                                                                                                            | 349 us: 1.38x slower                                                                                                          |
| Geometric mean       | (ref)                                                                                                             | 1.08x slower                                                                                                                  |

Benchmark hidden because not significant (6): unpickle, pickle_list, json_loads, pickle, pickle_dict, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-PYTHON_UOPS/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| django_template | 41.9 ms                                                                                                           | 49.9 ms: 1.19x slower                                                                                                         |
| mako            | 13.2 ms                                                                                                           | 16.5 ms: 1.25x slower                                                                                                         |
| genshi_xml      | 61.0 ms                                                                                                           | 77.7 ms: 1.27x slower                                                                                                         |
| genshi_text     | 28.0 ms                                                                                                           | 36.6 ms: 1.31x slower                                                                                                         |
| Geometric mean  | (ref)                                                                                                             | 1.25x slower                                                                                                                  |

All benchmarks:
===============

| Benchmark                | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-PYTHON_UOPS/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|--------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list            | 6.59 us                                                                                                           | 6.51 us: 1.01x faster                                                                                                         |
| telco                    | 164 ms                                                                                                            | 166 ms: 1.01x slower                                                                                                          |
| regex_v8                 | 30.7 ms                                                                                                           | 31.1 ms: 1.01x slower                                                                                                         |
| asyncio_tcp_ssl          | 2.21 sec                                                                                                          | 2.24 sec: 1.01x slower                                                                                                        |
| create_gc_cycles         | 2.40 ms                                                                                                           | 2.43 ms: 1.01x slower                                                                                                         |
| sqlite_synth             | 3.90 us                                                                                                           | 3.96 us: 1.02x slower                                                                                                         |
| coverage                 | 97.5 ms                                                                                                           | 99.1 ms: 1.02x slower                                                                                                         |
| logging_simple           | 7.15 us                                                                                                           | 7.28 us: 1.02x slower                                                                                                         |
| json                     | 5.67 ms                                                                                                           | 5.79 ms: 1.02x slower                                                                                                         |
| regex_dna                | 254 ms                                                                                                            | 261 ms: 1.03x slower                                                                                                          |
| async_tree_io_tg         | 1.23 sec                                                                                                          | 1.26 sec: 1.03x slower                                                                                                        |
| async_tree_none_tg       | 465 ms                                                                                                            | 478 ms: 1.03x slower                                                                                                          |
| async_tree_cpu_io_mixed  | 792 ms                                                                                                            | 816 ms: 1.03x slower                                                                                                          |
| thrift                   | 952 us                                                                                                            | 985 us: 1.03x slower                                                                                                          |
| async_tree_memoization   | 644 ms                                                                                                            | 670 ms: 1.04x slower                                                                                                          |
| logging_format           | 7.76 us                                                                                                           | 8.09 us: 1.04x slower                                                                                                         |
| coroutines               | 29.2 ms                                                                                                           | 30.4 ms: 1.04x slower                                                                                                         |
| pathlib                  | 23.1 ms                                                                                                           | 24.3 ms: 1.05x slower                                                                                                         |
| json_dumps               | 13.3 ms                                                                                                           | 14.0 ms: 1.05x slower                                                                                                         |
| dulwich_log              | 61.4 ms                                                                                                           | 64.9 ms: 1.06x slower                                                                                                         |
| bench_thread_pool        | 1.28 ms                                                                                                           | 1.36 ms: 1.06x slower                                                                                                         |
| async_tree_none          | 487 ms                                                                                                            | 517 ms: 1.06x slower                                                                                                          |
| async_generators         | 489 ms                                                                                                            | 523 ms: 1.07x slower                                                                                                          |
| mdp                      | 3.35 sec                                                                                                          | 3.60 sec: 1.08x slower                                                                                                        |
| xml_etree_iterparse      | 149 ms                                                                                                            | 162 ms: 1.09x slower                                                                                                          |
| chameleon                | 8.99 ms                                                                                                           | 9.96 ms: 1.11x slower                                                                                                         |
| html5lib                 | 67.1 ms                                                                                                           | 74.8 ms: 1.11x slower                                                                                                         |
| xml_etree_process        | 79.3 ms                                                                                                           | 88.5 ms: 1.12x slower                                                                                                         |
| xml_etree_generate       | 112 ms                                                                                                            | 125 ms: 1.12x slower                                                                                                          |
| pycparser                | 1.22 sec                                                                                                          | 1.37 sec: 1.13x slower                                                                                                        |
| sympy_expand             | 459 ms                                                                                                            | 522 ms: 1.14x slower                                                                                                          |
| pylint                   | 343 ms                                                                                                            | 392 ms: 1.14x slower                                                                                                          |
| docutils                 | 3.09 sec                                                                                                          | 3.54 sec: 1.14x slower                                                                                                        |
| sqlglot_normalize        | 129 ms                                                                                                            | 149 ms: 1.15x slower                                                                                                          |
| raytrace                 | 296 ms                                                                                                            | 342 ms: 1.15x slower                                                                                                          |
| sympy_sum                | 149 ms                                                                                                            | 172 ms: 1.16x slower                                                                                                          |
| sqlglot_optimize         | 62.6 ms                                                                                                           | 72.4 ms: 1.16x slower                                                                                                         |
| typing_runtime_protocols | 196 us                                                                                                            | 227 us: 1.16x slower                                                                                                          |
| 2to3                     | 306 ms                                                                                                            | 354 ms: 1.16x slower                                                                                                          |
| deepcopy_reduce          | 4.15 us                                                                                                           | 4.84 us: 1.17x slower                                                                                                         |
| meteor_contest           | 113 ms                                                                                                            | 132 ms: 1.17x slower                                                                                                          |
| sympy_str                | 269 ms                                                                                                            | 317 ms: 1.18x slower                                                                                                          |
| django_template          | 41.9 ms                                                                                                           | 49.9 ms: 1.19x slower                                                                                                         |
| tomli_loads              | 2.58 sec                                                                                                          | 3.08 sec: 1.19x slower                                                                                                        |
| deepcopy                 | 454 us                                                                                                            | 541 us: 1.19x slower                                                                                                          |
| richards_super           | 60.3 ms                                                                                                           | 71.9 ms: 1.19x slower                                                                                                         |
| bench_mp_pool            | 7.14 ms                                                                                                           | 8.60 ms: 1.21x slower                                                                                                         |
| scimark_fft              | 444 ms                                                                                                            | 537 ms: 1.21x slower                                                                                                          |
| scimark_sparse_mat_mult  | 6.58 ms                                                                                                           | 7.98 ms: 1.21x slower                                                                                                         |
| sympy_integrate          | 21.6 ms                                                                                                           | 26.3 ms: 1.22x slower                                                                                                         |
| richards                 | 53.4 ms                                                                                                           | 65.4 ms: 1.22x slower                                                                                                         |
| go                       | 161 ms                                                                                                            | 198 ms: 1.23x slower                                                                                                          |
| pprint_safe_repr         | 941 ms                                                                                                            | 1.16 sec: 1.23x slower                                                                                                        |
| nbody                    | 112 ms                                                                                                            | 138 ms: 1.23x slower                                                                                                          |
| pprint_pformat           | 1.92 sec                                                                                                          | 2.37 sec: 1.24x slower                                                                                                        |
| crypto_pyaes             | 81.9 ms                                                                                                           | 102 ms: 1.25x slower                                                                                                          |
| mako                     | 13.2 ms                                                                                                           | 16.5 ms: 1.25x slower                                                                                                         |
| fannkuch                 | 461 ms                                                                                                            | 575 ms: 1.25x slower                                                                                                          |
| pickle_pure_python       | 360 us                                                                                                            | 449 us: 1.25x slower                                                                                                          |
| pyflate                  | 581 ms                                                                                                            | 726 ms: 1.25x slower                                                                                                          |
| sqlglot_parse            | 1.40 ms                                                                                                           | 1.75 ms: 1.25x slower                                                                                                         |
| chaos                    | 67.8 ms                                                                                                           | 85.1 ms: 1.26x slower                                                                                                         |
| scimark_sor              | 158 ms                                                                                                            | 198 ms: 1.26x slower                                                                                                          |
| float                    | 90.2 ms                                                                                                           | 114 ms: 1.26x slower                                                                                                          |
| sqlglot_transpile        | 1.75 ms                                                                                                           | 2.21 ms: 1.26x slower                                                                                                         |
| genshi_xml               | 61.0 ms                                                                                                           | 77.7 ms: 1.27x slower                                                                                                         |
| regex_compile            | 130 ms                                                                                                            | 167 ms: 1.28x slower                                                                                                          |
| genshi_text              | 28.0 ms                                                                                                           | 36.6 ms: 1.31x slower                                                                                                         |
| spectral_norm            | 141 ms                                                                                                            | 186 ms: 1.32x slower                                                                                                          |
| nqueens                  | 98.0 ms                                                                                                           | 130 ms: 1.32x slower                                                                                                          |
| deltablue                | 3.85 ms                                                                                                           | 5.19 ms: 1.35x slower                                                                                                         |
| scimark_monte_carlo      | 83.9 ms                                                                                                           | 114 ms: 1.36x slower                                                                                                          |
| unpickle_pure_python     | 252 us                                                                                                            | 349 us: 1.38x slower                                                                                                          |
| deepcopy_memo            | 51.4 us                                                                                                           | 71.6 us: 1.39x slower                                                                                                         |
| logging_silent           | 134 ns                                                                                                            | 188 ns: 1.41x slower                                                                                                          |
| comprehensions           | 20.9 us                                                                                                           | 30.0 us: 1.44x slower                                                                                                         |
| hexiom                   | 7.11 ms                                                                                                           | 10.5 ms: 1.48x slower                                                                                                         |
| scimark_lu               | 138 ms                                                                                                            | 207 ms: 1.50x slower                                                                                                          |
| Geometric mean           | (ref)                                                                                                             | 1.13x slower                                                                                                                  |

Benchmark hidden because not significant (20): python_startup_no_site, asyncio_tcp, asyncio_websockets, gc_traversal, unpickle, python_startup, pickle_list, pidigits, regex_effbot, json_loads, pickle, async_tree_memoization_tg, generators, dask, pickle_dict, flaskblogging, xml_etree_parse, async_tree_cpu_io_mixed_tg, async_tree_io, tornado_http

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.01x