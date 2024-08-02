# Results vs. base

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-aarch64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.13x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 303 ms                                                                                                            | 353 ms: 1.17x slower                                                                                                          |
| chameleon      | 9.03 ms                                                                                                           | 9.93 ms: 1.10x slower                                                                                                         |
| docutils       | 3.09 sec                                                                                                          | 3.51 sec: 1.13x slower                                                                                                        |
| html5lib       | 68.3 ms                                                                                                           | 73.7 ms: 1.08x slower                                                                                                         |
| tornado_http   | 131 ms                                                                                                            | 139 ms: 1.06x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                             | 1.11x slower                                                                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.23 sec                                                                                                          | 1.26 sec: 1.03x slower                                                                                                        |
| async_tree_cpu_io_mixed_tg | 792 ms                                                                                                            | 816 ms: 1.03x slower                                                                                                          |
| async_tree_none_tg         | 465 ms                                                                                                            | 481 ms: 1.03x slower                                                                                                          |
| async_tree_memoization     | 642 ms                                                                                                            | 665 ms: 1.04x slower                                                                                                          |
| async_tree_cpu_io_mixed    | 785 ms                                                                                                            | 814 ms: 1.04x slower                                                                                                          |
| async_tree_none            | 486 ms                                                                                                            | 507 ms: 1.04x slower                                                                                                          |
| Geometric mean             | (ref)                                                                                                             | 1.03x slower                                                                                                                  |

Benchmark hidden because not significant (2): async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 113 ms                                                                                                            | 137 ms: 1.22x slower                                                                                                          |
| float          | 90.6 ms                                                                                                           | 113 ms: 1.25x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                             | 1.15x slower                                                                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 131 ms                                                                                                            | 166 ms: 1.27x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                             | 1.06x slower                                                                                                                  |

Benchmark hidden because not significant (3): regex_effbot, regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| unpickle             | 19.7 us                                                                                                           | 19.5 us: 1.01x faster                                                                                                         |
| pickle               | 13.8 us                                                                                                           | 14.0 us: 1.02x slower                                                                                                         |
| pickle_list          | 5.19 us                                                                                                           | 5.28 us: 1.02x slower                                                                                                         |
| unpickle_list        | 6.63 us                                                                                                           | 6.77 us: 1.02x slower                                                                                                         |
| json_dumps           | 13.3 ms                                                                                                           | 13.9 ms: 1.05x slower                                                                                                         |
| xml_etree_iterparse  | 152 ms                                                                                                            | 162 ms: 1.06x slower                                                                                                          |
| xml_etree_process    | 80.3 ms                                                                                                           | 87.2 ms: 1.09x slower                                                                                                         |
| xml_etree_generate   | 112 ms                                                                                                            | 125 ms: 1.12x slower                                                                                                          |
| tomli_loads          | 2.56 sec                                                                                                          | 3.09 sec: 1.21x slower                                                                                                        |
| pickle_pure_python   | 358 us                                                                                                            | 440 us: 1.23x slower                                                                                                          |
| unpickle_pure_python | 254 us                                                                                                            | 349 us: 1.38x slower                                                                                                          |
| Geometric mean       | (ref)                                                                                                             | 1.08x slower                                                                                                                  |

Benchmark hidden because not significant (3): json_loads, pickle_dict, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 12.3 ms                                                                                                           | 12.6 ms: 1.02x slower                                                                                                         |
| Geometric mean | (ref)                                                                                                             | 1.02x slower                                                                                                                  |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| django_template | 41.7 ms                                                                                                           | 48.9 ms: 1.17x slower                                                                                                         |
| genshi_xml      | 61.2 ms                                                                                                           | 76.1 ms: 1.24x slower                                                                                                         |
| mako            | 13.5 ms                                                                                                           | 16.8 ms: 1.25x slower                                                                                                         |
| genshi_text     | 28.6 ms                                                                                                           | 35.6 ms: 1.25x slower                                                                                                         |
| Geometric mean  | (ref)                                                                                                             | 1.23x slower                                                                                                                  |

All benchmarks:
===============

| Benchmark                  | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| unpickle                   | 19.7 us                                                                                                           | 19.5 us: 1.01x faster                                                                                                         |
| asyncio_tcp_ssl            | 2.22 sec                                                                                                          | 2.26 sec: 1.01x slower                                                                                                        |
| pickle                     | 13.8 us                                                                                                           | 14.0 us: 1.02x slower                                                                                                         |
| asyncio_websockets         | 658 ms                                                                                                            | 668 ms: 1.02x slower                                                                                                          |
| pickle_list                | 5.19 us                                                                                                           | 5.28 us: 1.02x slower                                                                                                         |
| sqlite_synth               | 3.90 us                                                                                                           | 3.98 us: 1.02x slower                                                                                                         |
| unpickle_list              | 6.63 us                                                                                                           | 6.77 us: 1.02x slower                                                                                                         |
| python_startup             | 12.3 ms                                                                                                           | 12.6 ms: 1.02x slower                                                                                                         |
| json                       | 5.68 ms                                                                                                           | 5.81 ms: 1.02x slower                                                                                                         |
| async_tree_io_tg           | 1.23 sec                                                                                                          | 1.26 sec: 1.03x slower                                                                                                        |
| async_tree_cpu_io_mixed_tg | 792 ms                                                                                                            | 816 ms: 1.03x slower                                                                                                          |
| asyncio_tcp                | 574 ms                                                                                                            | 592 ms: 1.03x slower                                                                                                          |
| async_tree_none_tg         | 465 ms                                                                                                            | 481 ms: 1.03x slower                                                                                                          |
| async_tree_memoization     | 642 ms                                                                                                            | 665 ms: 1.04x slower                                                                                                          |
| async_tree_cpu_io_mixed    | 785 ms                                                                                                            | 814 ms: 1.04x slower                                                                                                          |
| bench_mp_pool              | 7.41 ms                                                                                                           | 7.71 ms: 1.04x slower                                                                                                         |
| async_generators           | 496 ms                                                                                                            | 517 ms: 1.04x slower                                                                                                          |
| thrift                     | 942 us                                                                                                            | 983 us: 1.04x slower                                                                                                          |
| async_tree_none            | 486 ms                                                                                                            | 507 ms: 1.04x slower                                                                                                          |
| bench_thread_pool          | 1.29 ms                                                                                                           | 1.35 ms: 1.05x slower                                                                                                         |
| pathlib                    | 21.8 ms                                                                                                           | 22.8 ms: 1.05x slower                                                                                                         |
| dask                       | 373 ms                                                                                                            | 391 ms: 1.05x slower                                                                                                          |
| json_dumps                 | 13.3 ms                                                                                                           | 13.9 ms: 1.05x slower                                                                                                         |
| logging_simple             | 7.00 us                                                                                                           | 7.38 us: 1.05x slower                                                                                                         |
| flaskblogging              | 4.76 ms                                                                                                           | 5.02 ms: 1.06x slower                                                                                                         |
| tornado_http               | 131 ms                                                                                                            | 139 ms: 1.06x slower                                                                                                          |
| xml_etree_iterparse        | 152 ms                                                                                                            | 162 ms: 1.06x slower                                                                                                          |
| coroutines                 | 29.0 ms                                                                                                           | 30.8 ms: 1.06x slower                                                                                                         |
| mdp                        | 3.37 sec                                                                                                          | 3.59 sec: 1.06x slower                                                                                                        |
| html5lib                   | 68.3 ms                                                                                                           | 73.7 ms: 1.08x slower                                                                                                         |
| xml_etree_process          | 80.3 ms                                                                                                           | 87.2 ms: 1.09x slower                                                                                                         |
| chameleon                  | 9.03 ms                                                                                                           | 9.93 ms: 1.10x slower                                                                                                         |
| xml_etree_generate         | 112 ms                                                                                                            | 125 ms: 1.12x slower                                                                                                          |
| dulwich_log                | 58.3 ms                                                                                                           | 65.2 ms: 1.12x slower                                                                                                         |
| pycparser                  | 1.22 sec                                                                                                          | 1.37 sec: 1.13x slower                                                                                                        |
| sympy_expand               | 462 ms                                                                                                            | 522 ms: 1.13x slower                                                                                                          |
| docutils                   | 3.09 sec                                                                                                          | 3.51 sec: 1.13x slower                                                                                                        |
| sqlglot_optimize           | 63.0 ms                                                                                                           | 72.3 ms: 1.15x slower                                                                                                         |
| raytrace                   | 297 ms                                                                                                            | 342 ms: 1.15x slower                                                                                                          |
| typing_runtime_protocols   | 197 us                                                                                                            | 227 us: 1.15x slower                                                                                                          |
| pylint                     | 342 ms                                                                                                            | 396 ms: 1.16x slower                                                                                                          |
| sqlglot_normalize          | 128 ms                                                                                                            | 149 ms: 1.16x slower                                                                                                          |
| 2to3                       | 303 ms                                                                                                            | 353 ms: 1.17x slower                                                                                                          |
| django_template            | 41.7 ms                                                                                                           | 48.9 ms: 1.17x slower                                                                                                         |
| meteor_contest             | 113 ms                                                                                                            | 133 ms: 1.17x slower                                                                                                          |
| deepcopy_reduce            | 4.07 us                                                                                                           | 4.80 us: 1.18x slower                                                                                                         |
| sympy_str                  | 268 ms                                                                                                            | 317 ms: 1.18x slower                                                                                                          |
| deepcopy                   | 450 us                                                                                                            | 535 us: 1.19x slower                                                                                                          |
| richards_super             | 60.1 ms                                                                                                           | 72.5 ms: 1.21x slower                                                                                                         |
| tomli_loads                | 2.56 sec                                                                                                          | 3.09 sec: 1.21x slower                                                                                                        |
| richards                   | 53.3 ms                                                                                                           | 64.4 ms: 1.21x slower                                                                                                         |
| go                         | 161 ms                                                                                                            | 195 ms: 1.21x slower                                                                                                          |
| sympy_sum                  | 144 ms                                                                                                            | 175 ms: 1.21x slower                                                                                                          |
| scimark_fft                | 443 ms                                                                                                            | 539 ms: 1.22x slower                                                                                                          |
| nbody                      | 113 ms                                                                                                            | 137 ms: 1.22x slower                                                                                                          |
| sympy_integrate            | 21.1 ms                                                                                                           | 25.9 ms: 1.23x slower                                                                                                         |
| pickle_pure_python         | 358 us                                                                                                            | 440 us: 1.23x slower                                                                                                          |
| scimark_sparse_mat_mult    | 6.53 ms                                                                                                           | 8.05 ms: 1.23x slower                                                                                                         |
| fannkuch                   | 463 ms                                                                                                            | 574 ms: 1.24x slower                                                                                                          |
| crypto_pyaes               | 81.5 ms                                                                                                           | 101 ms: 1.24x slower                                                                                                          |
| scimark_sor                | 159 ms                                                                                                            | 198 ms: 1.24x slower                                                                                                          |
| genshi_xml                 | 61.2 ms                                                                                                           | 76.1 ms: 1.24x slower                                                                                                         |
| mako                       | 13.5 ms                                                                                                           | 16.8 ms: 1.25x slower                                                                                                         |
| genshi_text                | 28.6 ms                                                                                                           | 35.6 ms: 1.25x slower                                                                                                         |
| float                      | 90.6 ms                                                                                                           | 113 ms: 1.25x slower                                                                                                          |
| pyflate                    | 578 ms                                                                                                            | 727 ms: 1.26x slower                                                                                                          |
| sqlglot_parse              | 1.40 ms                                                                                                           | 1.77 ms: 1.26x slower                                                                                                         |
| pprint_pformat             | 1.91 sec                                                                                                          | 2.41 sec: 1.26x slower                                                                                                        |
| pprint_safe_repr           | 935 ms                                                                                                            | 1.18 sec: 1.27x slower                                                                                                        |
| chaos                      | 67.6 ms                                                                                                           | 85.6 ms: 1.27x slower                                                                                                         |
| regex_compile              | 131 ms                                                                                                            | 166 ms: 1.27x slower                                                                                                          |
| sqlglot_transpile          | 1.73 ms                                                                                                           | 2.22 ms: 1.28x slower                                                                                                         |
| spectral_norm              | 141 ms                                                                                                            | 185 ms: 1.31x slower                                                                                                          |
| nqueens                    | 99.0 ms                                                                                                           | 130 ms: 1.32x slower                                                                                                          |
| deltablue                  | 3.88 ms                                                                                                           | 5.14 ms: 1.32x slower                                                                                                         |
| scimark_monte_carlo        | 83.0 ms                                                                                                           | 114 ms: 1.37x slower                                                                                                          |
| unpickle_pure_python       | 254 us                                                                                                            | 349 us: 1.38x slower                                                                                                          |
| deepcopy_memo              | 51.3 us                                                                                                           | 71.9 us: 1.40x slower                                                                                                         |
| logging_silent             | 133 ns                                                                                                            | 189 ns: 1.42x slower                                                                                                          |
| comprehensions             | 20.7 us                                                                                                           | 30.1 us: 1.46x slower                                                                                                         |
| hexiom                     | 7.03 ms                                                                                                           | 10.5 ms: 1.49x slower                                                                                                         |
| scimark_lu                 | 139 ms                                                                                                            | 207 ms: 1.49x slower                                                                                                          |
| Geometric mean             | (ref)                                                                                                             | 1.13x slower                                                                                                                  |

Benchmark hidden because not significant (16): gc_traversal, json_loads, regex_effbot, regex_v8, pidigits, regex_dna, coverage, pickle_dict, generators, xml_etree_parse, telco, python_startup_no_site, create_gc_cycles, async_tree_io, logging_format, async_tree_memoization_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.01x