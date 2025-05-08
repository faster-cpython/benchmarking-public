# Results vs. base

- fork: faster-cpython
- ref: make_decref_a_call
- machine: linux-x86_64
- commit hash: bdf907f
- commit date: 2025-05-08
- overall geometric mean: 1.032x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250508-linux-x86_64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                                | 266 ms: 1.04x slower                                                          |
| docutils       | 2.61 sec                                                              | 2.69 sec: 1.03x slower                                                        |
| html5lib       | 61.7 ms                                                               | 63.8 ms: 1.03x slower                                                         |
| sphinx         | 1.02 sec                                                              | 1.05 sec: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250508-linux-x86_64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| asyncio_websockets               | 550 ms                                                                | 552 ms: 1.00x slower                                                          |
| async_tree_io_tg                 | 628 ms                                                                | 644 ms: 1.03x slower                                                          |
| async_tree_cpu_io_mixed_tg       | 489 ms                                                                | 505 ms: 1.03x slower                                                          |
| async_generators                 | 406 ms                                                                | 421 ms: 1.04x slower                                                          |
| async_tree_eager_cpu_io_mixed    | 391 ms                                                                | 406 ms: 1.04x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 462 ms                                                                | 480 ms: 1.04x slower                                                          |
| coroutines                       | 24.1 ms                                                               | 25.1 ms: 1.04x slower                                                         |
| async_tree_eager_tg              | 211 ms                                                                | 220 ms: 1.04x slower                                                          |
| async_tree_cpu_io_mixed          | 499 ms                                                                | 520 ms: 1.04x slower                                                          |
| async_tree_none                  | 263 ms                                                                | 275 ms: 1.04x slower                                                          |
| async_tree_eager_memoization_tg  | 277 ms                                                                | 289 ms: 1.05x slower                                                          |
| async_tree_io                    | 603 ms                                                                | 631 ms: 1.05x slower                                                          |
| async_tree_memoization_tg        | 308 ms                                                                | 322 ms: 1.05x slower                                                          |
| async_tree_none_tg               | 245 ms                                                                | 257 ms: 1.05x slower                                                          |
| async_tree_eager_io_tg           | 630 ms                                                                | 662 ms: 1.05x slower                                                          |
| async_tree_eager_io              | 623 ms                                                                | 656 ms: 1.05x slower                                                          |
| async_tree_eager_memoization     | 199 ms                                                                | 210 ms: 1.05x slower                                                          |
| async_tree_memoization           | 312 ms                                                                | 331 ms: 1.06x slower                                                          |
| async_tree_eager                 | 102 ms                                                                | 110 ms: 1.08x slower                                                          |
| Geometric mean                   | (ref)                                                                 | 1.04x slower                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250508-linux-x86_64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 102 ms                                                                | 104 ms: 1.01x slower                                                          |
| float          | 71.4 ms                                                               | 72.5 ms: 1.01x slower                                                         |
| pidigits       | 188 ms                                                                | 200 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250508-linux-x86_64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 24.0 ms                                                               | 23.8 ms: 1.01x faster                                                         |
| regex_dna      | 202 ms                                                                | 208 ms: 1.03x slower                                                          |
| regex_effbot   | 3.15 ms                                                               | 3.26 ms: 1.04x slower                                                         |
| regex_compile  | 128 ms                                                                | 133 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250508-linux-x86_64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.09 sec                                                              | 2.08 sec: 1.01x faster                                                        |
| xml_etree_parse      | 142 ms                                                                | 147 ms: 1.03x slower                                                          |
| xml_etree_iterparse  | 99.0 ms                                                               | 103 ms: 1.04x slower                                                          |
| json_dumps           | 11.9 ms                                                               | 12.5 ms: 1.04x slower                                                         |
| unpickle_pure_python | 218 us                                                                | 230 us: 1.05x slower                                                          |
| xml_etree_generate   | 85.3 ms                                                               | 90.1 ms: 1.06x slower                                                         |
| json_loads           | 29.6 us                                                               | 31.4 us: 1.06x slower                                                         |
| pickle_pure_python   | 319 us                                                                | 341 us: 1.07x slower                                                          |
| xml_etree_process    | 59.5 ms                                                               | 63.7 ms: 1.07x slower                                                         |
| Geometric mean       | (ref)                                                                 | 1.05x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250508-linux-x86_64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.93 ms                                                               | 7.01 ms: 1.01x slower                                                         |
| python_startup         | 12.2 ms                                                               | 12.4 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250508-linux-x86_64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 50.9 ms                                                               | 53.0 ms: 1.04x slower                                                         |
| mako            | 11.8 ms                                                               | 12.4 ms: 1.05x slower                                                         |
| django_template | 32.5 ms                                                               | 34.9 ms: 1.07x slower                                                         |
| genshi_text     | 21.1 ms                                                               | 23.4 ms: 1.11x slower                                                         |
| Geometric mean  | (ref)                                                                 | 1.07x slower                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20250508-linux-x86_64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                           | 149 ms                                                                | 832 us: 178.64x faster                                                        |
| coverage                         | 415 ms                                                                | 93.1 ms: 4.46x faster                                                         |
| dask                             | 915 ms                                                                | 774 ms: 1.18x faster                                                          |
| tomli_loads                      | 2.09 sec                                                              | 2.08 sec: 1.01x faster                                                        |
| regex_v8                         | 24.0 ms                                                               | 23.8 ms: 1.01x faster                                                         |
| spectral_norm                    | 108 ms                                                                | 107 ms: 1.00x faster                                                          |
| asyncio_websockets               | 550 ms                                                                | 552 ms: 1.00x slower                                                          |
| shortest_path                    | 490 ms                                                                | 494 ms: 1.01x slower                                                          |
| connected_components             | 455 ms                                                                | 459 ms: 1.01x slower                                                          |
| scimark_sparse_mat_mult          | 5.07 ms                                                               | 5.12 ms: 1.01x slower                                                         |
| python_startup_no_site           | 6.93 ms                                                               | 7.01 ms: 1.01x slower                                                         |
| pathlib                          | 17.1 ms                                                               | 17.3 ms: 1.01x slower                                                         |
| nbody                            | 102 ms                                                                | 104 ms: 1.01x slower                                                          |
| python_startup                   | 12.2 ms                                                               | 12.4 ms: 1.01x slower                                                         |
| float                            | 71.4 ms                                                               | 72.5 ms: 1.01x slower                                                         |
| bench_mp_pool                    | 93.5 ms                                                               | 95.1 ms: 1.02x slower                                                         |
| dulwich_log                      | 59.7 ms                                                               | 60.7 ms: 1.02x slower                                                         |
| scimark_sor                      | 120 ms                                                                | 123 ms: 1.02x slower                                                          |
| generators                       | 29.2 ms                                                               | 29.8 ms: 1.02x slower                                                         |
| bench_thread_pool                | 891 us                                                                | 909 us: 1.02x slower                                                          |
| chaos                            | 59.3 ms                                                               | 60.8 ms: 1.02x slower                                                         |
| async_tree_io_tg                 | 628 ms                                                                | 644 ms: 1.03x slower                                                          |
| sympy_integrate                  | 19.0 ms                                                               | 19.5 ms: 1.03x slower                                                         |
| scimark_monte_carlo              | 68.0 ms                                                               | 69.8 ms: 1.03x slower                                                         |
| gc_traversal                     | 4.95 ms                                                               | 5.08 ms: 1.03x slower                                                         |
| pycparser                        | 1.17 sec                                                              | 1.20 sec: 1.03x slower                                                        |
| docutils                         | 2.61 sec                                                              | 2.69 sec: 1.03x slower                                                        |
| sphinx                           | 1.02 sec                                                              | 1.05 sec: 1.03x slower                                                        |
| regex_dna                        | 202 ms                                                                | 208 ms: 1.03x slower                                                          |
| crypto_pyaes                     | 74.9 ms                                                               | 77.2 ms: 1.03x slower                                                         |
| async_tree_cpu_io_mixed_tg       | 489 ms                                                                | 505 ms: 1.03x slower                                                          |
| xml_etree_parse                  | 142 ms                                                                | 147 ms: 1.03x slower                                                          |
| many_optionals                   | 966 us                                                                | 998 us: 1.03x slower                                                          |
| html5lib                         | 61.7 ms                                                               | 63.8 ms: 1.03x slower                                                         |
| deepcopy_memo                    | 29.9 us                                                               | 30.9 us: 1.03x slower                                                         |
| sympy_sum                        | 149 ms                                                                | 154 ms: 1.04x slower                                                          |
| 2to3                             | 257 ms                                                                | 266 ms: 1.04x slower                                                          |
| xml_etree_iterparse              | 99.0 ms                                                               | 103 ms: 1.04x slower                                                          |
| async_generators                 | 406 ms                                                                | 421 ms: 1.04x slower                                                          |
| regex_effbot                     | 3.15 ms                                                               | 3.26 ms: 1.04x slower                                                         |
| async_tree_eager_cpu_io_mixed    | 391 ms                                                                | 406 ms: 1.04x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 462 ms                                                                | 480 ms: 1.04x slower                                                          |
| sympy_expand                     | 458 ms                                                                | 475 ms: 1.04x slower                                                          |
| genshi_xml                       | 50.9 ms                                                               | 53.0 ms: 1.04x slower                                                         |
| logging_simple                   | 5.56 us                                                               | 5.79 us: 1.04x slower                                                         |
| logging_format                   | 6.15 us                                                               | 6.40 us: 1.04x slower                                                         |
| raytrace                         | 270 ms                                                                | 281 ms: 1.04x slower                                                          |
| coroutines                       | 24.1 ms                                                               | 25.1 ms: 1.04x slower                                                         |
| async_tree_eager_tg              | 211 ms                                                                | 220 ms: 1.04x slower                                                          |
| async_tree_cpu_io_mixed          | 499 ms                                                                | 520 ms: 1.04x slower                                                          |
| json_dumps                       | 11.9 ms                                                               | 12.5 ms: 1.04x slower                                                         |
| sympy_str                        | 267 ms                                                                | 279 ms: 1.04x slower                                                          |
| async_tree_none                  | 263 ms                                                                | 275 ms: 1.04x slower                                                          |
| async_tree_eager_memoization_tg  | 277 ms                                                                | 289 ms: 1.05x slower                                                          |
| scimark_fft                      | 371 ms                                                                | 388 ms: 1.05x slower                                                          |
| async_tree_io                    | 603 ms                                                                | 631 ms: 1.05x slower                                                          |
| regex_compile                    | 128 ms                                                                | 133 ms: 1.05x slower                                                          |
| json                             | 5.29 ms                                                               | 5.53 ms: 1.05x slower                                                         |
| async_tree_memoization_tg        | 308 ms                                                                | 322 ms: 1.05x slower                                                          |
| async_tree_none_tg               | 245 ms                                                                | 257 ms: 1.05x slower                                                          |
| richards                         | 43.0 ms                                                               | 45.0 ms: 1.05x slower                                                         |
| telco                            | 8.06 ms                                                               | 8.45 ms: 1.05x slower                                                         |
| richards_super                   | 49.1 ms                                                               | 51.4 ms: 1.05x slower                                                         |
| typing_runtime_protocols         | 168 us                                                                | 177 us: 1.05x slower                                                          |
| bpe_tokeniser                    | 4.47 sec                                                              | 4.69 sec: 1.05x slower                                                        |
| mako                             | 11.8 ms                                                               | 12.4 ms: 1.05x slower                                                         |
| async_tree_eager_io_tg           | 630 ms                                                                | 662 ms: 1.05x slower                                                          |
| pprint_pformat                   | 1.49 sec                                                              | 1.57 sec: 1.05x slower                                                        |
| sqlglot_v2_parse                 | 1.24 ms                                                               | 1.30 ms: 1.05x slower                                                         |
| mdp                              | 1.22 sec                                                              | 1.29 sec: 1.05x slower                                                        |
| meteor_contest                   | 106 ms                                                                | 112 ms: 1.05x slower                                                          |
| go                               | 111 ms                                                                | 117 ms: 1.05x slower                                                          |
| async_tree_eager_io              | 623 ms                                                                | 656 ms: 1.05x slower                                                          |
| sqlglot_v2_transpile             | 1.55 ms                                                               | 1.63 ms: 1.05x slower                                                         |
| subparsers                       | 22.9 ms                                                               | 24.1 ms: 1.05x slower                                                         |
| async_tree_eager_memoization     | 199 ms                                                                | 210 ms: 1.05x slower                                                          |
| unpickle_pure_python             | 218 us                                                                | 230 us: 1.05x slower                                                          |
| logging_silent                   | 98.8 ns                                                               | 104 ns: 1.06x slower                                                          |
| deepcopy_reduce                  | 2.77 us                                                               | 2.92 us: 1.06x slower                                                         |
| pprint_safe_repr                 | 729 ms                                                                | 770 ms: 1.06x slower                                                          |
| xml_etree_generate               | 85.3 ms                                                               | 90.1 ms: 1.06x slower                                                         |
| nqueens                          | 81.9 ms                                                               | 86.6 ms: 1.06x slower                                                         |
| sqlglot_v2_optimize              | 52.6 ms                                                               | 55.6 ms: 1.06x slower                                                         |
| hexiom                           | 6.22 ms                                                               | 6.58 ms: 1.06x slower                                                         |
| sqlglot_v2_normalize             | 107 ms                                                                | 113 ms: 1.06x slower                                                          |
| deepcopy                         | 260 us                                                                | 276 us: 1.06x slower                                                          |
| json_loads                       | 29.6 us                                                               | 31.4 us: 1.06x slower                                                         |
| async_tree_memoization           | 312 ms                                                                | 331 ms: 1.06x slower                                                          |
| pyflate                          | 443 ms                                                                | 471 ms: 1.06x slower                                                          |
| pidigits                         | 188 ms                                                                | 200 ms: 1.06x slower                                                          |
| comprehensions                   | 16.7 us                                                               | 17.9 us: 1.07x slower                                                         |
| scimark_lu                       | 118 ms                                                                | 126 ms: 1.07x slower                                                          |
| pickle_pure_python               | 319 us                                                                | 341 us: 1.07x slower                                                          |
| xml_etree_process                | 59.5 ms                                                               | 63.7 ms: 1.07x slower                                                         |
| django_template                  | 32.5 ms                                                               | 34.9 ms: 1.07x slower                                                         |
| fannkuch                         | 410 ms                                                                | 441 ms: 1.08x slower                                                          |
| async_tree_eager                 | 102 ms                                                                | 110 ms: 1.08x slower                                                          |
| deltablue                        | 3.32 ms                                                               | 3.59 ms: 1.08x slower                                                         |
| genshi_text                      | 21.1 ms                                                               | 23.4 ms: 1.11x slower                                                         |
| Geometric mean                   | (ref)                                                                 | 1.03x faster                                                                  |

Benchmark hidden because not significant (4): create_gc_cycles, k_core, sqlite_synth, pylint
Ignored benchmarks (1) of results/bm-20250508-3.15.0a0-bdf907f/bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f.json: djangocms

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 0.99x