# Results vs. base

- fork: brandtbucher
- ref: justin_unlikely
- machine: darwin-arm64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.00x slower
- HPT reliability: 99.57%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 1.57 sec                                                               | 1.58 sec: 1.00x slower                                                  |
| html5lib       | 34.3 ms                                                                | 34.0 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (3): 2to3, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_eager                 | 63.8 ms                                                                | 63.4 ms: 1.01x faster                                                   |
| async_tree_eager_tg              | 42.6 ms                                                                | 42.4 ms: 1.01x faster                                                   |
| async_tree_io_tg                 | 611 ms                                                                 | 613 ms: 1.00x slower                                                    |
| async_generators                 | 294 ms                                                                 | 295 ms: 1.00x slower                                                    |
| async_tree_eager_cpu_io_mixed_tg | 336 ms                                                                 | 337 ms: 1.00x slower                                                    |
| async_tree_none                  | 198 ms                                                                 | 199 ms: 1.01x slower                                                    |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (15): async_tree_eager_memoization, asyncio_websockets, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_io_tg, async_tree_eager_io, async_tree_io, async_tree_memoization_tg, async_tree_memoization, coroutines, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_tcp_ssl, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 48.3 ms                                                                | 48.4 ms: 1.00x slower                                                   |
| pidigits       | 283 ms                                                                 | 284 ms: 1.00x slower                                                    |
| nbody          | 65.3 ms                                                                | 65.5 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 76.1 ms                                                                | 75.8 ms: 1.00x faster                                                   |
| regex_v8       | 16.8 ms                                                                | 16.9 ms: 1.01x slower                                                   |
| regex_effbot   | 2.61 ms                                                                | 2.63 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_list          | 2.92 us                                                                | 2.86 us: 1.02x faster                                                   |
| json_dumps           | 7.22 ms                                                                | 7.14 ms: 1.01x faster                                                   |
| xml_etree_parse      | 108 ms                                                                 | 107 ms: 1.01x faster                                                    |
| pickle_dict          | 18.2 us                                                                | 18.2 us: 1.00x slower                                                   |
| unpickle             | 9.09 us                                                                | 9.13 us: 1.00x slower                                                   |
| unpickle_pure_python | 131 us                                                                 | 132 us: 1.01x slower                                                    |
| xml_etree_generate   | 50.4 ms                                                                | 50.8 ms: 1.01x slower                                                   |
| xml_etree_process    | 34.7 ms                                                                | 35.0 ms: 1.01x slower                                                   |
| unpickle_list        | 2.93 us                                                                | 2.96 us: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_iterparse, json_loads, pickle, tomli_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 17.3 ms                                                                | 17.0 ms: 1.02x faster                                                   |
| django_template | 23.1 ms                                                                | 22.8 ms: 1.02x faster                                                   |
| genshi_xml      | 43.2 ms                                                                | 42.9 ms: 1.01x faster                                                   |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                        | bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text                      | 17.3 ms                                                                | 17.0 ms: 1.02x faster                                                   |
| pickle_list                      | 2.92 us                                                                | 2.86 us: 1.02x faster                                                   |
| django_template                  | 23.1 ms                                                                | 22.8 ms: 1.02x faster                                                   |
| generators                       | 25.5 ms                                                                | 25.2 ms: 1.01x faster                                                   |
| json_dumps                       | 7.22 ms                                                                | 7.14 ms: 1.01x faster                                                   |
| go                               | 99.3 ms                                                                | 98.2 ms: 1.01x faster                                                   |
| html5lib                         | 34.3 ms                                                                | 34.0 ms: 1.01x faster                                                   |
| create_gc_cycles                 | 1.32 ms                                                                | 1.31 ms: 1.01x faster                                                   |
| comprehensions                   | 13.1 us                                                                | 12.9 us: 1.01x faster                                                   |
| xml_etree_parse                  | 108 ms                                                                 | 107 ms: 1.01x faster                                                    |
| coverage                         | 43.9 ms                                                                | 43.5 ms: 1.01x faster                                                   |
| sqlglot_normalize                | 188 ms                                                                 | 186 ms: 1.01x faster                                                    |
| sympy_sum                        | 79.9 ms                                                                | 79.3 ms: 1.01x faster                                                   |
| genshi_xml                       | 43.2 ms                                                                | 42.9 ms: 1.01x faster                                                   |
| async_tree_eager                 | 63.8 ms                                                                | 63.4 ms: 1.01x faster                                                   |
| async_tree_eager_tg              | 42.6 ms                                                                | 42.4 ms: 1.01x faster                                                   |
| mdp                              | 1.56 sec                                                               | 1.55 sec: 1.00x faster                                                  |
| logging_format                   | 3.41 us                                                                | 3.40 us: 1.00x faster                                                   |
| regex_compile                    | 76.1 ms                                                                | 75.8 ms: 1.00x faster                                                   |
| meteor_contest                   | 74.9 ms                                                                | 74.6 ms: 1.00x faster                                                   |
| hexiom                           | 4.97 ms                                                                | 4.95 ms: 1.00x faster                                                   |
| sympy_expand                     | 248 ms                                                                 | 247 ms: 1.00x faster                                                    |
| logging_silent                   | 70.0 ns                                                                | 69.9 ns: 1.00x faster                                                   |
| float                            | 48.3 ms                                                                | 48.4 ms: 1.00x slower                                                   |
| scimark_sor                      | 85.9 ms                                                                | 86.1 ms: 1.00x slower                                                   |
| spectral_norm                    | 69.6 ms                                                                | 69.8 ms: 1.00x slower                                                   |
| async_tree_io_tg                 | 611 ms                                                                 | 613 ms: 1.00x slower                                                    |
| scimark_fft                      | 191 ms                                                                 | 191 ms: 1.00x slower                                                    |
| docutils                         | 1.57 sec                                                               | 1.58 sec: 1.00x slower                                                  |
| pyflate                          | 326 ms                                                                 | 327 ms: 1.00x slower                                                    |
| nqueens                          | 58.0 ms                                                                | 58.2 ms: 1.00x slower                                                   |
| pidigits                         | 283 ms                                                                 | 284 ms: 1.00x slower                                                    |
| nbody                            | 65.3 ms                                                                | 65.5 ms: 1.00x slower                                                   |
| pickle_dict                      | 18.2 us                                                                | 18.2 us: 1.00x slower                                                   |
| async_generators                 | 294 ms                                                                 | 295 ms: 1.00x slower                                                    |
| sqlite_synth                     | 1.53 us                                                                | 1.54 us: 1.00x slower                                                   |
| unpickle                         | 9.09 us                                                                | 9.13 us: 1.00x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 336 ms                                                                 | 337 ms: 1.00x slower                                                    |
| scimark_monte_carlo              | 45.7 ms                                                                | 45.9 ms: 1.00x slower                                                   |
| crypto_pyaes                     | 53.8 ms                                                                | 54.1 ms: 1.00x slower                                                   |
| async_tree_none                  | 198 ms                                                                 | 199 ms: 1.01x slower                                                    |
| regex_v8                         | 16.8 ms                                                                | 16.9 ms: 1.01x slower                                                   |
| fannkuch                         | 264 ms                                                                 | 266 ms: 1.01x slower                                                    |
| pprint_safe_repr                 | 493 ms                                                                 | 496 ms: 1.01x slower                                                    |
| unpickle_pure_python             | 131 us                                                                 | 132 us: 1.01x slower                                                    |
| xml_etree_generate               | 50.4 ms                                                                | 50.8 ms: 1.01x slower                                                   |
| chaos                            | 41.5 ms                                                                | 41.8 ms: 1.01x slower                                                   |
| xml_etree_process                | 34.7 ms                                                                | 35.0 ms: 1.01x slower                                                   |
| regex_effbot                     | 2.61 ms                                                                | 2.63 ms: 1.01x slower                                                   |
| unpickle_list                    | 2.93 us                                                                | 2.96 us: 1.01x slower                                                   |
| raytrace                         | 171 ms                                                                 | 173 ms: 1.01x slower                                                    |
| deepcopy_reduce                  | 1.54 us                                                                | 1.56 us: 1.01x slower                                                   |
| bpe_tokeniser                    | 3.05 sec                                                               | 3.09 sec: 1.01x slower                                                  |
| thrift                           | 421 us                                                                 | 426 us: 1.01x slower                                                    |
| unpack_sequence                  | 76.0 ns                                                                | 77.0 ns: 1.01x slower                                                   |
| pprint_pformat                   | 1.00 sec                                                               | 1.02 sec: 1.01x slower                                                  |
| telco                            | 4.57 ms                                                                | 4.67 ms: 1.02x slower                                                   |
| pathlib                          | 21.9 ms                                                                | 22.4 ms: 1.02x slower                                                   |
| richards_super                   | 37.6 ms                                                                | 38.7 ms: 1.03x slower                                                   |
| richards                         | 33.8 ms                                                                | 35.2 ms: 1.04x slower                                                   |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (46): tornado_http, gc_traversal, async_tree_eager_memoization, bench_mp_pool, sqlglot_transpile, scimark_sparse_mat_mult, sympy_integrate, deltablue, xml_etree_iterparse, regex_dna, json, sympy_str, dulwich_log, bench_thread_pool, asyncio_websockets, deepcopy_memo, pycparser, scimark_lu, json_loads, sphinx, sqlglot_optimize, logging_simple, python_startup_no_site, 2to3, async_tree_eager_memoization_tg, mako, deepcopy, pickle, async_tree_eager_cpu_io_mixed, python_startup, async_tree_eager_io_tg, async_tree_eager_io, async_tree_io, tomli_loads, async_tree_memoization_tg, sqlglot_parse, async_tree_memoization, typing_runtime_protocols, coroutines, async_tree_cpu_io_mixed_tg, pickle_pure_python, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_tcp_ssl, asyncio_tcp, pylint

# HPT report

- Reliability score: 99.57% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x