# Results vs. 3.13.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-aarch64
- commit hash: be0ebdc
- commit date: 2025-06-20
- overall geometric mean: 1.058x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 303 ms: 1.03x faster                                                              |
| html5lib       | 65.6 ms                                                  | 61.9 ms: 1.06x faster                                                             |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                            |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 463 ms: 1.43x faster                                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                              |
| async_tree_none            | 504 ms                                                   | 390 ms: 1.29x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 884 ms: 1.29x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 906 ms: 1.29x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 378 ms: 1.28x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 659 ms: 1.22x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 658 ms: 1.20x faster                                                              |
| async_generators           | 500 ms                                                   | 450 ms: 1.11x faster                                                              |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                                      |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.0 ms: 1.11x faster                                                             |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                             |
| regex_v8       | 32.5 ms                                                  | 26.8 ms: 1.21x faster                                                             |
| regex_dna      | 263 ms                                                   | 224 ms: 1.17x faster                                                              |
| regex_compile  | 134 ms                                                   | 124 ms: 1.08x faster                                                              |
| Geometric mean | (ref)                                                    | 1.19x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.12x faster                                                              |
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                                              |
| xml_etree_generate  | 118 ms                                                   | 111 ms: 1.06x faster                                                              |
| tomli_loads         | 2.67 sec                                                 | 2.52 sec: 1.06x faster                                                            |
| xml_etree_process   | 82.1 ms                                                  | 79.3 ms: 1.04x faster                                                             |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (4): json_dumps, json_loads, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.67 sec: 2.07x faster                                                            |
| deepcopy                   | 479 us                                                   | 333 us: 1.44x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 463 ms: 1.43x faster                                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                              |
| deepcopy_memo              | 53.0 us                                                  | 38.3 us: 1.38x faster                                                             |
| regex_effbot               | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                             |
| async_tree_none            | 504 ms                                                   | 390 ms: 1.29x faster                                                              |
| go                         | 164 ms                                                   | 128 ms: 1.29x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 884 ms: 1.29x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 906 ms: 1.29x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 378 ms: 1.28x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 659 ms: 1.22x faster                                                              |
| regex_v8                   | 32.5 ms                                                  | 26.8 ms: 1.21x faster                                                             |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 658 ms: 1.20x faster                                                              |
| spectral_norm              | 143 ms                                                   | 120 ms: 1.19x faster                                                              |
| deepcopy_reduce            | 4.24 us                                                  | 3.62 us: 1.17x faster                                                             |
| regex_dna                  | 263 ms                                                   | 224 ms: 1.17x faster                                                              |
| generators                 | 40.3 ms                                                  | 34.9 ms: 1.16x faster                                                             |
| scimark_sor                | 164 ms                                                   | 145 ms: 1.13x faster                                                              |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.12x faster                                                              |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                                              |
| float                      | 95.8 ms                                                  | 86.0 ms: 1.11x faster                                                             |
| pyflate                    | 582 ms                                                   | 522 ms: 1.11x faster                                                              |
| async_generators           | 500 ms                                                   | 450 ms: 1.11x faster                                                              |
| telco                      | 10.5 ms                                                  | 9.48 ms: 1.10x faster                                                             |
| pylint                     | 345 ms                                                   | 316 ms: 1.09x faster                                                              |
| bpe_tokeniser              | 6.02 sec                                                 | 5.53 sec: 1.09x faster                                                            |
| scimark_monte_carlo        | 87.8 ms                                                  | 81.0 ms: 1.08x faster                                                             |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.08x faster                                                            |
| nqueens                    | 105 ms                                                   | 97.2 ms: 1.08x faster                                                             |
| regex_compile              | 134 ms                                                   | 124 ms: 1.08x faster                                                              |
| pathlib                    | 24.3 ms                                                  | 22.7 ms: 1.07x faster                                                             |
| xml_etree_generate         | 118 ms                                                   | 111 ms: 1.06x faster                                                              |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                             |
| html5lib                   | 65.6 ms                                                  | 61.9 ms: 1.06x faster                                                             |
| sqlite_synth               | 4.08 us                                                  | 3.85 us: 1.06x faster                                                             |
| tomli_loads                | 2.67 sec                                                 | 2.52 sec: 1.06x faster                                                            |
| sympy_integrate            | 21.4 ms                                                  | 20.3 ms: 1.05x faster                                                             |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                                            |
| scimark_fft                | 463 ms                                                   | 440 ms: 1.05x faster                                                              |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                            |
| coverage                   | 106 ms                                                   | 101 ms: 1.05x faster                                                              |
| xml_etree_process          | 82.1 ms                                                  | 79.3 ms: 1.04x faster                                                             |
| 2to3                       | 313 ms                                                   | 303 ms: 1.03x faster                                                              |
| richards                   | 54.5 ms                                                  | 53.5 ms: 1.02x faster                                                             |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                             |
| shortest_path              | 565 ms                                                   | 580 ms: 1.03x slower                                                              |
| connected_components       | 547 ms                                                   | 561 ms: 1.03x slower                                                              |
| pprint_pformat             | 1.99 sec                                                 | 2.07 sec: 1.04x slower                                                            |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.94 ms: 1.04x slower                                                             |
| raytrace                   | 310 ms                                                   | 326 ms: 1.05x slower                                                              |
| pprint_safe_repr           | 962 ms                                                   | 1.01 sec: 1.05x slower                                                            |
| scimark_lu                 | 146 ms                                                   | 155 ms: 1.06x slower                                                              |
| logging_simple             | 7.25 us                                                  | 7.72 us: 1.07x slower                                                             |
| create_gc_cycles           | 3.39 ms                                                  | 3.81 ms: 1.12x slower                                                             |
| gc_traversal               | 5.92 ms                                                  | 6.92 ms: 1.17x slower                                                             |
| many_optionals             | 626 us                                                   | 750 us: 1.20x slower                                                              |
| subparsers                 | 20.3 ms                                                  | 28.3 ms: 1.39x slower                                                             |
| logging_silent             | 135 ns                                                   | 629 ns: 4.67x slower                                                              |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                                      |

Benchmark hidden because not significant (29): sympy_sum, hexiom, meteor_contest, thrift, json, comprehensions, genshi_text, chaos, typing_runtime_protocols, json_dumps, python_startup_no_site, asyncio_websockets, docutils, crypto_pyaes, pidigits, genshi_xml, deltablue, json_loads, richards_super, django_template, fannkuch, unpickle_pure_python, mako, sympy_expand, logging_format, coroutines, sympy_str, nbody, pickle_pure_python
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250620-3.15.0a0-be0ebdc/bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x