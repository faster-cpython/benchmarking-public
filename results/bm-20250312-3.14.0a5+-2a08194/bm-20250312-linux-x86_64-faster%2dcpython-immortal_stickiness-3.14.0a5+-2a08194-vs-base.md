# Results vs. base

- fork: faster-cpython
- ref: immortal_stickiness
- machine: linux-x86_64
- commit hash: 2a08194
- commit date: 2025-03-12
- overall geometric mean: 1.002x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 256 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 251 ms                                                                 | 248 ms: 1.02x faster                                                            |
| async_generators           | 397 ms                                                                 | 391 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                                 | 485 ms: 1.01x faster                                                            |
| coroutines                 | 23.6 ms                                                                | 23.4 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 471 ms: 1.01x faster                                                            |
| async_tree_memoization     | 316 ms                                                                 | 315 ms: 1.01x faster                                                            |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (5): async_tree_io, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 196 ms                                                                 | 186 ms: 1.05x faster                                                            |
| nbody          | 97.3 ms                                                                | 95.7 ms: 1.02x faster                                                           |
| float          | 69.7 ms                                                                | 70.0 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                                | 23.5 ms: 1.02x faster                                                           |
| regex_compile  | 125 ms                                                                 | 125 ms: 1.00x faster                                                            |
| regex_effbot   | 3.48 ms                                                                | 3.53 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 320 us                                                                 | 314 us: 1.02x faster                                                            |
| xml_etree_process    | 58.7 ms                                                                | 58.0 ms: 1.01x faster                                                           |
| unpickle_pure_python | 219 us                                                                 | 217 us: 1.01x faster                                                            |
| xml_etree_generate   | 84.0 ms                                                                | 83.3 ms: 1.01x faster                                                           |
| json_dumps           | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                                           |
| json_loads           | 30.0 us                                                                | 30.2 us: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                           |
| python_startup_no_site | 8.20 ms                                                                | 8.19 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                                           |
| genshi_xml     | 49.2 ms                                                                | 49.9 ms: 1.01x slower                                                           |
| genshi_text    | 21.4 ms                                                                | 21.8 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| logging_silent             | 100 ns                                                                 | 93.6 ns: 1.07x faster                                                           |
| pidigits                   | 196 ms                                                                 | 186 ms: 1.05x faster                                                            |
| deltablue                  | 3.19 ms                                                                | 3.08 ms: 1.03x faster                                                           |
| richards                   | 43.9 ms                                                                | 42.6 ms: 1.03x faster                                                           |
| richards_super             | 50.3 ms                                                                | 49.0 ms: 1.03x faster                                                           |
| scimark_sor                | 119 ms                                                                 | 117 ms: 1.02x faster                                                            |
| deepcopy_memo              | 29.7 us                                                                | 29.1 us: 1.02x faster                                                           |
| pickle_pure_python         | 320 us                                                                 | 314 us: 1.02x faster                                                            |
| regex_v8                   | 23.9 ms                                                                | 23.5 ms: 1.02x faster                                                           |
| nbody                      | 97.3 ms                                                                | 95.7 ms: 1.02x faster                                                           |
| raytrace                   | 271 ms                                                                 | 266 ms: 1.02x faster                                                            |
| typing_runtime_protocols   | 163 us                                                                 | 160 us: 1.02x faster                                                            |
| async_tree_none_tg         | 251 ms                                                                 | 248 ms: 1.02x faster                                                            |
| sympy_expand               | 457 ms                                                                 | 450 ms: 1.01x faster                                                            |
| async_generators           | 397 ms                                                                 | 391 ms: 1.01x faster                                                            |
| pprint_safe_repr           | 738 ms                                                                 | 730 ms: 1.01x faster                                                            |
| xml_etree_process          | 58.7 ms                                                                | 58.0 ms: 1.01x faster                                                           |
| unpickle_pure_python       | 219 us                                                                 | 217 us: 1.01x faster                                                            |
| sympy_sum                  | 149 ms                                                                 | 147 ms: 1.01x faster                                                            |
| spectral_norm              | 99.3 ms                                                                | 98.4 ms: 1.01x faster                                                           |
| 2to3                       | 258 ms                                                                 | 256 ms: 1.01x faster                                                            |
| sympy_integrate            | 20.0 ms                                                                | 19.8 ms: 1.01x faster                                                           |
| sympy_str                  | 270 ms                                                                 | 267 ms: 1.01x faster                                                            |
| subparsers                 | 20.7 ms                                                                | 20.5 ms: 1.01x faster                                                           |
| go                         | 115 ms                                                                 | 114 ms: 1.01x faster                                                            |
| xml_etree_generate         | 84.0 ms                                                                | 83.3 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                                 | 485 ms: 1.01x faster                                                            |
| json_dumps                 | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                                           |
| mako                       | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                                           |
| coroutines                 | 23.6 ms                                                                | 23.4 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 471 ms: 1.01x faster                                                            |
| hexiom                     | 6.16 ms                                                                | 6.13 ms: 1.01x faster                                                           |
| async_tree_memoization     | 316 ms                                                                 | 315 ms: 1.01x faster                                                            |
| scimark_lu                 | 115 ms                                                                 | 114 ms: 1.01x faster                                                            |
| chaos                      | 60.0 ms                                                                | 59.7 ms: 1.00x faster                                                           |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                           |
| regex_compile              | 125 ms                                                                 | 125 ms: 1.00x faster                                                            |
| python_startup_no_site     | 8.20 ms                                                                | 8.19 ms: 1.00x faster                                                           |
| nqueens                    | 83.3 ms                                                                | 83.5 ms: 1.00x slower                                                           |
| deepcopy                   | 259 us                                                                 | 261 us: 1.00x slower                                                            |
| float                      | 69.7 ms                                                                | 70.0 ms: 1.01x slower                                                           |
| comprehensions             | 16.6 us                                                                | 16.7 us: 1.01x slower                                                           |
| json_loads                 | 30.0 us                                                                | 30.2 us: 1.01x slower                                                           |
| telco                      | 7.86 ms                                                                | 7.92 ms: 1.01x slower                                                           |
| sqlglot_v2_parse           | 1.26 ms                                                                | 1.27 ms: 1.01x slower                                                           |
| generators                 | 28.3 ms                                                                | 28.6 ms: 1.01x slower                                                           |
| create_gc_cycles           | 2.47 ms                                                                | 2.50 ms: 1.01x slower                                                           |
| fannkuch                   | 425 ms                                                                 | 430 ms: 1.01x slower                                                            |
| crypto_pyaes               | 75.5 ms                                                                | 76.4 ms: 1.01x slower                                                           |
| genshi_xml                 | 49.2 ms                                                                | 49.9 ms: 1.01x slower                                                           |
| pathlib                    | 16.5 ms                                                                | 16.8 ms: 1.01x slower                                                           |
| regex_effbot               | 3.48 ms                                                                | 3.53 ms: 1.01x slower                                                           |
| scimark_fft                | 348 ms                                                                 | 353 ms: 1.02x slower                                                            |
| genshi_text                | 21.4 ms                                                                | 21.8 ms: 1.02x slower                                                           |
| coverage                   | 90.9 ms                                                                | 93.2 ms: 1.02x slower                                                           |
| gc_traversal               | 4.78 ms                                                                | 4.92 ms: 1.03x slower                                                           |
| scimark_sparse_mat_mult    | 4.74 ms                                                                | 5.01 ms: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (39): async_tree_io, pycparser, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, pyflate, django_template, bench_mp_pool, asyncio_websockets, k_core, dulwich_log, scimark_monte_carlo, pprint_pformat, sqlglot_v2_normalize, many_optionals, pylint, mdp, sqlalchemy_declarative, thrift, sqlalchemy_imperative, sqlglot_v2_optimize, connected_components, bench_thread_pool, regex_dna, html5lib, xml_etree_iterparse, xml_etree_parse, shortest_path, docutils, bpe_tokeniser, sqlglot_v2_transpile, logging_simple, sphinx, logging_format, tomli_loads, deepcopy_reduce, sqlite_synth, json, meteor_contest

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x