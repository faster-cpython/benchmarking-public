# Results vs. base

- fork: brandtbucher
- ref: justin_cold_14
- machine: linux-x86_64
- commit hash: b9d0b2b
- commit date: 2024-12-10
- overall geometric mean: 1.004x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 259 ms: 1.01x slower                                                   |
| docutils       | 2.68 sec                                                               | 2.65 sec: 1.01x faster                                                 |
| sphinx         | 1.05 sec                                                               | 1.04 sec: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 503 ms                                                                 | 497 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg | 489 ms                                                                 | 483 ms: 1.01x faster                                                   |
| coroutines                 | 23.1 ms                                                                | 23.2 ms: 1.01x slower                                                  |
| async_generators           | 449 ms                                                                 | 454 ms: 1.01x slower                                                   |
| async_tree_io_tg           | 612 ms                                                                 | 629 ms: 1.03x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (6): async_tree_none, async_tree_memoization, async_tree_memoization_tg, asyncio_websockets, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                                | 3.26 ms: 1.08x faster                                                  |
| regex_dna      | 220 ms                                                                 | 215 ms: 1.02x faster                                                   |
| regex_v8       | 25.1 ms                                                                | 25.1 ms: 1.00x faster                                                  |
| regex_compile  | 128 ms                                                                 | 130 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps          | 11.2 ms                                                                | 11.0 ms: 1.01x faster                                                  |
| json_loads          | 26.3 us                                                                | 26.1 us: 1.01x faster                                                  |
| xml_etree_iterparse | 94.9 ms                                                                | 95.4 ms: 1.01x slower                                                  |
| pickle_pure_python  | 318 us                                                                 | 322 us: 1.01x slower                                                   |
| xml_etree_generate  | 78.2 ms                                                                | 80.2 ms: 1.03x slower                                                  |
| xml_etree_process   | 54.9 ms                                                                | 57.1 ms: 1.04x slower                                                  |
| Geometric mean      | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (3): xml_etree_parse, tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.04 ms                                                                | 7.06 ms: 1.00x slower                                                  |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 10.2 ms                                                                | 10.2 ms: 1.00x slower                                                  |
| genshi_xml     | 57.0 ms                                                                | 58.8 ms: 1.03x slower                                                  |
| genshi_text    | 24.0 ms                                                                | 25.0 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot               | 3.51 ms                                                                | 3.26 ms: 1.08x faster                                                  |
| json                       | 4.92 ms                                                                | 4.74 ms: 1.04x faster                                                  |
| regex_dna                  | 220 ms                                                                 | 215 ms: 1.02x faster                                                   |
| deepcopy_reduce            | 2.81 us                                                                | 2.74 us: 1.02x faster                                                  |
| sympy_expand               | 473 ms                                                                 | 465 ms: 1.02x faster                                                   |
| json_dumps                 | 11.2 ms                                                                | 11.0 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed    | 503 ms                                                                 | 497 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg | 489 ms                                                                 | 483 ms: 1.01x faster                                                   |
| docutils                   | 2.68 sec                                                               | 2.65 sec: 1.01x faster                                                 |
| sphinx                     | 1.05 sec                                                               | 1.04 sec: 1.01x faster                                                 |
| scimark_monte_carlo        | 64.8 ms                                                                | 64.1 ms: 1.01x faster                                                  |
| sympy_str                  | 280 ms                                                                 | 277 ms: 1.01x faster                                                   |
| sqlite_synth               | 2.82 us                                                                | 2.80 us: 1.01x faster                                                  |
| json_loads                 | 26.3 us                                                                | 26.1 us: 1.01x faster                                                  |
| pathlib                    | 16.2 ms                                                                | 16.1 ms: 1.01x faster                                                  |
| regex_v8                   | 25.1 ms                                                                | 25.1 ms: 1.00x faster                                                  |
| mako                       | 10.2 ms                                                                | 10.2 ms: 1.00x slower                                                  |
| python_startup_no_site     | 7.04 ms                                                                | 7.06 ms: 1.00x slower                                                  |
| scimark_fft                | 321 ms                                                                 | 322 ms: 1.00x slower                                                   |
| sqlalchemy_declarative     | 130 ms                                                                 | 130 ms: 1.00x slower                                                   |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                  |
| bench_thread_pool          | 877 us                                                                 | 880 us: 1.00x slower                                                   |
| create_gc_cycles           | 2.44 ms                                                                | 2.45 ms: 1.00x slower                                                  |
| mdp                        | 2.77 sec                                                               | 2.78 sec: 1.00x slower                                                 |
| scimark_lu                 | 111 ms                                                                 | 112 ms: 1.00x slower                                                   |
| connected_components       | 434 ms                                                                 | 436 ms: 1.00x slower                                                   |
| chaos                      | 59.1 ms                                                                | 59.4 ms: 1.00x slower                                                  |
| deltablue                  | 3.17 ms                                                                | 3.18 ms: 1.01x slower                                                  |
| xml_etree_iterparse        | 94.9 ms                                                                | 95.4 ms: 1.01x slower                                                  |
| logging_silent             | 101 ns                                                                 | 101 ns: 1.01x slower                                                   |
| sqlglot_parse              | 1.32 ms                                                                | 1.33 ms: 1.01x slower                                                  |
| 2to3                       | 258 ms                                                                 | 259 ms: 1.01x slower                                                   |
| crypto_pyaes               | 68.6 ms                                                                | 69.0 ms: 1.01x slower                                                  |
| coroutines                 | 23.1 ms                                                                | 23.2 ms: 1.01x slower                                                  |
| sqlalchemy_imperative      | 16.7 ms                                                                | 16.8 ms: 1.01x slower                                                  |
| generators                 | 36.2 ms                                                                | 36.5 ms: 1.01x slower                                                  |
| shortest_path              | 478 ms                                                                 | 482 ms: 1.01x slower                                                   |
| bench_mp_pool              | 81.3 ms                                                                | 82.0 ms: 1.01x slower                                                  |
| dulwich_log                | 67.6 ms                                                                | 68.3 ms: 1.01x slower                                                  |
| async_generators           | 449 ms                                                                 | 454 ms: 1.01x slower                                                   |
| scimark_sor                | 118 ms                                                                 | 119 ms: 1.01x slower                                                   |
| comprehensions             | 17.2 us                                                                | 17.4 us: 1.01x slower                                                  |
| pickle_pure_python         | 318 us                                                                 | 322 us: 1.01x slower                                                   |
| pyflate                    | 447 ms                                                                 | 453 ms: 1.01x slower                                                   |
| thrift                     | 786 us                                                                 | 797 us: 1.01x slower                                                   |
| logging_simple             | 5.75 us                                                                | 5.83 us: 1.01x slower                                                  |
| coverage                   | 82.6 ms                                                                | 83.8 ms: 1.01x slower                                                  |
| regex_compile              | 128 ms                                                                 | 130 ms: 1.02x slower                                                   |
| raytrace                   | 282 ms                                                                 | 287 ms: 1.02x slower                                                   |
| hexiom                     | 6.98 ms                                                                | 7.10 ms: 1.02x slower                                                  |
| pprint_pformat             | 1.46 sec                                                               | 1.49 sec: 1.02x slower                                                 |
| typing_runtime_protocols   | 169 us                                                                 | 172 us: 1.02x slower                                                   |
| richards                   | 37.3 ms                                                                | 38.2 ms: 1.02x slower                                                  |
| xml_etree_generate         | 78.2 ms                                                                | 80.2 ms: 1.03x slower                                                  |
| gc_traversal               | 4.75 ms                                                                | 4.87 ms: 1.03x slower                                                  |
| async_tree_io_tg           | 612 ms                                                                 | 629 ms: 1.03x slower                                                   |
| genshi_xml                 | 57.0 ms                                                                | 58.8 ms: 1.03x slower                                                  |
| pycparser                  | 1.15 sec                                                               | 1.19 sec: 1.03x slower                                                 |
| genshi_text                | 24.0 ms                                                                | 25.0 ms: 1.04x slower                                                  |
| xml_etree_process          | 54.9 ms                                                                | 57.1 ms: 1.04x slower                                                  |
| scimark_sparse_mat_mult    | 4.57 ms                                                                | 4.76 ms: 1.04x slower                                                  |
| bpe_tokeniser              | 4.39 sec                                                               | 4.59 sec: 1.05x slower                                                 |
| fannkuch                   | 385 ms                                                                 | 402 ms: 1.05x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (35): pylint, go, djangocms, deepcopy, k_core, sqlglot_optimize, async_tree_none, sympy_integrate, pidigits, async_tree_memoization, sqlglot_normalize, telco, async_tree_memoization_tg, asyncio_websockets, sqlglot_transpile, async_tree_none_tg, xml_etree_parse, nbody, subparsers, meteor_contest, sympy_sum, deepcopy_memo, tomli_loads, html5lib, unpickle_pure_python, many_optionals, logging_format, mypy2, nqueens, async_tree_io, richards_super, float, django_template, pprint_safe_repr, spectral_norm

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x