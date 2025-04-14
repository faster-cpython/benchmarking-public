# Results vs. 3.13.0

- fork: python
- ref: 313b96eb8b8d0ad3bac5
- machine: linux-aarch64
- commit hash: 313b96e
- commit date: 2025-01-16
- overall geometric mean: 1.018x slower
- HPT reliability: 96.22%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.13 sec: 1.05x slower                                                   |
| Geometric mean | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 486 ms: 1.36x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 513 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 927 ms: 1.26x faster                                                     |
| async_tree_none            | 504 ms                                                   | 409 ms: 1.23x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 931 ms: 1.22x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 396 ms: 1.22x faster                                                     |
| async_generators           | 500 ms                                                   | 462 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 765 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 767 ms: 1.03x faster                                                     |
| coroutines                 | 29.4 ms                                                  | 30.7 ms: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.15x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 118 ms                                                   | 135 ms: 1.14x slower                                                     |
| pidigits       | 238 ms                                                   | 293 ms: 1.23x slower                                                     |
| Geometric mean | (ref)                                                    | 1.11x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.31 ms: 1.18x faster                                                    |
| regex_dna      | 263 ms                                                   | 243 ms: 1.08x faster                                                     |
| regex_compile  | 134 ms                                                   | 142 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.67 sec                                                 | 2.90 sec: 1.09x slower                                                   |
| json_dumps           | 14.2 ms                                                  | 15.8 ms: 1.11x slower                                                    |
| unpickle_pure_python | 265 us                                                   | 312 us: 1.18x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 449 us: 1.20x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.07x slower                                                             |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_iterparse, xml_etree_process, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 16.7 ms: 1.04x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 9.22 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.04x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 31.0 ms: 1.09x slower                                                    |
| mako            | 14.0 ms                                                  | 15.5 ms: 1.11x slower                                                    |
| genshi_xml      | 61.6 ms                                                  | 70.0 ms: 1.14x slower                                                    |
| django_template | 39.4 ms                                                  | 45.3 ms: 1.15x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.12x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 486 ms: 1.36x faster                                                     |
| deepcopy                   | 479 us                                                   | 369 us: 1.30x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 513 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 927 ms: 1.26x faster                                                     |
| async_tree_none            | 504 ms                                                   | 409 ms: 1.23x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 931 ms: 1.22x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 396 ms: 1.22x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.31 ms: 1.18x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 45.5 us: 1.17x faster                                                    |
| scimark_fft                | 463 ms                                                   | 398 ms: 1.16x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.7 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.04 ms: 1.10x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.86 us: 1.10x faster                                                    |
| spectral_norm              | 143 ms                                                   | 131 ms: 1.09x faster                                                     |
| async_generators           | 500 ms                                                   | 462 ms: 1.08x faster                                                     |
| regex_dna                  | 263 ms                                                   | 243 ms: 1.08x faster                                                     |
| coverage                   | 106 ms                                                   | 99.4 ms: 1.06x faster                                                    |
| mdp                        | 3.45 sec                                                 | 3.26 sec: 1.06x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 765 ms: 1.05x faster                                                     |
| k_core                     | 2.99 sec                                                 | 2.87 sec: 1.04x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 767 ms: 1.03x faster                                                     |
| sqlite_synth               | 4.08 us                                                  | 4.18 us: 1.02x slower                                                    |
| shortest_path              | 565 ms                                                   | 585 ms: 1.03x slower                                                     |
| connected_components       | 547 ms                                                   | 568 ms: 1.04x slower                                                     |
| python_startup             | 16.0 ms                                                  | 16.7 ms: 1.04x slower                                                    |
| nqueens                    | 105 ms                                                   | 109 ms: 1.04x slower                                                     |
| coroutines                 | 29.4 ms                                                  | 30.7 ms: 1.04x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 9.22 ms: 1.05x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.13 sec: 1.05x slower                                                   |
| typing_runtime_protocols   | 197 us                                                   | 209 us: 1.06x slower                                                     |
| meteor_contest             | 117 ms                                                   | 124 ms: 1.06x slower                                                     |
| logging_simple             | 7.25 us                                                  | 7.72 us: 1.06x slower                                                    |
| regex_compile              | 134 ms                                                   | 142 ms: 1.07x slower                                                     |
| sqlglot_optimize           | 65.2 ms                                                  | 69.6 ms: 1.07x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.62 ms: 1.07x slower                                                    |
| generators                 | 40.3 ms                                                  | 43.1 ms: 1.07x slower                                                    |
| logging_silent             | 135 ns                                                   | 144 ns: 1.07x slower                                                     |
| sqlalchemy_imperative      | 16.1 ms                                                  | 17.3 ms: 1.08x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 91.7 ms: 1.08x slower                                                    |
| genshi_text                | 28.6 ms                                                  | 31.0 ms: 1.09x slower                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.90 sec: 1.09x slower                                                   |
| sympy_expand               | 472 ms                                                   | 515 ms: 1.09x slower                                                     |
| scimark_sor                | 164 ms                                                   | 179 ms: 1.09x slower                                                     |
| sqlglot_transpile          | 1.84 ms                                                  | 2.01 ms: 1.09x slower                                                    |
| chaos                      | 70.7 ms                                                  | 77.4 ms: 1.09x slower                                                    |
| raytrace                   | 310 ms                                                   | 341 ms: 1.10x slower                                                     |
| richards_super             | 60.8 ms                                                  | 66.9 ms: 1.10x slower                                                    |
| comprehensions             | 20.8 us                                                  | 23.0 us: 1.11x slower                                                    |
| json_dumps                 | 14.2 ms                                                  | 15.8 ms: 1.11x slower                                                    |
| sympy_str                  | 265 ms                                                   | 294 ms: 1.11x slower                                                     |
| mako                       | 14.0 ms                                                  | 15.5 ms: 1.11x slower                                                    |
| sqlglot_normalize          | 131 ms                                                   | 145 ms: 1.11x slower                                                     |
| sqlglot_parse              | 1.43 ms                                                  | 1.61 ms: 1.12x slower                                                    |
| richards                   | 54.5 ms                                                  | 61.3 ms: 1.13x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.71 ms: 1.13x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.25 sec: 1.13x slower                                                   |
| genshi_xml                 | 61.6 ms                                                  | 70.0 ms: 1.14x slower                                                    |
| nbody                      | 118 ms                                                   | 135 ms: 1.14x slower                                                     |
| deltablue                  | 3.97 ms                                                  | 4.53 ms: 1.14x slower                                                    |
| django_template            | 39.4 ms                                                  | 45.3 ms: 1.15x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 1.11 sec: 1.15x slower                                                   |
| hexiom                     | 7.34 ms                                                  | 8.58 ms: 1.17x slower                                                    |
| unpickle_pure_python       | 265 us                                                   | 312 us: 1.18x slower                                                     |
| pickle_pure_python         | 374 us                                                   | 449 us: 1.20x slower                                                     |
| fannkuch                   | 478 ms                                                   | 578 ms: 1.21x slower                                                     |
| pidigits                   | 238 ms                                                   | 293 ms: 1.23x slower                                                     |
| many_optionals             | 626 us                                                   | 776 us: 1.24x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 28.9 ms: 1.42x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 6.44 sec: 798.53x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.10x slower                                                             |

Benchmark hidden because not significant (26): pylint, float, telco, sqlalchemy_declarative, sphinx, xml_etree_generate, bpe_tokeniser, html5lib, json, bench_thread_pool, thrift, asyncio_websockets, pycparser, go, xml_etree_iterparse, sympy_sum, logging_format, pyflate, xml_etree_process, sympy_integrate, json_loads, scimark_monte_carlo, 2to3, regex_v8, xml_etree_parse, scimark_lu
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250116-3.14.0a4+-313b96e-CLANG/bm-20250116-arminc-aarch64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e.json: dulwich_log

- Geometric mean (including insignificant results): 1.018x slower

# HPT report

- Reliability score: 96.22% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x