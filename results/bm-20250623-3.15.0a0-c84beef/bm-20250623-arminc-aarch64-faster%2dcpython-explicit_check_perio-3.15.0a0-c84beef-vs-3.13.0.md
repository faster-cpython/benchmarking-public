# Results vs. 3.13.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-aarch64
- commit hash: c84beef
- commit date: 2025-06-23
- overall geometric mean: 1.065x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 303 ms: 1.03x faster                                                              |
| html5lib       | 65.6 ms                                                  | 62.4 ms: 1.05x faster                                                             |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.06x faster                                                            |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 467 ms: 1.42x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 374 ms: 1.30x faster                                                              |
| async_tree_none            | 504 ms                                                   | 389 ms: 1.30x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 908 ms: 1.28x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 896 ms: 1.27x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 651 ms: 1.23x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 656 ms: 1.20x faster                                                              |
| async_generators           | 500 ms                                                   | 452 ms: 1.11x faster                                                              |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                                      |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.0 ms: 1.11x faster                                                             |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.03 ms: 1.27x faster                                                             |
| regex_v8       | 32.5 ms                                                  | 27.3 ms: 1.19x faster                                                             |
| regex_dna      | 263 ms                                                   | 225 ms: 1.17x faster                                                              |
| regex_compile  | 134 ms                                                   | 120 ms: 1.12x faster                                                              |
| Geometric mean | (ref)                                                    | 1.19x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.12x faster                                                              |
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                                              |
| tomli_loads         | 2.67 sec                                                 | 2.42 sec: 1.10x faster                                                            |
| xml_etree_process   | 82.1 ms                                                  | 79.4 ms: 1.03x faster                                                             |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                                      |

Benchmark hidden because not significant (5): xml_etree_generate, json_dumps, json_loads, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.2 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.5 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                      |

Benchmark hidden because not significant (3): django_template, genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.63 sec: 2.11x faster                                                            |
| deepcopy                   | 479 us                                                   | 325 us: 1.47x faster                                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 467 ms: 1.42x faster                                                              |
| deepcopy_memo              | 53.0 us                                                  | 39.2 us: 1.35x faster                                                             |
| go                         | 164 ms                                                   | 126 ms: 1.31x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 374 ms: 1.30x faster                                                              |
| async_tree_none            | 504 ms                                                   | 389 ms: 1.30x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 908 ms: 1.28x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 896 ms: 1.27x faster                                                              |
| regex_effbot               | 5.10 ms                                                  | 4.03 ms: 1.27x faster                                                             |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 651 ms: 1.23x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 656 ms: 1.20x faster                                                              |
| regex_v8                   | 32.5 ms                                                  | 27.3 ms: 1.19x faster                                                             |
| deepcopy_reduce            | 4.24 us                                                  | 3.59 us: 1.18x faster                                                             |
| regex_dna                  | 263 ms                                                   | 225 ms: 1.17x faster                                                              |
| spectral_norm              | 143 ms                                                   | 124 ms: 1.16x faster                                                              |
| scimark_sor                | 164 ms                                                   | 142 ms: 1.15x faster                                                              |
| pyflate                    | 582 ms                                                   | 513 ms: 1.13x faster                                                              |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.12x faster                                                              |
| generators                 | 40.3 ms                                                  | 35.9 ms: 1.12x faster                                                             |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                                              |
| regex_compile              | 134 ms                                                   | 120 ms: 1.12x faster                                                              |
| float                      | 95.8 ms                                                  | 86.0 ms: 1.11x faster                                                             |
| telco                      | 10.5 ms                                                  | 9.40 ms: 1.11x faster                                                             |
| async_generators           | 500 ms                                                   | 452 ms: 1.11x faster                                                              |
| sqlite_synth               | 4.08 us                                                  | 3.70 us: 1.10x faster                                                             |
| tomli_loads                | 2.67 sec                                                 | 2.42 sec: 1.10x faster                                                            |
| pylint                     | 345 ms                                                   | 316 ms: 1.09x faster                                                              |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.3 ms: 1.09x faster                                                             |
| bpe_tokeniser              | 6.02 sec                                                 | 5.51 sec: 1.09x faster                                                            |
| scimark_fft                | 463 ms                                                   | 428 ms: 1.08x faster                                                              |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.08x faster                                                            |
| genshi_text                | 28.6 ms                                                  | 26.5 ms: 1.08x faster                                                             |
| k_core                     | 2.99 sec                                                 | 2.78 sec: 1.08x faster                                                            |
| nqueens                    | 105 ms                                                   | 98.0 ms: 1.07x faster                                                             |
| meteor_contest             | 117 ms                                                   | 110 ms: 1.06x faster                                                              |
| hexiom                     | 7.34 ms                                                  | 6.92 ms: 1.06x faster                                                             |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.06x faster                                                            |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.05x faster                                                             |
| html5lib                   | 65.6 ms                                                  | 62.4 ms: 1.05x faster                                                             |
| coverage                   | 106 ms                                                   | 101 ms: 1.05x faster                                                              |
| richards                   | 54.5 ms                                                  | 52.4 ms: 1.04x faster                                                             |
| xml_etree_process          | 82.1 ms                                                  | 79.4 ms: 1.03x faster                                                             |
| 2to3                       | 313 ms                                                   | 303 ms: 1.03x faster                                                              |
| richards_super             | 60.8 ms                                                  | 59.0 ms: 1.03x faster                                                             |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                             |
| shortest_path              | 565 ms                                                   | 575 ms: 1.02x slower                                                              |
| connected_components       | 547 ms                                                   | 560 ms: 1.02x slower                                                              |
| pprint_safe_repr           | 962 ms                                                   | 988 ms: 1.03x slower                                                              |
| raytrace                   | 310 ms                                                   | 325 ms: 1.05x slower                                                              |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.08 ms: 1.06x slower                                                             |
| logging_simple             | 7.25 us                                                  | 7.75 us: 1.07x slower                                                             |
| create_gc_cycles           | 3.39 ms                                                  | 3.83 ms: 1.13x slower                                                             |
| gc_traversal               | 5.92 ms                                                  | 6.92 ms: 1.17x slower                                                             |
| many_optionals             | 626 us                                                   | 760 us: 1.21x slower                                                              |
| subparsers                 | 20.3 ms                                                  | 28.1 ms: 1.38x slower                                                             |
| logging_silent             | 135 ns                                                   | 614 ns: 4.56x slower                                                              |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                                      |

Benchmark hidden because not significant (30): pathlib, sympy_sum, json, xml_etree_generate, json_dumps, thrift, sympy_integrate, sympy_expand, comprehensions, asyncio_websockets, chaos, json_loads, crypto_pyaes, python_startup_no_site, pidigits, django_template, fannkuch, genshi_xml, typing_runtime_protocols, docutils, deltablue, sympy_str, unpickle_pure_python, pprint_pformat, coroutines, mako, logging_format, pickle_pure_python, scimark_lu, nbody
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250623-3.15.0a0-c84beef/bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.065x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x