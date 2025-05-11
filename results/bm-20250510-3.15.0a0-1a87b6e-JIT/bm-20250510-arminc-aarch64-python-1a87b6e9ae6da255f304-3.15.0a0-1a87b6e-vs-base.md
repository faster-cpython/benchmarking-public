# Results vs. base

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-aarch64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.020x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| docutils       | 2.95 sec                                                                                                          | 3.09 sec: 1.05x slower                                                                                                |
| html5lib       | 62.0 ms                                                                                                           | 61.0 ms: 1.02x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.17 sec                                                                                                          | 2.22 sec: 1.02x slower                                                                                                |
| async_generators           | 460 ms                                                                                                            | 473 ms: 1.03x slower                                                                                                  |
| async_tree_io              | 887 ms                                                                                                            | 915 ms: 1.03x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 655 ms                                                                                                            | 676 ms: 1.03x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 651 ms                                                                                                            | 677 ms: 1.04x slower                                                                                                  |
| async_tree_memoization     | 465 ms                                                                                                            | 483 ms: 1.04x slower                                                                                                  |
| async_tree_none_tg         | 373 ms                                                                                                            | 389 ms: 1.04x slower                                                                                                  |
| async_tree_memoization_tg  | 463 ms                                                                                                            | 483 ms: 1.04x slower                                                                                                  |
| async_tree_io_tg           | 900 ms                                                                                                            | 945 ms: 1.05x slower                                                                                                  |
| async_tree_none            | 387 ms                                                                                                            | 412 ms: 1.06x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (3): coroutines, asyncio_websockets, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 86.3 ms                                                                                                           | 84.4 ms: 1.02x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 240 ms                                                                                                            | 232 ms: 1.03x faster                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmark hidden because not significant (3): regex_effbot, regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|---------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads         | 2.44 sec                                                                                                          | 2.37 sec: 1.03x faster                                                                                                |
| xml_etree_process   | 79.6 ms                                                                                                           | 78.8 ms: 1.01x faster                                                                                                 |
| xml_etree_iterparse | 143 ms                                                                                                            | 144 ms: 1.01x slower                                                                                                  |
| xml_etree_parse     | 180 ms                                                                                                            | 185 ms: 1.03x slower                                                                                                  |
| Geometric mean      | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (10): unpickle_list, json_loads, json_dumps, unpickle_pure_python, unpickle, pickle, pickle_dict, pickle_list, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 4.01 sec                                                                                                          | 1.40 sec: 2.87x faster                                                                                                |
| richards_super             | 58.3 ms                                                                                                           | 51.9 ms: 1.12x faster                                                                                                 |
| richards                   | 51.6 ms                                                                                                           | 46.9 ms: 1.10x faster                                                                                                 |
| telco                      | 9.70 ms                                                                                                           | 9.18 ms: 1.06x faster                                                                                                 |
| scimark_fft                | 445 ms                                                                                                            | 426 ms: 1.04x faster                                                                                                  |
| regex_dna                  | 240 ms                                                                                                            | 232 ms: 1.03x faster                                                                                                  |
| tomli_loads                | 2.44 sec                                                                                                          | 2.37 sec: 1.03x faster                                                                                                |
| float                      | 86.3 ms                                                                                                           | 84.4 ms: 1.02x faster                                                                                                 |
| bpe_tokeniser              | 5.50 sec                                                                                                          | 5.40 sec: 1.02x faster                                                                                                |
| html5lib                   | 62.0 ms                                                                                                           | 61.0 ms: 1.02x faster                                                                                                 |
| xml_etree_process          | 79.6 ms                                                                                                           | 78.8 ms: 1.01x faster                                                                                                 |
| xml_etree_iterparse        | 143 ms                                                                                                            | 144 ms: 1.01x slower                                                                                                  |
| connected_components       | 558 ms                                                                                                            | 566 ms: 1.01x slower                                                                                                  |
| k_core                     | 2.80 sec                                                                                                          | 2.84 sec: 1.02x slower                                                                                                |
| deltablue                  | 3.78 ms                                                                                                           | 3.85 ms: 1.02x slower                                                                                                 |
| asyncio_tcp_ssl            | 2.17 sec                                                                                                          | 2.22 sec: 1.02x slower                                                                                                |
| shortest_path              | 578 ms                                                                                                            | 589 ms: 1.02x slower                                                                                                  |
| async_generators           | 460 ms                                                                                                            | 473 ms: 1.03x slower                                                                                                  |
| xml_etree_parse            | 180 ms                                                                                                            | 185 ms: 1.03x slower                                                                                                  |
| async_tree_io              | 887 ms                                                                                                            | 915 ms: 1.03x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 655 ms                                                                                                            | 676 ms: 1.03x slower                                                                                                  |
| scimark_lu                 | 142 ms                                                                                                            | 148 ms: 1.04x slower                                                                                                  |
| logging_silent             | 605 ns                                                                                                            | 629 ns: 1.04x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 651 ms                                                                                                            | 677 ms: 1.04x slower                                                                                                  |
| sympy_expand               | 465 ms                                                                                                            | 483 ms: 1.04x slower                                                                                                  |
| async_tree_memoization     | 465 ms                                                                                                            | 483 ms: 1.04x slower                                                                                                  |
| sqlglot_v2_parse           | 1.44 ms                                                                                                           | 1.50 ms: 1.04x slower                                                                                                 |
| async_tree_none_tg         | 373 ms                                                                                                            | 389 ms: 1.04x slower                                                                                                  |
| async_tree_memoization_tg  | 463 ms                                                                                                            | 483 ms: 1.04x slower                                                                                                  |
| docutils                   | 2.95 sec                                                                                                          | 3.09 sec: 1.05x slower                                                                                                |
| async_tree_io_tg           | 900 ms                                                                                                            | 945 ms: 1.05x slower                                                                                                  |
| scimark_monte_carlo        | 80.6 ms                                                                                                           | 84.7 ms: 1.05x slower                                                                                                 |
| fannkuch                   | 474 ms                                                                                                            | 499 ms: 1.05x slower                                                                                                  |
| sympy_integrate            | 20.1 ms                                                                                                           | 21.1 ms: 1.05x slower                                                                                                 |
| sympy_sum                  | 141 ms                                                                                                            | 148 ms: 1.05x slower                                                                                                  |
| async_tree_none            | 387 ms                                                                                                            | 412 ms: 1.06x slower                                                                                                  |
| dulwich_log                | 54.0 ms                                                                                                           | 57.7 ms: 1.07x slower                                                                                                 |
| pycparser                  | 1.26 sec                                                                                                          | 1.36 sec: 1.07x slower                                                                                                |
| nqueens                    | 100 ms                                                                                                            | 108 ms: 1.08x slower                                                                                                  |
| typing_runtime_protocols   | 198 us                                                                                                            | 214 us: 1.08x slower                                                                                                  |
| pyflate                    | 523 ms                                                                                                            | 567 ms: 1.08x slower                                                                                                  |
| hexiom                     | 7.14 ms                                                                                                           | 7.82 ms: 1.10x slower                                                                                                 |
| crypto_pyaes               | 85.1 ms                                                                                                           | 93.7 ms: 1.10x slower                                                                                                 |
| meteor_contest             | 113 ms                                                                                                            | 125 ms: 1.11x slower                                                                                                  |
| comprehensions             | 21.2 us                                                                                                           | 23.6 us: 1.11x slower                                                                                                 |
| pprint_safe_repr           | 891 ms                                                                                                            | 1.14 sec: 1.28x slower                                                                                                |
| pprint_pformat             | 1.84 sec                                                                                                          | 2.37 sec: 1.29x slower                                                                                                |
| go                         | 129 ms                                                                                                            | 167 ms: 1.30x slower                                                                                                  |
| unpack_sequence            | 53.3 ns                                                                                                           | 82.8 ns: 1.55x slower                                                                                                 |
| Geometric mean             | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (53): unpickle_list, json_loads, gc_traversal, nbody, json_dumps, genshi_text, unpickle_pure_python, unpickle, deepcopy_memo, pickle, mako, pickle_dict, scimark_sor, pickle_list, xml_etree_generate, pickle_pure_python, coroutines, deepcopy_reduce, regex_effbot, python_startup_no_site, coverage, sqlglot_v2_normalize, thrift, subparsers, create_gc_cycles, sympy_str, regex_compile, python_startup, logging_format, asyncio_websockets, chaos, mdp, bench_thread_pool, deepcopy, generators, pidigits, sphinx, sqlglot_v2_optimize, pathlib, raytrace, regex_v8, logging_simple, genshi_xml, pylint, asyncio_tcp, scimark_sparse_mat_mult, json, 2to3, many_optionals, sqlglot_v2_transpile, spectral_norm, sqlite_synth, django_template

- Geometric mean (including insignificant results): 1.020x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.02x