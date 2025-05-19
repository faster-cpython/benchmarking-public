# Results vs. base

- fork: faster-cpython
- ref: make_decref_a_call
- machine: darwin-arm64
- commit hash: 4fee8de
- commit date: 2025-05-19
- overall geometric mean: 1.065x faster
- HPT reliability: 96.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 193 ms                                                                | 190 ms: 1.02x faster                                                          |
| docutils       | 1.57 sec                                                              | 1.57 sec: 1.00x slower                                                        |
| html5lib       | 35.2 ms                                                               | 34.8 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager_memoization     | 155 ms                                                                | 154 ms: 1.01x faster                                                          |
| async_tree_eager                 | 77.6 ms                                                               | 77.0 ms: 1.01x faster                                                         |
| asyncio_websockets               | 242 ms                                                                | 243 ms: 1.00x slower                                                          |
| async_tree_cpu_io_mixed_tg       | 426 ms                                                                | 429 ms: 1.01x slower                                                          |
| async_tree_cpu_io_mixed          | 440 ms                                                                | 442 ms: 1.01x slower                                                          |
| async_tree_eager_cpu_io_mixed    | 372 ms                                                                | 374 ms: 1.01x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 401 ms                                                                | 405 ms: 1.01x slower                                                          |
| async_tree_none                  | 186 ms                                                                | 188 ms: 1.01x slower                                                          |
| coroutines                       | 19.7 ms                                                               | 20.3 ms: 1.03x slower                                                         |
| async_generators                 | 274 ms                                                                | 292 ms: 1.06x slower                                                          |
| Geometric mean                   | (ref)                                                                 | 1.01x slower                                                                  |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_io, async_tree_eager_io, async_tree_none_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_eager_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 91.7 ms                                                               | 89.0 ms: 1.03x faster                                                         |
| pidigits       | 283 ms                                                                | 284 ms: 1.00x slower                                                          |
| float          | 58.9 ms                                                               | 59.4 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 86.7 ms                                                               | 84.4 ms: 1.03x faster                                                         |
| regex_dna      | 137 ms                                                                | 138 ms: 1.00x slower                                                          |
| regex_v8       | 15.8 ms                                                               | 15.8 ms: 1.01x slower                                                         |
| regex_effbot   | 2.16 ms                                                               | 2.18 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                                | 179 us: 1.06x faster                                                          |
| tomli_loads          | 1.52 sec                                                              | 1.49 sec: 1.02x faster                                                        |
| pickle_pure_python   | 250 us                                                                | 244 us: 1.02x faster                                                          |
| xml_etree_process    | 45.8 ms                                                               | 46.2 ms: 1.01x slower                                                         |
| json_loads           | 18.3 us                                                               | 18.5 us: 1.02x slower                                                         |
| xml_etree_generate   | 61.4 ms                                                               | 62.9 ms: 1.02x slower                                                         |
| json_dumps           | 7.16 ms                                                               | 7.38 ms: 1.03x slower                                                         |
| xml_etree_parse      | 105 ms                                                                | 108 ms: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                               | 8.74 ms: 1.04x faster                                                         |
| django_template | 26.6 ms                                                               | 26.2 ms: 1.02x faster                                                         |
| genshi_text     | 18.6 ms                                                               | 18.4 ms: 1.01x faster                                                         |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                                  |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                           | 43.9 ms                                                               | 505 us: 87.05x faster                                                         |
| coverage                         | 332 ms                                                                | 54.0 ms: 6.16x faster                                                         |
| dask                             | 860 ms                                                                | 772 ms: 1.11x faster                                                          |
| unpickle_pure_python             | 189 us                                                                | 179 us: 1.06x faster                                                          |
| deepcopy_memo                    | 23.8 us                                                               | 22.5 us: 1.06x faster                                                         |
| hexiom                           | 5.47 ms                                                               | 5.18 ms: 1.06x faster                                                         |
| richards                         | 39.4 ms                                                               | 37.4 ms: 1.05x faster                                                         |
| go                               | 105 ms                                                                | 100 ms: 1.05x faster                                                          |
| richards_super                   | 44.0 ms                                                               | 42.2 ms: 1.04x faster                                                         |
| mako                             | 9.10 ms                                                               | 8.74 ms: 1.04x faster                                                         |
| scimark_sor                      | 94.8 ms                                                               | 91.3 ms: 1.04x faster                                                         |
| pprint_safe_repr                 | 588 ms                                                                | 570 ms: 1.03x faster                                                          |
| nbody                            | 91.7 ms                                                               | 89.0 ms: 1.03x faster                                                         |
| scimark_monte_carlo              | 53.8 ms                                                               | 52.3 ms: 1.03x faster                                                         |
| nqueens                          | 75.7 ms                                                               | 73.7 ms: 1.03x faster                                                         |
| regex_compile                    | 86.7 ms                                                               | 84.4 ms: 1.03x faster                                                         |
| deltablue                        | 2.86 ms                                                               | 2.79 ms: 1.03x faster                                                         |
| tomli_loads                      | 1.52 sec                                                              | 1.49 sec: 1.02x faster                                                        |
| pickle_pure_python               | 250 us                                                                | 244 us: 1.02x faster                                                          |
| pprint_pformat                   | 1.19 sec                                                              | 1.17 sec: 1.02x faster                                                        |
| comprehensions                   | 14.6 us                                                               | 14.2 us: 1.02x faster                                                         |
| pycparser                        | 766 ms                                                                | 752 ms: 1.02x faster                                                          |
| 2to3                             | 193 ms                                                                | 190 ms: 1.02x faster                                                          |
| django_template                  | 26.6 ms                                                               | 26.2 ms: 1.02x faster                                                         |
| dulwich_log                      | 27.4 ms                                                               | 27.1 ms: 1.01x faster                                                         |
| sqlglot_v2_transpile             | 1.18 ms                                                               | 1.16 ms: 1.01x faster                                                         |
| html5lib                         | 35.2 ms                                                               | 34.8 ms: 1.01x faster                                                         |
| genshi_text                      | 18.6 ms                                                               | 18.4 ms: 1.01x faster                                                         |
| bench_thread_pool                | 544 us                                                                | 539 us: 1.01x faster                                                          |
| async_tree_eager_memoization     | 155 ms                                                                | 154 ms: 1.01x faster                                                          |
| many_optionals                   | 512 us                                                                | 508 us: 1.01x faster                                                          |
| deepcopy                         | 187 us                                                                | 185 us: 1.01x faster                                                          |
| sqlglot_v2_parse                 | 982 us                                                                | 974 us: 1.01x faster                                                          |
| async_tree_eager                 | 77.6 ms                                                               | 77.0 ms: 1.01x faster                                                         |
| create_gc_cycles                 | 1.37 ms                                                               | 1.36 ms: 1.01x faster                                                         |
| generators                       | 31.5 ms                                                               | 31.4 ms: 1.00x faster                                                         |
| gc_traversal                     | 3.22 ms                                                               | 3.22 ms: 1.00x faster                                                         |
| pidigits                         | 283 ms                                                                | 284 ms: 1.00x slower                                                          |
| asyncio_websockets               | 242 ms                                                                | 243 ms: 1.00x slower                                                          |
| sympy_integrate                  | 11.6 ms                                                               | 11.6 ms: 1.00x slower                                                         |
| docutils                         | 1.57 sec                                                              | 1.57 sec: 1.00x slower                                                        |
| regex_dna                        | 137 ms                                                                | 138 ms: 1.00x slower                                                          |
| chaos                            | 46.9 ms                                                               | 47.1 ms: 1.00x slower                                                         |
| regex_v8                         | 15.8 ms                                                               | 15.8 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed_tg       | 426 ms                                                                | 429 ms: 1.01x slower                                                          |
| regex_effbot                     | 2.16 ms                                                               | 2.18 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed          | 440 ms                                                                | 442 ms: 1.01x slower                                                          |
| async_tree_eager_cpu_io_mixed    | 372 ms                                                                | 374 ms: 1.01x slower                                                          |
| float                            | 58.9 ms                                                               | 59.4 ms: 1.01x slower                                                         |
| connected_components             | 313 ms                                                                | 316 ms: 1.01x slower                                                          |
| xml_etree_process                | 45.8 ms                                                               | 46.2 ms: 1.01x slower                                                         |
| pathlib                          | 24.2 ms                                                               | 24.4 ms: 1.01x slower                                                         |
| logging_format                   | 4.54 us                                                               | 4.58 us: 1.01x slower                                                         |
| logging_simple                   | 4.22 us                                                               | 4.26 us: 1.01x slower                                                         |
| shortest_path                    | 341 ms                                                                | 344 ms: 1.01x slower                                                          |
| subparsers                       | 15.2 ms                                                               | 15.4 ms: 1.01x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 401 ms                                                                | 405 ms: 1.01x slower                                                          |
| spectral_norm                    | 78.5 ms                                                               | 79.4 ms: 1.01x slower                                                         |
| async_tree_none                  | 186 ms                                                                | 188 ms: 1.01x slower                                                          |
| mdp                              | 867 ms                                                                | 879 ms: 1.01x slower                                                          |
| typing_runtime_protocols         | 112 us                                                                | 114 us: 1.01x slower                                                          |
| json_loads                       | 18.3 us                                                               | 18.5 us: 1.02x slower                                                         |
| sympy_sum                        | 82.8 ms                                                               | 84.2 ms: 1.02x slower                                                         |
| sympy_str                        | 160 ms                                                                | 162 ms: 1.02x slower                                                          |
| sqlglot_v2_normalize             | 78.9 ms                                                               | 80.4 ms: 1.02x slower                                                         |
| crypto_pyaes                     | 61.4 ms                                                               | 62.7 ms: 1.02x slower                                                         |
| sympy_expand                     | 271 ms                                                                | 277 ms: 1.02x slower                                                          |
| xml_etree_generate               | 61.4 ms                                                               | 62.9 ms: 1.02x slower                                                         |
| scimark_lu                       | 86.3 ms                                                               | 88.6 ms: 1.03x slower                                                         |
| coroutines                       | 19.7 ms                                                               | 20.3 ms: 1.03x slower                                                         |
| json_dumps                       | 7.16 ms                                                               | 7.38 ms: 1.03x slower                                                         |
| sqlglot_v2_optimize              | 37.8 ms                                                               | 39.0 ms: 1.03x slower                                                         |
| xml_etree_parse                  | 105 ms                                                                | 108 ms: 1.03x slower                                                          |
| scimark_sparse_mat_mult          | 3.24 ms                                                               | 3.35 ms: 1.03x slower                                                         |
| scimark_fft                      | 209 ms                                                                | 218 ms: 1.04x slower                                                          |
| sqlite_synth                     | 1.59 us                                                               | 1.66 us: 1.04x slower                                                         |
| logging_silent                   | 344 ns                                                                | 359 ns: 1.04x slower                                                          |
| bpe_tokeniser                    | 3.31 sec                                                              | 3.47 sec: 1.05x slower                                                        |
| pyflate                          | 350 ms                                                                | 369 ms: 1.06x slower                                                          |
| fannkuch                         | 301 ms                                                                | 320 ms: 1.06x slower                                                          |
| async_generators                 | 274 ms                                                                | 292 ms: 1.06x slower                                                          |
| meteor_contest                   | 77.8 ms                                                               | 82.8 ms: 1.06x slower                                                         |
| telco                            | 4.82 ms                                                               | 5.19 ms: 1.08x slower                                                         |
| Geometric mean                   | (ref)                                                                 | 1.06x faster                                                                  |

Benchmark hidden because not significant (20): sphinx, deepcopy_reduce, python_startup, python_startup_no_site, xml_etree_iterparse, async_tree_memoization, json, k_core, raytrace, genshi_xml, pylint, async_tree_io, async_tree_eager_io, async_tree_none_tg, bench_mp_pool, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_eager_tg

- Geometric mean (including insignificant results): 1.065x faster

# HPT report

- Reliability score: 96.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x