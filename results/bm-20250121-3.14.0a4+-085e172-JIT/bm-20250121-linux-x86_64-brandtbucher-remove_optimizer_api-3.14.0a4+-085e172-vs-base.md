# Results vs. base

- fork: brandtbucher
- ref: remove_optimizer_api
- machine: linux-x86_64
- commit hash: 085e172
- commit date: 2025-01-21
- overall geometric mean: 1.002x slower
- HPT reliability: 95.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                 | 262 ms: 1.00x slower                                                         |
| docutils       | 2.69 sec                                                               | 2.70 sec: 1.00x slower                                                       |
| html5lib       | 62.6 ms                                                                | 64.6 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 466 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed    | 496 ms                                                                 | 485 ms: 1.02x faster                                                         |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (9): async_tree_io, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_generators, coroutines, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 87.2 ms                                                                | 86.7 ms: 1.01x faster                                                        |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                                | 23.6 ms: 1.01x faster                                                        |
| regex_compile  | 130 ms                                                                 | 130 ms: 1.01x slower                                                         |
| regex_dna      | 209 ms                                                                 | 212 ms: 1.01x slower                                                         |
| regex_effbot   | 3.24 ms                                                                | 3.30 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 96.0 ms                                                                | 94.0 ms: 1.02x faster                                                        |
| unpickle_pure_python | 205 us                                                                 | 206 us: 1.00x slower                                                         |
| xml_etree_generate   | 78.8 ms                                                                | 80.3 ms: 1.02x slower                                                        |
| pickle_pure_python   | 318 us                                                                 | 328 us: 1.03x slower                                                         |
| xml_etree_process    | 57.0 ms                                                                | 59.6 ms: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (4): xml_etree_parse, json_loads, json_dumps, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                | 12.9 ms: 1.00x faster                                                        |
| python_startup_no_site | 7.10 ms                                                                | 7.07 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 9.99 ms                                                                | 9.83 ms: 1.02x faster                                                        |
| django_template | 33.0 ms                                                                | 33.5 ms: 1.02x slower                                                        |
| genshi_xml      | 57.5 ms                                                                | 59.1 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| scimark_sparse_mat_mult    | 4.61 ms                                                                | 4.42 ms: 1.04x faster                                                        |
| generators                 | 38.8 ms                                                                | 37.2 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 466 ms: 1.03x faster                                                         |
| deepcopy_reduce            | 2.76 us                                                                | 2.69 us: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 496 ms                                                                 | 485 ms: 1.02x faster                                                         |
| xml_etree_iterparse        | 96.0 ms                                                                | 94.0 ms: 1.02x faster                                                        |
| mako                       | 9.99 ms                                                                | 9.83 ms: 1.02x faster                                                        |
| regex_v8                   | 23.9 ms                                                                | 23.6 ms: 1.01x faster                                                        |
| typing_runtime_protocols   | 169 us                                                                 | 167 us: 1.01x faster                                                         |
| gc_traversal               | 4.65 ms                                                                | 4.60 ms: 1.01x faster                                                        |
| scimark_monte_carlo        | 62.9 ms                                                                | 62.2 ms: 1.01x faster                                                        |
| deepcopy_memo              | 30.3 us                                                                | 30.0 us: 1.01x faster                                                        |
| nbody                      | 87.2 ms                                                                | 86.7 ms: 1.01x faster                                                        |
| sympy_sum                  | 156 ms                                                                 | 155 ms: 1.01x faster                                                         |
| create_gc_cycles           | 2.46 ms                                                                | 2.45 ms: 1.01x faster                                                        |
| bpe_tokeniser              | 4.38 sec                                                               | 4.36 sec: 1.00x faster                                                       |
| python_startup             | 12.9 ms                                                                | 12.9 ms: 1.00x faster                                                        |
| python_startup_no_site     | 7.10 ms                                                                | 7.07 ms: 1.00x faster                                                        |
| dulwich_log                | 68.1 ms                                                                | 67.9 ms: 1.00x faster                                                        |
| mdp                        | 2.56 sec                                                               | 2.56 sec: 1.00x faster                                                       |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                                         |
| bench_thread_pool          | 888 us                                                                 | 890 us: 1.00x slower                                                         |
| 2to3                       | 261 ms                                                                 | 262 ms: 1.00x slower                                                         |
| scimark_fft                | 312 ms                                                                 | 313 ms: 1.00x slower                                                         |
| connected_components       | 434 ms                                                                 | 436 ms: 1.00x slower                                                         |
| sympy_str                  | 280 ms                                                                 | 281 ms: 1.00x slower                                                         |
| docutils                   | 2.69 sec                                                               | 2.70 sec: 1.00x slower                                                       |
| shortest_path              | 476 ms                                                                 | 478 ms: 1.00x slower                                                         |
| unpickle_pure_python       | 205 us                                                                 | 206 us: 1.00x slower                                                         |
| sqlglot_optimize           | 54.6 ms                                                                | 54.9 ms: 1.01x slower                                                        |
| regex_compile              | 130 ms                                                                 | 130 ms: 1.01x slower                                                         |
| sympy_expand               | 472 ms                                                                 | 475 ms: 1.01x slower                                                         |
| richards                   | 46.8 ms                                                                | 47.1 ms: 1.01x slower                                                        |
| sqlite_synth               | 2.72 us                                                                | 2.74 us: 1.01x slower                                                        |
| fannkuch                   | 389 ms                                                                 | 393 ms: 1.01x slower                                                         |
| sqlalchemy_imperative      | 17.1 ms                                                                | 17.2 ms: 1.01x slower                                                        |
| sqlglot_parse              | 1.26 ms                                                                | 1.27 ms: 1.01x slower                                                        |
| comprehensions             | 17.2 us                                                                | 17.4 us: 1.01x slower                                                        |
| regex_dna                  | 209 ms                                                                 | 212 ms: 1.01x slower                                                         |
| hexiom                     | 7.03 ms                                                                | 7.11 ms: 1.01x slower                                                        |
| go                         | 131 ms                                                                 | 133 ms: 1.01x slower                                                         |
| chaos                      | 58.2 ms                                                                | 59.0 ms: 1.01x slower                                                        |
| scimark_sor                | 113 ms                                                                 | 115 ms: 1.01x slower                                                         |
| django_template            | 33.0 ms                                                                | 33.5 ms: 1.02x slower                                                        |
| nqueens                    | 89.5 ms                                                                | 90.9 ms: 1.02x slower                                                        |
| raytrace                   | 281 ms                                                                 | 286 ms: 1.02x slower                                                         |
| pprint_pformat             | 1.51 sec                                                               | 1.54 sec: 1.02x slower                                                       |
| regex_effbot               | 3.24 ms                                                                | 3.30 ms: 1.02x slower                                                        |
| spectral_norm              | 93.3 ms                                                                | 95.1 ms: 1.02x slower                                                        |
| xml_etree_generate         | 78.8 ms                                                                | 80.3 ms: 1.02x slower                                                        |
| logging_format             | 6.57 us                                                                | 6.71 us: 1.02x slower                                                        |
| genshi_xml                 | 57.5 ms                                                                | 59.1 ms: 1.03x slower                                                        |
| pyflate                    | 430 ms                                                                 | 443 ms: 1.03x slower                                                         |
| pickle_pure_python         | 318 us                                                                 | 328 us: 1.03x slower                                                         |
| html5lib                   | 62.6 ms                                                                | 64.6 ms: 1.03x slower                                                        |
| logging_simple             | 5.95 us                                                                | 6.15 us: 1.03x slower                                                        |
| logging_silent             | 107 ns                                                                 | 111 ns: 1.04x slower                                                         |
| xml_etree_process          | 57.0 ms                                                                | 59.6 ms: 1.05x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (38): async_tree_io, xml_etree_parse, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, subparsers, pylint, crypto_pyaes, meteor_contest, float, sqlglot_transpile, async_generators, json_loads, deepcopy, coroutines, genshi_text, richards_super, sqlglot_normalize, bench_mp_pool, asyncio_websockets, k_core, sqlalchemy_declarative, async_tree_none, pathlib, scimark_lu, many_optionals, sympy_integrate, json_dumps, thrift, pprint_safe_repr, telco, json, sphinx, coverage, tomli_loads, deltablue, pycparser

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 95.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x