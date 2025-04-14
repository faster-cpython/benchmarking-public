# Results vs. base

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-aarch64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.021x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| html5lib       | 64.6 ms                                                                                                             | 59.9 ms: 1.08x faster                                                                                                     |
| sphinx         | 1.18 sec                                                                                                            | 1.13 sec: 1.05x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.05x faster                                                                                                              |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_generators           | 459 ms                                                                                                              | 415 ms: 1.11x faster                                                                                                      |
| async_tree_io              | 929 ms                                                                                                              | 904 ms: 1.03x faster                                                                                                      |
| async_tree_cpu_io_mixed    | 681 ms                                                                                                              | 745 ms: 1.09x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 671 ms                                                                                                              | 735 ms: 1.10x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.00x faster                                                                                                              |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, coroutines, asyncio_websockets, asyncio_tcp_ssl, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 238 ms                                                                                                              | 306 ms: 1.28x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.07x slower                                                                                                              |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 262 ms                                                                                                              | 250 ms: 1.05x faster                                                                                                      |
| regex_v8       | 31.6 ms                                                                                                             | 34.2 ms: 1.08x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list        | 6.87 us                                                                                                             | 5.83 us: 1.18x faster                                                                                                     |
| xml_etree_process    | 82.6 ms                                                                                                             | 74.8 ms: 1.10x faster                                                                                                     |
| unpickle             | 18.2 us                                                                                                             | 16.6 us: 1.10x faster                                                                                                     |
| unpickle_pure_python | 276 us                                                                                                              | 255 us: 1.08x faster                                                                                                      |
| pickle_dict          | 39.7 us                                                                                                             | 36.7 us: 1.08x faster                                                                                                     |
| tomli_loads          | 2.56 sec                                                                                                            | 2.47 sec: 1.03x faster                                                                                                    |
| json_dumps           | 13.9 ms                                                                                                             | 14.5 ms: 1.04x slower                                                                                                     |
| xml_etree_parse      | 182 ms                                                                                                              | 212 ms: 1.16x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (6): xml_etree_generate, pickle_list, pickle_pure_python, json_loads, pickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml     | 64.9 ms                                                                                                             | 60.1 ms: 1.08x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.04x faster                                                                                                              |

Benchmark hidden because not significant (3): mako, django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| logging_silent             | 135 ns                                                                                                              | 112 ns: 1.20x faster                                                                                                      |
| unpickle_list              | 6.87 us                                                                                                             | 5.83 us: 1.18x faster                                                                                                     |
| deepcopy_reduce            | 3.83 us                                                                                                             | 3.28 us: 1.17x faster                                                                                                     |
| deepcopy_memo              | 40.6 us                                                                                                             | 35.6 us: 1.14x faster                                                                                                     |
| deepcopy                   | 361 us                                                                                                              | 318 us: 1.14x faster                                                                                                      |
| spectral_norm              | 126 ms                                                                                                              | 111 ms: 1.13x faster                                                                                                      |
| typing_runtime_protocols   | 209 us                                                                                                              | 186 us: 1.12x faster                                                                                                      |
| scimark_monte_carlo        | 85.9 ms                                                                                                             | 76.8 ms: 1.12x faster                                                                                                     |
| scimark_fft                | 429 ms                                                                                                              | 386 ms: 1.11x faster                                                                                                      |
| async_generators           | 459 ms                                                                                                              | 415 ms: 1.11x faster                                                                                                      |
| xml_etree_process          | 82.6 ms                                                                                                             | 74.8 ms: 1.10x faster                                                                                                     |
| richards                   | 53.3 ms                                                                                                             | 48.5 ms: 1.10x faster                                                                                                     |
| comprehensions             | 21.5 us                                                                                                             | 19.5 us: 1.10x faster                                                                                                     |
| unpickle                   | 18.2 us                                                                                                             | 16.6 us: 1.10x faster                                                                                                     |
| unpickle_pure_python       | 276 us                                                                                                              | 255 us: 1.08x faster                                                                                                      |
| genshi_xml                 | 64.9 ms                                                                                                             | 60.1 ms: 1.08x faster                                                                                                     |
| pickle_dict                | 39.7 us                                                                                                             | 36.7 us: 1.08x faster                                                                                                     |
| html5lib                   | 64.6 ms                                                                                                             | 59.9 ms: 1.08x faster                                                                                                     |
| logging_simple             | 7.47 us                                                                                                             | 6.94 us: 1.08x faster                                                                                                     |
| scimark_sor                | 155 ms                                                                                                              | 144 ms: 1.07x faster                                                                                                      |
| richards_super             | 59.1 ms                                                                                                             | 55.0 ms: 1.07x faster                                                                                                     |
| logging_format             | 8.03 us                                                                                                             | 7.49 us: 1.07x faster                                                                                                     |
| pyflate                    | 564 ms                                                                                                              | 527 ms: 1.07x faster                                                                                                      |
| gc_traversal               | 7.33 ms                                                                                                             | 6.87 ms: 1.07x faster                                                                                                     |
| sympy_sum                  | 148 ms                                                                                                              | 139 ms: 1.07x faster                                                                                                      |
| telco                      | 9.81 ms                                                                                                             | 9.22 ms: 1.06x faster                                                                                                     |
| hexiom                     | 7.49 ms                                                                                                             | 7.04 ms: 1.06x faster                                                                                                     |
| bpe_tokeniser              | 5.77 sec                                                                                                            | 5.42 sec: 1.06x faster                                                                                                    |
| sqlglot_transpile          | 1.79 ms                                                                                                             | 1.69 ms: 1.06x faster                                                                                                     |
| raytrace                   | 326 ms                                                                                                              | 308 ms: 1.06x faster                                                                                                      |
| pprint_pformat             | 2.03 sec                                                                                                            | 1.92 sec: 1.05x faster                                                                                                    |
| nqueens                    | 104 ms                                                                                                              | 98.6 ms: 1.05x faster                                                                                                     |
| mdp                        | 3.44 sec                                                                                                            | 3.27 sec: 1.05x faster                                                                                                    |
| coverage                   | 98.7 ms                                                                                                             | 94.0 ms: 1.05x faster                                                                                                     |
| sphinx                     | 1.18 sec                                                                                                            | 1.13 sec: 1.05x faster                                                                                                    |
| regex_dna                  | 262 ms                                                                                                              | 250 ms: 1.05x faster                                                                                                      |
| pprint_safe_repr           | 978 ms                                                                                                              | 934 ms: 1.05x faster                                                                                                      |
| bench_thread_pool          | 1.32 ms                                                                                                             | 1.27 ms: 1.04x faster                                                                                                     |
| tomli_loads                | 2.56 sec                                                                                                            | 2.47 sec: 1.03x faster                                                                                                    |
| k_core                     | 2.92 sec                                                                                                            | 2.83 sec: 1.03x faster                                                                                                    |
| scimark_sparse_mat_mult    | 6.32 ms                                                                                                             | 6.12 ms: 1.03x faster                                                                                                     |
| async_tree_io              | 929 ms                                                                                                              | 904 ms: 1.03x faster                                                                                                      |
| json_dumps                 | 13.9 ms                                                                                                             | 14.5 ms: 1.04x slower                                                                                                     |
| regex_v8                   | 31.6 ms                                                                                                             | 34.2 ms: 1.08x slower                                                                                                     |
| async_tree_cpu_io_mixed    | 681 ms                                                                                                              | 745 ms: 1.09x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 671 ms                                                                                                              | 735 ms: 1.10x slower                                                                                                      |
| xml_etree_parse            | 182 ms                                                                                                              | 212 ms: 1.16x slower                                                                                                      |
| pidigits                   | 238 ms                                                                                                              | 306 ms: 1.28x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (56): sqlglot_optimize, xml_etree_generate, bench_mp_pool, sympy_integrate, unpack_sequence, 2to3, regex_compile, nbody, thrift, chaos, pickle_list, sqlglot_parse, go, sympy_str, deltablue, pickle_pure_python, mako, sympy_expand, async_tree_memoization, dulwich_log, pathlib, django_template, genshi_text, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, connected_components, sqlglot_normalize, json_loads, pycparser, async_tree_none, sqlite_synth, float, docutils, many_optionals, shortest_path, sqlalchemy_declarative, subparsers, fannkuch, generators, coroutines, python_startup, asyncio_websockets, meteor_contest, python_startup_no_site, crypto_pyaes, json, asyncio_tcp_ssl, pickle, pylint, asyncio_tcp, scimark_lu, create_gc_cycles, xml_etree_iterparse, regex_effbot, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.021x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x