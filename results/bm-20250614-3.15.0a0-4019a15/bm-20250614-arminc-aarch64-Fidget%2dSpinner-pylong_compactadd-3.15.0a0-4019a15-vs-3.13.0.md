# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: pylong_compactadd
- machine: linux-aarch64
- commit hash: 4019a15
- commit date: 2025-06-14
- overall geometric mean: 1.020x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 300 ms: 1.04x faster                                                           |
| html5lib       | 65.6 ms                                                  | 62.5 ms: 1.05x faster                                                          |
| sphinx         | 1.20 sec                                                 | 1.12 sec: 1.07x faster                                                         |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 467 ms: 1.42x faster                                                           |
| async_tree_memoization_tg  | 663 ms                                                   | 468 ms: 1.42x faster                                                           |
| async_tree_none_tg         | 484 ms                                                   | 377 ms: 1.28x faster                                                           |
| async_tree_io_tg           | 1.16 sec                                                 | 908 ms: 1.28x faster                                                           |
| async_tree_none            | 504 ms                                                   | 398 ms: 1.27x faster                                                           |
| async_tree_io              | 1.14 sec                                                 | 900 ms: 1.27x faster                                                           |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 651 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 659 ms: 1.20x faster                                                           |
| async_generators           | 500 ms                                                   | 452 ms: 1.11x faster                                                           |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                                   |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.7 ms: 1.12x faster                                                          |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                   |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.93 ms: 1.30x faster                                                          |
| regex_dna      | 263 ms                                                   | 220 ms: 1.20x faster                                                           |
| regex_v8       | 32.5 ms                                                  | 27.7 ms: 1.18x faster                                                          |
| regex_compile  | 134 ms                                                   | 122 ms: 1.10x faster                                                           |
| Geometric mean | (ref)                                                    | 1.19x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 178 ms: 1.14x faster                                                           |
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                                           |
| tomli_loads         | 2.67 sec                                                 | 2.43 sec: 1.10x faster                                                         |
| xml_etree_process   | 82.1 ms                                                  | 79.2 ms: 1.04x faster                                                          |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                                   |

Benchmark hidden because not significant (5): xml_etree_generate, json_dumps, unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                          |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.62 sec: 2.12x faster                                                         |
| deepcopy                   | 479 us                                                   | 332 us: 1.44x faster                                                           |
| async_tree_memoization     | 664 ms                                                   | 467 ms: 1.42x faster                                                           |
| async_tree_memoization_tg  | 663 ms                                                   | 468 ms: 1.42x faster                                                           |
| deepcopy_memo              | 53.0 us                                                  | 38.2 us: 1.39x faster                                                          |
| regex_effbot               | 5.10 ms                                                  | 3.93 ms: 1.30x faster                                                          |
| async_tree_none_tg         | 484 ms                                                   | 377 ms: 1.28x faster                                                           |
| async_tree_io_tg           | 1.16 sec                                                 | 908 ms: 1.28x faster                                                           |
| go                         | 164 ms                                                   | 129 ms: 1.27x faster                                                           |
| async_tree_none            | 504 ms                                                   | 398 ms: 1.27x faster                                                           |
| async_tree_io              | 1.14 sec                                                 | 900 ms: 1.27x faster                                                           |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 651 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 659 ms: 1.20x faster                                                           |
| regex_dna                  | 263 ms                                                   | 220 ms: 1.20x faster                                                           |
| regex_v8                   | 32.5 ms                                                  | 27.7 ms: 1.18x faster                                                          |
| deepcopy_reduce            | 4.24 us                                                  | 3.66 us: 1.16x faster                                                          |
| spectral_norm              | 143 ms                                                   | 125 ms: 1.15x faster                                                           |
| generators                 | 40.3 ms                                                  | 35.2 ms: 1.14x faster                                                          |
| xml_etree_parse            | 203 ms                                                   | 178 ms: 1.14x faster                                                           |
| telco                      | 10.5 ms                                                  | 9.32 ms: 1.12x faster                                                          |
| scimark_sor                | 164 ms                                                   | 147 ms: 1.12x faster                                                           |
| float                      | 95.8 ms                                                  | 85.7 ms: 1.12x faster                                                          |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                                           |
| async_generators           | 500 ms                                                   | 452 ms: 1.11x faster                                                           |
| pathlib                    | 24.3 ms                                                  | 22.1 ms: 1.10x faster                                                          |
| regex_compile              | 134 ms                                                   | 122 ms: 1.10x faster                                                           |
| tomli_loads                | 2.67 sec                                                 | 2.43 sec: 1.10x faster                                                         |
| pylint                     | 345 ms                                                   | 315 ms: 1.10x faster                                                           |
| bpe_tokeniser              | 6.02 sec                                                 | 5.52 sec: 1.09x faster                                                         |
| pyflate                    | 582 ms                                                   | 535 ms: 1.09x faster                                                           |
| pycparser                  | 1.34 sec                                                 | 1.24 sec: 1.08x faster                                                         |
| sqlite_synth               | 4.08 us                                                  | 3.77 us: 1.08x faster                                                          |
| meteor_contest             | 117 ms                                                   | 109 ms: 1.07x faster                                                           |
| nqueens                    | 105 ms                                                   | 97.7 ms: 1.07x faster                                                          |
| sphinx                     | 1.20 sec                                                 | 1.12 sec: 1.07x faster                                                         |
| scimark_monte_carlo        | 87.8 ms                                                  | 82.0 ms: 1.07x faster                                                          |
| k_core                     | 2.99 sec                                                 | 2.80 sec: 1.07x faster                                                         |
| scimark_fft                | 463 ms                                                   | 433 ms: 1.07x faster                                                           |
| hexiom                     | 7.34 ms                                                  | 6.92 ms: 1.06x faster                                                          |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                          |
| html5lib                   | 65.6 ms                                                  | 62.5 ms: 1.05x faster                                                          |
| richards_super             | 60.8 ms                                                  | 58.2 ms: 1.05x faster                                                          |
| 2to3                       | 313 ms                                                   | 300 ms: 1.04x faster                                                           |
| xml_etree_process          | 82.1 ms                                                  | 79.2 ms: 1.04x faster                                                          |
| sympy_str                  | 265 ms                                                   | 262 ms: 1.01x faster                                                           |
| connected_components       | 547 ms                                                   | 555 ms: 1.02x slower                                                           |
| pprint_safe_repr           | 962 ms                                                   | 983 ms: 1.02x slower                                                           |
| raytrace                   | 310 ms                                                   | 323 ms: 1.04x slower                                                           |
| shortest_path              | 565 ms                                                   | 595 ms: 1.05x slower                                                           |
| create_gc_cycles           | 3.39 ms                                                  | 3.97 ms: 1.17x slower                                                          |
| gc_traversal               | 5.92 ms                                                  | 7.02 ms: 1.18x slower                                                          |
| many_optionals             | 626 us                                                   | 745 us: 1.19x slower                                                           |
| subparsers                 | 20.3 ms                                                  | 28.1 ms: 1.38x slower                                                          |
| logging_silent             | 135 ns                                                   | 634 ns: 4.71x slower                                                           |
| coverage                   | 106 ms                                                   | 544 ms: 5.15x slower                                                           |
| thrift                     | 1.01 ms                                                  | 193 ms: 191.45x slower                                                         |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                                   |

Benchmark hidden because not significant (31): xml_etree_generate, sympy_sum, sympy_integrate, json_dumps, genshi_text, richards, chaos, json, comprehensions, genshi_xml, python_startup_no_site, mako, sympy_expand, typing_runtime_protocols, docutils, crypto_pyaes, asyncio_websockets, pidigits, logging_format, unpickle_pure_python, json_loads, django_template, scimark_lu, nbody, fannkuch, pickle_pure_python, pprint_pformat, coroutines, deltablue, logging_simple, scimark_sparse_mat_mult
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250614-3.15.0a0-4019a15/bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.020x slower

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x