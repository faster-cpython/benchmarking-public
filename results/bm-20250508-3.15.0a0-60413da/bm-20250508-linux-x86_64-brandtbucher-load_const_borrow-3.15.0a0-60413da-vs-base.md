# Results vs. base

- fork: brandtbucher
- ref: load_const_borrow
- machine: linux-x86_64
- commit hash: 60413da
- commit date: 2025-05-08
- overall geometric mean: 1.005x faster
- HPT reliability: 97.14%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250508-linux-x86_64-python-c492ac72525ea5887082-3.15.0a0-c492ac7 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                                | 257 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250508-linux-x86_64-python-c492ac72525ea5887082-3.15.0a0-c492ac7 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed    | 398 ms                                                                | 381 ms: 1.05x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 473 ms                                                                | 453 ms: 1.04x faster                                                     |
| async_tree_cpu_io_mixed_tg       | 499 ms                                                                | 482 ms: 1.03x faster                                                     |
| coroutines                       | 25.1 ms                                                               | 24.4 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed          | 506 ms                                                                | 493 ms: 1.03x faster                                                     |
| async_tree_eager                 | 104 ms                                                                | 103 ms: 1.02x faster                                                     |
| async_generators                 | 402 ms                                                                | 410 ms: 1.02x slower                                                     |
| Geometric mean                   | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (12): async_tree_memoization_tg, async_tree_eager_memoization, async_tree_eager_io, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_none_tg, async_tree_eager_io_tg, asyncio_websockets, async_tree_io, async_tree_none, async_tree_memoization, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250508-linux-x86_64-python-c492ac72525ea5887082-3.15.0a0-c492ac7 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 195 ms                                                                | 188 ms: 1.04x faster                                                     |
| nbody          | 99.6 ms                                                               | 96.0 ms: 1.04x faster                                                    |
| float          | 71.0 ms                                                               | 72.6 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250508-linux-x86_64-python-c492ac72525ea5887082-3.15.0a0-c492ac7 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.25 ms                                                               | 3.19 ms: 1.02x faster                                                    |
| regex_compile  | 128 ms                                                                | 127 ms: 1.01x faster                                                     |
| regex_dna      | 205 ms                                                                | 204 ms: 1.00x faster                                                     |
| regex_v8       | 23.1 ms                                                               | 23.4 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250508-linux-x86_64-python-c492ac72525ea5887082-3.15.0a0-c492ac7 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.06 sec                                                              | 2.03 sec: 1.02x faster                                                   |
| json_dumps           | 11.9 ms                                                               | 11.8 ms: 1.01x faster                                                    |
| pickle_pure_python   | 322 us                                                                | 319 us: 1.01x faster                                                     |
| unpickle_pure_python | 218 us                                                                | 217 us: 1.01x faster                                                     |
| xml_etree_process    | 59.8 ms                                                               | 60.2 ms: 1.01x slower                                                    |
| json_loads           | 29.8 us                                                               | 30.3 us: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250508-linux-x86_64-python-c492ac72525ea5887082-3.15.0a0-c492ac7 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.92 ms                                                               | 6.91 ms: 1.00x faster                                                    |
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250508-linux-x86_64-python-c492ac72525ea5887082-3.15.0a0-c492ac7 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 21.5 ms                                                               | 21.0 ms: 1.02x faster                                                    |
| genshi_xml      | 50.0 ms                                                               | 49.3 ms: 1.01x faster                                                    |
| mako            | 12.0 ms                                                               | 11.9 ms: 1.01x faster                                                    |
| django_template | 32.3 ms                                                               | 32.7 ms: 1.01x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                             |

All benchmarks:
===============

| Benchmark                        | bm-20250508-linux-x86_64-python-c492ac72525ea5887082-3.15.0a0-c492ac7 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| spectral_norm                    | 111 ms                                                                | 104 ms: 1.06x faster                                                     |
| scimark_sparse_mat_mult          | 5.26 ms                                                               | 5.00 ms: 1.05x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 398 ms                                                                | 381 ms: 1.05x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 473 ms                                                                | 453 ms: 1.04x faster                                                     |
| pidigits                         | 195 ms                                                                | 188 ms: 1.04x faster                                                     |
| nbody                            | 99.6 ms                                                               | 96.0 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg       | 499 ms                                                                | 482 ms: 1.03x faster                                                     |
| coroutines                       | 25.1 ms                                                               | 24.4 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed          | 506 ms                                                                | 493 ms: 1.03x faster                                                     |
| genshi_text                      | 21.5 ms                                                               | 21.0 ms: 1.02x faster                                                    |
| subparsers                       | 23.1 ms                                                               | 22.6 ms: 1.02x faster                                                    |
| meteor_contest                   | 108 ms                                                                | 106 ms: 1.02x faster                                                     |
| regex_effbot                     | 3.25 ms                                                               | 3.19 ms: 1.02x faster                                                    |
| typing_runtime_protocols         | 171 us                                                                | 168 us: 1.02x faster                                                     |
| crypto_pyaes                     | 75.2 ms                                                               | 73.8 ms: 1.02x faster                                                    |
| sqlite_synth                     | 2.89 us                                                               | 2.84 us: 1.02x faster                                                    |
| coverage                         | 426 ms                                                                | 419 ms: 1.02x faster                                                     |
| tomli_loads                      | 2.06 sec                                                              | 2.03 sec: 1.02x faster                                                   |
| async_tree_eager                 | 104 ms                                                                | 103 ms: 1.02x faster                                                     |
| deepcopy_memo                    | 29.9 us                                                               | 29.5 us: 1.01x faster                                                    |
| genshi_xml                       | 50.0 ms                                                               | 49.3 ms: 1.01x faster                                                    |
| chaos                            | 60.6 ms                                                               | 59.8 ms: 1.01x faster                                                    |
| scimark_monte_carlo              | 68.5 ms                                                               | 67.7 ms: 1.01x faster                                                    |
| sqlglot_v2_parse                 | 1.25 ms                                                               | 1.23 ms: 1.01x faster                                                    |
| sqlglot_v2_transpile             | 1.55 ms                                                               | 1.53 ms: 1.01x faster                                                    |
| fannkuch                         | 411 ms                                                                | 407 ms: 1.01x faster                                                     |
| mako                             | 12.0 ms                                                               | 11.9 ms: 1.01x faster                                                    |
| json_dumps                       | 11.9 ms                                                               | 11.8 ms: 1.01x faster                                                    |
| pickle_pure_python               | 322 us                                                                | 319 us: 1.01x faster                                                     |
| regex_compile                    | 128 ms                                                                | 127 ms: 1.01x faster                                                     |
| many_optionals                   | 972 us                                                                | 966 us: 1.01x faster                                                     |
| scimark_sor                      | 122 ms                                                                | 121 ms: 1.01x faster                                                     |
| unpickle_pure_python             | 218 us                                                                | 217 us: 1.01x faster                                                     |
| regex_dna                        | 205 ms                                                                | 204 ms: 1.00x faster                                                     |
| comprehensions                   | 16.9 us                                                               | 16.8 us: 1.00x faster                                                    |
| nqueens                          | 81.8 ms                                                               | 81.5 ms: 1.00x faster                                                    |
| deltablue                        | 3.42 ms                                                               | 3.40 ms: 1.00x faster                                                    |
| create_gc_cycles                 | 2.57 ms                                                               | 2.56 ms: 1.00x faster                                                    |
| bench_thread_pool                | 889 us                                                                | 886 us: 1.00x faster                                                     |
| 2to3                             | 257 ms                                                                | 257 ms: 1.00x faster                                                     |
| python_startup_no_site           | 6.92 ms                                                               | 6.91 ms: 1.00x faster                                                    |
| python_startup                   | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                                    |
| dulwich_log                      | 60.0 ms                                                               | 60.1 ms: 1.00x slower                                                    |
| sqlglot_v2_normalize             | 106 ms                                                                | 106 ms: 1.00x slower                                                     |
| mdp                              | 1.23 sec                                                              | 1.23 sec: 1.00x slower                                                   |
| deepcopy                         | 261 us                                                                | 262 us: 1.00x slower                                                     |
| thrift                           | 148 ms                                                                | 148 ms: 1.00x slower                                                     |
| telco                            | 7.98 ms                                                               | 8.03 ms: 1.01x slower                                                    |
| go                               | 114 ms                                                                | 115 ms: 1.01x slower                                                     |
| scimark_fft                      | 371 ms                                                                | 374 ms: 1.01x slower                                                     |
| xml_etree_process                | 59.8 ms                                                               | 60.2 ms: 1.01x slower                                                    |
| richards_super                   | 49.2 ms                                                               | 49.6 ms: 1.01x slower                                                    |
| richards                         | 43.1 ms                                                               | 43.4 ms: 1.01x slower                                                    |
| json                             | 5.32 ms                                                               | 5.36 ms: 1.01x slower                                                    |
| connected_components             | 451 ms                                                                | 455 ms: 1.01x slower                                                     |
| gc_traversal                     | 4.86 ms                                                               | 4.91 ms: 1.01x slower                                                    |
| generators                       | 29.4 ms                                                               | 29.7 ms: 1.01x slower                                                    |
| logging_format                   | 6.77 us                                                               | 6.85 us: 1.01x slower                                                    |
| pyflate                          | 443 ms                                                                | 448 ms: 1.01x slower                                                     |
| hexiom                           | 6.22 ms                                                               | 6.29 ms: 1.01x slower                                                    |
| django_template                  | 32.3 ms                                                               | 32.7 ms: 1.01x slower                                                    |
| pprint_pformat                   | 1.48 sec                                                              | 1.50 sec: 1.01x slower                                                   |
| regex_v8                         | 23.1 ms                                                               | 23.4 ms: 1.01x slower                                                    |
| bpe_tokeniser                    | 4.46 sec                                                              | 4.53 sec: 1.02x slower                                                   |
| json_loads                       | 29.8 us                                                               | 30.3 us: 1.02x slower                                                    |
| async_generators                 | 402 ms                                                                | 410 ms: 1.02x slower                                                     |
| deepcopy_reduce                  | 2.76 us                                                               | 2.81 us: 1.02x slower                                                    |
| float                            | 71.0 ms                                                               | 72.6 ms: 1.02x slower                                                    |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (35): async_tree_memoization_tg, async_tree_eager_memoization, pycparser, xml_etree_iterparse, sphinx, shortest_path, k_core, sympy_expand, async_tree_eager_io, dask, xml_etree_parse, xml_etree_generate, async_tree_eager_memoization_tg, bench_mp_pool, sqlglot_v2_optimize, async_tree_eager_tg, docutils, sympy_sum, async_tree_none_tg, sympy_str, pylint, async_tree_eager_io_tg, logging_simple, sympy_integrate, logging_silent, raytrace, asyncio_websockets, async_tree_io, pprint_safe_repr, async_tree_none, pathlib, async_tree_memoization, scimark_lu, html5lib, async_tree_io_tg

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 97.14% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x