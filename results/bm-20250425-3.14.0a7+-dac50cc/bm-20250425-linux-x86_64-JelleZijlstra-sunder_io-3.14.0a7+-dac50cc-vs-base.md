# Results vs. base

- fork: JelleZijlstra
- ref: sunder_io
- machine: linux-x86_64
- commit hash: dac50cc
- commit date: 2025-04-25
- overall geometric mean: 1.003x faster
- HPT reliability: 77.24%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 254 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| coroutines                       | 24.6 ms                                                                | 24.4 ms: 1.01x faster                                              |
| async_tree_eager                 | 103 ms                                                                 | 102 ms: 1.01x faster                                               |
| async_tree_memoization           | 314 ms                                                                 | 316 ms: 1.01x slower                                               |
| async_tree_eager_cpu_io_mixed_tg | 455 ms                                                                 | 458 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed          | 488 ms                                                                 | 492 ms: 1.01x slower                                               |
| async_generators                 | 398 ms                                                                 | 403 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed_tg       | 483 ms                                                                 | 489 ms: 1.01x slower                                               |
| async_tree_memoization_tg        | 308 ms                                                                 | 312 ms: 1.01x slower                                               |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (11): async_tree_eager_io, async_tree_io, asyncio_websockets, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed, async_tree_none, async_tree_eager_memoization, async_tree_none_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 103 ms                                                                 | 99.4 ms: 1.04x faster                                              |
| float          | 69.6 ms                                                                | 68.4 ms: 1.02x faster                                              |
| pidigits       | 187 ms                                                                 | 195 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 24.7 ms                                                                | 22.1 ms: 1.12x faster                                              |
| regex_compile  | 126 ms                                                                 | 125 ms: 1.01x faster                                               |
| regex_dna      | 206 ms                                                                 | 209 ms: 1.02x slower                                               |
| regex_effbot   | 3.11 ms                                                                | 3.19 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|--------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_generate | 85.8 ms                                                                | 84.9 ms: 1.01x faster                                              |
| xml_etree_process  | 60.0 ms                                                                | 59.5 ms: 1.01x faster                                              |
| tomli_loads        | 1.97 sec                                                               | 1.96 sec: 1.01x faster                                             |
| json_loads         | 30.2 us                                                                | 30.4 us: 1.00x slower                                              |
| xml_etree_parse    | 141 ms                                                                 | 143 ms: 1.01x slower                                               |
| json_dumps         | 11.6 ms                                                                | 11.8 ms: 1.01x slower                                              |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (3): pickle_pure_python, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 8.22 ms                                                                | 6.90 ms: 1.19x faster                                              |
| python_startup         | 13.3 ms                                                                | 13.3 ms: 1.00x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.09x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text    | 21.4 ms                                                                | 21.2 ms: 1.01x faster                                              |
| mako           | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                              |
| genshi_xml     | 48.8 ms                                                                | 49.5 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                        | bm-20250425-linux-x86_64-python-17718b0503e5d1c98725-3.14.0a7+-17718b0 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site           | 8.22 ms                                                                | 6.90 ms: 1.19x faster                                              |
| regex_v8                         | 24.7 ms                                                                | 22.1 ms: 1.12x faster                                              |
| scimark_sparse_mat_mult          | 4.95 ms                                                                | 4.76 ms: 1.04x faster                                              |
| nbody                            | 103 ms                                                                 | 99.4 ms: 1.04x faster                                              |
| logging_silent                   | 98.3 ns                                                                | 96.0 ns: 1.02x faster                                              |
| pyflate                          | 464 ms                                                                 | 454 ms: 1.02x faster                                               |
| fannkuch                         | 423 ms                                                                 | 415 ms: 1.02x faster                                               |
| float                            | 69.6 ms                                                                | 68.4 ms: 1.02x faster                                              |
| hexiom                           | 6.26 ms                                                                | 6.15 ms: 1.02x faster                                              |
| logging_format                   | 6.23 us                                                                | 6.13 us: 1.02x faster                                              |
| scimark_fft                      | 362 ms                                                                 | 356 ms: 1.02x faster                                               |
| subparsers                       | 21.0 ms                                                                | 20.7 ms: 1.01x faster                                              |
| crypto_pyaes                     | 73.7 ms                                                                | 72.7 ms: 1.01x faster                                              |
| richards                         | 43.5 ms                                                                | 43.0 ms: 1.01x faster                                              |
| scimark_sor                      | 120 ms                                                                 | 119 ms: 1.01x faster                                               |
| coroutines                       | 24.6 ms                                                                | 24.4 ms: 1.01x faster                                              |
| deepcopy_memo                    | 28.7 us                                                                | 28.4 us: 1.01x faster                                              |
| bpe_tokeniser                    | 4.54 sec                                                               | 4.49 sec: 1.01x faster                                             |
| xml_etree_generate               | 85.8 ms                                                                | 84.9 ms: 1.01x faster                                              |
| comprehensions                   | 17.1 us                                                                | 16.9 us: 1.01x faster                                              |
| logging_simple                   | 5.60 us                                                                | 5.54 us: 1.01x faster                                              |
| async_tree_eager                 | 103 ms                                                                 | 102 ms: 1.01x faster                                               |
| genshi_text                      | 21.4 ms                                                                | 21.2 ms: 1.01x faster                                              |
| sqlalchemy_declarative           | 132 ms                                                                 | 131 ms: 1.01x faster                                               |
| xml_etree_process                | 60.0 ms                                                                | 59.5 ms: 1.01x faster                                              |
| sympy_sum                        | 148 ms                                                                 | 147 ms: 1.01x faster                                               |
| regex_compile                    | 126 ms                                                                 | 125 ms: 1.01x faster                                               |
| nqueens                          | 81.1 ms                                                                | 80.5 ms: 1.01x faster                                              |
| meteor_contest                   | 107 ms                                                                 | 106 ms: 1.01x faster                                               |
| coverage                         | 93.4 ms                                                                | 92.8 ms: 1.01x faster                                              |
| sqlalchemy_imperative            | 17.1 ms                                                                | 17.0 ms: 1.01x faster                                              |
| sqlglot_v2_transpile             | 1.54 ms                                                                | 1.53 ms: 1.01x faster                                              |
| tomli_loads                      | 1.97 sec                                                               | 1.96 sec: 1.01x faster                                             |
| chaos                            | 57.2 ms                                                                | 56.9 ms: 1.01x faster                                              |
| sqlglot_v2_parse                 | 1.23 ms                                                                | 1.22 ms: 1.00x faster                                              |
| sqlglot_v2_normalize             | 105 ms                                                                 | 105 ms: 1.00x faster                                               |
| sqlglot_v2_optimize              | 52.3 ms                                                                | 52.0 ms: 1.00x faster                                              |
| sympy_integrate                  | 19.0 ms                                                                | 18.9 ms: 1.00x faster                                              |
| 2to3                             | 254 ms                                                                 | 254 ms: 1.00x faster                                               |
| many_optionals                   | 937 us                                                                 | 934 us: 1.00x faster                                               |
| python_startup                   | 13.3 ms                                                                | 13.3 ms: 1.00x slower                                              |
| json_loads                       | 30.2 us                                                                | 30.4 us: 1.00x slower                                              |
| async_tree_memoization           | 314 ms                                                                 | 316 ms: 1.01x slower                                               |
| create_gc_cycles                 | 2.47 ms                                                                | 2.48 ms: 1.01x slower                                              |
| connected_components             | 452 ms                                                                 | 456 ms: 1.01x slower                                               |
| go                               | 113 ms                                                                 | 113 ms: 1.01x slower                                               |
| gc_traversal                     | 4.81 ms                                                                | 4.84 ms: 1.01x slower                                              |
| raytrace                         | 261 ms                                                                 | 263 ms: 1.01x slower                                               |
| async_tree_eager_cpu_io_mixed_tg | 455 ms                                                                 | 458 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed          | 488 ms                                                                 | 492 ms: 1.01x slower                                               |
| sqlite_synth                     | 2.81 us                                                                | 2.84 us: 1.01x slower                                              |
| xml_etree_parse                  | 141 ms                                                                 | 143 ms: 1.01x slower                                               |
| mako                             | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                              |
| deltablue                        | 3.37 ms                                                                | 3.41 ms: 1.01x slower                                              |
| async_generators                 | 398 ms                                                                 | 403 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed_tg       | 483 ms                                                                 | 489 ms: 1.01x slower                                               |
| json_dumps                       | 11.6 ms                                                                | 11.8 ms: 1.01x slower                                              |
| generators                       | 29.1 ms                                                                | 29.5 ms: 1.01x slower                                              |
| async_tree_memoization_tg        | 308 ms                                                                 | 312 ms: 1.01x slower                                               |
| pathlib                          | 16.7 ms                                                                | 17.0 ms: 1.01x slower                                              |
| genshi_xml                       | 48.8 ms                                                                | 49.5 ms: 1.01x slower                                              |
| shortest_path                    | 496 ms                                                                 | 504 ms: 1.01x slower                                               |
| scimark_lu                       | 117 ms                                                                 | 119 ms: 1.02x slower                                               |
| pprint_safe_repr                 | 715 ms                                                                 | 728 ms: 1.02x slower                                               |
| pprint_pformat                   | 1.45 sec                                                               | 1.48 sec: 1.02x slower                                             |
| regex_dna                        | 206 ms                                                                 | 209 ms: 1.02x slower                                               |
| regex_effbot                     | 3.11 ms                                                                | 3.19 ms: 1.03x slower                                              |
| pidigits                         | 187 ms                                                                 | 195 ms: 1.04x slower                                               |
| typing_runtime_protocols         | 168 us                                                                 | 175 us: 1.04x slower                                               |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (34): richards_super, scimark_monte_carlo, pycparser, telco, html5lib, async_tree_eager_io, pickle_pure_python, sympy_str, async_tree_io, docutils, dulwich_log, asyncio_websockets, sphinx, unpickle_pure_python, k_core, sympy_expand, mdp, deepcopy, async_tree_eager_io_tg, pylint, bench_thread_pool, xml_etree_iterparse, deepcopy_reduce, django_template, async_tree_eager_cpu_io_mixed, async_tree_none, spectral_norm, bench_mp_pool, json, async_tree_eager_memoization, async_tree_none_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_eager_memoization_tg

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 77.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x