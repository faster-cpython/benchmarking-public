# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-aarch64
- commit hash: a684067
- commit date: 2025-05-28
- overall geometric mean: 1.025x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 302 ms: 1.04x faster                                                              |
| html5lib       | 65.6 ms                                                  | 61.1 ms: 1.07x faster                                                             |
| sphinx         | 1.20 sec                                                 | 1.13 sec: 1.07x faster                                                            |
| Geometric mean | (ref)                                                    | 1.05x faster                                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 464 ms: 1.43x faster                                                              |
| async_tree_none            | 504 ms                                                   | 387 ms: 1.30x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 372 ms: 1.30x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 879 ms: 1.30x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 904 ms: 1.29x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 654 ms: 1.22x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 660 ms: 1.20x faster                                                              |
| async_generators           | 500 ms                                                   | 450 ms: 1.11x faster                                                              |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                                      |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 87.5 ms: 1.09x faster                                                             |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                             |
| regex_v8       | 32.5 ms                                                  | 27.4 ms: 1.19x faster                                                             |
| regex_dna      | 263 ms                                                   | 229 ms: 1.15x faster                                                              |
| regex_compile  | 134 ms                                                   | 121 ms: 1.10x faster                                                              |
| Geometric mean | (ref)                                                    | 1.19x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                              |
| xml_etree_parse     | 203 ms                                                   | 184 ms: 1.10x faster                                                              |
| tomli_loads         | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                            |
| xml_etree_process   | 82.1 ms                                                  | 78.6 ms: 1.04x faster                                                             |
| json_loads          | 32.8 us                                                  | 35.3 us: 1.08x slower                                                             |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                                      |

Benchmark hidden because not significant (4): xml_etree_generate, json_dumps, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 27.0 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (3): genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.71 sec: 2.01x faster                                                            |
| deepcopy                   | 479 us                                                   | 328 us: 1.46x faster                                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 464 ms: 1.43x faster                                                              |
| deepcopy_memo              | 53.0 us                                                  | 37.6 us: 1.41x faster                                                             |
| regex_effbot               | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                             |
| async_tree_none            | 504 ms                                                   | 387 ms: 1.30x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 372 ms: 1.30x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 879 ms: 1.30x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 904 ms: 1.29x faster                                                              |
| go                         | 164 ms                                                   | 129 ms: 1.27x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 654 ms: 1.22x faster                                                              |
| deepcopy_reduce            | 4.24 us                                                  | 3.53 us: 1.20x faster                                                             |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 660 ms: 1.20x faster                                                              |
| regex_v8                   | 32.5 ms                                                  | 27.4 ms: 1.19x faster                                                             |
| regex_dna                  | 263 ms                                                   | 229 ms: 1.15x faster                                                              |
| scimark_sor                | 164 ms                                                   | 145 ms: 1.14x faster                                                              |
| spectral_norm              | 143 ms                                                   | 128 ms: 1.12x faster                                                              |
| telco                      | 10.5 ms                                                  | 9.38 ms: 1.11x faster                                                             |
| pylint                     | 345 ms                                                   | 310 ms: 1.11x faster                                                              |
| bpe_tokeniser              | 6.02 sec                                                 | 5.40 sec: 1.11x faster                                                            |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                              |
| async_generators           | 500 ms                                                   | 450 ms: 1.11x faster                                                              |
| regex_compile              | 134 ms                                                   | 121 ms: 1.10x faster                                                              |
| xml_etree_parse            | 203 ms                                                   | 184 ms: 1.10x faster                                                              |
| generators                 | 40.3 ms                                                  | 36.7 ms: 1.10x faster                                                             |
| float                      | 95.8 ms                                                  | 87.5 ms: 1.09x faster                                                             |
| tomli_loads                | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                            |
| scimark_monte_carlo        | 87.8 ms                                                  | 81.1 ms: 1.08x faster                                                             |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.08x faster                                                            |
| pyflate                    | 582 ms                                                   | 541 ms: 1.08x faster                                                              |
| html5lib                   | 65.6 ms                                                  | 61.1 ms: 1.07x faster                                                             |
| sympy_sum                  | 151 ms                                                   | 141 ms: 1.07x faster                                                              |
| nqueens                    | 105 ms                                                   | 98.1 ms: 1.07x faster                                                             |
| sqlite_synth               | 4.08 us                                                  | 3.83 us: 1.07x faster                                                             |
| richards                   | 54.5 ms                                                  | 51.1 ms: 1.07x faster                                                             |
| sphinx                     | 1.20 sec                                                 | 1.13 sec: 1.07x faster                                                            |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                             |
| sympy_integrate            | 21.4 ms                                                  | 20.3 ms: 1.06x faster                                                             |
| genshi_text                | 28.6 ms                                                  | 27.0 ms: 1.06x faster                                                             |
| richards_super             | 60.8 ms                                                  | 57.7 ms: 1.05x faster                                                             |
| scimark_fft                | 463 ms                                                   | 439 ms: 1.05x faster                                                              |
| xml_etree_process          | 82.1 ms                                                  | 78.6 ms: 1.04x faster                                                             |
| k_core                     | 2.99 sec                                                 | 2.87 sec: 1.04x faster                                                            |
| meteor_contest             | 117 ms                                                   | 112 ms: 1.04x faster                                                              |
| 2to3                       | 313 ms                                                   | 302 ms: 1.04x faster                                                              |
| pprint_safe_repr           | 962 ms                                                   | 985 ms: 1.02x slower                                                              |
| shortest_path              | 565 ms                                                   | 579 ms: 1.03x slower                                                              |
| connected_components       | 547 ms                                                   | 562 ms: 1.03x slower                                                              |
| logging_format             | 8.10 us                                                  | 8.41 us: 1.04x slower                                                             |
| raytrace                   | 310 ms                                                   | 328 ms: 1.06x slower                                                              |
| logging_simple             | 7.25 us                                                  | 7.70 us: 1.06x slower                                                             |
| json_loads                 | 32.8 us                                                  | 35.3 us: 1.08x slower                                                             |
| create_gc_cycles           | 3.39 ms                                                  | 3.78 ms: 1.11x slower                                                             |
| gc_traversal               | 5.92 ms                                                  | 6.97 ms: 1.18x slower                                                             |
| many_optionals             | 626 us                                                   | 872 us: 1.39x slower                                                              |
| subparsers                 | 20.3 ms                                                  | 28.5 ms: 1.40x slower                                                             |
| logging_silent             | 135 ns                                                   | 628 ns: 4.67x slower                                                              |
| coverage                   | 106 ms                                                   | 553 ms: 5.23x slower                                                              |
| thrift                     | 1.01 ms                                                  | 193 ms: 190.68x slower                                                            |
| bench_mp_pool              | 8.07 ms                                                  | 2.26 sec: 280.02x slower                                                          |
| Geometric mean             | (ref)                                                    | 1.10x slower                                                                      |

Benchmark hidden because not significant (28): pathlib, xml_etree_generate, hexiom, crypto_pyaes, sympy_expand, chaos, json_dumps, fannkuch, python_startup_no_site, asyncio_websockets, docutils, pidigits, comprehensions, genshi_xml, django_template, scimark_lu, mako, deltablue, unpickle_pure_python, nbody, pprint_pformat, sympy_str, coroutines, json, typing_runtime_protocols, scimark_sparse_mat_mult, bench_thread_pool, pickle_pure_python
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250528-3.15.0a0-a684067/bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.025x slower

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x