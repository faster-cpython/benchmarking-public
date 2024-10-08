# Results vs. 3.13.0b2

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-x86_64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.44x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 437 ms: 1.50x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.44 sec: 1.15x slower                                                      |
| html5lib       | 74.7 ms                                                          | 107 ms: 1.43x slower                                                        |
| tornado_http   | 119 ms                                                           | 169 ms: 1.41x slower                                                        |
| Geometric mean | (ref)                                                            | 1.37x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 909 ms: 1.01x slower                                                        |
| async_tree_none_tg         | 340 ms                                                           | 373 ms: 1.10x slower                                                        |
| async_tree_io              | 873 ms                                                           | 963 ms: 1.10x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 645 ms: 1.13x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 686 ms: 1.13x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 524 ms: 1.14x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 484 ms: 1.15x slower                                                        |
| async_tree_none            | 365 ms                                                           | 421 ms: 1.15x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.11x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| float          | 80.2 ms                                                          | 145 ms: 1.81x slower                                                        |
| nbody          | 87.8 ms                                                          | 195 ms: 2.22x slower                                                        |
| Geometric mean | (ref)                                                            | 1.58x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 241 ms: 1.04x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.54 ms: 1.04x slower                                                       |
| regex_v8       | 26.0 ms                                                          | 27.3 ms: 1.05x slower                                                       |
| regex_compile  | 144 ms                                                           | 231 ms: 1.60x slower                                                        |
| Geometric mean | (ref)                                                            | 1.14x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                           | 137 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 110 ms: 1.08x slower                                                        |
| json_loads           | 25.0 us                                                          | 29.5 us: 1.18x slower                                                       |
| json_dumps           | 10.8 ms                                                          | 14.2 ms: 1.32x slower                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 118 ms: 1.37x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 3.38 sec: 1.41x slower                                                      |
| xml_etree_process    | 59.7 ms                                                          | 96.7 ms: 1.62x slower                                                       |
| unpickle_pure_python | 224 us                                                           | 417 us: 1.86x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 593 us: 1.93x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.38x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 17.4 ms: 1.32x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 12.0 ms: 1.35x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.33x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 83.9 ms: 1.45x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 43.6 ms: 1.68x slower                                                       |
| django_template | 39.0 ms                                                          | 68.9 ms: 1.77x slower                                                       |
| mako            | 10.4 ms                                                          | 21.9 ms: 2.11x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.74x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.69 ms                                                          | 2.99 ms: 1.57x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.67 ms: 1.20x faster                                                       |
| xml_etree_parse            | 144 ms                                                           | 137 ms: 1.05x faster                                                        |
| regex_dna                  | 249 ms                                                           | 241 ms: 1.04x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 385 ms: 1.02x faster                                                        |
| pidigits                   | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 909 ms: 1.01x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.54 ms: 1.04x slower                                                       |
| regex_v8                   | 26.0 ms                                                          | 27.3 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 110 ms: 1.08x slower                                                        |
| async_tree_none_tg         | 340 ms                                                           | 373 ms: 1.10x slower                                                        |
| async_tree_io              | 873 ms                                                           | 963 ms: 1.10x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 645 ms: 1.13x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 686 ms: 1.13x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 524 ms: 1.14x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 484 ms: 1.15x slower                                                        |
| docutils                   | 2.98 sec                                                         | 3.44 sec: 1.15x slower                                                      |
| async_tree_none            | 365 ms                                                           | 421 ms: 1.15x slower                                                        |
| json                       | 5.35 ms                                                          | 6.19 ms: 1.16x slower                                                       |
| pathlib                    | 17.1 ms                                                          | 19.9 ms: 1.16x slower                                                       |
| json_loads                 | 25.0 us                                                          | 29.5 us: 1.18x slower                                                       |
| asyncio_tcp                | 378 ms                                                           | 451 ms: 1.19x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.90 sec: 1.20x slower                                                      |
| deepcopy                   | 377 us                                                           | 455 us: 1.21x slower                                                        |
| generators                 | 33.5 ms                                                          | 41.3 ms: 1.23x slower                                                       |
| telco                      | 8.40 ms                                                          | 10.6 ms: 1.26x slower                                                       |
| scimark_fft                | 312 ms                                                           | 399 ms: 1.28x slower                                                        |
| pylint                     | 339 ms                                                           | 441 ms: 1.30x slower                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 5.57 ms: 1.30x slower                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 6.68 sec: 1.30x slower                                                      |
| coverage                   | 83.5 ms                                                          | 109 ms: 1.31x slower                                                        |
| python_startup             | 13.2 ms                                                          | 17.4 ms: 1.32x slower                                                       |
| mdp                        | 2.46 sec                                                         | 3.24 sec: 1.32x slower                                                      |
| json_dumps                 | 10.8 ms                                                          | 14.2 ms: 1.32x slower                                                       |
| coroutines                 | 22.0 ms                                                          | 29.2 ms: 1.33x slower                                                       |
| dulwich_log                | 67.3 ms                                                          | 90.5 ms: 1.34x slower                                                       |
| meteor_contest             | 128 ms                                                           | 172 ms: 1.34x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 12.0 ms: 1.35x slower                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 118 ms: 1.37x slower                                                        |
| async_generators           | 363 ms                                                           | 501 ms: 1.38x slower                                                        |
| sympy_integrate            | 23.2 ms                                                          | 32.1 ms: 1.39x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 3.38 sec: 1.41x slower                                                      |
| tornado_http               | 119 ms                                                           | 169 ms: 1.41x slower                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 4.83 us: 1.43x slower                                                       |
| html5lib                   | 74.7 ms                                                          | 107 ms: 1.43x slower                                                        |
| deepcopy_memo              | 37.3 us                                                          | 53.4 us: 1.43x slower                                                       |
| genshi_xml                 | 58.1 ms                                                          | 83.9 ms: 1.45x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.77 sec: 1.45x slower                                                      |
| nqueens                    | 88.4 ms                                                          | 132 ms: 1.49x slower                                                        |
| 2to3                       | 291 ms                                                           | 437 ms: 1.50x slower                                                        |
| sympy_str                  | 295 ms                                                           | 455 ms: 1.54x slower                                                        |
| thrift                     | 880 us                                                           | 1.37 ms: 1.55x slower                                                       |
| richards                   | 53.4 ms                                                          | 83.2 ms: 1.56x slower                                                       |
| sqlglot_normalize          | 120 ms                                                           | 192 ms: 1.59x slower                                                        |
| regex_compile              | 144 ms                                                           | 231 ms: 1.60x slower                                                        |
| pyflate                    | 482 ms                                                           | 771 ms: 1.60x slower                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 95.9 ms: 1.61x slower                                                       |
| xml_etree_process          | 59.7 ms                                                          | 96.7 ms: 1.62x slower                                                       |
| fannkuch                   | 353 ms                                                           | 571 ms: 1.62x slower                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 120 ms: 1.63x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 279 us: 1.64x slower                                                        |
| sympy_expand               | 501 ms                                                           | 827 ms: 1.65x slower                                                        |
| richards_super             | 61.2 ms                                                          | 101 ms: 1.66x slower                                                        |
| genshi_text                | 25.9 ms                                                          | 43.6 ms: 1.68x slower                                                       |
| sympy_sum                  | 155 ms                                                           | 264 ms: 1.70x slower                                                        |
| spectral_norm              | 97.3 ms                                                          | 170 ms: 1.75x slower                                                        |
| logging_format             | 7.11 us                                                          | 12.5 us: 1.75x slower                                                       |
| comprehensions             | 17.0 us                                                          | 29.7 us: 1.75x slower                                                       |
| pprint_safe_repr           | 818 ms                                                           | 1.44 sec: 1.76x slower                                                      |
| go                         | 165 ms                                                           | 291 ms: 1.76x slower                                                        |
| django_template            | 39.0 ms                                                          | 68.9 ms: 1.77x slower                                                       |
| pprint_pformat             | 1.66 sec                                                         | 2.99 sec: 1.80x slower                                                      |
| float                      | 80.2 ms                                                          | 145 ms: 1.81x slower                                                        |
| logging_simple             | 6.40 us                                                          | 11.6 us: 1.81x slower                                                       |
| unpickle_pure_python       | 224 us                                                           | 417 us: 1.86x slower                                                        |
| hexiom                     | 6.35 ms                                                          | 11.9 ms: 1.87x slower                                                       |
| bench_thread_pool          | 908 us                                                           | 1.73 ms: 1.90x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 3.39 ms: 1.92x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 593 us: 1.93x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 191 ns: 1.99x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 134 ms: 2.04x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 2.87 ms: 2.06x slower                                                       |
| chaos                      | 59.6 ms                                                          | 125 ms: 2.10x slower                                                        |
| scimark_sor                | 119 ms                                                           | 250 ms: 2.11x slower                                                        |
| mako                       | 10.4 ms                                                          | 21.9 ms: 2.11x slower                                                       |
| nbody                      | 87.8 ms                                                          | 195 ms: 2.22x slower                                                        |
| raytrace                   | 260 ms                                                           | 611 ms: 2.35x slower                                                        |
| scimark_lu                 | 97.5 ms                                                          | 237 ms: 2.43x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 8.35 ms: 2.47x slower                                                       |
| Geometric mean             | (ref)                                                            | 1.44x slower                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.33x
- 95% likely to have a slowdown of 1.32x
- 99% likely to have a slowdown of 1.30x

# Memory
- memory change: 1.16x