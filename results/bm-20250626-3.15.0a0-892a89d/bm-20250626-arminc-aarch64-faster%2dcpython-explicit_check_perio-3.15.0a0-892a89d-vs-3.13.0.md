# Results vs. 3.13.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-aarch64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.056x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| html5lib       | 65.6 ms                                                  | 62.9 ms: 1.04x faster                                                             |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                            |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                      |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 467 ms: 1.42x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 471 ms: 1.41x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 908 ms: 1.28x faster                                                              |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 380 ms: 1.27x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 901 ms: 1.26x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 648 ms: 1.23x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 664 ms: 1.19x faster                                                              |
| async_generators           | 500 ms                                                   | 452 ms: 1.11x faster                                                              |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                                      |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 87.3 ms: 1.10x faster                                                             |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                             |
| regex_v8       | 32.5 ms                                                  | 27.1 ms: 1.20x faster                                                             |
| regex_dna      | 263 ms                                                   | 220 ms: 1.20x faster                                                              |
| regex_compile  | 134 ms                                                   | 123 ms: 1.08x faster                                                              |
| Geometric mean | (ref)                                                    | 1.19x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_iterparse | 159 ms                                                   | 141 ms: 1.12x faster                                                              |
| xml_etree_parse     | 203 ms                                                   | 182 ms: 1.12x faster                                                              |
| tomli_loads         | 2.67 sec                                                 | 2.47 sec: 1.08x faster                                                            |
| xml_etree_generate  | 118 ms                                                   | 111 ms: 1.07x faster                                                              |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (5): json_dumps, json_loads, xml_etree_process, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                             |
| python_startup_no_site | 8.79 ms                                                  | 8.62 ms: 1.02x faster                                                             |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.6 ms: 1.07x faster                                                             |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (3): genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.06x faster                                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 467 ms: 1.42x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 471 ms: 1.41x faster                                                              |
| deepcopy                   | 479 us                                                   | 341 us: 1.40x faster                                                              |
| deepcopy_memo              | 53.0 us                                                  | 38.3 us: 1.38x faster                                                             |
| regex_effbot               | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                             |
| go                         | 164 ms                                                   | 127 ms: 1.30x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 908 ms: 1.28x faster                                                              |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 380 ms: 1.27x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 901 ms: 1.26x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 648 ms: 1.23x faster                                                              |
| regex_v8                   | 32.5 ms                                                  | 27.1 ms: 1.20x faster                                                             |
| regex_dna                  | 263 ms                                                   | 220 ms: 1.20x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 664 ms: 1.19x faster                                                              |
| deepcopy_reduce            | 4.24 us                                                  | 3.58 us: 1.19x faster                                                             |
| spectral_norm              | 143 ms                                                   | 122 ms: 1.18x faster                                                              |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.12x faster                                                              |
| xml_etree_parse            | 203 ms                                                   | 182 ms: 1.12x faster                                                              |
| scimark_sor                | 164 ms                                                   | 148 ms: 1.11x faster                                                              |
| async_generators           | 500 ms                                                   | 452 ms: 1.11x faster                                                              |
| float                      | 95.8 ms                                                  | 87.3 ms: 1.10x faster                                                             |
| pylint                     | 345 ms                                                   | 316 ms: 1.09x faster                                                              |
| telco                      | 10.5 ms                                                  | 9.61 ms: 1.09x faster                                                             |
| pyflate                    | 582 ms                                                   | 537 ms: 1.08x faster                                                              |
| regex_compile              | 134 ms                                                   | 123 ms: 1.08x faster                                                              |
| generators                 | 40.3 ms                                                  | 37.2 ms: 1.08x faster                                                             |
| pycparser                  | 1.34 sec                                                 | 1.24 sec: 1.08x faster                                                            |
| tomli_loads                | 2.67 sec                                                 | 2.47 sec: 1.08x faster                                                            |
| sqlite_synth               | 4.08 us                                                  | 3.79 us: 1.08x faster                                                             |
| genshi_text                | 28.6 ms                                                  | 26.6 ms: 1.07x faster                                                             |
| scimark_fft                | 463 ms                                                   | 433 ms: 1.07x faster                                                              |
| nqueens                    | 105 ms                                                   | 98.2 ms: 1.07x faster                                                             |
| scimark_monte_carlo        | 87.8 ms                                                  | 82.2 ms: 1.07x faster                                                             |
| xml_etree_generate         | 118 ms                                                   | 111 ms: 1.07x faster                                                              |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                             |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                            |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                                            |
| html5lib                   | 65.6 ms                                                  | 62.9 ms: 1.04x faster                                                             |
| bpe_tokeniser              | 6.02 sec                                                 | 5.78 sec: 1.04x faster                                                            |
| comprehensions             | 20.8 us                                                  | 20.1 us: 1.04x faster                                                             |
| python_startup_no_site     | 8.79 ms                                                  | 8.62 ms: 1.02x faster                                                             |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                             |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.87 ms: 1.03x slower                                                             |
| logging_format             | 8.10 us                                                  | 8.38 us: 1.03x slower                                                             |
| sympy_str                  | 265 ms                                                   | 277 ms: 1.05x slower                                                              |
| pprint_pformat             | 1.99 sec                                                 | 2.08 sec: 1.05x slower                                                            |
| scimark_lu                 | 146 ms                                                   | 155 ms: 1.06x slower                                                              |
| pprint_safe_repr           | 962 ms                                                   | 1.03 sec: 1.07x slower                                                            |
| raytrace                   | 310 ms                                                   | 332 ms: 1.07x slower                                                              |
| logging_simple             | 7.25 us                                                  | 7.79 us: 1.07x slower                                                             |
| create_gc_cycles           | 3.39 ms                                                  | 3.77 ms: 1.11x slower                                                             |
| gc_traversal               | 5.92 ms                                                  | 6.83 ms: 1.15x slower                                                             |
| many_optionals             | 626 us                                                   | 759 us: 1.21x slower                                                              |
| subparsers                 | 20.3 ms                                                  | 28.3 ms: 1.39x slower                                                             |
| logging_silent             | 135 ns                                                   | 650 ns: 4.83x slower                                                              |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                                      |

Benchmark hidden because not significant (32): pathlib, meteor_contest, json, hexiom, json_dumps, coverage, sympy_integrate, thrift, sympy_sum, 2to3, chaos, json_loads, xml_etree_process, asyncio_websockets, unpickle_pure_python, sympy_expand, genshi_xml, typing_runtime_protocols, fannkuch, pidigits, crypto_pyaes, docutils, django_template, connected_components, coroutines, shortest_path, richards_super, mako, deltablue, nbody, richards, pickle_pure_python
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250626-3.15.0a0-892a89d/bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x