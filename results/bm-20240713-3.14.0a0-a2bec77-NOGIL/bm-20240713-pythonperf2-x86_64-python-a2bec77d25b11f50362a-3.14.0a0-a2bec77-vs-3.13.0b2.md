# Results vs. 3.13.0b2

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-x86_64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.44x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 433 ms: 1.48x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.49 sec: 1.17x slower                                                      |
| html5lib       | 74.7 ms                                                          | 106 ms: 1.43x slower                                                        |
| tornado_http   | 119 ms                                                           | 163 ms: 1.36x slower                                                        |
| Geometric mean | (ref)                                                            | 1.35x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 340 ms                                                           | 369 ms: 1.08x slower                                                        |
| async_tree_io              | 873 ms                                                           | 968 ms: 1.11x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 645 ms: 1.13x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 478 ms: 1.14x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 693 ms: 1.15x slower                                                        |
| async_tree_none            | 365 ms                                                           | 429 ms: 1.17x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 540 ms: 1.17x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.12x slower                                                                |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 256 ms: 1.01x slower                                                        |
| float          | 80.2 ms                                                          | 148 ms: 1.85x slower                                                        |
| nbody          | 87.8 ms                                                          | 204 ms: 2.33x slower                                                        |
| Geometric mean | (ref)                                                            | 1.63x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 234 ms: 1.07x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.33 ms: 1.02x faster                                                       |
| regex_v8       | 26.0 ms                                                          | 28.4 ms: 1.09x slower                                                       |
| regex_compile  | 144 ms                                                           | 231 ms: 1.60x slower                                                        |
| Geometric mean | (ref)                                                            | 1.13x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                           | 137 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 110 ms: 1.08x slower                                                        |
| json_loads           | 25.0 us                                                          | 30.5 us: 1.22x slower                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 114 ms: 1.33x slower                                                        |
| json_dumps           | 10.8 ms                                                          | 14.4 ms: 1.34x slower                                                       |
| tomli_loads          | 2.40 sec                                                         | 3.38 sec: 1.41x slower                                                      |
| xml_etree_process    | 59.7 ms                                                          | 94.4 ms: 1.58x slower                                                       |
| unpickle_pure_python | 224 us                                                           | 418 us: 1.86x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 589 us: 1.92x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.38x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 16.9 ms: 1.28x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 11.5 ms: 1.30x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.29x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 83.1 ms: 1.43x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 42.4 ms: 1.64x slower                                                       |
| django_template | 39.0 ms                                                          | 68.2 ms: 1.75x slower                                                       |
| mako            | 10.4 ms                                                          | 22.3 ms: 2.15x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.72x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.69 ms                                                          | 3.10 ms: 1.51x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.75 ms: 1.14x faster                                                       |
| bench_mp_pool              | 4.91 ms                                                          | 4.44 ms: 1.11x faster                                                       |
| regex_dna                  | 249 ms                                                           | 234 ms: 1.07x faster                                                        |
| xml_etree_parse            | 144 ms                                                           | 137 ms: 1.05x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 381 ms: 1.04x faster                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.33 ms: 1.02x faster                                                       |
| pidigits                   | 254 ms                                                           | 256 ms: 1.01x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                           | 110 ms: 1.08x slower                                                        |
| async_tree_none_tg         | 340 ms                                                           | 369 ms: 1.08x slower                                                        |
| regex_v8                   | 26.0 ms                                                          | 28.4 ms: 1.09x slower                                                       |
| async_tree_io              | 873 ms                                                           | 968 ms: 1.11x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 645 ms: 1.13x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.79 sec: 1.13x slower                                                      |
| async_tree_memoization_tg  | 421 ms                                                           | 478 ms: 1.14x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 693 ms: 1.15x slower                                                        |
| json                       | 5.35 ms                                                          | 6.18 ms: 1.15x slower                                                       |
| pathlib                    | 17.1 ms                                                          | 19.8 ms: 1.16x slower                                                       |
| docutils                   | 2.98 sec                                                         | 3.49 sec: 1.17x slower                                                      |
| async_tree_none            | 365 ms                                                           | 429 ms: 1.17x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 540 ms: 1.17x slower                                                        |
| deepcopy                   | 377 us                                                           | 444 us: 1.18x slower                                                        |
| asyncio_tcp                | 378 ms                                                           | 452 ms: 1.20x slower                                                        |
| json_loads                 | 25.0 us                                                          | 30.5 us: 1.22x slower                                                       |
| telco                      | 8.40 ms                                                          | 10.4 ms: 1.23x slower                                                       |
| coverage                   | 83.5 ms                                                          | 105 ms: 1.25x slower                                                        |
| pylint                     | 339 ms                                                           | 427 ms: 1.26x slower                                                        |
| python_startup             | 13.2 ms                                                          | 16.9 ms: 1.28x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 11.5 ms: 1.30x slower                                                       |
| coroutines                 | 22.0 ms                                                          | 28.8 ms: 1.31x slower                                                       |
| scimark_fft                | 312 ms                                                           | 415 ms: 1.33x slower                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 114 ms: 1.33x slower                                                        |
| mdp                        | 2.46 sec                                                         | 3.29 sec: 1.34x slower                                                      |
| json_dumps                 | 10.8 ms                                                          | 14.4 ms: 1.34x slower                                                       |
| dulwich_log                | 67.3 ms                                                          | 90.2 ms: 1.34x slower                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 5.79 ms: 1.35x slower                                                       |
| meteor_contest             | 128 ms                                                           | 174 ms: 1.36x slower                                                        |
| generators                 | 33.5 ms                                                          | 45.5 ms: 1.36x slower                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 6.98 sec: 1.36x slower                                                      |
| tornado_http               | 119 ms                                                           | 163 ms: 1.36x slower                                                        |
| deepcopy_memo              | 37.3 us                                                          | 51.0 us: 1.37x slower                                                       |
| async_generators           | 363 ms                                                           | 497 ms: 1.37x slower                                                        |
| sympy_integrate            | 23.2 ms                                                          | 32.2 ms: 1.39x slower                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 4.73 us: 1.40x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 3.38 sec: 1.41x slower                                                      |
| html5lib                   | 74.7 ms                                                          | 106 ms: 1.43x slower                                                        |
| genshi_xml                 | 58.1 ms                                                          | 83.1 ms: 1.43x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.77 sec: 1.45x slower                                                      |
| nqueens                    | 88.4 ms                                                          | 131 ms: 1.48x slower                                                        |
| 2to3                       | 291 ms                                                           | 433 ms: 1.48x slower                                                        |
| sympy_str                  | 295 ms                                                           | 455 ms: 1.54x slower                                                        |
| sqlglot_normalize          | 120 ms                                                           | 187 ms: 1.56x slower                                                        |
| richards                   | 53.4 ms                                                          | 83.5 ms: 1.56x slower                                                       |
| xml_etree_process          | 59.7 ms                                                          | 94.4 ms: 1.58x slower                                                       |
| typing_runtime_protocols   | 171 us                                                           | 271 us: 1.59x slower                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 94.6 ms: 1.59x slower                                                       |
| regex_compile              | 144 ms                                                           | 231 ms: 1.60x slower                                                        |
| pyflate                    | 482 ms                                                           | 774 ms: 1.61x slower                                                        |
| thrift                     | 880 us                                                           | 1.42 ms: 1.61x slower                                                       |
| genshi_text                | 25.9 ms                                                          | 42.4 ms: 1.64x slower                                                       |
| richards_super             | 61.2 ms                                                          | 100 ms: 1.64x slower                                                        |
| fannkuch                   | 353 ms                                                           | 582 ms: 1.65x slower                                                        |
| sympy_expand               | 501 ms                                                           | 827 ms: 1.65x slower                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 124 ms: 1.68x slower                                                        |
| sympy_sum                  | 155 ms                                                           | 263 ms: 1.70x slower                                                        |
| bench_thread_pool          | 908 us                                                           | 1.56 ms: 1.72x slower                                                       |
| django_template            | 39.0 ms                                                          | 68.2 ms: 1.75x slower                                                       |
| logging_format             | 7.11 us                                                          | 12.5 us: 1.75x slower                                                       |
| spectral_norm              | 97.3 ms                                                          | 172 ms: 1.77x slower                                                        |
| pprint_safe_repr           | 818 ms                                                           | 1.45 sec: 1.77x slower                                                      |
| comprehensions             | 17.0 us                                                          | 30.3 us: 1.79x slower                                                       |
| logging_simple             | 6.40 us                                                          | 11.5 us: 1.80x slower                                                       |
| pprint_pformat             | 1.66 sec                                                         | 2.99 sec: 1.80x slower                                                      |
| float                      | 80.2 ms                                                          | 148 ms: 1.85x slower                                                        |
| unpickle_pure_python       | 224 us                                                           | 418 us: 1.86x slower                                                        |
| hexiom                     | 6.35 ms                                                          | 12.1 ms: 1.90x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 183 ns: 1.90x slower                                                        |
| pickle_pure_python         | 307 us                                                           | 589 us: 1.92x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 3.42 ms: 1.94x slower                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 134 ms: 2.05x slower                                                        |
| go                         | 165 ms                                                           | 342 ms: 2.07x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 2.91 ms: 2.09x slower                                                       |
| scimark_sor                | 119 ms                                                           | 251 ms: 2.12x slower                                                        |
| chaos                      | 59.6 ms                                                          | 127 ms: 2.12x slower                                                        |
| mako                       | 10.4 ms                                                          | 22.3 ms: 2.15x slower                                                       |
| nbody                      | 87.8 ms                                                          | 204 ms: 2.33x slower                                                        |
| raytrace                   | 260 ms                                                           | 623 ms: 2.39x slower                                                        |
| scimark_lu                 | 97.5 ms                                                          | 236 ms: 2.42x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 8.39 ms: 2.48x slower                                                       |
| Geometric mean             | (ref)                                                            | 1.44x slower                                                                |

Benchmark hidden because not significant (1): async_tree_io_tg
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.35x
- 95% likely to have a slowdown of 1.33x
- 99% likely to have a slowdown of 1.32x

# Memory
- memory change: 1.15x