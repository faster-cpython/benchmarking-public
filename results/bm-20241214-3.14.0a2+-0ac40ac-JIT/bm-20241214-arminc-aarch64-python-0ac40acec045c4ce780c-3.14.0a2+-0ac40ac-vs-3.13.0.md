# Results vs. 3.13.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-aarch64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.021x slower
- HPT reliability: 90.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.18 sec: 1.07x slower                                                   |
| html5lib       | 65.6 ms                                                  | 71.4 ms: 1.09x slower                                                    |
| sphinx         | 1.20 sec                                                 | 1.26 sec: 1.05x slower                                                   |
| Geometric mean | (ref)                                                    | 1.06x slower                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 494 ms: 1.34x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 524 ms: 1.27x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 924 ms: 1.26x faster                                                     |
| async_tree_none            | 504 ms                                                   | 409 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 396 ms: 1.22x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 938 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 687 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 702 ms: 1.12x faster                                                     |
| async_generators           | 500 ms                                                   | 540 ms: 1.08x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.15x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.98 ms: 1.28x faster                                                    |
| regex_compile  | 134 ms                                                   | 145 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.52 sec: 1.06x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 416 us: 1.11x slower                                                     |
| Geometric mean      | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_process, json_loads, unpickle_pure_python, json_dumps

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
| genshi_text     | 28.6 ms                                                  | 34.5 ms: 1.21x slower                                                    |
| django_template | 39.4 ms                                                  | 49.1 ms: 1.25x slower                                                    |
| genshi_xml      | 61.6 ms                                                  | 80.3 ms: 1.30x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 494 ms: 1.34x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 40.1 us: 1.32x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.98 ms: 1.28x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 524 ms: 1.27x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 924 ms: 1.26x faster                                                     |
| deepcopy                   | 479 us                                                   | 383 us: 1.25x faster                                                     |
| async_tree_none            | 504 ms                                                   | 409 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 396 ms: 1.22x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 938 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 687 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 702 ms: 1.12x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                     |
| scimark_fft                | 463 ms                                                   | 427 ms: 1.08x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.82 ms: 1.07x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.52 sec: 1.06x faster                                                   |
| coverage                   | 106 ms                                                   | 100 ms: 1.06x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.80 sec: 1.04x faster                                                   |
| richards                   | 54.5 ms                                                  | 55.8 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                    |
| connected_components       | 547 ms                                                   | 564 ms: 1.03x slower                                                     |
| pyflate                    | 582 ms                                                   | 603 ms: 1.04x slower                                                     |
| mdp                        | 3.45 sec                                                 | 3.58 sec: 1.04x slower                                                   |
| sphinx                     | 1.20 sec                                                 | 1.26 sec: 1.05x slower                                                   |
| richards_super             | 60.8 ms                                                  | 64.6 ms: 1.06x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.62 ms: 1.07x slower                                                    |
| pycparser                  | 1.34 sec                                                 | 1.44 sec: 1.07x slower                                                   |
| sqlglot_normalize          | 131 ms                                                   | 140 ms: 1.07x slower                                                     |
| sympy_integrate            | 21.4 ms                                                  | 23.0 ms: 1.07x slower                                                    |
| meteor_contest             | 117 ms                                                   | 125 ms: 1.07x slower                                                     |
| docutils                   | 2.96 sec                                                 | 3.18 sec: 1.07x slower                                                   |
| async_generators           | 500 ms                                                   | 540 ms: 1.08x slower                                                     |
| logging_silent             | 135 ns                                                   | 145 ns: 1.08x slower                                                     |
| regex_compile              | 134 ms                                                   | 145 ms: 1.08x slower                                                     |
| deltablue                  | 3.97 ms                                                  | 4.30 ms: 1.08x slower                                                    |
| logging_format             | 8.10 us                                                  | 8.79 us: 1.08x slower                                                    |
| html5lib                   | 65.6 ms                                                  | 71.4 ms: 1.09x slower                                                    |
| fannkuch                   | 478 ms                                                   | 522 ms: 1.09x slower                                                     |
| logging_simple             | 7.25 us                                                  | 7.92 us: 1.09x slower                                                    |
| sympy_expand               | 472 ms                                                   | 517 ms: 1.09x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 92.9 ms: 1.09x slower                                                    |
| sqlglot_parse              | 1.43 ms                                                  | 1.59 ms: 1.11x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 416 us: 1.11x slower                                                     |
| typing_runtime_protocols   | 197 us                                                   | 222 us: 1.12x slower                                                     |
| sympy_str                  | 265 ms                                                   | 300 ms: 1.13x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.80 ms: 1.15x slower                                                    |
| raytrace                   | 310 ms                                                   | 363 ms: 1.17x slower                                                     |
| chaos                      | 70.7 ms                                                  | 84.6 ms: 1.20x slower                                                    |
| genshi_text                | 28.6 ms                                                  | 34.5 ms: 1.21x slower                                                    |
| comprehensions             | 20.8 us                                                  | 25.5 us: 1.22x slower                                                    |
| generators                 | 40.3 ms                                                  | 49.7 ms: 1.23x slower                                                    |
| django_template            | 39.4 ms                                                  | 49.1 ms: 1.25x slower                                                    |
| nqueens                    | 105 ms                                                   | 131 ms: 1.25x slower                                                     |
| hexiom                     | 7.34 ms                                                  | 9.28 ms: 1.26x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 80.3 ms: 1.30x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 26.6 ms: 1.31x slower                                                    |
| many_optionals             | 626 us                                                   | 841 us: 1.34x slower                                                     |
| pprint_pformat             | 1.99 sec                                                 | 2.69 sec: 1.36x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.31 sec: 1.36x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 1.51 sec: 187.54x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.09x slower                                                             |

Benchmark hidden because not significant (36): deepcopy_reduce, sqlalchemy_declarative, xml_etree_generate, scimark_sor, scimark_monte_carlo, k_core, json, xml_etree_process, pathlib, float, json_loads, nbody, djangocms, sqlite_synth, coroutines, thrift, unpickle_pure_python, asyncio_websockets, mako, json_dumps, regex_v8, scimark_lu, regex_dna, python_startup, 2to3, spectral_norm, shortest_path, pidigits, scimark_sparse_mat_mult, bench_thread_pool, go, sympy_sum, pylint, sqlglot_optimize, sqlalchemy_imperative, sqlglot_transpile
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.021x slower

# HPT report

- Reliability score: 90.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x