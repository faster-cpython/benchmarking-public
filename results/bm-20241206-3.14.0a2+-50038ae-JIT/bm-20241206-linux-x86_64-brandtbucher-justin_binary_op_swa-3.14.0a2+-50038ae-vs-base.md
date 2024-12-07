# Results vs. base

- fork: brandtbucher
- ref: justin_binary_op_swa
- machine: linux-x86_64
- commit hash: 50038ae
- commit date: 2024-12-06
- overall geometric mean: 1.011x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 259 ms: 1.00x slower                                                         |
| html5lib       | 64.2 ms                                                                | 65.6 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization     | 340 ms                                                                 | 343 ms: 1.01x slower                                                         |
| async_generators           | 445 ms                                                                 | 451 ms: 1.01x slower                                                         |
| async_tree_none            | 267 ms                                                                 | 272 ms: 1.02x slower                                                         |
| async_tree_memoization_tg  | 313 ms                                                                 | 319 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 480 ms                                                                 | 491 ms: 1.02x slower                                                         |
| async_tree_none_tg         | 249 ms                                                                 | 256 ms: 1.02x slower                                                         |
| async_tree_io_tg           | 600 ms                                                                 | 619 ms: 1.03x slower                                                         |
| coroutines                 | 23.1 ms                                                                | 23.9 ms: 1.03x slower                                                        |
| async_tree_cpu_io_mixed    | 490 ms                                                                 | 507 ms: 1.04x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 187 ms: 1.01x slower                                                         |
| float          | 75.9 ms                                                                | 76.8 ms: 1.01x slower                                                        |
| nbody          | 82.8 ms                                                                | 94.2 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 130 ms: 1.01x slower                                                         |
| regex_v8       | 25.0 ms                                                                | 25.2 ms: 1.01x slower                                                        |
| regex_dna      | 212 ms                                                                 | 217 ms: 1.02x slower                                                         |
| regex_effbot   | 3.20 ms                                                                | 3.47 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse | 95.2 ms                                                                | 94.7 ms: 1.01x faster                                                        |
| tomli_loads         | 1.91 sec                                                               | 1.96 sec: 1.02x slower                                                       |
| xml_etree_generate  | 78.3 ms                                                                | 80.5 ms: 1.03x slower                                                        |
| Geometric mean      | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (6): json_loads, xml_etree_process, xml_etree_parse, json_dumps, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.00x faster                                                        |
| python_startup_no_site | 7.04 ms                                                                | 7.03 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 57.7 ms                                                                | 56.5 ms: 1.02x faster                                                        |
| genshi_text    | 23.9 ms                                                                | 24.4 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 5.01 ms                                                                | 4.80 ms: 1.05x faster                                                        |
| pycparser                  | 1.20 sec                                                               | 1.15 sec: 1.04x faster                                                       |
| genshi_xml                 | 57.7 ms                                                                | 56.5 ms: 1.02x faster                                                        |
| djangocms                  | 22.4 us                                                                | 22.0 us: 1.02x faster                                                        |
| logging_silent             | 102 ns                                                                 | 101 ns: 1.01x faster                                                         |
| scimark_lu                 | 115 ms                                                                 | 114 ms: 1.01x faster                                                         |
| subparsers                 | 20.9 ms                                                                | 20.8 ms: 1.01x faster                                                        |
| deepcopy_memo              | 29.4 us                                                                | 29.2 us: 1.01x faster                                                        |
| sympy_sum                  | 156 ms                                                                 | 156 ms: 1.01x faster                                                         |
| xml_etree_iterparse        | 95.2 ms                                                                | 94.7 ms: 1.01x faster                                                        |
| shortest_path              | 481 ms                                                                 | 479 ms: 1.00x faster                                                         |
| mdp                        | 2.58 sec                                                               | 2.57 sec: 1.00x faster                                                       |
| connected_components       | 438 ms                                                                 | 437 ms: 1.00x faster                                                         |
| generators                 | 36.5 ms                                                                | 36.4 ms: 1.00x faster                                                        |
| python_startup             | 12.8 ms                                                                | 12.7 ms: 1.00x faster                                                        |
| python_startup_no_site     | 7.04 ms                                                                | 7.03 ms: 1.00x faster                                                        |
| create_gc_cycles           | 2.46 ms                                                                | 2.46 ms: 1.00x slower                                                        |
| bench_thread_pool          | 872 us                                                                 | 875 us: 1.00x slower                                                         |
| 2to3                       | 258 ms                                                                 | 259 ms: 1.00x slower                                                         |
| sympy_str                  | 282 ms                                                                 | 283 ms: 1.00x slower                                                         |
| sqlglot_transpile          | 1.63 ms                                                                | 1.64 ms: 1.00x slower                                                        |
| pidigits                   | 186 ms                                                                 | 187 ms: 1.01x slower                                                         |
| dulwich_log                | 67.8 ms                                                                | 68.2 ms: 1.01x slower                                                        |
| regex_compile              | 130 ms                                                                 | 130 ms: 1.01x slower                                                         |
| richards_super             | 43.7 ms                                                                | 44.1 ms: 1.01x slower                                                        |
| regex_v8                   | 25.0 ms                                                                | 25.2 ms: 1.01x slower                                                        |
| sqlglot_parse              | 1.32 ms                                                                | 1.33 ms: 1.01x slower                                                        |
| async_tree_memoization     | 340 ms                                                                 | 343 ms: 1.01x slower                                                         |
| bpe_tokeniser              | 4.41 sec                                                               | 4.46 sec: 1.01x slower                                                       |
| pathlib                    | 16.2 ms                                                                | 16.4 ms: 1.01x slower                                                        |
| float                      | 75.9 ms                                                                | 76.8 ms: 1.01x slower                                                        |
| async_generators           | 445 ms                                                                 | 451 ms: 1.01x slower                                                         |
| thrift                     | 768 us                                                                 | 779 us: 1.01x slower                                                         |
| deltablue                  | 3.14 ms                                                                | 3.19 ms: 1.01x slower                                                        |
| telco                      | 7.52 ms                                                                | 7.64 ms: 1.02x slower                                                        |
| coverage                   | 84.9 ms                                                                | 86.3 ms: 1.02x slower                                                        |
| richards                   | 37.4 ms                                                                | 38.0 ms: 1.02x slower                                                        |
| nqueens                    | 89.9 ms                                                                | 91.4 ms: 1.02x slower                                                        |
| async_tree_none            | 267 ms                                                                 | 272 ms: 1.02x slower                                                         |
| logging_format             | 6.30 us                                                                | 6.41 us: 1.02x slower                                                        |
| genshi_text                | 23.9 ms                                                                | 24.4 ms: 1.02x slower                                                        |
| json                       | 4.79 ms                                                                | 4.89 ms: 1.02x slower                                                        |
| async_tree_memoization_tg  | 313 ms                                                                 | 319 ms: 1.02x slower                                                         |
| go                         | 132 ms                                                                 | 135 ms: 1.02x slower                                                         |
| regex_dna                  | 212 ms                                                                 | 217 ms: 1.02x slower                                                         |
| html5lib                   | 64.2 ms                                                                | 65.6 ms: 1.02x slower                                                        |
| scimark_sor                | 119 ms                                                                 | 121 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 480 ms                                                                 | 491 ms: 1.02x slower                                                         |
| tomli_loads                | 1.91 sec                                                               | 1.96 sec: 1.02x slower                                                       |
| async_tree_none_tg         | 249 ms                                                                 | 256 ms: 1.02x slower                                                         |
| scimark_monte_carlo        | 64.2 ms                                                                | 65.9 ms: 1.03x slower                                                        |
| pyflate                    | 449 ms                                                                 | 461 ms: 1.03x slower                                                         |
| xml_etree_generate         | 78.3 ms                                                                | 80.5 ms: 1.03x slower                                                        |
| logging_simple             | 5.74 us                                                                | 5.92 us: 1.03x slower                                                        |
| async_tree_io_tg           | 600 ms                                                                 | 619 ms: 1.03x slower                                                         |
| crypto_pyaes               | 68.5 ms                                                                | 70.8 ms: 1.03x slower                                                        |
| coroutines                 | 23.1 ms                                                                | 23.9 ms: 1.03x slower                                                        |
| async_tree_cpu_io_mixed    | 490 ms                                                                 | 507 ms: 1.04x slower                                                         |
| scimark_sparse_mat_mult    | 4.86 ms                                                                | 5.07 ms: 1.04x slower                                                        |
| raytrace                   | 285 ms                                                                 | 298 ms: 1.04x slower                                                         |
| spectral_norm              | 115 ms                                                                 | 121 ms: 1.06x slower                                                         |
| scimark_fft                | 319 ms                                                                 | 341 ms: 1.07x slower                                                         |
| chaos                      | 59.0 ms                                                                | 63.4 ms: 1.07x slower                                                        |
| regex_effbot               | 3.20 ms                                                                | 3.47 ms: 1.09x slower                                                        |
| nbody                      | 82.8 ms                                                                | 94.2 ms: 1.14x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (32): pprint_safe_repr, meteor_contest, deepcopy_reduce, sqlglot_optimize, django_template, json_loads, pylint, xml_etree_process, sqlglot_normalize, comprehensions, deepcopy, sqlalchemy_declarative, sympy_expand, bench_mp_pool, xml_etree_parse, json_dumps, mako, sympy_integrate, docutils, asyncio_websockets, sphinx, hexiom, k_core, sqlalchemy_imperative, pickle_pure_python, many_optionals, sqlite_synth, unpickle_pure_python, async_tree_io, typing_runtime_protocols, pprint_pformat, fannkuch

- Geometric mean (including insignificant results): 1.011x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x