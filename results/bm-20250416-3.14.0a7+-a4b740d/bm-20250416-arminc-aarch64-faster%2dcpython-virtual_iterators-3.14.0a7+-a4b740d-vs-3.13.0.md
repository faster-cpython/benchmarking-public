# Results vs. 3.13.0

- fork: faster-cpython
- ref: virtual_iterators
- machine: linux-aarch64
- commit hash: a4b740d
- commit date: 2025-04-16
- overall geometric mean: 1.077x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 290 ms: 1.08x faster                                                            |
| docutils       | 2.96 sec                                                 | 2.89 sec: 1.03x faster                                                          |
| html5lib       | 65.6 ms                                                  | 62.2 ms: 1.05x faster                                                           |
| sphinx         | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                          |
| Geometric mean | (ref)                                                    | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 457 ms: 1.45x faster                                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 886 ms: 1.31x faster                                                            |
| async_tree_none            | 504 ms                                                   | 387 ms: 1.30x faster                                                            |
| async_tree_none_tg         | 484 ms                                                   | 375 ms: 1.29x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 884 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 646 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 657 ms: 1.20x faster                                                            |
| async_generators           | 500 ms                                                   | 450 ms: 1.11x faster                                                            |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 83.0 ms: 1.15x faster                                                           |
| Geometric mean | (ref)                                                    | 1.05x faster                                                                    |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.83 ms: 1.33x faster                                                           |
| regex_v8       | 32.5 ms                                                  | 28.1 ms: 1.16x faster                                                           |
| regex_compile  | 134 ms                                                   | 121 ms: 1.11x faster                                                            |
| regex_dna      | 263 ms                                                   | 241 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                    | 1.17x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|---------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 181 ms: 1.12x faster                                                            |
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                                            |
| tomli_loads         | 2.67 sec                                                 | 2.41 sec: 1.11x faster                                                          |
| xml_etree_process   | 82.1 ms                                                  | 79.2 ms: 1.04x faster                                                           |
| json_loads          | 32.8 us                                                  | 34.8 us: 1.06x slower                                                           |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                                    |

Benchmark hidden because not significant (4): xml_etree_generate, unpickle_pure_python, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.3 ms: 1.09x faster                                                           |
| genshi_xml     | 61.6 ms                                                  | 59.2 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                    |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.60 sec: 2.15x faster                                                          |
| deepcopy                   | 479 us                                                   | 326 us: 1.47x faster                                                            |
| async_tree_memoization     | 664 ms                                                   | 457 ms: 1.45x faster                                                            |
| deepcopy_memo              | 53.0 us                                                  | 36.6 us: 1.45x faster                                                           |
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                            |
| regex_effbot               | 5.10 ms                                                  | 3.83 ms: 1.33x faster                                                           |
| async_tree_io_tg           | 1.16 sec                                                 | 886 ms: 1.31x faster                                                            |
| async_tree_none            | 504 ms                                                   | 387 ms: 1.30x faster                                                            |
| async_tree_none_tg         | 484 ms                                                   | 375 ms: 1.29x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 884 ms: 1.29x faster                                                            |
| go                         | 164 ms                                                   | 130 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 646 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 657 ms: 1.20x faster                                                            |
| deepcopy_reduce            | 4.24 us                                                  | 3.58 us: 1.19x faster                                                           |
| regex_v8                   | 32.5 ms                                                  | 28.1 ms: 1.16x faster                                                           |
| float                      | 95.8 ms                                                  | 83.0 ms: 1.15x faster                                                           |
| scimark_monte_carlo        | 87.8 ms                                                  | 77.6 ms: 1.13x faster                                                           |
| spectral_norm              | 143 ms                                                   | 127 ms: 1.13x faster                                                            |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                                            |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                                            |
| scimark_sor                | 164 ms                                                   | 147 ms: 1.12x faster                                                            |
| scimark_fft                | 463 ms                                                   | 416 ms: 1.11x faster                                                            |
| async_generators           | 500 ms                                                   | 450 ms: 1.11x faster                                                            |
| telco                      | 10.5 ms                                                  | 9.44 ms: 1.11x faster                                                           |
| regex_compile              | 134 ms                                                   | 121 ms: 1.11x faster                                                            |
| tomli_loads                | 2.67 sec                                                 | 2.41 sec: 1.11x faster                                                          |
| generators                 | 40.3 ms                                                  | 36.6 ms: 1.10x faster                                                           |
| pathlib                    | 24.3 ms                                                  | 22.2 ms: 1.10x faster                                                           |
| pprint_pformat             | 1.99 sec                                                 | 1.82 sec: 1.09x faster                                                          |
| regex_dna                  | 263 ms                                                   | 241 ms: 1.09x faster                                                            |
| pycparser                  | 1.34 sec                                                 | 1.24 sec: 1.09x faster                                                          |
| pyflate                    | 582 ms                                                   | 536 ms: 1.09x faster                                                            |
| genshi_text                | 28.6 ms                                                  | 26.3 ms: 1.09x faster                                                           |
| sqlite_synth               | 4.08 us                                                  | 3.77 us: 1.08x faster                                                           |
| pprint_safe_repr           | 962 ms                                                   | 888 ms: 1.08x faster                                                            |
| 2to3                       | 313 ms                                                   | 290 ms: 1.08x faster                                                            |
| bpe_tokeniser              | 6.02 sec                                                 | 5.57 sec: 1.08x faster                                                          |
| k_core                     | 2.99 sec                                                 | 2.77 sec: 1.08x faster                                                          |
| nqueens                    | 105 ms                                                   | 97.4 ms: 1.08x faster                                                           |
| meteor_contest             | 117 ms                                                   | 109 ms: 1.08x faster                                                            |
| logging_format             | 8.10 us                                                  | 7.53 us: 1.08x faster                                                           |
| chaos                      | 70.7 ms                                                  | 66.3 ms: 1.07x faster                                                           |
| sphinx                     | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                          |
| logging_simple             | 7.25 us                                                  | 6.82 us: 1.06x faster                                                           |
| logging_silent             | 135 ns                                                   | 127 ns: 1.06x faster                                                            |
| typing_runtime_protocols   | 197 us                                                   | 186 us: 1.06x faster                                                            |
| html5lib                   | 65.6 ms                                                  | 62.2 ms: 1.05x faster                                                           |
| hexiom                     | 7.34 ms                                                  | 6.97 ms: 1.05x faster                                                           |
| richards                   | 54.5 ms                                                  | 52.0 ms: 1.05x faster                                                           |
| coverage                   | 106 ms                                                   | 101 ms: 1.05x faster                                                            |
| genshi_xml                 | 61.6 ms                                                  | 59.2 ms: 1.04x faster                                                           |
| xml_etree_process          | 82.1 ms                                                  | 79.2 ms: 1.04x faster                                                           |
| richards_super             | 60.8 ms                                                  | 58.7 ms: 1.04x faster                                                           |
| docutils                   | 2.96 sec                                                 | 2.89 sec: 1.03x faster                                                          |
| connected_components       | 547 ms                                                   | 560 ms: 1.02x slower                                                            |
| create_gc_cycles           | 3.39 ms                                                  | 3.59 ms: 1.06x slower                                                           |
| json_loads                 | 32.8 us                                                  | 34.8 us: 1.06x slower                                                           |
| gc_traversal               | 5.92 ms                                                  | 6.54 ms: 1.10x slower                                                           |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                           |
| subparsers                 | 20.3 ms                                                  | 25.5 ms: 1.26x slower                                                           |
| many_optionals             | 626 us                                                   | 824 us: 1.32x slower                                                            |
| bench_mp_pool              | 8.07 ms                                                  | 6.60 sec: 817.94x slower                                                        |
| Geometric mean             | (ref)                                                    | 1.00x faster                                                                    |

Benchmark hidden because not significant (23): xml_etree_generate, sqlalchemy_imperative, sqlalchemy_declarative, deltablue, comprehensions, crypto_pyaes, fannkuch, mako, unpickle_pure_python, json_dumps, json, pidigits, asyncio_websockets, pickle_pure_python, scimark_lu, django_template, nbody, bench_thread_pool, python_startup, coroutines, raytrace, shortest_path, scimark_sparse_mat_mult
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
Ignored benchmarks (5) of results/bm-20250416-3.14.0a7+-a4b740d/bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.077x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.04x