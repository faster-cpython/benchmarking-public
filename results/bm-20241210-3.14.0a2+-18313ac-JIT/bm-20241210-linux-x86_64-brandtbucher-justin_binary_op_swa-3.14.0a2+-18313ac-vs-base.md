# Results vs. base

- fork: brandtbucher
- ref: justin_binary_op_swa
- machine: linux-x86_64
- commit hash: 18313ac
- commit date: 2024-12-10
- overall geometric mean: 1.002x slower
- HPT reliability: 82.47%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 257 ms: 1.00x faster                                                         |
| docutils       | 2.68 sec                                                               | 2.69 sec: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 489 ms                                                                 | 476 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed    | 503 ms                                                                 | 492 ms: 1.02x faster                                                         |
| async_tree_memoization     | 342 ms                                                                 | 337 ms: 1.01x faster                                                         |
| async_tree_none_tg         | 254 ms                                                                 | 251 ms: 1.01x faster                                                         |
| async_tree_none            | 272 ms                                                                 | 268 ms: 1.01x faster                                                         |
| async_tree_memoization_tg  | 317 ms                                                                 | 314 ms: 1.01x faster                                                         |
| coroutines                 | 23.1 ms                                                                | 22.9 ms: 1.01x faster                                                        |
| async_generators           | 449 ms                                                                 | 446 ms: 1.01x faster                                                         |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (3): async_tree_io, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x faster                                                         |
| float          | 75.6 ms                                                                | 76.7 ms: 1.01x slower                                                        |
| nbody          | 80.8 ms                                                                | 93.2 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                                | 3.25 ms: 1.08x faster                                                        |
| regex_dna      | 220 ms                                                                 | 216 ms: 1.02x faster                                                         |
| regex_v8       | 25.1 ms                                                                | 25.0 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|--------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_loads         | 26.3 us                                                                | 26.1 us: 1.01x faster                                                        |
| tomli_loads        | 1.93 sec                                                               | 1.94 sec: 1.01x slower                                                       |
| xml_etree_parse    | 137 ms                                                                 | 139 ms: 1.01x slower                                                         |
| xml_etree_generate | 78.2 ms                                                                | 81.1 ms: 1.04x slower                                                        |
| Geometric mean     | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (5): unpickle_pure_python, json_dumps, xml_etree_process, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                        |
| python_startup_no_site | 7.04 ms                                                                | 7.06 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 34.2 ms                                                                | 33.3 ms: 1.03x faster                                                        |
| mako            | 10.2 ms                                                                | 10.1 ms: 1.01x faster                                                        |
| genshi_xml      | 57.0 ms                                                                | 58.6 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot               | 3.51 ms                                                                | 3.25 ms: 1.08x faster                                                        |
| mdp                        | 2.77 sec                                                               | 2.58 sec: 1.07x faster                                                       |
| gc_traversal               | 4.75 ms                                                                | 4.60 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 489 ms                                                                 | 476 ms: 1.03x faster                                                         |
| django_template            | 34.2 ms                                                                | 33.3 ms: 1.03x faster                                                        |
| json                       | 4.92 ms                                                                | 4.79 ms: 1.03x faster                                                        |
| deepcopy_reduce            | 2.81 us                                                                | 2.74 us: 1.03x faster                                                        |
| richards_super             | 44.7 ms                                                                | 43.6 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 503 ms                                                                 | 492 ms: 1.02x faster                                                         |
| logging_simple             | 5.75 us                                                                | 5.64 us: 1.02x faster                                                        |
| regex_dna                  | 220 ms                                                                 | 216 ms: 1.02x faster                                                         |
| deepcopy                   | 275 us                                                                 | 270 us: 1.02x faster                                                         |
| sqlite_synth               | 2.82 us                                                                | 2.78 us: 1.02x faster                                                        |
| async_tree_memoization     | 342 ms                                                                 | 337 ms: 1.01x faster                                                         |
| thrift                     | 786 us                                                                 | 775 us: 1.01x faster                                                         |
| logging_format             | 6.30 us                                                                | 6.21 us: 1.01x faster                                                        |
| logging_silent             | 101 ns                                                                 | 99.1 ns: 1.01x faster                                                        |
| async_tree_none_tg         | 254 ms                                                                 | 251 ms: 1.01x faster                                                         |
| richards                   | 37.3 ms                                                                | 36.9 ms: 1.01x faster                                                        |
| async_tree_none            | 272 ms                                                                 | 268 ms: 1.01x faster                                                         |
| typing_runtime_protocols   | 169 us                                                                 | 167 us: 1.01x faster                                                         |
| async_tree_memoization_tg  | 317 ms                                                                 | 314 ms: 1.01x faster                                                         |
| dulwich_log                | 67.6 ms                                                                | 67.1 ms: 1.01x faster                                                        |
| coroutines                 | 23.1 ms                                                                | 22.9 ms: 1.01x faster                                                        |
| async_generators           | 449 ms                                                                 | 446 ms: 1.01x faster                                                         |
| regex_v8                   | 25.1 ms                                                                | 25.0 ms: 1.01x faster                                                        |
| json_loads                 | 26.3 us                                                                | 26.1 us: 1.01x faster                                                        |
| sqlglot_transpile          | 1.64 ms                                                                | 1.63 ms: 1.01x faster                                                        |
| mako                       | 10.2 ms                                                                | 10.1 ms: 1.01x faster                                                        |
| bench_thread_pool          | 877 us                                                                 | 873 us: 1.00x faster                                                         |
| sqlglot_parse              | 1.32 ms                                                                | 1.31 ms: 1.00x faster                                                        |
| sqlalchemy_declarative     | 130 ms                                                                 | 129 ms: 1.00x faster                                                         |
| 2to3                       | 258 ms                                                                 | 257 ms: 1.00x faster                                                         |
| pidigits                   | 187 ms                                                                 | 187 ms: 1.00x faster                                                         |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                        |
| docutils                   | 2.68 sec                                                               | 2.69 sec: 1.00x slower                                                       |
| python_startup_no_site     | 7.04 ms                                                                | 7.06 ms: 1.00x slower                                                        |
| sympy_str                  | 280 ms                                                                 | 281 ms: 1.01x slower                                                         |
| comprehensions             | 17.2 us                                                                | 17.3 us: 1.01x slower                                                        |
| bpe_tokeniser              | 4.39 sec                                                               | 4.41 sec: 1.01x slower                                                       |
| subparsers                 | 20.9 ms                                                                | 21.1 ms: 1.01x slower                                                        |
| meteor_contest             | 108 ms                                                                 | 109 ms: 1.01x slower                                                         |
| sympy_expand               | 473 ms                                                                 | 476 ms: 1.01x slower                                                         |
| tomli_loads                | 1.93 sec                                                               | 1.94 sec: 1.01x slower                                                       |
| fannkuch                   | 385 ms                                                                 | 388 ms: 1.01x slower                                                         |
| sympy_integrate            | 20.5 ms                                                                | 20.7 ms: 1.01x slower                                                        |
| crypto_pyaes               | 68.6 ms                                                                | 69.3 ms: 1.01x slower                                                        |
| xml_etree_parse            | 137 ms                                                                 | 139 ms: 1.01x slower                                                         |
| float                      | 75.6 ms                                                                | 76.7 ms: 1.01x slower                                                        |
| scimark_lu                 | 111 ms                                                                 | 113 ms: 1.02x slower                                                         |
| scimark_monte_carlo        | 64.8 ms                                                                | 65.8 ms: 1.02x slower                                                        |
| sympy_sum                  | 153 ms                                                                 | 156 ms: 1.02x slower                                                         |
| pyflate                    | 447 ms                                                                 | 455 ms: 1.02x slower                                                         |
| scimark_sor                | 118 ms                                                                 | 120 ms: 1.02x slower                                                         |
| genshi_xml                 | 57.0 ms                                                                | 58.6 ms: 1.03x slower                                                        |
| pycparser                  | 1.15 sec                                                               | 1.19 sec: 1.03x slower                                                       |
| spectral_norm              | 114 ms                                                                 | 118 ms: 1.04x slower                                                         |
| xml_etree_generate         | 78.2 ms                                                                | 81.1 ms: 1.04x slower                                                        |
| coverage                   | 82.6 ms                                                                | 85.7 ms: 1.04x slower                                                        |
| raytrace                   | 282 ms                                                                 | 294 ms: 1.04x slower                                                         |
| scimark_fft                | 321 ms                                                                 | 336 ms: 1.05x slower                                                         |
| chaos                      | 59.1 ms                                                                | 62.3 ms: 1.05x slower                                                        |
| scimark_sparse_mat_mult    | 4.57 ms                                                                | 5.09 ms: 1.11x slower                                                        |
| nbody                      | 80.8 ms                                                                | 93.2 ms: 1.15x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (34): djangocms, pprint_safe_repr, unpickle_pure_python, async_tree_io, pprint_pformat, html5lib, sqlalchemy_imperative, deltablue, asyncio_websockets, sphinx, regex_compile, pathlib, connected_components, mypy2, go, shortest_path, create_gc_cycles, genshi_text, sqlglot_optimize, pylint, nqueens, generators, bench_mp_pool, json_dumps, xml_etree_process, hexiom, sqlglot_normalize, many_optionals, k_core, telco, pickle_pure_python, deepcopy_memo, async_tree_io_tg, xml_etree_iterparse

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 82.47% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x