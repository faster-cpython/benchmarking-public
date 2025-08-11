# Results vs. base

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-aarch64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.014x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 299 ms                                                                                                            | 314 ms: 1.05x slower                                                                                                  |
| docutils       | 2.90 sec                                                                                                          | 3.12 sec: 1.08x slower                                                                                                |
| sphinx         | 1.13 sec                                                                                                          | 1.17 sec: 1.03x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.04x slower                                                                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 645 ms                                                                                                            | 659 ms: 1.02x slower                                                                                                  |
| async_tree_io              | 866 ms                                                                                                            | 884 ms: 1.02x slower                                                                                                  |
| async_tree_none_tg         | 372 ms                                                                                                            | 380 ms: 1.02x slower                                                                                                  |
| async_tree_memoization     | 461 ms                                                                                                            | 472 ms: 1.03x slower                                                                                                  |
| async_tree_memoization_tg  | 453 ms                                                                                                            | 470 ms: 1.04x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 646 ms                                                                                                            | 672 ms: 1.04x slower                                                                                                  |
| async_tree_none            | 384 ms                                                                                                            | 399 ms: 1.04x slower                                                                                                  |
| async_generators           | 454 ms                                                                                                            | 487 ms: 1.07x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (5): asyncio_websockets, asyncio_tcp_ssl, coroutines, async_tree_io_tg, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 84.5 ms                                                                                                           | 82.3 ms: 1.03x faster                                                                                                 |
| nbody          | 119 ms                                                                                                            | 127 ms: 1.07x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 27.5 ms                                                                                                           | 26.3 ms: 1.05x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (3): regex_compile, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|---------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads         | 2.45 sec                                                                                                          | 2.33 sec: 1.05x faster                                                                                                |
| xml_etree_process   | 81.2 ms                                                                                                           | 77.2 ms: 1.05x faster                                                                                                 |
| xml_etree_iterparse | 143 ms                                                                                                            | 146 ms: 1.03x slower                                                                                                  |
| Geometric mean      | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (11): xml_etree_generate, unpickle_pure_python, pickle, unpickle_list, unpickle, json_loads, xml_etree_parse, json_dumps, pickle_list, pickle_pure_python, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.56 ms                                                                                                           | 8.64 ms: 1.01x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako           | 13.5 ms                                                                                                           | 12.7 ms: 1.06x faster                                                                                                 |
| genshi_xml     | 60.0 ms                                                                                                           | 62.9 ms: 1.05x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 5.71 sec                                                                                                          | 1.23 sec: 4.64x faster                                                                                                |
| richards                   | 52.7 ms                                                                                                           | 46.3 ms: 1.14x faster                                                                                                 |
| richards_super             | 59.8 ms                                                                                                           | 53.4 ms: 1.12x faster                                                                                                 |
| mako                       | 13.5 ms                                                                                                           | 12.7 ms: 1.06x faster                                                                                                 |
| tomli_loads                | 2.45 sec                                                                                                          | 2.33 sec: 1.05x faster                                                                                                |
| xml_etree_process          | 81.2 ms                                                                                                           | 77.2 ms: 1.05x faster                                                                                                 |
| create_gc_cycles           | 3.90 ms                                                                                                           | 3.72 ms: 1.05x faster                                                                                                 |
| regex_v8                   | 27.5 ms                                                                                                           | 26.3 ms: 1.05x faster                                                                                                 |
| scimark_fft                | 424 ms                                                                                                            | 406 ms: 1.04x faster                                                                                                  |
| pyflate                    | 534 ms                                                                                                            | 513 ms: 1.04x faster                                                                                                  |
| bpe_tokeniser              | 5.51 sec                                                                                                          | 5.36 sec: 1.03x faster                                                                                                |
| float                      | 84.5 ms                                                                                                           | 82.3 ms: 1.03x faster                                                                                                 |
| sqlite_synth               | 3.79 us                                                                                                           | 3.70 us: 1.02x faster                                                                                                 |
| deltablue                  | 3.88 ms                                                                                                           | 3.79 ms: 1.02x faster                                                                                                 |
| json                       | 5.84 ms                                                                                                           | 5.71 ms: 1.02x faster                                                                                                 |
| mdp                        | 1.66 sec                                                                                                          | 1.63 sec: 1.02x faster                                                                                                |
| python_startup_no_site     | 8.56 ms                                                                                                           | 8.64 ms: 1.01x slower                                                                                                 |
| k_core                     | 2.81 sec                                                                                                          | 2.86 sec: 1.02x slower                                                                                                |
| async_tree_cpu_io_mixed_tg | 645 ms                                                                                                            | 659 ms: 1.02x slower                                                                                                  |
| async_tree_io              | 866 ms                                                                                                            | 884 ms: 1.02x slower                                                                                                  |
| logging_format             | 7.49 us                                                                                                           | 7.65 us: 1.02x slower                                                                                                 |
| async_tree_none_tg         | 372 ms                                                                                                            | 380 ms: 1.02x slower                                                                                                  |
| async_tree_memoization     | 461 ms                                                                                                            | 472 ms: 1.03x slower                                                                                                  |
| xml_etree_iterparse        | 143 ms                                                                                                            | 146 ms: 1.03x slower                                                                                                  |
| chaos                      | 65.3 ms                                                                                                           | 67.1 ms: 1.03x slower                                                                                                 |
| sphinx                     | 1.13 sec                                                                                                          | 1.17 sec: 1.03x slower                                                                                                |
| async_tree_memoization_tg  | 453 ms                                                                                                            | 470 ms: 1.04x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 646 ms                                                                                                            | 672 ms: 1.04x slower                                                                                                  |
| async_tree_none            | 384 ms                                                                                                            | 399 ms: 1.04x slower                                                                                                  |
| meteor_contest             | 107 ms                                                                                                            | 112 ms: 1.04x slower                                                                                                  |
| logging_simple             | 6.75 us                                                                                                           | 7.04 us: 1.04x slower                                                                                                 |
| sympy_sum                  | 141 ms                                                                                                            | 148 ms: 1.05x slower                                                                                                  |
| sympy_expand               | 464 ms                                                                                                            | 486 ms: 1.05x slower                                                                                                  |
| pylint                     | 311 ms                                                                                                            | 326 ms: 1.05x slower                                                                                                  |
| genshi_xml                 | 60.0 ms                                                                                                           | 62.9 ms: 1.05x slower                                                                                                 |
| 2to3                       | 299 ms                                                                                                            | 314 ms: 1.05x slower                                                                                                  |
| sqlglot_v2_transpile       | 1.74 ms                                                                                                           | 1.83 ms: 1.05x slower                                                                                                 |
| typing_runtime_protocols   | 194 us                                                                                                            | 204 us: 1.05x slower                                                                                                  |
| crypto_pyaes               | 84.3 ms                                                                                                           | 89.2 ms: 1.06x slower                                                                                                 |
| many_optionals             | 932 us                                                                                                            | 991 us: 1.06x slower                                                                                                  |
| hexiom                     | 6.90 ms                                                                                                           | 7.35 ms: 1.07x slower                                                                                                 |
| nbody                      | 119 ms                                                                                                            | 127 ms: 1.07x slower                                                                                                  |
| async_generators           | 454 ms                                                                                                            | 487 ms: 1.07x slower                                                                                                  |
| docutils                   | 2.90 sec                                                                                                          | 3.12 sec: 1.08x slower                                                                                                |
| sqlglot_v2_parse           | 1.39 ms                                                                                                           | 1.53 ms: 1.10x slower                                                                                                 |
| pycparser                  | 1.22 sec                                                                                                          | 1.36 sec: 1.12x slower                                                                                                |
| comprehensions             | 20.0 us                                                                                                           | 22.6 us: 1.13x slower                                                                                                 |
| go                         | 127 ms                                                                                                            | 151 ms: 1.19x slower                                                                                                  |
| pprint_safe_repr           | 881 ms                                                                                                            | 1.09 sec: 1.24x slower                                                                                                |
| pprint_pformat             | 1.80 sec                                                                                                          | 2.25 sec: 1.25x slower                                                                                                |
| unpack_sequence            | 51.2 ns                                                                                                           | 71.8 ns: 1.40x slower                                                                                                 |
| Geometric mean             | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (52): xml_etree_generate, gc_traversal, unpickle_pure_python, pickle, fannkuch, pidigits, html5lib, unpickle_list, logging_silent, deepcopy, unpickle, regex_compile, bench_thread_pool, json_loads, asyncio_websockets, asyncio_tcp_ssl, spectral_norm, djangocms, regex_effbot, pathlib, subparsers, xml_etree_parse, telco, shortest_path, json_dumps, deepcopy_memo, python_startup, scimark_monte_carlo, genshi_text, connected_components, regex_dna, pickle_list, nqueens, coroutines, pickle_pure_python, async_tree_io_tg, asyncio_tcp, raytrace, sympy_str, deepcopy_reduce, generators, sqlglot_v2_optimize, scimark_sor, coverage, pickle_dict, dulwich_log, scimark_sparse_mat_mult, thrift, scimark_lu, django_template, sympy_integrate, sqlglot_v2_normalize

- Geometric mean (including insignificant results): 1.014x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x