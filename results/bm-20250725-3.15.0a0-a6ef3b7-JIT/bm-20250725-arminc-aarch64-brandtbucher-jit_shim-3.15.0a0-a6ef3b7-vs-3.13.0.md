# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_shim
- machine: linux-aarch64
- commit hash: a6ef3b7
- commit date: 2025-07-25
- overall geometric mean: 1.015x faster
- HPT reliability: 98.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                            |
| html5lib       | 65.6 ms                                                  | 62.2 ms: 1.05x faster                                             |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                            |
| Geometric mean | (ref)                                                    | 1.01x faster                                                      |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 467 ms: 1.42x faster                                              |
| async_tree_memoization     | 664 ms                                                   | 471 ms: 1.41x faster                                              |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                              |
| async_tree_io              | 1.14 sec                                                 | 898 ms: 1.27x faster                                              |
| async_tree_none            | 504 ms                                                   | 399 ms: 1.26x faster                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 922 ms: 1.26x faster                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 655 ms: 1.22x faster                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 668 ms: 1.18x faster                                              |
| async_generators           | 500 ms                                                   | 486 ms: 1.03x faster                                              |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                      |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.5 ms: 1.16x faster                                             |
| nbody          | 118 ms                                                   | 124 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                    | 1.03x faster                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.89 ms: 1.31x faster                                             |
| regex_v8       | 32.5 ms                                                  | 27.2 ms: 1.20x faster                                             |
| regex_dna      | 263 ms                                                   | 221 ms: 1.19x faster                                              |
| regex_compile  | 134 ms                                                   | 120 ms: 1.11x faster                                              |
| Geometric mean | (ref)                                                    | 1.20x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.67 sec                                                 | 2.32 sec: 1.15x faster                                            |
| xml_etree_parse      | 203 ms                                                   | 179 ms: 1.13x faster                                              |
| xml_etree_iterparse  | 159 ms                                                   | 145 ms: 1.10x faster                                              |
| xml_etree_generate   | 118 ms                                                   | 111 ms: 1.07x faster                                              |
| unpickle_pure_python | 265 us                                                   | 249 us: 1.06x faster                                              |
| xml_etree_process    | 82.1 ms                                                  | 77.8 ms: 1.06x faster                                             |
| pickle_pure_python   | 374 us                                                   | 394 us: 1.05x slower                                              |
| Geometric mean       | (ref)                                                    | 1.06x faster                                                      |

Benchmark hidden because not significant (2): json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                             |
| python_startup_no_site | 8.79 ms                                                  | 8.62 ms: 1.02x faster                                             |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 12.8 ms: 1.09x faster                                             |
| genshi_text    | 28.6 ms                                                  | 26.4 ms: 1.08x faster                                             |
| Geometric mean | (ref)                                                    | 1.04x faster                                                      |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.62 sec: 2.13x faster                                            |
| deepcopy_memo              | 53.0 us                                                  | 36.0 us: 1.47x faster                                             |
| deepcopy                   | 479 us                                                   | 337 us: 1.42x faster                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 467 ms: 1.42x faster                                              |
| async_tree_memoization     | 664 ms                                                   | 471 ms: 1.41x faster                                              |
| regex_effbot               | 5.10 ms                                                  | 3.89 ms: 1.31x faster                                             |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                              |
| async_tree_io              | 1.14 sec                                                 | 898 ms: 1.27x faster                                              |
| async_tree_none            | 504 ms                                                   | 399 ms: 1.26x faster                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 922 ms: 1.26x faster                                              |
| richards                   | 54.5 ms                                                  | 43.3 ms: 1.26x faster                                             |
| richards_super             | 60.8 ms                                                  | 49.7 ms: 1.22x faster                                             |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 655 ms: 1.22x faster                                              |
| spectral_norm              | 143 ms                                                   | 117 ms: 1.22x faster                                              |
| deepcopy_reduce            | 4.24 us                                                  | 3.54 us: 1.20x faster                                             |
| regex_v8                   | 32.5 ms                                                  | 27.2 ms: 1.20x faster                                             |
| regex_dna                  | 263 ms                                                   | 221 ms: 1.19x faster                                              |
| scimark_sor                | 164 ms                                                   | 139 ms: 1.18x faster                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 668 ms: 1.18x faster                                              |
| float                      | 95.8 ms                                                  | 82.5 ms: 1.16x faster                                             |
| tomli_loads                | 2.67 sec                                                 | 2.32 sec: 1.15x faster                                            |
| sqlite_synth               | 4.08 us                                                  | 3.61 us: 1.13x faster                                             |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                              |
| generators                 | 40.3 ms                                                  | 35.7 ms: 1.13x faster                                             |
| scimark_fft                | 463 ms                                                   | 411 ms: 1.13x faster                                              |
| bpe_tokeniser              | 6.02 sec                                                 | 5.41 sec: 1.11x faster                                            |
| regex_compile              | 134 ms                                                   | 120 ms: 1.11x faster                                              |
| xml_etree_iterparse        | 159 ms                                                   | 145 ms: 1.10x faster                                              |
| pathlib                    | 24.3 ms                                                  | 22.2 ms: 1.09x faster                                             |
| mako                       | 14.0 ms                                                  | 12.8 ms: 1.09x faster                                             |
| go                         | 164 ms                                                   | 150 ms: 1.09x faster                                              |
| scimark_monte_carlo        | 87.8 ms                                                  | 81.0 ms: 1.08x faster                                             |
| genshi_text                | 28.6 ms                                                  | 26.4 ms: 1.08x faster                                             |
| pyflate                    | 582 ms                                                   | 541 ms: 1.08x faster                                              |
| pylint                     | 345 ms                                                   | 321 ms: 1.08x faster                                              |
| logging_format             | 8.10 us                                                  | 7.55 us: 1.07x faster                                             |
| python_startup             | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                             |
| xml_etree_generate         | 118 ms                                                   | 111 ms: 1.07x faster                                              |
| unpickle_pure_python       | 265 us                                                   | 249 us: 1.06x faster                                              |
| xml_etree_process          | 82.1 ms                                                  | 77.8 ms: 1.06x faster                                             |
| logging_silent             | 135 ns                                                   | 128 ns: 1.06x faster                                              |
| html5lib                   | 65.6 ms                                                  | 62.2 ms: 1.05x faster                                             |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                            |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.03x faster                                              |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                            |
| async_generators           | 500 ms                                                   | 486 ms: 1.03x faster                                              |
| python_startup_no_site     | 8.79 ms                                                  | 8.62 ms: 1.02x faster                                             |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                             |
| sympy_expand               | 472 ms                                                   | 490 ms: 1.04x slower                                              |
| docutils                   | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                            |
| connected_components       | 547 ms                                                   | 570 ms: 1.04x slower                                              |
| shortest_path              | 565 ms                                                   | 592 ms: 1.05x slower                                              |
| comprehensions             | 20.8 us                                                  | 21.9 us: 1.05x slower                                             |
| typing_runtime_protocols   | 197 us                                                   | 207 us: 1.05x slower                                              |
| nbody                      | 118 ms                                                   | 124 ms: 1.05x slower                                              |
| pickle_pure_python         | 374 us                                                   | 394 us: 1.05x slower                                              |
| sympy_str                  | 265 ms                                                   | 281 ms: 1.06x slower                                              |
| raytrace                   | 310 ms                                                   | 330 ms: 1.07x slower                                              |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.15 ms: 1.07x slower                                             |
| crypto_pyaes               | 84.9 ms                                                  | 93.2 ms: 1.10x slower                                             |
| create_gc_cycles           | 3.39 ms                                                  | 3.78 ms: 1.12x slower                                             |
| pprint_pformat             | 1.99 sec                                                 | 2.24 sec: 1.13x slower                                            |
| gc_traversal               | 5.92 ms                                                  | 6.75 ms: 1.14x slower                                             |
| pprint_safe_repr           | 962 ms                                                   | 1.11 sec: 1.15x slower                                            |
| many_optionals             | 626 us                                                   | 990 us: 1.58x slower                                              |
| subparsers                 | 20.3 ms                                                  | 48.9 ms: 2.40x slower                                             |
| telco                      | 10.5 ms                                                  | 164 ms: 15.68x slower                                             |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                      |

Benchmark hidden because not significant (21): sympy_integrate, sympy_sum, logging_simple, deltablue, chaos, coverage, thrift, json_dumps, scimark_lu, fannkuch, 2to3, asyncio_websockets, json, coroutines, json_loads, pidigits, pycparser, genshi_xml, nqueens, hexiom, django_template
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.015x faster

# HPT report

- Reliability score: 98.48% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x