# Results vs. base

- fork: brandtbucher
- ref: macos_10_15
- machine: darwin-arm64
- commit hash: e5eacd1
- commit date: 2025-05-21
- overall geometric mean: 1.001x slower
- HPT reliability: 99.69%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250520-darwin-arm64-python-1298511b41ec0f9be925-3.15.0a0-1298511 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 172 ms                                                                | 169 ms: 1.01x faster                                               |
| docutils       | 1.45 sec                                                              | 1.45 sec: 1.00x slower                                             |
| html5lib       | 29.4 ms                                                               | 30.8 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250520-darwin-arm64-python-1298511b41ec0f9be925-3.15.0a0-1298511 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 407 ms                                                                | 405 ms: 1.01x faster                                               |
| coroutines                 | 16.1 ms                                                               | 16.2 ms: 1.00x slower                                              |
| async_generators           | 276 ms                                                                | 279 ms: 1.01x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (16): async_tree_eager, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_none_tg, asyncio_websockets, async_tree_eager_cpu_io_mixed_tg, async_tree_none, async_tree_eager_io_tg, async_tree_eager_io, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250520-darwin-arm64-python-1298511b41ec0f9be925-3.15.0a0-1298511 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 76.0 ms                                                               | 75.5 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250520-darwin-arm64-python-1298511b41ec0f9be925-3.15.0a0-1298511 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                               | 15.8 ms: 1.01x slower                                              |
| regex_dna      | 138 ms                                                                | 143 ms: 1.04x slower                                               |
| regex_effbot   | 2.14 ms                                                               | 2.26 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250520-darwin-arm64-python-1298511b41ec0f9be925-3.15.0a0-1298511 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 1.23 sec                                                              | 1.21 sec: 1.01x faster                                             |
| xml_etree_process    | 35.9 ms                                                               | 35.5 ms: 1.01x faster                                              |
| xml_etree_generate   | 51.7 ms                                                               | 51.1 ms: 1.01x faster                                              |
| json_dumps           | 6.63 ms                                                               | 6.60 ms: 1.01x faster                                              |
| unpickle_pure_python | 136 us                                                                | 135 us: 1.01x faster                                               |
| json_loads           | 18.1 us                                                               | 18.2 us: 1.01x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250520-darwin-arm64-python-1298511b41ec0f9be925-3.15.0a0-1298511 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 14.7 ms                                                               | 14.6 ms: 1.00x faster                                              |
| python_startup         | 19.2 ms                                                               | 19.1 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250520-darwin-arm64-python-1298511b41ec0f9be925-3.15.0a0-1298511 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 28.8 ms                                                               | 28.9 ms: 1.00x slower                                              |
| django_template | 20.7 ms                                                               | 20.8 ms: 1.01x slower                                              |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250520-darwin-arm64-python-1298511b41ec0f9be925-3.15.0a0-1298511 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| logging_simple             | 3.52 us                                                               | 3.46 us: 1.02x faster                                              |
| 2to3                       | 172 ms                                                                | 169 ms: 1.01x faster                                               |
| logging_format             | 3.82 us                                                               | 3.77 us: 1.01x faster                                              |
| tomli_loads                | 1.23 sec                                                              | 1.21 sec: 1.01x faster                                             |
| xml_etree_process          | 35.9 ms                                                               | 35.5 ms: 1.01x faster                                              |
| xml_etree_generate         | 51.7 ms                                                               | 51.1 ms: 1.01x faster                                              |
| deepcopy_memo              | 17.7 us                                                               | 17.5 us: 1.01x faster                                              |
| scimark_sparse_mat_mult    | 3.56 ms                                                               | 3.54 ms: 1.01x faster                                              |
| nbody                      | 76.0 ms                                                               | 75.5 ms: 1.01x faster                                              |
| pprint_pformat             | 1.09 sec                                                              | 1.08 sec: 1.01x faster                                             |
| many_optionals             | 466 us                                                                | 463 us: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg | 407 ms                                                                | 405 ms: 1.01x faster                                               |
| deepcopy_reduce            | 1.62 us                                                               | 1.61 us: 1.01x faster                                              |
| telco                      | 4.56 ms                                                               | 4.54 ms: 1.01x faster                                              |
| json_dumps                 | 6.63 ms                                                               | 6.60 ms: 1.01x faster                                              |
| unpickle_pure_python       | 136 us                                                                | 135 us: 1.01x faster                                               |
| python_startup_no_site     | 14.7 ms                                                               | 14.6 ms: 1.00x faster                                              |
| dask                       | 817 ms                                                                | 814 ms: 1.00x faster                                               |
| python_startup             | 19.2 ms                                                               | 19.1 ms: 1.00x faster                                              |
| generators                 | 23.2 ms                                                               | 23.1 ms: 1.00x faster                                              |
| spectral_norm              | 69.3 ms                                                               | 69.1 ms: 1.00x faster                                              |
| dulwich_log                | 24.7 ms                                                               | 24.6 ms: 1.00x faster                                              |
| logging_silent             | 322 ns                                                                | 321 ns: 1.00x faster                                               |
| hexiom                     | 4.29 ms                                                               | 4.28 ms: 1.00x faster                                              |
| richards                   | 32.1 ms                                                               | 32.0 ms: 1.00x faster                                              |
| chaos                      | 37.6 ms                                                               | 37.7 ms: 1.00x slower                                              |
| coroutines                 | 16.1 ms                                                               | 16.2 ms: 1.00x slower                                              |
| scimark_sor                | 77.3 ms                                                               | 77.5 ms: 1.00x slower                                              |
| scimark_lu                 | 74.3 ms                                                               | 74.4 ms: 1.00x slower                                              |
| richards_super             | 35.8 ms                                                               | 35.9 ms: 1.00x slower                                              |
| coverage                   | 268 ms                                                                | 269 ms: 1.00x slower                                               |
| sympy_expand               | 236 ms                                                                | 236 ms: 1.00x slower                                               |
| docutils                   | 1.45 sec                                                              | 1.45 sec: 1.00x slower                                             |
| genshi_xml                 | 28.8 ms                                                               | 28.9 ms: 1.00x slower                                              |
| mdp                        | 754 ms                                                                | 757 ms: 1.00x slower                                               |
| bpe_tokeniser              | 3.07 sec                                                              | 3.09 sec: 1.00x slower                                             |
| comprehensions             | 12.5 us                                                               | 12.6 us: 1.01x slower                                              |
| regex_v8                   | 15.7 ms                                                               | 15.8 ms: 1.01x slower                                              |
| json_loads                 | 18.1 us                                                               | 18.2 us: 1.01x slower                                              |
| meteor_contest             | 77.7 ms                                                               | 78.2 ms: 1.01x slower                                              |
| json                       | 3.01 ms                                                               | 3.03 ms: 1.01x slower                                              |
| scimark_fft                | 205 ms                                                                | 207 ms: 1.01x slower                                               |
| nqueens                    | 58.9 ms                                                               | 59.4 ms: 1.01x slower                                              |
| django_template            | 20.7 ms                                                               | 20.8 ms: 1.01x slower                                              |
| async_generators           | 276 ms                                                                | 279 ms: 1.01x slower                                               |
| shortest_path              | 346 ms                                                                | 350 ms: 1.01x slower                                               |
| pathlib                    | 23.0 ms                                                               | 23.4 ms: 1.01x slower                                              |
| pyflate                    | 286 ms                                                                | 291 ms: 1.02x slower                                               |
| fannkuch                   | 305 ms                                                                | 312 ms: 1.02x slower                                               |
| regex_dna                  | 138 ms                                                                | 143 ms: 1.04x slower                                               |
| html5lib                   | 29.4 ms                                                               | 30.8 ms: 1.05x slower                                              |
| regex_effbot               | 2.14 ms                                                               | 2.26 ms: 1.05x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (51): xml_etree_iterparse, pprint_safe_repr, k_core, xml_etree_parse, sqlglot_v2_transpile, async_tree_eager, gc_traversal, sqlite_synth, crypto_pyaes, connected_components, sqlglot_v2_normalize, async_tree_cpu_io_mixed, mako, pycparser, async_tree_eager_cpu_io_mixed, raytrace, float, genshi_text, scimark_monte_carlo, deltablue, async_tree_eager_memoization_tg, thrift, async_tree_eager_memoization, pidigits, async_tree_memoization_tg, sphinx, go, async_tree_eager_tg, sqlglot_v2_parse, async_tree_io_tg, async_tree_none_tg, asyncio_websockets, create_gc_cycles, async_tree_eager_cpu_io_mixed_tg, deepcopy, pickle_pure_python, sympy_integrate, async_tree_none, sqlglot_v2_optimize, sympy_str, regex_compile, async_tree_eager_io_tg, bench_mp_pool, async_tree_eager_io, sympy_sum, async_tree_memoization, pylint, subparsers, typing_runtime_protocols, async_tree_io, bench_thread_pool

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 99.69% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x