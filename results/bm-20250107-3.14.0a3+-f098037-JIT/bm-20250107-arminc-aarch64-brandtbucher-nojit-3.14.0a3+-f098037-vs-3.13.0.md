# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: linux-aarch64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.024x slower
- HPT reliability: 95.71%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 324 ms: 1.04x slower                                            |
| docutils       | 2.96 sec                                                 | 3.20 sec: 1.08x slower                                          |
| html5lib       | 65.6 ms                                                  | 72.8 ms: 1.11x slower                                           |
| sphinx         | 1.20 sec                                                 | 1.27 sec: 1.05x slower                                          |
| Geometric mean | (ref)                                                    | 1.07x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 491 ms: 1.35x faster                                            |
| async_tree_memoization     | 664 ms                                                   | 525 ms: 1.27x faster                                            |
| async_tree_none            | 504 ms                                                   | 404 ms: 1.25x faster                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 936 ms: 1.24x faster                                            |
| async_tree_io              | 1.14 sec                                                 | 933 ms: 1.22x faster                                            |
| async_tree_none_tg         | 484 ms                                                   | 400 ms: 1.21x faster                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 686 ms: 1.17x faster                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 698 ms: 1.13x faster                                            |
| async_generators           | 500 ms                                                   | 534 ms: 1.07x slower                                            |
| Geometric mean             | (ref)                                                    | 1.15x faster                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 90.9 ms: 1.05x faster                                           |
| Geometric mean | (ref)                                                    | 1.03x faster                                                    |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.98 ms: 1.28x faster                                           |
| regex_dna      | 263 ms                                                   | 255 ms: 1.03x faster                                            |
| Geometric mean | (ref)                                                    | 1.06x faster                                                    |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                            |
| xml_etree_parse     | 203 ms                                                   | 183 ms: 1.11x faster                                            |
| tomli_loads         | 2.67 sec                                                 | 2.54 sec: 1.05x faster                                          |
| pickle_pure_python  | 374 us                                                   | 412 us: 1.10x slower                                            |
| Geometric mean      | (ref)                                                    | 1.02x faster                                                    |

Benchmark hidden because not significant (5): json_loads, unpickle_pure_python, xml_etree_process, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.16 ms: 1.04x slower                                           |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 34.3 ms: 1.20x slower                                           |
| django_template | 39.4 ms                                                  | 48.4 ms: 1.23x slower                                           |
| genshi_xml      | 61.6 ms                                                  | 82.7 ms: 1.34x slower                                           |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 491 ms: 1.35x faster                                            |
| deepcopy_memo              | 53.0 us                                                  | 40.2 us: 1.32x faster                                           |
| regex_effbot               | 5.10 ms                                                  | 3.98 ms: 1.28x faster                                           |
| async_tree_memoization     | 664 ms                                                   | 525 ms: 1.27x faster                                            |
| async_tree_none            | 504 ms                                                   | 404 ms: 1.25x faster                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 936 ms: 1.24x faster                                            |
| deepcopy                   | 479 us                                                   | 392 us: 1.22x faster                                            |
| async_tree_io              | 1.14 sec                                                 | 933 ms: 1.22x faster                                            |
| async_tree_none_tg         | 484 ms                                                   | 400 ms: 1.21x faster                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 686 ms: 1.17x faster                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 698 ms: 1.13x faster                                            |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                            |
| xml_etree_parse            | 203 ms                                                   | 183 ms: 1.11x faster                                            |
| telco                      | 10.5 ms                                                  | 9.52 ms: 1.10x faster                                           |
| scimark_fft                | 463 ms                                                   | 422 ms: 1.10x faster                                            |
| pathlib                    | 24.3 ms                                                  | 22.3 ms: 1.09x faster                                           |
| float                      | 95.8 ms                                                  | 90.9 ms: 1.05x faster                                           |
| tomli_loads                | 2.67 sec                                                 | 2.54 sec: 1.05x faster                                          |
| regex_dna                  | 263 ms                                                   | 255 ms: 1.03x faster                                            |
| bpe_tokeniser              | 6.02 sec                                                 | 5.87 sec: 1.03x faster                                          |
| pyflate                    | 582 ms                                                   | 599 ms: 1.03x slower                                            |
| 2to3                       | 313 ms                                                   | 324 ms: 1.04x slower                                            |
| python_startup_no_site     | 8.79 ms                                                  | 9.16 ms: 1.04x slower                                           |
| shortest_path              | 565 ms                                                   | 589 ms: 1.04x slower                                            |
| mdp                        | 3.45 sec                                                 | 3.60 sec: 1.05x slower                                          |
| create_gc_cycles           | 3.39 ms                                                  | 3.56 ms: 1.05x slower                                           |
| sphinx                     | 1.20 sec                                                 | 1.27 sec: 1.05x slower                                          |
| sqlglot_normalize          | 131 ms                                                   | 139 ms: 1.06x slower                                            |
| fannkuch                   | 478 ms                                                   | 507 ms: 1.06x slower                                            |
| sqlglot_optimize           | 65.2 ms                                                  | 69.6 ms: 1.07x slower                                           |
| async_generators           | 500 ms                                                   | 534 ms: 1.07x slower                                            |
| docutils                   | 2.96 sec                                                 | 3.20 sec: 1.08x slower                                          |
| meteor_contest             | 117 ms                                                   | 126 ms: 1.08x slower                                            |
| sqlalchemy_imperative      | 16.1 ms                                                  | 17.4 ms: 1.08x slower                                           |
| logging_silent             | 135 ns                                                   | 147 ns: 1.09x slower                                            |
| pycparser                  | 1.34 sec                                                 | 1.47 sec: 1.09x slower                                          |
| typing_runtime_protocols   | 197 us                                                   | 215 us: 1.09x slower                                            |
| crypto_pyaes               | 84.9 ms                                                  | 92.9 ms: 1.09x slower                                           |
| logging_format             | 8.10 us                                                  | 8.87 us: 1.10x slower                                           |
| pickle_pure_python         | 374 us                                                   | 412 us: 1.10x slower                                            |
| sympy_sum                  | 151 ms                                                   | 167 ms: 1.11x slower                                            |
| html5lib                   | 65.6 ms                                                  | 72.8 ms: 1.11x slower                                           |
| logging_simple             | 7.25 us                                                  | 8.08 us: 1.11x slower                                           |
| sympy_integrate            | 21.4 ms                                                  | 24.0 ms: 1.12x slower                                           |
| sqlglot_parse              | 1.43 ms                                                  | 1.61 ms: 1.12x slower                                           |
| sympy_expand               | 472 ms                                                   | 531 ms: 1.12x slower                                            |
| deltablue                  | 3.97 ms                                                  | 4.56 ms: 1.15x slower                                           |
| sympy_str                  | 265 ms                                                   | 309 ms: 1.17x slower                                            |
| gc_traversal               | 5.92 ms                                                  | 6.94 ms: 1.17x slower                                           |
| chaos                      | 70.7 ms                                                  | 83.5 ms: 1.18x slower                                           |
| raytrace                   | 310 ms                                                   | 368 ms: 1.19x slower                                            |
| comprehensions             | 20.8 us                                                  | 24.9 us: 1.20x slower                                           |
| genshi_text                | 28.6 ms                                                  | 34.3 ms: 1.20x slower                                           |
| nqueens                    | 105 ms                                                   | 127 ms: 1.21x slower                                            |
| django_template            | 39.4 ms                                                  | 48.4 ms: 1.23x slower                                           |
| generators                 | 40.3 ms                                                  | 50.6 ms: 1.25x slower                                           |
| pprint_safe_repr           | 962 ms                                                   | 1.24 sec: 1.29x slower                                          |
| pprint_pformat             | 1.99 sec                                                 | 2.58 sec: 1.30x slower                                          |
| hexiom                     | 7.34 ms                                                  | 9.60 ms: 1.31x slower                                           |
| genshi_xml                 | 61.6 ms                                                  | 82.7 ms: 1.34x slower                                           |
| subparsers                 | 20.3 ms                                                  | 27.3 ms: 1.34x slower                                           |
| many_optionals             | 626 us                                                   | 867 us: 1.38x slower                                            |
| bench_mp_pool              | 8.07 ms                                                  | 1.51 sec: 186.73x slower                                        |
| Geometric mean             | (ref)                                                    | 1.09x slower                                                    |

Benchmark hidden because not significant (32): deepcopy_reduce, scimark_monte_carlo, nbody, json_loads, json, spectral_norm, regex_v8, k_core, scimark_sor, unpickle_pure_python, thrift, xml_etree_process, mako, xml_etree_generate, pylint, connected_components, asyncio_websockets, sqlite_synth, scimark_sparse_mat_mult, json_dumps, pidigits, coroutines, python_startup, bench_thread_pool, richards, sqlglot_transpile, coverage, regex_compile, richards_super, go, sqlalchemy_declarative, scimark_lu
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.024x slower

# HPT report

- Reliability score: 95.71% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x