# Results vs. 3.13.0b2

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-x86_64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.46x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 442 ms: 1.52x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.52 sec: 1.18x slower                                                      |
| html5lib       | 74.7 ms                                                          | 110 ms: 1.47x slower                                                        |
| tornado_http   | 119 ms                                                           | 170 ms: 1.42x slower                                                        |
| Geometric mean | (ref)                                                            | 1.39x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 920 ms: 1.02x slower                                                        |
| async_tree_io              | 873 ms                                                           | 964 ms: 1.10x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 634 ms: 1.11x slower                                                        |
| async_tree_none_tg         | 340 ms                                                           | 387 ms: 1.14x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 688 ms: 1.14x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 479 ms: 1.14x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 533 ms: 1.16x slower                                                        |
| async_tree_none            | 365 ms                                                           | 428 ms: 1.17x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.12x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| float          | 80.2 ms                                                          | 143 ms: 1.78x slower                                                        |
| nbody          | 87.8 ms                                                          | 196 ms: 2.23x slower                                                        |
| Geometric mean | (ref)                                                            | 1.58x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 255 ms: 1.02x slower                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.59 ms: 1.06x slower                                                       |
| regex_v8       | 26.0 ms                                                          | 28.5 ms: 1.09x slower                                                       |
| regex_compile  | 144 ms                                                           | 234 ms: 1.62x slower                                                        |
| Geometric mean | (ref)                                                            | 1.18x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                           | 140 ms: 1.02x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 112 ms: 1.09x slower                                                        |
| json_loads           | 25.0 us                                                          | 30.1 us: 1.20x slower                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 116 ms: 1.35x slower                                                        |
| json_dumps           | 10.8 ms                                                          | 14.6 ms: 1.36x slower                                                       |
| tomli_loads          | 2.40 sec                                                         | 3.43 sec: 1.43x slower                                                      |
| xml_etree_process    | 59.7 ms                                                          | 95.7 ms: 1.60x slower                                                       |
| unpickle_pure_python | 224 us                                                           | 427 us: 1.90x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 608 us: 1.98x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.40x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 17.3 ms: 1.31x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 11.9 ms: 1.35x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.33x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 84.2 ms: 1.45x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 43.4 ms: 1.68x slower                                                       |
| django_template | 39.0 ms                                                          | 68.4 ms: 1.75x slower                                                       |
| mako            | 10.4 ms                                                          | 21.8 ms: 2.10x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.73x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.69 ms                                                          | 2.90 ms: 1.61x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.70 ms: 1.18x faster                                                       |
| asyncio_websockets         | 395 ms                                                           | 385 ms: 1.03x faster                                                        |
| xml_etree_parse            | 144 ms                                                           | 140 ms: 1.02x faster                                                        |
| pidigits                   | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| regex_dna                  | 249 ms                                                           | 255 ms: 1.02x slower                                                        |
| async_tree_io_tg           | 900 ms                                                           | 920 ms: 1.02x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.59 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 112 ms: 1.09x slower                                                        |
| regex_v8                   | 26.0 ms                                                          | 28.5 ms: 1.09x slower                                                       |
| async_tree_io              | 873 ms                                                           | 964 ms: 1.10x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 634 ms: 1.11x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.77 sec: 1.12x slower                                                      |
| async_tree_none_tg         | 340 ms                                                           | 387 ms: 1.14x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 688 ms: 1.14x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 479 ms: 1.14x slower                                                        |
| json                       | 5.35 ms                                                          | 6.19 ms: 1.16x slower                                                       |
| pathlib                    | 17.1 ms                                                          | 19.8 ms: 1.16x slower                                                       |
| async_tree_memoization     | 460 ms                                                           | 533 ms: 1.16x slower                                                        |
| async_tree_none            | 365 ms                                                           | 428 ms: 1.17x slower                                                        |
| docutils                   | 2.98 sec                                                         | 3.52 sec: 1.18x slower                                                      |
| deepcopy                   | 377 us                                                           | 450 us: 1.19x slower                                                        |
| asyncio_tcp                | 378 ms                                                           | 452 ms: 1.20x slower                                                        |
| json_loads                 | 25.0 us                                                          | 30.1 us: 1.20x slower                                                       |
| scimark_fft                | 312 ms                                                           | 394 ms: 1.26x slower                                                        |
| generators                 | 33.5 ms                                                          | 42.4 ms: 1.27x slower                                                       |
| telco                      | 8.40 ms                                                          | 10.7 ms: 1.28x slower                                                       |
| pylint                     | 339 ms                                                           | 440 ms: 1.30x slower                                                        |
| python_startup             | 13.2 ms                                                          | 17.3 ms: 1.31x slower                                                       |
| coverage                   | 83.5 ms                                                          | 110 ms: 1.32x slower                                                        |
| mdp                        | 2.46 sec                                                         | 3.25 sec: 1.32x slower                                                      |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 5.65 ms: 1.32x slower                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 6.88 sec: 1.34x slower                                                      |
| python_startup_no_site     | 8.85 ms                                                          | 11.9 ms: 1.35x slower                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 116 ms: 1.35x slower                                                        |
| meteor_contest             | 128 ms                                                           | 174 ms: 1.36x slower                                                        |
| json_dumps                 | 10.8 ms                                                          | 14.6 ms: 1.36x slower                                                       |
| coroutines                 | 22.0 ms                                                          | 30.5 ms: 1.39x slower                                                       |
| deepcopy_memo              | 37.3 us                                                          | 51.7 us: 1.39x slower                                                       |
| async_generators           | 363 ms                                                           | 511 ms: 1.41x slower                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 4.78 us: 1.41x slower                                                       |
| sympy_integrate            | 23.2 ms                                                          | 32.9 ms: 1.42x slower                                                       |
| tornado_http               | 119 ms                                                           | 170 ms: 1.42x slower                                                        |
| tomli_loads                | 2.40 sec                                                         | 3.43 sec: 1.43x slower                                                      |
| pycparser                  | 1.22 sec                                                         | 1.76 sec: 1.44x slower                                                      |
| genshi_xml                 | 58.1 ms                                                          | 84.2 ms: 1.45x slower                                                       |
| html5lib                   | 74.7 ms                                                          | 110 ms: 1.47x slower                                                        |
| nqueens                    | 88.4 ms                                                          | 130 ms: 1.48x slower                                                        |
| 2to3                       | 291 ms                                                           | 442 ms: 1.52x slower                                                        |
| sympy_str                  | 295 ms                                                           | 462 ms: 1.57x slower                                                        |
| sqlglot_normalize          | 120 ms                                                           | 189 ms: 1.57x slower                                                        |
| thrift                     | 880 us                                                           | 1.39 ms: 1.58x slower                                                       |
| xml_etree_process          | 59.7 ms                                                          | 95.7 ms: 1.60x slower                                                       |
| richards                   | 53.4 ms                                                          | 85.7 ms: 1.60x slower                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 95.9 ms: 1.61x slower                                                       |
| regex_compile              | 144 ms                                                           | 234 ms: 1.62x slower                                                        |
| pyflate                    | 482 ms                                                           | 785 ms: 1.63x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 279 us: 1.64x slower                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 122 ms: 1.66x slower                                                        |
| sympy_expand               | 501 ms                                                           | 837 ms: 1.67x slower                                                        |
| richards_super             | 61.2 ms                                                          | 103 ms: 1.68x slower                                                        |
| genshi_text                | 25.9 ms                                                          | 43.4 ms: 1.68x slower                                                       |
| fannkuch                   | 353 ms                                                           | 593 ms: 1.68x slower                                                        |
| spectral_norm              | 97.3 ms                                                          | 165 ms: 1.69x slower                                                        |
| sympy_sum                  | 155 ms                                                           | 266 ms: 1.72x slower                                                        |
| django_template            | 39.0 ms                                                          | 68.4 ms: 1.75x slower                                                       |
| float                      | 80.2 ms                                                          | 143 ms: 1.78x slower                                                        |
| pprint_safe_repr           | 818 ms                                                           | 1.47 sec: 1.79x slower                                                      |
| logging_format             | 7.11 us                                                          | 12.9 us: 1.81x slower                                                       |
| comprehensions             | 17.0 us                                                          | 30.9 us: 1.82x slower                                                       |
| pprint_pformat             | 1.66 sec                                                         | 3.04 sec: 1.83x slower                                                      |
| logging_simple             | 6.40 us                                                          | 11.9 us: 1.86x slower                                                       |
| bench_thread_pool          | 908 us                                                           | 1.70 ms: 1.87x slower                                                       |
| unpickle_pure_python       | 224 us                                                           | 427 us: 1.90x slower                                                        |
| hexiom                     | 6.35 ms                                                          | 12.2 ms: 1.91x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 3.42 ms: 1.94x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 608 us: 1.98x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 135 ms: 2.06x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 2.88 ms: 2.07x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 202 ns: 2.09x slower                                                        |
| mako                       | 10.4 ms                                                          | 21.8 ms: 2.10x slower                                                       |
| chaos                      | 59.6 ms                                                          | 126 ms: 2.11x slower                                                        |
| go                         | 165 ms                                                           | 351 ms: 2.12x slower                                                        |
| nbody                      | 87.8 ms                                                          | 196 ms: 2.23x slower                                                        |
| scimark_sor                | 119 ms                                                           | 266 ms: 2.24x slower                                                        |
| raytrace                   | 260 ms                                                           | 626 ms: 2.41x slower                                                        |
| scimark_lu                 | 97.5 ms                                                          | 238 ms: 2.44x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 8.55 ms: 2.53x slower                                                       |
| Geometric mean             | (ref)                                                            | 1.46x slower                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.35x
- 95% likely to have a slowdown of 1.33x
- 99% likely to have a slowdown of 1.31x

# Memory
- memory change: 1.16x