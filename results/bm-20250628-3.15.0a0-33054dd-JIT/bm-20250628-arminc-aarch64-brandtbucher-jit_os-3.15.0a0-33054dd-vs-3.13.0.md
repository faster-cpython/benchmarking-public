# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_os
- machine: linux-aarch64
- commit hash: 33054dd
- commit date: 2025-06-28
- overall geometric mean: 1.049x faster
- HPT reliability: 99.39%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.11 sec: 1.05x slower                                          |
| html5lib       | 65.6 ms                                                  | 62.8 ms: 1.05x faster                                           |
| sphinx         | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                          |
| Geometric mean | (ref)                                                    | 1.01x faster                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 473 ms: 1.40x faster                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 473 ms: 1.40x faster                                            |
| async_tree_none_tg         | 484 ms                                                   | 383 ms: 1.27x faster                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 924 ms: 1.26x faster                                            |
| async_tree_io              | 1.14 sec                                                 | 908 ms: 1.26x faster                                            |
| async_tree_none            | 504 ms                                                   | 402 ms: 1.25x faster                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 666 ms: 1.20x faster                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 672 ms: 1.17x faster                                            |
| async_generators           | 500 ms                                                   | 479 ms: 1.04x faster                                            |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 83.7 ms: 1.14x faster                                           |
| nbody          | 118 ms                                                   | 129 ms: 1.09x slower                                            |
| Geometric mean | (ref)                                                    | 1.02x faster                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.80 ms: 1.34x faster                                           |
| regex_v8       | 32.5 ms                                                  | 26.4 ms: 1.23x faster                                           |
| regex_dna      | 263 ms                                                   | 224 ms: 1.18x faster                                            |
| regex_compile  | 134 ms                                                   | 122 ms: 1.09x faster                                            |
| Geometric mean | (ref)                                                    | 1.21x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.32 sec: 1.15x faster                                          |
| xml_etree_parse     | 203 ms                                                   | 177 ms: 1.15x faster                                            |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                            |
| xml_etree_generate  | 118 ms                                                   | 108 ms: 1.10x faster                                            |
| xml_etree_process   | 82.1 ms                                                  | 77.6 ms: 1.06x faster                                           |
| pickle_pure_python  | 374 us                                                   | 397 us: 1.06x slower                                            |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                    |

Benchmark hidden because not significant (3): unpickle_pure_python, json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                           |
| Geometric mean | (ref)                                                    | 1.03x faster                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 13.1 ms: 1.07x faster                                           |
| genshi_xml     | 61.6 ms                                                  | 62.8 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                    | 1.02x faster                                                    |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.69 sec: 2.04x faster                                          |
| deepcopy_memo              | 53.0 us                                                  | 36.3 us: 1.46x faster                                           |
| deepcopy                   | 479 us                                                   | 336 us: 1.42x faster                                            |
| async_tree_memoization     | 664 ms                                                   | 473 ms: 1.40x faster                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 473 ms: 1.40x faster                                            |
| regex_effbot               | 5.10 ms                                                  | 3.80 ms: 1.34x faster                                           |
| async_tree_none_tg         | 484 ms                                                   | 383 ms: 1.27x faster                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 924 ms: 1.26x faster                                            |
| async_tree_io              | 1.14 sec                                                 | 908 ms: 1.26x faster                                            |
| async_tree_none            | 504 ms                                                   | 402 ms: 1.25x faster                                            |
| regex_v8                   | 32.5 ms                                                  | 26.4 ms: 1.23x faster                                           |
| spectral_norm              | 143 ms                                                   | 117 ms: 1.23x faster                                            |
| richards                   | 54.5 ms                                                  | 44.7 ms: 1.22x faster                                           |
| richards_super             | 60.8 ms                                                  | 50.4 ms: 1.21x faster                                           |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 666 ms: 1.20x faster                                            |
| deepcopy_reduce            | 4.24 us                                                  | 3.56 us: 1.19x faster                                           |
| regex_dna                  | 263 ms                                                   | 224 ms: 1.18x faster                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 672 ms: 1.17x faster                                            |
| tomli_loads                | 2.67 sec                                                 | 2.32 sec: 1.15x faster                                          |
| xml_etree_parse            | 203 ms                                                   | 177 ms: 1.15x faster                                            |
| float                      | 95.8 ms                                                  | 83.7 ms: 1.14x faster                                           |
| scimark_sor                | 164 ms                                                   | 145 ms: 1.13x faster                                            |
| scimark_fft                | 463 ms                                                   | 410 ms: 1.13x faster                                            |
| generators                 | 40.3 ms                                                  | 35.9 ms: 1.12x faster                                           |
| pyflate                    | 582 ms                                                   | 520 ms: 1.12x faster                                            |
| bpe_tokeniser              | 6.02 sec                                                 | 5.40 sec: 1.11x faster                                          |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                            |
| xml_etree_generate         | 118 ms                                                   | 108 ms: 1.10x faster                                            |
| regex_compile              | 134 ms                                                   | 122 ms: 1.09x faster                                            |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.6 ms: 1.09x faster                                           |
| sqlite_synth               | 4.08 us                                                  | 3.77 us: 1.08x faster                                           |
| telco                      | 10.5 ms                                                  | 9.76 ms: 1.07x faster                                           |
| mako                       | 14.0 ms                                                  | 13.1 ms: 1.07x faster                                           |
| go                         | 164 ms                                                   | 154 ms: 1.06x faster                                            |
| pathlib                    | 24.3 ms                                                  | 22.9 ms: 1.06x faster                                           |
| xml_etree_process          | 82.1 ms                                                  | 77.6 ms: 1.06x faster                                           |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                           |
| k_core                     | 2.99 sec                                                 | 2.85 sec: 1.05x faster                                          |
| logging_format             | 8.10 us                                                  | 7.74 us: 1.05x faster                                           |
| html5lib                   | 65.6 ms                                                  | 62.8 ms: 1.05x faster                                           |
| async_generators           | 500 ms                                                   | 479 ms: 1.04x faster                                            |
| logging_silent             | 135 ns                                                   | 130 ns: 1.03x faster                                            |
| logging_simple             | 7.25 us                                                  | 7.01 us: 1.03x faster                                           |
| sphinx                     | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                          |
| genshi_xml                 | 61.6 ms                                                  | 62.8 ms: 1.02x slower                                           |
| connected_components       | 547 ms                                                   | 573 ms: 1.05x slower                                            |
| docutils                   | 2.96 sec                                                 | 3.11 sec: 1.05x slower                                          |
| comprehensions             | 20.8 us                                                  | 21.8 us: 1.05x slower                                           |
| shortest_path              | 565 ms                                                   | 594 ms: 1.05x slower                                            |
| pickle_pure_python         | 374 us                                                   | 397 us: 1.06x slower                                            |
| sympy_str                  | 265 ms                                                   | 282 ms: 1.06x slower                                            |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.10 ms: 1.07x slower                                           |
| raytrace                   | 310 ms                                                   | 335 ms: 1.08x slower                                            |
| nbody                      | 118 ms                                                   | 129 ms: 1.09x slower                                            |
| typing_runtime_protocols   | 197 us                                                   | 214 us: 1.09x slower                                            |
| crypto_pyaes               | 84.9 ms                                                  | 93.2 ms: 1.10x slower                                           |
| gc_traversal               | 5.92 ms                                                  | 6.91 ms: 1.17x slower                                           |
| pprint_pformat             | 1.99 sec                                                 | 2.32 sec: 1.17x slower                                          |
| create_gc_cycles           | 3.39 ms                                                  | 3.97 ms: 1.17x slower                                           |
| pprint_safe_repr           | 962 ms                                                   | 1.15 sec: 1.20x slower                                          |
| many_optionals             | 626 us                                                   | 835 us: 1.33x slower                                            |
| subparsers                 | 20.3 ms                                                  | 28.6 ms: 1.41x slower                                           |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                    |

Benchmark hidden because not significant (26): pylint, genshi_text, json, fannkuch, unpickle_pure_python, coverage, thrift, deltablue, chaos, nqueens, python_startup_no_site, pidigits, meteor_contest, sympy_integrate, asyncio_websockets, djangocms, json_loads, hexiom, 2to3, sympy_sum, django_template, json_dumps, pycparser, sympy_expand, coroutines, scimark_lu
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250628-3.15.0a0-33054dd-JIT/bm-20250628-arminc-aarch64-brandtbucher-jit_os-3.15.0a0-33054dd.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 99.39% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x