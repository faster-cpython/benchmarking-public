# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_nops
- machine: linux-aarch64
- commit hash: 75922b6
- commit date: 2025-06-27
- overall geometric mean: 1.051x faster
- HPT reliability: 99.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.07 sec: 1.04x slower                                            |
| html5lib       | 65.6 ms                                                  | 62.6 ms: 1.05x faster                                             |
| sphinx         | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                            |
| Geometric mean | (ref)                                                    | 1.01x faster                                                      |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.40x faster                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 477 ms: 1.39x faster                                              |
| async_tree_io              | 1.14 sec                                                 | 905 ms: 1.26x faster                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 927 ms: 1.26x faster                                              |
| async_tree_none_tg         | 484 ms                                                   | 386 ms: 1.25x faster                                              |
| async_tree_none            | 504 ms                                                   | 404 ms: 1.25x faster                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 668 ms: 1.20x faster                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 671 ms: 1.18x faster                                              |
| async_generators           | 500 ms                                                   | 484 ms: 1.03x faster                                              |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                      |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 83.1 ms: 1.15x faster                                             |
| nbody          | 118 ms                                                   | 126 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                    | 1.03x faster                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.88 ms: 1.32x faster                                             |
| regex_v8       | 32.5 ms                                                  | 26.6 ms: 1.22x faster                                             |
| regex_dna      | 263 ms                                                   | 218 ms: 1.20x faster                                              |
| regex_compile  | 134 ms                                                   | 123 ms: 1.08x faster                                              |
| Geometric mean | (ref)                                                    | 1.20x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.67 sec                                                 | 2.31 sec: 1.16x faster                                            |
| xml_etree_parse      | 203 ms                                                   | 179 ms: 1.13x faster                                              |
| xml_etree_iterparse  | 159 ms                                                   | 144 ms: 1.10x faster                                              |
| xml_etree_generate   | 118 ms                                                   | 108 ms: 1.09x faster                                              |
| unpickle_pure_python | 265 us                                                   | 248 us: 1.07x faster                                              |
| json_dumps           | 14.2 ms                                                  | 13.3 ms: 1.07x faster                                             |
| xml_etree_process    | 82.1 ms                                                  | 77.2 ms: 1.06x faster                                             |
| pickle_pure_python   | 374 us                                                   | 401 us: 1.07x slower                                              |
| Geometric mean       | (ref)                                                    | 1.07x faster                                                      |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                             |
| Geometric mean | (ref)                                                    | 1.03x faster                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.7 ms: 1.07x faster                                             |
| mako           | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                             |
| genshi_xml     | 61.6 ms                                                  | 62.4 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                    | 1.03x faster                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                            |
| deepcopy                   | 479 us                                                   | 337 us: 1.42x faster                                              |
| deepcopy_memo              | 53.0 us                                                  | 37.7 us: 1.41x faster                                             |
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.40x faster                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 477 ms: 1.39x faster                                              |
| regex_effbot               | 5.10 ms                                                  | 3.88 ms: 1.32x faster                                             |
| async_tree_io              | 1.14 sec                                                 | 905 ms: 1.26x faster                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 927 ms: 1.26x faster                                              |
| async_tree_none_tg         | 484 ms                                                   | 386 ms: 1.25x faster                                              |
| async_tree_none            | 504 ms                                                   | 404 ms: 1.25x faster                                              |
| richards                   | 54.5 ms                                                  | 44.1 ms: 1.24x faster                                             |
| regex_v8                   | 32.5 ms                                                  | 26.6 ms: 1.22x faster                                             |
| regex_dna                  | 263 ms                                                   | 218 ms: 1.20x faster                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 668 ms: 1.20x faster                                              |
| spectral_norm              | 143 ms                                                   | 120 ms: 1.20x faster                                              |
| richards_super             | 60.8 ms                                                  | 51.1 ms: 1.19x faster                                             |
| scimark_sor                | 164 ms                                                   | 139 ms: 1.18x faster                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 671 ms: 1.18x faster                                              |
| deepcopy_reduce            | 4.24 us                                                  | 3.65 us: 1.16x faster                                             |
| tomli_loads                | 2.67 sec                                                 | 2.31 sec: 1.16x faster                                            |
| float                      | 95.8 ms                                                  | 83.1 ms: 1.15x faster                                             |
| telco                      | 10.5 ms                                                  | 9.08 ms: 1.15x faster                                             |
| scimark_fft                | 463 ms                                                   | 409 ms: 1.13x faster                                              |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                              |
| bpe_tokeniser              | 6.02 sec                                                 | 5.40 sec: 1.11x faster                                            |
| generators                 | 40.3 ms                                                  | 36.5 ms: 1.11x faster                                             |
| scimark_monte_carlo        | 87.8 ms                                                  | 79.7 ms: 1.10x faster                                             |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.10x faster                                              |
| sqlite_synth               | 4.08 us                                                  | 3.72 us: 1.10x faster                                             |
| xml_etree_generate         | 118 ms                                                   | 108 ms: 1.09x faster                                              |
| pylint                     | 345 ms                                                   | 318 ms: 1.08x faster                                              |
| regex_compile              | 134 ms                                                   | 123 ms: 1.08x faster                                              |
| pyflate                    | 582 ms                                                   | 539 ms: 1.08x faster                                              |
| genshi_text                | 28.6 ms                                                  | 26.7 ms: 1.07x faster                                             |
| thrift                     | 1.01 ms                                                  | 944 us: 1.07x faster                                              |
| unpickle_pure_python       | 265 us                                                   | 248 us: 1.07x faster                                              |
| json_dumps                 | 14.2 ms                                                  | 13.3 ms: 1.07x faster                                             |
| xml_etree_process          | 82.1 ms                                                  | 77.2 ms: 1.06x faster                                             |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                             |
| mako                       | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                             |
| go                         | 164 ms                                                   | 156 ms: 1.06x faster                                              |
| html5lib                   | 65.6 ms                                                  | 62.6 ms: 1.05x faster                                             |
| k_core                     | 2.99 sec                                                 | 2.86 sec: 1.05x faster                                            |
| nqueens                    | 105 ms                                                   | 100 ms: 1.04x faster                                              |
| chaos                      | 70.7 ms                                                  | 67.8 ms: 1.04x faster                                             |
| logging_silent             | 135 ns                                                   | 129 ns: 1.04x faster                                              |
| logging_simple             | 7.25 us                                                  | 6.99 us: 1.04x faster                                             |
| logging_format             | 8.10 us                                                  | 7.82 us: 1.04x faster                                             |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.03x faster                                              |
| async_generators           | 500 ms                                                   | 484 ms: 1.03x faster                                              |
| sphinx                     | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                            |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                             |
| genshi_xml                 | 61.6 ms                                                  | 62.4 ms: 1.01x slower                                             |
| pycparser                  | 1.34 sec                                                 | 1.38 sec: 1.03x slower                                            |
| docutils                   | 2.96 sec                                                 | 3.07 sec: 1.04x slower                                            |
| comprehensions             | 20.8 us                                                  | 21.7 us: 1.04x slower                                             |
| sympy_expand               | 472 ms                                                   | 493 ms: 1.04x slower                                              |
| connected_components       | 547 ms                                                   | 572 ms: 1.05x slower                                              |
| sympy_str                  | 265 ms                                                   | 279 ms: 1.05x slower                                              |
| shortest_path              | 565 ms                                                   | 594 ms: 1.05x slower                                              |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.06 ms: 1.06x slower                                             |
| raytrace                   | 310 ms                                                   | 329 ms: 1.06x slower                                              |
| nbody                      | 118 ms                                                   | 126 ms: 1.07x slower                                              |
| pickle_pure_python         | 374 us                                                   | 401 us: 1.07x slower                                              |
| typing_runtime_protocols   | 197 us                                                   | 213 us: 1.08x slower                                              |
| crypto_pyaes               | 84.9 ms                                                  | 94.6 ms: 1.11x slower                                             |
| create_gc_cycles           | 3.39 ms                                                  | 3.84 ms: 1.13x slower                                             |
| gc_traversal               | 5.92 ms                                                  | 6.86 ms: 1.16x slower                                             |
| pprint_pformat             | 1.99 sec                                                 | 2.39 sec: 1.20x slower                                            |
| pprint_safe_repr           | 962 ms                                                   | 1.16 sec: 1.21x slower                                            |
| many_optionals             | 626 us                                                   | 830 us: 1.32x slower                                              |
| subparsers                 | 20.3 ms                                                  | 29.1 ms: 1.43x slower                                             |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                      |

Benchmark hidden because not significant (16): pathlib, json, coverage, sympy_sum, deltablue, sympy_integrate, fannkuch, python_startup_no_site, json_loads, 2to3, coroutines, asyncio_websockets, pidigits, django_template, hexiom, scimark_lu
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250627-3.15.0a0-75922b6-JIT/bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 99.50% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x