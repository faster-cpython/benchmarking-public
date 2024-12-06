# Results vs. base

- fork: brandtbucher
- ref: justin_cold_17
- machine: linux-x86_64
- commit hash: 06d5d2f
- commit date: 2024-12-05
- overall geometric mean: 1.001x slower
- HPT reliability: 96.31%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 2.68 sec                                                               | 2.70 sec: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines                 | 23.1 ms                                                                | 23.3 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 480 ms                                                                 | 484 ms: 1.01x slower                                                   |
| async_tree_memoization_tg  | 313 ms                                                                 | 317 ms: 1.01x slower                                                   |
| async_tree_none_tg         | 249 ms                                                                 | 253 ms: 1.02x slower                                                   |
| async_tree_none            | 267 ms                                                                 | 272 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed    | 490 ms                                                                 | 499 ms: 1.02x slower                                                   |
| async_tree_io_tg           | 600 ms                                                                 | 616 ms: 1.03x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (4): asyncio_websockets, async_generators, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 129 ms: 1.01x faster                                                   |
| regex_dna      | 212 ms                                                                 | 213 ms: 1.00x slower                                                   |
| regex_effbot   | 3.20 ms                                                                | 3.43 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 321 us                                                                 | 318 us: 1.01x faster                                                   |
| xml_etree_parse      | 138 ms                                                                 | 137 ms: 1.01x faster                                                   |
| unpickle_pure_python | 196 us                                                                 | 194 us: 1.01x faster                                                   |
| xml_etree_iterparse  | 95.2 ms                                                                | 94.8 ms: 1.00x faster                                                  |
| tomli_loads          | 1.91 sec                                                               | 1.92 sec: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (4): json_loads, xml_etree_process, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.04 ms                                                                | 7.06 ms: 1.00x slower                                                  |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 10.1 ms                                                                | 10.0 ms: 1.00x faster                                                  |
| genshi_xml     | 57.7 ms                                                                | 58.2 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pycparser                  | 1.20 sec                                                               | 1.15 sec: 1.04x faster                                                 |
| gc_traversal               | 5.01 ms                                                                | 4.88 ms: 1.03x faster                                                  |
| meteor_contest             | 110 ms                                                                 | 107 ms: 1.02x faster                                                   |
| deepcopy_memo              | 29.4 us                                                                | 28.8 us: 1.02x faster                                                  |
| richards                   | 37.4 ms                                                                | 36.6 ms: 1.02x faster                                                  |
| spectral_norm              | 115 ms                                                                 | 113 ms: 1.02x faster                                                   |
| hexiom                     | 7.12 ms                                                                | 6.99 ms: 1.02x faster                                                  |
| logging_silent             | 102 ns                                                                 | 99.8 ns: 1.02x faster                                                  |
| pprint_safe_repr           | 718 ms                                                                 | 708 ms: 1.01x faster                                                   |
| scimark_lu                 | 115 ms                                                                 | 113 ms: 1.01x faster                                                   |
| coverage                   | 84.9 ms                                                                | 83.9 ms: 1.01x faster                                                  |
| sqlite_synth               | 2.81 us                                                                | 2.77 us: 1.01x faster                                                  |
| pickle_pure_python         | 321 us                                                                 | 318 us: 1.01x faster                                                   |
| xml_etree_parse            | 138 ms                                                                 | 137 ms: 1.01x faster                                                   |
| unpickle_pure_python       | 196 us                                                                 | 194 us: 1.01x faster                                                   |
| generators                 | 36.5 ms                                                                | 36.2 ms: 1.01x faster                                                  |
| bpe_tokeniser              | 4.41 sec                                                               | 4.38 sec: 1.01x faster                                                 |
| chaos                      | 59.0 ms                                                                | 58.6 ms: 1.01x faster                                                  |
| many_optionals             | 977 us                                                                 | 970 us: 1.01x faster                                                   |
| logging_format             | 6.30 us                                                                | 6.26 us: 1.01x faster                                                  |
| dulwich_log                | 67.8 ms                                                                | 67.4 ms: 1.01x faster                                                  |
| regex_compile              | 130 ms                                                                 | 129 ms: 1.01x faster                                                   |
| richards_super             | 43.7 ms                                                                | 43.5 ms: 1.01x faster                                                  |
| connected_components       | 438 ms                                                                 | 437 ms: 1.00x faster                                                   |
| xml_etree_iterparse        | 95.2 ms                                                                | 94.8 ms: 1.00x faster                                                  |
| mako                       | 10.1 ms                                                                | 10.0 ms: 1.00x faster                                                  |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                                   |
| regex_dna                  | 212 ms                                                                 | 213 ms: 1.00x slower                                                   |
| create_gc_cycles           | 2.46 ms                                                                | 2.47 ms: 1.00x slower                                                  |
| shortest_path              | 481 ms                                                                 | 483 ms: 1.00x slower                                                   |
| python_startup_no_site     | 7.04 ms                                                                | 7.06 ms: 1.00x slower                                                  |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                  |
| bench_mp_pool              | 80.9 ms                                                                | 81.3 ms: 1.00x slower                                                  |
| sympy_expand               | 475 ms                                                                 | 477 ms: 1.00x slower                                                   |
| tomli_loads                | 1.91 sec                                                               | 1.92 sec: 1.01x slower                                                 |
| docutils                   | 2.68 sec                                                               | 2.70 sec: 1.01x slower                                                 |
| deltablue                  | 3.14 ms                                                                | 3.17 ms: 1.01x slower                                                  |
| coroutines                 | 23.1 ms                                                                | 23.3 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 480 ms                                                                 | 484 ms: 1.01x slower                                                   |
| genshi_xml                 | 57.7 ms                                                                | 58.2 ms: 1.01x slower                                                  |
| scimark_sor                | 119 ms                                                                 | 120 ms: 1.01x slower                                                   |
| pathlib                    | 16.2 ms                                                                | 16.4 ms: 1.01x slower                                                  |
| scimark_monte_carlo        | 64.2 ms                                                                | 64.8 ms: 1.01x slower                                                  |
| nqueens                    | 89.9 ms                                                                | 90.9 ms: 1.01x slower                                                  |
| async_tree_memoization_tg  | 313 ms                                                                 | 317 ms: 1.01x slower                                                   |
| async_tree_none_tg         | 249 ms                                                                 | 253 ms: 1.02x slower                                                   |
| async_tree_none            | 267 ms                                                                 | 272 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed    | 490 ms                                                                 | 499 ms: 1.02x slower                                                   |
| pyflate                    | 449 ms                                                                 | 458 ms: 1.02x slower                                                   |
| scimark_fft                | 319 ms                                                                 | 326 ms: 1.02x slower                                                   |
| async_tree_io_tg           | 600 ms                                                                 | 616 ms: 1.03x slower                                                   |
| thrift                     | 768 us                                                                 | 792 us: 1.03x slower                                                   |
| mdp                        | 2.58 sec                                                               | 2.75 sec: 1.06x slower                                                 |
| regex_effbot               | 3.20 ms                                                                | 3.43 ms: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (43): pprint_pformat, html5lib, float, scimark_sparse_mat_mult, raytrace, fannkuch, json, deepcopy, typing_runtime_protocols, sympy_integrate, json_loads, sqlglot_transpile, sympy_sum, django_template, regex_v8, sqlglot_parse, 2to3, xml_etree_process, go, logging_simple, telco, asyncio_websockets, comprehensions, sympy_str, subparsers, bench_thread_pool, sqlglot_normalize, sqlglot_optimize, sqlalchemy_declarative, crypto_pyaes, sphinx, async_generators, xml_etree_generate, sqlalchemy_imperative, nbody, json_dumps, k_core, genshi_text, async_tree_io, async_tree_memoization, deepcopy_reduce, djangocms, pylint

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 96.31% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x