# Results vs. base

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-aarch64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.00x slower
- HPT reliability: 81.26%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240725-arminc-aarch64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| html5lib       | 70.0 ms                                                                 | 70.5 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                               |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240725-arminc-aarch64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators | 513 ms                                                                  | 505 ms: 1.02x faster                                                       |
| asyncio_tcp_ssl  | 2.26 sec                                                                | 2.25 sec: 1.01x faster                                                     |
| asyncio_tcp      | 614 ms                                                                  | 626 ms: 1.02x slower                                                       |
| Geometric mean   | (ref)                                                                   | 1.00x faster                                                               |

Benchmark hidden because not significant (10): async_tree_io, async_tree_memoization, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none, async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, coroutines, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240725-arminc-aarch64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                  | 248 ms: 1.04x faster                                                       |
| regex_v8       | 30.6 ms                                                                 | 31.1 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                               |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240725-arminc-aarch64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 147 ms                                                                  | 146 ms: 1.01x faster                                                       |
| json_loads           | 32.4 us                                                                 | 32.6 us: 1.01x slower                                                      |
| unpickle_pure_python | 275 us                                                                  | 278 us: 1.01x slower                                                       |
| pickle_pure_python   | 393 us                                                                  | 399 us: 1.01x slower                                                       |
| json_dumps           | 13.2 ms                                                                 | 13.4 ms: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                                   | 1.01x slower                                                               |

Benchmark hidden because not significant (4): xml_etree_process, tomli_loads, xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240725-arminc-aarch64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                 | 13.0 ms: 1.01x faster                                                      |
| python_startup_no_site | 8.91 ms                                                                 | 8.86 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240725-arminc-aarch64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text    | 35.1 ms                                                                 | 36.5 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                               |

Benchmark hidden because not significant (3): django_template, mako, genshi_xml

All benchmarks:
===============

| Benchmark              | bm-20240725-arminc-aarch64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna              | 257 ms                                                                  | 248 ms: 1.04x faster                                                       |
| gc_traversal           | 5.06 ms                                                                 | 4.91 ms: 1.03x faster                                                      |
| async_generators       | 513 ms                                                                  | 505 ms: 1.02x faster                                                       |
| nqueens                | 121 ms                                                                  | 119 ms: 1.02x faster                                                       |
| comprehensions         | 24.0 us                                                                 | 23.7 us: 1.02x faster                                                      |
| coverage               | 100 ms                                                                  | 98.7 ms: 1.01x faster                                                      |
| sympy_integrate        | 27.2 ms                                                                 | 26.8 ms: 1.01x faster                                                      |
| deepcopy_memo          | 39.2 us                                                                 | 38.7 us: 1.01x faster                                                      |
| fannkuch               | 473 ms                                                                  | 469 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl        | 2.26 sec                                                                | 2.25 sec: 1.01x faster                                                     |
| xml_etree_iterparse    | 147 ms                                                                  | 146 ms: 1.01x faster                                                       |
| python_startup         | 13.1 ms                                                                 | 13.0 ms: 1.01x faster                                                      |
| python_startup_no_site | 8.91 ms                                                                 | 8.86 ms: 1.01x faster                                                      |
| json_loads             | 32.4 us                                                                 | 32.6 us: 1.01x slower                                                      |
| html5lib               | 70.0 ms                                                                 | 70.5 ms: 1.01x slower                                                      |
| bench_thread_pool      | 1.32 ms                                                                 | 1.33 ms: 1.01x slower                                                      |
| sqlglot_parse          | 1.60 ms                                                                 | 1.62 ms: 1.01x slower                                                      |
| logging_format         | 7.82 us                                                                 | 7.92 us: 1.01x slower                                                      |
| sympy_expand           | 572 ms                                                                  | 580 ms: 1.01x slower                                                       |
| unpickle_pure_python   | 275 us                                                                  | 278 us: 1.01x slower                                                       |
| pickle_pure_python     | 393 us                                                                  | 399 us: 1.01x slower                                                       |
| richards_super         | 61.3 ms                                                                 | 62.2 ms: 1.02x slower                                                      |
| regex_v8               | 30.6 ms                                                                 | 31.1 ms: 1.02x slower                                                      |
| json_dumps             | 13.2 ms                                                                 | 13.4 ms: 1.02x slower                                                      |
| chaos                  | 87.6 ms                                                                 | 89.1 ms: 1.02x slower                                                      |
| asyncio_tcp            | 614 ms                                                                  | 626 ms: 1.02x slower                                                       |
| richards               | 53.9 ms                                                                 | 55.2 ms: 1.02x slower                                                      |
| deepcopy_reduce        | 4.21 us                                                                 | 4.32 us: 1.02x slower                                                      |
| genshi_text            | 35.1 ms                                                                 | 36.5 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                                   | 1.00x slower                                                               |

Benchmark hidden because not significant (61): async_tree_io, xml_etree_process, sympy_sum, sqlglot_optimize, async_tree_memoization, asyncio_websockets, async_tree_cpu_io_mixed, regex_effbot, async_tree_none, scimark_fft, pathlib, sympy_str, async_tree_io_tg, deepcopy, docutils, django_template, crypto_pyaes, pylint, bpe_tokeniser, async_tree_none_tg, async_tree_cpu_io_mixed_tg, sqlglot_transpile, go, bench_mp_pool, coroutines, logging_silent, scimark_sparse_mat_mult, dask, pyflate, spectral_norm, deltablue, raytrace, meteor_contest, pycparser, pprint_pformat, scimark_monte_carlo, mako, tomli_loads, pidigits, mdp, float, tornado_http, scimark_sor, hexiom, 2to3, scimark_lu, pprint_safe_repr, thrift, create_gc_cycles, sqlglot_normalize, genshi_xml, xml_etree_parse, typing_runtime_protocols, nbody, async_tree_memoization_tg, json, telco, regex_compile, logging_simple, xml_etree_generate, generators

# HPT report

- Reliability score: 81.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x