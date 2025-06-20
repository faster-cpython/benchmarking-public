# Results vs. 3.13.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-aarch64
- commit hash: 494c825
- commit date: 2025-06-20
- overall geometric mean: 1.052x faster
- HPT reliability: 99.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 301 ms: 1.04x faster                                                              |
| html5lib       | 65.6 ms                                                  | 62.2 ms: 1.05x faster                                                             |
| sphinx         | 1.20 sec                                                 | 1.15 sec: 1.05x faster                                                            |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 469 ms: 1.41x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.41x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 891 ms: 1.28x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 380 ms: 1.27x faster                                                              |
| async_tree_none            | 504 ms                                                   | 398 ms: 1.27x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 925 ms: 1.26x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 658 ms: 1.22x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 667 ms: 1.18x faster                                                              |
| async_generators           | 500 ms                                                   | 456 ms: 1.10x faster                                                              |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                                      |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 87.2 ms: 1.10x faster                                                             |
| nbody          | 118 ms                                                   | 129 ms: 1.09x slower                                                              |
| Geometric mean | (ref)                                                    | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.86 ms: 1.32x faster                                                             |
| regex_dna      | 263 ms                                                   | 219 ms: 1.20x faster                                                              |
| regex_v8       | 32.5 ms                                                  | 28.6 ms: 1.14x faster                                                             |
| regex_compile  | 134 ms                                                   | 124 ms: 1.08x faster                                                              |
| Geometric mean | (ref)                                                    | 1.18x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 179 ms: 1.13x faster                                                              |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                              |
| tomli_loads         | 2.67 sec                                                 | 2.47 sec: 1.08x faster                                                            |
| pickle_pure_python  | 374 us                                                   | 412 us: 1.10x slower                                                              |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                                      |

Benchmark hidden because not significant (5): json_dumps, xml_etree_generate, json_loads, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                             |
| python_startup_no_site | 8.79 ms                                                  | 8.63 ms: 1.02x faster                                                             |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 14.4 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                    | 1.02x slower                                                                      |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 469 ms: 1.41x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.41x faster                                                              |
| deepcopy                   | 479 us                                                   | 341 us: 1.40x faster                                                              |
| deepcopy_memo              | 53.0 us                                                  | 40.0 us: 1.33x faster                                                             |
| regex_effbot               | 5.10 ms                                                  | 3.86 ms: 1.32x faster                                                             |
| async_tree_io              | 1.14 sec                                                 | 891 ms: 1.28x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 380 ms: 1.27x faster                                                              |
| async_tree_none            | 504 ms                                                   | 398 ms: 1.27x faster                                                              |
| go                         | 164 ms                                                   | 130 ms: 1.26x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 925 ms: 1.26x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 658 ms: 1.22x faster                                                              |
| regex_dna                  | 263 ms                                                   | 219 ms: 1.20x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 667 ms: 1.18x faster                                                              |
| spectral_norm              | 143 ms                                                   | 122 ms: 1.17x faster                                                              |
| deepcopy_reduce            | 4.24 us                                                  | 3.70 us: 1.15x faster                                                             |
| generators                 | 40.3 ms                                                  | 35.1 ms: 1.15x faster                                                             |
| regex_v8                   | 32.5 ms                                                  | 28.6 ms: 1.14x faster                                                             |
| scimark_sor                | 164 ms                                                   | 145 ms: 1.13x faster                                                              |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                                              |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                              |
| pyflate                    | 582 ms                                                   | 526 ms: 1.11x faster                                                              |
| telco                      | 10.5 ms                                                  | 9.50 ms: 1.10x faster                                                             |
| float                      | 95.8 ms                                                  | 87.2 ms: 1.10x faster                                                             |
| async_generators           | 500 ms                                                   | 456 ms: 1.10x faster                                                              |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.3 ms: 1.09x faster                                                             |
| pylint                     | 345 ms                                                   | 318 ms: 1.08x faster                                                              |
| sqlite_synth               | 4.08 us                                                  | 3.77 us: 1.08x faster                                                             |
| bpe_tokeniser              | 6.02 sec                                                 | 5.57 sec: 1.08x faster                                                            |
| regex_compile              | 134 ms                                                   | 124 ms: 1.08x faster                                                              |
| tomli_loads                | 2.67 sec                                                 | 2.47 sec: 1.08x faster                                                            |
| k_core                     | 2.99 sec                                                 | 2.78 sec: 1.08x faster                                                            |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.07x faster                                                            |
| python_startup             | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                             |
| scimark_fft                | 463 ms                                                   | 433 ms: 1.07x faster                                                              |
| pathlib                    | 24.3 ms                                                  | 22.9 ms: 1.06x faster                                                             |
| nqueens                    | 105 ms                                                   | 99.5 ms: 1.05x faster                                                             |
| html5lib                   | 65.6 ms                                                  | 62.2 ms: 1.05x faster                                                             |
| hexiom                     | 7.34 ms                                                  | 6.99 ms: 1.05x faster                                                             |
| sphinx                     | 1.20 sec                                                 | 1.15 sec: 1.05x faster                                                            |
| 2to3                       | 313 ms                                                   | 301 ms: 1.04x faster                                                              |
| coverage                   | 106 ms                                                   | 102 ms: 1.04x faster                                                              |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                             |
| python_startup_no_site     | 8.79 ms                                                  | 8.63 ms: 1.02x faster                                                             |
| sympy_str                  | 265 ms                                                   | 267 ms: 1.01x slower                                                              |
| mako                       | 14.0 ms                                                  | 14.4 ms: 1.03x slower                                                             |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.95 ms: 1.04x slower                                                             |
| logging_format             | 8.10 us                                                  | 8.57 us: 1.06x slower                                                             |
| pprint_pformat             | 1.99 sec                                                 | 2.11 sec: 1.06x slower                                                            |
| pprint_safe_repr           | 962 ms                                                   | 1.03 sec: 1.07x slower                                                            |
| raytrace                   | 310 ms                                                   | 336 ms: 1.08x slower                                                              |
| nbody                      | 118 ms                                                   | 129 ms: 1.09x slower                                                              |
| logging_simple             | 7.25 us                                                  | 7.93 us: 1.09x slower                                                             |
| pickle_pure_python         | 374 us                                                   | 412 us: 1.10x slower                                                              |
| create_gc_cycles           | 3.39 ms                                                  | 3.75 ms: 1.11x slower                                                             |
| gc_traversal               | 5.92 ms                                                  | 6.72 ms: 1.13x slower                                                             |
| many_optionals             | 626 us                                                   | 776 us: 1.24x slower                                                              |
| subparsers                 | 20.3 ms                                                  | 28.6 ms: 1.41x slower                                                             |
| logging_silent             | 135 ns                                                   | 643 ns: 4.78x slower                                                              |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (29): sympy_integrate, json, json_dumps, meteor_contest, genshi_text, xml_etree_generate, crypto_pyaes, comprehensions, json_loads, xml_etree_process, asyncio_websockets, sympy_expand, thrift, docutils, sympy_sum, chaos, richards, pidigits, typing_runtime_protocols, shortest_path, fannkuch, connected_components, unpickle_pure_python, coroutines, deltablue, django_template, richards_super, genshi_xml, scimark_lu
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250620-3.15.0a0-494c825/bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 99.57% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x