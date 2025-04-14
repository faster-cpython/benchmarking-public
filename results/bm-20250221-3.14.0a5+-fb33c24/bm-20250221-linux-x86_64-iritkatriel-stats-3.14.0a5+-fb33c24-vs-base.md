# Results vs. base

- fork: iritkatriel
- ref: stats
- machine: linux-x86_64
- commit hash: fb33c24
- commit date: 2025-02-21
- overall geometric mean: 1.008x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 256 ms: 1.01x slower                                         |
| docutils       | 2.56 sec                                                               | 2.62 sec: 1.02x slower                                       |
| html5lib       | 59.8 ms                                                                | 61.6 ms: 1.03x slower                                        |
| sphinx         | 993 ms                                                                 | 1.01 sec: 1.02x slower                                       |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization     | 327 ms                                                                 | 320 ms: 1.02x faster                                         |
| async_generators           | 389 ms                                                                 | 387 ms: 1.01x faster                                         |
| async_tree_cpu_io_mixed_tg | 473 ms                                                                 | 476 ms: 1.01x slower                                         |
| coroutines                 | 23.5 ms                                                                | 23.8 ms: 1.01x slower                                        |
| async_tree_cpu_io_mixed    | 484 ms                                                                 | 493 ms: 1.02x slower                                         |
| async_tree_none_tg         | 247 ms                                                                 | 252 ms: 1.02x slower                                         |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (5): async_tree_io_tg, asyncio_websockets, async_tree_none, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                         |
| float          | 69.8 ms                                                                | 72.7 ms: 1.04x slower                                        |
| nbody          | 93.6 ms                                                                | 97.6 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 25.4 ms                                                                | 23.3 ms: 1.09x faster                                        |
| regex_compile  | 125 ms                                                                 | 126 ms: 1.01x slower                                         |
| regex_dna      | 216 ms                                                                 | 221 ms: 1.02x slower                                         |
| regex_effbot   | 3.06 ms                                                                | 3.46 ms: 1.13x slower                                        |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 141 ms                                                                 | 139 ms: 1.01x faster                                         |
| json_loads           | 30.0 us                                                                | 29.7 us: 1.01x faster                                        |
| unpickle_pure_python | 219 us                                                                 | 222 us: 1.01x slower                                         |
| pickle_pure_python   | 315 us                                                                 | 319 us: 1.01x slower                                         |
| json_dumps           | 11.5 ms                                                                | 11.8 ms: 1.02x slower                                        |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 7.07 ms                                                                | 7.06 ms: 1.00x faster                                        |
| python_startup         | 12.9 ms                                                                | 12.9 ms: 1.00x faster                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 31.7 ms                                                                | 31.8 ms: 1.00x slower                                        |
| genshi_text     | 21.5 ms                                                                | 21.9 ms: 1.02x slower                                        |
| genshi_xml      | 48.3 ms                                                                | 49.5 ms: 1.02x slower                                        |
| mako            | 11.0 ms                                                                | 11.2 ms: 1.02x slower                                        |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8                   | 25.4 ms                                                                | 23.3 ms: 1.09x faster                                        |
| nqueens                    | 83.3 ms                                                                | 81.6 ms: 1.02x faster                                        |
| async_tree_memoization     | 327 ms                                                                 | 320 ms: 1.02x faster                                         |
| xml_etree_parse            | 141 ms                                                                 | 139 ms: 1.01x faster                                         |
| dulwich_log                | 64.8 ms                                                                | 64.0 ms: 1.01x faster                                        |
| connected_components       | 440 ms                                                                 | 436 ms: 1.01x faster                                         |
| json_loads                 | 30.0 us                                                                | 29.7 us: 1.01x faster                                        |
| pathlib                    | 16.9 ms                                                                | 16.7 ms: 1.01x faster                                        |
| scimark_lu                 | 116 ms                                                                 | 115 ms: 1.01x faster                                         |
| spectral_norm              | 98.0 ms                                                                | 97.4 ms: 1.01x faster                                        |
| async_generators           | 389 ms                                                                 | 387 ms: 1.01x faster                                         |
| deltablue                  | 3.14 ms                                                                | 3.12 ms: 1.01x faster                                        |
| sympy_sum                  | 147 ms                                                                 | 147 ms: 1.00x faster                                         |
| python_startup_no_site     | 7.07 ms                                                                | 7.06 ms: 1.00x faster                                        |
| python_startup             | 12.9 ms                                                                | 12.9 ms: 1.00x faster                                        |
| gc_traversal               | 4.79 ms                                                                | 4.78 ms: 1.00x faster                                        |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                         |
| comprehensions             | 16.3 us                                                                | 16.4 us: 1.00x slower                                        |
| django_template            | 31.7 ms                                                                | 31.8 ms: 1.00x slower                                        |
| mdp                        | 2.49 sec                                                               | 2.50 sec: 1.00x slower                                       |
| bench_thread_pool          | 863 us                                                                 | 867 us: 1.00x slower                                         |
| pprint_pformat             | 1.47 sec                                                               | 1.47 sec: 1.01x slower                                       |
| deepcopy                   | 255 us                                                                 | 257 us: 1.01x slower                                         |
| async_tree_cpu_io_mixed_tg | 473 ms                                                                 | 476 ms: 1.01x slower                                         |
| generators                 | 27.9 ms                                                                | 28.0 ms: 1.01x slower                                        |
| thrift                     | 758 us                                                                 | 764 us: 1.01x slower                                         |
| many_optionals             | 934 us                                                                 | 941 us: 1.01x slower                                         |
| richards_super             | 50.3 ms                                                                | 50.7 ms: 1.01x slower                                        |
| 2to3                       | 253 ms                                                                 | 256 ms: 1.01x slower                                         |
| scimark_monte_carlo        | 67.1 ms                                                                | 67.8 ms: 1.01x slower                                        |
| unpickle_pure_python       | 219 us                                                                 | 222 us: 1.01x slower                                         |
| deepcopy_memo              | 29.8 us                                                                | 30.1 us: 1.01x slower                                        |
| pprint_safe_repr           | 714 ms                                                                 | 723 ms: 1.01x slower                                         |
| pickle_pure_python         | 315 us                                                                 | 319 us: 1.01x slower                                         |
| logging_format             | 6.15 us                                                                | 6.22 us: 1.01x slower                                        |
| regex_compile              | 125 ms                                                                 | 126 ms: 1.01x slower                                         |
| scimark_fft                | 343 ms                                                                 | 348 ms: 1.01x slower                                         |
| hexiom                     | 6.15 ms                                                                | 6.23 ms: 1.01x slower                                        |
| create_gc_cycles           | 2.45 ms                                                                | 2.48 ms: 1.01x slower                                        |
| subparsers                 | 20.4 ms                                                                | 20.7 ms: 1.01x slower                                        |
| coroutines                 | 23.5 ms                                                                | 23.8 ms: 1.01x slower                                        |
| sphinx                     | 993 ms                                                                 | 1.01 sec: 1.02x slower                                       |
| richards                   | 43.7 ms                                                                | 44.4 ms: 1.02x slower                                        |
| bpe_tokeniser              | 4.41 sec                                                               | 4.49 sec: 1.02x slower                                       |
| scimark_sparse_mat_mult    | 4.75 ms                                                                | 4.83 ms: 1.02x slower                                        |
| genshi_text                | 21.5 ms                                                                | 21.9 ms: 1.02x slower                                        |
| coverage                   | 89.5 ms                                                                | 91.0 ms: 1.02x slower                                        |
| async_tree_cpu_io_mixed    | 484 ms                                                                 | 493 ms: 1.02x slower                                         |
| bench_mp_pool              | 81.9 ms                                                                | 83.5 ms: 1.02x slower                                        |
| async_tree_none_tg         | 247 ms                                                                 | 252 ms: 1.02x slower                                         |
| chaos                      | 58.3 ms                                                                | 59.4 ms: 1.02x slower                                        |
| docutils                   | 2.56 sec                                                               | 2.62 sec: 1.02x slower                                       |
| json_dumps                 | 11.5 ms                                                                | 11.8 ms: 1.02x slower                                        |
| go                         | 115 ms                                                                 | 118 ms: 1.02x slower                                         |
| regex_dna                  | 216 ms                                                                 | 221 ms: 1.02x slower                                         |
| genshi_xml                 | 48.3 ms                                                                | 49.5 ms: 1.02x slower                                        |
| mako                       | 11.0 ms                                                                | 11.2 ms: 1.02x slower                                        |
| scimark_sor                | 120 ms                                                                 | 123 ms: 1.03x slower                                         |
| crypto_pyaes               | 72.8 ms                                                                | 74.7 ms: 1.03x slower                                        |
| html5lib                   | 59.8 ms                                                                | 61.6 ms: 1.03x slower                                        |
| logging_silent             | 102 ns                                                                 | 105 ns: 1.03x slower                                         |
| fannkuch                   | 402 ms                                                                 | 415 ms: 1.03x slower                                         |
| float                      | 69.8 ms                                                                | 72.7 ms: 1.04x slower                                        |
| nbody                      | 93.6 ms                                                                | 97.6 ms: 1.04x slower                                        |
| pycparser                  | 1.11 sec                                                               | 1.17 sec: 1.05x slower                                       |
| pyflate                    | 433 ms                                                                 | 470 ms: 1.09x slower                                         |
| regex_effbot               | 3.06 ms                                                                | 3.46 ms: 1.13x slower                                        |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                 |

Benchmark hidden because not significant (25): async_tree_io_tg, json, k_core, logging_simple, sqlite_synth, sympy_integrate, xml_etree_generate, sympy_expand, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, deepcopy_reduce, asyncio_websockets, pylint, xml_etree_process, sympy_str, tomli_loads, async_tree_none, xml_etree_iterparse, raytrace, typing_runtime_protocols, telco, meteor_contest, async_tree_io, async_tree_memoization_tg
Ignored benchmarks (4) of results/bm-20250221-3.14.0a5+-5d66c55/bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55.json: sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
Ignored benchmarks (4) of results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x