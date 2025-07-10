# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_oz
- machine: linux-aarch64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.032x faster
- HPT reliability: 88.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.16 sec: 1.07x slower                                          |
| html5lib       | 65.6 ms                                                  | 63.1 ms: 1.04x faster                                           |
| sphinx         | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                          |
| Geometric mean | (ref)                                                    | 1.00x slower                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 468 ms: 1.42x faster                                            |
| async_tree_memoization     | 664 ms                                                   | 470 ms: 1.41x faster                                            |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                            |
| async_tree_none            | 504 ms                                                   | 396 ms: 1.27x faster                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 922 ms: 1.26x faster                                            |
| async_tree_io              | 1.14 sec                                                 | 905 ms: 1.26x faster                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 664 ms: 1.21x faster                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 664 ms: 1.19x faster                                            |
| async_generators           | 500 ms                                                   | 481 ms: 1.04x faster                                            |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                    |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 84.4 ms: 1.13x faster                                           |
| nbody          | 118 ms                                                   | 125 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                    | 1.02x faster                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.91 ms: 1.31x faster                                           |
| regex_v8       | 32.5 ms                                                  | 27.0 ms: 1.21x faster                                           |
| regex_dna      | 263 ms                                                   | 220 ms: 1.19x faster                                            |
| regex_compile  | 134 ms                                                   | 124 ms: 1.08x faster                                            |
| Geometric mean | (ref)                                                    | 1.19x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 179 ms: 1.13x faster                                            |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.10x faster                                            |
| tomli_loads         | 2.67 sec                                                 | 2.43 sec: 1.10x faster                                          |
| xml_etree_generate  | 118 ms                                                   | 112 ms: 1.06x faster                                            |
| pickle_pure_python  | 374 us                                                   | 405 us: 1.08x slower                                            |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                    |

Benchmark hidden because not significant (4): json_dumps, xml_etree_process, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.3 ms: 1.05x faster                                           |
| Geometric mean | (ref)                                                    | 1.03x faster                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.70 sec: 2.02x faster                                          |
| deepcopy                   | 479 us                                                   | 335 us: 1.43x faster                                            |
| deepcopy_memo              | 53.0 us                                                  | 37.2 us: 1.42x faster                                           |
| async_tree_memoization_tg  | 663 ms                                                   | 468 ms: 1.42x faster                                            |
| async_tree_memoization     | 664 ms                                                   | 470 ms: 1.41x faster                                            |
| regex_effbot               | 5.10 ms                                                  | 3.91 ms: 1.31x faster                                           |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                            |
| async_tree_none            | 504 ms                                                   | 396 ms: 1.27x faster                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 922 ms: 1.26x faster                                            |
| async_tree_io              | 1.14 sec                                                 | 905 ms: 1.26x faster                                            |
| richards                   | 54.5 ms                                                  | 44.6 ms: 1.22x faster                                           |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 664 ms: 1.21x faster                                            |
| regex_v8                   | 32.5 ms                                                  | 27.0 ms: 1.21x faster                                           |
| regex_dna                  | 263 ms                                                   | 220 ms: 1.19x faster                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 664 ms: 1.19x faster                                            |
| richards_super             | 60.8 ms                                                  | 51.9 ms: 1.17x faster                                           |
| scimark_sor                | 164 ms                                                   | 142 ms: 1.16x faster                                            |
| float                      | 95.8 ms                                                  | 84.4 ms: 1.13x faster                                           |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                            |
| deepcopy_reduce            | 4.24 us                                                  | 3.75 us: 1.13x faster                                           |
| generators                 | 40.3 ms                                                  | 36.2 ms: 1.12x faster                                           |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.10x faster                                            |
| tomli_loads                | 2.67 sec                                                 | 2.43 sec: 1.10x faster                                          |
| telco                      | 10.5 ms                                                  | 9.64 ms: 1.09x faster                                           |
| regex_compile              | 134 ms                                                   | 124 ms: 1.08x faster                                            |
| spectral_norm              | 143 ms                                                   | 134 ms: 1.07x faster                                            |
| xml_etree_generate         | 118 ms                                                   | 112 ms: 1.06x faster                                            |
| python_startup             | 16.0 ms                                                  | 15.3 ms: 1.05x faster                                           |
| bpe_tokeniser              | 6.02 sec                                                 | 5.74 sec: 1.05x faster                                          |
| coverage                   | 106 ms                                                   | 101 ms: 1.04x faster                                            |
| logging_silent             | 135 ns                                                   | 129 ns: 1.04x faster                                            |
| async_generators           | 500 ms                                                   | 481 ms: 1.04x faster                                            |
| html5lib                   | 65.6 ms                                                  | 63.1 ms: 1.04x faster                                           |
| logging_simple             | 7.25 us                                                  | 7.00 us: 1.04x faster                                           |
| sqlite_synth               | 4.08 us                                                  | 3.95 us: 1.03x faster                                           |
| scimark_fft                | 463 ms                                                   | 448 ms: 1.03x faster                                            |
| sphinx                     | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                          |
| k_core                     | 2.99 sec                                                 | 2.93 sec: 1.02x faster                                          |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                           |
| pycparser                  | 1.34 sec                                                 | 1.40 sec: 1.04x slower                                          |
| sympy_str                  | 265 ms                                                   | 276 ms: 1.04x slower                                            |
| sympy_expand               | 472 ms                                                   | 495 ms: 1.05x slower                                            |
| nbody                      | 118 ms                                                   | 125 ms: 1.06x slower                                            |
| hexiom                     | 7.34 ms                                                  | 7.77 ms: 1.06x slower                                           |
| docutils                   | 2.96 sec                                                 | 3.16 sec: 1.07x slower                                          |
| typing_runtime_protocols   | 197 us                                                   | 211 us: 1.07x slower                                            |
| comprehensions             | 20.8 us                                                  | 22.5 us: 1.08x slower                                           |
| pickle_pure_python         | 374 us                                                   | 405 us: 1.08x slower                                            |
| connected_components       | 547 ms                                                   | 593 ms: 1.08x slower                                            |
| raytrace                   | 310 ms                                                   | 338 ms: 1.09x slower                                            |
| shortest_path              | 565 ms                                                   | 618 ms: 1.09x slower                                            |
| fannkuch                   | 478 ms                                                   | 527 ms: 1.10x slower                                            |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.37 ms: 1.11x slower                                           |
| create_gc_cycles           | 3.39 ms                                                  | 3.78 ms: 1.11x slower                                           |
| crypto_pyaes               | 84.9 ms                                                  | 97.7 ms: 1.15x slower                                           |
| gc_traversal               | 5.92 ms                                                  | 6.84 ms: 1.16x slower                                           |
| pprint_safe_repr           | 962 ms                                                   | 1.23 sec: 1.27x slower                                          |
| pprint_pformat             | 1.99 sec                                                 | 2.54 sec: 1.28x slower                                          |
| many_optionals             | 626 us                                                   | 837 us: 1.34x slower                                            |
| subparsers                 | 20.3 ms                                                  | 28.6 ms: 1.41x slower                                           |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                    |

Benchmark hidden because not significant (28): scimark_monte_carlo, pylint, json_dumps, genshi_text, thrift, logging_format, pathlib, sympy_sum, chaos, pyflate, json, go, python_startup_no_site, xml_etree_process, coroutines, deltablue, asyncio_websockets, nqueens, pidigits, genshi_xml, 2to3, sympy_integrate, unpickle_pure_python, django_template, json_loads, mako, scimark_lu, meteor_contest
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250628-3.15.0a0-6448067-JIT/bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 88.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x