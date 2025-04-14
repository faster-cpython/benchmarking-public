# Results vs. base

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: darwin-arm64
- commit hash: 553888a
- commit date: 2025-03-07
- overall geometric mean: 1.013x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250306-darwin-arm64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 164 ms                                                                 | 165 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250306-darwin-arm64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_generators              | 269 ms                                                                 | 255 ms: 1.06x faster                                                             |
| async_tree_io                 | 373 ms                                                                 | 366 ms: 1.02x faster                                                             |
| async_tree_eager_cpu_io_mixed | 357 ms                                                                 | 359 ms: 1.00x slower                                                             |
| async_tree_eager_io_tg        | 370 ms                                                                 | 374 ms: 1.01x slower                                                             |
| async_tree_eager_memoization  | 140 ms                                                                 | 141 ms: 1.01x slower                                                             |
| async_tree_none_tg            | 154 ms                                                                 | 156 ms: 1.01x slower                                                             |
| coroutines                    | 16.6 ms                                                                | 16.8 ms: 1.02x slower                                                            |
| async_tree_io_tg              | 360 ms                                                                 | 366 ms: 1.02x slower                                                             |
| async_tree_eager              | 60.9 ms                                                                | 62.1 ms: 1.02x slower                                                            |
| async_tree_memoization        | 195 ms                                                                 | 203 ms: 1.04x slower                                                             |
| Geometric mean                | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (9): async_tree_none, asyncio_websockets, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_tg, async_tree_eager_memoization_tg, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250306-darwin-arm64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 47.4 ms                                                                | 47.9 ms: 1.01x slower                                                            |
| nbody          | 64.6 ms                                                                | 67.7 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250306-darwin-arm64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 141 ms                                                                 | 141 ms: 1.01x faster                                                             |
| regex_effbot   | 2.25 ms                                                                | 2.24 ms: 1.00x faster                                                            |
| regex_v8       | 16.7 ms                                                                | 16.7 ms: 1.00x slower                                                            |
| regex_compile  | 68.7 ms                                                                | 71.0 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250306-darwin-arm64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 7.26 ms                                                                | 7.29 ms: 1.00x slower                                                            |
| json_loads           | 17.6 us                                                                | 17.7 us: 1.01x slower                                                            |
| xml_etree_iterparse  | 70.5 ms                                                                | 71.1 ms: 1.01x slower                                                            |
| xml_etree_parse      | 102 ms                                                                 | 103 ms: 1.02x slower                                                             |
| xml_etree_generate   | 50.8 ms                                                                | 52.2 ms: 1.03x slower                                                            |
| xml_etree_process    | 35.7 ms                                                                | 37.2 ms: 1.04x slower                                                            |
| unpickle_pure_python | 134 us                                                                 | 142 us: 1.06x slower                                                             |
| tomli_loads          | 1.20 sec                                                               | 1.29 sec: 1.08x slower                                                           |
| pickle_pure_python   | 197 us                                                                 | 214 us: 1.09x slower                                                             |
| Geometric mean       | (ref)                                                                  | 1.04x slower                                                                     |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250306-darwin-arm64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 29.2 ms                                                                | 29.6 ms: 1.01x slower                                                            |
| django_template | 21.0 ms                                                                | 21.3 ms: 1.01x slower                                                            |
| genshi_text     | 13.8 ms                                                                | 14.1 ms: 1.02x slower                                                            |
| mako            | 6.48 ms                                                                | 6.66 ms: 1.03x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                                     |

All benchmarks:
===============

| Benchmark                     | bm-20250306-darwin-arm64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_generators              | 269 ms                                                                 | 255 ms: 1.06x faster                                                             |
| async_tree_io                 | 373 ms                                                                 | 366 ms: 1.02x faster                                                             |
| meteor_contest                | 74.9 ms                                                                | 74.0 ms: 1.01x faster                                                            |
| create_gc_cycles              | 1.28 ms                                                                | 1.27 ms: 1.01x faster                                                            |
| regex_dna                     | 141 ms                                                                 | 141 ms: 1.01x faster                                                             |
| regex_effbot                  | 2.25 ms                                                                | 2.24 ms: 1.00x faster                                                            |
| gc_traversal                  | 3.10 ms                                                                | 3.09 ms: 1.00x faster                                                            |
| regex_v8                      | 16.7 ms                                                                | 16.7 ms: 1.00x slower                                                            |
| scimark_monte_carlo           | 43.3 ms                                                                | 43.5 ms: 1.00x slower                                                            |
| json_dumps                    | 7.26 ms                                                                | 7.29 ms: 1.00x slower                                                            |
| deepcopy_reduce               | 1.57 us                                                                | 1.58 us: 1.00x slower                                                            |
| async_tree_eager_cpu_io_mixed | 357 ms                                                                 | 359 ms: 1.00x slower                                                             |
| pathlib                       | 23.2 ms                                                                | 23.4 ms: 1.01x slower                                                            |
| json_loads                    | 17.6 us                                                                | 17.7 us: 1.01x slower                                                            |
| generators                    | 23.6 ms                                                                | 23.8 ms: 1.01x slower                                                            |
| telco                         | 4.52 ms                                                                | 4.55 ms: 1.01x slower                                                            |
| logging_simple                | 3.20 us                                                                | 3.22 us: 1.01x slower                                                            |
| xml_etree_iterparse           | 70.5 ms                                                                | 71.1 ms: 1.01x slower                                                            |
| sympy_sum                     | 73.5 ms                                                                | 74.2 ms: 1.01x slower                                                            |
| scimark_lu                    | 73.5 ms                                                                | 74.3 ms: 1.01x slower                                                            |
| scimark_sparse_mat_mult       | 2.94 ms                                                                | 2.97 ms: 1.01x slower                                                            |
| async_tree_eager_io_tg        | 370 ms                                                                 | 374 ms: 1.01x slower                                                             |
| logging_format                | 3.50 us                                                                | 3.53 us: 1.01x slower                                                            |
| float                         | 47.4 ms                                                                | 47.9 ms: 1.01x slower                                                            |
| 2to3                          | 164 ms                                                                 | 165 ms: 1.01x slower                                                             |
| sqlalchemy_declarative        | 58.6 ms                                                                | 59.2 ms: 1.01x slower                                                            |
| bench_mp_pool                 | 60.5 ms                                                                | 61.2 ms: 1.01x slower                                                            |
| deepcopy                      | 150 us                                                                 | 152 us: 1.01x slower                                                             |
| many_optionals                | 451 us                                                                 | 456 us: 1.01x slower                                                             |
| spectral_norm                 | 71.4 ms                                                                | 72.2 ms: 1.01x slower                                                            |
| async_tree_eager_memoization  | 140 ms                                                                 | 141 ms: 1.01x slower                                                             |
| sympy_integrate               | 11.3 ms                                                                | 11.5 ms: 1.01x slower                                                            |
| crypto_pyaes                  | 55.4 ms                                                                | 56.0 ms: 1.01x slower                                                            |
| genshi_xml                    | 29.2 ms                                                                | 29.6 ms: 1.01x slower                                                            |
| sympy_expand                  | 238 ms                                                                 | 241 ms: 1.01x slower                                                             |
| django_template               | 21.0 ms                                                                | 21.3 ms: 1.01x slower                                                            |
| async_tree_none_tg            | 154 ms                                                                 | 156 ms: 1.01x slower                                                             |
| sympy_str                     | 140 ms                                                                 | 142 ms: 1.01x slower                                                             |
| chaos                         | 39.0 ms                                                                | 39.6 ms: 1.01x slower                                                            |
| sqlalchemy_imperative         | 6.66 ms                                                                | 6.76 ms: 1.02x slower                                                            |
| xml_etree_parse               | 102 ms                                                                 | 103 ms: 1.02x slower                                                             |
| coroutines                    | 16.6 ms                                                                | 16.8 ms: 1.02x slower                                                            |
| async_tree_io_tg              | 360 ms                                                                 | 366 ms: 1.02x slower                                                             |
| genshi_text                   | 13.8 ms                                                                | 14.1 ms: 1.02x slower                                                            |
| async_tree_eager              | 60.9 ms                                                                | 62.1 ms: 1.02x slower                                                            |
| pyflate                       | 307 ms                                                                 | 313 ms: 1.02x slower                                                             |
| scimark_sor                   | 79.3 ms                                                                | 80.9 ms: 1.02x slower                                                            |
| hexiom                        | 4.38 ms                                                                | 4.47 ms: 1.02x slower                                                            |
| go                            | 81.4 ms                                                                | 83.1 ms: 1.02x slower                                                            |
| richards                      | 32.1 ms                                                                | 32.8 ms: 1.02x slower                                                            |
| richards_super                | 36.4 ms                                                                | 37.2 ms: 1.02x slower                                                            |
| bpe_tokeniser                 | 2.92 sec                                                               | 3.00 sec: 1.02x slower                                                           |
| dulwich_log                   | 28.1 ms                                                                | 28.8 ms: 1.02x slower                                                            |
| deepcopy_memo                 | 18.2 us                                                                | 18.7 us: 1.03x slower                                                            |
| nqueens                       | 58.6 ms                                                                | 60.1 ms: 1.03x slower                                                            |
| xml_etree_generate            | 50.8 ms                                                                | 52.2 ms: 1.03x slower                                                            |
| mako                          | 6.48 ms                                                                | 6.66 ms: 1.03x slower                                                            |
| scimark_fft                   | 183 ms                                                                 | 187 ms: 1.03x slower                                                             |
| typing_runtime_protocols      | 92.0 us                                                                | 94.5 us: 1.03x slower                                                            |
| subparsers                    | 11.9 ms                                                                | 12.2 ms: 1.03x slower                                                            |
| raytrace                      | 178 ms                                                                 | 183 ms: 1.03x slower                                                             |
| deltablue                     | 2.35 ms                                                                | 2.42 ms: 1.03x slower                                                            |
| regex_compile                 | 68.7 ms                                                                | 71.0 ms: 1.03x slower                                                            |
| async_tree_memoization        | 195 ms                                                                 | 203 ms: 1.04x slower                                                             |
| xml_etree_process             | 35.7 ms                                                                | 37.2 ms: 1.04x slower                                                            |
| logging_silent                | 64.8 ns                                                                | 67.7 ns: 1.04x slower                                                            |
| nbody                         | 64.6 ms                                                                | 67.7 ms: 1.05x slower                                                            |
| sqlglot_transpile             | 1.02 ms                                                                | 1.07 ms: 1.05x slower                                                            |
| unpickle_pure_python          | 134 us                                                                 | 142 us: 1.06x slower                                                             |
| sqlglot_parse                 | 847 us                                                                 | 900 us: 1.06x slower                                                             |
| bench_thread_pool             | 464 us                                                                 | 496 us: 1.07x slower                                                             |
| fannkuch                      | 285 ms                                                                 | 305 ms: 1.07x slower                                                             |
| tomli_loads                   | 1.20 sec                                                               | 1.29 sec: 1.08x slower                                                           |
| pickle_pure_python            | 197 us                                                                 | 214 us: 1.09x slower                                                             |
| Geometric mean                | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (26): async_tree_none, dask, asyncio_websockets, pidigits, comprehensions, sqlite_synth, python_startup, shortest_path, python_startup_no_site, thrift, mdp, pycparser, connected_components, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, k_core, coverage, json, sphinx, pylint, async_tree_memoization_tg, async_tree_eager_tg, html5lib, async_tree_eager_memoization_tg, async_tree_eager_io
Ignored benchmarks (5) of results/bm-20250306-3.14.0a5+-052cb71-JIT/bm-20250306-darwin-arm64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71.json: docutils, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x