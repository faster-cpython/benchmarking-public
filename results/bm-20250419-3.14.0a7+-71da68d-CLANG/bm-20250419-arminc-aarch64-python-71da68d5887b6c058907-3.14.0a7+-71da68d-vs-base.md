# Results vs. base

- fork: python
- ref: 71da68d5887b6c058907
- machine: linux-aarch64
- commit hash: 71da68d
- commit date: 2025-04-19
- overall geometric mean: 1.006x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250419-3.14.0a7+-71da68d/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json | results/bm-20250419-3.14.0a7+-71da68d-CLANG/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 294 ms                                                                                                              | 289 ms: 1.02x faster                                                                                                      |
| docutils       | 2.95 sec                                                                                                            | 2.90 sec: 1.01x faster                                                                                                    |
| html5lib       | 64.8 ms                                                                                                             | 58.6 ms: 1.11x faster                                                                                                     |
| sphinx         | 1.14 sec                                                                                                            | 1.11 sec: 1.03x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.04x faster                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250419-3.14.0a7+-71da68d/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json | results/bm-20250419-3.14.0a7+-71da68d-CLANG/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_generators           | 443 ms                                                                                                              | 416 ms: 1.07x faster                                                                                                      |
| async_tree_memoization_tg  | 470 ms                                                                                                              | 452 ms: 1.04x faster                                                                                                      |
| async_tree_memoization     | 469 ms                                                                                                              | 455 ms: 1.03x faster                                                                                                      |
| async_tree_io_tg           | 898 ms                                                                                                              | 871 ms: 1.03x faster                                                                                                      |
| async_tree_none_tg         | 379 ms                                                                                                              | 368 ms: 1.03x faster                                                                                                      |
| async_tree_io              | 882 ms                                                                                                              | 861 ms: 1.02x faster                                                                                                      |
| async_tree_none            | 390 ms                                                                                                              | 381 ms: 1.02x faster                                                                                                      |
| async_tree_cpu_io_mixed_tg | 652 ms                                                                                                              | 704 ms: 1.08x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 663 ms                                                                                                              | 727 ms: 1.10x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (4): coroutines, asyncio_tcp, asyncio_tcp_ssl, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250419-3.14.0a7+-71da68d/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json | results/bm-20250419-3.14.0a7+-71da68d-CLANG/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 83.2 ms                                                                                                             | 84.0 ms: 1.01x slower                                                                                                     |
| nbody          | 119 ms                                                                                                              | 126 ms: 1.06x slower                                                                                                      |
| pidigits       | 235 ms                                                                                                              | 291 ms: 1.24x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.10x slower                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250419-3.14.0a7+-71da68d/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json | results/bm-20250419-3.14.0a7+-71da68d-CLANG/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 243 ms                                                                                                              | 232 ms: 1.05x faster                                                                                                      |
| regex_v8       | 27.9 ms                                                                                                             | 30.3 ms: 1.08x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.02x slower                                                                                                              |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250419-3.14.0a7+-71da68d/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json | results/bm-20250419-3.14.0a7+-71da68d-CLANG/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json |
|---------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list       | 6.71 us                                                                                                             | 5.72 us: 1.17x faster                                                                                                     |
| xml_etree_generate  | 115 ms                                                                                                              | 104 ms: 1.10x faster                                                                                                      |
| xml_etree_process   | 81.1 ms                                                                                                             | 74.9 ms: 1.08x faster                                                                                                     |
| pickle_list         | 5.75 us                                                                                                             | 5.32 us: 1.08x faster                                                                                                     |
| unpickle            | 17.7 us                                                                                                             | 16.4 us: 1.08x faster                                                                                                     |
| pickle_dict         | 38.9 us                                                                                                             | 36.4 us: 1.07x faster                                                                                                     |
| pickle_pure_python  | 384 us                                                                                                              | 367 us: 1.05x faster                                                                                                      |
| tomli_loads         | 2.42 sec                                                                                                            | 2.35 sec: 1.03x faster                                                                                                    |
| json_loads          | 34.2 us                                                                                                             | 33.5 us: 1.02x faster                                                                                                     |
| xml_etree_iterparse | 142 ms                                                                                                              | 150 ms: 1.06x slower                                                                                                      |
| xml_etree_parse     | 179 ms                                                                                                              | 207 ms: 1.16x slower                                                                                                      |
| Geometric mean      | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (3): unpickle_pure_python, pickle, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250419-3.14.0a7+-71da68d/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json | results/bm-20250419-3.14.0a7+-71da68d-CLANG/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml     | 60.7 ms                                                                                                             | 58.6 ms: 1.04x faster                                                                                                     |
| mako           | 13.7 ms                                                                                                             | 14.0 ms: 1.02x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20250419-3.14.0a7+-71da68d/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json | results/bm-20250419-3.14.0a7+-71da68d-CLANG/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 3.58 sec                                                                                                            | 1.85 sec: 1.94x faster                                                                                                    |
| unpickle_list              | 6.71 us                                                                                                             | 5.72 us: 1.17x faster                                                                                                     |
| logging_silent             | 132 ns                                                                                                              | 114 ns: 1.16x faster                                                                                                      |
| html5lib                   | 64.8 ms                                                                                                             | 58.6 ms: 1.11x faster                                                                                                     |
| xml_etree_generate         | 115 ms                                                                                                              | 104 ms: 1.10x faster                                                                                                      |
| deepcopy_memo              | 38.9 us                                                                                                             | 35.6 us: 1.09x faster                                                                                                     |
| sqlglot_v2_parse           | 1.45 ms                                                                                                             | 1.33 ms: 1.09x faster                                                                                                     |
| richards                   | 52.9 ms                                                                                                             | 48.7 ms: 1.08x faster                                                                                                     |
| xml_etree_process          | 81.1 ms                                                                                                             | 74.9 ms: 1.08x faster                                                                                                     |
| pickle_list                | 5.75 us                                                                                                             | 5.32 us: 1.08x faster                                                                                                     |
| deepcopy_reduce            | 3.53 us                                                                                                             | 3.27 us: 1.08x faster                                                                                                     |
| pathlib                    | 22.8 ms                                                                                                             | 21.2 ms: 1.08x faster                                                                                                     |
| unpickle                   | 17.7 us                                                                                                             | 16.4 us: 1.08x faster                                                                                                     |
| generators                 | 37.8 ms                                                                                                             | 35.2 ms: 1.07x faster                                                                                                     |
| pickle_dict                | 38.9 us                                                                                                             | 36.4 us: 1.07x faster                                                                                                     |
| async_generators           | 443 ms                                                                                                              | 416 ms: 1.07x faster                                                                                                      |
| dulwich_log                | 53.5 ms                                                                                                             | 50.7 ms: 1.06x faster                                                                                                     |
| sqlglot_v2_optimize        | 61.1 ms                                                                                                             | 57.9 ms: 1.06x faster                                                                                                     |
| regex_dna                  | 243 ms                                                                                                              | 232 ms: 1.05x faster                                                                                                      |
| comprehensions             | 20.9 us                                                                                                             | 20.0 us: 1.05x faster                                                                                                     |
| bench_thread_pool          | 1.39 ms                                                                                                             | 1.32 ms: 1.05x faster                                                                                                     |
| deepcopy                   | 323 us                                                                                                              | 308 us: 1.05x faster                                                                                                      |
| pickle_pure_python         | 384 us                                                                                                              | 367 us: 1.05x faster                                                                                                      |
| hexiom                     | 7.24 ms                                                                                                             | 6.94 ms: 1.04x faster                                                                                                     |
| sympy_integrate            | 20.1 ms                                                                                                             | 19.4 ms: 1.04x faster                                                                                                     |
| async_tree_memoization_tg  | 470 ms                                                                                                              | 452 ms: 1.04x faster                                                                                                      |
| sympy_sum                  | 142 ms                                                                                                              | 136 ms: 1.04x faster                                                                                                      |
| genshi_xml                 | 60.7 ms                                                                                                             | 58.6 ms: 1.04x faster                                                                                                     |
| telco                      | 9.48 ms                                                                                                             | 9.18 ms: 1.03x faster                                                                                                     |
| async_tree_memoization     | 469 ms                                                                                                              | 455 ms: 1.03x faster                                                                                                      |
| sphinx                     | 1.14 sec                                                                                                            | 1.11 sec: 1.03x faster                                                                                                    |
| async_tree_io_tg           | 898 ms                                                                                                              | 871 ms: 1.03x faster                                                                                                      |
| async_tree_none_tg         | 379 ms                                                                                                              | 368 ms: 1.03x faster                                                                                                      |
| tomli_loads                | 2.42 sec                                                                                                            | 2.35 sec: 1.03x faster                                                                                                    |
| bpe_tokeniser              | 5.36 sec                                                                                                            | 5.23 sec: 1.02x faster                                                                                                    |
| async_tree_io              | 882 ms                                                                                                              | 861 ms: 1.02x faster                                                                                                      |
| async_tree_none            | 390 ms                                                                                                              | 381 ms: 1.02x faster                                                                                                      |
| json_loads                 | 34.2 us                                                                                                             | 33.5 us: 1.02x faster                                                                                                     |
| pyflate                    | 538 ms                                                                                                              | 527 ms: 1.02x faster                                                                                                      |
| chaos                      | 66.3 ms                                                                                                             | 65.1 ms: 1.02x faster                                                                                                     |
| 2to3                       | 294 ms                                                                                                              | 289 ms: 1.02x faster                                                                                                      |
| mdp                        | 1.63 sec                                                                                                            | 1.61 sec: 1.02x faster                                                                                                    |
| pycparser                  | 1.24 sec                                                                                                            | 1.23 sec: 1.02x faster                                                                                                    |
| docutils                   | 2.95 sec                                                                                                            | 2.90 sec: 1.01x faster                                                                                                    |
| gc_traversal               | 6.73 ms                                                                                                             | 6.64 ms: 1.01x faster                                                                                                     |
| json                       | 5.91 ms                                                                                                             | 5.84 ms: 1.01x faster                                                                                                     |
| shortest_path              | 584 ms                                                                                                              | 578 ms: 1.01x faster                                                                                                      |
| logging_format             | 7.62 us                                                                                                             | 7.56 us: 1.01x faster                                                                                                     |
| float                      | 83.2 ms                                                                                                             | 84.0 ms: 1.01x slower                                                                                                     |
| mako                       | 13.7 ms                                                                                                             | 14.0 ms: 1.02x slower                                                                                                     |
| subparsers                 | 25.3 ms                                                                                                             | 25.8 ms: 1.02x slower                                                                                                     |
| pprint_safe_repr           | 893 ms                                                                                                              | 913 ms: 1.02x slower                                                                                                      |
| connected_components       | 553 ms                                                                                                              | 569 ms: 1.03x slower                                                                                                      |
| pprint_pformat             | 1.83 sec                                                                                                            | 1.88 sec: 1.03x slower                                                                                                    |
| create_gc_cycles           | 3.59 ms                                                                                                             | 3.73 ms: 1.04x slower                                                                                                     |
| fannkuch                   | 468 ms                                                                                                              | 495 ms: 1.06x slower                                                                                                      |
| xml_etree_iterparse        | 142 ms                                                                                                              | 150 ms: 1.06x slower                                                                                                      |
| nbody                      | 119 ms                                                                                                              | 126 ms: 1.06x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 652 ms                                                                                                              | 704 ms: 1.08x slower                                                                                                      |
| regex_v8                   | 27.9 ms                                                                                                             | 30.3 ms: 1.08x slower                                                                                                     |
| async_tree_cpu_io_mixed    | 663 ms                                                                                                              | 727 ms: 1.10x slower                                                                                                      |
| xml_etree_parse            | 179 ms                                                                                                              | 207 ms: 1.16x slower                                                                                                      |
| pidigits                   | 235 ms                                                                                                              | 291 ms: 1.24x slower                                                                                                      |
| unpack_sequence            | 52.7 ns                                                                                                             | 68.6 ns: 1.30x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (39): richards_super, coroutines, genshi_text, scimark_lu, unpickle_pure_python, typing_runtime_protocols, go, spectral_norm, sympy_str, scimark_sor, pickle, sqlglot_v2_normalize, sympy_expand, pylint, sqlglot_v2_transpile, django_template, sqlite_synth, deltablue, asyncio_tcp, many_optionals, scimark_sparse_mat_mult, logging_simple, python_startup_no_site, crypto_pyaes, asyncio_tcp_ssl, python_startup, k_core, raytrace, asyncio_websockets, coverage, sqlalchemy_declarative, meteor_contest, scimark_fft, nqueens, regex_compile, scimark_monte_carlo, sqlalchemy_imperative, json_dumps, regex_effbot

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x