# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.056x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 304 ms: 1.03x faster                                                    |
| html5lib       | 65.6 ms                                                  | 62.3 ms: 1.05x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                  |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 470 ms: 1.41x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 870 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 372 ms: 1.30x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 905 ms: 1.29x faster                                                    |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 650 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 665 ms: 1.19x faster                                                    |
| async_generators           | 500 ms                                                   | 458 ms: 1.09x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.1 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 26.8 ms: 1.21x faster                                                   |
| regex_dna      | 263 ms                                                   | 227 ms: 1.16x faster                                                    |
| regex_compile  | 134 ms                                                   | 123 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                    | 1.19x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 182 ms: 1.11x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| tomli_loads         | 2.67 sec                                                 | 2.47 sec: 1.08x faster                                                  |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (6): xml_etree_generate, json_dumps, xml_etree_process, json_loads, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 61.6 ms                                                  | 60.3 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (3): genshi_text, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                  |
| deepcopy                   | 479 us                                                   | 331 us: 1.45x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 470 ms: 1.41x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 38.2 us: 1.39x faster                                                   |
| async_tree_io              | 1.14 sec                                                 | 870 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 372 ms: 1.30x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                   |
| async_tree_io_tg           | 1.16 sec                                                 | 905 ms: 1.29x faster                                                    |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                    |
| go                         | 164 ms                                                   | 130 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 650 ms: 1.23x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 26.8 ms: 1.21x faster                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 3.55 us: 1.19x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 665 ms: 1.19x faster                                                    |
| regex_dna                  | 263 ms                                                   | 227 ms: 1.16x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 182 ms: 1.11x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| float                      | 95.8 ms                                                  | 86.1 ms: 1.11x faster                                                   |
| scimark_sor                | 164 ms                                                   | 148 ms: 1.11x faster                                                    |
| spectral_norm              | 143 ms                                                   | 130 ms: 1.11x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 79.7 ms: 1.10x faster                                                   |
| generators                 | 40.3 ms                                                  | 36.8 ms: 1.10x faster                                                   |
| async_generators           | 500 ms                                                   | 458 ms: 1.09x faster                                                    |
| pyflate                    | 582 ms                                                   | 533 ms: 1.09x faster                                                    |
| pylint                     | 345 ms                                                   | 317 ms: 1.09x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.55 sec: 1.08x faster                                                  |
| regex_compile              | 134 ms                                                   | 123 ms: 1.08x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.47 sec: 1.08x faster                                                  |
| sqlite_synth               | 4.08 us                                                  | 3.78 us: 1.08x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 22.5 ms: 1.08x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.07x faster                                                  |
| telco                      | 10.5 ms                                                  | 9.74 ms: 1.07x faster                                                   |
| scimark_fft                | 463 ms                                                   | 433 ms: 1.07x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.80 sec: 1.07x faster                                                  |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                   |
| html5lib                   | 65.6 ms                                                  | 62.3 ms: 1.05x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                  |
| sympy_integrate            | 21.4 ms                                                  | 20.4 ms: 1.05x faster                                                   |
| richards_super             | 60.8 ms                                                  | 58.3 ms: 1.04x faster                                                   |
| coverage                   | 106 ms                                                   | 102 ms: 1.04x faster                                                    |
| 2to3                       | 313 ms                                                   | 304 ms: 1.03x faster                                                    |
| genshi_xml                 | 61.6 ms                                                  | 60.3 ms: 1.02x faster                                                   |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| connected_components       | 547 ms                                                   | 560 ms: 1.02x slower                                                    |
| shortest_path              | 565 ms                                                   | 581 ms: 1.03x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.04 sec: 1.03x slower                                                  |
| logging_format             | 8.10 us                                                  | 8.39 us: 1.04x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.01 sec: 1.05x slower                                                  |
| logging_simple             | 7.25 us                                                  | 7.64 us: 1.05x slower                                                   |
| raytrace                   | 310 ms                                                   | 328 ms: 1.06x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.80 ms: 1.12x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.90 ms: 1.16x slower                                                   |
| many_optionals             | 626 us                                                   | 874 us: 1.40x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 28.6 ms: 1.41x slower                                                   |
| logging_silent             | 135 ns                                                   | 623 ns: 4.63x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (32): nqueens, xml_etree_generate, genshi_text, json_dumps, xml_etree_process, richards, fannkuch, sympy_sum, hexiom, sympy_expand, json, chaos, typing_runtime_protocols, meteor_contest, python_startup_no_site, asyncio_websockets, json_loads, crypto_pyaes, pidigits, comprehensions, mako, thrift, docutils, django_template, sympy_str, deltablue, nbody, unpickle_pure_python, coroutines, pickle_pure_python, scimark_sparse_mat_mult, scimark_lu
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x