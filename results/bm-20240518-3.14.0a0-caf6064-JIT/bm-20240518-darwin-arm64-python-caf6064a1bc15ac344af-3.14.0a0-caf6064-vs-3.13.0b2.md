# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: darwin-arm64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.61x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 192 ms: 1.19x slower                                                  |
| chameleon      | 4.27 ms                                                    | 4.45 ms: 1.04x slower                                                 |
| docutils       | 1.44 sec                                                   | 1.52 sec: 1.05x slower                                                |
| html5lib       | 31.2 ms                                                    | 30.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.06x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 333 ms: 1.01x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.7 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 63.1 ms: 1.05x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (12): async_tree_eager_io, async_tree_eager_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io, async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_none, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 47.5 ms: 1.02x faster                                                 |
| pidigits       | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| nbody          | 59.6 ms                                                    | 63.5 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.58 ms: 1.00x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 17.4 ms: 1.00x slower                                                 |
| regex_compile  | 68.5 ms                                                    | 72.5 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                |
| unpickle_pure_python | 141 us                                                     | 131 us: 1.07x faster                                                  |
| xml_etree_process    | 37.1 ms                                                    | 35.3 ms: 1.05x faster                                                 |
| pickle_pure_python   | 179 us                                                     | 172 us: 1.04x faster                                                  |
| xml_etree_generate   | 52.7 ms                                                    | 50.8 ms: 1.04x faster                                                 |
| xml_etree_parse      | 106 ms                                                     | 102 ms: 1.04x faster                                                  |
| json_dumps           | 6.23 ms                                                    | 6.10 ms: 1.02x faster                                                 |
| pickle_list          | 2.96 us                                                    | 2.92 us: 1.01x faster                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 71.1 ms: 1.01x faster                                                 |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.00x faster                                                 |
| json_loads           | 16.8 us                                                    | 17.1 us: 1.01x slower                                                 |
| unpickle             | 9.12 us                                                    | 9.39 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                          |

Benchmark hidden because not significant (2): pickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.3 ms: 1.01x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 12.8 ms: 1.04x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.03x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.38 ms: 1.09x faster                                                 |
| django_template | 19.4 ms                                                    | 21.0 ms: 1.08x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 17.0 ms: 1.22x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 40.4 ms: 1.35x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.13x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads                      | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                |
| mako                             | 6.99 ms                                                    | 6.38 ms: 1.09x faster                                                 |
| unpickle_pure_python             | 141 us                                                     | 131 us: 1.07x faster                                                  |
| fannkuch                         | 248 ms                                                     | 235 ms: 1.06x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 21.5 us: 1.05x faster                                                 |
| xml_etree_process                | 37.1 ms                                                    | 35.3 ms: 1.05x faster                                                 |
| pickle_pure_python               | 179 us                                                     | 172 us: 1.04x faster                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 50.8 ms: 1.04x faster                                                 |
| xml_etree_parse                  | 106 ms                                                     | 102 ms: 1.04x faster                                                  |
| pathlib                          | 23.3 ms                                                    | 22.7 ms: 1.03x faster                                                 |
| float                            | 48.6 ms                                                    | 47.5 ms: 1.02x faster                                                 |
| flaskblogging                    | 3.61 ms                                                    | 3.53 ms: 1.02x faster                                                 |
| pyflate                          | 321 ms                                                     | 314 ms: 1.02x faster                                                  |
| json_dumps                       | 6.23 ms                                                    | 6.10 ms: 1.02x faster                                                 |
| pickle_list                      | 2.96 us                                                    | 2.92 us: 1.01x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.81 us: 1.01x faster                                                 |
| html5lib                         | 31.2 ms                                                    | 30.9 ms: 1.01x faster                                                 |
| xml_etree_iterparse              | 71.5 ms                                                    | 71.1 ms: 1.01x faster                                                 |
| thrift                           | 435 us                                                     | 434 us: 1.00x faster                                                  |
| logging_simple                   | 3.04 us                                                    | 3.03 us: 1.00x faster                                                 |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.00x faster                                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.58 ms: 1.00x faster                                                 |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 17.4 ms: 1.00x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 333 ms: 1.01x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 15.9 ms: 1.01x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.7 ms: 1.01x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 15.3 ms: 1.01x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 955 ms: 1.01x slower                                                  |
| telco                            | 4.60 ms                                                    | 4.65 ms: 1.01x slower                                                 |
| richards                         | 31.8 ms                                                    | 32.2 ms: 1.01x slower                                                 |
| sqlite_synth                     | 1.55 us                                                    | 1.57 us: 1.01x slower                                                 |
| generators                       | 22.9 ms                                                    | 23.2 ms: 1.01x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.1 us: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 67.2 ms: 1.01x slower                                                 |
| coverage                         | 45.0 ms                                                    | 45.7 ms: 1.02x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 184 ms: 1.02x slower                                                  |
| go                               | 101 ms                                                     | 103 ms: 1.03x slower                                                  |
| create_gc_cycles                 | 897 us                                                     | 920 us: 1.03x slower                                                  |
| richards_super                   | 35.2 ms                                                    | 36.2 ms: 1.03x slower                                                 |
| unpickle                         | 9.12 us                                                    | 9.39 us: 1.03x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 72.5 ms: 1.03x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 62.1 ns: 1.03x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 49.0 ms: 1.04x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 12.8 ms: 1.04x slower                                                 |
| chameleon                        | 4.27 ms                                                    | 4.45 ms: 1.04x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 44.3 ms: 1.04x slower                                                 |
| sympy_sum                        | 69.2 ms                                                    | 72.3 ms: 1.05x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.90 ms: 1.05x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 63.1 ms: 1.05x slower                                                 |
| sympy_str                        | 131 ms                                                     | 138 ms: 1.05x slower                                                  |
| async_generators                 | 281 ms                                                     | 294 ms: 1.05x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 51.9 ms: 1.05x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 237 ms: 1.05x slower                                                  |
| scimark_sor                      | 94.9 ms                                                    | 99.9 ms: 1.05x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 10.9 ms: 1.05x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.52 sec: 1.05x slower                                                |
| typing_runtime_protocols         | 87.6 us                                                    | 92.5 us: 1.06x slower                                                 |
| mdp                              | 1.53 sec                                                   | 1.62 sec: 1.06x slower                                                |
| regex_compile                    | 68.5 ms                                                    | 72.5 ms: 1.06x slower                                                 |
| pycparser                        | 632 ms                                                     | 671 ms: 1.06x slower                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.61 ms: 1.06x slower                                                 |
| nbody                            | 59.6 ms                                                    | 63.5 ms: 1.07x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 33.0 ms: 1.07x slower                                                 |
| pylint                           | 170 ms                                                     | 183 ms: 1.08x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 482 us: 1.08x slower                                                  |
| django_template                  | 19.4 ms                                                    | 21.0 ms: 1.08x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.43 ms: 1.09x slower                                                 |
| raytrace                         | 147 ms                                                     | 161 ms: 1.10x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 57.4 ms: 1.10x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 1.01 ms: 1.13x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 833 us: 1.14x slower                                                  |
| chaos                            | 34.0 ms                                                    | 39.2 ms: 1.15x slower                                                 |
| deltablue                        | 2.14 ms                                                    | 2.48 ms: 1.16x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 78.6 ms: 1.18x slower                                                 |
| 2to3                             | 161 ms                                                     | 192 ms: 1.19x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 12.3 us: 1.21x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 17.0 ms: 1.22x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 40.4 ms: 1.35x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.03x slower                                                          |

Benchmark hidden because not significant (24): async_tree_eager_io, pickle, asyncio_websockets, logging_format, unpickle_list, regex_dna, asyncio_tcp_ssl, json, deepcopy, pprint_safe_repr, async_tree_eager_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, dask, async_tree_memoization, async_tree_io, async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_none, tornado_http, async_tree_eager_memoization, asyncio_tcp
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, dulwich_log, gunicorn, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.61x