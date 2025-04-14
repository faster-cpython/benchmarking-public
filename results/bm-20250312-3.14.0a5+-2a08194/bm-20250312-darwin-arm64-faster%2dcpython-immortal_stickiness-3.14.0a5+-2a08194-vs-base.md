# Results vs. base

- fork: faster-cpython
- ref: immortal_stickiness
- machine: darwin-arm64
- commit hash: 2a08194
- commit date: 2025-03-12
- overall geometric mean: 1.003x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 173 ms                                                                 | 170 ms: 1.02x faster                                                            |
| docutils       | 1.50 sec                                                               | 1.49 sec: 1.01x faster                                                          |
| html5lib       | 31.9 ms                                                                | 32.3 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager                 | 67.2 ms                                                                | 65.4 ms: 1.03x faster                                                           |
| async_tree_memoization           | 213 ms                                                                 | 208 ms: 1.02x faster                                                            |
| coroutines                       | 17.6 ms                                                                | 17.3 ms: 1.02x faster                                                           |
| async_tree_eager_memoization     | 149 ms                                                                 | 147 ms: 1.02x faster                                                            |
| async_tree_none                  | 175 ms                                                                 | 172 ms: 1.02x faster                                                            |
| async_tree_eager_memoization_tg  | 185 ms                                                                 | 183 ms: 1.01x faster                                                            |
| async_tree_none_tg               | 166 ms                                                                 | 164 ms: 1.01x faster                                                            |
| async_tree_eager_io_tg           | 395 ms                                                                 | 391 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed          | 426 ms                                                                 | 422 ms: 1.01x faster                                                            |
| async_tree_io_tg                 | 388 ms                                                                 | 384 ms: 1.01x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 365 ms                                                                 | 362 ms: 1.01x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 400 ms                                                                 | 397 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 425 ms                                                                 | 423 ms: 1.00x faster                                                            |
| async_generators                 | 264 ms                                                                 | 264 ms: 1.00x faster                                                            |
| Geometric mean                   | (ref)                                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_eager_tg, async_tree_io, async_tree_eager_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 52.3 ms                                                                | 52.6 ms: 1.01x slower                                                           |
| nbody          | 80.3 ms                                                                | 81.0 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 76.4 ms                                                                | 75.3 ms: 1.01x faster                                                           |
| regex_dna      | 142 ms                                                                 | 141 ms: 1.00x faster                                                            |
| regex_effbot   | 2.27 ms                                                                | 2.27 ms: 1.00x slower                                                           |
| regex_v8       | 15.7 ms                                                                | 15.9 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 103 ms                                                                 | 99.8 ms: 1.04x faster                                                           |
| pickle_pure_python   | 228 us                                                                 | 221 us: 1.03x faster                                                            |
| xml_etree_generate   | 56.9 ms                                                                | 56.0 ms: 1.02x faster                                                           |
| xml_etree_process    | 41.3 ms                                                                | 40.9 ms: 1.01x faster                                                           |
| unpickle_pure_python | 166 us                                                                 | 164 us: 1.01x faster                                                            |
| json_dumps           | 7.54 ms                                                                | 7.50 ms: 1.01x faster                                                           |
| tomli_loads          | 1.32 sec                                                               | 1.40 sec: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 13.9 ms                                                                | 13.7 ms: 1.02x faster                                                           |
| python_startup         | 18.1 ms                                                                | 17.8 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 15.9 ms                                                                | 15.3 ms: 1.04x faster                                                           |
| genshi_xml      | 32.6 ms                                                                | 31.7 ms: 1.03x faster                                                           |
| mako            | 8.11 ms                                                                | 7.96 ms: 1.02x faster                                                           |
| django_template | 23.0 ms                                                                | 22.8 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                       | 27.8 ms                                                                | 24.9 ms: 1.12x faster                                                           |
| deepcopy_memo                    | 21.4 us                                                                | 20.4 us: 1.05x faster                                                           |
| genshi_text                      | 15.9 ms                                                                | 15.3 ms: 1.04x faster                                                           |
| deltablue                        | 2.76 ms                                                                | 2.65 ms: 1.04x faster                                                           |
| xml_etree_parse                  | 103 ms                                                                 | 99.8 ms: 1.04x faster                                                           |
| pickle_pure_python               | 228 us                                                                 | 221 us: 1.03x faster                                                            |
| async_tree_eager                 | 67.2 ms                                                                | 65.4 ms: 1.03x faster                                                           |
| sqlglot_v2_transpile             | 1.06 ms                                                                | 1.04 ms: 1.03x faster                                                           |
| sqlglot_v2_parse                 | 882 us                                                                 | 858 us: 1.03x faster                                                            |
| sqlglot_v2_normalize             | 71.8 ms                                                                | 69.9 ms: 1.03x faster                                                           |
| genshi_xml                       | 32.6 ms                                                                | 31.7 ms: 1.03x faster                                                           |
| pprint_safe_repr                 | 518 ms                                                                 | 506 ms: 1.02x faster                                                            |
| async_tree_memoization           | 213 ms                                                                 | 208 ms: 1.02x faster                                                            |
| go                               | 94.5 ms                                                                | 92.7 ms: 1.02x faster                                                           |
| hexiom                           | 5.06 ms                                                                | 4.96 ms: 1.02x faster                                                           |
| bench_thread_pool                | 514 us                                                                 | 504 us: 1.02x faster                                                            |
| mako                             | 8.11 ms                                                                | 7.96 ms: 1.02x faster                                                           |
| sympy_sum                        | 78.7 ms                                                                | 77.3 ms: 1.02x faster                                                           |
| python_startup_no_site           | 13.9 ms                                                                | 13.7 ms: 1.02x faster                                                           |
| 2to3                             | 173 ms                                                                 | 170 ms: 1.02x faster                                                            |
| xml_etree_generate               | 56.9 ms                                                                | 56.0 ms: 1.02x faster                                                           |
| json                             | 3.24 ms                                                                | 3.19 ms: 1.02x faster                                                           |
| subparsers                       | 12.9 ms                                                                | 12.7 ms: 1.02x faster                                                           |
| coroutines                       | 17.6 ms                                                                | 17.3 ms: 1.02x faster                                                           |
| async_tree_eager_memoization     | 149 ms                                                                 | 147 ms: 1.02x faster                                                            |
| async_tree_none                  | 175 ms                                                                 | 172 ms: 1.02x faster                                                            |
| regex_compile                    | 76.4 ms                                                                | 75.3 ms: 1.01x faster                                                           |
| python_startup                   | 18.1 ms                                                                | 17.8 ms: 1.01x faster                                                           |
| sympy_str                        | 150 ms                                                                 | 148 ms: 1.01x faster                                                            |
| sympy_expand                     | 251 ms                                                                 | 248 ms: 1.01x faster                                                            |
| async_tree_eager_memoization_tg  | 185 ms                                                                 | 183 ms: 1.01x faster                                                            |
| async_tree_none_tg               | 166 ms                                                                 | 164 ms: 1.01x faster                                                            |
| pprint_pformat                   | 1.04 sec                                                               | 1.03 sec: 1.01x faster                                                          |
| async_tree_eager_io_tg           | 395 ms                                                                 | 391 ms: 1.01x faster                                                            |
| deepcopy_reduce                  | 1.72 us                                                                | 1.70 us: 1.01x faster                                                           |
| pathlib                          | 23.8 ms                                                                | 23.5 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed          | 426 ms                                                                 | 422 ms: 1.01x faster                                                            |
| mdp                              | 1.54 sec                                                               | 1.53 sec: 1.01x faster                                                          |
| sqlalchemy_declarative           | 61.6 ms                                                                | 61.0 ms: 1.01x faster                                                           |
| typing_runtime_protocols         | 101 us                                                                 | 100.0 us: 1.01x faster                                                          |
| async_tree_io_tg                 | 388 ms                                                                 | 384 ms: 1.01x faster                                                            |
| xml_etree_process                | 41.3 ms                                                                | 40.9 ms: 1.01x faster                                                           |
| sqlglot_v2_optimize              | 35.0 ms                                                                | 34.6 ms: 1.01x faster                                                           |
| scimark_monte_carlo              | 47.5 ms                                                                | 47.1 ms: 1.01x faster                                                           |
| docutils                         | 1.50 sec                                                               | 1.49 sec: 1.01x faster                                                          |
| bench_mp_pool                    | 61.4 ms                                                                | 60.9 ms: 1.01x faster                                                           |
| unpickle_pure_python             | 166 us                                                                 | 164 us: 1.01x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 365 ms                                                                 | 362 ms: 1.01x faster                                                            |
| deepcopy                         | 166 us                                                                 | 164 us: 1.01x faster                                                            |
| many_optionals                   | 469 us                                                                 | 465 us: 1.01x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 400 ms                                                                 | 397 ms: 1.01x faster                                                            |
| django_template                  | 23.0 ms                                                                | 22.8 ms: 1.01x faster                                                           |
| create_gc_cycles                 | 1.30 ms                                                                | 1.29 ms: 1.01x faster                                                           |
| comprehensions                   | 13.0 us                                                                | 12.9 us: 1.01x faster                                                           |
| json_dumps                       | 7.54 ms                                                                | 7.50 ms: 1.01x faster                                                           |
| thrift                           | 462 us                                                                 | 459 us: 1.00x faster                                                            |
| sympy_integrate                  | 12.1 ms                                                                | 12.1 ms: 1.00x faster                                                           |
| regex_dna                        | 142 ms                                                                 | 141 ms: 1.00x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 425 ms                                                                 | 423 ms: 1.00x faster                                                            |
| sqlite_synth                     | 1.54 us                                                                | 1.53 us: 1.00x faster                                                           |
| async_generators                 | 264 ms                                                                 | 264 ms: 1.00x faster                                                            |
| scimark_sparse_mat_mult          | 3.10 ms                                                                | 3.09 ms: 1.00x faster                                                           |
| dulwich_log                      | 25.6 ms                                                                | 25.6 ms: 1.00x faster                                                           |
| logging_silent                   | 73.1 ns                                                                | 73.3 ns: 1.00x slower                                                           |
| regex_effbot                     | 2.27 ms                                                                | 2.27 ms: 1.00x slower                                                           |
| logging_simple                   | 3.60 us                                                                | 3.62 us: 1.00x slower                                                           |
| scimark_fft                      | 192 ms                                                                 | 193 ms: 1.01x slower                                                            |
| float                            | 52.3 ms                                                                | 52.6 ms: 1.01x slower                                                           |
| scimark_sor                      | 87.8 ms                                                                | 88.3 ms: 1.01x slower                                                           |
| scimark_lu                       | 78.6 ms                                                                | 79.2 ms: 1.01x slower                                                           |
| nbody                            | 80.3 ms                                                                | 81.0 ms: 1.01x slower                                                           |
| shortest_path                    | 339 ms                                                                 | 343 ms: 1.01x slower                                                            |
| telco                            | 4.63 ms                                                                | 4.68 ms: 1.01x slower                                                           |
| meteor_contest                   | 75.5 ms                                                                | 76.4 ms: 1.01x slower                                                           |
| html5lib                         | 31.9 ms                                                                | 32.3 ms: 1.01x slower                                                           |
| regex_v8                         | 15.7 ms                                                                | 15.9 ms: 1.01x slower                                                           |
| chaos                            | 43.9 ms                                                                | 44.5 ms: 1.01x slower                                                           |
| raytrace                         | 189 ms                                                                 | 192 ms: 1.02x slower                                                            |
| connected_components             | 312 ms                                                                 | 317 ms: 1.02x slower                                                            |
| crypto_pyaes                     | 59.7 ms                                                                | 60.9 ms: 1.02x slower                                                           |
| nqueens                          | 66.5 ms                                                                | 68.8 ms: 1.03x slower                                                           |
| bpe_tokeniser                    | 3.19 sec                                                               | 3.30 sec: 1.03x slower                                                          |
| richards_super                   | 40.3 ms                                                                | 41.7 ms: 1.04x slower                                                           |
| fannkuch                         | 295 ms                                                                 | 308 ms: 1.05x slower                                                            |
| tomli_loads                      | 1.32 sec                                                               | 1.40 sec: 1.06x slower                                                          |
| richards                         | 35.0 ms                                                                | 37.2 ms: 1.06x slower                                                           |
| pyflate                          | 326 ms                                                                 | 351 ms: 1.08x slower                                                            |
| spectral_norm                    | 70.3 ms                                                                | 79.9 ms: 1.14x slower                                                           |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (17): async_tree_memoization_tg, async_tree_eager_tg, pycparser, sphinx, async_tree_io, async_tree_eager_io, sqlalchemy_imperative, xml_etree_iterparse, asyncio_websockets, json_loads, dask, pidigits, coverage, logging_format, pylint, gc_traversal, k_core

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x