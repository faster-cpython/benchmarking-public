# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_o2
- machine: linux-aarch64
- commit hash: f528bf3
- commit date: 2025-06-28
- overall geometric mean: 1.047x faster
- HPT reliability: 98.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.11 sec: 1.05x slower                                          |
| html5lib       | 65.6 ms                                                  | 62.9 ms: 1.04x faster                                           |
| sphinx         | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                          |
| Geometric mean | (ref)                                                    | 1.01x faster                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 470 ms: 1.41x faster                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 478 ms: 1.39x faster                                            |
| async_tree_none            | 504 ms                                                   | 397 ms: 1.27x faster                                            |
| async_tree_io              | 1.14 sec                                                 | 898 ms: 1.27x faster                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 924 ms: 1.26x faster                                            |
| async_tree_none_tg         | 484 ms                                                   | 385 ms: 1.26x faster                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 666 ms: 1.20x faster                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 664 ms: 1.19x faster                                            |
| async_generators           | 500 ms                                                   | 482 ms: 1.04x faster                                            |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 83.4 ms: 1.15x faster                                           |
| nbody          | 118 ms                                                   | 128 ms: 1.08x slower                                            |
| Geometric mean | (ref)                                                    | 1.02x faster                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.94 ms: 1.30x faster                                           |
| regex_v8       | 32.5 ms                                                  | 26.6 ms: 1.22x faster                                           |
| regex_dna      | 263 ms                                                   | 226 ms: 1.16x faster                                            |
| regex_compile  | 134 ms                                                   | 125 ms: 1.07x faster                                            |
| Geometric mean | (ref)                                                    | 1.18x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.33 sec: 1.14x faster                                          |
| xml_etree_parse     | 203 ms                                                   | 178 ms: 1.14x faster                                            |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.10x faster                                            |
| xml_etree_generate  | 118 ms                                                   | 109 ms: 1.08x faster                                            |
| xml_etree_process   | 82.1 ms                                                  | 77.2 ms: 1.06x faster                                           |
| Geometric mean      | (ref)                                                    | 1.06x faster                                                    |

Benchmark hidden because not significant (4): json_dumps, unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                           |
| python_startup_no_site | 8.79 ms                                                  | 8.63 ms: 1.02x faster                                           |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                           |
| genshi_xml     | 61.6 ms                                                  | 64.0 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                    | 1.01x faster                                                    |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.65 sec: 2.08x faster                                          |
| deepcopy_memo              | 53.0 us                                                  | 37.4 us: 1.42x faster                                           |
| async_tree_memoization     | 664 ms                                                   | 470 ms: 1.41x faster                                            |
| deepcopy                   | 479 us                                                   | 339 us: 1.41x faster                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 478 ms: 1.39x faster                                            |
| regex_effbot               | 5.10 ms                                                  | 3.94 ms: 1.30x faster                                           |
| async_tree_none            | 504 ms                                                   | 397 ms: 1.27x faster                                            |
| async_tree_io              | 1.14 sec                                                 | 898 ms: 1.27x faster                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 924 ms: 1.26x faster                                            |
| async_tree_none_tg         | 484 ms                                                   | 385 ms: 1.26x faster                                            |
| regex_v8                   | 32.5 ms                                                  | 26.6 ms: 1.22x faster                                           |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 666 ms: 1.20x faster                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 664 ms: 1.19x faster                                            |
| spectral_norm              | 143 ms                                                   | 121 ms: 1.19x faster                                            |
| richards                   | 54.5 ms                                                  | 46.5 ms: 1.17x faster                                           |
| regex_dna                  | 263 ms                                                   | 226 ms: 1.16x faster                                            |
| float                      | 95.8 ms                                                  | 83.4 ms: 1.15x faster                                           |
| deepcopy_reduce            | 4.24 us                                                  | 3.71 us: 1.14x faster                                           |
| tomli_loads                | 2.67 sec                                                 | 2.33 sec: 1.14x faster                                          |
| xml_etree_parse            | 203 ms                                                   | 178 ms: 1.14x faster                                            |
| richards_super             | 60.8 ms                                                  | 53.5 ms: 1.14x faster                                           |
| scimark_sor                | 164 ms                                                   | 145 ms: 1.13x faster                                            |
| scimark_fft                | 463 ms                                                   | 409 ms: 1.13x faster                                            |
| bpe_tokeniser              | 6.02 sec                                                 | 5.39 sec: 1.12x faster                                          |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.10x faster                                            |
| telco                      | 10.5 ms                                                  | 9.50 ms: 1.10x faster                                           |
| pyflate                    | 582 ms                                                   | 532 ms: 1.09x faster                                            |
| generators                 | 40.3 ms                                                  | 37.1 ms: 1.09x faster                                           |
| xml_etree_generate         | 118 ms                                                   | 109 ms: 1.08x faster                                            |
| scimark_monte_carlo        | 87.8 ms                                                  | 81.7 ms: 1.07x faster                                           |
| regex_compile              | 134 ms                                                   | 125 ms: 1.07x faster                                            |
| pylint                     | 345 ms                                                   | 323 ms: 1.07x faster                                            |
| sqlite_synth               | 4.08 us                                                  | 3.83 us: 1.07x faster                                           |
| xml_etree_process          | 82.1 ms                                                  | 77.2 ms: 1.06x faster                                           |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                           |
| mako                       | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                           |
| json                       | 5.94 ms                                                  | 5.63 ms: 1.05x faster                                           |
| logging_silent             | 135 ns                                                   | 129 ns: 1.04x faster                                            |
| k_core                     | 2.99 sec                                                 | 2.87 sec: 1.04x faster                                          |
| html5lib                   | 65.6 ms                                                  | 62.9 ms: 1.04x faster                                           |
| go                         | 164 ms                                                   | 158 ms: 1.04x faster                                            |
| async_generators           | 500 ms                                                   | 482 ms: 1.04x faster                                            |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.03x faster                                            |
| sphinx                     | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                          |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                           |
| python_startup_no_site     | 8.79 ms                                                  | 8.63 ms: 1.02x faster                                           |
| shortest_path              | 565 ms                                                   | 585 ms: 1.03x slower                                            |
| pycparser                  | 1.34 sec                                                 | 1.39 sec: 1.03x slower                                          |
| connected_components       | 547 ms                                                   | 566 ms: 1.03x slower                                            |
| genshi_xml                 | 61.6 ms                                                  | 64.0 ms: 1.04x slower                                           |
| docutils                   | 2.96 sec                                                 | 3.11 sec: 1.05x slower                                          |
| comprehensions             | 20.8 us                                                  | 21.8 us: 1.05x slower                                           |
| sympy_str                  | 265 ms                                                   | 278 ms: 1.05x slower                                            |
| sympy_expand               | 472 ms                                                   | 498 ms: 1.05x slower                                            |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.15 ms: 1.07x slower                                           |
| create_gc_cycles           | 3.39 ms                                                  | 3.65 ms: 1.08x slower                                           |
| scimark_lu                 | 146 ms                                                   | 158 ms: 1.08x slower                                            |
| raytrace                   | 310 ms                                                   | 335 ms: 1.08x slower                                            |
| nbody                      | 118 ms                                                   | 128 ms: 1.08x slower                                            |
| crypto_pyaes               | 84.9 ms                                                  | 95.2 ms: 1.12x slower                                           |
| gc_traversal               | 5.92 ms                                                  | 6.80 ms: 1.15x slower                                           |
| pprint_pformat             | 1.99 sec                                                 | 2.30 sec: 1.16x slower                                          |
| pprint_safe_repr           | 962 ms                                                   | 1.13 sec: 1.18x slower                                          |
| many_optionals             | 626 us                                                   | 819 us: 1.31x slower                                            |
| subparsers                 | 20.3 ms                                                  | 28.5 ms: 1.40x slower                                           |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                    |

Benchmark hidden because not significant (23): pathlib, thrift, json_dumps, coverage, unpickle_pure_python, genshi_text, logging_format, deltablue, nqueens, chaos, logging_simple, sympy_sum, sympy_integrate, fannkuch, asyncio_websockets, 2to3, pidigits, json_loads, coroutines, django_template, hexiom, pickle_pure_python, typing_runtime_protocols
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250628-3.15.0a0-f528bf3-JIT/bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 98.86% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x