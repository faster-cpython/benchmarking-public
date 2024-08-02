# Results vs. base

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-aarch64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.01x faster
- HPT reliability: 99.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 358 ms                                                                  | 363 ms: 1.01x slower                                                       |
| html5lib       | 70.9 ms                                                                 | 69.4 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                               |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 117 ms                                                                  | 115 ms: 1.01x faster                                                       |
| float          | 89.6 ms                                                                 | 90.1 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 4.92 ms                                                                 | 4.99 ms: 1.02x slower                                                      |
| regex_dna      | 250 ms                                                                  | 257 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                               |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 277 us                                                                  | 261 us: 1.06x faster                                                       |
| tomli_loads          | 2.63 sec                                                                | 2.58 sec: 1.02x faster                                                     |
| pickle_pure_python   | 398 us                                                                  | 393 us: 1.01x faster                                                       |
| json_loads           | 33.4 us                                                                 | 32.9 us: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                                   | 1.01x faster                                                               |

Benchmark hidden because not significant (5): json_dumps, xml_etree_iterparse, xml_etree_parse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.93 ms                                                                 | 8.85 ms: 1.01x faster                                                      |
| python_startup         | 13.2 ms                                                                 | 13.1 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 81.7 ms                                                                 | 75.7 ms: 1.08x faster                                                      |
| genshi_text     | 34.2 ms                                                                 | 32.6 ms: 1.05x faster                                                      |
| mako            | 13.2 ms                                                                 | 13.0 ms: 1.02x faster                                                      |
| django_template | 49.6 ms                                                                 | 50.0 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                                   | 1.03x faster                                                               |

All benchmarks:
===============

| Benchmark              | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml             | 81.7 ms                                                                 | 75.7 ms: 1.08x faster                                                      |
| unpickle_pure_python   | 277 us                                                                  | 261 us: 1.06x faster                                                       |
| scimark_monte_carlo    | 90.4 ms                                                                 | 85.8 ms: 1.05x faster                                                      |
| genshi_text            | 34.2 ms                                                                 | 32.6 ms: 1.05x faster                                                      |
| richards               | 53.5 ms                                                                 | 51.4 ms: 1.04x faster                                                      |
| json                   | 5.93 ms                                                                 | 5.72 ms: 1.04x faster                                                      |
| richards_super         | 60.5 ms                                                                 | 58.7 ms: 1.03x faster                                                      |
| chaos                  | 89.3 ms                                                                 | 87.0 ms: 1.03x faster                                                      |
| sympy_str              | 331 ms                                                                  | 324 ms: 1.02x faster                                                       |
| html5lib               | 70.9 ms                                                                 | 69.4 ms: 1.02x faster                                                      |
| tomli_loads            | 2.63 sec                                                                | 2.58 sec: 1.02x faster                                                     |
| mako                   | 13.2 ms                                                                 | 13.0 ms: 1.02x faster                                                      |
| fannkuch               | 476 ms                                                                  | 468 ms: 1.02x faster                                                       |
| pickle_pure_python     | 398 us                                                                  | 393 us: 1.01x faster                                                       |
| json_loads             | 33.4 us                                                                 | 32.9 us: 1.01x faster                                                      |
| nbody                  | 117 ms                                                                  | 115 ms: 1.01x faster                                                       |
| meteor_contest         | 116 ms                                                                  | 115 ms: 1.01x faster                                                       |
| deepcopy_memo          | 38.8 us                                                                 | 38.4 us: 1.01x faster                                                      |
| spectral_norm          | 148 ms                                                                  | 147 ms: 1.01x faster                                                       |
| python_startup_no_site | 8.93 ms                                                                 | 8.85 ms: 1.01x faster                                                      |
| pprint_safe_repr       | 1.12 sec                                                                | 1.11 sec: 1.01x faster                                                     |
| sqlglot_transpile      | 2.01 ms                                                                 | 2.00 ms: 1.01x faster                                                      |
| python_startup         | 13.2 ms                                                                 | 13.1 ms: 1.01x faster                                                      |
| bench_thread_pool      | 1.33 ms                                                                 | 1.32 ms: 1.01x faster                                                      |
| float                  | 89.6 ms                                                                 | 90.1 ms: 1.01x slower                                                      |
| django_template        | 49.6 ms                                                                 | 50.0 ms: 1.01x slower                                                      |
| comprehensions         | 23.2 us                                                                 | 23.4 us: 1.01x slower                                                      |
| 2to3                   | 358 ms                                                                  | 363 ms: 1.01x slower                                                       |
| regex_effbot           | 4.92 ms                                                                 | 4.99 ms: 1.02x slower                                                      |
| hexiom                 | 9.00 ms                                                                 | 9.17 ms: 1.02x slower                                                      |
| logging_format         | 7.79 us                                                                 | 7.94 us: 1.02x slower                                                      |
| regex_dna              | 250 ms                                                                  | 257 ms: 1.03x slower                                                       |
| deltablue              | 4.47 ms                                                                 | 4.70 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                               |

Benchmark hidden because not significant (58): tornado_http, sympy_integrate, json_dumps, dulwich_log, pylint, scimark_sor, sympy_sum, logging_silent, regex_compile, coroutines, bench_mp_pool, asyncio_tcp, xml_etree_iterparse, typing_runtime_protocols, crypto_pyaes, bpe_tokeniser, sqlglot_parse, pathlib, scimark_lu, go, deepcopy_reduce, async_tree_memoization_tg, pycparser, sqlglot_optimize, asyncio_websockets, asyncio_tcp_ssl, telco, mdp, generators, async_tree_io, pyflate, pidigits, xml_etree_parse, pprint_pformat, sympy_expand, xml_etree_process, nqueens, async_tree_cpu_io_mixed_tg, raytrace, async_tree_memoization, scimark_fft, thrift, gc_traversal, deepcopy, async_tree_io_tg, dask, docutils, async_generators, logging_simple, coverage, scimark_sparse_mat_mult, sqlglot_normalize, async_tree_cpu_io_mixed, regex_v8, async_tree_none, async_tree_none_tg, create_gc_cycles, xml_etree_generate

# HPT report

- Reliability score: 99.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x