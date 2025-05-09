# Results vs. base

- fork: faster-cpython
- ref: make_decref_a_call
- machine: darwin-arm64
- commit hash: bdf907f
- commit date: 2025-05-08
- overall geometric mean: 1.064x faster
- HPT reliability: 96.91%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250508-darwin-arm64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 193 ms                                                                | 188 ms: 1.02x faster                                                          |
| docutils       | 1.56 sec                                                              | 1.57 sec: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20250508-darwin-arm64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|---------------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed         | 442 ms                                                                | 439 ms: 1.01x faster                                                          |
| async_tree_eager_cpu_io_mixed   | 375 ms                                                                | 374 ms: 1.00x faster                                                          |
| async_tree_eager_memoization_tg | 187 ms                                                                | 189 ms: 1.01x slower                                                          |
| async_tree_io                   | 422 ms                                                                | 427 ms: 1.01x slower                                                          |
| async_tree_eager_io_tg          | 410 ms                                                                | 417 ms: 1.02x slower                                                          |
| coroutines                      | 19.7 ms                                                               | 20.3 ms: 1.03x slower                                                         |
| async_generators                | 275 ms                                                                | 293 ms: 1.07x slower                                                          |
| Geometric mean                  | (ref)                                                                 | 1.01x slower                                                                  |

Benchmark hidden because not significant (12): async_tree_eager_memoization, async_tree_io_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_eager, async_tree_memoization, async_tree_none_tg, async_tree_none, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_tg, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250508-darwin-arm64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 91.5 ms                                                               | 91.0 ms: 1.01x faster                                                         |
| float          | 58.2 ms                                                               | 58.8 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250508-darwin-arm64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 2.24 ms                                                               | 2.16 ms: 1.04x faster                                                         |
| regex_compile  | 85.8 ms                                                               | 84.4 ms: 1.02x faster                                                         |
| regex_dna      | 139 ms                                                                | 137 ms: 1.01x faster                                                          |
| regex_v8       | 16.1 ms                                                               | 16.3 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250508-darwin-arm64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 188 us                                                                | 178 us: 1.05x faster                                                          |
| tomli_loads          | 1.51 sec                                                              | 1.49 sec: 1.01x faster                                                        |
| pickle_pure_python   | 250 us                                                                | 249 us: 1.01x faster                                                          |
| json_loads           | 18.4 us                                                               | 18.6 us: 1.01x slower                                                         |
| xml_etree_iterparse  | 76.0 ms                                                               | 76.8 ms: 1.01x slower                                                         |
| xml_etree_process    | 45.6 ms                                                               | 46.3 ms: 1.02x slower                                                         |
| xml_etree_generate   | 61.2 ms                                                               | 62.8 ms: 1.03x slower                                                         |
| json_dumps           | 8.15 ms                                                               | 8.43 ms: 1.03x slower                                                         |
| xml_etree_parse      | 105 ms                                                                | 109 ms: 1.04x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250508-darwin-arm64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 12.6 ms                                                               | 11.9 ms: 1.06x faster                                                         |
| python_startup         | 16.8 ms                                                               | 16.3 ms: 1.03x faster                                                         |
| Geometric mean         | (ref)                                                                 | 1.05x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250508-darwin-arm64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.18 ms                                                               | 8.70 ms: 1.06x faster                                                         |
| django_template | 26.2 ms                                                               | 26.1 ms: 1.00x faster                                                         |
| genshi_xml      | 37.3 ms                                                               | 37.6 ms: 1.01x slower                                                         |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                       | bm-20250508-darwin-arm64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|---------------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                          | 44.0 ms                                                               | 509 us: 86.47x faster                                                         |
| coverage                        | 333 ms                                                                | 53.5 ms: 6.23x faster                                                         |
| dask                            | 859 ms                                                                | 770 ms: 1.12x faster                                                          |
| python_startup_no_site          | 12.6 ms                                                               | 11.9 ms: 1.06x faster                                                         |
| hexiom                          | 5.47 ms                                                               | 5.17 ms: 1.06x faster                                                         |
| deepcopy_memo                   | 23.8 us                                                               | 22.5 us: 1.06x faster                                                         |
| mako                            | 9.18 ms                                                               | 8.70 ms: 1.06x faster                                                         |
| go                              | 106 ms                                                                | 100 ms: 1.05x faster                                                          |
| unpickle_pure_python            | 188 us                                                                | 178 us: 1.05x faster                                                          |
| logging_silent                  | 79.5 ns                                                               | 76.2 ns: 1.04x faster                                                         |
| deltablue                       | 2.90 ms                                                               | 2.79 ms: 1.04x faster                                                         |
| regex_effbot                    | 2.24 ms                                                               | 2.16 ms: 1.04x faster                                                         |
| scimark_sor                     | 94.6 ms                                                               | 91.8 ms: 1.03x faster                                                         |
| richards                        | 39.0 ms                                                               | 37.8 ms: 1.03x faster                                                         |
| python_startup                  | 16.8 ms                                                               | 16.3 ms: 1.03x faster                                                         |
| richards_super                  | 44.2 ms                                                               | 42.9 ms: 1.03x faster                                                         |
| 2to3                            | 193 ms                                                                | 188 ms: 1.02x faster                                                          |
| nqueens                         | 75.2 ms                                                               | 73.8 ms: 1.02x faster                                                         |
| comprehensions                  | 14.5 us                                                               | 14.3 us: 1.02x faster                                                         |
| deepcopy                        | 187 us                                                                | 183 us: 1.02x faster                                                          |
| regex_compile                   | 85.8 ms                                                               | 84.4 ms: 1.02x faster                                                         |
| scimark_monte_carlo             | 53.8 ms                                                               | 53.0 ms: 1.02x faster                                                         |
| dulwich_log                     | 27.3 ms                                                               | 26.9 ms: 1.01x faster                                                         |
| tomli_loads                     | 1.51 sec                                                              | 1.49 sec: 1.01x faster                                                        |
| many_optionals                  | 509 us                                                                | 503 us: 1.01x faster                                                          |
| regex_dna                       | 139 ms                                                                | 137 ms: 1.01x faster                                                          |
| pprint_safe_repr                | 579 ms                                                                | 573 ms: 1.01x faster                                                          |
| pprint_pformat                  | 1.18 sec                                                              | 1.17 sec: 1.01x faster                                                        |
| sqlglot_v2_parse                | 990 us                                                                | 981 us: 1.01x faster                                                          |
| sqlglot_v2_transpile            | 1.17 ms                                                               | 1.16 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed         | 442 ms                                                                | 439 ms: 1.01x faster                                                          |
| bench_thread_pool               | 546 us                                                                | 542 us: 1.01x faster                                                          |
| pickle_pure_python              | 250 us                                                                | 249 us: 1.01x faster                                                          |
| nbody                           | 91.5 ms                                                               | 91.0 ms: 1.01x faster                                                         |
| deepcopy_reduce                 | 1.99 us                                                               | 1.98 us: 1.00x faster                                                         |
| async_tree_eager_cpu_io_mixed   | 375 ms                                                                | 374 ms: 1.00x faster                                                          |
| django_template                 | 26.2 ms                                                               | 26.1 ms: 1.00x faster                                                         |
| sympy_integrate                 | 11.6 ms                                                               | 11.7 ms: 1.00x slower                                                         |
| docutils                        | 1.56 sec                                                              | 1.57 sec: 1.00x slower                                                        |
| chaos                           | 46.9 ms                                                               | 47.1 ms: 1.00x slower                                                         |
| generators                      | 31.4 ms                                                               | 31.6 ms: 1.00x slower                                                         |
| json                            | 3.10 ms                                                               | 3.12 ms: 1.01x slower                                                         |
| raytrace                        | 206 ms                                                                | 208 ms: 1.01x slower                                                          |
| connected_components            | 313 ms                                                                | 315 ms: 1.01x slower                                                          |
| genshi_xml                      | 37.3 ms                                                               | 37.6 ms: 1.01x slower                                                         |
| json_loads                      | 18.4 us                                                               | 18.6 us: 1.01x slower                                                         |
| xml_etree_iterparse             | 76.0 ms                                                               | 76.8 ms: 1.01x slower                                                         |
| shortest_path                   | 341 ms                                                                | 344 ms: 1.01x slower                                                          |
| float                           | 58.2 ms                                                               | 58.8 ms: 1.01x slower                                                         |
| logging_format                  | 4.28 us                                                               | 4.33 us: 1.01x slower                                                         |
| logging_simple                  | 3.97 us                                                               | 4.02 us: 1.01x slower                                                         |
| async_tree_eager_memoization_tg | 187 ms                                                                | 189 ms: 1.01x slower                                                          |
| regex_v8                        | 16.1 ms                                                               | 16.3 ms: 1.01x slower                                                         |
| sympy_str                       | 160 ms                                                                | 162 ms: 1.01x slower                                                          |
| async_tree_io                   | 422 ms                                                                | 427 ms: 1.01x slower                                                          |
| xml_etree_process               | 45.6 ms                                                               | 46.3 ms: 1.02x slower                                                         |
| mdp                             | 868 ms                                                                | 881 ms: 1.02x slower                                                          |
| crypto_pyaes                    | 61.6 ms                                                               | 62.6 ms: 1.02x slower                                                         |
| async_tree_eager_io_tg          | 410 ms                                                                | 417 ms: 1.02x slower                                                          |
| sympy_sum                       | 82.6 ms                                                               | 84.3 ms: 1.02x slower                                                         |
| spectral_norm                   | 78.3 ms                                                               | 80.1 ms: 1.02x slower                                                         |
| typing_runtime_protocols        | 112 us                                                                | 115 us: 1.02x slower                                                          |
| xml_etree_generate              | 61.2 ms                                                               | 62.8 ms: 1.03x slower                                                         |
| coroutines                      | 19.7 ms                                                               | 20.3 ms: 1.03x slower                                                         |
| sympy_expand                    | 270 ms                                                                | 278 ms: 1.03x slower                                                          |
| sqlglot_v2_normalize            | 78.7 ms                                                               | 81.0 ms: 1.03x slower                                                         |
| sqlite_synth                    | 1.61 us                                                               | 1.66 us: 1.03x slower                                                         |
| json_dumps                      | 8.15 ms                                                               | 8.43 ms: 1.03x slower                                                         |
| xml_etree_parse                 | 105 ms                                                                | 109 ms: 1.04x slower                                                          |
| sqlglot_v2_optimize             | 37.6 ms                                                               | 39.2 ms: 1.04x slower                                                         |
| scimark_sparse_mat_mult         | 3.24 ms                                                               | 3.37 ms: 1.04x slower                                                         |
| bpe_tokeniser                   | 3.32 sec                                                              | 3.47 sec: 1.04x slower                                                        |
| fannkuch                        | 304 ms                                                                | 320 ms: 1.05x slower                                                          |
| pyflate                         | 350 ms                                                                | 369 ms: 1.05x slower                                                          |
| scimark_fft                     | 207 ms                                                                | 219 ms: 1.06x slower                                                          |
| meteor_contest                  | 77.6 ms                                                               | 82.5 ms: 1.06x slower                                                         |
| async_generators                | 275 ms                                                                | 293 ms: 1.07x slower                                                          |
| telco                           | 4.80 ms                                                               | 5.12 ms: 1.07x slower                                                         |
| scimark_lu                      | 83.1 ms                                                               | 91.2 ms: 1.10x slower                                                         |
| Geometric mean                  | (ref)                                                                 | 1.06x faster                                                                  |

Benchmark hidden because not significant (24): pycparser, async_tree_eager_memoization, html5lib, k_core, async_tree_io_tg, pidigits, gc_traversal, subparsers, async_tree_cpu_io_mixed_tg, asyncio_websockets, pylint, async_tree_eager, async_tree_memoization, genshi_text, create_gc_cycles, pathlib, async_tree_none_tg, bench_mp_pool, async_tree_none, async_tree_eager_cpu_io_mixed_tg, sphinx, async_tree_memoization_tg, async_tree_eager_tg, async_tree_eager_io

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 96.91% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x