# Results vs. base

- fork: kumaraditya303
- ref: experiment_gc_async
- machine: linux-x86_64
- commit hash: bd38cdb
- commit date: 2025-04-30
- overall geometric mean: 1.008x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 292 ms                                                                 | 291 ms: 1.00x faster                                                          |
| html5lib       | 67.6 ms                                                                | 67.2 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager_memoization     | 222 ms                                                                 | 217 ms: 1.02x faster                                                          |
| async_tree_eager                 | 129 ms                                                                 | 127 ms: 1.02x faster                                                          |
| async_tree_none                  | 266 ms                                                                 | 262 ms: 1.02x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 403 ms                                                                 | 398 ms: 1.01x faster                                                          |
| async_tree_none_tg               | 228 ms                                                                 | 225 ms: 1.01x faster                                                          |
| async_tree_eager_cpu_io_mixed_tg | 442 ms                                                                 | 437 ms: 1.01x faster                                                          |
| async_tree_eager_io              | 526 ms                                                                 | 521 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 459 ms                                                                 | 456 ms: 1.01x faster                                                          |
| coroutines                       | 24.9 ms                                                                | 25.0 ms: 1.00x slower                                                         |
| Geometric mean                   | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io, async_generators, async_tree_memoization, async_tree_eager_memoization_tg, asyncio_websockets, async_tree_eager_io_tg, async_tree_eager_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 70.9 ms                                                                | 70.3 ms: 1.01x faster                                                         |
| pidigits       | 181 ms                                                                 | 181 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 212 ms                                                                 | 206 ms: 1.03x faster                                                          |
| regex_v8       | 22.4 ms                                                                | 22.0 ms: 1.02x faster                                                         |
| regex_compile  | 145 ms                                                                 | 144 ms: 1.01x faster                                                          |
| regex_effbot   | 3.17 ms                                                                | 3.15 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 97.6 ms                                                                | 96.4 ms: 1.01x faster                                                         |
| xml_etree_parse      | 150 ms                                                                 | 148 ms: 1.01x faster                                                          |
| json_dumps           | 13.1 ms                                                                | 12.9 ms: 1.01x faster                                                         |
| unpickle_pure_python | 239 us                                                                 | 238 us: 1.00x faster                                                          |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (5): xml_etree_generate, tomli_loads, xml_etree_process, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 9.12 ms                                                                | 9.06 ms: 1.01x faster                                                         |
| python_startup         | 15.5 ms                                                                | 15.4 ms: 1.00x faster                                                         |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 59.5 ms                                                                | 57.8 ms: 1.03x faster                                                         |
| genshi_text     | 27.3 ms                                                                | 26.7 ms: 1.02x faster                                                         |
| django_template | 39.3 ms                                                                | 38.9 ms: 1.01x faster                                                         |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                        | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| gc_traversal                     | 2.29 ms                                                                | 2.14 ms: 1.07x faster                                                         |
| logging_silent                   | 110 ns                                                                 | 103 ns: 1.07x faster                                                          |
| scimark_sor                      | 137 ms                                                                 | 131 ms: 1.05x faster                                                          |
| pycparser                        | 1.15 sec                                                               | 1.10 sec: 1.04x faster                                                        |
| scimark_fft                      | 411 ms                                                                 | 395 ms: 1.04x faster                                                          |
| scimark_lu                       | 139 ms                                                                 | 134 ms: 1.04x faster                                                          |
| go                               | 133 ms                                                                 | 129 ms: 1.03x faster                                                          |
| regex_dna                        | 212 ms                                                                 | 206 ms: 1.03x faster                                                          |
| genshi_xml                       | 59.5 ms                                                                | 57.8 ms: 1.03x faster                                                         |
| pyflate                          | 503 ms                                                                 | 489 ms: 1.03x faster                                                          |
| deepcopy_reduce                  | 3.16 us                                                                | 3.09 us: 1.03x faster                                                         |
| async_tree_eager_memoization     | 222 ms                                                                 | 217 ms: 1.02x faster                                                          |
| genshi_text                      | 27.3 ms                                                                | 26.7 ms: 1.02x faster                                                         |
| meteor_contest                   | 132 ms                                                                 | 129 ms: 1.02x faster                                                          |
| regex_v8                         | 22.4 ms                                                                | 22.0 ms: 1.02x faster                                                         |
| create_gc_cycles                 | 1.69 ms                                                                | 1.65 ms: 1.02x faster                                                         |
| raytrace                         | 321 ms                                                                 | 316 ms: 1.02x faster                                                          |
| async_tree_eager                 | 129 ms                                                                 | 127 ms: 1.02x faster                                                          |
| deltablue                        | 3.70 ms                                                                | 3.65 ms: 1.02x faster                                                         |
| async_tree_none                  | 266 ms                                                                 | 262 ms: 1.02x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 403 ms                                                                 | 398 ms: 1.01x faster                                                          |
| sqlglot_v2_transpile             | 1.82 ms                                                                | 1.79 ms: 1.01x faster                                                         |
| deepcopy                         | 298 us                                                                 | 294 us: 1.01x faster                                                          |
| subparsers                       | 23.6 ms                                                                | 23.2 ms: 1.01x faster                                                         |
| xml_etree_iterparse              | 97.6 ms                                                                | 96.4 ms: 1.01x faster                                                         |
| async_tree_none_tg               | 228 ms                                                                 | 225 ms: 1.01x faster                                                          |
| sqlglot_v2_parse                 | 1.47 ms                                                                | 1.45 ms: 1.01x faster                                                         |
| richards_super                   | 60.0 ms                                                                | 59.3 ms: 1.01x faster                                                         |
| xml_etree_parse                  | 150 ms                                                                 | 148 ms: 1.01x faster                                                          |
| async_tree_eager_cpu_io_mixed_tg | 442 ms                                                                 | 437 ms: 1.01x faster                                                          |
| hexiom                           | 7.29 ms                                                                | 7.21 ms: 1.01x faster                                                         |
| django_template                  | 39.3 ms                                                                | 38.9 ms: 1.01x faster                                                         |
| json_dumps                       | 13.1 ms                                                                | 12.9 ms: 1.01x faster                                                         |
| deepcopy_memo                    | 36.4 us                                                                | 36.0 us: 1.01x faster                                                         |
| sqlglot_v2_optimize              | 59.1 ms                                                                | 58.5 ms: 1.01x faster                                                         |
| async_tree_eager_io              | 526 ms                                                                 | 521 ms: 1.01x faster                                                          |
| sqlglot_v2_normalize             | 116 ms                                                                 | 115 ms: 1.01x faster                                                          |
| telco                            | 9.08 ms                                                                | 9.00 ms: 1.01x faster                                                         |
| bench_thread_pool                | 3.27 ms                                                                | 3.24 ms: 1.01x faster                                                         |
| scimark_monte_carlo              | 82.8 ms                                                                | 82.0 ms: 1.01x faster                                                         |
| sympy_integrate                  | 22.3 ms                                                                | 22.1 ms: 1.01x faster                                                         |
| richards                         | 50.6 ms                                                                | 50.2 ms: 1.01x faster                                                         |
| float                            | 70.9 ms                                                                | 70.3 ms: 1.01x faster                                                         |
| regex_compile                    | 145 ms                                                                 | 144 ms: 1.01x faster                                                          |
| regex_effbot                     | 3.17 ms                                                                | 3.15 ms: 1.01x faster                                                         |
| spectral_norm                    | 119 ms                                                                 | 118 ms: 1.01x faster                                                          |
| k_core                           | 2.43 sec                                                               | 2.41 sec: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg       | 459 ms                                                                 | 456 ms: 1.01x faster                                                          |
| python_startup_no_site           | 9.12 ms                                                                | 9.06 ms: 1.01x faster                                                         |
| chaos                            | 67.7 ms                                                                | 67.3 ms: 1.01x faster                                                         |
| pprint_pformat                   | 1.67 sec                                                               | 1.66 sec: 1.01x faster                                                        |
| html5lib                         | 67.6 ms                                                                | 67.2 ms: 1.01x faster                                                         |
| unpickle_pure_python             | 239 us                                                                 | 238 us: 1.00x faster                                                          |
| python_startup                   | 15.5 ms                                                                | 15.4 ms: 1.00x faster                                                         |
| sympy_str                        | 305 ms                                                                 | 304 ms: 1.00x faster                                                          |
| pprint_safe_repr                 | 806 ms                                                                 | 803 ms: 1.00x faster                                                          |
| 2to3                             | 292 ms                                                                 | 291 ms: 1.00x faster                                                          |
| fannkuch                         | 503 ms                                                                 | 502 ms: 1.00x faster                                                          |
| pidigits                         | 181 ms                                                                 | 181 ms: 1.00x faster                                                          |
| nqueens                          | 91.7 ms                                                                | 91.9 ms: 1.00x slower                                                         |
| sqlalchemy_declarative           | 157 ms                                                                 | 158 ms: 1.00x slower                                                          |
| coroutines                       | 24.9 ms                                                                | 25.0 ms: 1.00x slower                                                         |
| many_optionals                   | 1.03 ms                                                                | 1.03 ms: 1.01x slower                                                         |
| mdp                              | 1.39 sec                                                               | 1.40 sec: 1.01x slower                                                        |
| bpe_tokeniser                    | 4.84 sec                                                               | 4.87 sec: 1.01x slower                                                        |
| shortest_path                    | 568 ms                                                                 | 572 ms: 1.01x slower                                                          |
| dulwich_log                      | 62.4 ms                                                                | 62.8 ms: 1.01x slower                                                         |
| connected_components             | 527 ms                                                                 | 532 ms: 1.01x slower                                                          |
| comprehensions                   | 19.7 us                                                                | 20.0 us: 1.01x slower                                                         |
| logging_simple                   | 6.58 us                                                                | 6.66 us: 1.01x slower                                                         |
| pathlib                          | 17.5 ms                                                                | 17.8 ms: 1.02x slower                                                         |
| logging_format                   | 7.38 us                                                                | 7.51 us: 1.02x slower                                                         |
| Geometric mean                   | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (31): json, sqlite_synth, async_tree_cpu_io_mixed, sympy_expand, async_tree_io_tg, docutils, xml_etree_generate, tomli_loads, crypto_pyaes, generators, pylint, xml_etree_process, sympy_sum, async_tree_io, bench_mp_pool, async_generators, sphinx, async_tree_memoization, async_tree_eager_memoization_tg, pickle_pure_python, asyncio_websockets, async_tree_eager_io_tg, json_loads, nbody, mako, typing_runtime_protocols, scimark_sparse_mat_mult, async_tree_eager_tg, coverage, sqlalchemy_imperative, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x