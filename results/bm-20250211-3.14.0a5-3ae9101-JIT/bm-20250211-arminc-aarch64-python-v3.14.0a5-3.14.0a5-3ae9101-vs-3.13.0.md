# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a5
- machine: linux-aarch64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.006x faster
- HPT reliability: 92.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.26 sec: 1.10x slower                                       |
| Geometric mean | (ref)                                                    | 1.02x slower                                                 |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 505 ms: 1.31x faster                                         |
| async_tree_memoization     | 664 ms                                                   | 513 ms: 1.29x faster                                         |
| async_tree_none            | 504 ms                                                   | 401 ms: 1.26x faster                                         |
| async_tree_io_tg           | 1.16 sec                                                 | 933 ms: 1.25x faster                                         |
| async_tree_io              | 1.14 sec                                                 | 936 ms: 1.22x faster                                         |
| async_tree_none_tg         | 484 ms                                                   | 399 ms: 1.22x faster                                         |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 679 ms: 1.18x faster                                         |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 701 ms: 1.13x faster                                         |
| Geometric mean             | (ref)                                                    | 1.17x faster                                                 |

Benchmark hidden because not significant (3): async_generators, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.9 ms: 1.10x faster                                        |
| Geometric mean | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.10 ms: 1.24x faster                                        |
| regex_compile  | 134 ms                                                   | 125 ms: 1.07x faster                                         |
| Geometric mean | (ref)                                                    | 1.07x faster                                                 |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_iterparse | 159 ms                                                   | 147 ms: 1.08x faster                                         |
| xml_etree_parse     | 203 ms                                                   | 188 ms: 1.08x faster                                         |
| tomli_loads         | 2.67 sec                                                 | 2.48 sec: 1.07x faster                                       |
| pickle_pure_python  | 374 us                                                   | 426 us: 1.14x slower                                         |
| Geometric mean      | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_process, json_dumps, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.04 ms: 1.03x slower                                        |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                 |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml     | 61.6 ms                                                  | 66.9 ms: 1.09x slower                                        |
| Geometric mean | (ref)                                                    | 1.03x slower                                                 |

Benchmark hidden because not significant (3): mako, django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 341 us: 1.40x faster                                         |
| deepcopy_memo              | 53.0 us                                                  | 39.3 us: 1.35x faster                                        |
| async_tree_memoization_tg  | 663 ms                                                   | 505 ms: 1.31x faster                                         |
| async_tree_memoization     | 664 ms                                                   | 513 ms: 1.29x faster                                         |
| async_tree_none            | 504 ms                                                   | 401 ms: 1.26x faster                                         |
| async_tree_io_tg           | 1.16 sec                                                 | 933 ms: 1.25x faster                                         |
| regex_effbot               | 5.10 ms                                                  | 4.10 ms: 1.24x faster                                        |
| async_tree_io              | 1.14 sec                                                 | 936 ms: 1.22x faster                                         |
| async_tree_none_tg         | 484 ms                                                   | 399 ms: 1.22x faster                                         |
| spectral_norm              | 143 ms                                                   | 118 ms: 1.21x faster                                         |
| deepcopy_reduce            | 4.24 us                                                  | 3.58 us: 1.19x faster                                        |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 679 ms: 1.18x faster                                         |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 701 ms: 1.13x faster                                         |
| scimark_fft                | 463 ms                                                   | 419 ms: 1.10x faster                                         |
| float                      | 95.8 ms                                                  | 86.9 ms: 1.10x faster                                        |
| generators                 | 40.3 ms                                                  | 37.1 ms: 1.09x faster                                        |
| xml_etree_iterparse        | 159 ms                                                   | 147 ms: 1.08x faster                                         |
| telco                      | 10.5 ms                                                  | 9.68 ms: 1.08x faster                                        |
| xml_etree_parse            | 203 ms                                                   | 188 ms: 1.08x faster                                         |
| coverage                   | 106 ms                                                   | 98.2 ms: 1.08x faster                                        |
| tomli_loads                | 2.67 sec                                                 | 2.48 sec: 1.07x faster                                       |
| pathlib                    | 24.3 ms                                                  | 22.7 ms: 1.07x faster                                        |
| regex_compile              | 134 ms                                                   | 125 ms: 1.07x faster                                         |
| scimark_sor                | 164 ms                                                   | 155 ms: 1.06x faster                                         |
| bpe_tokeniser              | 6.02 sec                                                 | 5.76 sec: 1.04x faster                                       |
| python_startup_no_site     | 8.79 ms                                                  | 9.04 ms: 1.03x slower                                        |
| mdp                        | 3.45 sec                                                 | 3.57 sec: 1.04x slower                                       |
| shortest_path              | 565 ms                                                   | 588 ms: 1.04x slower                                         |
| sympy_expand               | 472 ms                                                   | 497 ms: 1.05x slower                                         |
| deltablue                  | 3.97 ms                                                  | 4.22 ms: 1.06x slower                                        |
| pycparser                  | 1.34 sec                                                 | 1.43 sec: 1.07x slower                                       |
| create_gc_cycles           | 3.39 ms                                                  | 3.64 ms: 1.07x slower                                        |
| sympy_str                  | 265 ms                                                   | 288 ms: 1.08x slower                                         |
| genshi_xml                 | 61.6 ms                                                  | 66.9 ms: 1.09x slower                                        |
| sqlglot_parse              | 1.43 ms                                                  | 1.56 ms: 1.09x slower                                        |
| raytrace                   | 310 ms                                                   | 338 ms: 1.09x slower                                         |
| docutils                   | 2.96 sec                                                 | 3.26 sec: 1.10x slower                                       |
| typing_runtime_protocols   | 197 us                                                   | 218 us: 1.11x slower                                         |
| meteor_contest             | 117 ms                                                   | 129 ms: 1.11x slower                                         |
| crypto_pyaes               | 84.9 ms                                                  | 96.3 ms: 1.13x slower                                        |
| pickle_pure_python         | 374 us                                                   | 426 us: 1.14x slower                                         |
| fannkuch                   | 478 ms                                                   | 548 ms: 1.15x slower                                         |
| gc_traversal               | 5.92 ms                                                  | 6.85 ms: 1.16x slower                                        |
| nqueens                    | 105 ms                                                   | 122 ms: 1.16x slower                                         |
| comprehensions             | 20.8 us                                                  | 24.5 us: 1.18x slower                                        |
| hexiom                     | 7.34 ms                                                  | 8.94 ms: 1.22x slower                                        |
| subparsers                 | 20.3 ms                                                  | 27.4 ms: 1.35x slower                                        |
| many_optionals             | 626 us                                                   | 855 us: 1.36x slower                                         |
| pprint_pformat             | 1.99 sec                                                 | 2.72 sec: 1.37x slower                                       |
| pprint_safe_repr           | 962 ms                                                   | 1.32 sec: 1.38x slower                                       |
| bench_mp_pool              | 8.07 ms                                                  | 3.45 sec: 427.27x slower                                     |
| Geometric mean             | (ref)                                                    | 1.06x slower                                                 |

Benchmark hidden because not significant (44): pylint, logging_format, xml_etree_generate, thrift, scimark_monte_carlo, chaos, async_generators, sqlalchemy_imperative, xml_etree_process, richards_super, richards, logging_simple, sqlalchemy_declarative, sqlglot_normalize, mako, html5lib, k_core, scimark_lu, sympy_sum, regex_dna, sphinx, pyflate, sqlite_synth, asyncio_websockets, coroutines, django_template, go, connected_components, bench_thread_pool, pidigits, json_dumps, scimark_sparse_mat_mult, 2to3, json, python_startup, regex_v8, sqlglot_transpile, logging_silent, sympy_integrate, unpickle_pure_python, json_loads, genshi_text, sqlglot_optimize, nbody
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250211-3.14.0a5-3ae9101-JIT/bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101.json: dulwich_log

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 92.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x