# Results vs. base

- fork: python
- ref: 718d234e4086a65d78c8
- machine: linux-aarch64
- commit hash: 718d234
- commit date: 2025-04-12
- overall geometric mean: 1.010x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250412-3.14.0a7+-718d234/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json | results/bm-20250412-3.14.0a7+-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 2.95 sec                                                                                                            | 2.87 sec: 1.03x faster                                                                                                    |
| html5lib       | 62.6 ms                                                                                                             | 59.6 ms: 1.05x faster                                                                                                     |
| sphinx         | 1.14 sec                                                                                                            | 1.11 sec: 1.03x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250412-3.14.0a7+-718d234/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json | results/bm-20250412-3.14.0a7+-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_generators           | 453 ms                                                                                                              | 410 ms: 1.11x faster                                                                                                      |
| async_tree_none_tg         | 379 ms                                                                                                              | 355 ms: 1.07x faster                                                                                                      |
| async_tree_none            | 388 ms                                                                                                              | 366 ms: 1.06x faster                                                                                                      |
| async_tree_io_tg           | 894 ms                                                                                                              | 854 ms: 1.05x faster                                                                                                      |
| async_tree_memoization_tg  | 465 ms                                                                                                              | 449 ms: 1.03x faster                                                                                                      |
| async_tree_io              | 885 ms                                                                                                              | 859 ms: 1.03x faster                                                                                                      |
| async_tree_memoization     | 466 ms                                                                                                              | 455 ms: 1.02x faster                                                                                                      |
| asyncio_tcp                | 539 ms                                                                                                              | 552 ms: 1.02x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 662 ms                                                                                                              | 709 ms: 1.07x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 648 ms                                                                                                              | 708 ms: 1.09x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (3): coroutines, asyncio_tcp_ssl, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250412-3.14.0a7+-718d234/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json | results/bm-20250412-3.14.0a7+-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 83.2 ms                                                                                                             | 84.8 ms: 1.02x slower                                                                                                     |
| nbody          | 119 ms                                                                                                              | 124 ms: 1.04x slower                                                                                                      |
| pidigits       | 236 ms                                                                                                              | 291 ms: 1.23x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.10x slower                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250412-3.14.0a7+-718d234/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json | results/bm-20250412-3.14.0a7+-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 27.7 ms                                                                                                             | 29.4 ms: 1.06x slower                                                                                                     |
| regex_effbot   | 3.79 ms                                                                                                             | 4.04 ms: 1.07x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.04x slower                                                                                                              |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250412-3.14.0a7+-718d234/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json | results/bm-20250412-3.14.0a7+-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json |
|---------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list       | 6.42 us                                                                                                             | 5.56 us: 1.16x faster                                                                                                     |
| pickle_dict         | 38.9 us                                                                                                             | 36.0 us: 1.08x faster                                                                                                     |
| unpickle            | 17.7 us                                                                                                             | 16.4 us: 1.08x faster                                                                                                     |
| xml_etree_process   | 78.7 ms                                                                                                             | 74.5 ms: 1.06x faster                                                                                                     |
| xml_etree_generate  | 110 ms                                                                                                              | 105 ms: 1.05x faster                                                                                                      |
| tomli_loads         | 2.41 sec                                                                                                            | 2.31 sec: 1.04x faster                                                                                                    |
| json_dumps          | 13.6 ms                                                                                                             | 13.9 ms: 1.02x slower                                                                                                     |
| xml_etree_iterparse | 141 ms                                                                                                              | 148 ms: 1.05x slower                                                                                                      |
| xml_etree_parse     | 181 ms                                                                                                              | 205 ms: 1.13x slower                                                                                                      |
| Geometric mean      | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (5): pickle_list, unpickle_pure_python, pickle_pure_python, json_loads, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250412-3.14.0a7+-718d234/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json | results/bm-20250412-3.14.0a7+-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 10.1 ms                                                                                                             | 10.2 ms: 1.01x slower                                                                                                     |
| python_startup         | 16.0 ms                                                                                                             | 16.2 ms: 1.01x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.01x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250412-3.14.0a7+-718d234/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json | results/bm-20250412-3.14.0a7+-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml     | 59.4 ms                                                                                                             | 57.0 ms: 1.04x faster                                                                                                     |
| genshi_text    | 26.6 ms                                                                                                             | 25.7 ms: 1.03x faster                                                                                                     |
| mako           | 13.7 ms                                                                                                             | 13.9 ms: 1.01x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20250412-3.14.0a7+-718d234/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json | results/bm-20250412-3.14.0a7+-718d234-CLANG/bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list              | 6.42 us                                                                                                             | 5.56 us: 1.16x faster                                                                                                     |
| logging_silent             | 127 ns                                                                                                              | 112 ns: 1.13x faster                                                                                                      |
| async_generators           | 453 ms                                                                                                              | 410 ms: 1.11x faster                                                                                                      |
| telco                      | 9.74 ms                                                                                                             | 8.90 ms: 1.09x faster                                                                                                     |
| deepcopy                   | 322 us                                                                                                              | 294 us: 1.09x faster                                                                                                      |
| richards                   | 52.4 ms                                                                                                             | 48.2 ms: 1.09x faster                                                                                                     |
| pickle_dict                | 38.9 us                                                                                                             | 36.0 us: 1.08x faster                                                                                                     |
| spectral_norm              | 125 ms                                                                                                              | 116 ms: 1.08x faster                                                                                                      |
| unpickle                   | 17.7 us                                                                                                             | 16.4 us: 1.08x faster                                                                                                     |
| sqlglot_v2_parse           | 1.42 ms                                                                                                             | 1.33 ms: 1.07x faster                                                                                                     |
| async_tree_none_tg         | 379 ms                                                                                                              | 355 ms: 1.07x faster                                                                                                      |
| sympy_str                  | 270 ms                                                                                                              | 253 ms: 1.07x faster                                                                                                      |
| comprehensions             | 21.0 us                                                                                                             | 19.7 us: 1.06x faster                                                                                                     |
| typing_runtime_protocols   | 199 us                                                                                                              | 187 us: 1.06x faster                                                                                                      |
| async_tree_none            | 388 ms                                                                                                              | 366 ms: 1.06x faster                                                                                                      |
| richards_super             | 58.1 ms                                                                                                             | 54.9 ms: 1.06x faster                                                                                                     |
| xml_etree_process          | 78.7 ms                                                                                                             | 74.5 ms: 1.06x faster                                                                                                     |
| deepcopy_memo              | 36.9 us                                                                                                             | 35.0 us: 1.05x faster                                                                                                     |
| xml_etree_generate         | 110 ms                                                                                                              | 105 ms: 1.05x faster                                                                                                      |
| scimark_fft                | 413 ms                                                                                                              | 393 ms: 1.05x faster                                                                                                      |
| pyflate                    | 541 ms                                                                                                              | 515 ms: 1.05x faster                                                                                                      |
| html5lib                   | 62.6 ms                                                                                                             | 59.6 ms: 1.05x faster                                                                                                     |
| sqlglot_v2_optimize        | 60.9 ms                                                                                                             | 58.0 ms: 1.05x faster                                                                                                     |
| logging_simple             | 7.03 us                                                                                                             | 6.70 us: 1.05x faster                                                                                                     |
| async_tree_io_tg           | 894 ms                                                                                                              | 854 ms: 1.05x faster                                                                                                      |
| logging_format             | 7.81 us                                                                                                             | 7.47 us: 1.05x faster                                                                                                     |
| genshi_xml                 | 59.4 ms                                                                                                             | 57.0 ms: 1.04x faster                                                                                                     |
| scimark_lu                 | 143 ms                                                                                                              | 137 ms: 1.04x faster                                                                                                      |
| tomli_loads                | 2.41 sec                                                                                                            | 2.31 sec: 1.04x faster                                                                                                    |
| coverage                   | 101 ms                                                                                                              | 96.7 ms: 1.04x faster                                                                                                     |
| bpe_tokeniser              | 5.53 sec                                                                                                            | 5.32 sec: 1.04x faster                                                                                                    |
| sympy_expand               | 462 ms                                                                                                              | 446 ms: 1.04x faster                                                                                                      |
| async_tree_memoization_tg  | 465 ms                                                                                                              | 449 ms: 1.03x faster                                                                                                      |
| genshi_text                | 26.6 ms                                                                                                             | 25.7 ms: 1.03x faster                                                                                                     |
| generators                 | 36.7 ms                                                                                                             | 35.5 ms: 1.03x faster                                                                                                     |
| deltablue                  | 3.89 ms                                                                                                             | 3.76 ms: 1.03x faster                                                                                                     |
| sphinx                     | 1.14 sec                                                                                                            | 1.11 sec: 1.03x faster                                                                                                    |
| async_tree_io              | 885 ms                                                                                                              | 859 ms: 1.03x faster                                                                                                      |
| pathlib                    | 22.1 ms                                                                                                             | 21.4 ms: 1.03x faster                                                                                                     |
| pycparser                  | 1.25 sec                                                                                                            | 1.22 sec: 1.03x faster                                                                                                    |
| docutils                   | 2.95 sec                                                                                                            | 2.87 sec: 1.03x faster                                                                                                    |
| async_tree_memoization     | 466 ms                                                                                                              | 455 ms: 1.02x faster                                                                                                      |
| k_core                     | 2.81 sec                                                                                                            | 2.75 sec: 1.02x faster                                                                                                    |
| bench_thread_pool          | 1.35 ms                                                                                                             | 1.32 ms: 1.02x faster                                                                                                     |
| scimark_monte_carlo        | 78.6 ms                                                                                                             | 77.5 ms: 1.01x faster                                                                                                     |
| hexiom                     | 6.96 ms                                                                                                             | 6.90 ms: 1.01x faster                                                                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                                                                             | 6.60 ms: 1.01x faster                                                                                                     |
| pprint_pformat             | 1.82 sec                                                                                                            | 1.84 sec: 1.01x slower                                                                                                    |
| python_startup_no_site     | 10.1 ms                                                                                                             | 10.2 ms: 1.01x slower                                                                                                     |
| python_startup             | 16.0 ms                                                                                                             | 16.2 ms: 1.01x slower                                                                                                     |
| mako                       | 13.7 ms                                                                                                             | 13.9 ms: 1.01x slower                                                                                                     |
| pprint_safe_repr           | 886 ms                                                                                                              | 900 ms: 1.02x slower                                                                                                      |
| float                      | 83.2 ms                                                                                                             | 84.8 ms: 1.02x slower                                                                                                     |
| json_dumps                 | 13.6 ms                                                                                                             | 13.9 ms: 1.02x slower                                                                                                     |
| asyncio_tcp                | 539 ms                                                                                                              | 552 ms: 1.02x slower                                                                                                      |
| nbody                      | 119 ms                                                                                                              | 124 ms: 1.04x slower                                                                                                      |
| xml_etree_iterparse        | 141 ms                                                                                                              | 148 ms: 1.05x slower                                                                                                      |
| fannkuch                   | 467 ms                                                                                                              | 493 ms: 1.06x slower                                                                                                      |
| regex_v8                   | 27.7 ms                                                                                                             | 29.4 ms: 1.06x slower                                                                                                     |
| regex_effbot               | 3.79 ms                                                                                                             | 4.04 ms: 1.07x slower                                                                                                     |
| async_tree_cpu_io_mixed    | 662 ms                                                                                                              | 709 ms: 1.07x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 648 ms                                                                                                              | 708 ms: 1.09x slower                                                                                                      |
| xml_etree_parse            | 181 ms                                                                                                              | 205 ms: 1.13x slower                                                                                                      |
| pidigits                   | 236 ms                                                                                                              | 291 ms: 1.23x slower                                                                                                      |
| unpack_sequence            | 52.1 ns                                                                                                             | 73.1 ns: 1.40x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (38): deepcopy_reduce, sqlglot_v2_normalize, pickle_list, coroutines, sqlglot_v2_transpile, sympy_sum, django_template, sympy_integrate, unpickle_pure_python, 2to3, pickle_pure_python, mdp, chaos, go, json, json_loads, connected_components, nqueens, scimark_sor, crypto_pyaes, many_optionals, asyncio_tcp_ssl, sqlalchemy_imperative, subparsers, gc_traversal, regex_dna, asyncio_websockets, pylint, pickle, sqlite_synth, sqlalchemy_declarative, shortest_path, create_gc_cycles, raytrace, dulwich_log, regex_compile, meteor_contest, bench_mp_pool

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x