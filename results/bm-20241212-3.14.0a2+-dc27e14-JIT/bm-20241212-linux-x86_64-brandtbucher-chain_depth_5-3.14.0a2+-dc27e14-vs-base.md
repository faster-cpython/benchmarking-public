# Results vs. base

- fork: brandtbucher
- ref: chain_depth_5
- machine: linux-x86_64
- commit hash: dc27e14
- commit date: 2024-12-12
- overall geometric mean: 1.002x slower
- HPT reliability: 87.92%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 258 ms: 1.00x slower                                                  |
| docutils       | 2.68 sec                                                               | 2.71 sec: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 489 ms                                                                 | 479 ms: 1.02x faster                                                  |
| async_tree_io_tg           | 612 ms                                                                 | 602 ms: 1.02x faster                                                  |
| async_tree_none_tg         | 254 ms                                                                 | 250 ms: 1.02x faster                                                  |
| coroutines                 | 23.1 ms                                                                | 22.7 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed    | 503 ms                                                                 | 496 ms: 1.01x faster                                                  |
| async_tree_memoization_tg  | 317 ms                                                                 | 313 ms: 1.01x faster                                                  |
| async_generators           | 449 ms                                                                 | 455 ms: 1.01x slower                                                  |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (4): async_tree_io, async_tree_memoization, async_tree_none, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 80.8 ms                                                                | 80.5 ms: 1.00x faster                                                 |
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                                | 3.39 ms: 1.04x faster                                                 |
| regex_dna      | 220 ms                                                                 | 215 ms: 1.02x faster                                                  |
| regex_v8       | 25.1 ms                                                                | 24.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|--------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python | 318 us                                                                 | 315 us: 1.01x faster                                                  |
| json_loads         | 26.3 us                                                                | 26.1 us: 1.01x faster                                                 |
| xml_etree_process  | 54.9 ms                                                                | 55.4 ms: 1.01x slower                                                 |
| tomli_loads        | 1.93 sec                                                               | 1.95 sec: 1.01x slower                                                |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (5): xml_etree_generate, unpickle_pure_python, json_dumps, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.04 ms                                                                | 7.03 ms: 1.00x faster                                                 |
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.2 ms                                                                | 33.9 ms: 1.01x faster                                                 |
| genshi_xml      | 57.0 ms                                                                | 57.7 ms: 1.01x slower                                                 |
| genshi_text     | 24.0 ms                                                                | 24.7 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| richards_super             | 44.7 ms                                                                | 43.1 ms: 1.04x faster                                                 |
| regex_effbot               | 3.51 ms                                                                | 3.39 ms: 1.04x faster                                                 |
| deepcopy_reduce            | 2.81 us                                                                | 2.73 us: 1.03x faster                                                 |
| json                       | 4.92 ms                                                                | 4.80 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg | 489 ms                                                                 | 479 ms: 1.02x faster                                                  |
| regex_dna                  | 220 ms                                                                 | 215 ms: 1.02x faster                                                  |
| async_tree_io_tg           | 612 ms                                                                 | 602 ms: 1.02x faster                                                  |
| async_tree_none_tg         | 254 ms                                                                 | 250 ms: 1.02x faster                                                  |
| coroutines                 | 23.1 ms                                                                | 22.7 ms: 1.01x faster                                                 |
| spectral_norm              | 114 ms                                                                 | 112 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed    | 503 ms                                                                 | 496 ms: 1.01x faster                                                  |
| async_tree_memoization_tg  | 317 ms                                                                 | 313 ms: 1.01x faster                                                  |
| deepcopy                   | 275 us                                                                 | 272 us: 1.01x faster                                                  |
| pickle_pure_python         | 318 us                                                                 | 315 us: 1.01x faster                                                  |
| logging_format             | 6.30 us                                                                | 6.24 us: 1.01x faster                                                 |
| typing_runtime_protocols   | 169 us                                                                 | 167 us: 1.01x faster                                                  |
| django_template            | 34.2 ms                                                                | 33.9 ms: 1.01x faster                                                 |
| regex_v8                   | 25.1 ms                                                                | 24.9 ms: 1.01x faster                                                 |
| json_loads                 | 26.3 us                                                                | 26.1 us: 1.01x faster                                                 |
| bench_mp_pool              | 81.3 ms                                                                | 80.8 ms: 1.01x faster                                                 |
| nbody                      | 80.8 ms                                                                | 80.5 ms: 1.00x faster                                                 |
| mdp                        | 2.77 sec                                                               | 2.76 sec: 1.00x faster                                                |
| pidigits                   | 187 ms                                                                 | 186 ms: 1.00x faster                                                  |
| python_startup_no_site     | 7.04 ms                                                                | 7.03 ms: 1.00x faster                                                 |
| python_startup             | 12.8 ms                                                                | 12.7 ms: 1.00x faster                                                 |
| shortest_path              | 478 ms                                                                 | 479 ms: 1.00x slower                                                  |
| 2to3                       | 258 ms                                                                 | 258 ms: 1.00x slower                                                  |
| sqlalchemy_declarative     | 130 ms                                                                 | 130 ms: 1.00x slower                                                  |
| sqlglot_optimize           | 55.3 ms                                                                | 55.5 ms: 1.00x slower                                                 |
| bpe_tokeniser              | 4.39 sec                                                               | 4.41 sec: 1.00x slower                                                |
| create_gc_cycles           | 2.44 ms                                                                | 2.46 ms: 1.00x slower                                                 |
| scimark_lu                 | 111 ms                                                                 | 112 ms: 1.00x slower                                                  |
| pathlib                    | 16.2 ms                                                                | 16.2 ms: 1.01x slower                                                 |
| deltablue                  | 3.17 ms                                                                | 3.19 ms: 1.01x slower                                                 |
| sqlglot_parse              | 1.32 ms                                                                | 1.33 ms: 1.01x slower                                                 |
| raytrace                   | 282 ms                                                                 | 284 ms: 1.01x slower                                                  |
| fannkuch                   | 385 ms                                                                 | 388 ms: 1.01x slower                                                  |
| xml_etree_process          | 54.9 ms                                                                | 55.4 ms: 1.01x slower                                                 |
| logging_silent             | 101 ns                                                                 | 101 ns: 1.01x slower                                                  |
| meteor_contest             | 108 ms                                                                 | 109 ms: 1.01x slower                                                  |
| sympy_expand               | 473 ms                                                                 | 478 ms: 1.01x slower                                                  |
| telco                      | 7.56 ms                                                                | 7.64 ms: 1.01x slower                                                 |
| gc_traversal               | 4.75 ms                                                                | 4.80 ms: 1.01x slower                                                 |
| many_optionals             | 974 us                                                                 | 984 us: 1.01x slower                                                  |
| scimark_fft                | 321 ms                                                                 | 325 ms: 1.01x slower                                                  |
| comprehensions             | 17.2 us                                                                | 17.4 us: 1.01x slower                                                 |
| sympy_str                  | 280 ms                                                                 | 283 ms: 1.01x slower                                                  |
| docutils                   | 2.68 sec                                                               | 2.71 sec: 1.01x slower                                                |
| genshi_xml                 | 57.0 ms                                                                | 57.7 ms: 1.01x slower                                                 |
| sympy_integrate            | 20.5 ms                                                                | 20.8 ms: 1.01x slower                                                 |
| tomli_loads                | 1.93 sec                                                               | 1.95 sec: 1.01x slower                                                |
| sympy_sum                  | 153 ms                                                                 | 155 ms: 1.01x slower                                                  |
| async_generators           | 449 ms                                                                 | 455 ms: 1.01x slower                                                  |
| pprint_safe_repr           | 715 ms                                                                 | 725 ms: 1.01x slower                                                  |
| hexiom                     | 6.98 ms                                                                | 7.10 ms: 1.02x slower                                                 |
| chaos                      | 59.1 ms                                                                | 60.2 ms: 1.02x slower                                                 |
| genshi_text                | 24.0 ms                                                                | 24.7 ms: 1.03x slower                                                 |
| pyflate                    | 447 ms                                                                 | 460 ms: 1.03x slower                                                  |
| pprint_pformat             | 1.46 sec                                                               | 1.50 sec: 1.03x slower                                                |
| coverage                   | 82.6 ms                                                                | 86.5 ms: 1.05x slower                                                 |
| scimark_sparse_mat_mult    | 4.57 ms                                                                | 4.85 ms: 1.06x slower                                                 |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (37): go, nqueens, scimark_monte_carlo, async_tree_io, async_tree_memoization, sqlite_synth, k_core, subparsers, thrift, deepcopy_memo, djangocms, xml_etree_generate, logging_simple, crypto_pyaes, unpickle_pure_python, async_tree_none, asyncio_websockets, pycparser, json_dumps, scimark_sor, connected_components, dulwich_log, bench_thread_pool, sphinx, sqlglot_transpile, pylint, regex_compile, generators, xml_etree_iterparse, sqlalchemy_imperative, xml_etree_parse, float, mypy2, sqlglot_normalize, richards, html5lib, mako

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 87.92% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x