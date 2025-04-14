# Results vs. 3.13.0

- fork: zooba
- ref: gh_91349
- machine: linux-aarch64
- commit hash: 548daa7
- commit date: 2025-03-19
- overall geometric mean: 1.042x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 301 ms: 1.04x faster                                        |
| docutils       | 2.96 sec                                                 | 3.07 sec: 1.03x slower                                      |
| html5lib       | 65.6 ms                                                  | 64.5 ms: 1.02x faster                                       |
| sphinx         | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                      |
| Geometric mean | (ref)                                                    | 1.01x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 467 ms: 1.42x faster                                        |
| async_tree_memoization     | 664 ms                                                   | 468 ms: 1.42x faster                                        |
| async_tree_none            | 504 ms                                                   | 383 ms: 1.31x faster                                        |
| async_tree_none_tg         | 484 ms                                                   | 370 ms: 1.31x faster                                        |
| async_tree_io              | 1.14 sec                                                 | 884 ms: 1.29x faster                                        |
| async_tree_io_tg           | 1.16 sec                                                 | 918 ms: 1.27x faster                                        |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 648 ms: 1.24x faster                                        |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 658 ms: 1.20x faster                                        |
| async_generators           | 500 ms                                                   | 451 ms: 1.11x faster                                        |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 95.8 ms                                                  | 87.0 ms: 1.10x faster                                       |
| nbody          | 118 ms                                                   | 125 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                    | 1.02x faster                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.01 ms: 1.27x faster                                       |
| regex_v8       | 32.5 ms                                                  | 28.9 ms: 1.13x faster                                       |
| regex_dna      | 263 ms                                                   | 247 ms: 1.06x faster                                        |
| Geometric mean | (ref)                                                    | 1.13x faster                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 176 ms: 1.15x faster                                        |
| xml_etree_iterparse | 159 ms                                                   | 141 ms: 1.13x faster                                        |
| tomli_loads         | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                      |
| xml_etree_process   | 82.1 ms                                                  | 79.4 ms: 1.03x faster                                       |
| json_loads          | 32.8 us                                                  | 35.2 us: 1.07x slower                                       |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                |

Benchmark hidden because not significant (4): xml_etree_generate, json_dumps, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                       |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 27.0 ms: 1.06x faster                                       |
| genshi_xml     | 61.6 ms                                                  | 60.4 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                    | 1.01x faster                                                |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 467 ms: 1.42x faster                                        |
| async_tree_memoization     | 664 ms                                                   | 468 ms: 1.42x faster                                        |
| deepcopy                   | 479 us                                                   | 341 us: 1.41x faster                                        |
| deepcopy_memo              | 53.0 us                                                  | 39.1 us: 1.36x faster                                       |
| async_tree_none            | 504 ms                                                   | 383 ms: 1.31x faster                                        |
| async_tree_none_tg         | 484 ms                                                   | 370 ms: 1.31x faster                                        |
| async_tree_io              | 1.14 sec                                                 | 884 ms: 1.29x faster                                        |
| regex_effbot               | 5.10 ms                                                  | 4.01 ms: 1.27x faster                                       |
| async_tree_io_tg           | 1.16 sec                                                 | 918 ms: 1.27x faster                                        |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 648 ms: 1.24x faster                                        |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 658 ms: 1.20x faster                                        |
| deepcopy_reduce            | 4.24 us                                                  | 3.59 us: 1.18x faster                                       |
| go                         | 164 ms                                                   | 140 ms: 1.18x faster                                        |
| xml_etree_parse            | 203 ms                                                   | 176 ms: 1.15x faster                                        |
| spectral_norm              | 143 ms                                                   | 125 ms: 1.15x faster                                        |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.13x faster                                        |
| regex_v8                   | 32.5 ms                                                  | 28.9 ms: 1.13x faster                                       |
| pylint                     | 345 ms                                                   | 311 ms: 1.11x faster                                        |
| generators                 | 40.3 ms                                                  | 36.3 ms: 1.11x faster                                       |
| async_generators           | 500 ms                                                   | 451 ms: 1.11x faster                                        |
| pathlib                    | 24.3 ms                                                  | 22.1 ms: 1.10x faster                                       |
| float                      | 95.8 ms                                                  | 87.0 ms: 1.10x faster                                       |
| scimark_fft                | 463 ms                                                   | 424 ms: 1.09x faster                                        |
| tomli_loads                | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                      |
| scimark_sor                | 164 ms                                                   | 151 ms: 1.09x faster                                        |
| thrift                     | 1.01 ms                                                  | 936 us: 1.08x faster                                        |
| sqlite_synth               | 4.08 us                                                  | 3.82 us: 1.07x faster                                       |
| bpe_tokeniser              | 6.02 sec                                                 | 5.64 sec: 1.07x faster                                      |
| regex_dna                  | 263 ms                                                   | 247 ms: 1.06x faster                                        |
| coverage                   | 106 ms                                                   | 99.7 ms: 1.06x faster                                       |
| genshi_text                | 28.6 ms                                                  | 27.0 ms: 1.06x faster                                       |
| pycparser                  | 1.34 sec                                                 | 1.27 sec: 1.06x faster                                      |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                      |
| richards                   | 54.5 ms                                                  | 52.0 ms: 1.05x faster                                       |
| 2to3                       | 313 ms                                                   | 301 ms: 1.04x faster                                        |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.04x faster                                        |
| pyflate                    | 582 ms                                                   | 561 ms: 1.04x faster                                        |
| pprint_pformat             | 1.99 sec                                                 | 1.92 sec: 1.04x faster                                      |
| xml_etree_process          | 82.1 ms                                                  | 79.4 ms: 1.03x faster                                       |
| mdp                        | 3.45 sec                                                 | 3.34 sec: 1.03x faster                                      |
| sphinx                     | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                      |
| pprint_safe_repr           | 962 ms                                                   | 940 ms: 1.02x faster                                        |
| genshi_xml                 | 61.6 ms                                                  | 60.4 ms: 1.02x faster                                       |
| html5lib                   | 65.6 ms                                                  | 64.5 ms: 1.02x faster                                       |
| connected_components       | 547 ms                                                   | 558 ms: 1.02x slower                                        |
| docutils                   | 2.96 sec                                                 | 3.07 sec: 1.03x slower                                      |
| shortest_path              | 565 ms                                                   | 591 ms: 1.05x slower                                        |
| sympy_str                  | 265 ms                                                   | 277 ms: 1.05x slower                                        |
| fannkuch                   | 478 ms                                                   | 500 ms: 1.05x slower                                        |
| crypto_pyaes               | 84.9 ms                                                  | 89.1 ms: 1.05x slower                                       |
| nbody                      | 118 ms                                                   | 125 ms: 1.06x slower                                        |
| create_gc_cycles           | 3.39 ms                                                  | 3.60 ms: 1.06x slower                                       |
| json_loads                 | 32.8 us                                                  | 35.2 us: 1.07x slower                                       |
| scimark_lu                 | 146 ms                                                   | 157 ms: 1.08x slower                                        |
| gc_traversal               | 5.92 ms                                                  | 6.59 ms: 1.11x slower                                       |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                       |
| subparsers                 | 20.3 ms                                                  | 25.7 ms: 1.26x slower                                       |
| many_optionals             | 626 us                                                   | 830 us: 1.33x slower                                        |
| bench_mp_pool              | 8.07 ms                                                  | 3.19 sec: 395.27x slower                                    |
| Geometric mean             | (ref)                                                    | 1.02x slower                                                |

Benchmark hidden because not significant (32): regex_compile, telco, sqlalchemy_declarative, xml_etree_generate, sympy_sum, logging_format, scimark_monte_carlo, nqueens, logging_simple, richards_super, scimark_sparse_mat_mult, logging_silent, pidigits, json_dumps, asyncio_websockets, sympy_expand, typing_runtime_protocols, sympy_integrate, chaos, sqlalchemy_imperative, coroutines, python_startup, json, mako, bench_thread_pool, unpickle_pure_python, deltablue, comprehensions, hexiom, pickle_pure_python, raytrace, django_template
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250319-3.14.0a6+-548daa7/bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x