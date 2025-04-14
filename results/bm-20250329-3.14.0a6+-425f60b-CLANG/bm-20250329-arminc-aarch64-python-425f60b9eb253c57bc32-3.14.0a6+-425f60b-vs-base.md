# Results vs. base

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: linux-aarch64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.010x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-CLANG/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| html5lib       | 63.3 ms                                                                                                             | 59.7 ms: 1.06x faster                                                                                                     |
| sphinx         | 1.14 sec                                                                                                            | 1.11 sec: 1.04x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-CLANG/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_generators           | 441 ms                                                                                                              | 414 ms: 1.06x faster                                                                                                      |
| async_tree_memoization     | 470 ms                                                                                                              | 455 ms: 1.03x faster                                                                                                      |
| async_tree_none            | 392 ms                                                                                                              | 382 ms: 1.03x faster                                                                                                      |
| async_tree_none_tg         | 374 ms                                                                                                              | 364 ms: 1.03x faster                                                                                                      |
| async_tree_memoization_tg  | 465 ms                                                                                                              | 453 ms: 1.03x faster                                                                                                      |
| asyncio_tcp_ssl            | 2.17 sec                                                                                                            | 2.15 sec: 1.01x faster                                                                                                    |
| async_tree_cpu_io_mixed    | 660 ms                                                                                                              | 721 ms: 1.09x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 642 ms                                                                                                              | 709 ms: 1.10x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.00x faster                                                                                                              |

Benchmark hidden because not significant (5): coroutines, async_tree_io, asyncio_websockets, asyncio_tcp, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-CLANG/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 128 ms                                                                                                              | 113 ms: 1.13x faster                                                                                                      |
| float          | 85.6 ms                                                                                                             | 83.2 ms: 1.03x faster                                                                                                     |
| pidigits       | 237 ms                                                                                                              | 293 ms: 1.24x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.02x slower                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-CLANG/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 246 ms                                                                                                              | 243 ms: 1.01x faster                                                                                                      |
| regex_effbot   | 3.99 ms                                                                                                             | 4.17 ms: 1.05x slower                                                                                                     |
| regex_v8       | 28.4 ms                                                                                                             | 30.3 ms: 1.07x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.02x slower                                                                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-CLANG/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|---------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list       | 6.35 us                                                                                                             | 5.71 us: 1.11x faster                                                                                                     |
| json_dumps          | 14.9 ms                                                                                                             | 13.9 ms: 1.07x faster                                                                                                     |
| unpickle            | 18.0 us                                                                                                             | 16.9 us: 1.07x faster                                                                                                     |
| xml_etree_process   | 78.4 ms                                                                                                             | 74.2 ms: 1.06x faster                                                                                                     |
| json_loads          | 35.0 us                                                                                                             | 33.3 us: 1.05x faster                                                                                                     |
| tomli_loads         | 2.46 sec                                                                                                            | 2.39 sec: 1.03x faster                                                                                                    |
| pickle_pure_python  | 386 us                                                                                                              | 381 us: 1.01x faster                                                                                                      |
| xml_etree_iterparse | 141 ms                                                                                                              | 148 ms: 1.05x slower                                                                                                      |
| xml_etree_parse     | 173 ms                                                                                                              | 202 ms: 1.17x slower                                                                                                      |
| Geometric mean      | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (5): xml_etree_generate, pickle_dict, pickle, unpickle_pure_python, pickle_list

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-CLANG/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako           | 14.5 ms                                                                                                             | 14.3 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-CLANG/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| nbody                      | 128 ms                                                                                                              | 113 ms: 1.13x faster                                                                                                      |
| logging_silent             | 128 ns                                                                                                              | 115 ns: 1.12x faster                                                                                                      |
| spectral_norm              | 125 ms                                                                                                              | 112 ms: 1.12x faster                                                                                                      |
| unpickle_list              | 6.35 us                                                                                                             | 5.71 us: 1.11x faster                                                                                                     |
| scimark_fft                | 422 ms                                                                                                              | 382 ms: 1.10x faster                                                                                                      |
| deepcopy                   | 340 us                                                                                                              | 309 us: 1.10x faster                                                                                                      |
| deepcopy_memo              | 39.5 us                                                                                                             | 36.2 us: 1.09x faster                                                                                                     |
| scimark_monte_carlo        | 83.0 ms                                                                                                             | 76.5 ms: 1.08x faster                                                                                                     |
| deepcopy_reduce            | 3.68 us                                                                                                             | 3.40 us: 1.08x faster                                                                                                     |
| dulwich_log                | 53.7 ms                                                                                                             | 49.7 ms: 1.08x faster                                                                                                     |
| json_dumps                 | 14.9 ms                                                                                                             | 13.9 ms: 1.07x faster                                                                                                     |
| unpickle                   | 18.0 us                                                                                                             | 16.9 us: 1.07x faster                                                                                                     |
| async_generators           | 441 ms                                                                                                              | 414 ms: 1.06x faster                                                                                                      |
| comprehensions             | 21.3 us                                                                                                             | 20.0 us: 1.06x faster                                                                                                     |
| pyflate                    | 554 ms                                                                                                              | 521 ms: 1.06x faster                                                                                                      |
| scimark_sor                | 147 ms                                                                                                              | 138 ms: 1.06x faster                                                                                                      |
| html5lib                   | 63.3 ms                                                                                                             | 59.7 ms: 1.06x faster                                                                                                     |
| telco                      | 9.58 ms                                                                                                             | 9.05 ms: 1.06x faster                                                                                                     |
| xml_etree_process          | 78.4 ms                                                                                                             | 74.2 ms: 1.06x faster                                                                                                     |
| scimark_sparse_mat_mult    | 6.35 ms                                                                                                             | 6.02 ms: 1.05x faster                                                                                                     |
| chaos                      | 69.3 ms                                                                                                             | 65.8 ms: 1.05x faster                                                                                                     |
| json_loads                 | 35.0 us                                                                                                             | 33.3 us: 1.05x faster                                                                                                     |
| richards                   | 50.7 ms                                                                                                             | 48.3 ms: 1.05x faster                                                                                                     |
| scimark_lu                 | 140 ms                                                                                                              | 134 ms: 1.05x faster                                                                                                      |
| richards_super             | 57.3 ms                                                                                                             | 54.9 ms: 1.04x faster                                                                                                     |
| bpe_tokeniser              | 5.55 sec                                                                                                            | 5.33 sec: 1.04x faster                                                                                                    |
| sphinx                     | 1.14 sec                                                                                                            | 1.11 sec: 1.04x faster                                                                                                    |
| coverage                   | 99.0 ms                                                                                                             | 95.6 ms: 1.04x faster                                                                                                     |
| pathlib                    | 21.9 ms                                                                                                             | 21.2 ms: 1.03x faster                                                                                                     |
| mdp                        | 1.65 sec                                                                                                            | 1.59 sec: 1.03x faster                                                                                                    |
| async_tree_memoization     | 470 ms                                                                                                              | 455 ms: 1.03x faster                                                                                                      |
| tomli_loads                | 2.46 sec                                                                                                            | 2.39 sec: 1.03x faster                                                                                                    |
| float                      | 85.6 ms                                                                                                             | 83.2 ms: 1.03x faster                                                                                                     |
| async_tree_none            | 392 ms                                                                                                              | 382 ms: 1.03x faster                                                                                                      |
| async_tree_none_tg         | 374 ms                                                                                                              | 364 ms: 1.03x faster                                                                                                      |
| sqlglot_v2_transpile       | 1.74 ms                                                                                                             | 1.69 ms: 1.03x faster                                                                                                     |
| async_tree_memoization_tg  | 465 ms                                                                                                              | 453 ms: 1.03x faster                                                                                                      |
| pprint_pformat             | 1.94 sec                                                                                                            | 1.90 sec: 1.02x faster                                                                                                    |
| pickle_pure_python         | 386 us                                                                                                              | 381 us: 1.01x faster                                                                                                      |
| regex_dna                  | 246 ms                                                                                                              | 243 ms: 1.01x faster                                                                                                      |
| mako                       | 14.5 ms                                                                                                             | 14.3 ms: 1.01x faster                                                                                                     |
| logging_format             | 7.62 us                                                                                                             | 7.55 us: 1.01x faster                                                                                                     |
| asyncio_tcp_ssl            | 2.17 sec                                                                                                            | 2.15 sec: 1.01x faster                                                                                                    |
| deltablue                  | 3.79 ms                                                                                                             | 3.81 ms: 1.01x slower                                                                                                     |
| meteor_contest             | 113 ms                                                                                                              | 114 ms: 1.01x slower                                                                                                      |
| regex_effbot               | 3.99 ms                                                                                                             | 4.17 ms: 1.05x slower                                                                                                     |
| create_gc_cycles           | 3.63 ms                                                                                                             | 3.80 ms: 1.05x slower                                                                                                     |
| xml_etree_iterparse        | 141 ms                                                                                                              | 148 ms: 1.05x slower                                                                                                      |
| regex_v8                   | 28.4 ms                                                                                                             | 30.3 ms: 1.07x slower                                                                                                     |
| async_tree_cpu_io_mixed    | 660 ms                                                                                                              | 721 ms: 1.09x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 642 ms                                                                                                              | 709 ms: 1.10x slower                                                                                                      |
| xml_etree_parse            | 173 ms                                                                                                              | 202 ms: 1.17x slower                                                                                                      |
| unpack_sequence            | 60.4 ns                                                                                                             | 72.3 ns: 1.20x slower                                                                                                     |
| pidigits                   | 237 ms                                                                                                              | 293 ms: 1.24x slower                                                                                                      |
| bench_mp_pool              | 1.93 sec                                                                                                            | 2.90 sec: 1.50x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                               | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (48): xml_etree_generate, pickle_dict, sqlglot_v2_normalize, sympy_integrate, coroutines, genshi_text, pickle, generators, unpickle_pure_python, pylint, typing_runtime_protocols, raytrace, django_template, many_optionals, nqueens, bench_thread_pool, 2to3, sqlglot_v2_parse, sympy_expand, hexiom, fannkuch, sqlglot_v2_optimize, go, shortest_path, docutils, async_tree_io, sympy_sum, pickle_list, pprint_safe_repr, python_startup, genshi_xml, asyncio_websockets, regex_compile, k_core, python_startup_no_site, pycparser, subparsers, sympy_str, sqlalchemy_declarative, sqlite_synth, asyncio_tcp, gc_traversal, async_tree_io_tg, logging_simple, json, connected_components, crypto_pyaes, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x