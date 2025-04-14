# Results vs. base

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-x86_64
- commit hash: 553888a
- commit date: 2025-03-07
- overall geometric mean: 1.002x slower
- HPT reliability: 82.52%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250306-linux-x86_64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| html5lib       | 62.0 ms                                                                | 60.7 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250306-linux-x86_64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_generators           | 403 ms                                                                 | 391 ms: 1.03x faster                                                             |
| async_tree_cpu_io_mixed_tg | 483 ms                                                                 | 477 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed    | 494 ms                                                                 | 488 ms: 1.01x faster                                                             |
| coroutines                 | 23.6 ms                                                                | 23.5 ms: 1.01x faster                                                            |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_memoization, async_tree_none_tg, async_tree_none, asyncio_websockets, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250306-linux-x86_64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 87.4 ms                                                                | 88.9 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250306-linux-x86_64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 25.5 ms                                                                | 24.6 ms: 1.03x faster                                                            |
| regex_effbot   | 3.47 ms                                                                | 3.36 ms: 1.03x faster                                                            |
| regex_dna      | 223 ms                                                                 | 217 ms: 1.03x faster                                                             |
| regex_compile  | 129 ms                                                                 | 128 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250306-linux-x86_64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 323 us                                                                 | 320 us: 1.01x faster                                                             |
| xml_etree_process    | 54.9 ms                                                                | 55.2 ms: 1.00x slower                                                            |
| json_dumps           | 11.3 ms                                                                | 11.3 ms: 1.01x slower                                                            |
| xml_etree_parse      | 146 ms                                                                 | 147 ms: 1.01x slower                                                             |
| unpickle_pure_python | 204 us                                                                 | 206 us: 1.01x slower                                                             |
| xml_etree_iterparse  | 99.0 ms                                                                | 101 ms: 1.02x slower                                                             |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (3): tomli_loads, json_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250306-linux-x86_64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                | 13.1 ms: 1.01x slower                                                            |
| python_startup_no_site | 8.12 ms                                                                | 8.19 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250306-linux-x86_64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 10.2 ms                                                                | 10.2 ms: 1.00x faster                                                            |
| genshi_text     | 21.8 ms                                                                | 21.9 ms: 1.01x slower                                                            |
| django_template | 31.8 ms                                                                | 32.1 ms: 1.01x slower                                                            |
| genshi_xml      | 49.4 ms                                                                | 50.1 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20250306-linux-x86_64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| comprehensions             | 17.9 us                                                                | 17.3 us: 1.04x faster                                                            |
| regex_v8                   | 25.5 ms                                                                | 24.6 ms: 1.03x faster                                                            |
| regex_effbot               | 3.47 ms                                                                | 3.36 ms: 1.03x faster                                                            |
| async_generators           | 403 ms                                                                 | 391 ms: 1.03x faster                                                             |
| logging_format             | 6.21 us                                                                | 6.04 us: 1.03x faster                                                            |
| regex_dna                  | 223 ms                                                                 | 217 ms: 1.03x faster                                                             |
| typing_runtime_protocols   | 166 us                                                                 | 161 us: 1.03x faster                                                             |
| logging_simple             | 5.62 us                                                                | 5.48 us: 1.02x faster                                                            |
| html5lib                   | 62.0 ms                                                                | 60.7 ms: 1.02x faster                                                            |
| scimark_lu                 | 118 ms                                                                 | 116 ms: 1.02x faster                                                             |
| deepcopy_reduce            | 2.71 us                                                                | 2.66 us: 1.02x faster                                                            |
| connected_components       | 443 ms                                                                 | 436 ms: 1.02x faster                                                             |
| async_tree_cpu_io_mixed_tg | 483 ms                                                                 | 477 ms: 1.01x faster                                                             |
| regex_compile              | 129 ms                                                                 | 128 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed    | 494 ms                                                                 | 488 ms: 1.01x faster                                                             |
| pickle_pure_python         | 323 us                                                                 | 320 us: 1.01x faster                                                             |
| shortest_path              | 476 ms                                                                 | 472 ms: 1.01x faster                                                             |
| sympy_str                  | 274 ms                                                                 | 272 ms: 1.01x faster                                                             |
| sympy_expand               | 468 ms                                                                 | 464 ms: 1.01x faster                                                             |
| thrift                     | 754 us                                                                 | 747 us: 1.01x faster                                                             |
| dulwich_log                | 67.2 ms                                                                | 66.8 ms: 1.01x faster                                                            |
| coroutines                 | 23.6 ms                                                                | 23.5 ms: 1.01x faster                                                            |
| scimark_fft                | 315 ms                                                                 | 313 ms: 1.00x faster                                                             |
| bpe_tokeniser              | 4.46 sec                                                               | 4.44 sec: 1.00x faster                                                           |
| mako                       | 10.2 ms                                                                | 10.2 ms: 1.00x faster                                                            |
| spectral_norm              | 98.0 ms                                                                | 97.8 ms: 1.00x faster                                                            |
| bench_thread_pool          | 877 us                                                                 | 878 us: 1.00x slower                                                             |
| meteor_contest             | 108 ms                                                                 | 108 ms: 1.00x slower                                                             |
| deepcopy                   | 259 us                                                                 | 260 us: 1.00x slower                                                             |
| xml_etree_process          | 54.9 ms                                                                | 55.2 ms: 1.00x slower                                                            |
| genshi_text                | 21.8 ms                                                                | 21.9 ms: 1.01x slower                                                            |
| sympy_sum                  | 150 ms                                                                 | 151 ms: 1.01x slower                                                             |
| json_dumps                 | 11.3 ms                                                                | 11.3 ms: 1.01x slower                                                            |
| create_gc_cycles           | 2.45 ms                                                                | 2.46 ms: 1.01x slower                                                            |
| python_startup             | 13.0 ms                                                                | 13.1 ms: 1.01x slower                                                            |
| subparsers                 | 20.8 ms                                                                | 20.9 ms: 1.01x slower                                                            |
| xml_etree_parse            | 146 ms                                                                 | 147 ms: 1.01x slower                                                             |
| python_startup_no_site     | 8.12 ms                                                                | 8.19 ms: 1.01x slower                                                            |
| sqlalchemy_declarative     | 130 ms                                                                 | 132 ms: 1.01x slower                                                             |
| bench_mp_pool              | 81.6 ms                                                                | 82.4 ms: 1.01x slower                                                            |
| unpickle_pure_python       | 204 us                                                                 | 206 us: 1.01x slower                                                             |
| hexiom                     | 6.29 ms                                                                | 6.36 ms: 1.01x slower                                                            |
| django_template            | 31.8 ms                                                                | 32.1 ms: 1.01x slower                                                            |
| telco                      | 7.64 ms                                                                | 7.74 ms: 1.01x slower                                                            |
| generators                 | 27.8 ms                                                                | 28.2 ms: 1.01x slower                                                            |
| raytrace                   | 273 ms                                                                 | 277 ms: 1.01x slower                                                             |
| fannkuch                   | 400 ms                                                                 | 406 ms: 1.02x slower                                                             |
| genshi_xml                 | 49.4 ms                                                                | 50.1 ms: 1.02x slower                                                            |
| xml_etree_iterparse        | 99.0 ms                                                                | 101 ms: 1.02x slower                                                             |
| sqlglot_transpile          | 1.58 ms                                                                | 1.61 ms: 1.02x slower                                                            |
| sqlglot_parse              | 1.28 ms                                                                | 1.30 ms: 1.02x slower                                                            |
| nbody                      | 87.4 ms                                                                | 88.9 ms: 1.02x slower                                                            |
| json                       | 5.29 ms                                                                | 5.39 ms: 1.02x slower                                                            |
| richards_super             | 51.0 ms                                                                | 52.0 ms: 1.02x slower                                                            |
| chaos                      | 59.0 ms                                                                | 60.4 ms: 1.02x slower                                                            |
| deepcopy_memo              | 30.1 us                                                                | 30.9 us: 1.02x slower                                                            |
| deltablue                  | 3.27 ms                                                                | 3.36 ms: 1.03x slower                                                            |
| go                         | 118 ms                                                                 | 121 ms: 1.03x slower                                                             |
| scimark_sparse_mat_mult    | 4.51 ms                                                                | 4.65 ms: 1.03x slower                                                            |
| richards                   | 44.6 ms                                                                | 45.9 ms: 1.03x slower                                                            |
| scimark_monte_carlo        | 67.8 ms                                                                | 69.8 ms: 1.03x slower                                                            |
| pyflate                    | 432 ms                                                                 | 448 ms: 1.04x slower                                                             |
| gc_traversal               | 4.78 ms                                                                | 5.02 ms: 1.05x slower                                                            |
| logging_silent             | 103 ns                                                                 | 111 ns: 1.08x slower                                                             |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (27): async_tree_io_tg, sphinx, tomli_loads, pycparser, async_tree_memoization, sqlalchemy_imperative, many_optionals, async_tree_none_tg, coverage, crypto_pyaes, pylint, async_tree_none, json_loads, pidigits, 2to3, float, xml_etree_generate, asyncio_websockets, scimark_sor, sympy_integrate, sqlite_synth, pathlib, nqueens, mdp, async_tree_memoization_tg, k_core, async_tree_io
Ignored benchmarks (5) of results/bm-20250306-3.14.0a5+-052cb71-JIT/bm-20250306-linux-x86_64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71.json: docutils, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 82.52% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x