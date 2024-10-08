# Results vs. base

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-aarch64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.60x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                                                                            | 516 ms: 1.70x slower                                                                                                    |
| docutils       | 3.11 sec                                                                                                          | 4.15 sec: 1.33x slower                                                                                                  |
| html5lib       | 66.4 ms                                                                                                           | 121 ms: 1.83x slower                                                                                                    |
| tornado_http   | 129 ms                                                                                                            | 200 ms: 1.55x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.59x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets         | 659 ms                                                                                                            | 672 ms: 1.02x slower                                                                                                    |
| asyncio_tcp_ssl            | 2.24 sec                                                                                                          | 2.46 sec: 1.10x slower                                                                                                  |
| asyncio_tcp                | 580 ms                                                                                                            | 660 ms: 1.14x slower                                                                                                    |
| async_tree_io_tg           | 1.13 sec                                                                                                          | 1.35 sec: 1.19x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 712 ms                                                                                                            | 871 ms: 1.22x slower                                                                                                    |
| async_tree_io              | 1.13 sec                                                                                                          | 1.44 sec: 1.28x slower                                                                                                  |
| async_tree_memoization_tg  | 543 ms                                                                                                            | 696 ms: 1.28x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 730 ms                                                                                                            | 942 ms: 1.29x slower                                                                                                    |
| coroutines                 | 28.7 ms                                                                                                           | 39.0 ms: 1.36x slower                                                                                                   |
| async_tree_memoization     | 563 ms                                                                                                            | 767 ms: 1.36x slower                                                                                                    |
| async_tree_none_tg         | 413 ms                                                                                                            | 566 ms: 1.37x slower                                                                                                    |
| async_generators           | 493 ms                                                                                                            | 692 ms: 1.41x slower                                                                                                    |
| async_tree_none            | 444 ms                                                                                                            | 631 ms: 1.42x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.26x slower                                                                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 92.0 ms                                                                                                           | 207 ms: 2.26x slower                                                                                                    |
| nbody          | 109 ms                                                                                                            | 285 ms: 2.61x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.81x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 4.92 ms                                                                                                           | 4.41 ms: 1.12x faster                                                                                                   |
| regex_v8       | 30.4 ms                                                                                                           | 32.8 ms: 1.08x slower                                                                                                   |
| regex_compile  | 128 ms                                                                                                            | 256 ms: 1.99x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.17x slower                                                                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_parse      | 188 ms                                                                                                            | 177 ms: 1.06x faster                                                                                                    |
| xml_etree_iterparse  | 145 ms                                                                                                            | 155 ms: 1.07x slower                                                                                                    |
| json_loads           | 32.8 us                                                                                                           | 39.1 us: 1.19x slower                                                                                                   |
| json_dumps           | 13.4 ms                                                                                                           | 17.9 ms: 1.33x slower                                                                                                   |
| xml_etree_generate   | 112 ms                                                                                                            | 162 ms: 1.45x slower                                                                                                    |
| xml_etree_process    | 80.2 ms                                                                                                           | 130 ms: 1.63x slower                                                                                                    |
| tomli_loads          | 2.55 sec                                                                                                          | 4.19 sec: 1.64x slower                                                                                                  |
| pickle_pure_python   | 360 us                                                                                                            | 781 us: 2.17x slower                                                                                                    |
| unpickle_pure_python | 251 us                                                                                                            | 550 us: 2.19x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.46x slower                                                                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.89 ms                                                                                                           | 11.7 ms: 1.32x slower                                                                                                   |
| python_startup         | 13.2 ms                                                                                                           | 17.6 ms: 1.33x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.32x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 61.2 ms                                                                                                           | 105 ms: 1.71x slower                                                                                                    |
| genshi_text     | 28.0 ms                                                                                                           | 52.8 ms: 1.89x slower                                                                                                   |
| django_template | 41.6 ms                                                                                                           | 82.3 ms: 1.98x slower                                                                                                   |
| mako            | 13.3 ms                                                                                                           | 29.1 ms: 2.18x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.93x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| create_gc_cycles           | 2.33 ms                                                                                                           | 1.60 ms: 1.46x faster                                                                                                   |
| gc_traversal               | 4.82 ms                                                                                                           | 3.45 ms: 1.40x faster                                                                                                   |
| bench_mp_pool              | 7.15 ms                                                                                                           | 6.14 ms: 1.16x faster                                                                                                   |
| regex_effbot               | 4.92 ms                                                                                                           | 4.41 ms: 1.12x faster                                                                                                   |
| xml_etree_parse            | 188 ms                                                                                                            | 177 ms: 1.06x faster                                                                                                    |
| asyncio_websockets         | 659 ms                                                                                                            | 672 ms: 1.02x slower                                                                                                    |
| xml_etree_iterparse        | 145 ms                                                                                                            | 155 ms: 1.07x slower                                                                                                    |
| regex_v8                   | 30.4 ms                                                                                                           | 32.8 ms: 1.08x slower                                                                                                   |
| asyncio_tcp_ssl            | 2.24 sec                                                                                                          | 2.46 sec: 1.10x slower                                                                                                  |
| asyncio_tcp                | 580 ms                                                                                                            | 660 ms: 1.14x slower                                                                                                    |
| async_tree_io_tg           | 1.13 sec                                                                                                          | 1.35 sec: 1.19x slower                                                                                                  |
| json_loads                 | 32.8 us                                                                                                           | 39.1 us: 1.19x slower                                                                                                   |
| json                       | 5.74 ms                                                                                                           | 6.96 ms: 1.21x slower                                                                                                   |
| pathlib                    | 21.3 ms                                                                                                           | 26.0 ms: 1.22x slower                                                                                                   |
| async_tree_cpu_io_mixed_tg | 712 ms                                                                                                            | 871 ms: 1.22x slower                                                                                                    |
| telco                      | 9.95 ms                                                                                                           | 12.4 ms: 1.24x slower                                                                                                   |
| async_tree_io              | 1.13 sec                                                                                                          | 1.44 sec: 1.28x slower                                                                                                  |
| async_tree_memoization_tg  | 543 ms                                                                                                            | 696 ms: 1.28x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 730 ms                                                                                                            | 942 ms: 1.29x slower                                                                                                    |
| mdp                        | 3.33 sec                                                                                                          | 4.33 sec: 1.30x slower                                                                                                  |
| python_startup_no_site     | 8.89 ms                                                                                                           | 11.7 ms: 1.32x slower                                                                                                   |
| python_startup             | 13.2 ms                                                                                                           | 17.6 ms: 1.33x slower                                                                                                   |
| docutils                   | 3.11 sec                                                                                                          | 4.15 sec: 1.33x slower                                                                                                  |
| json_dumps                 | 13.4 ms                                                                                                           | 17.9 ms: 1.33x slower                                                                                                   |
| scimark_fft                | 438 ms                                                                                                            | 593 ms: 1.36x slower                                                                                                    |
| coroutines                 | 28.7 ms                                                                                                           | 39.0 ms: 1.36x slower                                                                                                   |
| async_tree_memoization     | 563 ms                                                                                                            | 767 ms: 1.36x slower                                                                                                    |
| async_tree_none_tg         | 413 ms                                                                                                            | 566 ms: 1.37x slower                                                                                                    |
| scimark_sparse_mat_mult    | 6.37 ms                                                                                                           | 8.82 ms: 1.39x slower                                                                                                   |
| coverage                   | 97.4 ms                                                                                                           | 135 ms: 1.39x slower                                                                                                    |
| async_generators           | 493 ms                                                                                                            | 692 ms: 1.41x slower                                                                                                    |
| async_tree_none            | 444 ms                                                                                                            | 631 ms: 1.42x slower                                                                                                    |
| pylint                     | 356 ms                                                                                                            | 508 ms: 1.43x slower                                                                                                    |
| xml_etree_generate         | 112 ms                                                                                                            | 162 ms: 1.45x slower                                                                                                    |
| meteor_contest             | 114 ms                                                                                                            | 173 ms: 1.52x slower                                                                                                    |
| bench_thread_pool          | 1.23 ms                                                                                                           | 1.87 ms: 1.52x slower                                                                                                   |
| nqueens                    | 99.5 ms                                                                                                           | 152 ms: 1.52x slower                                                                                                    |
| tornado_http               | 129 ms                                                                                                            | 200 ms: 1.55x slower                                                                                                    |
| fannkuch                   | 476 ms                                                                                                            | 758 ms: 1.59x slower                                                                                                    |
| generators                 | 35.3 ms                                                                                                           | 57.0 ms: 1.61x slower                                                                                                   |
| xml_etree_process          | 80.2 ms                                                                                                           | 130 ms: 1.63x slower                                                                                                    |
| bpe_tokeniser              | 5.84 sec                                                                                                          | 9.52 sec: 1.63x slower                                                                                                  |
| tomli_loads                | 2.55 sec                                                                                                          | 4.19 sec: 1.64x slower                                                                                                  |
| sympy_integrate            | 21.1 ms                                                                                                           | 34.9 ms: 1.65x slower                                                                                                   |
| spectral_norm              | 140 ms                                                                                                            | 233 ms: 1.67x slower                                                                                                    |
| pycparser                  | 1.23 sec                                                                                                          | 2.06 sec: 1.68x slower                                                                                                  |
| deepcopy                   | 335 us                                                                                                            | 566 us: 1.69x slower                                                                                                    |
| typing_runtime_protocols   | 197 us                                                                                                            | 334 us: 1.70x slower                                                                                                    |
| 2to3                       | 304 ms                                                                                                            | 516 ms: 1.70x slower                                                                                                    |
| genshi_xml                 | 61.2 ms                                                                                                           | 105 ms: 1.71x slower                                                                                                    |
| crypto_pyaes               | 81.9 ms                                                                                                           | 141 ms: 1.73x slower                                                                                                    |
| thrift                     | 977 us                                                                                                            | 1.69 ms: 1.73x slower                                                                                                   |
| pyflate                    | 580 ms                                                                                                            | 1.02 sec: 1.77x slower                                                                                                  |
| deepcopy_reduce            | 3.43 us                                                                                                           | 6.07 us: 1.77x slower                                                                                                   |
| sqlglot_normalize          | 127 ms                                                                                                            | 231 ms: 1.81x slower                                                                                                    |
| html5lib                   | 66.4 ms                                                                                                           | 121 ms: 1.83x slower                                                                                                    |
| sqlglot_optimize           | 62.4 ms                                                                                                           | 114 ms: 1.84x slower                                                                                                    |
| pprint_safe_repr           | 952 ms                                                                                                            | 1.77 sec: 1.86x slower                                                                                                  |
| pprint_pformat             | 1.95 sec                                                                                                          | 3.64 sec: 1.87x slower                                                                                                  |
| deepcopy_memo              | 38.2 us                                                                                                           | 71.9 us: 1.88x slower                                                                                                   |
| genshi_text                | 28.0 ms                                                                                                           | 52.8 ms: 1.89x slower                                                                                                   |
| sympy_str                  | 268 ms                                                                                                            | 514 ms: 1.91x slower                                                                                                    |
| django_template            | 41.6 ms                                                                                                           | 82.3 ms: 1.98x slower                                                                                                   |
| regex_compile              | 128 ms                                                                                                            | 256 ms: 1.99x slower                                                                                                    |
| comprehensions             | 20.6 us                                                                                                           | 41.3 us: 2.01x slower                                                                                                   |
| sympy_expand               | 463 ms                                                                                                            | 951 ms: 2.06x slower                                                                                                    |
| logging_format             | 7.67 us                                                                                                           | 15.8 us: 2.06x slower                                                                                                   |
| logging_simple             | 6.97 us                                                                                                           | 14.7 us: 2.11x slower                                                                                                   |
| sympy_sum                  | 147 ms                                                                                                            | 313 ms: 2.13x slower                                                                                                    |
| pickle_pure_python         | 360 us                                                                                                            | 781 us: 2.17x slower                                                                                                    |
| mako                       | 13.3 ms                                                                                                           | 29.1 ms: 2.18x slower                                                                                                   |
| scimark_monte_carlo        | 82.0 ms                                                                                                           | 179 ms: 2.18x slower                                                                                                    |
| unpickle_pure_python       | 251 us                                                                                                            | 550 us: 2.19x slower                                                                                                    |
| scimark_sor                | 157 ms                                                                                                            | 345 ms: 2.19x slower                                                                                                    |
| logging_silent             | 129 ns                                                                                                            | 285 ns: 2.20x slower                                                                                                    |
| hexiom                     | 7.15 ms                                                                                                           | 15.8 ms: 2.21x slower                                                                                                   |
| float                      | 92.0 ms                                                                                                           | 207 ms: 2.26x slower                                                                                                    |
| richards                   | 52.3 ms                                                                                                           | 121 ms: 2.32x slower                                                                                                    |
| richards_super             | 58.7 ms                                                                                                           | 139 ms: 2.37x slower                                                                                                    |
| sqlglot_transpile          | 1.79 ms                                                                                                           | 4.29 ms: 2.40x slower                                                                                                   |
| chaos                      | 67.5 ms                                                                                                           | 162 ms: 2.40x slower                                                                                                    |
| scimark_lu                 | 136 ms                                                                                                            | 343 ms: 2.52x slower                                                                                                    |
| nbody                      | 109 ms                                                                                                            | 285 ms: 2.61x slower                                                                                                    |
| sqlglot_parse              | 1.41 ms                                                                                                           | 3.70 ms: 2.63x slower                                                                                                   |
| go                         | 162 ms                                                                                                            | 448 ms: 2.77x slower                                                                                                    |
| raytrace                   | 296 ms                                                                                                            | 826 ms: 2.79x slower                                                                                                    |
| deltablue                  | 3.84 ms                                                                                                           | 12.8 ms: 3.35x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.60x slower                                                                                                            |

Benchmark hidden because not significant (2): regex_dna, pidigits
Ignored benchmarks (1) of results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: dask

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.49x
- 95% likely to have a slowdown of 1.46x
- 99% likely to have a slowdown of 1.41x

# Memory
- memory change: 1.16x