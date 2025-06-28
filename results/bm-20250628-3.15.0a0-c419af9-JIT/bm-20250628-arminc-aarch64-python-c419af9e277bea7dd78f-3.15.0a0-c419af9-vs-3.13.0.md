# Results vs. 3.13.0

- fork: python
- ref: c419af9e277bea7dd78f
- machine: linux-aarch64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.052x faster
- HPT reliability: 99.14%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.13 sec: 1.05x slower                                                  |
| html5lib       | 65.6 ms                                                  | 62.5 ms: 1.05x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                  |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 471 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 475 ms: 1.39x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 383 ms: 1.27x faster                                                    |
| async_tree_none            | 504 ms                                                   | 404 ms: 1.25x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 936 ms: 1.24x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 918 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 665 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 666 ms: 1.19x faster                                                    |
| async_generators           | 500 ms                                                   | 473 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 83.1 ms: 1.15x faster                                                   |
| nbody          | 118 ms                                                   | 129 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 26.5 ms: 1.23x faster                                                   |
| regex_dna      | 263 ms                                                   | 217 ms: 1.21x faster                                                    |
| regex_compile  | 134 ms                                                   | 124 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                    | 1.21x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.31 sec: 1.15x faster                                                  |
| xml_etree_parse     | 203 ms                                                   | 178 ms: 1.14x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| xml_etree_generate  | 118 ms                                                   | 109 ms: 1.09x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 78.3 ms: 1.05x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 396 us: 1.06x slower                                                    |
| Geometric mean      | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (3): json_dumps, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 13.1 ms: 1.06x faster                                                   |
| genshi_xml     | 61.6 ms                                                  | 62.5 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.66 sec: 2.08x faster                                                  |
| deepcopy                   | 479 us                                                   | 329 us: 1.45x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 471 ms: 1.41x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 37.8 us: 1.40x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 475 ms: 1.39x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 383 ms: 1.27x faster                                                    |
| async_tree_none            | 504 ms                                                   | 404 ms: 1.25x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 936 ms: 1.24x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 918 ms: 1.24x faster                                                    |
| richards                   | 54.5 ms                                                  | 44.3 ms: 1.23x faster                                                   |
| regex_v8                   | 32.5 ms                                                  | 26.5 ms: 1.23x faster                                                   |
| regex_dna                  | 263 ms                                                   | 217 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 665 ms: 1.20x faster                                                    |
| spectral_norm              | 143 ms                                                   | 119 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 666 ms: 1.19x faster                                                    |
| richards_super             | 60.8 ms                                                  | 51.3 ms: 1.18x faster                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 3.62 us: 1.17x faster                                                   |
| scimark_sor                | 164 ms                                                   | 141 ms: 1.16x faster                                                    |
| float                      | 95.8 ms                                                  | 83.1 ms: 1.15x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.31 sec: 1.15x faster                                                  |
| generators                 | 40.3 ms                                                  | 35.2 ms: 1.15x faster                                                   |
| xml_etree_parse            | 203 ms                                                   | 178 ms: 1.14x faster                                                    |
| scimark_fft                | 463 ms                                                   | 413 ms: 1.12x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.39 sec: 1.12x faster                                                  |
| telco                      | 10.5 ms                                                  | 9.38 ms: 1.12x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.66 us: 1.11x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| pyflate                    | 582 ms                                                   | 531 ms: 1.10x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.3 ms: 1.09x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 109 ms: 1.09x faster                                                    |
| pylint                     | 345 ms                                                   | 320 ms: 1.08x faster                                                    |
| regex_compile              | 134 ms                                                   | 124 ms: 1.08x faster                                                    |
| mako                       | 14.0 ms                                                  | 13.1 ms: 1.06x faster                                                   |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| async_generators           | 500 ms                                                   | 473 ms: 1.06x faster                                                    |
| go                         | 164 ms                                                   | 156 ms: 1.05x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                                  |
| html5lib                   | 65.6 ms                                                  | 62.5 ms: 1.05x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                  |
| xml_etree_process          | 82.1 ms                                                  | 78.3 ms: 1.05x faster                                                   |
| logging_format             | 8.10 us                                                  | 7.76 us: 1.04x faster                                                   |
| logging_silent             | 135 ns                                                   | 129 ns: 1.04x faster                                                    |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| genshi_xml                 | 61.6 ms                                                  | 62.5 ms: 1.02x slower                                                   |
| connected_components       | 547 ms                                                   | 563 ms: 1.03x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 203 us: 1.03x slower                                                    |
| shortest_path              | 565 ms                                                   | 585 ms: 1.03x slower                                                    |
| sympy_str                  | 265 ms                                                   | 279 ms: 1.05x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.13 sec: 1.05x slower                                                  |
| pickle_pure_python         | 374 us                                                   | 396 us: 1.06x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.08 ms: 1.06x slower                                                   |
| comprehensions             | 20.8 us                                                  | 22.4 us: 1.07x slower                                                   |
| raytrace                   | 310 ms                                                   | 333 ms: 1.08x slower                                                    |
| nbody                      | 118 ms                                                   | 129 ms: 1.09x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.75 ms: 1.11x slower                                                   |
| crypto_pyaes               | 84.9 ms                                                  | 95.3 ms: 1.12x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.93 ms: 1.17x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.34 sec: 1.18x slower                                                  |
| pprint_safe_repr           | 962 ms                                                   | 1.14 sec: 1.18x slower                                                  |
| many_optionals             | 626 us                                                   | 819 us: 1.31x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 28.4 ms: 1.40x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (26): json_dumps, pathlib, unpickle_pure_python, thrift, logging_simple, deltablue, json, chaos, coverage, sympy_integrate, meteor_contest, python_startup_no_site, asyncio_websockets, genshi_text, 2to3, pidigits, fannkuch, django_template, nqueens, json_loads, sympy_expand, coroutines, sympy_sum, hexiom, pycparser, scimark_lu
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-arminc-aarch64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 99.14% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x