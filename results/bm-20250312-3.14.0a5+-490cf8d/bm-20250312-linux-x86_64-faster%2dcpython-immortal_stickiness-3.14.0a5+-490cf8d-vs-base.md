# Results vs. base

- fork: faster-cpython
- ref: immortal_stickiness
- machine: linux-x86_64
- commit hash: 490cf8d
- commit date: 2025-03-12
- overall geometric mean: 1.007x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                 | 257 ms: 1.01x slower                                                            |
| html5lib       | 62.0 ms                                                                | 61.3 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_generators           | 395 ms                                                                 | 391 ms: 1.01x faster                                                            |
| async_tree_memoization     | 314 ms                                                                 | 316 ms: 1.01x slower                                                            |
| coroutines                 | 23.1 ms                                                                | 23.5 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed    | 487 ms                                                                 | 496 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 481 ms: 1.02x slower                                                            |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (6): async_tree_io_tg, asyncio_websockets, async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 194 ms                                                                 | 186 ms: 1.04x faster                                                            |
| float          | 69.3 ms                                                                | 71.0 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                                | 24.0 ms: 1.00x slower                                                           |
| regex_compile  | 125 ms                                                                 | 126 ms: 1.01x slower                                                            |
| regex_dna      | 214 ms                                                                 | 227 ms: 1.06x slower                                                            |
| regex_effbot   | 3.22 ms                                                                | 3.56 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 98.7 ms                                                                | 98.0 ms: 1.01x faster                                                           |
| xml_etree_generate   | 83.8 ms                                                                | 84.1 ms: 1.00x slower                                                           |
| unpickle_pure_python | 215 us                                                                 | 217 us: 1.01x slower                                                            |
| xml_etree_process    | 58.2 ms                                                                | 58.7 ms: 1.01x slower                                                           |
| json_loads           | 29.9 us                                                                | 30.2 us: 1.01x slower                                                           |
| pickle_pure_python   | 315 us                                                                 | 318 us: 1.01x slower                                                            |
| json_dumps           | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                                           |
| tomli_loads          | 1.94 sec                                                               | 1.98 sec: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.22 ms                                                                | 8.18 ms: 1.00x faster                                                           |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.4 ms                                                                | 11.4 ms: 1.01x faster                                                           |
| django_template | 31.8 ms                                                                | 31.9 ms: 1.00x slower                                                           |
| genshi_text     | 21.5 ms                                                                | 21.8 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pyflate                    | 462 ms                                                                 | 436 ms: 1.06x faster                                                            |
| pidigits                   | 194 ms                                                                 | 186 ms: 1.04x faster                                                            |
| fannkuch                   | 427 ms                                                                 | 422 ms: 1.01x faster                                                            |
| async_generators           | 395 ms                                                                 | 391 ms: 1.01x faster                                                            |
| html5lib                   | 62.0 ms                                                                | 61.3 ms: 1.01x faster                                                           |
| bpe_tokeniser              | 4.60 sec                                                               | 4.56 sec: 1.01x faster                                                          |
| comprehensions             | 16.7 us                                                                | 16.6 us: 1.01x faster                                                           |
| sympy_expand               | 456 ms                                                                 | 452 ms: 1.01x faster                                                            |
| xml_etree_iterparse        | 98.7 ms                                                                | 98.0 ms: 1.01x faster                                                           |
| sqlite_synth               | 2.80 us                                                                | 2.79 us: 1.01x faster                                                           |
| mako                       | 11.4 ms                                                                | 11.4 ms: 1.01x faster                                                           |
| python_startup_no_site     | 8.22 ms                                                                | 8.18 ms: 1.00x faster                                                           |
| mdp                        | 2.49 sec                                                               | 2.48 sec: 1.00x faster                                                          |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                           |
| create_gc_cycles           | 2.48 ms                                                                | 2.48 ms: 1.00x slower                                                           |
| sympy_integrate            | 19.8 ms                                                                | 19.9 ms: 1.00x slower                                                           |
| xml_etree_generate         | 83.8 ms                                                                | 84.1 ms: 1.00x slower                                                           |
| django_template            | 31.8 ms                                                                | 31.9 ms: 1.00x slower                                                           |
| nqueens                    | 83.1 ms                                                                | 83.5 ms: 1.00x slower                                                           |
| regex_v8                   | 23.9 ms                                                                | 24.0 ms: 1.00x slower                                                           |
| sqlalchemy_declarative     | 130 ms                                                                 | 130 ms: 1.01x slower                                                            |
| 2to3                       | 255 ms                                                                 | 257 ms: 1.01x slower                                                            |
| go                         | 114 ms                                                                 | 115 ms: 1.01x slower                                                            |
| async_tree_memoization     | 314 ms                                                                 | 316 ms: 1.01x slower                                                            |
| unpickle_pure_python       | 215 us                                                                 | 217 us: 1.01x slower                                                            |
| xml_etree_process          | 58.2 ms                                                                | 58.7 ms: 1.01x slower                                                           |
| deepcopy_reduce            | 2.73 us                                                                | 2.75 us: 1.01x slower                                                           |
| crypto_pyaes               | 75.7 ms                                                                | 76.3 ms: 1.01x slower                                                           |
| bench_thread_pool          | 866 us                                                                 | 873 us: 1.01x slower                                                            |
| dulwich_log                | 57.9 ms                                                                | 58.4 ms: 1.01x slower                                                           |
| raytrace                   | 268 ms                                                                 | 271 ms: 1.01x slower                                                            |
| json_loads                 | 29.9 us                                                                | 30.2 us: 1.01x slower                                                           |
| pickle_pure_python         | 315 us                                                                 | 318 us: 1.01x slower                                                            |
| meteor_contest             | 106 ms                                                                 | 107 ms: 1.01x slower                                                            |
| hexiom                     | 6.08 ms                                                                | 6.15 ms: 1.01x slower                                                           |
| typing_runtime_protocols   | 161 us                                                                 | 163 us: 1.01x slower                                                            |
| genshi_text                | 21.5 ms                                                                | 21.8 ms: 1.01x slower                                                           |
| regex_compile              | 125 ms                                                                 | 126 ms: 1.01x slower                                                            |
| json_dumps                 | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                                           |
| sqlalchemy_imperative      | 16.4 ms                                                                | 16.6 ms: 1.01x slower                                                           |
| scimark_sor                | 117 ms                                                                 | 118 ms: 1.01x slower                                                            |
| json                       | 5.25 ms                                                                | 5.32 ms: 1.01x slower                                                           |
| scimark_sparse_mat_mult    | 4.84 ms                                                                | 4.90 ms: 1.01x slower                                                           |
| pprint_safe_repr           | 737 ms                                                                 | 746 ms: 1.01x slower                                                            |
| scimark_monte_carlo        | 68.0 ms                                                                | 68.8 ms: 1.01x slower                                                           |
| chaos                      | 59.5 ms                                                                | 60.3 ms: 1.01x slower                                                           |
| many_optionals             | 931 us                                                                 | 945 us: 1.01x slower                                                            |
| scimark_fft                | 347 ms                                                                 | 352 ms: 1.02x slower                                                            |
| logging_simple             | 5.49 us                                                                | 5.58 us: 1.02x slower                                                           |
| coroutines                 | 23.1 ms                                                                | 23.5 ms: 1.02x slower                                                           |
| spectral_norm              | 98.0 ms                                                                | 99.8 ms: 1.02x slower                                                           |
| logging_format             | 6.05 us                                                                | 6.16 us: 1.02x slower                                                           |
| deltablue                  | 3.09 ms                                                                | 3.15 ms: 1.02x slower                                                           |
| deepcopy                   | 258 us                                                                 | 262 us: 1.02x slower                                                            |
| async_tree_cpu_io_mixed    | 487 ms                                                                 | 496 ms: 1.02x slower                                                            |
| pprint_pformat             | 1.49 sec                                                               | 1.52 sec: 1.02x slower                                                          |
| sqlglot_v2_parse           | 1.25 ms                                                                | 1.28 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 481 ms: 1.02x slower                                                            |
| subparsers                 | 20.3 ms                                                                | 20.7 ms: 1.02x slower                                                           |
| richards_super             | 49.5 ms                                                                | 50.6 ms: 1.02x slower                                                           |
| sqlglot_v2_transpile       | 1.56 ms                                                                | 1.59 ms: 1.02x slower                                                           |
| tomli_loads                | 1.94 sec                                                               | 1.98 sec: 1.02x slower                                                          |
| float                      | 69.3 ms                                                                | 71.0 ms: 1.02x slower                                                           |
| richards                   | 43.0 ms                                                                | 44.1 ms: 1.03x slower                                                           |
| pycparser                  | 1.13 sec                                                               | 1.18 sec: 1.04x slower                                                          |
| regex_dna                  | 214 ms                                                                 | 227 ms: 1.06x slower                                                            |
| logging_silent             | 93.9 ns                                                                | 99.9 ns: 1.06x slower                                                           |
| gc_traversal               | 4.62 ms                                                                | 5.02 ms: 1.09x slower                                                           |
| regex_effbot               | 3.22 ms                                                                | 3.56 ms: 1.10x slower                                                           |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (27): telco, shortest_path, generators, sqlglot_v2_normalize, sympy_sum, thrift, nbody, sympy_str, coverage, pathlib, async_tree_io_tg, genshi_xml, connected_components, docutils, k_core, sqlglot_v2_optimize, deepcopy_memo, bench_mp_pool, asyncio_websockets, async_tree_none_tg, pylint, xml_etree_parse, async_tree_memoization_tg, scimark_lu, async_tree_io, async_tree_none, sphinx

- Geometric mean (including insignificant results): 1.007x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x