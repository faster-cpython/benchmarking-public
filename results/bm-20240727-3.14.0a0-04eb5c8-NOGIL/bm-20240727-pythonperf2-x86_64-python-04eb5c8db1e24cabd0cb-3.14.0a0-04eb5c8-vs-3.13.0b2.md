# Results vs. 3.13.0b2

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.45x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 435 ms: 1.49x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.54 sec: 1.19x slower                                                      |
| html5lib       | 74.7 ms                                                          | 109 ms: 1.46x slower                                                        |
| tornado_http   | 119 ms                                                           | 163 ms: 1.36x slower                                                        |
| Geometric mean | (ref)                                                            | 1.37x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 911 ms: 1.01x slower                                                        |
| async_tree_none_tg         | 340 ms                                                           | 372 ms: 1.09x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 634 ms: 1.11x slower                                                        |
| async_tree_io              | 873 ms                                                           | 967 ms: 1.11x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 687 ms: 1.14x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 479 ms: 1.14x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 531 ms: 1.16x slower                                                        |
| async_tree_none            | 365 ms                                                           | 430 ms: 1.18x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.12x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 256 ms: 1.01x slower                                                        |
| float          | 80.2 ms                                                          | 144 ms: 1.80x slower                                                        |
| nbody          | 87.8 ms                                                          | 200 ms: 2.28x slower                                                        |
| Geometric mean | (ref)                                                            | 1.61x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 239 ms: 1.04x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.52 ms: 1.04x slower                                                       |
| regex_v8       | 26.0 ms                                                          | 27.8 ms: 1.07x slower                                                       |
| regex_compile  | 144 ms                                                           | 233 ms: 1.62x slower                                                        |
| Geometric mean | (ref)                                                            | 1.14x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                           | 109 ms: 1.06x slower                                                        |
| json_loads           | 25.0 us                                                          | 29.8 us: 1.19x slower                                                       |
| json_dumps           | 10.8 ms                                                          | 14.3 ms: 1.33x slower                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 116 ms: 1.35x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 3.43 sec: 1.43x slower                                                      |
| xml_etree_process    | 59.7 ms                                                          | 94.3 ms: 1.58x slower                                                       |
| unpickle_pure_python | 224 us                                                           | 421 us: 1.87x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 596 us: 1.94x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.38x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 16.7 ms: 1.27x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 11.4 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 84.3 ms: 1.45x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 43.4 ms: 1.67x slower                                                       |
| django_template | 39.0 ms                                                          | 69.0 ms: 1.77x slower                                                       |
| mako            | 10.4 ms                                                          | 22.1 ms: 2.13x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.74x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.69 ms                                                          | 2.88 ms: 1.62x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.73 ms: 1.16x faster                                                       |
| bench_mp_pool              | 4.91 ms                                                          | 4.40 ms: 1.12x faster                                                       |
| regex_dna                  | 249 ms                                                           | 239 ms: 1.04x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 383 ms: 1.03x faster                                                        |
| pidigits                   | 254 ms                                                           | 256 ms: 1.01x slower                                                        |
| async_tree_io_tg           | 900 ms                                                           | 911 ms: 1.01x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.52 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 109 ms: 1.06x slower                                                        |
| regex_v8                   | 26.0 ms                                                          | 27.8 ms: 1.07x slower                                                       |
| async_tree_none_tg         | 340 ms                                                           | 372 ms: 1.09x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 634 ms: 1.11x slower                                                        |
| async_tree_io              | 873 ms                                                           | 967 ms: 1.11x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.77 sec: 1.12x slower                                                      |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 687 ms: 1.14x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 479 ms: 1.14x slower                                                        |
| pathlib                    | 17.1 ms                                                          | 19.6 ms: 1.14x slower                                                       |
| async_tree_memoization     | 460 ms                                                           | 531 ms: 1.16x slower                                                        |
| json                       | 5.35 ms                                                          | 6.21 ms: 1.16x slower                                                       |
| async_tree_none            | 365 ms                                                           | 430 ms: 1.18x slower                                                        |
| docutils                   | 2.98 sec                                                         | 3.54 sec: 1.19x slower                                                      |
| json_loads                 | 25.0 us                                                          | 29.8 us: 1.19x slower                                                       |
| asyncio_tcp                | 378 ms                                                           | 453 ms: 1.20x slower                                                        |
| deepcopy                   | 377 us                                                           | 453 us: 1.20x slower                                                        |
| telco                      | 8.40 ms                                                          | 10.3 ms: 1.22x slower                                                       |
| generators                 | 33.5 ms                                                          | 41.9 ms: 1.25x slower                                                       |
| python_startup             | 13.2 ms                                                          | 16.7 ms: 1.27x slower                                                       |
| coroutines                 | 22.0 ms                                                          | 28.1 ms: 1.28x slower                                                       |
| pylint                     | 339 ms                                                           | 435 ms: 1.28x slower                                                        |
| coverage                   | 83.5 ms                                                          | 107 ms: 1.28x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 11.4 ms: 1.29x slower                                                       |
| json_dumps                 | 10.8 ms                                                          | 14.3 ms: 1.33x slower                                                       |
| mdp                        | 2.46 sec                                                         | 3.27 sec: 1.33x slower                                                      |
| scimark_fft                | 312 ms                                                           | 417 ms: 1.34x slower                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 6.90 sec: 1.34x slower                                                      |
| xml_etree_generate         | 85.7 ms                                                          | 116 ms: 1.35x slower                                                        |
| tornado_http               | 119 ms                                                           | 163 ms: 1.36x slower                                                        |
| meteor_contest             | 128 ms                                                           | 175 ms: 1.37x slower                                                        |
| sympy_integrate            | 23.2 ms                                                          | 32.4 ms: 1.40x slower                                                       |
| async_generators           | 363 ms                                                           | 508 ms: 1.40x slower                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 6.01 ms: 1.40x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 3.43 sec: 1.43x slower                                                      |
| deepcopy_memo              | 37.3 us                                                          | 53.2 us: 1.43x slower                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 4.85 us: 1.43x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.75 sec: 1.44x slower                                                      |
| genshi_xml                 | 58.1 ms                                                          | 84.3 ms: 1.45x slower                                                       |
| html5lib                   | 74.7 ms                                                          | 109 ms: 1.46x slower                                                        |
| nqueens                    | 88.4 ms                                                          | 130 ms: 1.48x slower                                                        |
| 2to3                       | 291 ms                                                           | 435 ms: 1.49x slower                                                        |
| sympy_str                  | 295 ms                                                           | 456 ms: 1.55x slower                                                        |
| thrift                     | 880 us                                                           | 1.37 ms: 1.56x slower                                                       |
| sqlglot_normalize          | 120 ms                                                           | 188 ms: 1.57x slower                                                        |
| xml_etree_process          | 59.7 ms                                                          | 94.3 ms: 1.58x slower                                                       |
| richards                   | 53.4 ms                                                          | 85.1 ms: 1.59x slower                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 95.2 ms: 1.60x slower                                                       |
| regex_compile              | 144 ms                                                           | 233 ms: 1.62x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 278 us: 1.63x slower                                                        |
| sympy_expand               | 501 ms                                                           | 830 ms: 1.66x slower                                                        |
| genshi_text                | 25.9 ms                                                          | 43.4 ms: 1.67x slower                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 124 ms: 1.68x slower                                                        |
| pyflate                    | 482 ms                                                           | 813 ms: 1.69x slower                                                        |
| richards_super             | 61.2 ms                                                          | 103 ms: 1.69x slower                                                        |
| sympy_sum                  | 155 ms                                                           | 262 ms: 1.69x slower                                                        |
| bench_thread_pool          | 908 us                                                           | 1.56 ms: 1.72x slower                                                       |
| spectral_norm              | 97.3 ms                                                          | 169 ms: 1.74x slower                                                        |
| fannkuch                   | 353 ms                                                           | 614 ms: 1.74x slower                                                        |
| django_template            | 39.0 ms                                                          | 69.0 ms: 1.77x slower                                                       |
| logging_format             | 7.11 us                                                          | 12.7 us: 1.78x slower                                                       |
| comprehensions             | 17.0 us                                                          | 30.3 us: 1.79x slower                                                       |
| pprint_safe_repr           | 818 ms                                                           | 1.47 sec: 1.80x slower                                                      |
| float                      | 80.2 ms                                                          | 144 ms: 1.80x slower                                                        |
| pprint_pformat             | 1.66 sec                                                         | 3.04 sec: 1.83x slower                                                      |
| logging_simple             | 6.40 us                                                          | 11.8 us: 1.84x slower                                                       |
| unpickle_pure_python       | 224 us                                                           | 421 us: 1.87x slower                                                        |
| hexiom                     | 6.35 ms                                                          | 12.1 ms: 1.90x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 596 us: 1.94x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 187 ns: 1.94x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 3.44 ms: 1.95x slower                                                       |
| go                         | 165 ms                                                           | 338 ms: 2.05x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 136 ms: 2.08x slower                                                        |
| chaos                      | 59.6 ms                                                          | 124 ms: 2.08x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 2.94 ms: 2.11x slower                                                       |
| mako                       | 10.4 ms                                                          | 22.1 ms: 2.13x slower                                                       |
| scimark_sor                | 119 ms                                                           | 266 ms: 2.24x slower                                                        |
| nbody                      | 87.8 ms                                                          | 200 ms: 2.28x slower                                                        |
| raytrace                   | 260 ms                                                           | 612 ms: 2.35x slower                                                        |
| scimark_lu                 | 97.5 ms                                                          | 242 ms: 2.48x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 8.40 ms: 2.49x slower                                                       |
| Geometric mean             | (ref)                                                            | 1.45x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.35x
- 95% likely to have a slowdown of 1.34x
- 99% likely to have a slowdown of 1.30x

# Memory
- memory change: 1.16x