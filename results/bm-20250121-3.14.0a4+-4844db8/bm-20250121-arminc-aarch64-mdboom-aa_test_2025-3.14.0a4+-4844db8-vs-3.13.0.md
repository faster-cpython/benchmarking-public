# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025
- machine: linux-aarch64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.041x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.01 sec: 1.02x slower                                           |
| html5lib       | 65.6 ms                                                  | 63.0 ms: 1.04x faster                                            |
| sphinx         | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                           |
| Geometric mean | (ref)                                                    | 1.02x faster                                                     |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 477 ms: 1.39x faster                                             |
| async_tree_memoization     | 664 ms                                                   | 483 ms: 1.37x faster                                             |
| async_tree_none            | 504 ms                                                   | 379 ms: 1.33x faster                                             |
| async_tree_io_tg           | 1.16 sec                                                 | 889 ms: 1.31x faster                                             |
| async_tree_io              | 1.14 sec                                                 | 887 ms: 1.28x faster                                             |
| async_tree_none_tg         | 484 ms                                                   | 378 ms: 1.28x faster                                             |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 661 ms: 1.21x faster                                             |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 672 ms: 1.18x faster                                             |
| async_generators           | 500 ms                                                   | 446 ms: 1.12x faster                                             |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                     |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.7 ms: 1.12x faster                                            |
| Geometric mean | (ref)                                                    | 1.02x faster                                                     |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.06 ms: 1.26x faster                                            |
| regex_dna      | 263 ms                                                   | 251 ms: 1.05x faster                                             |
| Geometric mean | (ref)                                                    | 1.08x faster                                                     |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 183 ms: 1.11x faster                                             |
| xml_etree_iterparse  | 159 ms                                                   | 144 ms: 1.10x faster                                             |
| tomli_loads          | 2.67 sec                                                 | 2.59 sec: 1.03x faster                                           |
| unpickle_pure_python | 265 us                                                   | 285 us: 1.08x slower                                             |
| pickle_pure_python   | 374 us                                                   | 410 us: 1.10x slower                                             |
| Geometric mean       | (ref)                                                    | 1.00x faster                                                     |

Benchmark hidden because not significant (4): xml_etree_generate, json_loads, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.06 ms: 1.03x slower                                            |
| Geometric mean         | (ref)                                                    | 1.02x slower                                                     |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 477 ms: 1.39x faster                                             |
| async_tree_memoization     | 664 ms                                                   | 483 ms: 1.37x faster                                             |
| deepcopy                   | 479 us                                                   | 356 us: 1.34x faster                                             |
| async_tree_none            | 504 ms                                                   | 379 ms: 1.33x faster                                             |
| async_tree_io_tg           | 1.16 sec                                                 | 889 ms: 1.31x faster                                             |
| async_tree_io              | 1.14 sec                                                 | 887 ms: 1.28x faster                                             |
| deepcopy_memo              | 53.0 us                                                  | 41.3 us: 1.28x faster                                            |
| async_tree_none_tg         | 484 ms                                                   | 378 ms: 1.28x faster                                             |
| regex_effbot               | 5.10 ms                                                  | 4.06 ms: 1.26x faster                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 661 ms: 1.21x faster                                             |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 672 ms: 1.18x faster                                             |
| deepcopy_reduce            | 4.24 us                                                  | 3.66 us: 1.16x faster                                            |
| spectral_norm              | 143 ms                                                   | 125 ms: 1.15x faster                                             |
| go                         | 164 ms                                                   | 144 ms: 1.14x faster                                             |
| generators                 | 40.3 ms                                                  | 35.9 ms: 1.12x faster                                            |
| async_generators           | 500 ms                                                   | 446 ms: 1.12x faster                                             |
| float                      | 95.8 ms                                                  | 85.7 ms: 1.12x faster                                            |
| xml_etree_parse            | 203 ms                                                   | 183 ms: 1.11x faster                                             |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.10x faster                                             |
| scimark_fft                | 463 ms                                                   | 421 ms: 1.10x faster                                             |
| telco                      | 10.5 ms                                                  | 9.64 ms: 1.09x faster                                            |
| scimark_sor                | 164 ms                                                   | 152 ms: 1.08x faster                                             |
| pathlib                    | 24.3 ms                                                  | 22.6 ms: 1.08x faster                                            |
| sympy_sum                  | 151 ms                                                   | 142 ms: 1.06x faster                                             |
| coverage                   | 106 ms                                                   | 99.6 ms: 1.06x faster                                            |
| bpe_tokeniser              | 6.02 sec                                                 | 5.68 sec: 1.06x faster                                           |
| richards                   | 54.5 ms                                                  | 51.6 ms: 1.06x faster                                            |
| k_core                     | 2.99 sec                                                 | 2.85 sec: 1.05x faster                                           |
| regex_dna                  | 263 ms                                                   | 251 ms: 1.05x faster                                             |
| html5lib                   | 65.6 ms                                                  | 63.0 ms: 1.04x faster                                            |
| pycparser                  | 1.34 sec                                                 | 1.29 sec: 1.04x faster                                           |
| richards_super             | 60.8 ms                                                  | 58.5 ms: 1.04x faster                                            |
| tomli_loads                | 2.67 sec                                                 | 2.59 sec: 1.03x faster                                           |
| sqlglot_normalize          | 131 ms                                                   | 127 ms: 1.03x faster                                             |
| sphinx                     | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                           |
| docutils                   | 2.96 sec                                                 | 3.01 sec: 1.02x slower                                           |
| python_startup_no_site     | 8.79 ms                                                  | 9.06 ms: 1.03x slower                                            |
| typing_runtime_protocols   | 197 us                                                   | 207 us: 1.05x slower                                             |
| sympy_str                  | 265 ms                                                   | 279 ms: 1.05x slower                                             |
| create_gc_cycles           | 3.39 ms                                                  | 3.64 ms: 1.07x slower                                            |
| unpickle_pure_python       | 265 us                                                   | 285 us: 1.08x slower                                             |
| pickle_pure_python         | 374 us                                                   | 410 us: 1.10x slower                                             |
| gc_traversal               | 5.92 ms                                                  | 6.74 ms: 1.14x slower                                            |
| many_optionals             | 626 us                                                   | 733 us: 1.17x slower                                             |
| subparsers                 | 20.3 ms                                                  | 25.9 ms: 1.27x slower                                            |
| bench_mp_pool              | 8.07 ms                                                  | 4.70 sec: 582.92x slower                                         |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                     |

Benchmark hidden because not significant (49): pylint, sqlalchemy_declarative, xml_etree_generate, regex_compile, scimark_lu, thrift, pyflate, sqlglot_transpile, deltablue, scimark_sparse_mat_mult, chaos, connected_components, scimark_monte_carlo, 2to3, shortest_path, asyncio_websockets, sqlglot_optimize, sqlite_synth, mdp, sqlalchemy_imperative, bench_thread_pool, nqueens, crypto_pyaes, logging_format, json, meteor_contest, json_loads, regex_v8, logging_silent, pprint_pformat, comprehensions, sympy_expand, python_startup, hexiom, genshi_text, genshi_xml, pprint_safe_repr, pidigits, django_template, raytrace, coroutines, sympy_integrate, mako, sqlglot_parse, nbody, logging_simple, json_dumps, fannkuch, xml_etree_process
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250121-3.14.0a4+-4844db8/bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: dulwich_log

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x