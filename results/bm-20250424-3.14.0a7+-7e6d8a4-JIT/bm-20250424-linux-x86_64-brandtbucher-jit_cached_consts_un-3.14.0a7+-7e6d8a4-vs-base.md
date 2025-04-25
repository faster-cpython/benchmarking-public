# Results vs. base

- fork: brandtbucher
- ref: jit_cached_consts_un
- machine: linux-x86_64
- commit hash: 7e6d8a4
- commit date: 2025-04-24
- overall geometric mean: 1.002x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                 | 260 ms: 1.00x slower                                                         |
| docutils       | 2.67 sec                                                               | 2.68 sec: 1.00x slower                                                       |
| html5lib       | 60.3 ms                                                                | 63.2 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_generators                 | 420 ms                                                                 | 422 ms: 1.01x slower                                                         |
| async_tree_eager_io_tg           | 612 ms                                                                 | 618 ms: 1.01x slower                                                         |
| async_tree_eager_io              | 621 ms                                                                 | 628 ms: 1.01x slower                                                         |
| async_tree_none_tg               | 250 ms                                                                 | 253 ms: 1.01x slower                                                         |
| async_tree_eager_cpu_io_mixed    | 378 ms                                                                 | 383 ms: 1.01x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 449 ms                                                                 | 458 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg       | 476 ms                                                                 | 486 ms: 1.02x slower                                                         |
| coroutines                       | 24.2 ms                                                                | 24.7 ms: 1.02x slower                                                        |
| Geometric mean                   | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (11): async_tree_eager_memoization, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_none, async_tree_eager_tg, async_tree_eager, async_tree_io, async_tree_memoization, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 195 ms                                                                 | 190 ms: 1.03x faster                                                         |
| float          | 70.7 ms                                                                | 69.5 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 126 ms                                                                 | 127 ms: 1.01x slower                                                         |
| regex_dna      | 202 ms                                                                 | 204 ms: 1.01x slower                                                         |
| regex_v8       | 23.2 ms                                                                | 23.8 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 80.5 ms                                                                | 79.7 ms: 1.01x faster                                                        |
| xml_etree_process    | 56.3 ms                                                                | 55.8 ms: 1.01x faster                                                        |
| unpickle_pure_python | 209 us                                                                 | 208 us: 1.01x faster                                                         |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (6): pickle_pure_python, xml_etree_iterparse, json_dumps, json_loads, xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.21 ms                                                                | 8.27 ms: 1.01x slower                                                        |
| python_startup         | 13.2 ms                                                                | 13.3 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                                | 11.1 ms: 1.00x slower                                                        |
| genshi_text     | 20.8 ms                                                                | 21.1 ms: 1.01x slower                                                        |
| django_template | 31.6 ms                                                                | 32.2 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pyflate                          | 448 ms                                                                 | 433 ms: 1.04x faster                                                         |
| fannkuch                         | 424 ms                                                                 | 413 ms: 1.03x faster                                                         |
| pidigits                         | 195 ms                                                                 | 190 ms: 1.03x faster                                                         |
| spectral_norm                    | 103 ms                                                                 | 100 ms: 1.03x faster                                                         |
| deltablue                        | 3.06 ms                                                                | 3.00 ms: 1.02x faster                                                        |
| generators                       | 30.9 ms                                                                | 30.4 ms: 1.02x faster                                                        |
| float                            | 70.7 ms                                                                | 69.5 ms: 1.02x faster                                                        |
| subparsers                       | 21.0 ms                                                                | 20.8 ms: 1.01x faster                                                        |
| xml_etree_generate               | 80.5 ms                                                                | 79.7 ms: 1.01x faster                                                        |
| xml_etree_process                | 56.3 ms                                                                | 55.8 ms: 1.01x faster                                                        |
| crypto_pyaes                     | 74.5 ms                                                                | 73.9 ms: 1.01x faster                                                        |
| bpe_tokeniser                    | 4.43 sec                                                               | 4.39 sec: 1.01x faster                                                       |
| scimark_fft                      | 314 ms                                                                 | 312 ms: 1.01x faster                                                         |
| scimark_sparse_mat_mult          | 4.69 ms                                                                | 4.65 ms: 1.01x faster                                                        |
| go                               | 126 ms                                                                 | 125 ms: 1.01x faster                                                         |
| logging_simple                   | 5.60 us                                                                | 5.56 us: 1.01x faster                                                        |
| sqlglot_v2_normalize             | 107 ms                                                                 | 106 ms: 1.01x faster                                                         |
| unpickle_pure_python             | 209 us                                                                 | 208 us: 1.01x faster                                                         |
| shortest_path                    | 496 ms                                                                 | 493 ms: 1.00x faster                                                         |
| sqlglot_v2_optimize              | 53.2 ms                                                                | 53.3 ms: 1.00x slower                                                        |
| docutils                         | 2.67 sec                                                               | 2.68 sec: 1.00x slower                                                       |
| bench_thread_pool                | 891 us                                                                 | 894 us: 1.00x slower                                                         |
| sympy_str                        | 269 ms                                                                 | 270 ms: 1.00x slower                                                         |
| create_gc_cycles                 | 2.47 ms                                                                | 2.48 ms: 1.00x slower                                                        |
| mako                             | 11.0 ms                                                                | 11.1 ms: 1.00x slower                                                        |
| 2to3                             | 259 ms                                                                 | 260 ms: 1.00x slower                                                         |
| scimark_sor                      | 118 ms                                                                 | 119 ms: 1.00x slower                                                         |
| sympy_sum                        | 147 ms                                                                 | 148 ms: 1.00x slower                                                         |
| sqlalchemy_declarative           | 133 ms                                                                 | 134 ms: 1.01x slower                                                         |
| dulwich_log                      | 60.9 ms                                                                | 61.2 ms: 1.01x slower                                                        |
| async_generators                 | 420 ms                                                                 | 422 ms: 1.01x slower                                                         |
| bench_mp_pool                    | 81.3 ms                                                                | 81.8 ms: 1.01x slower                                                        |
| python_startup_no_site           | 8.21 ms                                                                | 8.27 ms: 1.01x slower                                                        |
| regex_compile                    | 126 ms                                                                 | 127 ms: 1.01x slower                                                         |
| sqlite_synth                     | 2.77 us                                                                | 2.79 us: 1.01x slower                                                        |
| python_startup                   | 13.2 ms                                                                | 13.3 ms: 1.01x slower                                                        |
| deepcopy                         | 251 us                                                                 | 253 us: 1.01x slower                                                         |
| chaos                            | 58.3 ms                                                                | 58.8 ms: 1.01x slower                                                        |
| sqlglot_v2_parse                 | 1.25 ms                                                                | 1.26 ms: 1.01x slower                                                        |
| regex_dna                        | 202 ms                                                                 | 204 ms: 1.01x slower                                                         |
| async_tree_eager_io_tg           | 612 ms                                                                 | 618 ms: 1.01x slower                                                         |
| scimark_monte_carlo              | 66.8 ms                                                                | 67.5 ms: 1.01x slower                                                        |
| comprehensions                   | 18.4 us                                                                | 18.6 us: 1.01x slower                                                        |
| coverage                         | 92.7 ms                                                                | 93.7 ms: 1.01x slower                                                        |
| hexiom                           | 6.57 ms                                                                | 6.64 ms: 1.01x slower                                                        |
| async_tree_eager_io              | 621 ms                                                                 | 628 ms: 1.01x slower                                                         |
| async_tree_none_tg               | 250 ms                                                                 | 253 ms: 1.01x slower                                                         |
| logging_format                   | 6.15 us                                                                | 6.24 us: 1.01x slower                                                        |
| async_tree_eager_cpu_io_mixed    | 378 ms                                                                 | 383 ms: 1.01x slower                                                         |
| genshi_text                      | 20.8 ms                                                                | 21.1 ms: 1.01x slower                                                        |
| django_template                  | 31.6 ms                                                                | 32.2 ms: 1.02x slower                                                        |
| async_tree_eager_cpu_io_mixed_tg | 449 ms                                                                 | 458 ms: 1.02x slower                                                         |
| connected_components             | 454 ms                                                                 | 464 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg       | 476 ms                                                                 | 486 ms: 1.02x slower                                                         |
| coroutines                       | 24.2 ms                                                                | 24.7 ms: 1.02x slower                                                        |
| scimark_lu                       | 117 ms                                                                 | 119 ms: 1.02x slower                                                         |
| json                             | 5.36 ms                                                                | 5.49 ms: 1.02x slower                                                        |
| regex_v8                         | 23.2 ms                                                                | 23.8 ms: 1.03x slower                                                        |
| deepcopy_memo                    | 28.3 us                                                                | 29.3 us: 1.03x slower                                                        |
| logging_silent                   | 98.0 ns                                                                | 102 ns: 1.04x slower                                                         |
| html5lib                         | 60.3 ms                                                                | 63.2 ms: 1.05x slower                                                        |
| gc_traversal                     | 4.80 ms                                                                | 5.03 ms: 1.05x slower                                                        |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (41): async_tree_eager_memoization, pprint_pformat, telco, typing_runtime_protocols, richards_super, pickle_pure_python, richards, pathlib, meteor_contest, sympy_expand, deepcopy_reduce, mdp, xml_etree_iterparse, k_core, sqlalchemy_imperative, raytrace, asyncio_websockets, json_dumps, sympy_integrate, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, json_loads, regex_effbot, sphinx, async_tree_none, pprint_safe_repr, async_tree_eager_tg, async_tree_eager, pylint, xml_etree_parse, sqlglot_v2_transpile, many_optionals, genshi_xml, tomli_loads, nbody, nqueens, async_tree_io, pycparser, async_tree_memoization, async_tree_memoization_tg, async_tree_io_tg

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x