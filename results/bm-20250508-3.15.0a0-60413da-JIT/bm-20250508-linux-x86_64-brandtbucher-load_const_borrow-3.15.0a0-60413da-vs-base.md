# Results vs. base

- fork: brandtbucher
- ref: load_const_borrow
- machine: linux-x86_64
- commit hash: 60413da
- commit date: 2025-05-08
- overall geometric mean: 1.001x faster
- HPT reliability: 58.57%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250508-linux-x86_64-python-c492ac72525ea5887082-3.15.0a0-c492ac7 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                | 263 ms: 1.00x faster                                                     |
| docutils       | 2.67 sec                                                              | 2.66 sec: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250508-linux-x86_64-python-c492ac72525ea5887082-3.15.0a0-c492ac7 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed          | 497 ms                                                                | 487 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed_tg       | 490 ms                                                                | 480 ms: 1.02x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 463 ms                                                                | 455 ms: 1.02x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 390 ms                                                                | 384 ms: 1.02x faster                                                     |
| async_tree_memoization           | 314 ms                                                                | 312 ms: 1.01x faster                                                     |
| asyncio_websockets               | 553 ms                                                                | 551 ms: 1.00x faster                                                     |
| async_generators                 | 424 ms                                                                | 426 ms: 1.01x slower                                                     |
| coroutines                       | 24.9 ms                                                               | 25.1 ms: 1.01x slower                                                    |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (11): async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none, async_tree_eager_memoization, async_tree_io, async_tree_eager, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250508-linux-x86_64-python-c492ac72525ea5887082-3.15.0a0-c492ac7 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 93.6 ms                                                               | 89.5 ms: 1.05x faster                                                    |
| float          | 63.3 ms                                                               | 64.2 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250508-linux-x86_64-python-c492ac72525ea5887082-3.15.0a0-c492ac7 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.09 ms                                                               | 3.01 ms: 1.02x faster                                                    |
| regex_dna      | 201 ms                                                                | 197 ms: 1.02x faster                                                     |
| regex_v8       | 23.0 ms                                                               | 22.7 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250508-linux-x86_64-python-c492ac72525ea5887082-3.15.0a0-c492ac7 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps          | 12.0 ms                                                               | 11.9 ms: 1.02x faster                                                    |
| xml_etree_iterparse | 98.2 ms                                                               | 98.5 ms: 1.00x slower                                                    |
| xml_etree_process   | 55.6 ms                                                               | 56.0 ms: 1.01x slower                                                    |
| xml_etree_parse     | 140 ms                                                                | 142 ms: 1.01x slower                                                     |
| pickle_pure_python  | 321 us                                                                | 329 us: 1.03x slower                                                     |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (4): tomli_loads, unpickle_pure_python, json_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250508-linux-x86_64-python-c492ac72525ea5887082-3.15.0a0-c492ac7 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 6.96 ms: 1.00x faster                                                    |
| python_startup         | 12.3 ms                                                               | 12.3 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250508-linux-x86_64-python-c492ac72525ea5887082-3.15.0a0-c492ac7 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 50.2 ms                                                               | 49.1 ms: 1.02x faster                                                    |
| genshi_text     | 21.9 ms                                                               | 21.7 ms: 1.01x faster                                                    |
| mako            | 11.2 ms                                                               | 11.1 ms: 1.01x faster                                                    |
| django_template | 32.1 ms                                                               | 32.6 ms: 1.01x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                             |

All benchmarks:
===============

| Benchmark                        | bm-20250508-linux-x86_64-python-c492ac72525ea5887082-3.15.0a0-c492ac7 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody                            | 93.6 ms                                                               | 89.5 ms: 1.05x faster                                                    |
| regex_effbot                     | 3.09 ms                                                               | 3.01 ms: 1.02x faster                                                    |
| scimark_fft                      | 328 ms                                                                | 320 ms: 1.02x faster                                                     |
| genshi_xml                       | 50.2 ms                                                               | 49.1 ms: 1.02x faster                                                    |
| pprint_safe_repr                 | 743 ms                                                                | 728 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed          | 497 ms                                                                | 487 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed_tg       | 490 ms                                                                | 480 ms: 1.02x faster                                                     |
| comprehensions                   | 18.2 us                                                               | 17.9 us: 1.02x faster                                                    |
| async_tree_eager_cpu_io_mixed_tg | 463 ms                                                                | 455 ms: 1.02x faster                                                     |
| meteor_contest                   | 110 ms                                                                | 108 ms: 1.02x faster                                                     |
| regex_dna                        | 201 ms                                                                | 197 ms: 1.02x faster                                                     |
| json_dumps                       | 12.0 ms                                                               | 11.9 ms: 1.02x faster                                                    |
| gc_traversal                     | 5.02 ms                                                               | 4.94 ms: 1.02x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 390 ms                                                                | 384 ms: 1.02x faster                                                     |
| richards_super                   | 39.2 ms                                                               | 38.6 ms: 1.02x faster                                                    |
| regex_v8                         | 23.0 ms                                                               | 22.7 ms: 1.01x faster                                                    |
| scimark_monte_carlo              | 68.1 ms                                                               | 67.3 ms: 1.01x faster                                                    |
| create_gc_cycles                 | 2.59 ms                                                               | 2.56 ms: 1.01x faster                                                    |
| genshi_text                      | 21.9 ms                                                               | 21.7 ms: 1.01x faster                                                    |
| spectral_norm                    | 100 ms                                                                | 99.3 ms: 1.01x faster                                                    |
| sqlite_synth                     | 2.83 us                                                               | 2.80 us: 1.01x faster                                                    |
| richards                         | 34.4 ms                                                               | 34.2 ms: 1.01x faster                                                    |
| typing_runtime_protocols         | 171 us                                                                | 170 us: 1.01x faster                                                     |
| mako                             | 11.2 ms                                                               | 11.1 ms: 1.01x faster                                                    |
| bpe_tokeniser                    | 4.37 sec                                                              | 4.34 sec: 1.01x faster                                                   |
| async_tree_memoization           | 314 ms                                                                | 312 ms: 1.01x faster                                                     |
| docutils                         | 2.67 sec                                                              | 2.66 sec: 1.01x faster                                                   |
| python_startup_no_site           | 6.99 ms                                                               | 6.96 ms: 1.00x faster                                                    |
| asyncio_websockets               | 553 ms                                                                | 551 ms: 1.00x faster                                                     |
| python_startup                   | 12.3 ms                                                               | 12.3 ms: 1.00x faster                                                    |
| sympy_integrate                  | 19.5 ms                                                               | 19.4 ms: 1.00x faster                                                    |
| thrift                           | 149 ms                                                                | 148 ms: 1.00x faster                                                     |
| 2to3                             | 263 ms                                                                | 263 ms: 1.00x faster                                                     |
| xml_etree_iterparse              | 98.2 ms                                                               | 98.5 ms: 1.00x slower                                                    |
| shortest_path                    | 485 ms                                                                | 487 ms: 1.00x slower                                                     |
| sympy_expand                     | 472 ms                                                                | 474 ms: 1.00x slower                                                     |
| dulwich_log                      | 61.4 ms                                                               | 61.6 ms: 1.00x slower                                                    |
| sympy_str                        | 272 ms                                                                | 273 ms: 1.00x slower                                                     |
| dask                             | 924 ms                                                                | 928 ms: 1.00x slower                                                     |
| raytrace                         | 275 ms                                                                | 276 ms: 1.01x slower                                                     |
| async_generators                 | 424 ms                                                                | 426 ms: 1.01x slower                                                     |
| deepcopy_memo                    | 30.2 us                                                               | 30.4 us: 1.01x slower                                                    |
| many_optionals                   | 981 us                                                                | 986 us: 1.01x slower                                                     |
| sqlglot_v2_parse                 | 1.25 ms                                                               | 1.26 ms: 1.01x slower                                                    |
| scimark_sparse_mat_mult          | 4.88 ms                                                               | 4.92 ms: 1.01x slower                                                    |
| coroutines                       | 24.9 ms                                                               | 25.1 ms: 1.01x slower                                                    |
| sqlglot_v2_transpile             | 1.57 ms                                                               | 1.58 ms: 1.01x slower                                                    |
| go                               | 125 ms                                                                | 126 ms: 1.01x slower                                                     |
| xml_etree_process                | 55.6 ms                                                               | 56.0 ms: 1.01x slower                                                    |
| deltablue                        | 3.06 ms                                                               | 3.08 ms: 1.01x slower                                                    |
| chaos                            | 60.7 ms                                                               | 61.1 ms: 1.01x slower                                                    |
| coverage                         | 426 ms                                                                | 430 ms: 1.01x slower                                                     |
| sqlglot_v2_optimize              | 52.5 ms                                                               | 53.1 ms: 1.01x slower                                                    |
| xml_etree_parse                  | 140 ms                                                                | 142 ms: 1.01x slower                                                     |
| nqueens                          | 84.0 ms                                                               | 85.1 ms: 1.01x slower                                                    |
| float                            | 63.3 ms                                                               | 64.2 ms: 1.01x slower                                                    |
| django_template                  | 32.1 ms                                                               | 32.6 ms: 1.01x slower                                                    |
| hexiom                           | 6.62 ms                                                               | 6.72 ms: 1.01x slower                                                    |
| fannkuch                         | 407 ms                                                                | 413 ms: 1.01x slower                                                     |
| mdp                              | 1.23 sec                                                              | 1.25 sec: 1.02x slower                                                   |
| logging_silent                   | 468 ns                                                                | 476 ns: 1.02x slower                                                     |
| pycparser                        | 1.13 sec                                                              | 1.15 sec: 1.02x slower                                                   |
| pickle_pure_python               | 321 us                                                                | 329 us: 1.03x slower                                                     |
| pyflate                          | 435 ms                                                                | 447 ms: 1.03x slower                                                     |
| generators                       | 30.3 ms                                                               | 31.3 ms: 1.04x slower                                                    |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (38): json, async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, logging_simple, async_tree_none, sphinx, tomli_loads, async_tree_eager_memoization, connected_components, k_core, bench_thread_pool, deepcopy, pprint_pformat, scimark_lu, sqlglot_v2_normalize, pidigits, unpickle_pure_python, bench_mp_pool, deepcopy_reduce, regex_compile, subparsers, scimark_sor, sympy_sum, pylint, json_loads, async_tree_io, xml_etree_generate, async_tree_eager, pathlib, async_tree_eager_io, crypto_pyaes, logging_format, telco, html5lib, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 58.57% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x