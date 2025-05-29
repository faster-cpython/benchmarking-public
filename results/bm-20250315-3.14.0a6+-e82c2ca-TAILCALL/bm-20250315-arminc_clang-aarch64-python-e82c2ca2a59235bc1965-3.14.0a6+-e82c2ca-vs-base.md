# Results vs. base

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: linux-aarch64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.015x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-CLANG/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 296 ms                                                                                                              | 291 ms: 1.02x faster                                                                                                      |
| docutils       | 2.99 sec                                                                                                            | 2.91 sec: 1.03x faster                                                                                                    |
| html5lib       | 64.3 ms                                                                                                             | 59.5 ms: 1.08x faster                                                                                                     |
| sphinx         | 1.14 sec                                                                                                            | 1.12 sec: 1.03x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.04x faster                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-CLANG/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_generators           | 451 ms                                                                                                              | 416 ms: 1.08x faster                                                                                                      |
| async_tree_none            | 388 ms                                                                                                              | 376 ms: 1.03x faster                                                                                                      |
| async_tree_memoization_tg  | 470 ms                                                                                                              | 458 ms: 1.03x faster                                                                                                      |
| async_tree_io_tg           | 911 ms                                                                                                              | 889 ms: 1.02x faster                                                                                                      |
| async_tree_memoization     | 477 ms                                                                                                              | 466 ms: 1.02x faster                                                                                                      |
| async_tree_none_tg         | 371 ms                                                                                                              | 366 ms: 1.02x faster                                                                                                      |
| async_tree_io              | 885 ms                                                                                                              | 876 ms: 1.01x faster                                                                                                      |
| asyncio_tcp_ssl            | 2.18 sec                                                                                                            | 2.16 sec: 1.01x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 650 ms                                                                                                              | 709 ms: 1.09x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 663 ms                                                                                                              | 725 ms: 1.09x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.00x faster                                                                                                              |

Benchmark hidden because not significant (3): coroutines, asyncio_websockets, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-CLANG/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 128 ms                                                                                                              | 119 ms: 1.08x faster                                                                                                      |
| float          | 87.7 ms                                                                                                             | 85.3 ms: 1.03x faster                                                                                                     |
| pidigits       | 234 ms                                                                                                              | 291 ms: 1.24x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.04x slower                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-CLANG/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 243 ms                                                                                                              | 233 ms: 1.05x faster                                                                                                      |
| regex_effbot   | 3.89 ms                                                                                                             | 4.21 ms: 1.08x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-CLANG/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|---------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list       | 6.39 us                                                                                                             | 5.68 us: 1.13x faster                                                                                                     |
| xml_etree_generate  | 115 ms                                                                                                              | 104 ms: 1.11x faster                                                                                                      |
| xml_etree_process   | 80.2 ms                                                                                                             | 74.1 ms: 1.08x faster                                                                                                     |
| pickle_dict         | 38.8 us                                                                                                             | 36.7 us: 1.06x faster                                                                                                     |
| tomli_loads         | 2.50 sec                                                                                                            | 2.37 sec: 1.05x faster                                                                                                    |
| pickle              | 15.7 us                                                                                                             | 15.0 us: 1.05x faster                                                                                                     |
| json_loads          | 34.0 us                                                                                                             | 33.1 us: 1.03x faster                                                                                                     |
| unpickle            | 17.6 us                                                                                                             | 17.2 us: 1.02x faster                                                                                                     |
| json_dumps          | 13.7 ms                                                                                                             | 13.9 ms: 1.01x slower                                                                                                     |
| xml_etree_iterparse | 141 ms                                                                                                              | 151 ms: 1.07x slower                                                                                                      |
| xml_etree_parse     | 178 ms                                                                                                              | 209 ms: 1.18x slower                                                                                                      |
| Geometric mean      | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (3): unpickle_pure_python, pickle_list, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-CLANG/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_text    | 26.7 ms                                                                                                             | 25.9 ms: 1.03x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.04x faster                                                                                                              |

Benchmark hidden because not significant (3): genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark                  | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-CLANG/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list              | 6.39 us                                                                                                             | 5.68 us: 1.13x faster                                                                                                     |
| scimark_fft                | 430 ms                                                                                                              | 388 ms: 1.11x faster                                                                                                      |
| xml_etree_generate         | 115 ms                                                                                                              | 104 ms: 1.11x faster                                                                                                      |
| logging_silent             | 133 ns                                                                                                              | 121 ns: 1.10x faster                                                                                                      |
| scimark_lu                 | 150 ms                                                                                                              | 137 ms: 1.09x faster                                                                                                      |
| async_generators           | 451 ms                                                                                                              | 416 ms: 1.08x faster                                                                                                      |
| scimark_monte_carlo        | 84.5 ms                                                                                                             | 78.0 ms: 1.08x faster                                                                                                     |
| xml_etree_process          | 80.2 ms                                                                                                             | 74.1 ms: 1.08x faster                                                                                                     |
| html5lib                   | 64.3 ms                                                                                                             | 59.5 ms: 1.08x faster                                                                                                     |
| pyflate                    | 569 ms                                                                                                              | 528 ms: 1.08x faster                                                                                                      |
| nbody                      | 128 ms                                                                                                              | 119 ms: 1.08x faster                                                                                                      |
| chaos                      | 71.3 ms                                                                                                             | 66.2 ms: 1.08x faster                                                                                                     |
| sympy_str                  | 277 ms                                                                                                              | 257 ms: 1.08x faster                                                                                                      |
| coverage                   | 100 ms                                                                                                              | 93.3 ms: 1.08x faster                                                                                                     |
| spectral_norm              | 122 ms                                                                                                              | 114 ms: 1.07x faster                                                                                                      |
| deepcopy                   | 333 us                                                                                                              | 312 us: 1.07x faster                                                                                                      |
| deepcopy_memo              | 37.9 us                                                                                                             | 35.6 us: 1.06x faster                                                                                                     |
| deepcopy_reduce            | 3.56 us                                                                                                             | 3.36 us: 1.06x faster                                                                                                     |
| pickle_dict                | 38.8 us                                                                                                             | 36.7 us: 1.06x faster                                                                                                     |
| comprehensions             | 21.3 us                                                                                                             | 20.2 us: 1.05x faster                                                                                                     |
| tomli_loads                | 2.50 sec                                                                                                            | 2.37 sec: 1.05x faster                                                                                                    |
| richards_super             | 58.9 ms                                                                                                             | 56.1 ms: 1.05x faster                                                                                                     |
| sqlglot_v2_optimize        | 62.6 ms                                                                                                             | 59.7 ms: 1.05x faster                                                                                                     |
| pickle                     | 15.7 us                                                                                                             | 15.0 us: 1.05x faster                                                                                                     |
| regex_dna                  | 243 ms                                                                                                              | 233 ms: 1.05x faster                                                                                                      |
| scimark_sparse_mat_mult    | 6.54 ms                                                                                                             | 6.25 ms: 1.04x faster                                                                                                     |
| hexiom                     | 7.52 ms                                                                                                             | 7.20 ms: 1.04x faster                                                                                                     |
| pprint_safe_repr           | 948 ms                                                                                                              | 910 ms: 1.04x faster                                                                                                      |
| sqlglot_v2_transpile       | 1.79 ms                                                                                                             | 1.72 ms: 1.04x faster                                                                                                     |
| sympy_expand               | 472 ms                                                                                                              | 455 ms: 1.04x faster                                                                                                      |
| bpe_tokeniser              | 5.65 sec                                                                                                            | 5.45 sec: 1.04x faster                                                                                                    |
| async_tree_none            | 388 ms                                                                                                              | 376 ms: 1.03x faster                                                                                                      |
| mdp                        | 3.32 sec                                                                                                            | 3.22 sec: 1.03x faster                                                                                                    |
| telco                      | 9.49 ms                                                                                                             | 9.22 ms: 1.03x faster                                                                                                     |
| json_loads                 | 34.0 us                                                                                                             | 33.1 us: 1.03x faster                                                                                                     |
| genshi_text                | 26.7 ms                                                                                                             | 25.9 ms: 1.03x faster                                                                                                     |
| docutils                   | 2.99 sec                                                                                                            | 2.91 sec: 1.03x faster                                                                                                    |
| float                      | 87.7 ms                                                                                                             | 85.3 ms: 1.03x faster                                                                                                     |
| async_tree_memoization_tg  | 470 ms                                                                                                              | 458 ms: 1.03x faster                                                                                                      |
| sphinx                     | 1.14 sec                                                                                                            | 1.12 sec: 1.03x faster                                                                                                    |
| async_tree_io_tg           | 911 ms                                                                                                              | 889 ms: 1.02x faster                                                                                                      |
| pprint_pformat             | 1.92 sec                                                                                                            | 1.88 sec: 1.02x faster                                                                                                    |
| k_core                     | 2.81 sec                                                                                                            | 2.75 sec: 1.02x faster                                                                                                    |
| async_tree_memoization     | 477 ms                                                                                                              | 466 ms: 1.02x faster                                                                                                      |
| unpickle                   | 17.6 us                                                                                                             | 17.2 us: 1.02x faster                                                                                                     |
| pycparser                  | 1.27 sec                                                                                                            | 1.24 sec: 1.02x faster                                                                                                    |
| gc_traversal               | 6.64 ms                                                                                                             | 6.52 ms: 1.02x faster                                                                                                     |
| 2to3                       | 296 ms                                                                                                              | 291 ms: 1.02x faster                                                                                                      |
| deltablue                  | 3.95 ms                                                                                                             | 3.88 ms: 1.02x faster                                                                                                     |
| bench_thread_pool          | 1.33 ms                                                                                                             | 1.31 ms: 1.02x faster                                                                                                     |
| async_tree_none_tg         | 371 ms                                                                                                              | 366 ms: 1.02x faster                                                                                                      |
| dulwich_log                | 51.4 ms                                                                                                             | 50.7 ms: 1.01x faster                                                                                                     |
| json                       | 5.85 ms                                                                                                             | 5.78 ms: 1.01x faster                                                                                                     |
| async_tree_io              | 885 ms                                                                                                              | 876 ms: 1.01x faster                                                                                                      |
| asyncio_tcp_ssl            | 2.18 sec                                                                                                            | 2.16 sec: 1.01x faster                                                                                                    |
| logging_simple             | 6.95 us                                                                                                             | 7.00 us: 1.01x slower                                                                                                     |
| logging_format             | 7.60 us                                                                                                             | 7.67 us: 1.01x slower                                                                                                     |
| json_dumps                 | 13.7 ms                                                                                                             | 13.9 ms: 1.01x slower                                                                                                     |
| create_gc_cycles           | 3.54 ms                                                                                                             | 3.65 ms: 1.03x slower                                                                                                     |
| xml_etree_iterparse        | 141 ms                                                                                                              | 151 ms: 1.07x slower                                                                                                      |
| regex_effbot               | 3.89 ms                                                                                                             | 4.21 ms: 1.08x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 650 ms                                                                                                              | 709 ms: 1.09x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 663 ms                                                                                                              | 725 ms: 1.09x slower                                                                                                      |
| xml_etree_parse            | 178 ms                                                                                                              | 209 ms: 1.18x slower                                                                                                      |
| unpack_sequence            | 60.1 ns                                                                                                             | 71.6 ns: 1.19x slower                                                                                                     |
| pidigits                   | 234 ms                                                                                                              | 291 ms: 1.24x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (38): bench_mp_pool, go, scimark_sor, genshi_xml, nqueens, richards, django_template, regex_compile, typing_runtime_protocols, raytrace, pathlib, unpickle_pure_python, mako, pylint, sqlglot_v2_normalize, sqlglot_v2_parse, sympy_sum, coroutines, sqlalchemy_declarative, sympy_integrate, generators, meteor_contest, shortest_path, connected_components, python_startup, python_startup_no_site, fannkuch, thrift, subparsers, asyncio_websockets, sqlite_synth, pickle_list, pickle_pure_python, many_optionals, asyncio_tcp, regex_v8, crypto_pyaes, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.015x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x