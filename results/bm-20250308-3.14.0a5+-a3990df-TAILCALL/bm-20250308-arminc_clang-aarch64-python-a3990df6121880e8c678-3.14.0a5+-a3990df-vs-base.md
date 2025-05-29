# Results vs. base

- fork: python
- ref: a3990df6121880e8c678
- machine: linux-aarch64
- commit hash: a3990df
- commit date: 2025-03-08
- overall geometric mean: 1.015x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250308-3.14.0a5+-a3990df/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json | results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 290 ms                                                                                                              | 284 ms: 1.02x faster                                                                                                      |
| docutils       | 2.89 sec                                                                                                            | 2.87 sec: 1.01x faster                                                                                                    |
| html5lib       | 59.9 ms                                                                                                             | 57.3 ms: 1.04x faster                                                                                                     |
| sphinx         | 1.11 sec                                                                                                            | 1.08 sec: 1.03x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250308-3.14.0a5+-a3990df/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json | results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_generators           | 424 ms                                                                                                              | 395 ms: 1.07x faster                                                                                                      |
| async_tree_io_tg           | 888 ms                                                                                                              | 847 ms: 1.05x faster                                                                                                      |
| async_tree_io              | 884 ms                                                                                                              | 861 ms: 1.03x faster                                                                                                      |
| async_tree_none_tg         | 366 ms                                                                                                              | 357 ms: 1.02x faster                                                                                                      |
| coroutines                 | 28.0 ms                                                                                                             | 27.4 ms: 1.02x faster                                                                                                     |
| async_tree_memoization     | 460 ms                                                                                                              | 453 ms: 1.02x faster                                                                                                      |
| async_tree_none            | 369 ms                                                                                                              | 364 ms: 1.01x faster                                                                                                      |
| async_tree_cpu_io_mixed_tg | 637 ms                                                                                                              | 703 ms: 1.10x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 642 ms                                                                                                              | 712 ms: 1.11x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.00x faster                                                                                                              |

Benchmark hidden because not significant (4): asyncio_tcp, asyncio_websockets, asyncio_tcp_ssl, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250308-3.14.0a5+-a3990df/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json | results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 116 ms                                                                                                              | 112 ms: 1.04x faster                                                                                                      |
| float          | 85.7 ms                                                                                                             | 84.4 ms: 1.01x faster                                                                                                     |
| pidigits       | 238 ms                                                                                                              | 296 ms: 1.24x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.06x slower                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250308-3.14.0a5+-a3990df/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json | results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 237 ms                                                                                                              | 245 ms: 1.03x slower                                                                                                      |
| regex_v8       | 30.8 ms                                                                                                             | 32.3 ms: 1.05x slower                                                                                                     |
| regex_effbot   | 3.88 ms                                                                                                             | 4.21 ms: 1.09x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.05x slower                                                                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250308-3.14.0a5+-a3990df/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json | results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json |
|---------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list       | 6.56 us                                                                                                             | 5.75 us: 1.14x faster                                                                                                     |
| pickle_dict         | 39.3 us                                                                                                             | 36.0 us: 1.09x faster                                                                                                     |
| xml_etree_generate  | 108 ms                                                                                                              | 100 ms: 1.08x faster                                                                                                      |
| xml_etree_process   | 77.7 ms                                                                                                             | 72.1 ms: 1.08x faster                                                                                                     |
| unpickle            | 17.8 us                                                                                                             | 16.5 us: 1.08x faster                                                                                                     |
| pickle              | 16.0 us                                                                                                             | 15.0 us: 1.07x faster                                                                                                     |
| tomli_loads         | 2.41 sec                                                                                                            | 2.29 sec: 1.05x faster                                                                                                    |
| pickle_list         | 5.63 us                                                                                                             | 5.35 us: 1.05x faster                                                                                                     |
| json_loads          | 33.9 us                                                                                                             | 32.9 us: 1.03x faster                                                                                                     |
| xml_etree_iterparse | 141 ms                                                                                                              | 149 ms: 1.05x slower                                                                                                      |
| xml_etree_parse     | 179 ms                                                                                                              | 207 ms: 1.16x slower                                                                                                      |
| Geometric mean      | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (3): pickle_pure_python, json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250308-3.14.0a5+-a3990df/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json | results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 10.1 ms                                                                                                             | 10.1 ms: 1.00x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250308-3.14.0a5+-a3990df/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json | results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml     | 59.1 ms                                                                                                             | 57.2 ms: 1.03x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (3): django_template, genshi_text, mako

All benchmarks:
===============

| Benchmark                  | results/bm-20250308-3.14.0a5+-a3990df/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json | results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| scimark_fft                | 446 ms                                                                                                              | 363 ms: 1.23x faster                                                                                                      |
| logging_silent             | 131 ns                                                                                                              | 114 ns: 1.15x faster                                                                                                      |
| unpickle_list              | 6.56 us                                                                                                             | 5.75 us: 1.14x faster                                                                                                     |
| scimark_sor                | 152 ms                                                                                                              | 135 ms: 1.13x faster                                                                                                      |
| spectral_norm              | 113 ms                                                                                                              | 102 ms: 1.11x faster                                                                                                      |
| scimark_monte_carlo        | 82.7 ms                                                                                                             | 75.2 ms: 1.10x faster                                                                                                     |
| deepcopy                   | 321 us                                                                                                              | 292 us: 1.10x faster                                                                                                      |
| pickle_dict                | 39.3 us                                                                                                             | 36.0 us: 1.09x faster                                                                                                     |
| deepcopy_memo              | 37.5 us                                                                                                             | 34.6 us: 1.09x faster                                                                                                     |
| typing_runtime_protocols   | 189 us                                                                                                              | 174 us: 1.09x faster                                                                                                      |
| comprehensions             | 20.4 us                                                                                                             | 18.8 us: 1.09x faster                                                                                                     |
| scimark_sparse_mat_mult    | 6.49 ms                                                                                                             | 5.98 ms: 1.09x faster                                                                                                     |
| xml_etree_generate         | 108 ms                                                                                                              | 100 ms: 1.08x faster                                                                                                      |
| coverage                   | 98.6 ms                                                                                                             | 91.3 ms: 1.08x faster                                                                                                     |
| xml_etree_process          | 77.7 ms                                                                                                             | 72.1 ms: 1.08x faster                                                                                                     |
| unpickle                   | 17.8 us                                                                                                             | 16.5 us: 1.08x faster                                                                                                     |
| scimark_lu                 | 142 ms                                                                                                              | 132 ms: 1.08x faster                                                                                                      |
| async_generators           | 424 ms                                                                                                              | 395 ms: 1.07x faster                                                                                                      |
| deepcopy_reduce            | 3.49 us                                                                                                             | 3.26 us: 1.07x faster                                                                                                     |
| pickle                     | 16.0 us                                                                                                             | 15.0 us: 1.07x faster                                                                                                     |
| sqlglot_normalize          | 125 ms                                                                                                              | 118 ms: 1.06x faster                                                                                                      |
| tomli_loads                | 2.41 sec                                                                                                            | 2.29 sec: 1.05x faster                                                                                                    |
| pickle_list                | 5.63 us                                                                                                             | 5.35 us: 1.05x faster                                                                                                     |
| richards_super             | 56.6 ms                                                                                                             | 53.9 ms: 1.05x faster                                                                                                     |
| sympy_integrate            | 20.7 ms                                                                                                             | 19.7 ms: 1.05x faster                                                                                                     |
| async_tree_io_tg           | 888 ms                                                                                                              | 847 ms: 1.05x faster                                                                                                      |
| mdp                        | 3.30 sec                                                                                                            | 3.16 sec: 1.05x faster                                                                                                    |
| html5lib                   | 59.9 ms                                                                                                             | 57.3 ms: 1.04x faster                                                                                                     |
| bpe_tokeniser              | 5.41 sec                                                                                                            | 5.19 sec: 1.04x faster                                                                                                    |
| sqlglot_transpile          | 1.71 ms                                                                                                             | 1.64 ms: 1.04x faster                                                                                                     |
| raytrace                   | 314 ms                                                                                                              | 302 ms: 1.04x faster                                                                                                      |
| nbody                      | 116 ms                                                                                                              | 112 ms: 1.04x faster                                                                                                      |
| pyflate                    | 524 ms                                                                                                              | 506 ms: 1.04x faster                                                                                                      |
| logging_simple             | 6.80 us                                                                                                             | 6.58 us: 1.03x faster                                                                                                     |
| genshi_xml                 | 59.1 ms                                                                                                             | 57.2 ms: 1.03x faster                                                                                                     |
| sphinx                     | 1.11 sec                                                                                                            | 1.08 sec: 1.03x faster                                                                                                    |
| json_loads                 | 33.9 us                                                                                                             | 32.9 us: 1.03x faster                                                                                                     |
| async_tree_io              | 884 ms                                                                                                              | 861 ms: 1.03x faster                                                                                                      |
| pprint_pformat             | 1.89 sec                                                                                                            | 1.84 sec: 1.03x faster                                                                                                    |
| bench_thread_pool          | 1.30 ms                                                                                                             | 1.27 ms: 1.03x faster                                                                                                     |
| logging_format             | 7.44 us                                                                                                             | 7.26 us: 1.03x faster                                                                                                     |
| async_tree_none_tg         | 366 ms                                                                                                              | 357 ms: 1.02x faster                                                                                                      |
| coroutines                 | 28.0 ms                                                                                                             | 27.4 ms: 1.02x faster                                                                                                     |
| 2to3                       | 290 ms                                                                                                              | 284 ms: 1.02x faster                                                                                                      |
| k_core                     | 2.82 sec                                                                                                            | 2.76 sec: 1.02x faster                                                                                                    |
| async_tree_memoization     | 460 ms                                                                                                              | 453 ms: 1.02x faster                                                                                                      |
| async_tree_none            | 369 ms                                                                                                              | 364 ms: 1.01x faster                                                                                                      |
| sqlite_synth               | 3.80 us                                                                                                             | 3.74 us: 1.01x faster                                                                                                     |
| float                      | 85.7 ms                                                                                                             | 84.4 ms: 1.01x faster                                                                                                     |
| shortest_path              | 557 ms                                                                                                              | 550 ms: 1.01x faster                                                                                                      |
| docutils                   | 2.89 sec                                                                                                            | 2.87 sec: 1.01x faster                                                                                                    |
| generators                 | 35.5 ms                                                                                                             | 35.4 ms: 1.00x faster                                                                                                     |
| python_startup_no_site     | 10.1 ms                                                                                                             | 10.1 ms: 1.00x slower                                                                                                     |
| meteor_contest             | 112 ms                                                                                                              | 113 ms: 1.01x slower                                                                                                      |
| crypto_pyaes               | 82.3 ms                                                                                                             | 83.5 ms: 1.01x slower                                                                                                     |
| create_gc_cycles           | 3.51 ms                                                                                                             | 3.61 ms: 1.03x slower                                                                                                     |
| regex_dna                  | 237 ms                                                                                                              | 245 ms: 1.03x slower                                                                                                      |
| regex_v8                   | 30.8 ms                                                                                                             | 32.3 ms: 1.05x slower                                                                                                     |
| xml_etree_iterparse        | 141 ms                                                                                                              | 149 ms: 1.05x slower                                                                                                      |
| regex_effbot               | 3.88 ms                                                                                                             | 4.21 ms: 1.09x slower                                                                                                     |
| unpack_sequence            | 62.9 ns                                                                                                             | 69.3 ns: 1.10x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 637 ms                                                                                                              | 703 ms: 1.10x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 642 ms                                                                                                              | 712 ms: 1.11x slower                                                                                                      |
| xml_etree_parse            | 179 ms                                                                                                              | 207 ms: 1.16x slower                                                                                                      |
| pidigits                   | 238 ms                                                                                                              | 296 ms: 1.24x slower                                                                                                      |
| bench_mp_pool              | 3.93 sec                                                                                                            | 5.87 sec: 1.49x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (38): chaos, sqlglot_optimize, richards, sqlglot_parse, dulwich_log, go, json, pathlib, nqueens, sqlalchemy_imperative, pylint, django_template, pickle_pure_python, sympy_expand, asyncio_tcp, pprint_safe_repr, gc_traversal, genshi_text, sympy_str, asyncio_websockets, mako, deltablue, asyncio_tcp_ssl, hexiom, pycparser, async_tree_memoization_tg, subparsers, telco, sqlalchemy_declarative, connected_components, many_optionals, python_startup, json_dumps, fannkuch, sympy_sum, thrift, unpickle_pure_python, regex_compile

- Geometric mean (including insignificant results): 1.015x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x