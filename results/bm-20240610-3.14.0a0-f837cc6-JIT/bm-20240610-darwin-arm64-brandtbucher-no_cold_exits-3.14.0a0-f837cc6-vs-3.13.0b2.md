# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_cold_exits
- machine: darwin-arm64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.02x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.64x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 168 ms: 1.05x slower                                                 |
| docutils       | 1.44 sec                                                   | 1.50 sec: 1.04x slower                                               |
| html5lib       | 31.2 ms                                                    | 30.7 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                      | 1.02x slower                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.3 ms: 1.02x slower                                                |
| async_tree_eager                 | 60.3 ms                                                    | 64.0 ms: 1.06x slower                                                |
| Geometric mean                   | (ref)                                                      | 1.01x slower                                                         |

Benchmark hidden because not significant (12): async_tree_eager_io_tg, async_tree_io_tg, async_tree_eager_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 47.6 ms: 1.02x faster                                                |
| nbody          | 59.6 ms                                                    | 63.7 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                      | 1.02x slower                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                |
| regex_dna      | 149 ms                                                     | 149 ms: 1.00x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 17.3 ms: 1.00x slower                                                |
| regex_compile  | 68.5 ms                                                    | 73.4 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                      | 1.02x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.26 sec: 1.16x faster                                               |
| unpickle_pure_python | 141 us                                                     | 132 us: 1.07x faster                                                 |
| pickle_pure_python   | 179 us                                                     | 173 us: 1.03x faster                                                 |
| xml_etree_process    | 37.1 ms                                                    | 35.9 ms: 1.03x faster                                                |
| xml_etree_parse      | 106 ms                                                     | 102 ms: 1.03x faster                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 51.2 ms: 1.03x faster                                                |
| xml_etree_iterparse  | 71.5 ms                                                    | 70.1 ms: 1.02x faster                                                |
| pickle               | 7.48 us                                                    | 7.45 us: 1.00x faster                                                |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.00x faster                                                |
| json_loads           | 16.8 us                                                    | 16.9 us: 1.00x slower                                                |
| pickle_list          | 2.96 us                                                    | 2.98 us: 1.01x slower                                                |
| json_dumps           | 6.23 ms                                                    | 6.31 ms: 1.01x slower                                                |
| unpickle             | 9.12 us                                                    | 9.31 us: 1.02x slower                                                |
| unpickle_list        | 2.88 us                                                    | 3.07 us: 1.07x slower                                                |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 14.1 ms: 1.07x faster                                                |
| python_startup_no_site | 12.3 ms                                                    | 11.6 ms: 1.06x faster                                                |
| Geometric mean         | (ref)                                                      | 1.07x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.36 ms: 1.10x faster                                                |
| django_template | 19.4 ms                                                    | 21.4 ms: 1.10x slower                                                |
| genshi_text     | 13.9 ms                                                    | 16.1 ms: 1.16x slower                                                |
| genshi_xml      | 29.9 ms                                                    | 39.6 ms: 1.32x slower                                                |
| Geometric mean  | (ref)                                                      | 1.11x slower                                                         |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads                      | 1.47 sec                                                   | 1.26 sec: 1.16x faster                                               |
| mako                             | 6.99 ms                                                    | 6.36 ms: 1.10x faster                                                |
| pathlib                          | 23.3 ms                                                    | 21.6 ms: 1.08x faster                                                |
| python_startup                   | 15.2 ms                                                    | 14.1 ms: 1.07x faster                                                |
| mdp                              | 1.53 sec                                                   | 1.44 sec: 1.07x faster                                               |
| unpickle_pure_python             | 141 us                                                     | 132 us: 1.07x faster                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 11.6 ms: 1.06x faster                                                |
| deepcopy_memo                    | 22.6 us                                                    | 21.2 us: 1.06x faster                                                |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.23 sec: 1.05x faster                                               |
| richards                         | 31.8 ms                                                    | 30.4 ms: 1.05x faster                                                |
| pickle_pure_python               | 179 us                                                     | 173 us: 1.03x faster                                                 |
| xml_etree_process                | 37.1 ms                                                    | 35.9 ms: 1.03x faster                                                |
| xml_etree_parse                  | 106 ms                                                     | 102 ms: 1.03x faster                                                 |
| richards_super                   | 35.2 ms                                                    | 34.2 ms: 1.03x faster                                                |
| xml_etree_generate               | 52.7 ms                                                    | 51.2 ms: 1.03x faster                                                |
| float                            | 48.6 ms                                                    | 47.6 ms: 1.02x faster                                                |
| xml_etree_iterparse              | 71.5 ms                                                    | 70.1 ms: 1.02x faster                                                |
| html5lib                         | 31.2 ms                                                    | 30.7 ms: 1.02x faster                                                |
| regex_effbot                     | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                |
| telco                            | 4.60 ms                                                    | 4.57 ms: 1.01x faster                                                |
| pickle                           | 7.48 us                                                    | 7.45 us: 1.00x faster                                                |
| pyflate                          | 321 ms                                                     | 320 ms: 1.00x faster                                                 |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.00x faster                                                |
| regex_dna                        | 149 ms                                                     | 149 ms: 1.00x faster                                                 |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                |
| regex_v8                         | 17.3 ms                                                    | 17.3 ms: 1.00x slower                                                |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                 |
| thrift                           | 435 us                                                     | 437 us: 1.00x slower                                                 |
| json_loads                       | 16.8 us                                                    | 16.9 us: 1.00x slower                                                |
| deepcopy_reduce                  | 1.82 us                                                    | 1.83 us: 1.01x slower                                                |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                 |
| pickle_list                      | 2.96 us                                                    | 2.98 us: 1.01x slower                                                |
| spectral_norm                    | 66.4 ms                                                    | 67.2 ms: 1.01x slower                                                |
| fannkuch                         | 248 ms                                                     | 251 ms: 1.01x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.31 ms: 1.01x slower                                                |
| deepcopy                         | 204 us                                                     | 207 us: 1.02x slower                                                 |
| logging_simple                   | 3.04 us                                                    | 3.09 us: 1.02x slower                                                |
| bench_mp_pool                    | 47.2 ms                                                    | 48.0 ms: 1.02x slower                                                |
| coverage                         | 45.0 ms                                                    | 45.9 ms: 1.02x slower                                                |
| generators                       | 22.9 ms                                                    | 23.3 ms: 1.02x slower                                                |
| async_generators                 | 281 ms                                                     | 287 ms: 1.02x slower                                                 |
| unpickle                         | 9.12 us                                                    | 9.31 us: 1.02x slower                                                |
| go                               | 101 ms                                                     | 103 ms: 1.02x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 185 ms: 1.02x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.3 ms: 1.02x slower                                                |
| logging_format                   | 3.31 us                                                    | 3.39 us: 1.02x slower                                                |
| logging_silent                   | 60.1 ns                                                    | 62.3 ns: 1.04x slower                                                |
| scimark_monte_carlo              | 42.5 ms                                                    | 44.0 ms: 1.04x slower                                                |
| pprint_safe_repr                 | 465 ms                                                     | 483 ms: 1.04x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 986 ms: 1.04x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.50 sec: 1.04x slower                                               |
| sympy_sum                        | 69.2 ms                                                    | 72.4 ms: 1.05x slower                                                |
| meteor_contest                   | 70.3 ms                                                    | 73.5 ms: 1.05x slower                                                |
| sympy_str                        | 131 ms                                                     | 138 ms: 1.05x slower                                                 |
| 2to3                             | 161 ms                                                     | 168 ms: 1.05x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 237 ms: 1.05x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.92 ms: 1.05x slower                                                |
| sympy_integrate                  | 10.3 ms                                                    | 10.9 ms: 1.05x slower                                                |
| async_tree_eager                 | 60.3 ms                                                    | 64.0 ms: 1.06x slower                                                |
| scimark_sor                      | 94.9 ms                                                    | 101 ms: 1.06x slower                                                 |
| unpickle_list                    | 2.88 us                                                    | 3.07 us: 1.07x slower                                                |
| crypto_pyaes                     | 49.5 ms                                                    | 52.8 ms: 1.07x slower                                                |
| pycparser                        | 632 ms                                                     | 676 ms: 1.07x slower                                                 |
| nbody                            | 59.6 ms                                                    | 63.7 ms: 1.07x slower                                                |
| regex_compile                    | 68.5 ms                                                    | 73.4 ms: 1.07x slower                                                |
| sqlglot_optimize                 | 30.9 ms                                                    | 33.2 ms: 1.07x slower                                                |
| typing_runtime_protocols         | 87.6 us                                                    | 94.1 us: 1.07x slower                                                |
| bench_thread_pool                | 447 us                                                     | 481 us: 1.08x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 57.1 ms: 1.09x slower                                                |
| hexiom                           | 4.06 ms                                                    | 4.44 ms: 1.10x slower                                                |
| django_template                  | 19.4 ms                                                    | 21.4 ms: 1.10x slower                                                |
| raytrace                         | 147 ms                                                     | 165 ms: 1.12x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 1.01 ms: 1.14x slower                                                |
| sqlglot_parse                    | 732 us                                                     | 840 us: 1.15x slower                                                 |
| deltablue                        | 2.14 ms                                                    | 2.46 ms: 1.15x slower                                                |
| genshi_text                      | 13.9 ms                                                    | 16.1 ms: 1.16x slower                                                |
| chaos                            | 34.0 ms                                                    | 39.5 ms: 1.16x slower                                                |
| scimark_lu                       | 66.9 ms                                                    | 79.4 ms: 1.19x slower                                                |
| comprehensions                   | 10.2 us                                                    | 12.4 us: 1.23x slower                                                |
| genshi_xml                       | 29.9 ms                                                    | 39.6 ms: 1.32x slower                                                |
| Geometric mean                   | (ref)                                                      | 1.02x slower                                                         |

Benchmark hidden because not significant (22): async_tree_eager_io_tg, async_tree_io_tg, async_tree_eager_io, async_tree_memoization_tg, async_tree_none_tg, create_gc_cycles, asyncio_websockets, pidigits, coroutines, async_tree_cpu_io_mixed_tg, sqlite_synth, json, dask, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io, tornado_http, async_tree_none, asyncio_tcp, pylint
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.64x