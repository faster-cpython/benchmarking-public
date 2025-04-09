# Results vs. 3.13.0

- fork: faster-cpython
- ref: tstate_in_dealloc
- machine: linux-aarch64
- commit hash: 49ac4ce
- commit date: 2025-04-09
- overall geometric mean: 1.060x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 300 ms: 1.04x faster                                                            |
| docutils       | 2.96 sec                                                 | 2.92 sec: 1.01x faster                                                          |
| html5lib       | 65.6 ms                                                  | 63.2 ms: 1.04x faster                                                           |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                          |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 464 ms: 1.43x faster                                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 465 ms: 1.42x faster                                                            |
| async_tree_none_tg         | 484 ms                                                   | 367 ms: 1.32x faster                                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 893 ms: 1.30x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 878 ms: 1.30x faster                                                            |
| async_tree_none            | 504 ms                                                   | 389 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 646 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 665 ms: 1.19x faster                                                            |
| async_generators           | 500 ms                                                   | 462 ms: 1.08x faster                                                            |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.0 ms: 1.11x faster                                                           |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                    |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.94 ms: 1.30x faster                                                           |
| regex_v8       | 32.5 ms                                                  | 28.0 ms: 1.16x faster                                                           |
| regex_dna      | 263 ms                                                   | 242 ms: 1.08x faster                                                            |
| regex_compile  | 134 ms                                                   | 123 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                    | 1.15x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|---------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 175 ms: 1.16x faster                                                            |
| xml_etree_iterparse | 159 ms                                                   | 141 ms: 1.12x faster                                                            |
| tomli_loads         | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                          |
| json_loads          | 32.8 us                                                  | 34.9 us: 1.06x slower                                                           |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                                    |

Benchmark hidden because not significant (5): xml_etree_generate, json_dumps, xml_etree_process, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.15x slower                                                           |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.66 sec: 2.08x faster                                                          |
| deepcopy                   | 479 us                                                   | 328 us: 1.46x faster                                                            |
| async_tree_memoization     | 664 ms                                                   | 464 ms: 1.43x faster                                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 465 ms: 1.42x faster                                                            |
| deepcopy_memo              | 53.0 us                                                  | 38.0 us: 1.40x faster                                                           |
| async_tree_none_tg         | 484 ms                                                   | 367 ms: 1.32x faster                                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 893 ms: 1.30x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 878 ms: 1.30x faster                                                            |
| regex_effbot               | 5.10 ms                                                  | 3.94 ms: 1.30x faster                                                           |
| async_tree_none            | 504 ms                                                   | 389 ms: 1.29x faster                                                            |
| go                         | 164 ms                                                   | 132 ms: 1.25x faster                                                            |
| deepcopy_reduce            | 4.24 us                                                  | 3.42 us: 1.24x faster                                                           |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 646 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 665 ms: 1.19x faster                                                            |
| regex_v8                   | 32.5 ms                                                  | 28.0 ms: 1.16x faster                                                           |
| xml_etree_parse            | 203 ms                                                   | 175 ms: 1.16x faster                                                            |
| spectral_norm              | 143 ms                                                   | 126 ms: 1.14x faster                                                            |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.12x faster                                                            |
| generators                 | 40.3 ms                                                  | 36.0 ms: 1.12x faster                                                           |
| telco                      | 10.5 ms                                                  | 9.37 ms: 1.12x faster                                                           |
| float                      | 95.8 ms                                                  | 86.0 ms: 1.11x faster                                                           |
| scimark_sor                | 164 ms                                                   | 149 ms: 1.11x faster                                                            |
| tomli_loads                | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                          |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.6 ms: 1.09x faster                                                           |
| regex_dna                  | 263 ms                                                   | 242 ms: 1.08x faster                                                            |
| regex_compile              | 134 ms                                                   | 123 ms: 1.08x faster                                                            |
| async_generators           | 500 ms                                                   | 462 ms: 1.08x faster                                                            |
| bpe_tokeniser              | 6.02 sec                                                 | 5.56 sec: 1.08x faster                                                          |
| pylint                     | 345 ms                                                   | 321 ms: 1.07x faster                                                            |
| sympy_sum                  | 151 ms                                                   | 141 ms: 1.07x faster                                                            |
| pycparser                  | 1.34 sec                                                 | 1.26 sec: 1.07x faster                                                          |
| scimark_fft                | 463 ms                                                   | 433 ms: 1.07x faster                                                            |
| pprint_pformat             | 1.99 sec                                                 | 1.86 sec: 1.07x faster                                                          |
| pprint_safe_repr           | 962 ms                                                   | 902 ms: 1.07x faster                                                            |
| sympy_integrate            | 21.4 ms                                                  | 20.1 ms: 1.07x faster                                                           |
| pyflate                    | 582 ms                                                   | 547 ms: 1.06x faster                                                            |
| pathlib                    | 24.3 ms                                                  | 22.9 ms: 1.06x faster                                                           |
| sqlite_synth               | 4.08 us                                                  | 3.85 us: 1.06x faster                                                           |
| k_core                     | 2.99 sec                                                 | 2.82 sec: 1.06x faster                                                          |
| logging_silent             | 135 ns                                                   | 127 ns: 1.06x faster                                                            |
| richards                   | 54.5 ms                                                  | 51.8 ms: 1.05x faster                                                           |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                          |
| scimark_lu                 | 146 ms                                                   | 140 ms: 1.04x faster                                                            |
| 2to3                       | 313 ms                                                   | 300 ms: 1.04x faster                                                            |
| chaos                      | 70.7 ms                                                  | 67.8 ms: 1.04x faster                                                           |
| logging_format             | 8.10 us                                                  | 7.79 us: 1.04x faster                                                           |
| html5lib                   | 65.6 ms                                                  | 63.2 ms: 1.04x faster                                                           |
| docutils                   | 2.96 sec                                                 | 2.92 sec: 1.01x faster                                                          |
| shortest_path              | 565 ms                                                   | 576 ms: 1.02x slower                                                            |
| raytrace                   | 310 ms                                                   | 324 ms: 1.05x slower                                                            |
| json_loads                 | 32.8 us                                                  | 34.9 us: 1.06x slower                                                           |
| create_gc_cycles           | 3.39 ms                                                  | 3.64 ms: 1.07x slower                                                           |
| gc_traversal               | 5.92 ms                                                  | 6.72 ms: 1.13x slower                                                           |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.15x slower                                                           |
| subparsers                 | 20.3 ms                                                  | 25.5 ms: 1.26x slower                                                           |
| many_optionals             | 626 us                                                   | 821 us: 1.31x slower                                                            |
| bench_mp_pool              | 8.07 ms                                                  | 2.46 sec: 305.09x slower                                                        |
| Geometric mean             | (ref)                                                    | 1.00x faster                                                                    |

Benchmark hidden because not significant (33): nqueens, xml_etree_generate, genshi_text, richards_super, deltablue, sqlalchemy_declarative, meteor_contest, sympy_expand, sqlalchemy_imperative, logging_simple, coverage, json_dumps, xml_etree_process, asyncio_websockets, hexiom, pidigits, pickle_pure_python, fannkuch, typing_runtime_protocols, python_startup, genshi_xml, connected_components, json, mako, sympy_str, bench_thread_pool, django_template, unpickle_pure_python, crypto_pyaes, scimark_sparse_mat_mult, coroutines, comprehensions, nbody
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (5) of results/bm-20250409-3.14.0a7+-49ac4ce/bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x