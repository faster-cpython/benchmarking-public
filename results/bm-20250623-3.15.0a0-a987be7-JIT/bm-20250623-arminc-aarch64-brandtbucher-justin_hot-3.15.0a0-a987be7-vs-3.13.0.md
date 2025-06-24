# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-aarch64
- commit hash: a987be7
- commit date: 2025-06-23
- overall geometric mean: 1.051x faster
- HPT reliability: 99.20%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                              |
| html5lib       | 65.6 ms                                                  | 62.9 ms: 1.04x faster                                               |
| sphinx         | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                              |
| Geometric mean | (ref)                                                    | 1.01x faster                                                        |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 465 ms: 1.43x faster                                                |
| async_tree_memoization_tg  | 663 ms                                                   | 468 ms: 1.41x faster                                                |
| async_tree_io_tg           | 1.16 sec                                                 | 906 ms: 1.29x faster                                                |
| async_tree_none_tg         | 484 ms                                                   | 378 ms: 1.28x faster                                                |
| async_tree_io              | 1.14 sec                                                 | 891 ms: 1.28x faster                                                |
| async_tree_none            | 504 ms                                                   | 398 ms: 1.26x faster                                                |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 658 ms: 1.22x faster                                                |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 659 ms: 1.20x faster                                                |
| async_generators           | 500 ms                                                   | 476 ms: 1.05x faster                                                |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                        |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.3 ms: 1.16x faster                                               |
| Geometric mean | (ref)                                                    | 1.06x faster                                                        |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.95 ms: 1.29x faster                                               |
| regex_v8       | 32.5 ms                                                  | 26.7 ms: 1.22x faster                                               |
| regex_dna      | 263 ms                                                   | 218 ms: 1.20x faster                                                |
| regex_compile  | 134 ms                                                   | 121 ms: 1.11x faster                                                |
| Geometric mean | (ref)                                                    | 1.20x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|---------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.35 sec: 1.13x faster                                              |
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.13x faster                                                |
| xml_etree_iterparse | 159 ms                                                   | 145 ms: 1.10x faster                                                |
| json_dumps          | 14.2 ms                                                  | 13.3 ms: 1.07x faster                                               |
| xml_etree_generate  | 118 ms                                                   | 111 ms: 1.07x faster                                                |
| xml_etree_process   | 82.1 ms                                                  | 78.1 ms: 1.05x faster                                               |
| Geometric mean      | (ref)                                                    | 1.06x faster                                                        |

Benchmark hidden because not significant (3): unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                               |
| python_startup_no_site | 8.79 ms                                                  | 8.63 ms: 1.02x faster                                               |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.9 ms: 1.06x faster                                               |
| mako           | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                    | 1.03x faster                                                        |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.67 sec: 2.07x faster                                              |
| deepcopy_memo              | 53.0 us                                                  | 36.6 us: 1.45x faster                                               |
| async_tree_memoization     | 664 ms                                                   | 465 ms: 1.43x faster                                                |
| async_tree_memoization_tg  | 663 ms                                                   | 468 ms: 1.41x faster                                                |
| deepcopy                   | 479 us                                                   | 340 us: 1.41x faster                                                |
| regex_effbot               | 5.10 ms                                                  | 3.95 ms: 1.29x faster                                               |
| async_tree_io_tg           | 1.16 sec                                                 | 906 ms: 1.29x faster                                                |
| async_tree_none_tg         | 484 ms                                                   | 378 ms: 1.28x faster                                                |
| async_tree_io              | 1.14 sec                                                 | 891 ms: 1.28x faster                                                |
| async_tree_none            | 504 ms                                                   | 398 ms: 1.26x faster                                                |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 658 ms: 1.22x faster                                                |
| regex_v8                   | 32.5 ms                                                  | 26.7 ms: 1.22x faster                                               |
| richards                   | 54.5 ms                                                  | 45.1 ms: 1.21x faster                                               |
| regex_dna                  | 263 ms                                                   | 218 ms: 1.20x faster                                                |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 659 ms: 1.20x faster                                                |
| deepcopy_reduce            | 4.24 us                                                  | 3.58 us: 1.19x faster                                               |
| richards_super             | 60.8 ms                                                  | 51.4 ms: 1.18x faster                                               |
| float                      | 95.8 ms                                                  | 82.3 ms: 1.16x faster                                               |
| tomli_loads                | 2.67 sec                                                 | 2.35 sec: 1.13x faster                                              |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.13x faster                                                |
| telco                      | 10.5 ms                                                  | 9.38 ms: 1.12x faster                                               |
| bpe_tokeniser              | 6.02 sec                                                 | 5.40 sec: 1.11x faster                                              |
| scimark_sor                | 164 ms                                                   | 148 ms: 1.11x faster                                                |
| regex_compile              | 134 ms                                                   | 121 ms: 1.11x faster                                                |
| spectral_norm              | 143 ms                                                   | 130 ms: 1.10x faster                                                |
| generators                 | 40.3 ms                                                  | 36.6 ms: 1.10x faster                                               |
| xml_etree_iterparse        | 159 ms                                                   | 145 ms: 1.10x faster                                                |
| pyflate                    | 582 ms                                                   | 532 ms: 1.09x faster                                                |
| sqlite_synth               | 4.08 us                                                  | 3.77 us: 1.08x faster                                               |
| scimark_fft                | 463 ms                                                   | 428 ms: 1.08x faster                                                |
| thrift                     | 1.01 ms                                                  | 938 us: 1.08x faster                                                |
| scimark_monte_carlo        | 87.8 ms                                                  | 82.0 ms: 1.07x faster                                               |
| pylint                     | 345 ms                                                   | 323 ms: 1.07x faster                                                |
| json_dumps                 | 14.2 ms                                                  | 13.3 ms: 1.07x faster                                               |
| pathlib                    | 24.3 ms                                                  | 22.8 ms: 1.07x faster                                               |
| xml_etree_generate         | 118 ms                                                   | 111 ms: 1.07x faster                                                |
| genshi_text                | 28.6 ms                                                  | 26.9 ms: 1.06x faster                                               |
| mako                       | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                               |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                               |
| xml_etree_process          | 82.1 ms                                                  | 78.1 ms: 1.05x faster                                               |
| async_generators           | 500 ms                                                   | 476 ms: 1.05x faster                                                |
| nqueens                    | 105 ms                                                   | 100.0 ms: 1.05x faster                                              |
| coverage                   | 106 ms                                                   | 101 ms: 1.05x faster                                                |
| k_core                     | 2.99 sec                                                 | 2.86 sec: 1.05x faster                                              |
| html5lib                   | 65.6 ms                                                  | 62.9 ms: 1.04x faster                                               |
| sphinx                     | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                              |
| go                         | 164 ms                                                   | 159 ms: 1.03x faster                                                |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                               |
| python_startup_no_site     | 8.79 ms                                                  | 8.63 ms: 1.02x faster                                               |
| pycparser                  | 1.34 sec                                                 | 1.38 sec: 1.03x slower                                              |
| connected_components       | 547 ms                                                   | 566 ms: 1.03x slower                                                |
| sympy_expand               | 472 ms                                                   | 491 ms: 1.04x slower                                                |
| shortest_path              | 565 ms                                                   | 589 ms: 1.04x slower                                                |
| docutils                   | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                              |
| sympy_str                  | 265 ms                                                   | 281 ms: 1.06x slower                                                |
| raytrace                   | 310 ms                                                   | 329 ms: 1.06x slower                                                |
| comprehensions             | 20.8 us                                                  | 22.2 us: 1.07x slower                                               |
| typing_runtime_protocols   | 197 us                                                   | 212 us: 1.08x slower                                                |
| crypto_pyaes               | 84.9 ms                                                  | 93.9 ms: 1.11x slower                                               |
| create_gc_cycles           | 3.39 ms                                                  | 3.87 ms: 1.14x slower                                               |
| gc_traversal               | 5.92 ms                                                  | 6.95 ms: 1.17x slower                                               |
| pprint_safe_repr           | 962 ms                                                   | 1.24 sec: 1.29x slower                                              |
| pprint_pformat             | 1.99 sec                                                 | 2.58 sec: 1.30x slower                                              |
| many_optionals             | 626 us                                                   | 827 us: 1.32x slower                                                |
| subparsers                 | 20.3 ms                                                  | 28.1 ms: 1.38x slower                                               |
| logging_silent             | 135 ns                                                   | 618 ns: 4.59x slower                                                |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                        |

Benchmark hidden because not significant (22): unpickle_pure_python, json, nbody, sympy_integrate, pidigits, deltablue, asyncio_websockets, meteor_contest, chaos, genshi_xml, json_loads, coroutines, 2to3, fannkuch, logging_format, django_template, hexiom, sympy_sum, scimark_lu, logging_simple, pickle_pure_python, scimark_sparse_mat_mult
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250623-3.15.0a0-a987be7-JIT/bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 99.20% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x