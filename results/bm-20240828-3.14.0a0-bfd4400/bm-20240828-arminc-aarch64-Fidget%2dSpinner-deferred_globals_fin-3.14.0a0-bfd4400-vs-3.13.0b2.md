# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-aarch64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 300 ms: 1.02x faster                                                              |
| docutils       | 3.10 sec                                                     | 3.13 sec: 1.01x slower                                                            |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                      |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 398 ms: 1.20x faster                                                              |
| async_tree_memoization     | 645 ms                                                       | 553 ms: 1.17x faster                                                              |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.15x faster                                                            |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.14x faster                                                            |
| async_tree_memoization_tg  | 604 ms                                                       | 532 ms: 1.14x faster                                                              |
| async_tree_none            | 492 ms                                                       | 436 ms: 1.13x faster                                                              |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 723 ms: 1.09x faster                                                              |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 698 ms: 1.09x faster                                                              |
| Geometric mean             | (ref)                                                        | 1.14x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 110 ms: 1.04x faster                                                              |
| float          | 91.4 ms                                                      | 94.6 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.0 ms: 1.04x faster                                                             |
| regex_dna      | 259 ms                                                       | 253 ms: 1.02x faster                                                              |
| regex_effbot   | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                      |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|--------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python | 359 us                                                       | 351 us: 1.02x faster                                                              |
| json_loads         | 32.1 us                                                      | 32.5 us: 1.01x slower                                                             |
| json_dumps         | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                                             |
| Geometric mean     | (ref)                                                        | 1.00x slower                                                                      |

Benchmark hidden because not significant (6): xml_etree_process, xml_etree_generate, unpickle_pure_python, tomli_loads, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 12.9 ms: 1.00x faster                                                             |
| python_startup_no_site | 8.60 ms                                                      | 8.75 ms: 1.02x slower                                                             |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 27.9 ms: 1.02x slower                                                             |
| mako           | 13.2 ms                                                      | 13.7 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 330 us: 1.36x faster                                                              |
| deepcopy_memo              | 50.8 us                                                      | 37.6 us: 1.35x faster                                                             |
| async_tree_none_tg         | 476 ms                                                       | 398 ms: 1.20x faster                                                              |
| deepcopy_reduce            | 4.04 us                                                      | 3.45 us: 1.17x faster                                                             |
| async_tree_memoization     | 645 ms                                                       | 553 ms: 1.17x faster                                                              |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.15x faster                                                            |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.14x faster                                                            |
| async_tree_memoization_tg  | 604 ms                                                       | 532 ms: 1.14x faster                                                              |
| async_tree_none            | 492 ms                                                       | 436 ms: 1.13x faster                                                              |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 723 ms: 1.09x faster                                                              |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 698 ms: 1.09x faster                                                              |
| pathlib                    | 22.8 ms                                                      | 21.1 ms: 1.08x faster                                                             |
| generators                 | 37.1 ms                                                      | 34.8 ms: 1.07x faster                                                             |
| gc_traversal               | 5.17 ms                                                      | 4.85 ms: 1.07x faster                                                             |
| richards                   | 55.9 ms                                                      | 52.5 ms: 1.06x faster                                                             |
| richards_super             | 62.3 ms                                                      | 58.6 ms: 1.06x faster                                                             |
| scimark_lu                 | 141 ms                                                       | 134 ms: 1.05x faster                                                              |
| asyncio_tcp                | 584 ms                                                       | 562 ms: 1.04x faster                                                              |
| regex_v8                   | 31.1 ms                                                      | 30.0 ms: 1.04x faster                                                             |
| nbody                      | 114 ms                                                       | 110 ms: 1.04x faster                                                              |
| pprint_pformat             | 1.93 sec                                                     | 1.88 sec: 1.03x faster                                                            |
| logging_format             | 7.82 us                                                      | 7.62 us: 1.03x faster                                                             |
| logging_simple             | 7.21 us                                                      | 7.02 us: 1.03x faster                                                             |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.39 ms: 1.02x faster                                                             |
| logging_silent             | 133 ns                                                       | 130 ns: 1.02x faster                                                              |
| hexiom                     | 7.08 ms                                                      | 6.91 ms: 1.02x faster                                                             |
| coroutines                 | 29.0 ms                                                      | 28.3 ms: 1.02x faster                                                             |
| pickle_pure_python         | 359 us                                                       | 351 us: 1.02x faster                                                              |
| regex_dna                  | 259 ms                                                       | 253 ms: 1.02x faster                                                              |
| scimark_sor                | 159 ms                                                       | 156 ms: 1.02x faster                                                              |
| regex_effbot               | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                             |
| pprint_safe_repr           | 933 ms                                                       | 916 ms: 1.02x faster                                                              |
| 2to3                       | 305 ms                                                       | 300 ms: 1.02x faster                                                              |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.01x faster                                                             |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.18 sec: 1.01x faster                                                            |
| meteor_contest             | 113 ms                                                       | 112 ms: 1.01x faster                                                              |
| go                         | 161 ms                                                       | 159 ms: 1.01x faster                                                              |
| python_startup             | 13.0 ms                                                      | 12.9 ms: 1.00x faster                                                             |
| sympy_str                  | 265 ms                                                       | 268 ms: 1.01x slower                                                              |
| docutils                   | 3.10 sec                                                     | 3.13 sec: 1.01x slower                                                            |
| sympy_expand               | 457 ms                                                       | 462 ms: 1.01x slower                                                              |
| json_loads                 | 32.1 us                                                      | 32.5 us: 1.01x slower                                                             |
| nqueens                    | 98.9 ms                                                      | 100 ms: 1.02x slower                                                              |
| genshi_text                | 27.4 ms                                                      | 27.9 ms: 1.02x slower                                                             |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                                             |
| python_startup_no_site     | 8.60 ms                                                      | 8.75 ms: 1.02x slower                                                             |
| bpe_tokeniser              | 5.83 sec                                                     | 5.94 sec: 1.02x slower                                                            |
| typing_runtime_protocols   | 193 us                                                       | 198 us: 1.03x slower                                                              |
| float                      | 91.4 ms                                                      | 94.6 ms: 1.03x slower                                                             |
| mako                       | 13.2 ms                                                      | 13.7 ms: 1.04x slower                                                             |
| pyflate                    | 557 ms                                                       | 579 ms: 1.04x slower                                                              |
| fannkuch                   | 451 ms                                                       | 471 ms: 1.04x slower                                                              |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                      |

Benchmark hidden because not significant (37): tornado_http, sqlglot_normalize, create_gc_cycles, django_template, deltablue, comprehensions, regex_compile, xml_etree_process, scimark_monte_carlo, sqlglot_optimize, pycparser, chaos, thrift, xml_etree_generate, bench_mp_pool, unpickle_pure_python, crypto_pyaes, scimark_fft, tomli_loads, async_generators, genshi_xml, raytrace, coverage, mdp, asyncio_websockets, xml_etree_parse, pidigits, html5lib, sqlglot_parse, telco, spectral_norm, sqlglot_transpile, sympy_sum, sympy_integrate, xml_etree_iterparse, json, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x