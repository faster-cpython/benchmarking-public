# Results vs. base

- fork: python
- ref: 7363e8d24d14abf65163
- machine: linux-aarch64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.003x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json | results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 298 ms                                                                                                              | 294 ms: 1.02x faster                                                                                                      |
| html5lib       | 61.4 ms                                                                                                             | 58.3 ms: 1.05x faster                                                                                                     |
| sphinx         | 1.16 sec                                                                                                            | 1.12 sec: 1.03x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json | results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 374 ms                                                                                                              | 357 ms: 1.05x faster                                                                                                      |
| async_tree_none            | 385 ms                                                                                                              | 372 ms: 1.04x faster                                                                                                      |
| async_tree_memoization_tg  | 463 ms                                                                                                              | 447 ms: 1.04x faster                                                                                                      |
| async_tree_io              | 888 ms                                                                                                              | 865 ms: 1.03x faster                                                                                                      |
| async_tree_io_tg           | 883 ms                                                                                                              | 861 ms: 1.02x faster                                                                                                      |
| async_tree_memoization     | 463 ms                                                                                                              | 452 ms: 1.02x faster                                                                                                      |
| asyncio_tcp                | 538 ms                                                                                                              | 552 ms: 1.03x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 668 ms                                                                                                              | 723 ms: 1.08x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 650 ms                                                                                                              | 706 ms: 1.09x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.00x faster                                                                                                              |

Benchmark hidden because not significant (4): coroutines, async_generators, asyncio_websockets, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json | results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 237 ms                                                                                                              | 292 ms: 1.23x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.09x slower                                                                                                              |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json | results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 236 ms                                                                                                              | 247 ms: 1.05x slower                                                                                                      |
| regex_v8       | 29.1 ms                                                                                                             | 32.3 ms: 1.11x slower                                                                                                     |
| regex_effbot   | 3.86 ms                                                                                                             | 4.59 ms: 1.19x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.08x slower                                                                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json | results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json |
|---------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list       | 6.64 us                                                                                                             | 5.71 us: 1.16x faster                                                                                                     |
| unpickle            | 18.4 us                                                                                                             | 17.1 us: 1.08x faster                                                                                                     |
| xml_etree_generate  | 114 ms                                                                                                              | 107 ms: 1.06x faster                                                                                                      |
| xml_etree_process   | 81.0 ms                                                                                                             | 76.5 ms: 1.06x faster                                                                                                     |
| pickle_dict         | 38.6 us                                                                                                             | 36.8 us: 1.05x faster                                                                                                     |
| pickle_list         | 5.70 us                                                                                                             | 5.43 us: 1.05x faster                                                                                                     |
| tomli_loads         | 2.45 sec                                                                                                            | 2.35 sec: 1.05x faster                                                                                                    |
| json_dumps          | 14.3 ms                                                                                                             | 14.6 ms: 1.02x slower                                                                                                     |
| xml_etree_iterparse | 142 ms                                                                                                              | 148 ms: 1.05x slower                                                                                                      |
| xml_etree_parse     | 178 ms                                                                                                              | 203 ms: 1.14x slower                                                                                                      |
| Geometric mean      | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (4): unpickle_pure_python, json_loads, pickle_pure_python, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json | results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.66 ms                                                                                                             | 8.71 ms: 1.01x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json | results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml     | 60.1 ms                                                                                                             | 58.3 ms: 1.03x faster                                                                                                     |
| genshi_text    | 26.5 ms                                                                                                             | 25.8 ms: 1.03x faster                                                                                                     |
| mako           | 14.1 ms                                                                                                             | 13.9 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json | results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 4.47 sec                                                                                                            | 2.64 sec: 1.69x faster                                                                                                    |
| unpickle_list              | 6.64 us                                                                                                             | 5.71 us: 1.16x faster                                                                                                     |
| logging_silent             | 131 ns                                                                                                              | 116 ns: 1.13x faster                                                                                                      |
| deepcopy_reduce            | 3.62 us                                                                                                             | 3.25 us: 1.11x faster                                                                                                     |
| deepcopy_memo              | 38.8 us                                                                                                             | 35.2 us: 1.10x faster                                                                                                     |
| comprehensions             | 21.4 us                                                                                                             | 19.6 us: 1.09x faster                                                                                                     |
| scimark_fft                | 441 ms                                                                                                              | 406 ms: 1.09x faster                                                                                                      |
| unpickle                   | 18.4 us                                                                                                             | 17.1 us: 1.08x faster                                                                                                     |
| sympy_sum                  | 148 ms                                                                                                              | 138 ms: 1.07x faster                                                                                                      |
| telco                      | 9.81 ms                                                                                                             | 9.24 ms: 1.06x faster                                                                                                     |
| sqlglot_v2_parse           | 1.44 ms                                                                                                             | 1.36 ms: 1.06x faster                                                                                                     |
| xml_etree_generate         | 114 ms                                                                                                              | 107 ms: 1.06x faster                                                                                                      |
| pyflate                    | 556 ms                                                                                                              | 524 ms: 1.06x faster                                                                                                      |
| xml_etree_process          | 81.0 ms                                                                                                             | 76.5 ms: 1.06x faster                                                                                                     |
| deepcopy                   | 328 us                                                                                                              | 312 us: 1.05x faster                                                                                                      |
| html5lib                   | 61.4 ms                                                                                                             | 58.3 ms: 1.05x faster                                                                                                     |
| sympy_str                  | 273 ms                                                                                                              | 260 ms: 1.05x faster                                                                                                      |
| pickle_dict                | 38.6 us                                                                                                             | 36.8 us: 1.05x faster                                                                                                     |
| sqlglot_v2_transpile       | 1.77 ms                                                                                                             | 1.68 ms: 1.05x faster                                                                                                     |
| pickle_list                | 5.70 us                                                                                                             | 5.43 us: 1.05x faster                                                                                                     |
| async_tree_none_tg         | 374 ms                                                                                                              | 357 ms: 1.05x faster                                                                                                      |
| tomli_loads                | 2.45 sec                                                                                                            | 2.35 sec: 1.05x faster                                                                                                    |
| coverage                   | 103 ms                                                                                                              | 98.5 ms: 1.04x faster                                                                                                     |
| spectral_norm              | 128 ms                                                                                                              | 122 ms: 1.04x faster                                                                                                      |
| bench_thread_pool          | 1.37 ms                                                                                                             | 1.32 ms: 1.04x faster                                                                                                     |
| async_tree_none            | 385 ms                                                                                                              | 372 ms: 1.04x faster                                                                                                      |
| async_tree_memoization_tg  | 463 ms                                                                                                              | 447 ms: 1.04x faster                                                                                                      |
| bpe_tokeniser              | 5.44 sec                                                                                                            | 5.26 sec: 1.04x faster                                                                                                    |
| sphinx                     | 1.16 sec                                                                                                            | 1.12 sec: 1.03x faster                                                                                                    |
| richards_super             | 56.8 ms                                                                                                             | 54.9 ms: 1.03x faster                                                                                                     |
| genshi_xml                 | 60.1 ms                                                                                                             | 58.3 ms: 1.03x faster                                                                                                     |
| json                       | 6.04 ms                                                                                                             | 5.87 ms: 1.03x faster                                                                                                     |
| chaos                      | 67.4 ms                                                                                                             | 65.5 ms: 1.03x faster                                                                                                     |
| genshi_text                | 26.5 ms                                                                                                             | 25.8 ms: 1.03x faster                                                                                                     |
| mdp                        | 1.67 sec                                                                                                            | 1.62 sec: 1.03x faster                                                                                                    |
| async_tree_io              | 888 ms                                                                                                              | 865 ms: 1.03x faster                                                                                                      |
| async_tree_io_tg           | 883 ms                                                                                                              | 861 ms: 1.02x faster                                                                                                      |
| async_tree_memoization     | 463 ms                                                                                                              | 452 ms: 1.02x faster                                                                                                      |
| 2to3                       | 298 ms                                                                                                              | 294 ms: 1.02x faster                                                                                                      |
| mako                       | 14.1 ms                                                                                                             | 13.9 ms: 1.01x faster                                                                                                     |
| deltablue                  | 3.82 ms                                                                                                             | 3.77 ms: 1.01x faster                                                                                                     |
| logging_simple             | 6.96 us                                                                                                             | 6.90 us: 1.01x faster                                                                                                     |
| python_startup_no_site     | 8.66 ms                                                                                                             | 8.71 ms: 1.01x slower                                                                                                     |
| json_dumps                 | 14.3 ms                                                                                                             | 14.6 ms: 1.02x slower                                                                                                     |
| pprint_pformat             | 1.83 sec                                                                                                            | 1.88 sec: 1.03x slower                                                                                                    |
| asyncio_tcp                | 538 ms                                                                                                              | 552 ms: 1.03x slower                                                                                                      |
| sqlite_synth               | 3.82 us                                                                                                             | 3.94 us: 1.03x slower                                                                                                     |
| pprint_safe_repr           | 895 ms                                                                                                              | 923 ms: 1.03x slower                                                                                                      |
| fannkuch                   | 478 ms                                                                                                              | 496 ms: 1.04x slower                                                                                                      |
| xml_etree_iterparse        | 142 ms                                                                                                              | 148 ms: 1.05x slower                                                                                                      |
| regex_dna                  | 236 ms                                                                                                              | 247 ms: 1.05x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 668 ms                                                                                                              | 723 ms: 1.08x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 650 ms                                                                                                              | 706 ms: 1.09x slower                                                                                                      |
| regex_v8                   | 29.1 ms                                                                                                             | 32.3 ms: 1.11x slower                                                                                                     |
| xml_etree_parse            | 178 ms                                                                                                              | 203 ms: 1.14x slower                                                                                                      |
| regex_effbot               | 3.86 ms                                                                                                             | 4.59 ms: 1.19x slower                                                                                                     |
| pidigits                   | 237 ms                                                                                                              | 292 ms: 1.23x slower                                                                                                      |
| unpack_sequence            | 51.7 ns                                                                                                             | 73.0 ns: 1.41x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (45): hexiom, sqlglot_v2_optimize, unpickle_pure_python, scimark_sparse_mat_mult, sqlglot_v2_normalize, subparsers, json_loads, typing_runtime_protocols, coroutines, scimark_sor, sympy_integrate, scimark_lu, pickle_pure_python, pathlib, regex_compile, go, dulwich_log, sympy_expand, sqlalchemy_declarative, richards, async_generators, pycparser, crypto_pyaes, scimark_monte_carlo, gc_traversal, shortest_path, django_template, pylint, k_core, raytrace, logging_format, python_startup, asyncio_websockets, many_optionals, generators, asyncio_tcp_ssl, docutils, sqlalchemy_imperative, create_gc_cycles, float, pickle, connected_components, nbody, meteor_contest, nqueens

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x