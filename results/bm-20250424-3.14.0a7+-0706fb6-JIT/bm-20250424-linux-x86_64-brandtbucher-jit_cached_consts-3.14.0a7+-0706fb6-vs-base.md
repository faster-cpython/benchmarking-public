# Results vs. base

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: 0706fb6
- commit date: 2025-04-24
- overall geometric mean: 1.002x faster
- HPT reliability: 79.30%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                 | 258 ms: 1.00x faster                                                      |
| html5lib       | 59.8 ms                                                                | 62.1 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|-------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines                    | 25.0 ms                                                                | 24.4 ms: 1.03x faster                                                     |
| async_tree_eager_cpu_io_mixed | 379 ms                                                                 | 381 ms: 1.01x slower                                                      |
| async_tree_memoization        | 313 ms                                                                 | 315 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg    | 478 ms                                                                 | 482 ms: 1.01x slower                                                      |
| async_tree_memoization_tg     | 306 ms                                                                 | 309 ms: 1.01x slower                                                      |
| async_tree_none_tg            | 250 ms                                                                 | 253 ms: 1.01x slower                                                      |
| async_generators              | 415 ms                                                                 | 422 ms: 1.02x slower                                                      |
| async_tree_io_tg              | 598 ms                                                                 | 613 ms: 1.03x slower                                                      |
| Geometric mean                | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (11): async_tree_eager, async_tree_eager_io, async_tree_io, async_tree_eager_io_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none, async_tree_eager_memoization, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_tg, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 71.2 ms                                                                | 70.8 ms: 1.01x faster                                                     |
| nbody          | 87.3 ms                                                                | 88.3 ms: 1.01x slower                                                     |
| pidigits       | 188 ms                                                                 | 194 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 201 ms                                                                 | 198 ms: 1.02x faster                                                      |
| regex_effbot   | 3.06 ms                                                                | 3.05 ms: 1.00x faster                                                     |
| regex_v8       | 22.4 ms                                                                | 23.2 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_process    | 56.8 ms                                                                | 56.2 ms: 1.01x faster                                                     |
| unpickle_pure_python | 209 us                                                                 | 208 us: 1.01x faster                                                      |
| xml_etree_generate   | 80.4 ms                                                                | 80.0 ms: 1.00x faster                                                     |
| xml_etree_iterparse  | 98.3 ms                                                                | 99.3 ms: 1.01x slower                                                     |
| tomli_loads          | 1.81 sec                                                               | 1.84 sec: 1.01x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (4): pickle_pure_python, json_dumps, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x faster                                                     |
| python_startup_no_site | 8.22 ms                                                                | 8.22 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                                | 11.1 ms: 1.01x faster                                                     |
| django_template | 31.9 ms                                                                | 32.3 ms: 1.01x slower                                                     |
| genshi_text     | 21.1 ms                                                                | 21.3 ms: 1.01x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                     | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|-------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pyflate                       | 457 ms                                                                 | 427 ms: 1.07x faster                                                      |
| pycparser                     | 1.18 sec                                                               | 1.14 sec: 1.03x faster                                                    |
| deltablue                     | 3.07 ms                                                                | 2.98 ms: 1.03x faster                                                     |
| coroutines                    | 25.0 ms                                                                | 24.4 ms: 1.03x faster                                                     |
| fannkuch                      | 424 ms                                                                 | 414 ms: 1.02x faster                                                      |
| spectral_norm                 | 105 ms                                                                 | 102 ms: 1.02x faster                                                      |
| subparsers                    | 21.0 ms                                                                | 20.6 ms: 1.02x faster                                                     |
| go                            | 128 ms                                                                 | 125 ms: 1.02x faster                                                      |
| richards                      | 36.6 ms                                                                | 35.9 ms: 1.02x faster                                                     |
| logging_format                | 6.20 us                                                                | 6.08 us: 1.02x faster                                                     |
| crypto_pyaes                  | 74.8 ms                                                                | 73.4 ms: 1.02x faster                                                     |
| scimark_sor                   | 122 ms                                                                 | 119 ms: 1.02x faster                                                      |
| regex_dna                     | 201 ms                                                                 | 198 ms: 1.02x faster                                                      |
| sqlite_synth                  | 2.76 us                                                                | 2.72 us: 1.01x faster                                                     |
| scimark_fft                   | 312 ms                                                                 | 308 ms: 1.01x faster                                                      |
| sqlalchemy_imperative         | 17.5 ms                                                                | 17.3 ms: 1.01x faster                                                     |
| logging_simple                | 5.61 us                                                                | 5.54 us: 1.01x faster                                                     |
| xml_etree_process             | 56.8 ms                                                                | 56.2 ms: 1.01x faster                                                     |
| sqlglot_v2_parse              | 1.26 ms                                                                | 1.24 ms: 1.01x faster                                                     |
| sqlglot_v2_transpile          | 1.58 ms                                                                | 1.56 ms: 1.01x faster                                                     |
| many_optionals                | 957 us                                                                 | 947 us: 1.01x faster                                                      |
| deepcopy_memo                 | 29.0 us                                                                | 28.7 us: 1.01x faster                                                     |
| pathlib                       | 16.8 ms                                                                | 16.7 ms: 1.01x faster                                                     |
| hexiom                        | 6.71 ms                                                                | 6.65 ms: 1.01x faster                                                     |
| coverage                      | 94.0 ms                                                                | 93.2 ms: 1.01x faster                                                     |
| generators                    | 30.2 ms                                                                | 29.9 ms: 1.01x faster                                                     |
| gc_traversal                  | 4.83 ms                                                                | 4.79 ms: 1.01x faster                                                     |
| chaos                         | 59.2 ms                                                                | 58.7 ms: 1.01x faster                                                     |
| dulwich_log                   | 61.1 ms                                                                | 60.6 ms: 1.01x faster                                                     |
| meteor_contest                | 110 ms                                                                 | 109 ms: 1.01x faster                                                      |
| float                         | 71.2 ms                                                                | 70.8 ms: 1.01x faster                                                     |
| sympy_expand                  | 469 ms                                                                 | 467 ms: 1.01x faster                                                      |
| unpickle_pure_python          | 209 us                                                                 | 208 us: 1.01x faster                                                      |
| mako                          | 11.1 ms                                                                | 11.1 ms: 1.01x faster                                                     |
| xml_etree_generate            | 80.4 ms                                                                | 80.0 ms: 1.00x faster                                                     |
| sympy_str                     | 270 ms                                                                 | 269 ms: 1.00x faster                                                      |
| 2to3                          | 259 ms                                                                 | 258 ms: 1.00x faster                                                      |
| regex_effbot                  | 3.06 ms                                                                | 3.05 ms: 1.00x faster                                                     |
| python_startup                | 13.2 ms                                                                | 13.2 ms: 1.00x faster                                                     |
| python_startup_no_site        | 8.22 ms                                                                | 8.22 ms: 1.00x faster                                                     |
| shortest_path                 | 488 ms                                                                 | 489 ms: 1.00x slower                                                      |
| sqlglot_v2_normalize          | 106 ms                                                                 | 106 ms: 1.00x slower                                                      |
| mdp                           | 1.21 sec                                                               | 1.21 sec: 1.00x slower                                                    |
| sympy_integrate               | 19.4 ms                                                                | 19.4 ms: 1.00x slower                                                     |
| bpe_tokeniser                 | 4.41 sec                                                               | 4.43 sec: 1.00x slower                                                    |
| connected_components          | 450 ms                                                                 | 454 ms: 1.01x slower                                                      |
| async_tree_eager_cpu_io_mixed | 379 ms                                                                 | 381 ms: 1.01x slower                                                      |
| create_gc_cycles              | 2.46 ms                                                                | 2.48 ms: 1.01x slower                                                     |
| async_tree_memoization        | 313 ms                                                                 | 315 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg    | 478 ms                                                                 | 482 ms: 1.01x slower                                                      |
| async_tree_memoization_tg     | 306 ms                                                                 | 309 ms: 1.01x slower                                                      |
| xml_etree_iterparse           | 98.3 ms                                                                | 99.3 ms: 1.01x slower                                                     |
| nbody                         | 87.3 ms                                                                | 88.3 ms: 1.01x slower                                                     |
| tomli_loads                   | 1.81 sec                                                               | 1.84 sec: 1.01x slower                                                    |
| django_template               | 31.9 ms                                                                | 32.3 ms: 1.01x slower                                                     |
| genshi_text                   | 21.1 ms                                                                | 21.3 ms: 1.01x slower                                                     |
| async_tree_none_tg            | 250 ms                                                                 | 253 ms: 1.01x slower                                                      |
| async_generators              | 415 ms                                                                 | 422 ms: 1.02x slower                                                      |
| pprint_safe_repr              | 725 ms                                                                 | 742 ms: 1.02x slower                                                      |
| async_tree_io_tg              | 598 ms                                                                 | 613 ms: 1.03x slower                                                      |
| regex_v8                      | 22.4 ms                                                                | 23.2 ms: 1.03x slower                                                     |
| pidigits                      | 188 ms                                                                 | 194 ms: 1.04x slower                                                      |
| html5lib                      | 59.8 ms                                                                | 62.1 ms: 1.04x slower                                                     |
| Geometric mean                | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (40): pickle_pure_python, richards_super, pprint_pformat, async_tree_eager, deepcopy_reduce, raytrace, sqlglot_v2_optimize, json, async_tree_eager_io, scimark_lu, bench_mp_pool, sqlalchemy_declarative, bench_thread_pool, docutils, json_dumps, pylint, async_tree_io, xml_etree_parse, async_tree_eager_io_tg, regex_compile, async_tree_cpu_io_mixed, asyncio_websockets, sympy_sum, comprehensions, telco, deepcopy, async_tree_none, async_tree_eager_memoization, async_tree_eager_cpu_io_mixed_tg, scimark_sparse_mat_mult, genshi_xml, sphinx, json_loads, nqueens, async_tree_eager_tg, typing_runtime_protocols, async_tree_eager_memoization_tg, scimark_monte_carlo, logging_silent, k_core

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 79.30% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x