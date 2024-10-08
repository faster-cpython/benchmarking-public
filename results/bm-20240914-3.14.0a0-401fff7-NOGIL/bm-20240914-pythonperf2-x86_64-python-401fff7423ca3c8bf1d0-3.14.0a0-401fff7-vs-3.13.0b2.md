# Results vs. 3.13.0b2

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-x86_64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.38x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 424 ms: 1.45x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.37 sec: 1.13x slower                                                      |
| html5lib       | 74.7 ms                                                          | 105 ms: 1.41x slower                                                        |
| tornado_http   | 119 ms                                                           | 166 ms: 1.39x slower                                                        |
| Geometric mean | (ref)                                                            | 1.34x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 878 ms: 1.02x faster                                                        |
| async_tree_io              | 873 ms                                                           | 928 ms: 1.06x slower                                                        |
| async_tree_none_tg         | 340 ms                                                           | 364 ms: 1.07x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 625 ms: 1.09x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 467 ms: 1.11x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 511 ms: 1.11x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 673 ms: 1.11x slower                                                        |
| async_tree_none            | 365 ms                                                           | 411 ms: 1.12x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.08x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 249 ms: 1.02x faster                                                        |
| float          | 80.2 ms                                                          | 142 ms: 1.77x slower                                                        |
| nbody          | 87.8 ms                                                          | 191 ms: 2.18x slower                                                        |
| Geometric mean | (ref)                                                            | 1.56x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 250 ms: 1.00x slower                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.61 ms: 1.06x slower                                                       |
| regex_v8       | 26.0 ms                                                          | 28.0 ms: 1.08x slower                                                       |
| regex_compile  | 144 ms                                                           | 224 ms: 1.56x slower                                                        |
| Geometric mean | (ref)                                                            | 1.16x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                           | 139 ms: 1.03x faster                                                        |
| pickle               | 10.6 us                                                          | 10.4 us: 1.02x faster                                                       |
| pickle_dict          | 32.8 us                                                          | 32.6 us: 1.01x faster                                                       |
| pickle_list          | 4.44 us                                                          | 4.53 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 107 ms: 1.04x slower                                                        |
| unpickle             | 15.7 us                                                          | 17.4 us: 1.11x slower                                                       |
| unpickle_list        | 4.70 us                                                          | 5.31 us: 1.13x slower                                                       |
| json_loads           | 25.0 us                                                          | 28.8 us: 1.15x slower                                                       |
| json_dumps           | 10.8 ms                                                          | 13.9 ms: 1.29x slower                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 113 ms: 1.32x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 3.33 sec: 1.38x slower                                                      |
| xml_etree_process    | 59.7 ms                                                          | 91.6 ms: 1.53x slower                                                       |
| unpickle_pure_python | 224 us                                                           | 399 us: 1.78x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 583 us: 1.90x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.23x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 17.5 ms: 1.32x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 11.8 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.33x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 82.4 ms: 1.42x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 42.3 ms: 1.63x slower                                                       |
| django_template | 39.0 ms                                                          | 66.4 ms: 1.71x slower                                                       |
| mako            | 10.4 ms                                                          | 21.4 ms: 2.06x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.69x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.69 ms                                                          | 3.04 ms: 1.54x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.67 ms: 1.20x faster                                                       |
| asyncio_websockets         | 395 ms                                                           | 379 ms: 1.04x faster                                                        |
| xml_etree_parse            | 144 ms                                                           | 139 ms: 1.03x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 878 ms: 1.02x faster                                                        |
| pickle                     | 10.6 us                                                          | 10.4 us: 1.02x faster                                                       |
| pidigits                   | 254 ms                                                           | 249 ms: 1.02x faster                                                        |
| pickle_dict                | 32.8 us                                                          | 32.6 us: 1.01x faster                                                       |
| regex_dna                  | 249 ms                                                           | 250 ms: 1.00x slower                                                        |
| pickle_list                | 4.44 us                                                          | 4.53 us: 1.02x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 107 ms: 1.04x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.61 ms: 1.06x slower                                                       |
| async_tree_io              | 873 ms                                                           | 928 ms: 1.06x slower                                                        |
| async_tree_none_tg         | 340 ms                                                           | 364 ms: 1.07x slower                                                        |
| sqlite_synth               | 2.80 us                                                          | 3.00 us: 1.07x slower                                                       |
| regex_v8                   | 26.0 ms                                                          | 28.0 ms: 1.08x slower                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 625 ms: 1.09x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 467 ms: 1.11x slower                                                        |
| unpickle                   | 15.7 us                                                          | 17.4 us: 1.11x slower                                                       |
| async_tree_memoization     | 460 ms                                                           | 511 ms: 1.11x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 673 ms: 1.11x slower                                                        |
| async_tree_none            | 365 ms                                                           | 411 ms: 1.12x slower                                                        |
| json                       | 5.35 ms                                                          | 6.03 ms: 1.13x slower                                                       |
| unpickle_list              | 4.70 us                                                          | 5.31 us: 1.13x slower                                                       |
| docutils                   | 2.98 sec                                                         | 3.37 sec: 1.13x slower                                                      |
| deepcopy                   | 377 us                                                           | 430 us: 1.14x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.80 sec: 1.14x slower                                                      |
| pathlib                    | 17.1 ms                                                          | 19.6 ms: 1.14x slower                                                       |
| json_loads                 | 25.0 us                                                          | 28.8 us: 1.15x slower                                                       |
| asyncio_tcp                | 378 ms                                                           | 452 ms: 1.20x slower                                                        |
| generators                 | 33.5 ms                                                          | 41.4 ms: 1.24x slower                                                       |
| telco                      | 8.40 ms                                                          | 10.4 ms: 1.24x slower                                                       |
| coroutines                 | 22.0 ms                                                          | 27.8 ms: 1.27x slower                                                       |
| pylint                     | 339 ms                                                           | 433 ms: 1.28x slower                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 6.61 sec: 1.29x slower                                                      |
| coverage                   | 83.5 ms                                                          | 108 ms: 1.29x slower                                                        |
| json_dumps                 | 10.8 ms                                                          | 13.9 ms: 1.29x slower                                                       |
| scimark_fft                | 312 ms                                                           | 407 ms: 1.30x slower                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 5.63 ms: 1.31x slower                                                       |
| meteor_contest             | 128 ms                                                           | 169 ms: 1.32x slower                                                        |
| deepcopy_memo              | 37.3 us                                                          | 49.2 us: 1.32x slower                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 113 ms: 1.32x slower                                                        |
| mdp                        | 2.46 sec                                                         | 3.25 sec: 1.32x slower                                                      |
| dulwich_log                | 67.3 ms                                                          | 89.1 ms: 1.32x slower                                                       |
| python_startup             | 13.2 ms                                                          | 17.5 ms: 1.32x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 11.8 ms: 1.34x slower                                                       |
| async_generators           | 363 ms                                                           | 489 ms: 1.35x slower                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 4.61 us: 1.36x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 3.33 sec: 1.38x slower                                                      |
| sympy_integrate            | 23.2 ms                                                          | 32.2 ms: 1.39x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.70 sec: 1.39x slower                                                      |
| tornado_http               | 119 ms                                                           | 166 ms: 1.39x slower                                                        |
| html5lib                   | 74.7 ms                                                          | 105 ms: 1.41x slower                                                        |
| genshi_xml                 | 58.1 ms                                                          | 82.4 ms: 1.42x slower                                                       |
| 2to3                       | 291 ms                                                           | 424 ms: 1.45x slower                                                        |
| nqueens                    | 88.4 ms                                                          | 129 ms: 1.46x slower                                                        |
| richards                   | 53.4 ms                                                          | 79.9 ms: 1.50x slower                                                       |
| sqlglot_normalize          | 120 ms                                                           | 180 ms: 1.50x slower                                                        |
| sympy_str                  | 295 ms                                                           | 446 ms: 1.51x slower                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 91.1 ms: 1.53x slower                                                       |
| xml_etree_process          | 59.7 ms                                                          | 91.6 ms: 1.53x slower                                                       |
| thrift                     | 880 us                                                           | 1.36 ms: 1.54x slower                                                       |
| typing_runtime_protocols   | 171 us                                                           | 263 us: 1.54x slower                                                        |
| regex_compile              | 144 ms                                                           | 224 ms: 1.56x slower                                                        |
| richards_super             | 61.2 ms                                                          | 96.3 ms: 1.57x slower                                                       |
| pyflate                    | 482 ms                                                           | 760 ms: 1.58x slower                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 118 ms: 1.60x slower                                                        |
| sympy_expand               | 501 ms                                                           | 811 ms: 1.62x slower                                                        |
| fannkuch                   | 353 ms                                                           | 575 ms: 1.63x slower                                                        |
| genshi_text                | 25.9 ms                                                          | 42.3 ms: 1.63x slower                                                       |
| spectral_norm              | 97.3 ms                                                          | 160 ms: 1.64x slower                                                        |
| pprint_safe_repr           | 818 ms                                                           | 1.37 sec: 1.67x slower                                                      |
| sympy_sum                  | 155 ms                                                           | 260 ms: 1.68x slower                                                        |
| pprint_pformat             | 1.66 sec                                                         | 2.81 sec: 1.69x slower                                                      |
| django_template            | 39.0 ms                                                          | 66.4 ms: 1.71x slower                                                       |
| comprehensions             | 17.0 us                                                          | 29.1 us: 1.72x slower                                                       |
| go                         | 165 ms                                                           | 285 ms: 1.73x slower                                                        |
| float                      | 80.2 ms                                                          | 142 ms: 1.77x slower                                                        |
| logging_format             | 7.11 us                                                          | 12.6 us: 1.78x slower                                                       |
| unpickle_pure_python       | 224 us                                                           | 399 us: 1.78x slower                                                        |
| hexiom                     | 6.35 ms                                                          | 11.4 ms: 1.80x slower                                                       |
| logging_simple             | 6.40 us                                                          | 11.6 us: 1.82x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 177 ns: 1.84x slower                                                        |
| bench_thread_pool          | 908 us                                                           | 1.70 ms: 1.87x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 583 us: 1.90x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 3.35 ms: 1.90x slower                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 133 ms: 2.03x slower                                                        |
| chaos                      | 59.6 ms                                                          | 122 ms: 2.04x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 2.84 ms: 2.04x slower                                                       |
| scimark_sor                | 119 ms                                                           | 244 ms: 2.05x slower                                                        |
| mako                       | 10.4 ms                                                          | 21.4 ms: 2.06x slower                                                       |
| nbody                      | 87.8 ms                                                          | 191 ms: 2.18x slower                                                        |
| raytrace                   | 260 ms                                                           | 596 ms: 2.29x slower                                                        |
| scimark_lu                 | 97.5 ms                                                          | 228 ms: 2.34x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 8.16 ms: 2.42x slower                                                       |
| Geometric mean             | (ref)                                                            | 1.38x slower                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240914-3.14.0a0-401fff7-NOGIL/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.32x
- 95% likely to have a slowdown of 1.31x
- 99% likely to have a slowdown of 1.28x

# Memory
- memory change: 1.16x