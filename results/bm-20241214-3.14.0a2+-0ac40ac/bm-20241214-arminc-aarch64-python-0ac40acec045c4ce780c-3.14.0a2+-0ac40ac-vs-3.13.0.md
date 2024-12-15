# Results vs. 3.13.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-aarch64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.033x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.05 sec: 1.03x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 481 ms: 1.38x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 512 ms: 1.30x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 904 ms: 1.29x faster                                                     |
| async_tree_none            | 504 ms                                                   | 401 ms: 1.26x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 390 ms: 1.24x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 922 ms: 1.24x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 671 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 686 ms: 1.15x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.18x faster                                                             |

Benchmark hidden because not significant (3): coroutines, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.07 ms: 1.25x faster                                                    |
| Geometric mean | (ref)                                                    | 1.06x faster                                                             |

Benchmark hidden because not significant (3): regex_compile, regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.11x faster                                                     |
| pickle_pure_python  | 374 us                                                   | 400 us: 1.07x slower                                                     |
| Geometric mean      | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (6): xml_etree_generate, xml_etree_process, json_loads, unpickle_pure_python, tomli_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 39.4 ms                                                  | 42.7 ms: 1.08x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 481 ms: 1.38x faster                                                     |
| deepcopy                   | 479 us                                                   | 353 us: 1.36x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 512 ms: 1.30x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 904 ms: 1.29x faster                                                     |
| async_tree_none            | 504 ms                                                   | 401 ms: 1.26x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.07 ms: 1.25x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 390 ms: 1.24x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 42.7 us: 1.24x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 922 ms: 1.24x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 671 ms: 1.19x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.65 us: 1.16x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 686 ms: 1.15x faster                                                     |
| go                         | 164 ms                                                   | 144 ms: 1.14x faster                                                     |
| pylint                     | 345 ms                                                   | 306 ms: 1.13x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.8 ms: 1.12x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.11x faster                                                     |
| scimark_fft                | 463 ms                                                   | 419 ms: 1.10x faster                                                     |
| spectral_norm              | 143 ms                                                   | 130 ms: 1.10x faster                                                     |
| generators                 | 40.3 ms                                                  | 36.6 ms: 1.10x faster                                                    |
| coverage                   | 106 ms                                                   | 97.7 ms: 1.08x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.73 ms: 1.08x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.26 sec: 1.06x faster                                                   |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.28 ms: 1.06x faster                                                    |
| json                       | 5.94 ms                                                  | 5.61 ms: 1.06x faster                                                    |
| scimark_lu                 | 146 ms                                                   | 139 ms: 1.05x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.74 sec: 1.05x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.86 sec: 1.05x faster                                                   |
| pyflate                    | 582 ms                                                   | 561 ms: 1.04x faster                                                     |
| mdp                        | 3.45 sec                                                 | 3.38 sec: 1.02x faster                                                   |
| connected_components       | 547 ms                                                   | 536 ms: 1.02x faster                                                     |
| docutils                   | 2.96 sec                                                 | 3.05 sec: 1.03x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.05 sec: 1.03x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 997 ms: 1.04x slower                                                     |
| raytrace                   | 310 ms                                                   | 324 ms: 1.04x slower                                                     |
| sympy_str                  | 265 ms                                                   | 278 ms: 1.05x slower                                                     |
| logging_silent             | 135 ns                                                   | 142 ns: 1.05x slower                                                     |
| pickle_pure_python         | 374 us                                                   | 400 us: 1.07x slower                                                     |
| django_template            | 39.4 ms                                                  | 42.7 ms: 1.08x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.72 ms: 1.10x slower                                                    |
| many_optionals             | 626 us                                                   | 715 us: 1.14x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.95 ms: 1.17x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 25.8 ms: 1.27x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 6.14 sec: 761.52x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (51): sqlalchemy_declarative, thrift, sympy_sum, sqlalchemy_imperative, xml_etree_generate, 2to3, scimark_sor, xml_etree_process, genshi_text, regex_compile, nqueens, html5lib, scimark_monte_carlo, sphinx, logging_format, sqlglot_optimize, json_loads, coroutines, regex_v8, fannkuch, shortest_path, async_generators, asyncio_websockets, crypto_pyaes, unpickle_pure_python, meteor_contest, djangocms, genshi_xml, deltablue, bench_thread_pool, regex_dna, sqlglot_normalize, float, tomli_loads, richards_super, hexiom, sqlglot_transpile, comprehensions, pidigits, python_startup, sqlite_synth, mako, sympy_expand, nbody, richards, sympy_integrate, json_dumps, chaos, sqlglot_parse, logging_simple, typing_runtime_protocols
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x