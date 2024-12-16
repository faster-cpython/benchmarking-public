# Results vs. base

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: darwin-arm64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.013x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| html5lib       | 33.4 ms                                                                | 33.0 ms: 1.01x faster                                                            |
| sphinx         | 599 ms                                                                 | 576 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_generators                 | 300 ms                                                                 | 282 ms: 1.06x faster                                                             |
| async_tree_eager_memoization_tg  | 128 ms                                                                 | 126 ms: 1.02x faster                                                             |
| async_tree_memoization           | 205 ms                                                                 | 201 ms: 1.02x faster                                                             |
| async_tree_eager_memoization     | 150 ms                                                                 | 147 ms: 1.01x faster                                                             |
| async_tree_eager                 | 67.8 ms                                                                | 67.1 ms: 1.01x faster                                                            |
| async_tree_memoization_tg        | 193 ms                                                                 | 192 ms: 1.01x faster                                                             |
| async_tree_eager_cpu_io_mixed_tg | 344 ms                                                                 | 342 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed          | 422 ms                                                                 | 419 ms: 1.01x faster                                                             |
| async_tree_eager_cpu_io_mixed    | 368 ms                                                                 | 366 ms: 1.01x faster                                                             |
| coroutines                       | 17.5 ms                                                                | 17.7 ms: 1.01x slower                                                            |
| async_tree_eager_tg              | 45.8 ms                                                                | 46.5 ms: 1.01x slower                                                            |
| async_tree_io_tg                 | 361 ms                                                                 | 374 ms: 1.04x slower                                                             |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (7): async_tree_eager_io, async_tree_none, async_tree_io, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 47.8 ms                                                                | 50.5 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.0 ms                                                                | 15.9 ms: 1.01x faster                                                            |
| regex_dna      | 136 ms                                                                 | 136 ms: 1.00x faster                                                             |
| regex_compile  | 69.5 ms                                                                | 69.8 ms: 1.01x slower                                                            |
| regex_effbot   | 2.01 ms                                                                | 2.03 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 197 us                                                                 | 190 us: 1.04x faster                                                             |
| xml_etree_generate   | 49.3 ms                                                                | 49.0 ms: 1.01x faster                                                            |
| tomli_loads          | 1.21 sec                                                               | 1.21 sec: 1.01x faster                                                           |
| json_loads           | 16.5 us                                                                | 16.5 us: 1.00x slower                                                            |
| unpickle_pure_python | 125 us                                                                 | 127 us: 1.01x slower                                                             |
| xml_etree_iterparse  | 69.9 ms                                                                | 71.9 ms: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 41.6 ms                                                                | 30.7 ms: 1.36x faster                                                            |
| genshi_text     | 17.6 ms                                                                | 14.5 ms: 1.22x faster                                                            |
| django_template | 23.2 ms                                                                | 21.1 ms: 1.10x faster                                                            |
| Geometric mean  | (ref)                                                                  | 1.16x faster                                                                     |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                        | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml                       | 41.6 ms                                                                | 30.7 ms: 1.36x faster                                                            |
| genshi_text                      | 17.6 ms                                                                | 14.5 ms: 1.22x faster                                                            |
| generators                       | 28.4 ms                                                                | 23.4 ms: 1.21x faster                                                            |
| go                               | 99.7 ms                                                                | 89.3 ms: 1.12x faster                                                            |
| django_template                  | 23.2 ms                                                                | 21.1 ms: 1.10x faster                                                            |
| nqueens                          | 62.7 ms                                                                | 57.8 ms: 1.08x faster                                                            |
| comprehensions                   | 14.0 us                                                                | 13.0 us: 1.07x faster                                                            |
| hexiom                           | 4.91 ms                                                                | 4.58 ms: 1.07x faster                                                            |
| raytrace                         | 184 ms                                                                 | 173 ms: 1.06x faster                                                             |
| async_generators                 | 300 ms                                                                 | 282 ms: 1.06x faster                                                             |
| chaos                            | 42.4 ms                                                                | 40.2 ms: 1.05x faster                                                            |
| logging_silent                   | 75.7 ns                                                                | 71.9 ns: 1.05x faster                                                            |
| mdp                              | 1.57 sec                                                               | 1.50 sec: 1.05x faster                                                           |
| sphinx                           | 599 ms                                                                 | 576 ms: 1.04x faster                                                             |
| pickle_pure_python               | 197 us                                                                 | 190 us: 1.04x faster                                                             |
| deepcopy                         | 158 us                                                                 | 153 us: 1.03x faster                                                             |
| richards                         | 34.6 ms                                                                | 33.6 ms: 1.03x faster                                                            |
| richards_super                   | 38.4 ms                                                                | 37.3 ms: 1.03x faster                                                            |
| pyflate                          | 319 ms                                                                 | 310 ms: 1.03x faster                                                             |
| sqlglot_normalize                | 187 ms                                                                 | 182 ms: 1.03x faster                                                             |
| sympy_sum                        | 75.4 ms                                                                | 73.5 ms: 1.03x faster                                                            |
| async_tree_eager_memoization_tg  | 128 ms                                                                 | 126 ms: 1.02x faster                                                             |
| thrift                           | 443 us                                                                 | 435 us: 1.02x faster                                                             |
| pprint_safe_repr                 | 498 ms                                                                 | 489 ms: 1.02x faster                                                             |
| async_tree_memoization           | 205 ms                                                                 | 201 ms: 1.02x faster                                                             |
| sqlglot_optimize                 | 34.2 ms                                                                | 33.6 ms: 1.02x faster                                                            |
| pprint_pformat                   | 1.01 sec                                                               | 991 ms: 1.02x faster                                                             |
| meteor_contest                   | 72.7 ms                                                                | 71.7 ms: 1.01x faster                                                            |
| async_tree_eager_memoization     | 150 ms                                                                 | 147 ms: 1.01x faster                                                             |
| html5lib                         | 33.4 ms                                                                | 33.0 ms: 1.01x faster                                                            |
| create_gc_cycles                 | 1.28 ms                                                                | 1.26 ms: 1.01x faster                                                            |
| logging_simple                   | 3.43 us                                                                | 3.39 us: 1.01x faster                                                            |
| bench_thread_pool                | 503 us                                                                 | 497 us: 1.01x faster                                                             |
| sympy_integrate                  | 11.8 ms                                                                | 11.6 ms: 1.01x faster                                                            |
| sympy_str                        | 144 ms                                                                 | 143 ms: 1.01x faster                                                             |
| async_tree_eager                 | 67.8 ms                                                                | 67.1 ms: 1.01x faster                                                            |
| sympy_expand                     | 244 ms                                                                 | 242 ms: 1.01x faster                                                             |
| logging_format                   | 3.73 us                                                                | 3.70 us: 1.01x faster                                                            |
| async_tree_memoization_tg        | 193 ms                                                                 | 192 ms: 1.01x faster                                                             |
| regex_v8                         | 16.0 ms                                                                | 15.9 ms: 1.01x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 344 ms                                                                 | 342 ms: 1.01x faster                                                             |
| xml_etree_generate               | 49.3 ms                                                                | 49.0 ms: 1.01x faster                                                            |
| fannkuch                         | 272 ms                                                                 | 270 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed          | 422 ms                                                                 | 419 ms: 1.01x faster                                                             |
| tomli_loads                      | 1.21 sec                                                               | 1.21 sec: 1.01x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 368 ms                                                                 | 366 ms: 1.01x faster                                                             |
| scimark_sparse_mat_mult          | 2.89 ms                                                                | 2.88 ms: 1.01x faster                                                            |
| regex_dna                        | 136 ms                                                                 | 136 ms: 1.00x faster                                                             |
| crypto_pyaes                     | 53.8 ms                                                                | 53.9 ms: 1.00x slower                                                            |
| sqlite_synth                     | 1.54 us                                                                | 1.55 us: 1.00x slower                                                            |
| json_loads                       | 16.5 us                                                                | 16.5 us: 1.00x slower                                                            |
| regex_compile                    | 69.5 ms                                                                | 69.8 ms: 1.01x slower                                                            |
| bench_mp_pool                    | 63.3 ms                                                                | 63.7 ms: 1.01x slower                                                            |
| regex_effbot                     | 2.01 ms                                                                | 2.03 ms: 1.01x slower                                                            |
| pathlib                          | 22.4 ms                                                                | 22.5 ms: 1.01x slower                                                            |
| sqlglot_transpile                | 1.03 ms                                                                | 1.04 ms: 1.01x slower                                                            |
| coroutines                       | 17.5 ms                                                                | 17.7 ms: 1.01x slower                                                            |
| telco                            | 4.46 ms                                                                | 4.51 ms: 1.01x slower                                                            |
| subparsers                       | 12.2 ms                                                                | 12.4 ms: 1.01x slower                                                            |
| deepcopy_reduce                  | 1.59 us                                                                | 1.61 us: 1.01x slower                                                            |
| unpickle_pure_python             | 125 us                                                                 | 127 us: 1.01x slower                                                             |
| async_tree_eager_tg              | 45.8 ms                                                                | 46.5 ms: 1.01x slower                                                            |
| sqlglot_parse                    | 854 us                                                                 | 867 us: 1.02x slower                                                             |
| spectral_norm                    | 62.0 ms                                                                | 63.0 ms: 1.02x slower                                                            |
| dulwich_log                      | 29.0 ms                                                                | 29.6 ms: 1.02x slower                                                            |
| sqlalchemy_imperative            | 6.64 ms                                                                | 6.79 ms: 1.02x slower                                                            |
| xml_etree_iterparse              | 69.9 ms                                                                | 71.9 ms: 1.03x slower                                                            |
| async_tree_io_tg                 | 361 ms                                                                 | 374 ms: 1.04x slower                                                             |
| float                            | 47.8 ms                                                                | 50.5 ms: 1.06x slower                                                            |
| deepcopy_memo                    | 17.2 us                                                                | 18.3 us: 1.06x slower                                                            |
| scimark_lu                       | 68.6 ms                                                                | 74.7 ms: 1.09x slower                                                            |
| scimark_sor                      | 82.2 ms                                                                | 97.3 ms: 1.18x slower                                                            |
| Geometric mean                   | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (33): pylint, k_core, async_tree_eager_io, async_tree_none, async_tree_io, xml_etree_parse, mypy2, connected_components, gc_traversal, python_startup, bpe_tokeniser, asyncio_websockets, json_dumps, scimark_monte_carlo, docutils, pidigits, scimark_fft, coverage, nbody, shortest_path, python_startup_no_site, mako, pycparser, xml_etree_process, async_tree_cpu_io_mixed_tg, sqlalchemy_declarative, many_optionals, deltablue, json, typing_runtime_protocols, async_tree_eager_io_tg, 2to3, async_tree_none_tg

- Geometric mean (including insignificant results): 1.013x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x