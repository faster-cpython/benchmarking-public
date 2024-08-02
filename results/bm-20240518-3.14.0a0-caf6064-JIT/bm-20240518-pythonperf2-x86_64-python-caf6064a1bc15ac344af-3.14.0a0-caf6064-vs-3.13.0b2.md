# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.05x slower
- HPT reliability: 97.49%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 306 ms: 1.05x slower                                                        |
| chameleon      | 7.40 ms                                                          | 8.00 ms: 1.08x slower                                                       |
| docutils       | 2.98 sec                                                         | 3.15 sec: 1.06x slower                                                      |
| html5lib       | 74.7 ms                                                          | 72.8 ms: 1.03x faster                                                       |
| tornado_http   | 119 ms                                                           | 124 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                            | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|---------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none           | 365 ms                                                           | 374 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 621 ms: 1.03x slower                                                        |
| async_tree_memoization_tg | 421 ms                                                           | 453 ms: 1.08x slower                                                        |
| Geometric mean            | (ref)                                                            | 1.02x slower                                                                |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 73.6 ms: 1.09x faster                                                       |
| nbody          | 87.8 ms                                                          | 82.6 ms: 1.06x faster                                                       |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 239 ms: 1.04x faster                                                        |
| regex_compile  | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.60 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.13 sec: 1.13x faster                                                      |
| unpickle             | 15.7 us                                                          | 14.8 us: 1.06x faster                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 81.4 ms: 1.05x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 214 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 99.6 ms: 1.03x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 58.3 ms: 1.03x faster                                                       |
| json_loads           | 25.0 us                                                          | 24.5 us: 1.02x faster                                                       |
| pickle_dict          | 32.8 us                                                          | 32.2 us: 1.02x faster                                                       |
| json_dumps           | 10.8 ms                                                          | 10.6 ms: 1.02x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 143 ms: 1.01x faster                                                        |
| pickle               | 10.6 us                                                          | 10.9 us: 1.03x slower                                                       |
| unpickle_list        | 4.70 us                                                          | 4.88 us: 1.04x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 321 us: 1.04x slower                                                        |
| pickle_list          | 4.44 us                                                          | 4.68 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.02x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.43 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.04x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.11 ms: 1.14x faster                                                       |
| django_template | 39.0 ms                                                          | 43.4 ms: 1.11x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 29.3 ms: 1.13x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 68.7 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.07x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|---------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| spectral_norm             | 97.3 ms                                                          | 83.0 ms: 1.17x faster                                                       |
| richards                  | 53.4 ms                                                          | 46.0 ms: 1.16x faster                                                       |
| richards_super            | 61.2 ms                                                          | 52.7 ms: 1.16x faster                                                       |
| mako                      | 10.4 ms                                                          | 9.11 ms: 1.14x faster                                                       |
| tomli_loads               | 2.40 sec                                                         | 2.13 sec: 1.13x faster                                                      |
| float                     | 80.2 ms                                                          | 73.6 ms: 1.09x faster                                                       |
| scimark_fft               | 312 ms                                                           | 289 ms: 1.08x faster                                                        |
| nbody                     | 87.8 ms                                                          | 82.6 ms: 1.06x faster                                                       |
| unpickle                  | 15.7 us                                                          | 14.8 us: 1.06x faster                                                       |
| scimark_sparse_mat_mult   | 4.28 ms                                                          | 4.06 ms: 1.05x faster                                                       |
| gc_traversal              | 4.69 ms                                                          | 4.45 ms: 1.05x faster                                                       |
| pathlib                   | 17.1 ms                                                          | 16.2 ms: 1.05x faster                                                       |
| xml_etree_generate        | 85.7 ms                                                          | 81.4 ms: 1.05x faster                                                       |
| unpickle_pure_python      | 224 us                                                           | 214 us: 1.05x faster                                                        |
| regex_dna                 | 249 ms                                                           | 239 ms: 1.04x faster                                                        |
| crypto_pyaes              | 73.6 ms                                                          | 70.6 ms: 1.04x faster                                                       |
| coverage                  | 83.5 ms                                                          | 80.6 ms: 1.04x faster                                                       |
| pprint_safe_repr          | 818 ms                                                           | 790 ms: 1.03x faster                                                        |
| json                      | 5.35 ms                                                          | 5.18 ms: 1.03x faster                                                       |
| coroutines                | 22.0 ms                                                          | 21.3 ms: 1.03x faster                                                       |
| xml_etree_iterparse       | 103 ms                                                           | 99.6 ms: 1.03x faster                                                       |
| pyflate                   | 482 ms                                                           | 470 ms: 1.03x faster                                                        |
| html5lib                  | 74.7 ms                                                          | 72.8 ms: 1.03x faster                                                       |
| xml_etree_process         | 59.7 ms                                                          | 58.3 ms: 1.03x faster                                                       |
| regex_compile             | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| json_loads                | 25.0 us                                                          | 24.5 us: 1.02x faster                                                       |
| create_gc_cycles          | 2.00 ms                                                          | 1.96 ms: 1.02x faster                                                       |
| deepcopy_memo             | 37.3 us                                                          | 36.6 us: 1.02x faster                                                       |
| pickle_dict               | 32.8 us                                                          | 32.2 us: 1.02x faster                                                       |
| json_dumps                | 10.8 ms                                                          | 10.6 ms: 1.02x faster                                                       |
| pprint_pformat            | 1.66 sec                                                         | 1.63 sec: 1.02x faster                                                      |
| asyncio_websockets        | 395 ms                                                           | 389 ms: 1.01x faster                                                        |
| pidigits                  | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| go                        | 165 ms                                                           | 164 ms: 1.01x faster                                                        |
| fannkuch                  | 353 ms                                                           | 350 ms: 1.01x faster                                                        |
| xml_etree_parse           | 144 ms                                                           | 143 ms: 1.01x faster                                                        |
| asyncio_tcp               | 378 ms                                                           | 375 ms: 1.01x faster                                                        |
| python_startup            | 13.2 ms                                                          | 13.4 ms: 1.02x slower                                                       |
| async_tree_none           | 365 ms                                                           | 374 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 621 ms: 1.03x slower                                                        |
| pickle                    | 10.6 us                                                          | 10.9 us: 1.03x slower                                                       |
| sqlglot_parse             | 1.39 ms                                                          | 1.44 ms: 1.03x slower                                                       |
| thrift                    | 880 us                                                           | 910 us: 1.03x slower                                                        |
| unpickle_list             | 4.70 us                                                          | 4.88 us: 1.04x slower                                                       |
| tornado_http              | 119 ms                                                           | 124 ms: 1.04x slower                                                        |
| generators                | 33.5 ms                                                          | 34.9 ms: 1.04x slower                                                       |
| meteor_contest            | 128 ms                                                           | 134 ms: 1.04x slower                                                        |
| pycparser                 | 1.22 sec                                                         | 1.27 sec: 1.04x slower                                                      |
| pickle_pure_python        | 307 us                                                           | 321 us: 1.04x slower                                                        |
| sqlglot_transpile         | 1.76 ms                                                          | 1.85 ms: 1.05x slower                                                       |
| logging_format            | 7.11 us                                                          | 7.47 us: 1.05x slower                                                       |
| 2to3                      | 291 ms                                                           | 306 ms: 1.05x slower                                                        |
| dask                      | 391 ms                                                           | 411 ms: 1.05x slower                                                        |
| hexiom                    | 6.35 ms                                                          | 6.68 ms: 1.05x slower                                                       |
| pickle_list               | 4.44 us                                                          | 4.68 us: 1.05x slower                                                       |
| comprehensions            | 17.0 us                                                          | 17.9 us: 1.06x slower                                                       |
| docutils                  | 2.98 sec                                                         | 3.15 sec: 1.06x slower                                                      |
| logging_simple            | 6.40 us                                                          | 6.76 us: 1.06x slower                                                       |
| mdp                       | 2.46 sec                                                         | 2.60 sec: 1.06x slower                                                      |
| regex_effbot              | 3.40 ms                                                          | 3.60 ms: 1.06x slower                                                       |
| flaskblogging             | 4.68 ms                                                          | 4.96 ms: 1.06x slower                                                       |
| bench_thread_pool         | 908 us                                                           | 963 us: 1.06x slower                                                        |
| python_startup_no_site    | 8.85 ms                                                          | 9.43 ms: 1.07x slower                                                       |
| sympy_expand              | 501 ms                                                           | 535 ms: 1.07x slower                                                        |
| sympy_str                 | 295 ms                                                           | 315 ms: 1.07x slower                                                        |
| async_tree_memoization_tg | 421 ms                                                           | 453 ms: 1.08x slower                                                        |
| chameleon                 | 7.40 ms                                                          | 8.00 ms: 1.08x slower                                                       |
| sqlglot_normalize         | 120 ms                                                           | 130 ms: 1.08x slower                                                        |
| deepcopy_reduce           | 3.39 us                                                          | 3.67 us: 1.08x slower                                                       |
| sqlglot_optimize          | 59.5 ms                                                          | 64.4 ms: 1.08x slower                                                       |
| sympy_sum                 | 155 ms                                                           | 168 ms: 1.09x slower                                                        |
| logging_silent            | 96.3 ns                                                          | 105 ns: 1.09x slower                                                        |
| raytrace                  | 260 ms                                                           | 284 ms: 1.09x slower                                                        |
| typing_runtime_protocols  | 171 us                                                           | 186 us: 1.09x slower                                                        |
| async_generators          | 363 ms                                                           | 396 ms: 1.09x slower                                                        |
| scimark_sor               | 119 ms                                                           | 130 ms: 1.09x slower                                                        |
| nqueens                   | 88.4 ms                                                          | 97.4 ms: 1.10x slower                                                       |
| chaos                     | 59.6 ms                                                          | 66.1 ms: 1.11x slower                                                       |
| django_template           | 39.0 ms                                                          | 43.4 ms: 1.11x slower                                                       |
| sympy_integrate           | 23.2 ms                                                          | 26.0 ms: 1.12x slower                                                       |
| deepcopy                  | 377 us                                                           | 424 us: 1.12x slower                                                        |
| deltablue                 | 3.37 ms                                                          | 3.79 ms: 1.12x slower                                                       |
| pylint                    | 339 ms                                                           | 383 ms: 1.13x slower                                                        |
| genshi_text               | 25.9 ms                                                          | 29.3 ms: 1.13x slower                                                       |
| scimark_lu                | 97.5 ms                                                          | 115 ms: 1.18x slower                                                        |
| genshi_xml                | 58.1 ms                                                          | 68.7 ms: 1.18x slower                                                       |
| telco                     | 8.40 ms                                                          | 174 ms: 20.67x slower                                                       |
| Geometric mean            | (ref)                                                            | 1.05x slower                                                                |

Benchmark hidden because not significant (11): bench_mp_pool, async_tree_io_tg, scimark_monte_carlo, regex_v8, async_tree_io, asyncio_tcp_ssl, dulwich_log, sqlite_synth, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 97.49% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x