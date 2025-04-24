# Results vs. base

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: d7c354b
- commit date: 2025-04-24
- overall geometric mean: 1.002x slower
- HPT reliability: 96.25%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                 | 260 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager                 | 106 ms                                                                 | 104 ms: 1.02x faster                                                      |
| async_generators                 | 420 ms                                                                 | 417 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed          | 487 ms                                                                 | 495 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg       | 476 ms                                                                 | 493 ms: 1.03x slower                                                      |
| async_tree_eager_cpu_io_mixed_tg | 449 ms                                                                 | 465 ms: 1.04x slower                                                      |
| async_tree_eager_cpu_io_mixed    | 378 ms                                                                 | 393 ms: 1.04x slower                                                      |
| coroutines                       | 24.2 ms                                                                | 25.4 ms: 1.05x slower                                                     |
| Geometric mean                   | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (12): async_tree_eager_memoization, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_eager_io_tg, asyncio_websockets, async_tree_io, async_tree_memoization, async_tree_eager_memoization_tg, async_tree_eager_io, async_tree_eager_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 195 ms                                                                 | 191 ms: 1.02x faster                                                      |
| nbody          | 88.8 ms                                                                | 87.1 ms: 1.02x faster                                                     |
| float          | 70.7 ms                                                                | 70.3 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.17 ms                                                                | 3.16 ms: 1.00x faster                                                     |
| regex_compile  | 126 ms                                                                 | 126 ms: 1.00x slower                                                      |
| regex_v8       | 23.2 ms                                                                | 23.8 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads         | 30.2 us                                                                | 29.8 us: 1.01x faster                                                     |
| json_dumps         | 11.5 ms                                                                | 11.5 ms: 1.01x faster                                                     |
| pickle_pure_python | 320 us                                                                 | 323 us: 1.01x slower                                                      |
| tomli_loads        | 1.83 sec                                                               | 1.85 sec: 1.01x slower                                                    |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_process, xml_etree_parse, xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                                | 11.2 ms: 1.01x slower                                                     |
| genshi_text     | 20.8 ms                                                                | 21.1 ms: 1.01x slower                                                     |
| genshi_xml      | 49.3 ms                                                                | 50.1 ms: 1.02x slower                                                     |
| django_template | 31.6 ms                                                                | 32.5 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pyflate                          | 448 ms                                                                 | 422 ms: 1.06x faster                                                      |
| generators                       | 30.9 ms                                                                | 29.7 ms: 1.04x faster                                                     |
| fannkuch                         | 424 ms                                                                 | 411 ms: 1.03x faster                                                      |
| deltablue                        | 3.06 ms                                                                | 2.99 ms: 1.03x faster                                                     |
| pidigits                         | 195 ms                                                                 | 191 ms: 1.02x faster                                                      |
| richards                         | 36.3 ms                                                                | 35.6 ms: 1.02x faster                                                     |
| nbody                            | 88.8 ms                                                                | 87.1 ms: 1.02x faster                                                     |
| async_tree_eager                 | 106 ms                                                                 | 104 ms: 1.02x faster                                                      |
| telco                            | 7.77 ms                                                                | 7.65 ms: 1.02x faster                                                     |
| json_loads                       | 30.2 us                                                                | 29.8 us: 1.01x faster                                                     |
| richards_super                   | 41.3 ms                                                                | 40.8 ms: 1.01x faster                                                     |
| sqlalchemy_imperative            | 17.3 ms                                                                | 17.1 ms: 1.01x faster                                                     |
| meteor_contest                   | 110 ms                                                                 | 109 ms: 1.01x faster                                                      |
| subparsers                       | 21.0 ms                                                                | 20.9 ms: 1.01x faster                                                     |
| json_dumps                       | 11.5 ms                                                                | 11.5 ms: 1.01x faster                                                     |
| float                            | 70.7 ms                                                                | 70.3 ms: 1.01x faster                                                     |
| async_generators                 | 420 ms                                                                 | 417 ms: 1.01x faster                                                      |
| sqlglot_v2_normalize             | 107 ms                                                                 | 107 ms: 1.00x faster                                                      |
| connected_components             | 454 ms                                                                 | 452 ms: 1.00x faster                                                      |
| regex_effbot                     | 3.17 ms                                                                | 3.16 ms: 1.00x faster                                                     |
| create_gc_cycles                 | 2.47 ms                                                                | 2.47 ms: 1.00x faster                                                     |
| python_startup                   | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                     |
| regex_compile                    | 126 ms                                                                 | 126 ms: 1.00x slower                                                      |
| dulwich_log                      | 60.9 ms                                                                | 61.0 ms: 1.00x slower                                                     |
| sympy_str                        | 269 ms                                                                 | 270 ms: 1.00x slower                                                      |
| bench_thread_pool                | 891 us                                                                 | 895 us: 1.00x slower                                                      |
| deepcopy                         | 251 us                                                                 | 252 us: 1.00x slower                                                      |
| 2to3                             | 259 ms                                                                 | 260 ms: 1.00x slower                                                      |
| sympy_expand                     | 466 ms                                                                 | 468 ms: 1.00x slower                                                      |
| many_optionals                   | 950 us                                                                 | 955 us: 1.00x slower                                                      |
| raytrace                         | 268 ms                                                                 | 270 ms: 1.01x slower                                                      |
| gc_traversal                     | 4.80 ms                                                                | 4.82 ms: 1.01x slower                                                     |
| comprehensions                   | 18.4 us                                                                | 18.5 us: 1.01x slower                                                     |
| sympy_sum                        | 147 ms                                                                 | 148 ms: 1.01x slower                                                      |
| sqlite_synth                     | 2.77 us                                                                | 2.78 us: 1.01x slower                                                     |
| sqlglot_v2_parse                 | 1.25 ms                                                                | 1.26 ms: 1.01x slower                                                     |
| sqlglot_v2_transpile             | 1.57 ms                                                                | 1.58 ms: 1.01x slower                                                     |
| coverage                         | 92.7 ms                                                                | 93.4 ms: 1.01x slower                                                     |
| pickle_pure_python               | 320 us                                                                 | 323 us: 1.01x slower                                                      |
| mako                             | 11.0 ms                                                                | 11.2 ms: 1.01x slower                                                     |
| hexiom                           | 6.57 ms                                                                | 6.64 ms: 1.01x slower                                                     |
| genshi_text                      | 20.8 ms                                                                | 21.1 ms: 1.01x slower                                                     |
| tomli_loads                      | 1.83 sec                                                               | 1.85 sec: 1.01x slower                                                    |
| chaos                            | 58.3 ms                                                                | 59.1 ms: 1.01x slower                                                     |
| scimark_sparse_mat_mult          | 4.69 ms                                                                | 4.75 ms: 1.01x slower                                                     |
| deepcopy_reduce                  | 2.67 us                                                                | 2.71 us: 1.01x slower                                                     |
| logging_simple                   | 5.60 us                                                                | 5.68 us: 1.01x slower                                                     |
| pathlib                          | 16.8 ms                                                                | 17.1 ms: 1.02x slower                                                     |
| logging_format                   | 6.15 us                                                                | 6.25 us: 1.02x slower                                                     |
| genshi_xml                       | 49.3 ms                                                                | 50.1 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed          | 487 ms                                                                 | 495 ms: 1.02x slower                                                      |
| spectral_norm                    | 103 ms                                                                 | 105 ms: 1.02x slower                                                      |
| scimark_sor                      | 118 ms                                                                 | 120 ms: 1.02x slower                                                      |
| scimark_lu                       | 117 ms                                                                 | 120 ms: 1.02x slower                                                      |
| regex_v8                         | 23.2 ms                                                                | 23.8 ms: 1.02x slower                                                     |
| logging_silent                   | 98.0 ns                                                                | 100 ns: 1.03x slower                                                      |
| django_template                  | 31.6 ms                                                                | 32.5 ms: 1.03x slower                                                     |
| json                             | 5.36 ms                                                                | 5.54 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed_tg       | 476 ms                                                                 | 493 ms: 1.03x slower                                                      |
| async_tree_eager_cpu_io_mixed_tg | 449 ms                                                                 | 465 ms: 1.04x slower                                                      |
| deepcopy_memo                    | 28.3 us                                                                | 29.3 us: 1.04x slower                                                     |
| async_tree_eager_cpu_io_mixed    | 378 ms                                                                 | 393 ms: 1.04x slower                                                      |
| coroutines                       | 24.2 ms                                                                | 25.4 ms: 1.05x slower                                                     |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (40): async_tree_eager_memoization, pprint_safe_repr, pprint_pformat, async_tree_none, sqlalchemy_declarative, docutils, shortest_path, crypto_pyaes, bpe_tokeniser, html5lib, pylint, sympy_integrate, async_tree_none_tg, mdp, sqlglot_v2_optimize, xml_etree_generate, python_startup_no_site, regex_dna, sphinx, async_tree_memoization_tg, nqueens, xml_etree_process, typing_runtime_protocols, xml_etree_parse, async_tree_eager_io_tg, scimark_fft, xml_etree_iterparse, asyncio_websockets, unpickle_pure_python, bench_mp_pool, go, async_tree_io, async_tree_memoization, async_tree_eager_memoization_tg, pycparser, k_core, async_tree_eager_io, scimark_monte_carlo, async_tree_eager_tg, async_tree_io_tg

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 96.25% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x