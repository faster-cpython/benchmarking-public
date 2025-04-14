# Results vs. base

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: linux-aarch64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.017x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 297 ms                                                                                                              | 306 ms: 1.03x slower                                                                                                    |
| docutils       | 2.95 sec                                                                                                            | 3.13 sec: 1.06x slower                                                                                                  |
| html5lib       | 63.3 ms                                                                                                             | 62.2 ms: 1.02x faster                                                                                                   |
| Geometric mean | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 374 ms                                                                                                              | 377 ms: 1.01x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 642 ms                                                                                                              | 649 ms: 1.01x slower                                                                                                    |
| async_tree_io              | 876 ms                                                                                                              | 886 ms: 1.01x slower                                                                                                    |
| async_tree_none            | 392 ms                                                                                                              | 398 ms: 1.01x slower                                                                                                    |
| async_tree_memoization     | 470 ms                                                                                                              | 479 ms: 1.02x slower                                                                                                    |
| async_tree_io_tg           | 890 ms                                                                                                              | 919 ms: 1.03x slower                                                                                                    |
| async_generators           | 441 ms                                                                                                              | 471 ms: 1.07x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                               | 1.01x slower                                                                                                            |

Benchmark hidden because not significant (6): coroutines, asyncio_tcp, asyncio_tcp_ssl, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 85.6 ms                                                                                                             | 81.4 ms: 1.05x faster                                                                                                   |
| Geometric mean | (ref)                                                                                                               | 1.03x faster                                                                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_v8, regex_dna, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|---------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| json_dumps          | 14.9 ms                                                                                                             | 13.9 ms: 1.07x faster                                                                                                   |
| xml_etree_generate  | 113 ms                                                                                                              | 108 ms: 1.05x faster                                                                                                    |
| tomli_loads         | 2.46 sec                                                                                                            | 2.40 sec: 1.03x faster                                                                                                  |
| xml_etree_process   | 78.4 ms                                                                                                             | 77.6 ms: 1.01x faster                                                                                                   |
| xml_etree_iterparse | 141 ms                                                                                                              | 142 ms: 1.01x slower                                                                                                    |
| pickle_pure_python  | 386 us                                                                                                              | 397 us: 1.03x slower                                                                                                    |
| Geometric mean      | (ref)                                                                                                               | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (8): unpickle, json_loads, pickle, xml_etree_parse, pickle_dict, unpickle_pure_python, unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.3 ms                                                                                                             | 16.0 ms: 1.02x faster                                                                                                   |
| python_startup_no_site | 10.2 ms                                                                                                             | 10.1 ms: 1.01x faster                                                                                                   |
| Geometric mean         | (ref)                                                                                                               | 1.01x faster                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| mako           | 14.5 ms                                                                                                             | 13.2 ms: 1.09x faster                                                                                                   |
| genshi_xml     | 59.0 ms                                                                                                             | 60.9 ms: 1.03x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                               | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 1.93 sec                                                                                                            | 1.09 sec: 1.77x faster                                                                                                  |
| mako                       | 14.5 ms                                                                                                             | 13.2 ms: 1.09x faster                                                                                                   |
| deepcopy_memo              | 39.5 us                                                                                                             | 36.3 us: 1.09x faster                                                                                                   |
| json_dumps                 | 14.9 ms                                                                                                             | 13.9 ms: 1.07x faster                                                                                                   |
| richards_super             | 57.3 ms                                                                                                             | 53.5 ms: 1.07x faster                                                                                                   |
| richards                   | 50.7 ms                                                                                                             | 48.1 ms: 1.06x faster                                                                                                   |
| float                      | 85.6 ms                                                                                                             | 81.4 ms: 1.05x faster                                                                                                   |
| xml_etree_generate         | 113 ms                                                                                                              | 108 ms: 1.05x faster                                                                                                    |
| sqlite_synth               | 3.84 us                                                                                                             | 3.68 us: 1.04x faster                                                                                                   |
| tomli_loads                | 2.46 sec                                                                                                            | 2.40 sec: 1.03x faster                                                                                                  |
| python_startup             | 16.3 ms                                                                                                             | 16.0 ms: 1.02x faster                                                                                                   |
| html5lib                   | 63.3 ms                                                                                                             | 62.2 ms: 1.02x faster                                                                                                   |
| xml_etree_process          | 78.4 ms                                                                                                             | 77.6 ms: 1.01x faster                                                                                                   |
| coverage                   | 99.0 ms                                                                                                             | 98.2 ms: 1.01x faster                                                                                                   |
| python_startup_no_site     | 10.2 ms                                                                                                             | 10.1 ms: 1.01x faster                                                                                                   |
| deltablue                  | 3.79 ms                                                                                                             | 3.81 ms: 1.01x slower                                                                                                   |
| async_tree_none_tg         | 374 ms                                                                                                              | 377 ms: 1.01x slower                                                                                                    |
| logging_format             | 7.62 us                                                                                                             | 7.70 us: 1.01x slower                                                                                                   |
| xml_etree_iterparse        | 141 ms                                                                                                              | 142 ms: 1.01x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 642 ms                                                                                                              | 649 ms: 1.01x slower                                                                                                    |
| async_tree_io              | 876 ms                                                                                                              | 886 ms: 1.01x slower                                                                                                    |
| async_tree_none            | 392 ms                                                                                                              | 398 ms: 1.01x slower                                                                                                    |
| async_tree_memoization     | 470 ms                                                                                                              | 479 ms: 1.02x slower                                                                                                    |
| connected_components       | 556 ms                                                                                                              | 569 ms: 1.02x slower                                                                                                    |
| scimark_sparse_mat_mult    | 6.35 ms                                                                                                             | 6.49 ms: 1.02x slower                                                                                                   |
| shortest_path              | 577 ms                                                                                                              | 590 ms: 1.02x slower                                                                                                    |
| pyflate                    | 554 ms                                                                                                              | 567 ms: 1.02x slower                                                                                                    |
| pickle_pure_python         | 386 us                                                                                                              | 397 us: 1.03x slower                                                                                                    |
| k_core                     | 2.78 sec                                                                                                            | 2.86 sec: 1.03x slower                                                                                                  |
| async_tree_io_tg           | 890 ms                                                                                                              | 919 ms: 1.03x slower                                                                                                    |
| 2to3                       | 297 ms                                                                                                              | 306 ms: 1.03x slower                                                                                                    |
| genshi_xml                 | 59.0 ms                                                                                                             | 60.9 ms: 1.03x slower                                                                                                   |
| sympy_str                  | 263 ms                                                                                                              | 272 ms: 1.03x slower                                                                                                    |
| sympy_sum                  | 142 ms                                                                                                              | 147 ms: 1.04x slower                                                                                                    |
| nqueens                    | 103 ms                                                                                                              | 107 ms: 1.04x slower                                                                                                    |
| sympy_expand               | 467 ms                                                                                                              | 486 ms: 1.04x slower                                                                                                    |
| sqlalchemy_imperative      | 15.5 ms                                                                                                             | 16.2 ms: 1.04x slower                                                                                                   |
| pathlib                    | 21.9 ms                                                                                                             | 23.0 ms: 1.05x slower                                                                                                   |
| docutils                   | 2.95 sec                                                                                                            | 3.13 sec: 1.06x slower                                                                                                  |
| sqlglot_v2_transpile       | 1.74 ms                                                                                                             | 1.86 ms: 1.07x slower                                                                                                   |
| async_generators           | 441 ms                                                                                                              | 471 ms: 1.07x slower                                                                                                    |
| hexiom                     | 7.30 ms                                                                                                             | 7.91 ms: 1.08x slower                                                                                                   |
| typing_runtime_protocols   | 194 us                                                                                                              | 211 us: 1.09x slower                                                                                                    |
| meteor_contest             | 113 ms                                                                                                              | 123 ms: 1.09x slower                                                                                                    |
| pycparser                  | 1.25 sec                                                                                                            | 1.38 sec: 1.11x slower                                                                                                  |
| crypto_pyaes               | 85.3 ms                                                                                                             | 94.9 ms: 1.11x slower                                                                                                   |
| sqlglot_v2_parse           | 1.40 ms                                                                                                             | 1.56 ms: 1.12x slower                                                                                                   |
| comprehensions             | 21.3 us                                                                                                             | 24.3 us: 1.14x slower                                                                                                   |
| pprint_pformat             | 1.94 sec                                                                                                            | 2.40 sec: 1.24x slower                                                                                                  |
| pprint_safe_repr           | 938 ms                                                                                                              | 1.17 sec: 1.24x slower                                                                                                  |
| go                         | 137 ms                                                                                                              | 171 ms: 1.25x slower                                                                                                    |
| unpack_sequence            | 60.4 ns                                                                                                             | 83.1 ns: 1.38x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (51): nbody, regex_v8, scimark_fft, unpickle, genshi_text, json_loads, coroutines, fannkuch, asyncio_tcp, mdp, create_gc_cycles, deepcopy, sqlglot_v2_normalize, generators, asyncio_tcp_ssl, gc_traversal, pickle, bpe_tokeniser, xml_etree_parse, pickle_dict, unpickle_pure_python, unpickle_list, bench_thread_pool, deepcopy_reduce, asyncio_websockets, logging_simple, regex_dna, async_tree_cpu_io_mixed, spectral_norm, regex_effbot, scimark_monte_carlo, pidigits, async_tree_memoization_tg, sympy_integrate, django_template, logging_silent, sphinx, json, scimark_lu, sqlglot_v2_optimize, telco, regex_compile, dulwich_log, raytrace, scimark_sor, sqlalchemy_declarative, subparsers, pylint, chaos, pickle_list, many_optionals

- Geometric mean (including insignificant results): 1.017x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x