# Results vs. 3.13.0

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: linux-aarch64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.040x faster
- HPT reliability: 97.33%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.12 sec: 1.05x slower                                                  |
| sphinx         | 1.20 sec                                                 | 1.17 sec: 1.02x faster                                                  |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 468 ms: 1.42x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 471 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 379 ms: 1.28x faster                                                    |
| async_tree_none            | 504 ms                                                   | 396 ms: 1.27x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 915 ms: 1.27x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 897 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 655 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 660 ms: 1.20x faster                                                    |
| async_generators           | 500 ms                                                   | 482 ms: 1.04x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 83.3 ms: 1.15x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 26.9 ms: 1.21x faster                                                   |
| regex_dna      | 263 ms                                                   | 225 ms: 1.17x faster                                                    |
| regex_compile  | 134 ms                                                   | 122 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                    | 1.19x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.42 sec: 1.10x faster                                                  |
| xml_etree_parse     | 203 ms                                                   | 187 ms: 1.08x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 149 ms: 1.07x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 78.7 ms: 1.04x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 408 us: 1.09x slower                                                    |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (4): xml_etree_generate, unpickle_pure_python, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.63 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.70 sec: 2.03x faster                                                  |
| deepcopy                   | 479 us                                                   | 334 us: 1.43x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 468 ms: 1.42x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 37.4 us: 1.41x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 471 ms: 1.41x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 379 ms: 1.28x faster                                                    |
| async_tree_none            | 504 ms                                                   | 396 ms: 1.27x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 915 ms: 1.27x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 897 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 655 ms: 1.22x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 26.9 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 660 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.56 us: 1.19x faster                                                   |
| richards_super             | 60.8 ms                                                  | 51.3 ms: 1.19x faster                                                   |
| richards                   | 54.5 ms                                                  | 46.1 ms: 1.18x faster                                                   |
| regex_dna                  | 263 ms                                                   | 225 ms: 1.17x faster                                                    |
| float                      | 95.8 ms                                                  | 83.3 ms: 1.15x faster                                                   |
| scimark_sor                | 164 ms                                                   | 146 ms: 1.12x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.36 ms: 1.12x faster                                                   |
| generators                 | 40.3 ms                                                  | 36.4 ms: 1.11x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.42 sec: 1.10x faster                                                  |
| regex_compile              | 134 ms                                                   | 122 ms: 1.10x faster                                                    |
| spectral_norm              | 143 ms                                                   | 131 ms: 1.09x faster                                                    |
| scimark_fft                | 463 ms                                                   | 425 ms: 1.09x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.53 sec: 1.09x faster                                                  |
| xml_etree_parse            | 203 ms                                                   | 187 ms: 1.08x faster                                                    |
| pyflate                    | 582 ms                                                   | 539 ms: 1.08x faster                                                    |
| pylint                     | 345 ms                                                   | 322 ms: 1.07x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.81 us: 1.07x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 149 ms: 1.07x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 82.8 ms: 1.06x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 23.0 ms: 1.06x faster                                                   |
| mako                       | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                                   |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 78.7 ms: 1.04x faster                                                   |
| go                         | 164 ms                                                   | 158 ms: 1.04x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.87 sec: 1.04x faster                                                  |
| async_generators           | 500 ms                                                   | 482 ms: 1.04x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.17 sec: 1.02x faster                                                  |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 8.63 ms: 1.02x faster                                                   |
| shortest_path              | 565 ms                                                   | 586 ms: 1.04x slower                                                    |
| connected_components       | 547 ms                                                   | 570 ms: 1.04x slower                                                    |
| sympy_str                  | 265 ms                                                   | 276 ms: 1.04x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.12 sec: 1.05x slower                                                  |
| logging_simple             | 7.25 us                                                  | 7.69 us: 1.06x slower                                                   |
| crypto_pyaes               | 84.9 ms                                                  | 90.9 ms: 1.07x slower                                                   |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.15 ms: 1.07x slower                                                   |
| raytrace                   | 310 ms                                                   | 333 ms: 1.07x slower                                                    |
| sympy_expand               | 472 ms                                                   | 509 ms: 1.08x slower                                                    |
| comprehensions             | 20.8 us                                                  | 22.5 us: 1.08x slower                                                   |
| pickle_pure_python         | 374 us                                                   | 408 us: 1.09x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 219 us: 1.11x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.83 ms: 1.13x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.92 ms: 1.17x slower                                                   |
| many_optionals             | 626 us                                                   | 819 us: 1.31x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 1.26 sec: 1.31x slower                                                  |
| pprint_pformat             | 1.99 sec                                                 | 2.66 sec: 1.34x slower                                                  |
| subparsers                 | 20.3 ms                                                  | 28.2 ms: 1.39x slower                                                   |
| logging_silent             | 135 ns                                                   | 622 ns: 4.62x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (27): xml_etree_generate, unpickle_pure_python, genshi_text, thrift, coverage, nqueens, json_dumps, html5lib, sympy_sum, chaos, json, sympy_integrate, json_loads, asyncio_websockets, deltablue, pidigits, 2to3, coroutines, meteor_contest, genshi_xml, django_template, fannkuch, pycparser, hexiom, logging_format, nbody, scimark_lu
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 97.33% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x