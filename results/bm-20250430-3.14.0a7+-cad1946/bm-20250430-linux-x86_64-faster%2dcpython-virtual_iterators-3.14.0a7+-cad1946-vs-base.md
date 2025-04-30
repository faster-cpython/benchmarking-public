# Results vs. base

- fork: faster-cpython
- ref: virtual_iterators
- machine: linux-x86_64
- commit hash: cad1946
- commit date: 2025-04-30
- overall geometric mean: 1.003x faster
- HPT reliability: 81.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250430-linux-x86_64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                 | 252 ms: 1.01x faster                                                          |
| docutils       | 2.62 sec                                                               | 2.60 sec: 1.01x faster                                                        |
| html5lib       | 60.4 ms                                                                | 60.9 ms: 1.01x slower                                                         |
| sphinx         | 1.02 sec                                                               | 1.00 sec: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250430-linux-x86_64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| coroutines                       | 25.7 ms                                                                | 24.8 ms: 1.04x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 386 ms                                                                 | 383 ms: 1.01x faster                                                          |
| async_tree_eager_cpu_io_mixed_tg | 459 ms                                                                 | 463 ms: 1.01x slower                                                          |
| async_tree_eager                 | 102 ms                                                                 | 103 ms: 1.01x slower                                                          |
| async_tree_io                    | 592 ms                                                                 | 598 ms: 1.01x slower                                                          |
| async_tree_memoization           | 312 ms                                                                 | 316 ms: 1.01x slower                                                          |
| async_tree_memoization_tg        | 306 ms                                                                 | 311 ms: 1.02x slower                                                          |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (12): async_tree_eager_io, asyncio_websockets, async_tree_eager_io_tg, async_tree_none, async_generators, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250430-linux-x86_64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 101 ms                                                                 | 98.8 ms: 1.02x faster                                                         |
| pidigits       | 187 ms                                                                 | 190 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250430-linux-x86_64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.14 ms                                                                | 3.10 ms: 1.01x faster                                                         |
| regex_dna      | 207 ms                                                                 | 205 ms: 1.01x faster                                                          |
| regex_v8       | 22.5 ms                                                                | 22.3 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250430-linux-x86_64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 143 ms                                                                 | 141 ms: 1.01x faster                                                          |
| json_loads           | 30.6 us                                                                | 30.4 us: 1.01x faster                                                         |
| unpickle_pure_python | 218 us                                                                 | 219 us: 1.00x slower                                                          |
| pickle_pure_python   | 317 us                                                                 | 319 us: 1.00x slower                                                          |
| json_dumps           | 12.0 ms                                                                | 12.1 ms: 1.01x slower                                                         |
| tomli_loads          | 1.98 sec                                                               | 2.01 sec: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250430-linux-x86_64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.92 ms                                                                | 6.92 ms: 1.00x slower                                                         |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                         |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250430-linux-x86_64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml     | 50.1 ms                                                                | 49.2 ms: 1.02x faster                                                         |
| genshi_text    | 21.2 ms                                                                | 21.0 ms: 1.01x faster                                                         |
| mako           | 11.5 ms                                                                | 11.7 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                        | bm-20250430-linux-x86_64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| comprehensions                   | 17.0 us                                                                | 16.2 us: 1.05x faster                                                         |
| typing_runtime_protocols         | 168 us                                                                 | 161 us: 1.04x faster                                                          |
| coroutines                       | 25.7 ms                                                                | 24.8 ms: 1.04x faster                                                         |
| pprint_pformat                   | 1.49 sec                                                               | 1.46 sec: 1.02x faster                                                        |
| logging_format                   | 6.27 us                                                                | 6.13 us: 1.02x faster                                                         |
| hexiom                           | 6.28 ms                                                                | 6.14 ms: 1.02x faster                                                         |
| go                               | 112 ms                                                                 | 110 ms: 1.02x faster                                                          |
| pprint_safe_repr                 | 730 ms                                                                 | 715 ms: 1.02x faster                                                          |
| nbody                            | 101 ms                                                                 | 98.8 ms: 1.02x faster                                                         |
| sphinx                           | 1.02 sec                                                               | 1.00 sec: 1.02x faster                                                        |
| mdp                              | 1.24 sec                                                               | 1.22 sec: 1.02x faster                                                        |
| richards                         | 43.9 ms                                                                | 43.1 ms: 1.02x faster                                                         |
| genshi_xml                       | 50.1 ms                                                                | 49.2 ms: 1.02x faster                                                         |
| logging_simple                   | 5.65 us                                                                | 5.57 us: 1.02x faster                                                         |
| sqlalchemy_declarative           | 133 ms                                                                 | 131 ms: 1.01x faster                                                          |
| deepcopy                         | 260 us                                                                 | 256 us: 1.01x faster                                                          |
| sqlglot_v2_normalize             | 107 ms                                                                 | 106 ms: 1.01x faster                                                          |
| scimark_lu                       | 118 ms                                                                 | 117 ms: 1.01x faster                                                          |
| pathlib                          | 17.4 ms                                                                | 17.1 ms: 1.01x faster                                                         |
| regex_effbot                     | 3.14 ms                                                                | 3.10 ms: 1.01x faster                                                         |
| 2to3                             | 255 ms                                                                 | 252 ms: 1.01x faster                                                          |
| genshi_text                      | 21.2 ms                                                                | 21.0 ms: 1.01x faster                                                         |
| scimark_sor                      | 121 ms                                                                 | 119 ms: 1.01x faster                                                          |
| sqlglot_v2_optimize              | 53.1 ms                                                                | 52.5 ms: 1.01x faster                                                         |
| coverage                         | 94.1 ms                                                                | 93.2 ms: 1.01x faster                                                         |
| xml_etree_parse                  | 143 ms                                                                 | 141 ms: 1.01x faster                                                          |
| crypto_pyaes                     | 75.7 ms                                                                | 75.1 ms: 1.01x faster                                                         |
| regex_dna                        | 207 ms                                                                 | 205 ms: 1.01x faster                                                          |
| regex_v8                         | 22.5 ms                                                                | 22.3 ms: 1.01x faster                                                         |
| gc_traversal                     | 4.85 ms                                                                | 4.82 ms: 1.01x faster                                                         |
| dulwich_log                      | 60.2 ms                                                                | 59.7 ms: 1.01x faster                                                         |
| telco                            | 7.99 ms                                                                | 7.93 ms: 1.01x faster                                                         |
| bpe_tokeniser                    | 4.53 sec                                                               | 4.50 sec: 1.01x faster                                                        |
| async_tree_eager_cpu_io_mixed    | 386 ms                                                                 | 383 ms: 1.01x faster                                                          |
| json_loads                       | 30.6 us                                                                | 30.4 us: 1.01x faster                                                         |
| docutils                         | 2.62 sec                                                               | 2.60 sec: 1.01x faster                                                        |
| raytrace                         | 270 ms                                                                 | 268 ms: 1.01x faster                                                          |
| many_optionals                   | 939 us                                                                 | 934 us: 1.01x faster                                                          |
| bench_thread_pool                | 889 us                                                                 | 885 us: 1.00x faster                                                          |
| meteor_contest                   | 106 ms                                                                 | 105 ms: 1.00x faster                                                          |
| create_gc_cycles                 | 2.48 ms                                                                | 2.48 ms: 1.00x faster                                                         |
| python_startup_no_site           | 6.92 ms                                                                | 6.92 ms: 1.00x slower                                                         |
| python_startup                   | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                         |
| unpickle_pure_python             | 218 us                                                                 | 219 us: 1.00x slower                                                          |
| sqlalchemy_imperative            | 17.1 ms                                                                | 17.1 ms: 1.00x slower                                                         |
| pickle_pure_python               | 317 us                                                                 | 319 us: 1.00x slower                                                          |
| fannkuch                         | 416 ms                                                                 | 418 ms: 1.01x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 459 ms                                                                 | 463 ms: 1.01x slower                                                          |
| html5lib                         | 60.4 ms                                                                | 60.9 ms: 1.01x slower                                                         |
| generators                       | 29.2 ms                                                                | 29.4 ms: 1.01x slower                                                         |
| json_dumps                       | 12.0 ms                                                                | 12.1 ms: 1.01x slower                                                         |
| scimark_fft                      | 368 ms                                                                 | 372 ms: 1.01x slower                                                          |
| deepcopy_memo                    | 28.6 us                                                                | 28.9 us: 1.01x slower                                                         |
| async_tree_eager                 | 102 ms                                                                 | 103 ms: 1.01x slower                                                          |
| async_tree_io                    | 592 ms                                                                 | 598 ms: 1.01x slower                                                          |
| sqlglot_v2_transpile             | 1.54 ms                                                                | 1.56 ms: 1.01x slower                                                         |
| scimark_monte_carlo              | 67.2 ms                                                                | 68.0 ms: 1.01x slower                                                         |
| async_tree_memoization           | 312 ms                                                                 | 316 ms: 1.01x slower                                                          |
| tomli_loads                      | 1.98 sec                                                               | 2.01 sec: 1.01x slower                                                        |
| sqlglot_v2_parse                 | 1.24 ms                                                                | 1.25 ms: 1.01x slower                                                         |
| chaos                            | 58.7 ms                                                                | 59.6 ms: 1.02x slower                                                         |
| async_tree_memoization_tg        | 306 ms                                                                 | 311 ms: 1.02x slower                                                          |
| logging_silent                   | 96.7 ns                                                                | 98.3 ns: 1.02x slower                                                         |
| pidigits                         | 187 ms                                                                 | 190 ms: 1.02x slower                                                          |
| mako                             | 11.5 ms                                                                | 11.7 ms: 1.02x slower                                                         |
| connected_components             | 453 ms                                                                 | 464 ms: 1.02x slower                                                          |
| shortest_path                    | 494 ms                                                                 | 510 ms: 1.03x slower                                                          |
| pyflate                          | 439 ms                                                                 | 457 ms: 1.04x slower                                                          |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (30): async_tree_eager_io, pycparser, sqlite_synth, json, float, deepcopy_reduce, richards_super, subparsers, nqueens, asyncio_websockets, async_tree_eager_io_tg, bench_mp_pool, regex_compile, spectral_norm, k_core, xml_etree_process, deltablue, scimark_sparse_mat_mult, xml_etree_iterparse, async_tree_none, xml_etree_generate, async_generators, async_tree_cpu_io_mixed_tg, django_template, async_tree_none_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg
Ignored benchmarks (5) of results/bm-20250430-3.14.0a7+-44e4c47/bm-20250430-linux-x86_64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47.json: pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 81.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x