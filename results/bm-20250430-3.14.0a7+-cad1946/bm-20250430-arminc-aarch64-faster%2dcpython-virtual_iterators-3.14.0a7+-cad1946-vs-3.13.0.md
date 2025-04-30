# Results vs. 3.13.0

- fork: faster-cpython
- ref: virtual_iterators
- machine: linux-aarch64
- commit hash: cad1946
- commit date: 2025-04-30
- overall geometric mean: 1.065x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 294 ms: 1.06x faster                                                            |
| docutils       | 2.96 sec                                                 | 2.91 sec: 1.02x faster                                                          |
| html5lib       | 65.6 ms                                                  | 63.2 ms: 1.04x faster                                                           |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                          |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 459 ms: 1.45x faster                                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                            |
| async_tree_none            | 504 ms                                                   | 381 ms: 1.32x faster                                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 886 ms: 1.31x faster                                                            |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 882 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 656 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 663 ms: 1.19x faster                                                            |
| async_generators           | 500 ms                                                   | 450 ms: 1.11x faster                                                            |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.9 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                    |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.81 ms: 1.34x faster                                                           |
| regex_v8       | 32.5 ms                                                  | 28.3 ms: 1.15x faster                                                           |
| regex_compile  | 134 ms                                                   | 120 ms: 1.11x faster                                                            |
| regex_dna      | 263 ms                                                   | 241 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                    | 1.17x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|---------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 182 ms: 1.11x faster                                                            |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.11x faster                                                            |
| tomli_loads         | 2.67 sec                                                 | 2.43 sec: 1.10x faster                                                          |
| xml_etree_generate  | 118 ms                                                   | 112 ms: 1.06x faster                                                            |
| xml_etree_process   | 82.1 ms                                                  | 79.2 ms: 1.04x faster                                                           |
| json_loads          | 32.8 us                                                  | 35.4 us: 1.08x slower                                                           |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                                    |

Benchmark hidden because not significant (3): json_dumps, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.64 sec: 2.11x faster                                                          |
| deepcopy                   | 479 us                                                   | 325 us: 1.47x faster                                                            |
| async_tree_memoization     | 664 ms                                                   | 459 ms: 1.45x faster                                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                            |
| deepcopy_memo              | 53.0 us                                                  | 37.6 us: 1.41x faster                                                           |
| regex_effbot               | 5.10 ms                                                  | 3.81 ms: 1.34x faster                                                           |
| async_tree_none            | 504 ms                                                   | 381 ms: 1.32x faster                                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 886 ms: 1.31x faster                                                            |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 882 ms: 1.29x faster                                                            |
| go                         | 164 ms                                                   | 128 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 656 ms: 1.22x faster                                                            |
| deepcopy_reduce            | 4.24 us                                                  | 3.54 us: 1.20x faster                                                           |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 663 ms: 1.19x faster                                                            |
| regex_v8                   | 32.5 ms                                                  | 28.3 ms: 1.15x faster                                                           |
| float                      | 95.8 ms                                                  | 85.9 ms: 1.12x faster                                                           |
| pathlib                    | 24.3 ms                                                  | 21.8 ms: 1.11x faster                                                           |
| xml_etree_parse            | 203 ms                                                   | 182 ms: 1.11x faster                                                            |
| async_generators           | 500 ms                                                   | 450 ms: 1.11x faster                                                            |
| regex_compile              | 134 ms                                                   | 120 ms: 1.11x faster                                                            |
| scimark_sor                | 164 ms                                                   | 148 ms: 1.11x faster                                                            |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.11x faster                                                            |
| bpe_tokeniser              | 6.02 sec                                                 | 5.45 sec: 1.10x faster                                                          |
| spectral_norm              | 143 ms                                                   | 130 ms: 1.10x faster                                                            |
| generators                 | 40.3 ms                                                  | 36.6 ms: 1.10x faster                                                           |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.0 ms: 1.10x faster                                                           |
| tomli_loads                | 2.67 sec                                                 | 2.43 sec: 1.10x faster                                                          |
| regex_dna                  | 263 ms                                                   | 241 ms: 1.09x faster                                                            |
| pycparser                  | 1.34 sec                                                 | 1.24 sec: 1.09x faster                                                          |
| pprint_pformat             | 1.99 sec                                                 | 1.84 sec: 1.08x faster                                                          |
| telco                      | 10.5 ms                                                  | 9.73 ms: 1.07x faster                                                           |
| pprint_safe_repr           | 962 ms                                                   | 899 ms: 1.07x faster                                                            |
| k_core                     | 2.99 sec                                                 | 2.79 sec: 1.07x faster                                                          |
| hexiom                     | 7.34 ms                                                  | 6.87 ms: 1.07x faster                                                           |
| logging_format             | 8.10 us                                                  | 7.62 us: 1.06x faster                                                           |
| 2to3                       | 313 ms                                                   | 294 ms: 1.06x faster                                                            |
| nqueens                    | 105 ms                                                   | 98.9 ms: 1.06x faster                                                           |
| pyflate                    | 582 ms                                                   | 549 ms: 1.06x faster                                                            |
| xml_etree_generate         | 118 ms                                                   | 112 ms: 1.06x faster                                                            |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                          |
| logging_simple             | 7.25 us                                                  | 6.92 us: 1.05x faster                                                           |
| richards                   | 54.5 ms                                                  | 52.2 ms: 1.04x faster                                                           |
| scimark_fft                | 463 ms                                                   | 444 ms: 1.04x faster                                                            |
| html5lib                   | 65.6 ms                                                  | 63.2 ms: 1.04x faster                                                           |
| xml_etree_process          | 82.1 ms                                                  | 79.2 ms: 1.04x faster                                                           |
| logging_silent             | 135 ns                                                   | 131 ns: 1.03x faster                                                            |
| docutils                   | 2.96 sec                                                 | 2.91 sec: 1.02x faster                                                          |
| connected_components       | 547 ms                                                   | 557 ms: 1.02x slower                                                            |
| shortest_path              | 565 ms                                                   | 585 ms: 1.03x slower                                                            |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.99 ms: 1.05x slower                                                           |
| raytrace                   | 310 ms                                                   | 326 ms: 1.05x slower                                                            |
| create_gc_cycles           | 3.39 ms                                                  | 3.59 ms: 1.06x slower                                                           |
| json_loads                 | 32.8 us                                                  | 35.4 us: 1.08x slower                                                           |
| gc_traversal               | 5.92 ms                                                  | 6.53 ms: 1.10x slower                                                           |
| subparsers                 | 20.3 ms                                                  | 26.1 ms: 1.28x slower                                                           |
| many_optionals             | 626 us                                                   | 825 us: 1.32x slower                                                            |
| bench_mp_pool              | 8.07 ms                                                  | 1.87 sec: 231.18x slower                                                        |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                                    |

Benchmark hidden because not significant (28): meteor_contest, richards_super, sqlite_synth, comprehensions, genshi_text, coverage, chaos, pidigits, sqlalchemy_declarative, python_startup_no_site, deltablue, asyncio_websockets, genshi_xml, scimark_lu, json_dumps, crypto_pyaes, typing_runtime_protocols, unpickle_pure_python, python_startup, sqlalchemy_imperative, json, fannkuch, pickle_pure_python, mako, django_template, coroutines, bench_thread_pool, nbody
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
Ignored benchmarks (5) of results/bm-20250430-3.14.0a7+-cad1946/bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.065x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.04x