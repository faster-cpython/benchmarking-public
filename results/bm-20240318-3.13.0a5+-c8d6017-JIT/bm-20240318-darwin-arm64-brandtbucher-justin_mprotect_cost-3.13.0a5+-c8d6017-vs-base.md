# Results vs. base

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: darwin-arm64
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.00x slower
- HPT reliability: 90.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 187 ms                                                                 | 188 ms: 1.01x slower                                                         |
| chameleon      | 4.87 ms                                                                | 4.82 ms: 1.01x faster                                                        |
| docutils       | 1.53 sec                                                               | 1.54 sec: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                    | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_eager             | 70.4 ms                                                                | 69.6 ms: 1.01x faster                                                        |
| async_tree_eager_tg          | 47.4 ms                                                                | 47.0 ms: 1.01x faster                                                        |
| async_tree_io                | 710 ms                                                                 | 706 ms: 1.00x faster                                                         |
| async_tree_eager_memoization | 173 ms                                                                 | 173 ms: 1.00x faster                                                         |
| Geometric mean               | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (12): async_tree_eager_cpu_io_mixed_tg, async_tree_memoization, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_none, async_tree_memoization_tg, async_tree_io_tg, async_tree_eager_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 283 ms                                                                 | 282 ms: 1.00x faster                                                         |
| nbody          | 70.2 ms                                                                | 70.8 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 17.2 ms                                                                | 17.2 ms: 1.00x faster                                                        |
| regex_effbot   | 2.63 ms                                                                | 2.63 ms: 1.00x faster                                                        |
| regex_compile  | 84.9 ms                                                                | 85.4 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle             | 9.19 us                                                                | 9.15 us: 1.00x faster                                                        |
| pickle_dict          | 18.2 us                                                                | 18.2 us: 1.00x faster                                                        |
| xml_etree_process    | 39.0 ms                                                                | 39.0 ms: 1.00x slower                                                        |
| unpickle_pure_python | 150 us                                                                 | 151 us: 1.00x slower                                                         |
| xml_etree_parse      | 105 ms                                                                 | 106 ms: 1.01x slower                                                         |
| json_dumps           | 6.47 ms                                                                | 6.53 ms: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (8): pickle_pure_python, json_loads, pickle, pickle_list, xml_etree_generate, xml_etree_iterparse, tomli_loads, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 18.5 ms                                                                | 20.6 ms: 1.12x slower                                                        |
| python_startup_no_site | 16.7 ms                                                                | 18.9 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.12x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 21.9 ms                                                                | 22.1 ms: 1.01x slower                                                        |
| genshi_xml      | 36.9 ms                                                                | 37.7 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                    | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_reduce              | 2.00 us                                                                | 1.98 us: 1.01x faster                                                        |
| chameleon                    | 4.87 ms                                                                | 4.82 ms: 1.01x faster                                                        |
| async_tree_eager             | 70.4 ms                                                                | 69.6 ms: 1.01x faster                                                        |
| pprint_safe_repr             | 519 ms                                                                 | 515 ms: 1.01x faster                                                         |
| async_tree_eager_tg          | 47.4 ms                                                                | 47.0 ms: 1.01x faster                                                        |
| logging_format               | 3.79 us                                                                | 3.76 us: 1.01x faster                                                        |
| coverage                     | 47.9 ms                                                                | 47.6 ms: 1.01x faster                                                        |
| nqueens                      | 64.2 ms                                                                | 63.7 ms: 1.01x faster                                                        |
| chaos                        | 40.4 ms                                                                | 40.1 ms: 1.01x faster                                                        |
| deepcopy                     | 231 us                                                                 | 229 us: 1.01x faster                                                         |
| sympy_expand                 | 249 ms                                                                 | 247 ms: 1.01x faster                                                         |
| async_tree_io                | 710 ms                                                                 | 706 ms: 1.00x faster                                                         |
| pprint_pformat               | 1.06 sec                                                               | 1.06 sec: 1.00x faster                                                       |
| unpickle                     | 9.19 us                                                                | 9.15 us: 1.00x faster                                                        |
| async_tree_eager_memoization | 173 ms                                                                 | 173 ms: 1.00x faster                                                         |
| sympy_str                    | 145 ms                                                                 | 145 ms: 1.00x faster                                                         |
| pickle_dict                  | 18.2 us                                                                | 18.2 us: 1.00x faster                                                        |
| pidigits                     | 283 ms                                                                 | 282 ms: 1.00x faster                                                         |
| generators                   | 28.5 ms                                                                | 28.4 ms: 1.00x faster                                                        |
| scimark_fft                  | 200 ms                                                                 | 199 ms: 1.00x faster                                                         |
| bench_thread_pool            | 514 us                                                                 | 512 us: 1.00x faster                                                         |
| thrift                       | 461 us                                                                 | 460 us: 1.00x faster                                                         |
| regex_v8                     | 17.2 ms                                                                | 17.2 ms: 1.00x faster                                                        |
| regex_effbot                 | 2.63 ms                                                                | 2.63 ms: 1.00x faster                                                        |
| meteor_contest               | 75.2 ms                                                                | 75.3 ms: 1.00x slower                                                        |
| xml_etree_process            | 39.0 ms                                                                | 39.0 ms: 1.00x slower                                                        |
| sqlglot_optimize             | 35.4 ms                                                                | 35.5 ms: 1.00x slower                                                        |
| go                           | 115 ms                                                                 | 115 ms: 1.00x slower                                                         |
| crypto_pyaes                 | 47.7 ms                                                                | 47.9 ms: 1.00x slower                                                        |
| sqlglot_normalize            | 182 ms                                                                 | 183 ms: 1.00x slower                                                         |
| unpickle_pure_python         | 150 us                                                                 | 151 us: 1.00x slower                                                         |
| docutils                     | 1.53 sec                                                               | 1.54 sec: 1.00x slower                                                       |
| richards                     | 37.5 ms                                                                | 37.7 ms: 1.00x slower                                                        |
| comprehensions               | 12.6 us                                                                | 12.7 us: 1.01x slower                                                        |
| regex_compile                | 84.9 ms                                                                | 85.4 ms: 1.01x slower                                                        |
| scimark_monte_carlo          | 44.2 ms                                                                | 44.5 ms: 1.01x slower                                                        |
| sqlite_synth                 | 1.58 us                                                                | 1.59 us: 1.01x slower                                                        |
| 2to3                         | 187 ms                                                                 | 188 ms: 1.01x slower                                                         |
| nbody                        | 70.2 ms                                                                | 70.8 ms: 1.01x slower                                                        |
| fannkuch                     | 311 ms                                                                 | 314 ms: 1.01x slower                                                         |
| xml_etree_parse              | 105 ms                                                                 | 106 ms: 1.01x slower                                                         |
| json_dumps                   | 6.47 ms                                                                | 6.53 ms: 1.01x slower                                                        |
| django_template              | 21.9 ms                                                                | 22.1 ms: 1.01x slower                                                        |
| mdp                          | 1.62 sec                                                               | 1.64 sec: 1.01x slower                                                       |
| sqlglot_parse                | 831 us                                                                 | 840 us: 1.01x slower                                                         |
| scimark_sor                  | 111 ms                                                                 | 113 ms: 1.01x slower                                                         |
| pyflate                      | 343 ms                                                                 | 348 ms: 1.02x slower                                                         |
| richards_super               | 41.5 ms                                                                | 42.1 ms: 1.02x slower                                                        |
| spectral_norm                | 74.8 ms                                                                | 76.0 ms: 1.02x slower                                                        |
| coroutines                   | 18.1 ms                                                                | 18.4 ms: 1.02x slower                                                        |
| genshi_xml                   | 36.9 ms                                                                | 37.7 ms: 1.02x slower                                                        |
| bench_mp_pool                | 53.2 ms                                                                | 56.1 ms: 1.06x slower                                                        |
| python_startup               | 18.5 ms                                                                | 20.6 ms: 1.12x slower                                                        |
| python_startup_no_site       | 16.7 ms                                                                | 18.9 ms: 1.13x slower                                                        |
| Geometric mean               | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (55): unpack_sequence, sympy_sum, json, aiohttp, dask, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization, async_tree_eager_cpu_io_mixed, mypy2, asyncio_tcp_ssl, async_tree_eager_memoization_tg, gc_traversal, mako, logging_simple, async_tree_cpu_io_mixed_tg, async_tree_eager_io, pickle_pure_python, json_loads, hexiom, async_tree_cpu_io_mixed, scimark_sparse_mat_mult, async_tree_none_tg, typing_runtime_protocols, scimark_lu, pickle, async_tree_none, pycparser, sympy_integrate, genshi_text, asyncio_websockets, create_gc_cycles, async_tree_memoization_tg, telco, async_tree_io_tg, dulwich_log, logging_silent, pickle_list, deepcopy_memo, regex_dna, pathlib, raytrace, xml_etree_generate, float, deltablue, xml_etree_iterparse, html5lib, tomli_loads, pylint, async_generators, unpickle_list, sqlglot_transpile, async_tree_eager_io_tg, gunicorn, asyncio_tcp, tornado_http


# HPT report

- Reliability score: 90.50% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.00x