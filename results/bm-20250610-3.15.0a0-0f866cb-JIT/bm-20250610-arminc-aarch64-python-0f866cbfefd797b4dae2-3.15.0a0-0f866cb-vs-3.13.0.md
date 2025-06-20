# Results vs. 3.13.0

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: linux-aarch64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.044x faster
- HPT reliability: 98.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.11 sec: 1.05x slower                                                  |
| html5lib       | 65.6 ms                                                  | 62.8 ms: 1.05x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.17 sec: 1.02x faster                                                  |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 478 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 481 ms: 1.38x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 903 ms: 1.26x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 389 ms: 1.24x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 938 ms: 1.24x faster                                                    |
| async_tree_none            | 504 ms                                                   | 406 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 675 ms: 1.19x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 675 ms: 1.17x faster                                                    |
| async_generators           | 500 ms                                                   | 472 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.19x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.5 ms: 1.16x faster                                                   |
| Geometric mean | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.93 ms: 1.30x faster                                                   |
| regex_dna      | 263 ms                                                   | 219 ms: 1.20x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 27.8 ms: 1.17x faster                                                   |
| regex_compile  | 134 ms                                                   | 121 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                    | 1.19x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.34 sec: 1.14x faster                                                  |
| xml_etree_parse     | 203 ms                                                   | 179 ms: 1.13x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| xml_etree_generate  | 118 ms                                                   | 108 ms: 1.09x faster                                                    |
| pickle_pure_python  | 374 us                                                   | 401 us: 1.07x slower                                                    |
| Geometric mean      | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (4): unpickle_pure_python, json_dumps, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 14.7 ms: 1.09x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.43 ms: 1.04x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.07x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 13.2 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                  |
| deepcopy_memo              | 53.0 us                                                  | 36.6 us: 1.45x faster                                                   |
| deepcopy                   | 479 us                                                   | 336 us: 1.43x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 478 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 481 ms: 1.38x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.93 ms: 1.30x faster                                                   |
| async_tree_io              | 1.14 sec                                                 | 903 ms: 1.26x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 389 ms: 1.24x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 938 ms: 1.24x faster                                                    |
| async_tree_none            | 504 ms                                                   | 406 ms: 1.24x faster                                                    |
| richards                   | 54.5 ms                                                  | 45.3 ms: 1.20x faster                                                   |
| regex_dna                  | 263 ms                                                   | 219 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 675 ms: 1.19x faster                                                    |
| richards_super             | 60.8 ms                                                  | 51.4 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 675 ms: 1.17x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 27.8 ms: 1.17x faster                                                   |
| float                      | 95.8 ms                                                  | 82.5 ms: 1.16x faster                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 3.67 us: 1.16x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.34 sec: 1.14x faster                                                  |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                                    |
| scimark_sor                | 164 ms                                                   | 145 ms: 1.13x faster                                                    |
| generators                 | 40.3 ms                                                  | 35.7 ms: 1.13x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.40 sec: 1.11x faster                                                  |
| telco                      | 10.5 ms                                                  | 9.40 ms: 1.11x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| regex_compile              | 134 ms                                                   | 121 ms: 1.10x faster                                                    |
| scimark_fft                | 463 ms                                                   | 420 ms: 1.10x faster                                                    |
| python_startup             | 16.0 ms                                                  | 14.7 ms: 1.09x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 108 ms: 1.09x faster                                                    |
| spectral_norm              | 143 ms                                                   | 132 ms: 1.09x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 81.4 ms: 1.08x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.79 us: 1.08x faster                                                   |
| pylint                     | 345 ms                                                   | 320 ms: 1.08x faster                                                    |
| thrift                     | 1.01 ms                                                  | 940 us: 1.08x faster                                                    |
| async_generators           | 500 ms                                                   | 472 ms: 1.06x faster                                                    |
| json                       | 5.94 ms                                                  | 5.62 ms: 1.06x faster                                                   |
| mako                       | 14.0 ms                                                  | 13.2 ms: 1.05x faster                                                   |
| pyflate                    | 582 ms                                                   | 553 ms: 1.05x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 62.8 ms: 1.05x faster                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 8.43 ms: 1.04x faster                                                   |
| go                         | 164 ms                                                   | 159 ms: 1.03x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.91 sec: 1.03x faster                                                  |
| sphinx                     | 1.20 sec                                                 | 1.17 sec: 1.02x faster                                                  |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.38 sec: 1.02x slower                                                  |
| sympy_str                  | 265 ms                                                   | 272 ms: 1.03x slower                                                    |
| logging_simple             | 7.25 us                                                  | 7.49 us: 1.03x slower                                                   |
| sympy_expand               | 472 ms                                                   | 491 ms: 1.04x slower                                                    |
| connected_components       | 547 ms                                                   | 574 ms: 1.05x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.11 sec: 1.05x slower                                                  |
| typing_runtime_protocols   | 197 us                                                   | 209 us: 1.06x slower                                                    |
| comprehensions             | 20.8 us                                                  | 22.2 us: 1.07x slower                                                   |
| raytrace                   | 310 ms                                                   | 332 ms: 1.07x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 401 us: 1.07x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.65 ms: 1.08x slower                                                   |
| crypto_pyaes               | 84.9 ms                                                  | 92.1 ms: 1.08x slower                                                   |
| shortest_path              | 565 ms                                                   | 618 ms: 1.09x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.82 ms: 1.15x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.25 sec: 1.30x slower                                                  |
| pprint_pformat             | 1.99 sec                                                 | 2.63 sec: 1.32x slower                                                  |
| many_optionals             | 626 us                                                   | 830 us: 1.32x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 28.2 ms: 1.39x slower                                                   |
| logging_silent             | 135 ns                                                   | 634 ns: 4.71x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (25): unpickle_pure_python, genshi_text, json_dumps, pathlib, xml_etree_process, sympy_sum, coverage, chaos, sympy_integrate, meteor_contest, asyncio_websockets, 2to3, nbody, coroutines, pidigits, nqueens, json_loads, deltablue, genshi_xml, fannkuch, hexiom, logging_format, django_template, scimark_lu, scimark_sparse_mat_mult
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 98.57% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x