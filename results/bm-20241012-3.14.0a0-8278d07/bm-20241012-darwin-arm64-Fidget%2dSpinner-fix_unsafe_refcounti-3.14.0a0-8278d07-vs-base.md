# Results vs. base

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: darwin-arm64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.00x slower
- HPT reliability: 96.37%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241011-darwin-arm64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 160 ms                                                                | 196 ms: 1.22x slower                                                            |
| docutils       | 1.40 sec                                                              | 1.41 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                                    |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241011-darwin-arm64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager                 | 59.8 ms                                                               | 59.7 ms: 1.00x faster                                                           |
| async_tree_eager_cpu_io_mixed_tg | 336 ms                                                                | 337 ms: 1.00x slower                                                            |
| async_tree_eager_tg              | 41.8 ms                                                               | 41.9 ms: 1.00x slower                                                           |
| async_generators                 | 277 ms                                                                | 279 ms: 1.01x slower                                                            |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (17): asyncio_tcp, async_tree_io_tg, async_tree_memoization_tg, async_tree_io, async_tree_none, async_tree_none_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_memoization, asyncio_websockets, coroutines, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241011-darwin-arm64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 16.9 ms                                                               | 16.5 ms: 1.02x faster                                                           |
| regex_effbot   | 2.66 ms                                                               | 2.60 ms: 1.02x faster                                                           |
| regex_dna      | 148 ms                                                                | 146 ms: 1.01x faster                                                            |
| regex_compile  | 68.0 ms                                                               | 68.3 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241011-darwin-arm64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 73.8 ms                                                               | 73.1 ms: 1.01x faster                                                           |
| pickle               | 7.37 us                                                               | 7.34 us: 1.00x faster                                                           |
| pickle_pure_python   | 183 us                                                                | 183 us: 1.00x slower                                                            |
| unpickle_pure_python | 142 us                                                                | 142 us: 1.00x slower                                                            |
| xml_etree_process    | 37.3 ms                                                               | 37.4 ms: 1.00x slower                                                           |
| xml_etree_generate   | 52.0 ms                                                               | 52.4 ms: 1.01x slower                                                           |
| json_dumps           | 7.19 ms                                                               | 7.25 ms: 1.01x slower                                                           |
| unpickle_list        | 2.96 us                                                               | 2.99 us: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (6): tomli_loads, json_loads, pickle_list, unpickle, pickle_dict, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241011-darwin-arm64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 17.2 ms                                                               | 19.0 ms: 1.11x slower                                                           |
| python_startup_no_site | 14.3 ms                                                               | 15.9 ms: 1.12x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.11x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241011-darwin-arm64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 19.9 ms                                                               | 20.0 ms: 1.01x slower                                                           |
| mako            | 6.86 ms                                                               | 7.00 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20241011-darwin-arm64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8                         | 16.9 ms                                                               | 16.5 ms: 1.02x faster                                                           |
| regex_effbot                     | 2.66 ms                                                               | 2.60 ms: 1.02x faster                                                           |
| scimark_monte_carlo              | 44.5 ms                                                               | 43.7 ms: 1.02x faster                                                           |
| regex_dna                        | 148 ms                                                                | 146 ms: 1.01x faster                                                            |
| sympy_sum                        | 70.0 ms                                                               | 69.3 ms: 1.01x faster                                                           |
| xml_etree_iterparse              | 73.8 ms                                                               | 73.1 ms: 1.01x faster                                                           |
| richards_super                   | 35.1 ms                                                               | 34.8 ms: 1.01x faster                                                           |
| telco                            | 4.60 ms                                                               | 4.57 ms: 1.01x faster                                                           |
| dulwich_log                      | 27.5 ms                                                               | 27.4 ms: 1.01x faster                                                           |
| scimark_fft                      | 191 ms                                                                | 190 ms: 1.01x faster                                                            |
| pickle                           | 7.37 us                                                               | 7.34 us: 1.00x faster                                                           |
| logging_simple                   | 3.07 us                                                               | 3.05 us: 1.00x faster                                                           |
| logging_silent                   | 60.8 ns                                                               | 60.6 ns: 1.00x faster                                                           |
| scimark_lu                       | 67.3 ms                                                               | 67.0 ms: 1.00x faster                                                           |
| bench_thread_pool                | 456 us                                                                | 455 us: 1.00x faster                                                            |
| deltablue                        | 2.23 ms                                                               | 2.22 ms: 1.00x faster                                                           |
| bpe_tokeniser                    | 3.09 sec                                                              | 3.08 sec: 1.00x faster                                                          |
| async_tree_eager                 | 59.8 ms                                                               | 59.7 ms: 1.00x faster                                                           |
| pickle_pure_python               | 183 us                                                                | 183 us: 1.00x slower                                                            |
| pyflate                          | 327 ms                                                                | 327 ms: 1.00x slower                                                            |
| spectral_norm                    | 70.6 ms                                                               | 70.8 ms: 1.00x slower                                                           |
| richards                         | 31.1 ms                                                               | 31.2 ms: 1.00x slower                                                           |
| deepcopy                         | 147 us                                                                | 147 us: 1.00x slower                                                            |
| unpickle_pure_python             | 142 us                                                                | 142 us: 1.00x slower                                                            |
| xml_etree_process                | 37.3 ms                                                               | 37.4 ms: 1.00x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 336 ms                                                                | 337 ms: 1.00x slower                                                            |
| scimark_sparse_mat_mult          | 2.81 ms                                                               | 2.82 ms: 1.00x slower                                                           |
| crypto_pyaes                     | 51.1 ms                                                               | 51.2 ms: 1.00x slower                                                           |
| regex_compile                    | 68.0 ms                                                               | 68.3 ms: 1.00x slower                                                           |
| async_tree_eager_tg              | 41.8 ms                                                               | 41.9 ms: 1.00x slower                                                           |
| sqlglot_normalize                | 166 ms                                                                | 166 ms: 1.00x slower                                                            |
| pprint_pformat                   | 937 ms                                                                | 943 ms: 1.01x slower                                                            |
| docutils                         | 1.40 sec                                                              | 1.41 sec: 1.01x slower                                                          |
| async_generators                 | 277 ms                                                                | 279 ms: 1.01x slower                                                            |
| django_template                  | 19.9 ms                                                               | 20.0 ms: 1.01x slower                                                           |
| xml_etree_generate               | 52.0 ms                                                               | 52.4 ms: 1.01x slower                                                           |
| raytrace                         | 153 ms                                                                | 154 ms: 1.01x slower                                                            |
| sqlglot_parse                    | 738 us                                                                | 743 us: 1.01x slower                                                            |
| json_dumps                       | 7.19 ms                                                               | 7.25 ms: 1.01x slower                                                           |
| pprint_safe_repr                 | 457 ms                                                                | 461 ms: 1.01x slower                                                            |
| deepcopy_reduce                  | 1.52 us                                                               | 1.53 us: 1.01x slower                                                           |
| unpickle_list                    | 2.96 us                                                               | 2.99 us: 1.01x slower                                                           |
| pathlib                          | 21.8 ms                                                               | 22.0 ms: 1.01x slower                                                           |
| deepcopy_memo                    | 17.1 us                                                               | 17.3 us: 1.01x slower                                                           |
| meteor_contest                   | 70.7 ms                                                               | 71.5 ms: 1.01x slower                                                           |
| thrift                           | 413 us                                                                | 419 us: 1.01x slower                                                            |
| create_gc_cycles                 | 914 us                                                                | 929 us: 1.02x slower                                                            |
| bench_mp_pool                    | 49.5 ms                                                               | 50.5 ms: 1.02x slower                                                           |
| mako                             | 6.86 ms                                                               | 7.00 ms: 1.02x slower                                                           |
| chaos                            | 36.4 ms                                                               | 37.4 ms: 1.03x slower                                                           |
| python_startup                   | 17.2 ms                                                               | 19.0 ms: 1.11x slower                                                           |
| python_startup_no_site           | 14.3 ms                                                               | 15.9 ms: 1.12x slower                                                           |
| 2to3                             | 160 ms                                                                | 196 ms: 1.22x slower                                                            |
| Geometric mean                   | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (52): asyncio_tcp, async_tree_io_tg, tomli_loads, async_tree_memoization_tg, json, tornado_http, async_tree_io, json_loads, float, async_tree_none, async_tree_none_tg, async_tree_eager_io, hexiom, async_tree_eager_io_tg, generators, coverage, async_tree_memoization, asyncio_websockets, sympy_expand, html5lib, pickle_list, sympy_str, comprehensions, coroutines, async_tree_cpu_io_mixed_tg, typing_runtime_protocols, unpickle, nqueens, go, genshi_text, sqlglot_optimize, sqlite_synth, pycparser, asyncio_tcp_ssl, logging_format, scimark_sor, mdp, async_tree_eager_memoization, pidigits, genshi_xml, nbody, pickle_dict, pylint, sympy_integrate, async_tree_eager_memoization_tg, unpack_sequence, fannkuch, xml_etree_parse, sqlglot_transpile, gc_traversal, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed

# HPT report

- Reliability score: 96.37% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x