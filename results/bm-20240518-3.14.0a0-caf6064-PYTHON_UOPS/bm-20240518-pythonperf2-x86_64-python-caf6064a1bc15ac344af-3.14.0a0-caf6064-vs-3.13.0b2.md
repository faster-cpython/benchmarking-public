# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.20x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 343 ms: 1.18x slower                                                        |
| chameleon      | 7.40 ms                                                          | 8.61 ms: 1.16x slower                                                       |
| docutils       | 2.98 sec                                                         | 3.46 sec: 1.16x slower                                                      |
| html5lib       | 74.7 ms                                                          | 84.5 ms: 1.13x slower                                                       |
| tornado_http   | 119 ms                                                           | 129 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                            | 1.14x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 873 ms                                                           | 898 ms: 1.03x slower                                                        |
| async_tree_none_tg         | 340 ms                                                           | 352 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 607 ms: 1.06x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 642 ms: 1.06x slower                                                        |
| async_tree_none            | 365 ms                                                           | 389 ms: 1.06x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 491 ms: 1.07x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 458 ms: 1.09x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.05x slower                                                                |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 254 ms: 1.00x slower                                                        |
| float          | 80.2 ms                                                          | 95.7 ms: 1.19x slower                                                       |
| nbody          | 87.8 ms                                                          | 123 ms: 1.40x slower                                                        |
| Geometric mean | (ref)                                                            | 1.19x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 239 ms: 1.04x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 26.1 ms: 1.00x slower                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.46 ms: 1.02x slower                                                       |
| regex_compile  | 144 ms                                                           | 214 ms: 1.49x slower                                                        |
| Geometric mean | (ref)                                                            | 1.10x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 30.7 us: 1.07x faster                                                       |
| unpickle             | 15.7 us                                                          | 15.4 us: 1.02x faster                                                       |
| json_loads           | 25.0 us                                                          | 24.6 us: 1.02x faster                                                       |
| pickle               | 10.6 us                                                          | 10.5 us: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                                        |
| pickle_list          | 4.44 us                                                          | 4.49 us: 1.01x slower                                                       |
| json_dumps           | 10.8 ms                                                          | 11.1 ms: 1.03x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 113 ms: 1.10x slower                                                        |
| xml_etree_generate   | 85.7 ms                                                          | 96.4 ms: 1.12x slower                                                       |
| xml_etree_process    | 59.7 ms                                                          | 67.8 ms: 1.14x slower                                                       |
| tomli_loads          | 2.40 sec                                                         | 2.88 sec: 1.20x slower                                                      |
| unpickle_pure_python | 224 us                                                           | 308 us: 1.37x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 440 us: 1.43x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.08x slower                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 12.9 ms: 1.02x faster                                                       |
| python_startup_no_site | 8.85 ms                                                          | 8.90 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 39.0 ms                                                          | 45.8 ms: 1.17x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 69.9 ms: 1.20x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 32.7 ms: 1.26x slower                                                       |
| mako            | 10.4 ms                                                          | 14.7 ms: 1.42x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.26x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict                | 32.8 us                                                          | 30.7 us: 1.07x faster                                                       |
| regex_dna                  | 249 ms                                                           | 239 ms: 1.04x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.51 ms: 1.04x faster                                                       |
| coverage                   | 83.5 ms                                                          | 80.7 ms: 1.03x faster                                                       |
| python_startup             | 13.2 ms                                                          | 12.9 ms: 1.02x faster                                                       |
| unpickle                   | 15.7 us                                                          | 15.4 us: 1.02x faster                                                       |
| json_loads                 | 25.0 us                                                          | 24.6 us: 1.02x faster                                                       |
| asyncio_websockets         | 395 ms                                                           | 390 ms: 1.01x faster                                                        |
| pickle                     | 10.6 us                                                          | 10.5 us: 1.01x faster                                                       |
| pidigits                   | 254 ms                                                           | 254 ms: 1.00x slower                                                        |
| regex_v8                   | 26.0 ms                                                          | 26.1 ms: 1.00x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 8.90 ms: 1.01x slower                                                       |
| xml_etree_parse            | 144 ms                                                           | 145 ms: 1.01x slower                                                        |
| pickle_list                | 4.44 us                                                          | 4.49 us: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.60 sec: 1.01x slower                                                      |
| regex_effbot               | 3.40 ms                                                          | 3.46 ms: 1.02x slower                                                       |
| asyncio_tcp                | 378 ms                                                           | 387 ms: 1.02x slower                                                        |
| json_dumps                 | 10.8 ms                                                          | 11.1 ms: 1.03x slower                                                       |
| async_tree_io              | 873 ms                                                           | 898 ms: 1.03x slower                                                        |
| generators                 | 33.5 ms                                                          | 34.6 ms: 1.03x slower                                                       |
| json                       | 5.35 ms                                                          | 5.53 ms: 1.03x slower                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 2.07 ms: 1.03x slower                                                       |
| logging_format             | 7.11 us                                                          | 7.36 us: 1.03x slower                                                       |
| async_tree_none_tg         | 340 ms                                                           | 352 ms: 1.04x slower                                                        |
| sqlite_synth               | 2.80 us                                                          | 2.91 us: 1.04x slower                                                       |
| coroutines                 | 22.0 ms                                                          | 22.9 ms: 1.04x slower                                                       |
| logging_simple             | 6.40 us                                                          | 6.70 us: 1.05x slower                                                       |
| thrift                     | 880 us                                                           | 927 us: 1.05x slower                                                        |
| flaskblogging              | 4.68 ms                                                          | 4.95 ms: 1.06x slower                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 607 ms: 1.06x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 642 ms: 1.06x slower                                                        |
| async_tree_none            | 365 ms                                                           | 389 ms: 1.06x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 491 ms: 1.07x slower                                                        |
| tornado_http               | 119 ms                                                           | 129 ms: 1.08x slower                                                        |
| dask                       | 391 ms                                                           | 423 ms: 1.08x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 458 ms: 1.09x slower                                                        |
| richards_super             | 61.2 ms                                                          | 66.9 ms: 1.09x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 113 ms: 1.10x slower                                                        |
| richards                   | 53.4 ms                                                          | 59.3 ms: 1.11x slower                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 96.4 ms: 1.12x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.78 sec: 1.13x slower                                                      |
| async_generators           | 363 ms                                                           | 411 ms: 1.13x slower                                                        |
| bench_thread_pool          | 908 us                                                           | 1.03 ms: 1.13x slower                                                       |
| html5lib                   | 74.7 ms                                                          | 84.5 ms: 1.13x slower                                                       |
| xml_etree_process          | 59.7 ms                                                          | 67.8 ms: 1.14x slower                                                       |
| meteor_contest             | 128 ms                                                           | 148 ms: 1.16x slower                                                        |
| docutils                   | 2.98 sec                                                         | 3.46 sec: 1.16x slower                                                      |
| dulwich_log                | 67.3 ms                                                          | 78.3 ms: 1.16x slower                                                       |
| chameleon                  | 7.40 ms                                                          | 8.61 ms: 1.16x slower                                                       |
| pylint                     | 339 ms                                                           | 396 ms: 1.17x slower                                                        |
| django_template            | 39.0 ms                                                          | 45.8 ms: 1.17x slower                                                       |
| typing_runtime_protocols   | 171 us                                                           | 200 us: 1.17x slower                                                        |
| 2to3                       | 291 ms                                                           | 343 ms: 1.18x slower                                                        |
| sqlglot_normalize          | 120 ms                                                           | 142 ms: 1.18x slower                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 4.03 us: 1.19x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.46 sec: 1.19x slower                                                      |
| sqlglot_optimize           | 59.5 ms                                                          | 71.0 ms: 1.19x slower                                                       |
| float                      | 80.2 ms                                                          | 95.7 ms: 1.19x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.88 sec: 1.20x slower                                                      |
| genshi_xml                 | 58.1 ms                                                          | 69.9 ms: 1.20x slower                                                       |
| sympy_integrate            | 23.2 ms                                                          | 28.3 ms: 1.22x slower                                                       |
| sympy_sum                  | 155 ms                                                           | 189 ms: 1.22x slower                                                        |
| go                         | 165 ms                                                           | 203 ms: 1.23x slower                                                        |
| sympy_expand               | 501 ms                                                           | 624 ms: 1.25x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 2.20 ms: 1.25x slower                                                       |
| deepcopy                   | 377 us                                                           | 473 us: 1.25x slower                                                        |
| pprint_safe_repr           | 818 ms                                                           | 1.03 sec: 1.25x slower                                                      |
| sqlglot_parse              | 1.39 ms                                                          | 1.75 ms: 1.26x slower                                                       |
| sympy_str                  | 295 ms                                                           | 370 ms: 1.26x slower                                                        |
| pprint_pformat             | 1.66 sec                                                         | 2.09 sec: 1.26x slower                                                      |
| genshi_text                | 25.9 ms                                                          | 32.7 ms: 1.26x slower                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 93.0 ms: 1.26x slower                                                       |
| raytrace                   | 260 ms                                                           | 333 ms: 1.28x slower                                                        |
| pyflate                    | 482 ms                                                           | 645 ms: 1.34x slower                                                        |
| nqueens                    | 88.4 ms                                                          | 119 ms: 1.34x slower                                                        |
| chaos                      | 59.6 ms                                                          | 80.5 ms: 1.35x slower                                                       |
| deltablue                  | 3.37 ms                                                          | 4.56 ms: 1.35x slower                                                       |
| fannkuch                   | 353 ms                                                           | 483 ms: 1.37x slower                                                        |
| unpickle_pure_python       | 224 us                                                           | 308 us: 1.37x slower                                                        |
| scimark_fft                | 312 ms                                                           | 429 ms: 1.38x slower                                                        |
| scimark_sor                | 119 ms                                                           | 166 ms: 1.39x slower                                                        |
| nbody                      | 87.8 ms                                                          | 123 ms: 1.40x slower                                                        |
| mako                       | 10.4 ms                                                          | 14.7 ms: 1.42x slower                                                       |
| scimark_lu                 | 97.5 ms                                                          | 138 ms: 1.42x slower                                                        |
| pickle_pure_python         | 307 us                                                           | 440 us: 1.43x slower                                                        |
| regex_compile              | 144 ms                                                           | 214 ms: 1.49x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 98.8 ms: 1.51x slower                                                       |
| deepcopy_memo              | 37.3 us                                                          | 58.2 us: 1.56x slower                                                       |
| spectral_norm              | 97.3 ms                                                          | 155 ms: 1.59x slower                                                        |
| comprehensions             | 17.0 us                                                          | 27.6 us: 1.63x slower                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 6.97 ms: 1.63x slower                                                       |
| hexiom                     | 6.35 ms                                                          | 10.6 ms: 1.66x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 161 ns: 1.67x slower                                                        |
| telco                      | 8.40 ms                                                          | 182 ms: 21.67x slower                                                       |
| Geometric mean             | (ref)                                                            | 1.20x slower                                                                |

Benchmark hidden because not significant (4): unpickle_list, pathlib, async_tree_io_tg, bench_mp_pool
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 1.02x