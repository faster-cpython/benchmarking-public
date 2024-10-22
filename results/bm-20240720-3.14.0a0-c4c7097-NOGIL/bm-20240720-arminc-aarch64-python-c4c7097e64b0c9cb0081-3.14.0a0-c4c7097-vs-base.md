# Results vs. base

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: linux-aarch64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.60x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.42x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-NOGIL/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 303 ms                                                                                                            | 513 ms: 1.69x slower                                                                                                    |
| docutils       | 3.09 sec                                                                                                          | 4.11 sec: 1.33x slower                                                                                                  |
| html5lib       | 68.0 ms                                                                                                           | 121 ms: 1.78x slower                                                                                                    |
| tornado_http   | 130 ms                                                                                                            | 207 ms: 1.60x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.59x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-NOGIL/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets         | 657 ms                                                                                                            | 672 ms: 1.02x slower                                                                                                    |
| asyncio_tcp_ssl            | 2.20 sec                                                                                                          | 2.46 sec: 1.12x slower                                                                                                  |
| asyncio_tcp                | 572 ms                                                                                                            | 671 ms: 1.17x slower                                                                                                    |
| async_tree_io_tg           | 1.14 sec                                                                                                          | 1.36 sec: 1.19x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 718 ms                                                                                                            | 859 ms: 1.20x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 732 ms                                                                                                            | 912 ms: 1.25x slower                                                                                                    |
| async_tree_io              | 1.12 sec                                                                                                          | 1.39 sec: 1.25x slower                                                                                                  |
| async_tree_memoization_tg  | 536 ms                                                                                                            | 688 ms: 1.28x slower                                                                                                    |
| async_tree_memoization     | 574 ms                                                                                                            | 739 ms: 1.29x slower                                                                                                    |
| async_tree_none_tg         | 413 ms                                                                                                            | 560 ms: 1.35x slower                                                                                                    |
| async_tree_none            | 446 ms                                                                                                            | 604 ms: 1.36x slower                                                                                                    |
| coroutines                 | 28.2 ms                                                                                                           | 38.5 ms: 1.36x slower                                                                                                   |
| async_generators           | 494 ms                                                                                                            | 686 ms: 1.39x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.24x slower                                                                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-NOGIL/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 91.9 ms                                                                                                           | 209 ms: 2.28x slower                                                                                                    |
| nbody          | 114 ms                                                                                                            | 290 ms: 2.54x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.80x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-NOGIL/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 4.91 ms                                                                                                           | 4.43 ms: 1.11x faster                                                                                                   |
| regex_dna      | 251 ms                                                                                                            | 256 ms: 1.02x slower                                                                                                    |
| regex_v8       | 30.3 ms                                                                                                           | 32.6 ms: 1.08x slower                                                                                                   |
| regex_compile  | 128 ms                                                                                                            | 254 ms: 1.99x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.18x slower                                                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-NOGIL/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_parse      | 186 ms                                                                                                            | 182 ms: 1.02x faster                                                                                                    |
| xml_etree_iterparse  | 147 ms                                                                                                            | 156 ms: 1.07x slower                                                                                                    |
| json_loads           | 33.5 us                                                                                                           | 38.8 us: 1.16x slower                                                                                                   |
| json_dumps           | 13.4 ms                                                                                                           | 17.7 ms: 1.32x slower                                                                                                   |
| xml_etree_generate   | 112 ms                                                                                                            | 157 ms: 1.40x slower                                                                                                    |
| xml_etree_process    | 80.9 ms                                                                                                           | 130 ms: 1.60x slower                                                                                                    |
| tomli_loads          | 2.56 sec                                                                                                          | 4.20 sec: 1.64x slower                                                                                                  |
| pickle_pure_python   | 364 us                                                                                                            | 773 us: 2.13x slower                                                                                                    |
| unpickle_pure_python | 251 us                                                                                                            | 538 us: 2.14x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.44x slower                                                                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-NOGIL/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.87 ms                                                                                                           | 11.8 ms: 1.34x slower                                                                                                   |
| python_startup         | 13.0 ms                                                                                                           | 17.6 ms: 1.36x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.35x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-NOGIL/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 60.9 ms                                                                                                           | 104 ms: 1.70x slower                                                                                                    |
| genshi_text     | 27.6 ms                                                                                                           | 52.2 ms: 1.89x slower                                                                                                   |
| django_template | 41.8 ms                                                                                                           | 81.3 ms: 1.94x slower                                                                                                   |
| mako            | 13.5 ms                                                                                                           | 28.9 ms: 2.15x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.91x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-NOGIL/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| create_gc_cycles           | 2.33 ms                                                                                                           | 1.60 ms: 1.46x faster                                                                                                   |
| gc_traversal               | 4.99 ms                                                                                                           | 3.45 ms: 1.45x faster                                                                                                   |
| bench_mp_pool              | 7.09 ms                                                                                                           | 6.23 ms: 1.14x faster                                                                                                   |
| regex_effbot               | 4.91 ms                                                                                                           | 4.43 ms: 1.11x faster                                                                                                   |
| xml_etree_parse            | 186 ms                                                                                                            | 182 ms: 1.02x faster                                                                                                    |
| regex_dna                  | 251 ms                                                                                                            | 256 ms: 1.02x slower                                                                                                    |
| asyncio_websockets         | 657 ms                                                                                                            | 672 ms: 1.02x slower                                                                                                    |
| xml_etree_iterparse        | 147 ms                                                                                                            | 156 ms: 1.07x slower                                                                                                    |
| regex_v8                   | 30.3 ms                                                                                                           | 32.6 ms: 1.08x slower                                                                                                   |
| asyncio_tcp_ssl            | 2.20 sec                                                                                                          | 2.46 sec: 1.12x slower                                                                                                  |
| json_loads                 | 33.5 us                                                                                                           | 38.8 us: 1.16x slower                                                                                                   |
| asyncio_tcp                | 572 ms                                                                                                            | 671 ms: 1.17x slower                                                                                                    |
| async_tree_io_tg           | 1.14 sec                                                                                                          | 1.36 sec: 1.19x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 718 ms                                                                                                            | 859 ms: 1.20x slower                                                                                                    |
| json                       | 5.81 ms                                                                                                           | 6.97 ms: 1.20x slower                                                                                                   |
| pathlib                    | 21.6 ms                                                                                                           | 26.6 ms: 1.23x slower                                                                                                   |
| async_tree_cpu_io_mixed    | 732 ms                                                                                                            | 912 ms: 1.25x slower                                                                                                    |
| async_tree_io              | 1.12 sec                                                                                                          | 1.39 sec: 1.25x slower                                                                                                  |
| telco                      | 9.93 ms                                                                                                           | 12.5 ms: 1.26x slower                                                                                                   |
| async_tree_memoization_tg  | 536 ms                                                                                                            | 688 ms: 1.28x slower                                                                                                    |
| async_tree_memoization     | 574 ms                                                                                                            | 739 ms: 1.29x slower                                                                                                    |
| mdp                        | 3.35 sec                                                                                                          | 4.38 sec: 1.30x slower                                                                                                  |
| json_dumps                 | 13.4 ms                                                                                                           | 17.7 ms: 1.32x slower                                                                                                   |
| coverage                   | 99.4 ms                                                                                                           | 132 ms: 1.32x slower                                                                                                    |
| docutils                   | 3.09 sec                                                                                                          | 4.11 sec: 1.33x slower                                                                                                  |
| python_startup_no_site     | 8.87 ms                                                                                                           | 11.8 ms: 1.34x slower                                                                                                   |
| async_tree_none_tg         | 413 ms                                                                                                            | 560 ms: 1.35x slower                                                                                                    |
| async_tree_none            | 446 ms                                                                                                            | 604 ms: 1.36x slower                                                                                                    |
| python_startup             | 13.0 ms                                                                                                           | 17.6 ms: 1.36x slower                                                                                                   |
| scimark_fft                | 441 ms                                                                                                            | 599 ms: 1.36x slower                                                                                                    |
| coroutines                 | 28.2 ms                                                                                                           | 38.5 ms: 1.36x slower                                                                                                   |
| scimark_sparse_mat_mult    | 6.43 ms                                                                                                           | 8.92 ms: 1.39x slower                                                                                                   |
| async_generators           | 494 ms                                                                                                            | 686 ms: 1.39x slower                                                                                                    |
| xml_etree_generate         | 112 ms                                                                                                            | 157 ms: 1.40x slower                                                                                                    |
| pylint                     | 335 ms                                                                                                            | 502 ms: 1.50x slower                                                                                                    |
| nqueens                    | 99.7 ms                                                                                                           | 149 ms: 1.50x slower                                                                                                    |
| bench_thread_pool          | 1.24 ms                                                                                                           | 1.87 ms: 1.51x slower                                                                                                   |
| meteor_contest             | 111 ms                                                                                                            | 172 ms: 1.54x slower                                                                                                    |
| tornado_http               | 130 ms                                                                                                            | 207 ms: 1.60x slower                                                                                                    |
| xml_etree_process          | 80.9 ms                                                                                                           | 130 ms: 1.60x slower                                                                                                    |
| fannkuch                   | 458 ms                                                                                                            | 740 ms: 1.62x slower                                                                                                    |
| bpe_tokeniser              | 5.85 sec                                                                                                          | 9.57 sec: 1.64x slower                                                                                                  |
| tomli_loads                | 2.56 sec                                                                                                          | 4.20 sec: 1.64x slower                                                                                                  |
| generators                 | 34.9 ms                                                                                                           | 57.7 ms: 1.65x slower                                                                                                   |
| sympy_integrate            | 21.1 ms                                                                                                           | 35.1 ms: 1.66x slower                                                                                                   |
| dulwich_log                | 59.1 ms                                                                                                           | 98.3 ms: 1.66x slower                                                                                                   |
| deepcopy                   | 332 us                                                                                                            | 553 us: 1.66x slower                                                                                                    |
| pycparser                  | 1.23 sec                                                                                                          | 2.06 sec: 1.68x slower                                                                                                  |
| 2to3                       | 303 ms                                                                                                            | 513 ms: 1.69x slower                                                                                                    |
| genshi_xml                 | 60.9 ms                                                                                                           | 104 ms: 1.70x slower                                                                                                    |
| crypto_pyaes               | 82.0 ms                                                                                                           | 140 ms: 1.70x slower                                                                                                    |
| spectral_norm              | 140 ms                                                                                                            | 239 ms: 1.71x slower                                                                                                    |
| typing_runtime_protocols   | 194 us                                                                                                            | 332 us: 1.71x slower                                                                                                    |
| deepcopy_reduce            | 3.50 us                                                                                                           | 5.99 us: 1.71x slower                                                                                                   |
| thrift                     | 961 us                                                                                                            | 1.65 ms: 1.72x slower                                                                                                   |
| pyflate                    | 574 ms                                                                                                            | 1.01 sec: 1.76x slower                                                                                                  |
| html5lib                   | 68.0 ms                                                                                                           | 121 ms: 1.78x slower                                                                                                    |
| sqlglot_normalize          | 128 ms                                                                                                            | 231 ms: 1.80x slower                                                                                                    |
| pprint_safe_repr           | 940 ms                                                                                                            | 1.74 sec: 1.85x slower                                                                                                  |
| pprint_pformat             | 1.91 sec                                                                                                          | 3.59 sec: 1.88x slower                                                                                                  |
| deepcopy_memo              | 38.7 us                                                                                                           | 72.8 us: 1.88x slower                                                                                                   |
| sqlglot_optimize           | 61.9 ms                                                                                                           | 117 ms: 1.89x slower                                                                                                    |
| genshi_text                | 27.6 ms                                                                                                           | 52.2 ms: 1.89x slower                                                                                                   |
| django_template            | 41.8 ms                                                                                                           | 81.3 ms: 1.94x slower                                                                                                   |
| sympy_str                  | 267 ms                                                                                                            | 520 ms: 1.95x slower                                                                                                    |
| comprehensions             | 20.6 us                                                                                                           | 40.5 us: 1.96x slower                                                                                                   |
| regex_compile              | 128 ms                                                                                                            | 254 ms: 1.99x slower                                                                                                    |
| logging_format             | 7.84 us                                                                                                           | 15.7 us: 2.00x slower                                                                                                   |
| logging_simple             | 7.18 us                                                                                                           | 14.7 us: 2.05x slower                                                                                                   |
| sympy_expand               | 457 ms                                                                                                            | 953 ms: 2.09x slower                                                                                                    |
| scimark_monte_carlo        | 81.5 ms                                                                                                           | 172 ms: 2.11x slower                                                                                                    |
| pickle_pure_python         | 364 us                                                                                                            | 773 us: 2.13x slower                                                                                                    |
| unpickle_pure_python       | 251 us                                                                                                            | 538 us: 2.14x slower                                                                                                    |
| mako                       | 13.5 ms                                                                                                           | 28.9 ms: 2.15x slower                                                                                                   |
| scimark_sor                | 158 ms                                                                                                            | 341 ms: 2.16x slower                                                                                                    |
| logging_silent             | 129 ns                                                                                                            | 281 ns: 2.18x slower                                                                                                    |
| sympy_sum                  | 144 ms                                                                                                            | 317 ms: 2.20x slower                                                                                                    |
| hexiom                     | 6.99 ms                                                                                                           | 15.6 ms: 2.23x slower                                                                                                   |
| richards                   | 52.3 ms                                                                                                           | 117 ms: 2.24x slower                                                                                                    |
| float                      | 91.9 ms                                                                                                           | 209 ms: 2.28x slower                                                                                                    |
| richards_super             | 59.2 ms                                                                                                           | 137 ms: 2.32x slower                                                                                                    |
| chaos                      | 68.5 ms                                                                                                           | 161 ms: 2.34x slower                                                                                                    |
| sqlglot_transpile          | 1.73 ms                                                                                                           | 4.41 ms: 2.54x slower                                                                                                   |
| nbody                      | 114 ms                                                                                                            | 290 ms: 2.54x slower                                                                                                    |
| scimark_lu                 | 136 ms                                                                                                            | 348 ms: 2.56x slower                                                                                                    |
| sqlglot_parse              | 1.41 ms                                                                                                           | 3.83 ms: 2.71x slower                                                                                                   |
| raytrace                   | 300 ms                                                                                                            | 829 ms: 2.76x slower                                                                                                    |
| go                         | 160 ms                                                                                                            | 446 ms: 2.79x slower                                                                                                    |
| deltablue                  | 3.83 ms                                                                                                           | 12.7 ms: 3.32x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.60x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (1) of results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: dask

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.52x
- 95% likely to have a slowdown of 1.49x
- 99% likely to have a slowdown of 1.42x

# Memory
- memory change: 1.16x