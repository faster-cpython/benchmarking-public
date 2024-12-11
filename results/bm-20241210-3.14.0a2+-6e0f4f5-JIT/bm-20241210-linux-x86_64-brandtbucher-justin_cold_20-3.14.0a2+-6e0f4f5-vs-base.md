# Results vs. base

- fork: brandtbucher
- ref: justin_cold_20
- machine: linux-x86_64
- commit hash: 6e0f4f5
- commit date: 2024-12-10
- overall geometric mean: 1.002x slower
- HPT reliability: 73.74%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 2.68 sec                                                               | 2.79 sec: 1.04x slower                                                 |
| sphinx         | 1.05 sec                                                               | 1.08 sec: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 489 ms                                                                 | 479 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed    | 503 ms                                                                 | 498 ms: 1.01x faster                                                   |
| async_generators           | 449 ms                                                                 | 446 ms: 1.01x faster                                                   |
| coroutines                 | 23.1 ms                                                                | 22.9 ms: 1.01x faster                                                  |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (7): async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, asyncio_websockets, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x faster                                                   |
| nbody          | 80.8 ms                                                                | 84.4 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                                | 24.7 ms: 1.02x faster                                                  |
| regex_effbot   | 3.51 ms                                                                | 3.46 ms: 1.01x faster                                                  |
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                   |
| regex_dna      | 220 ms                                                                 | 222 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 11.2 ms                                                                | 11.0 ms: 1.01x faster                                                  |
| unpickle_pure_python | 195 us                                                                 | 193 us: 1.01x faster                                                   |
| xml_etree_generate   | 78.2 ms                                                                | 77.7 ms: 1.01x faster                                                  |
| pickle_pure_python   | 318 us                                                                 | 324 us: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (5): tomli_loads, json_loads, xml_etree_iterparse, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                  |
| python_startup_no_site | 7.04 ms                                                                | 7.06 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.2 ms                                                                | 33.6 ms: 1.02x faster                                                  |
| genshi_text     | 24.0 ms                                                                | 23.8 ms: 1.01x faster                                                  |
| mako            | 10.2 ms                                                                | 10.1 ms: 1.00x faster                                                  |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| richards_super             | 44.7 ms                                                                | 43.4 ms: 1.03x faster                                                  |
| json                       | 4.92 ms                                                                | 4.80 ms: 1.02x faster                                                  |
| deepcopy_reduce            | 2.81 us                                                                | 2.75 us: 1.02x faster                                                  |
| mdp                        | 2.77 sec                                                               | 2.71 sec: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg | 489 ms                                                                 | 479 ms: 1.02x faster                                                   |
| regex_v8                   | 25.1 ms                                                                | 24.7 ms: 1.02x faster                                                  |
| django_template            | 34.2 ms                                                                | 33.6 ms: 1.02x faster                                                  |
| pycparser                  | 1.15 sec                                                               | 1.13 sec: 1.02x faster                                                 |
| json_dumps                 | 11.2 ms                                                                | 11.0 ms: 1.01x faster                                                  |
| thrift                     | 786 us                                                                 | 775 us: 1.01x faster                                                   |
| regex_effbot               | 3.51 ms                                                                | 3.46 ms: 1.01x faster                                                  |
| connected_components       | 434 ms                                                                 | 429 ms: 1.01x faster                                                   |
| meteor_contest             | 108 ms                                                                 | 107 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed    | 503 ms                                                                 | 498 ms: 1.01x faster                                                   |
| spectral_norm              | 114 ms                                                                 | 113 ms: 1.01x faster                                                   |
| genshi_text                | 24.0 ms                                                                | 23.8 ms: 1.01x faster                                                  |
| unpickle_pure_python       | 195 us                                                                 | 193 us: 1.01x faster                                                   |
| typing_runtime_protocols   | 169 us                                                                 | 167 us: 1.01x faster                                                   |
| async_generators           | 449 ms                                                                 | 446 ms: 1.01x faster                                                   |
| subparsers                 | 20.9 ms                                                                | 20.8 ms: 1.01x faster                                                  |
| coroutines                 | 23.1 ms                                                                | 22.9 ms: 1.01x faster                                                  |
| xml_etree_generate         | 78.2 ms                                                                | 77.7 ms: 1.01x faster                                                  |
| logging_silent             | 101 ns                                                                 | 99.9 ns: 1.01x faster                                                  |
| mako                       | 10.2 ms                                                                | 10.1 ms: 1.00x faster                                                  |
| comprehensions             | 17.2 us                                                                | 17.2 us: 1.00x faster                                                  |
| pidigits                   | 187 ms                                                                 | 187 ms: 1.00x faster                                                   |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                  |
| python_startup_no_site     | 7.04 ms                                                                | 7.06 ms: 1.00x slower                                                  |
| shortest_path              | 478 ms                                                                 | 480 ms: 1.00x slower                                                   |
| sqlalchemy_imperative      | 16.7 ms                                                                | 16.8 ms: 1.00x slower                                                  |
| bench_thread_pool          | 877 us                                                                 | 881 us: 1.00x slower                                                   |
| pathlib                    | 16.2 ms                                                                | 16.2 ms: 1.00x slower                                                  |
| many_optionals             | 974 us                                                                 | 979 us: 1.01x slower                                                   |
| sqlglot_optimize           | 55.3 ms                                                                | 55.6 ms: 1.01x slower                                                  |
| regex_compile              | 128 ms                                                                 | 129 ms: 1.01x slower                                                   |
| sympy_integrate            | 20.5 ms                                                                | 20.7 ms: 1.01x slower                                                  |
| create_gc_cycles           | 2.44 ms                                                                | 2.46 ms: 1.01x slower                                                  |
| gc_traversal               | 4.75 ms                                                                | 4.78 ms: 1.01x slower                                                  |
| regex_dna                  | 220 ms                                                                 | 222 ms: 1.01x slower                                                   |
| pyflate                    | 447 ms                                                                 | 452 ms: 1.01x slower                                                   |
| sympy_sum                  | 153 ms                                                                 | 155 ms: 1.01x slower                                                   |
| chaos                      | 59.1 ms                                                                | 59.7 ms: 1.01x slower                                                  |
| sympy_str                  | 280 ms                                                                 | 283 ms: 1.01x slower                                                   |
| coverage                   | 82.6 ms                                                                | 83.7 ms: 1.01x slower                                                  |
| raytrace                   | 282 ms                                                                 | 286 ms: 1.01x slower                                                   |
| generators                 | 36.2 ms                                                                | 36.7 ms: 1.01x slower                                                  |
| scimark_lu                 | 111 ms                                                                 | 113 ms: 1.02x slower                                                   |
| pickle_pure_python         | 318 us                                                                 | 324 us: 1.02x slower                                                   |
| scimark_fft                | 321 ms                                                                 | 328 ms: 1.02x slower                                                   |
| crypto_pyaes               | 68.6 ms                                                                | 70.2 ms: 1.02x slower                                                  |
| sphinx                     | 1.05 sec                                                               | 1.08 sec: 1.03x slower                                                 |
| sympy_expand               | 473 ms                                                                 | 490 ms: 1.04x slower                                                   |
| mypy2                      | 954 ms                                                                 | 991 ms: 1.04x slower                                                   |
| docutils                   | 2.68 sec                                                               | 2.79 sec: 1.04x slower                                                 |
| nbody                      | 80.8 ms                                                                | 84.4 ms: 1.04x slower                                                  |
| scimark_sparse_mat_mult    | 4.57 ms                                                                | 4.91 ms: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (42): nqueens, async_tree_io, async_tree_none_tg, telco, go, async_tree_memoization_tg, float, k_core, logging_simple, tomli_loads, scimark_monte_carlo, hexiom, genshi_xml, json_loads, async_tree_io_tg, sqlite_synth, sqlalchemy_declarative, html5lib, xml_etree_iterparse, asyncio_websockets, sqlglot_transpile, deltablue, async_tree_memoization, scimark_sor, xml_etree_process, xml_etree_parse, 2to3, async_tree_none, bench_mp_pool, dulwich_log, fannkuch, bpe_tokeniser, sqlglot_normalize, deepcopy_memo, logging_format, sqlglot_parse, deepcopy, richards, pprint_safe_repr, pprint_pformat, djangocms, pylint

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 73.74% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x