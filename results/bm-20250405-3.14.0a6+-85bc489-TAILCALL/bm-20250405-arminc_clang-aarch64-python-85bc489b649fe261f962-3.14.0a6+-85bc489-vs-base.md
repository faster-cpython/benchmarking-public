# Results vs. base

- fork: python
- ref: 85bc489b649fe261f962
- machine: linux-aarch64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.016x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json | results/bm-20250405-3.14.0a6+-85bc489-CLANG/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 295 ms                                                                                                              | 288 ms: 1.03x faster                                                                                                      |
| docutils       | 2.99 sec                                                                                                            | 2.91 sec: 1.03x faster                                                                                                    |
| html5lib       | 65.0 ms                                                                                                             | 58.3 ms: 1.12x faster                                                                                                     |
| sphinx         | 1.15 sec                                                                                                            | 1.11 sec: 1.04x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.05x faster                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json | results/bm-20250405-3.14.0a6+-85bc489-CLANG/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 31.0 ms                                                                                                             | 28.1 ms: 1.10x faster                                                                                                     |
| async_generators           | 445 ms                                                                                                              | 409 ms: 1.09x faster                                                                                                      |
| async_tree_memoization     | 459 ms                                                                                                              | 446 ms: 1.03x faster                                                                                                      |
| async_tree_memoization_tg  | 458 ms                                                                                                              | 445 ms: 1.03x faster                                                                                                      |
| async_tree_none            | 385 ms                                                                                                              | 375 ms: 1.03x faster                                                                                                      |
| async_tree_none_tg         | 371 ms                                                                                                              | 362 ms: 1.02x faster                                                                                                      |
| async_tree_io_tg           | 879 ms                                                                                                              | 860 ms: 1.02x faster                                                                                                      |
| async_tree_io              | 872 ms                                                                                                              | 862 ms: 1.01x faster                                                                                                      |
| asyncio_tcp_ssl            | 2.15 sec                                                                                                            | 2.17 sec: 1.01x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 660 ms                                                                                                              | 715 ms: 1.08x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 641 ms                                                                                                              | 698 ms: 1.09x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (2): asyncio_websockets, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json | results/bm-20250405-3.14.0a6+-85bc489-CLANG/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 120 ms                                                                                                              | 130 ms: 1.08x slower                                                                                                      |
| pidigits       | 237 ms                                                                                                              | 290 ms: 1.23x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.10x slower                                                                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json | results/bm-20250405-3.14.0a6+-85bc489-CLANG/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 28.3 ms                                                                                                             | 30.4 ms: 1.07x slower                                                                                                     |
| regex_effbot   | 3.95 ms                                                                                                             | 4.30 ms: 1.09x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.04x slower                                                                                                              |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json | results/bm-20250405-3.14.0a6+-85bc489-CLANG/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list        | 6.48 us                                                                                                             | 5.60 us: 1.16x faster                                                                                                     |
| pickle_dict          | 38.8 us                                                                                                             | 35.4 us: 1.10x faster                                                                                                     |
| unpickle             | 17.7 us                                                                                                             | 16.6 us: 1.07x faster                                                                                                     |
| json_dumps           | 14.6 ms                                                                                                             | 13.8 ms: 1.06x faster                                                                                                     |
| xml_etree_generate   | 111 ms                                                                                                              | 105 ms: 1.06x faster                                                                                                      |
| xml_etree_process    | 80.4 ms                                                                                                             | 75.9 ms: 1.06x faster                                                                                                     |
| pickle               | 15.7 us                                                                                                             | 14.9 us: 1.05x faster                                                                                                     |
| tomli_loads          | 2.44 sec                                                                                                            | 2.33 sec: 1.05x faster                                                                                                    |
| pickle_pure_python   | 386 us                                                                                                              | 370 us: 1.04x faster                                                                                                      |
| unpickle_pure_python | 263 us                                                                                                              | 253 us: 1.04x faster                                                                                                      |
| xml_etree_iterparse  | 139 ms                                                                                                              | 150 ms: 1.08x slower                                                                                                      |
| xml_etree_parse      | 173 ms                                                                                                              | 205 ms: 1.18x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (2): pickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json | results/bm-20250405-3.14.0a6+-85bc489-CLANG/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 16.4 ms                                                                                                             | 16.2 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json | results/bm-20250405-3.14.0a6+-85bc489-CLANG/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| django_template | 41.0 ms                                                                                                             | 38.0 ms: 1.08x faster                                                                                                     |
| genshi_text     | 27.1 ms                                                                                                             | 25.6 ms: 1.06x faster                                                                                                     |
| mako            | 14.0 ms                                                                                                             | 13.9 ms: 1.01x faster                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.05x faster                                                                                                              |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json | results/bm-20250405-3.14.0a6+-85bc489-CLANG/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 8.37 sec                                                                                                            | 2.87 sec: 2.92x faster                                                                                                    |
| logging_silent             | 130 ns                                                                                                              | 111 ns: 1.16x faster                                                                                                      |
| unpickle_list              | 6.48 us                                                                                                             | 5.60 us: 1.16x faster                                                                                                     |
| html5lib                   | 65.0 ms                                                                                                             | 58.3 ms: 1.12x faster                                                                                                     |
| deepcopy                   | 332 us                                                                                                              | 299 us: 1.11x faster                                                                                                      |
| coroutines                 | 31.0 ms                                                                                                             | 28.1 ms: 1.10x faster                                                                                                     |
| richards                   | 52.9 ms                                                                                                             | 48.1 ms: 1.10x faster                                                                                                     |
| pickle_dict                | 38.8 us                                                                                                             | 35.4 us: 1.10x faster                                                                                                     |
| async_generators           | 445 ms                                                                                                              | 409 ms: 1.09x faster                                                                                                      |
| coverage                   | 102 ms                                                                                                              | 94.4 ms: 1.09x faster                                                                                                     |
| django_template            | 41.0 ms                                                                                                             | 38.0 ms: 1.08x faster                                                                                                     |
| sympy_sum                  | 144 ms                                                                                                              | 135 ms: 1.07x faster                                                                                                      |
| unpickle                   | 17.7 us                                                                                                             | 16.6 us: 1.07x faster                                                                                                     |
| deepcopy_reduce            | 3.41 us                                                                                                             | 3.20 us: 1.07x faster                                                                                                     |
| comprehensions             | 21.3 us                                                                                                             | 20.1 us: 1.06x faster                                                                                                     |
| sqlglot_v2_optimize        | 61.4 ms                                                                                                             | 57.8 ms: 1.06x faster                                                                                                     |
| json_dumps                 | 14.6 ms                                                                                                             | 13.8 ms: 1.06x faster                                                                                                     |
| scimark_sor                | 148 ms                                                                                                              | 139 ms: 1.06x faster                                                                                                      |
| genshi_text                | 27.1 ms                                                                                                             | 25.6 ms: 1.06x faster                                                                                                     |
| xml_etree_generate         | 111 ms                                                                                                              | 105 ms: 1.06x faster                                                                                                      |
| xml_etree_process          | 80.4 ms                                                                                                             | 75.9 ms: 1.06x faster                                                                                                     |
| gc_traversal               | 6.95 ms                                                                                                             | 6.58 ms: 1.06x faster                                                                                                     |
| scimark_lu                 | 143 ms                                                                                                              | 135 ms: 1.06x faster                                                                                                      |
| logging_simple             | 6.99 us                                                                                                             | 6.62 us: 1.06x faster                                                                                                     |
| logging_format             | 7.67 us                                                                                                             | 7.27 us: 1.06x faster                                                                                                     |
| deepcopy_memo              | 37.9 us                                                                                                             | 35.9 us: 1.06x faster                                                                                                     |
| bpe_tokeniser              | 5.55 sec                                                                                                            | 5.27 sec: 1.05x faster                                                                                                    |
| richards_super             | 59.0 ms                                                                                                             | 56.0 ms: 1.05x faster                                                                                                     |
| pickle                     | 15.7 us                                                                                                             | 14.9 us: 1.05x faster                                                                                                     |
| sqlglot_v2_parse           | 1.42 ms                                                                                                             | 1.35 ms: 1.05x faster                                                                                                     |
| dulwich_log                | 52.7 ms                                                                                                             | 50.1 ms: 1.05x faster                                                                                                     |
| sqlglot_v2_transpile       | 1.75 ms                                                                                                             | 1.66 ms: 1.05x faster                                                                                                     |
| tomli_loads                | 2.44 sec                                                                                                            | 2.33 sec: 1.05x faster                                                                                                    |
| sphinx                     | 1.15 sec                                                                                                            | 1.11 sec: 1.04x faster                                                                                                    |
| typing_runtime_protocols   | 195 us                                                                                                              | 187 us: 1.04x faster                                                                                                      |
| pickle_pure_python         | 386 us                                                                                                              | 370 us: 1.04x faster                                                                                                      |
| pathlib                    | 22.2 ms                                                                                                             | 21.3 ms: 1.04x faster                                                                                                     |
| sqlglot_v2_normalize       | 126 ms                                                                                                              | 120 ms: 1.04x faster                                                                                                      |
| subparsers                 | 26.2 ms                                                                                                             | 25.2 ms: 1.04x faster                                                                                                     |
| unpickle_pure_python       | 263 us                                                                                                              | 253 us: 1.04x faster                                                                                                      |
| deltablue                  | 3.87 ms                                                                                                             | 3.73 ms: 1.04x faster                                                                                                     |
| telco                      | 9.21 ms                                                                                                             | 8.88 ms: 1.04x faster                                                                                                     |
| pylint                     | 310 ms                                                                                                              | 300 ms: 1.03x faster                                                                                                      |
| scimark_fft                | 412 ms                                                                                                              | 400 ms: 1.03x faster                                                                                                      |
| async_tree_memoization     | 459 ms                                                                                                              | 446 ms: 1.03x faster                                                                                                      |
| async_tree_memoization_tg  | 458 ms                                                                                                              | 445 ms: 1.03x faster                                                                                                      |
| docutils                   | 2.99 sec                                                                                                            | 2.91 sec: 1.03x faster                                                                                                    |
| async_tree_none            | 385 ms                                                                                                              | 375 ms: 1.03x faster                                                                                                      |
| bench_thread_pool          | 1.35 ms                                                                                                             | 1.32 ms: 1.03x faster                                                                                                     |
| mdp                        | 1.65 sec                                                                                                            | 1.61 sec: 1.03x faster                                                                                                    |
| 2to3                       | 295 ms                                                                                                              | 288 ms: 1.03x faster                                                                                                      |
| async_tree_none_tg         | 371 ms                                                                                                              | 362 ms: 1.02x faster                                                                                                      |
| async_tree_io_tg           | 879 ms                                                                                                              | 860 ms: 1.02x faster                                                                                                      |
| pprint_pformat             | 1.89 sec                                                                                                            | 1.86 sec: 1.01x faster                                                                                                    |
| async_tree_io              | 872 ms                                                                                                              | 862 ms: 1.01x faster                                                                                                      |
| python_startup             | 16.4 ms                                                                                                             | 16.2 ms: 1.01x faster                                                                                                     |
| mako                       | 14.0 ms                                                                                                             | 13.9 ms: 1.01x faster                                                                                                     |
| scimark_sparse_mat_mult    | 6.55 ms                                                                                                             | 6.59 ms: 1.01x slower                                                                                                     |
| sqlite_synth               | 3.81 us                                                                                                             | 3.84 us: 1.01x slower                                                                                                     |
| asyncio_tcp_ssl            | 2.15 sec                                                                                                            | 2.17 sec: 1.01x slower                                                                                                    |
| connected_components       | 550 ms                                                                                                              | 561 ms: 1.02x slower                                                                                                      |
| create_gc_cycles           | 3.66 ms                                                                                                             | 3.76 ms: 1.03x slower                                                                                                     |
| regex_v8                   | 28.3 ms                                                                                                             | 30.4 ms: 1.07x slower                                                                                                     |
| xml_etree_iterparse        | 139 ms                                                                                                              | 150 ms: 1.08x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 660 ms                                                                                                              | 715 ms: 1.08x slower                                                                                                      |
| nbody                      | 120 ms                                                                                                              | 130 ms: 1.08x slower                                                                                                      |
| regex_effbot               | 3.95 ms                                                                                                             | 4.30 ms: 1.09x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 641 ms                                                                                                              | 698 ms: 1.09x slower                                                                                                      |
| xml_etree_parse            | 173 ms                                                                                                              | 205 ms: 1.18x slower                                                                                                      |
| pidigits                   | 237 ms                                                                                                              | 290 ms: 1.23x slower                                                                                                      |
| unpack_sequence            | 56.8 ns                                                                                                             | 71.3 ns: 1.26x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (32): spectral_norm, scimark_monte_carlo, sympy_integrate, sympy_str, genshi_xml, chaos, hexiom, many_optionals, sympy_expand, raytrace, generators, pycparser, pickle_list, k_core, go, pyflate, regex_dna, json_loads, shortest_path, crypto_pyaes, asyncio_websockets, regex_compile, python_startup_no_site, float, pprint_safe_repr, sqlalchemy_declarative, asyncio_tcp, fannkuch, json, meteor_contest, nqueens, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.016x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x