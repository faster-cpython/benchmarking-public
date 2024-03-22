# Results vs. base

- fork: brandtbucher
- ref: justin_ghccc
- machine: darwin-arm64
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.00x slower
- HPT reliability: 92.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| chameleon      | 4.46 ms                                                                | 4.48 ms: 1.00x slower                                                |
| docutils       | 2.60 sec                                                               | 2.61 sec: 1.00x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|---------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_eager_tg             | 44.6 ms                                                                | 44.3 ms: 1.01x faster                                                |
| async_tree_eager_memoization_tg | 331 ms                                                                 | 332 ms: 1.00x slower                                                 |
| async_tree_eager_io             | 16.9 sec                                                               | 17.0 sec: 1.00x slower                                               |
| async_tree_io                   | 8.92 sec                                                               | 8.95 sec: 1.00x slower                                               |
| async_tree_io_tg                | 9.35 sec                                                               | 9.42 sec: 1.01x slower                                               |
| Geometric mean                  | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (11): async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_eager, async_tree_eager_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_eager_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 70.3 ms                                                                | 72.4 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                                | 2.62 ms: 1.01x faster                                                |
| regex_dna      | 152 ms                                                                 | 152 ms: 1.00x faster                                                 |
| regex_v8       | 17.1 ms                                                                | 17.2 ms: 1.00x slower                                                |
| regex_compile  | 82.0 ms                                                                | 83.2 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle               | 7.44 us                                                                | 7.41 us: 1.00x faster                                                |
| json_loads           | 17.0 us                                                                | 17.1 us: 1.00x slower                                                |
| unpickle_pure_python | 142 us                                                                 | 143 us: 1.00x slower                                                 |
| unpickle_list        | 3.05 us                                                                | 3.08 us: 1.01x slower                                                |
| xml_etree_generate   | 60.2 ms                                                                | 61.0 ms: 1.01x slower                                                |
| pickle_list          | 2.96 us                                                                | 3.01 us: 1.02x slower                                                |
| unpickle             | 9.11 us                                                                | 9.33 us: 1.02x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (7): tomli_loads, xml_etree_iterparse, xml_etree_parse, pickle_dict, json_dumps, pickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                                | 18.9 ms: 1.06x slower                                                |
| python_startup_no_site | 16.1 ms                                                                | 17.2 ms: 1.07x slower                                                |
| Geometric mean         | (ref)                                                                  | 1.07x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 35.7 ms                                                                | 35.4 ms: 1.01x faster                                                |
| django_template | 20.5 ms                                                                | 20.4 ms: 1.00x faster                                                |
| genshi_text     | 14.7 ms                                                                | 14.8 ms: 1.00x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                       | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|---------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml                      | 35.7 ms                                                                | 35.4 ms: 1.01x faster                                                |
| coverage                        | 47.2 ms                                                                | 46.8 ms: 1.01x faster                                                |
| sqlglot_parse                   | 826 us                                                                 | 820 us: 1.01x faster                                                 |
| regex_effbot                    | 2.64 ms                                                                | 2.62 ms: 1.01x faster                                                |
| sympy_sum                       | 75.0 ms                                                                | 74.5 ms: 1.01x faster                                                |
| pycparser                       | 840 ms                                                                 | 834 ms: 1.01x faster                                                 |
| scimark_sor                     | 107 ms                                                                 | 106 ms: 1.01x faster                                                 |
| chaos                           | 38.6 ms                                                                | 38.3 ms: 1.01x faster                                                |
| telco                           | 4.57 ms                                                                | 4.54 ms: 1.01x faster                                                |
| async_tree_eager_tg             | 44.6 ms                                                                | 44.3 ms: 1.01x faster                                                |
| richards_super                  | 35.0 ms                                                                | 34.8 ms: 1.00x faster                                                |
| logging_format                  | 3.60 us                                                                | 3.58 us: 1.00x faster                                                |
| pickle                          | 7.44 us                                                                | 7.41 us: 1.00x faster                                                |
| django_template                 | 20.5 ms                                                                | 20.4 ms: 1.00x faster                                                |
| dulwich_log                     | 29.8 ms                                                                | 29.8 ms: 1.00x faster                                                |
| regex_dna                       | 152 ms                                                                 | 152 ms: 1.00x faster                                                 |
| logging_silent                  | 65.5 ns                                                                | 65.6 ns: 1.00x slower                                                |
| scimark_lu                      | 81.4 ms                                                                | 81.5 ms: 1.00x slower                                                |
| async_tree_eager_memoization_tg | 331 ms                                                                 | 332 ms: 1.00x slower                                                 |
| richards                        | 31.7 ms                                                                | 31.8 ms: 1.00x slower                                                |
| async_tree_eager_io             | 16.9 sec                                                               | 17.0 sec: 1.00x slower                                               |
| gc_traversal                    | 2.43 ms                                                                | 2.44 ms: 1.00x slower                                                |
| chameleon                       | 4.46 ms                                                                | 4.48 ms: 1.00x slower                                                |
| async_tree_io                   | 8.92 sec                                                               | 8.95 sec: 1.00x slower                                               |
| docutils                        | 2.60 sec                                                               | 2.61 sec: 1.00x slower                                               |
| json_loads                      | 17.0 us                                                                | 17.1 us: 1.00x slower                                                |
| unpickle_pure_python            | 142 us                                                                 | 143 us: 1.00x slower                                                 |
| genshi_text                     | 14.7 ms                                                                | 14.8 ms: 1.00x slower                                                |
| regex_v8                        | 17.1 ms                                                                | 17.2 ms: 1.00x slower                                                |
| mdp                             | 1.60 sec                                                               | 1.61 sec: 1.01x slower                                               |
| hexiom                          | 4.82 ms                                                                | 4.85 ms: 1.01x slower                                                |
| scimark_monte_carlo             | 44.7 ms                                                                | 45.0 ms: 1.01x slower                                                |
| async_tree_io_tg                | 9.35 sec                                                               | 9.42 sec: 1.01x slower                                               |
| scimark_sparse_mat_mult         | 3.14 ms                                                                | 3.16 ms: 1.01x slower                                                |
| sympy_expand                    | 236 ms                                                                 | 238 ms: 1.01x slower                                                 |
| pprint_safe_repr                | 492 ms                                                                 | 496 ms: 1.01x slower                                                 |
| generators                      | 27.1 ms                                                                | 27.3 ms: 1.01x slower                                                |
| thrift                          | 433 us                                                                 | 437 us: 1.01x slower                                                 |
| json                            | 2.93 ms                                                                | 2.96 ms: 1.01x slower                                                |
| unpickle_list                   | 3.05 us                                                                | 3.08 us: 1.01x slower                                                |
| coroutines                      | 17.8 ms                                                                | 18.0 ms: 1.01x slower                                                |
| xml_etree_generate              | 60.2 ms                                                                | 61.0 ms: 1.01x slower                                                |
| create_gc_cycles                | 749 us                                                                 | 760 us: 1.01x slower                                                 |
| meteor_contest                  | 73.9 ms                                                                | 75.0 ms: 1.01x slower                                                |
| regex_compile                   | 82.0 ms                                                                | 83.2 ms: 1.01x slower                                                |
| fannkuch                        | 261 ms                                                                 | 266 ms: 1.02x slower                                                 |
| pickle_list                     | 2.96 us                                                                | 3.01 us: 1.02x slower                                                |
| deepcopy                        | 213 us                                                                 | 217 us: 1.02x slower                                                 |
| pyflate                         | 330 ms                                                                 | 336 ms: 1.02x slower                                                 |
| unpickle                        | 9.11 us                                                                | 9.33 us: 1.02x slower                                                |
| nbody                           | 70.3 ms                                                                | 72.4 ms: 1.03x slower                                                |
| raytrace                        | 179 ms                                                                 | 186 ms: 1.04x slower                                                 |
| python_startup                  | 17.8 ms                                                                | 18.9 ms: 1.06x slower                                                |
| python_startup_no_site          | 16.1 ms                                                                | 17.2 ms: 1.07x slower                                                |
| spectral_norm                   | 74.5 ms                                                                | 79.8 ms: 1.07x slower                                                |
| Geometric mean                  | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (54): tornado_http, gunicorn, asyncio_tcp, aiohttp, dask, asyncio_tcp_ssl, tomli_loads, xml_etree_iterparse, xml_etree_parse, async_tree_eager_cpu_io_mixed, html5lib, sympy_integrate, pylint, logging_simple, pickle_dict, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed_tg, async_tree_none, bench_thread_pool, scimark_fft, pidigits, deepcopy_memo, pprint_pformat, nqueens, asyncio_websockets, sqlglot_transpile, json_dumps, deltablue, 2to3, typing_runtime_protocols, async_tree_eager, go, sqlglot_normalize, async_tree_eager_io_tg, async_tree_none_tg, async_generators, pickle_pure_python, sqlglot_optimize, sympy_str, async_tree_memoization_tg, mako, async_tree_memoization, crypto_pyaes, unpack_sequence, async_tree_eager_memoization, float, async_tree_cpu_io_mixed, pathlib, mypy2, xml_etree_process, sqlite_synth, comprehensions, deepcopy_reduce, bench_mp_pool


# HPT report

- Reliability score: 92.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 0.99x