# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.03x slower
- HPT reliability: 90.24%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 289 ms: 1.01x faster                                                        |
| chameleon      | 7.40 ms                                                          | 7.29 ms: 1.01x faster                                                       |
| docutils       | 2.98 sec                                                         | 2.99 sec: 1.00x slower                                                      |
| html5lib       | 74.7 ms                                                          | 74.3 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|---------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg          | 900 ms                                                           | 885 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 615 ms: 1.02x slower                                                        |
| async_tree_memoization_tg | 421 ms                                                           | 441 ms: 1.05x slower                                                        |
| Geometric mean            | (ref)                                                            | 1.01x slower                                                                |

Benchmark hidden because not significant (5): async_tree_io, async_tree_none_tg, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                                       |
| regex_dna      | 249 ms                                                           | 246 ms: 1.01x faster                                                        |
| regex_compile  | 144 ms                                                           | 143 ms: 1.01x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.70 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 30.7 us: 1.07x faster                                                       |
| unpickle             | 15.7 us                                                          | 14.7 us: 1.07x faster                                                       |
| json_loads           | 25.0 us                                                          | 24.5 us: 1.02x faster                                                       |
| tomli_loads          | 2.40 sec                                                         | 2.35 sec: 1.02x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 84.6 ms: 1.01x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 222 us: 1.01x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                       |
| pickle               | 10.6 us                                                          | 10.5 us: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 142 ms: 1.01x faster                                                        |
| unpickle_list        | 4.70 us                                                          | 4.77 us: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 313 us: 1.02x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 105 ms: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (2): pickle_list, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 12.8 ms: 1.03x faster                                                       |
| python_startup_no_site | 8.85 ms                                                          | 8.82 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 55.9 ms: 1.04x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 25.4 ms: 1.02x faster                                                       |
| mako            | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                                       |
| django_template | 39.0 ms                                                          | 39.4 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|---------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| bench_mp_pool             | 4.91 ms                                                          | 4.53 ms: 1.08x faster                                                       |
| coverage                  | 83.5 ms                                                          | 77.7 ms: 1.07x faster                                                       |
| pickle_dict               | 32.8 us                                                          | 30.7 us: 1.07x faster                                                       |
| unpickle                  | 15.7 us                                                          | 14.7 us: 1.07x faster                                                       |
| gc_traversal              | 4.69 ms                                                          | 4.40 ms: 1.07x faster                                                       |
| scimark_fft               | 312 ms                                                           | 295 ms: 1.06x faster                                                        |
| pathlib                   | 17.1 ms                                                          | 16.2 ms: 1.06x faster                                                       |
| scimark_sparse_mat_mult   | 4.28 ms                                                          | 4.12 ms: 1.04x faster                                                       |
| genshi_xml                | 58.1 ms                                                          | 55.9 ms: 1.04x faster                                                       |
| richards                  | 53.4 ms                                                          | 51.6 ms: 1.04x faster                                                       |
| richards_super            | 61.2 ms                                                          | 59.2 ms: 1.03x faster                                                       |
| coroutines                | 22.0 ms                                                          | 21.3 ms: 1.03x faster                                                       |
| python_startup            | 13.2 ms                                                          | 12.8 ms: 1.03x faster                                                       |
| json_loads                | 25.0 us                                                          | 24.5 us: 1.02x faster                                                       |
| tomli_loads               | 2.40 sec                                                         | 2.35 sec: 1.02x faster                                                      |
| genshi_text               | 25.9 ms                                                          | 25.4 ms: 1.02x faster                                                       |
| crypto_pyaes              | 73.6 ms                                                          | 72.1 ms: 1.02x faster                                                       |
| scimark_monte_carlo       | 65.5 ms                                                          | 64.2 ms: 1.02x faster                                                       |
| logging_format            | 7.11 us                                                          | 6.97 us: 1.02x faster                                                       |
| async_tree_io_tg          | 900 ms                                                           | 885 ms: 1.02x faster                                                        |
| regex_v8                  | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                                       |
| chameleon                 | 7.40 ms                                                          | 7.29 ms: 1.01x faster                                                       |
| xml_etree_generate        | 85.7 ms                                                          | 84.6 ms: 1.01x faster                                                       |
| unpickle_pure_python      | 224 us                                                           | 222 us: 1.01x faster                                                        |
| regex_dna                 | 249 ms                                                           | 246 ms: 1.01x faster                                                        |
| asyncio_websockets        | 395 ms                                                           | 390 ms: 1.01x faster                                                        |
| json_dumps                | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                       |
| regex_compile             | 144 ms                                                           | 143 ms: 1.01x faster                                                        |
| pickle                    | 10.6 us                                                          | 10.5 us: 1.01x faster                                                       |
| pprint_safe_repr          | 818 ms                                                           | 810 ms: 1.01x faster                                                        |
| spectral_norm             | 97.3 ms                                                          | 96.4 ms: 1.01x faster                                                       |
| asyncio_tcp               | 378 ms                                                           | 374 ms: 1.01x faster                                                        |
| xml_etree_parse           | 144 ms                                                           | 142 ms: 1.01x faster                                                        |
| 2to3                      | 291 ms                                                           | 289 ms: 1.01x faster                                                        |
| logging_simple            | 6.40 us                                                          | 6.37 us: 1.01x faster                                                       |
| html5lib                  | 74.7 ms                                                          | 74.3 ms: 1.00x faster                                                       |
| pidigits                  | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| python_startup_no_site    | 8.85 ms                                                          | 8.82 ms: 1.00x faster                                                       |
| hexiom                    | 6.35 ms                                                          | 6.33 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl           | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                      |
| pyflate                   | 482 ms                                                           | 483 ms: 1.00x slower                                                        |
| docutils                  | 2.98 sec                                                         | 2.99 sec: 1.00x slower                                                      |
| generators                | 33.5 ms                                                          | 33.7 ms: 1.00x slower                                                       |
| sqlglot_optimize          | 59.5 ms                                                          | 60.1 ms: 1.01x slower                                                       |
| dulwich_log               | 67.3 ms                                                          | 67.9 ms: 1.01x slower                                                       |
| mako                      | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                                       |
| comprehensions            | 17.0 us                                                          | 17.1 us: 1.01x slower                                                       |
| deltablue                 | 3.37 ms                                                          | 3.41 ms: 1.01x slower                                                       |
| json                      | 5.35 ms                                                          | 5.42 ms: 1.01x slower                                                       |
| sympy_expand              | 501 ms                                                           | 507 ms: 1.01x slower                                                        |
| django_template           | 39.0 ms                                                          | 39.4 ms: 1.01x slower                                                       |
| sympy_integrate           | 23.2 ms                                                          | 23.5 ms: 1.01x slower                                                       |
| sympy_str                 | 295 ms                                                           | 298 ms: 1.01x slower                                                        |
| logging_silent            | 96.3 ns                                                          | 97.6 ns: 1.01x slower                                                       |
| fannkuch                  | 353 ms                                                           | 358 ms: 1.01x slower                                                        |
| unpickle_list             | 4.70 us                                                          | 4.77 us: 1.01x slower                                                       |
| sqlite_synth              | 2.80 us                                                          | 2.84 us: 1.02x slower                                                       |
| meteor_contest            | 128 ms                                                           | 130 ms: 1.02x slower                                                        |
| deepcopy_reduce           | 3.39 us                                                          | 3.44 us: 1.02x slower                                                       |
| mdp                       | 2.46 sec                                                         | 2.50 sec: 1.02x slower                                                      |
| sqlglot_parse             | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                       |
| scimark_lu                | 97.5 ms                                                          | 99.2 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 615 ms: 1.02x slower                                                        |
| pickle_pure_python        | 307 us                                                           | 313 us: 1.02x slower                                                        |
| deepcopy                  | 377 us                                                           | 384 us: 1.02x slower                                                        |
| sqlglot_normalize         | 120 ms                                                           | 123 ms: 1.02x slower                                                        |
| sqlglot_transpile         | 1.76 ms                                                          | 1.80 ms: 1.02x slower                                                       |
| xml_etree_iterparse       | 103 ms                                                           | 105 ms: 1.02x slower                                                        |
| deepcopy_memo             | 37.3 us                                                          | 38.2 us: 1.02x slower                                                       |
| thrift                    | 880 us                                                           | 904 us: 1.03x slower                                                        |
| async_generators          | 363 ms                                                           | 373 ms: 1.03x slower                                                        |
| go                        | 165 ms                                                           | 170 ms: 1.03x slower                                                        |
| typing_runtime_protocols  | 171 us                                                           | 177 us: 1.04x slower                                                        |
| pycparser                 | 1.22 sec                                                         | 1.27 sec: 1.04x slower                                                      |
| nqueens                   | 88.4 ms                                                          | 92.2 ms: 1.04x slower                                                       |
| async_tree_memoization_tg | 421 ms                                                           | 441 ms: 1.05x slower                                                        |
| raytrace                  | 260 ms                                                           | 276 ms: 1.06x slower                                                        |
| regex_effbot              | 3.40 ms                                                          | 3.70 ms: 1.09x slower                                                       |
| scimark_sor               | 119 ms                                                           | 138 ms: 1.16x slower                                                        |
| telco                     | 8.40 ms                                                          | 170 ms: 20.22x slower                                                       |
| Geometric mean            | (ref)                                                            | 1.03x slower                                                                |

Benchmark hidden because not significant (18): async_tree_io, bench_thread_pool, tornado_http, async_tree_none_tg, float, pprint_pformat, pickle_list, nbody, xml_etree_process, async_tree_none, sympy_sum, chaos, flaskblogging, dask, pylint, async_tree_memoization, create_gc_cycles, async_tree_cpu_io_mixed_tg
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 90.24% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x