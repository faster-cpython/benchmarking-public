# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-aarch64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.031x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 300 ms: 1.01x faster                                                              |
| docutils       | 2.89 sec                                                 | 3.13 sec: 1.08x slower                                                            |
| Geometric mean | (ref)                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 532 ms: 1.22x faster                                                              |
| async_tree_none_tg         | 470 ms                                                   | 398 ms: 1.18x faster                                                              |
| async_tree_memoization     | 651 ms                                                   | 553 ms: 1.18x faster                                                              |
| async_tree_none            | 497 ms                                                   | 436 ms: 1.14x faster                                                              |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 698 ms: 1.10x faster                                                              |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 723 ms: 1.06x faster                                                              |
| async_tree_io              | 1.11 sec                                                 | 1.07 sec: 1.03x faster                                                            |
| async_tree_io_tg           | 1.13 sec                                                 | 1.11 sec: 1.02x faster                                                            |
| coroutines                 | 28.5 ms                                                  | 28.3 ms: 1.01x faster                                                             |
| Geometric mean             | (ref)                                                    | 1.08x faster                                                                      |

Benchmark hidden because not significant (2): async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                                              |
| float          | 93.3 ms                                                  | 94.6 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.0 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                      |

Benchmark hidden because not significant (3): regex_compile, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|--------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python | 357 us                                                   | 351 us: 1.02x faster                                                              |
| tomli_loads        | 2.54 sec                                                 | 2.57 sec: 1.01x slower                                                            |
| json_loads         | 31.7 us                                                  | 32.5 us: 1.03x slower                                                             |
| Geometric mean     | (ref)                                                    | 1.00x faster                                                                      |

Benchmark hidden because not significant (6): xml_etree_parse, json_dumps, xml_etree_iterparse, xml_etree_process, xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 12.9 ms: 1.19x faster                                                             |
| Geometric mean | (ref)                                                    | 1.09x faster                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, django_template, genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.29 ms: 1.46x faster                                                             |
| deepcopy                   | 447 us                                                   | 330 us: 1.35x faster                                                              |
| deepcopy_memo              | 50.4 us                                                  | 37.6 us: 1.34x faster                                                             |
| async_tree_memoization_tg  | 649 ms                                                   | 532 ms: 1.22x faster                                                              |
| python_startup             | 15.4 ms                                                  | 12.9 ms: 1.19x faster                                                             |
| gc_traversal               | 5.77 ms                                                  | 4.85 ms: 1.19x faster                                                             |
| async_tree_none_tg         | 470 ms                                                   | 398 ms: 1.18x faster                                                              |
| deepcopy_reduce            | 4.07 us                                                  | 3.45 us: 1.18x faster                                                             |
| async_tree_memoization     | 651 ms                                                   | 553 ms: 1.18x faster                                                              |
| async_tree_none            | 497 ms                                                   | 436 ms: 1.14x faster                                                              |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 698 ms: 1.10x faster                                                              |
| bench_mp_pool              | 7.68 ms                                                  | 7.00 ms: 1.10x faster                                                             |
| generators                 | 37.6 ms                                                  | 34.8 ms: 1.08x faster                                                             |
| pathlib                    | 22.7 ms                                                  | 21.1 ms: 1.08x faster                                                             |
| regex_v8                   | 31.8 ms                                                  | 30.0 ms: 1.06x faster                                                             |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 723 ms: 1.06x faster                                                              |
| pycparser                  | 1.27 sec                                                 | 1.21 sec: 1.05x faster                                                            |
| nbody                      | 114 ms                                                   | 110 ms: 1.04x faster                                                              |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                              |
| async_tree_io              | 1.11 sec                                                 | 1.07 sec: 1.03x faster                                                            |
| hexiom                     | 7.11 ms                                                  | 6.91 ms: 1.03x faster                                                             |
| bench_thread_pool          | 1.27 ms                                                  | 1.24 ms: 1.03x faster                                                             |
| logging_format             | 7.82 us                                                  | 7.62 us: 1.03x faster                                                             |
| richards_super             | 60.1 ms                                                  | 58.6 ms: 1.02x faster                                                             |
| crypto_pyaes               | 83.7 ms                                                  | 81.7 ms: 1.02x faster                                                             |
| scimark_monte_carlo        | 83.6 ms                                                  | 81.6 ms: 1.02x faster                                                             |
| scimark_sor                | 160 ms                                                   | 156 ms: 1.02x faster                                                              |
| async_tree_io_tg           | 1.13 sec                                                 | 1.11 sec: 1.02x faster                                                            |
| richards                   | 53.6 ms                                                  | 52.5 ms: 1.02x faster                                                             |
| logging_silent             | 133 ns                                                   | 130 ns: 1.02x faster                                                              |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.39 ms: 1.02x faster                                                             |
| pickle_pure_python         | 357 us                                                   | 351 us: 1.02x faster                                                              |
| 2to3                       | 304 ms                                                   | 300 ms: 1.01x faster                                                              |
| meteor_contest             | 114 ms                                                   | 112 ms: 1.01x faster                                                              |
| thrift                     | 968 us                                                   | 956 us: 1.01x faster                                                              |
| raytrace                   | 300 ms                                                   | 296 ms: 1.01x faster                                                              |
| pprint_safe_repr           | 926 ms                                                   | 916 ms: 1.01x faster                                                              |
| pprint_pformat             | 1.90 sec                                                 | 1.88 sec: 1.01x faster                                                            |
| coroutines                 | 28.5 ms                                                  | 28.3 ms: 1.01x faster                                                             |
| mdp                        | 3.34 sec                                                 | 3.33 sec: 1.00x faster                                                            |
| tomli_loads                | 2.54 sec                                                 | 2.57 sec: 1.01x slower                                                            |
| sympy_expand               | 457 ms                                                   | 462 ms: 1.01x slower                                                              |
| bpe_tokeniser              | 5.87 sec                                                 | 5.94 sec: 1.01x slower                                                            |
| sympy_str                  | 264 ms                                                   | 268 ms: 1.01x slower                                                              |
| float                      | 93.3 ms                                                  | 94.6 ms: 1.01x slower                                                             |
| fannkuch                   | 461 ms                                                   | 471 ms: 1.02x slower                                                              |
| typing_runtime_protocols   | 193 us                                                   | 198 us: 1.03x slower                                                              |
| json_loads                 | 31.7 us                                                  | 32.5 us: 1.03x slower                                                             |
| telco                      | 9.74 ms                                                  | 10.1 ms: 1.03x slower                                                             |
| pyflate                    | 556 ms                                                   | 579 ms: 1.04x slower                                                              |
| docutils                   | 2.89 sec                                                 | 3.13 sec: 1.08x slower                                                            |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                                      |

Benchmark hidden because not significant (36): xml_etree_parse, tornado_http, json_dumps, coverage, sqlglot_transpile, logging_simple, xml_etree_iterparse, spectral_norm, scimark_fft, xml_etree_process, go, xml_etree_generate, async_generators, asyncio_websockets, regex_compile, comprehensions, json, html5lib, sqlglot_normalize, chaos, genshi_xml, regex_effbot, unpickle_pure_python, sqlglot_optimize, regex_dna, django_template, python_startup_no_site, nqueens, pidigits, deltablue, genshi_text, sympy_sum, sympy_integrate, mako, sqlglot_parse, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x