# Results vs. 3.13.0b2

- fork: python
- ref: db6f5e193315a3bbfa7b
- machine: linux-x86_64
- commit hash: db6f5e1
- commit date: 2024-08-13
- overall geometric mean: 1.44x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 437 ms: 1.50x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.51 sec: 1.18x slower                                                      |
| html5lib       | 74.7 ms                                                          | 109 ms: 1.47x slower                                                        |
| tornado_http   | 119 ms                                                           | 166 ms: 1.39x slower                                                        |
| Geometric mean | (ref)                                                            | 1.38x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 891 ms: 1.01x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 366 ms: 1.07x slower                                                        |
| async_tree_io              | 873 ms                                                           | 948 ms: 1.09x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 632 ms: 1.10x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 471 ms: 1.12x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 683 ms: 1.13x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 521 ms: 1.13x slower                                                        |
| async_tree_none            | 365 ms                                                           | 419 ms: 1.15x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.10x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| float          | 80.2 ms                                                          | 146 ms: 1.82x slower                                                        |
| nbody          | 87.8 ms                                                          | 201 ms: 2.29x slower                                                        |
| Geometric mean | (ref)                                                            | 1.60x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 237 ms: 1.05x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.48 ms: 1.02x slower                                                       |
| regex_v8       | 26.0 ms                                                          | 26.9 ms: 1.03x slower                                                       |
| regex_compile  | 144 ms                                                           | 233 ms: 1.62x slower                                                        |
| Geometric mean | (ref)                                                            | 1.13x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                           | 136 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 109 ms: 1.07x slower                                                        |
| json_loads           | 25.0 us                                                          | 29.7 us: 1.19x slower                                                       |
| json_dumps           | 10.8 ms                                                          | 14.5 ms: 1.35x slower                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 119 ms: 1.39x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 3.41 sec: 1.42x slower                                                      |
| xml_etree_process    | 59.7 ms                                                          | 97.6 ms: 1.63x slower                                                       |
| unpickle_pure_python | 224 us                                                           | 406 us: 1.81x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 598 us: 1.94x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.38x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 17.1 ms: 1.30x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 11.8 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.31x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 85.5 ms: 1.47x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 44.1 ms: 1.70x slower                                                       |
| django_template | 39.0 ms                                                          | 69.3 ms: 1.78x slower                                                       |
| mako            | 10.4 ms                                                          | 22.2 ms: 2.14x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.76x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.69 ms                                                          | 2.79 ms: 1.68x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.61 ms: 1.25x faster                                                       |
| xml_etree_parse            | 144 ms                                                           | 136 ms: 1.05x faster                                                        |
| regex_dna                  | 249 ms                                                           | 237 ms: 1.05x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 381 ms: 1.04x faster                                                        |
| pidigits                   | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 891 ms: 1.01x faster                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.48 ms: 1.02x slower                                                       |
| regex_v8                   | 26.0 ms                                                          | 26.9 ms: 1.03x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 109 ms: 1.07x slower                                                        |
| async_tree_none_tg         | 340 ms                                                           | 366 ms: 1.07x slower                                                        |
| async_tree_io              | 873 ms                                                           | 948 ms: 1.09x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 632 ms: 1.10x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 471 ms: 1.12x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 683 ms: 1.13x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 521 ms: 1.13x slower                                                        |
| async_tree_none            | 365 ms                                                           | 419 ms: 1.15x slower                                                        |
| json                       | 5.35 ms                                                          | 6.16 ms: 1.15x slower                                                       |
| pathlib                    | 17.1 ms                                                          | 19.8 ms: 1.16x slower                                                       |
| docutils                   | 2.98 sec                                                         | 3.51 sec: 1.18x slower                                                      |
| asyncio_tcp                | 378 ms                                                           | 448 ms: 1.18x slower                                                        |
| json_loads                 | 25.0 us                                                          | 29.7 us: 1.19x slower                                                       |
| deepcopy                   | 377 us                                                           | 453 us: 1.20x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.90 sec: 1.20x slower                                                      |
| generators                 | 33.5 ms                                                          | 41.3 ms: 1.23x slower                                                       |
| telco                      | 8.40 ms                                                          | 10.6 ms: 1.26x slower                                                       |
| pylint                     | 339 ms                                                           | 435 ms: 1.28x slower                                                        |
| python_startup             | 13.2 ms                                                          | 17.1 ms: 1.30x slower                                                       |
| coverage                   | 83.5 ms                                                          | 109 ms: 1.31x slower                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 6.77 sec: 1.32x slower                                                      |
| mdp                        | 2.46 sec                                                         | 3.25 sec: 1.32x slower                                                      |
| scimark_fft                | 312 ms                                                           | 413 ms: 1.32x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 11.8 ms: 1.33x slower                                                       |
| coroutines                 | 22.0 ms                                                          | 29.3 ms: 1.33x slower                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 5.72 ms: 1.34x slower                                                       |
| json_dumps                 | 10.8 ms                                                          | 14.5 ms: 1.35x slower                                                       |
| meteor_contest             | 128 ms                                                           | 176 ms: 1.37x slower                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 119 ms: 1.39x slower                                                        |
| tornado_http               | 119 ms                                                           | 166 ms: 1.39x slower                                                        |
| deepcopy_memo              | 37.3 us                                                          | 52.3 us: 1.40x slower                                                       |
| sympy_integrate            | 23.2 ms                                                          | 32.6 ms: 1.41x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 3.41 sec: 1.42x slower                                                      |
| deepcopy_reduce            | 3.39 us                                                          | 4.85 us: 1.43x slower                                                       |
| async_generators           | 363 ms                                                           | 521 ms: 1.44x slower                                                        |
| pycparser                  | 1.22 sec                                                         | 1.77 sec: 1.45x slower                                                      |
| html5lib                   | 74.7 ms                                                          | 109 ms: 1.47x slower                                                        |
| genshi_xml                 | 58.1 ms                                                          | 85.5 ms: 1.47x slower                                                       |
| 2to3                       | 291 ms                                                           | 437 ms: 1.50x slower                                                        |
| nqueens                    | 88.4 ms                                                          | 133 ms: 1.50x slower                                                        |
| richards                   | 53.4 ms                                                          | 82.7 ms: 1.55x slower                                                       |
| sympy_str                  | 295 ms                                                           | 456 ms: 1.55x slower                                                        |
| thrift                     | 880 us                                                           | 1.38 ms: 1.57x slower                                                       |
| sqlglot_normalize          | 120 ms                                                           | 189 ms: 1.57x slower                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 95.4 ms: 1.60x slower                                                       |
| pyflate                    | 482 ms                                                           | 774 ms: 1.61x slower                                                        |
| regex_compile              | 144 ms                                                           | 233 ms: 1.62x slower                                                        |
| richards_super             | 61.2 ms                                                          | 99.3 ms: 1.62x slower                                                       |
| xml_etree_process          | 59.7 ms                                                          | 97.6 ms: 1.63x slower                                                       |
| sympy_expand               | 501 ms                                                           | 823 ms: 1.64x slower                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 122 ms: 1.65x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 282 us: 1.65x slower                                                        |
| fannkuch                   | 353 ms                                                           | 583 ms: 1.65x slower                                                        |
| genshi_text                | 25.9 ms                                                          | 44.1 ms: 1.70x slower                                                       |
| sympy_sum                  | 155 ms                                                           | 265 ms: 1.71x slower                                                        |
| spectral_norm              | 97.3 ms                                                          | 171 ms: 1.76x slower                                                        |
| pprint_safe_repr           | 818 ms                                                           | 1.45 sec: 1.77x slower                                                      |
| logging_format             | 7.11 us                                                          | 12.6 us: 1.77x slower                                                       |
| django_template            | 39.0 ms                                                          | 69.3 ms: 1.78x slower                                                       |
| comprehensions             | 17.0 us                                                          | 30.2 us: 1.78x slower                                                       |
| pprint_pformat             | 1.66 sec                                                         | 3.00 sec: 1.81x slower                                                      |
| unpickle_pure_python       | 224 us                                                           | 406 us: 1.81x slower                                                        |
| logging_simple             | 6.40 us                                                          | 11.6 us: 1.81x slower                                                       |
| float                      | 80.2 ms                                                          | 146 ms: 1.82x slower                                                        |
| bench_thread_pool          | 908 us                                                           | 1.70 ms: 1.88x slower                                                       |
| hexiom                     | 6.35 ms                                                          | 11.9 ms: 1.88x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 3.39 ms: 1.92x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 186 ns: 1.93x slower                                                        |
| pickle_pure_python         | 307 us                                                           | 598 us: 1.94x slower                                                        |
| go                         | 165 ms                                                           | 333 ms: 2.02x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 134 ms: 2.04x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 2.87 ms: 2.06x slower                                                       |
| chaos                      | 59.6 ms                                                          | 127 ms: 2.13x slower                                                        |
| mako                       | 10.4 ms                                                          | 22.2 ms: 2.14x slower                                                       |
| scimark_sor                | 119 ms                                                           | 256 ms: 2.16x slower                                                        |
| nbody                      | 87.8 ms                                                          | 201 ms: 2.29x slower                                                        |
| raytrace                   | 260 ms                                                           | 610 ms: 2.34x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 8.31 ms: 2.46x slower                                                       |
| scimark_lu                 | 97.5 ms                                                          | 248 ms: 2.54x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.44x slower                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.34x
- 95% likely to have a slowdown of 1.33x
- 99% likely to have a slowdown of 1.31x

# Memory
- memory change: 1.16x