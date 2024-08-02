# Results vs. base

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-aarch64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.59x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-NOGIL/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                                                            | 517 ms: 1.69x slower                                                                                                    |
| docutils       | 3.12 sec                                                                                                          | 4.10 sec: 1.31x slower                                                                                                  |
| html5lib       | 68.2 ms                                                                                                           | 121 ms: 1.77x slower                                                                                                    |
| tornado_http   | 136 ms                                                                                                            | 202 ms: 1.49x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.56x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-NOGIL/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.10 sec                                                                                                          | 1.35 sec: 1.22x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 707 ms                                                                                                            | 869 ms: 1.23x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 725 ms                                                                                                            | 910 ms: 1.26x slower                                                                                                    |
| async_tree_io              | 1.07 sec                                                                                                          | 1.40 sec: 1.31x slower                                                                                                  |
| async_tree_memoization_tg  | 536 ms                                                                                                            | 702 ms: 1.31x slower                                                                                                    |
| async_tree_memoization     | 562 ms                                                                                                            | 748 ms: 1.33x slower                                                                                                    |
| async_tree_none_tg         | 407 ms                                                                                                            | 566 ms: 1.39x slower                                                                                                    |
| async_tree_none            | 437 ms                                                                                                            | 611 ms: 1.40x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.30x slower                                                                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-NOGIL/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 93.0 ms                                                                                                           | 210 ms: 2.25x slower                                                                                                    |
| nbody          | 116 ms                                                                                                            | 289 ms: 2.49x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.78x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-NOGIL/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                                                                           | 4.30 ms: 1.14x faster                                                                                                   |
| regex_dna      | 251 ms                                                                                                            | 245 ms: 1.02x faster                                                                                                    |
| regex_v8       | 30.8 ms                                                                                                           | 32.5 ms: 1.06x slower                                                                                                   |
| regex_compile  | 128 ms                                                                                                            | 256 ms: 2.00x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.16x slower                                                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-NOGIL/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_parse      | 189 ms                                                                                                            | 182 ms: 1.04x faster                                                                                                    |
| xml_etree_iterparse  | 149 ms                                                                                                            | 156 ms: 1.05x slower                                                                                                    |
| json_loads           | 33.3 us                                                                                                           | 38.7 us: 1.16x slower                                                                                                   |
| json_dumps           | 13.4 ms                                                                                                           | 17.6 ms: 1.31x slower                                                                                                   |
| xml_etree_generate   | 114 ms                                                                                                            | 160 ms: 1.40x slower                                                                                                    |
| xml_etree_process    | 79.6 ms                                                                                                           | 129 ms: 1.62x slower                                                                                                    |
| tomli_loads          | 2.53 sec                                                                                                          | 4.20 sec: 1.66x slower                                                                                                  |
| unpickle_pure_python | 254 us                                                                                                            | 542 us: 2.13x slower                                                                                                    |
| pickle_pure_python   | 360 us                                                                                                            | 774 us: 2.15x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.44x slower                                                                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-NOGIL/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 9.03 ms                                                                                                           | 11.7 ms: 1.30x slower                                                                                                   |
| python_startup         | 13.5 ms                                                                                                           | 17.6 ms: 1.31x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.30x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-NOGIL/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 61.5 ms                                                                                                           | 104 ms: 1.68x slower                                                                                                    |
| genshi_text     | 28.0 ms                                                                                                           | 53.2 ms: 1.90x slower                                                                                                   |
| django_template | 42.3 ms                                                                                                           | 83.2 ms: 1.97x slower                                                                                                   |
| mako            | 13.6 ms                                                                                                           | 28.8 ms: 2.11x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.91x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-NOGIL/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| gc_traversal               | 4.98 ms                                                                                                           | 3.42 ms: 1.45x faster                                                                                                   |
| create_gc_cycles           | 2.28 ms                                                                                                           | 1.58 ms: 1.44x faster                                                                                                   |
| regex_effbot               | 4.89 ms                                                                                                           | 4.30 ms: 1.14x faster                                                                                                   |
| bench_mp_pool              | 7.08 ms                                                                                                           | 6.25 ms: 1.13x faster                                                                                                   |
| xml_etree_parse            | 189 ms                                                                                                            | 182 ms: 1.04x faster                                                                                                    |
| regex_dna                  | 251 ms                                                                                                            | 245 ms: 1.02x faster                                                                                                    |
| asyncio_websockets         | 662 ms                                                                                                            | 671 ms: 1.01x slower                                                                                                    |
| xml_etree_iterparse        | 149 ms                                                                                                            | 156 ms: 1.05x slower                                                                                                    |
| regex_v8                   | 30.8 ms                                                                                                           | 32.5 ms: 1.06x slower                                                                                                   |
| asyncio_tcp_ssl            | 2.25 sec                                                                                                          | 2.47 sec: 1.10x slower                                                                                                  |
| asyncio_tcp                | 592 ms                                                                                                            | 684 ms: 1.15x slower                                                                                                    |
| json_loads                 | 33.3 us                                                                                                           | 38.7 us: 1.16x slower                                                                                                   |
| telco                      | 10.0 ms                                                                                                           | 11.8 ms: 1.18x slower                                                                                                   |
| async_tree_io_tg           | 1.10 sec                                                                                                          | 1.35 sec: 1.22x slower                                                                                                  |
| pathlib                    | 21.5 ms                                                                                                           | 26.3 ms: 1.22x slower                                                                                                   |
| json                       | 5.71 ms                                                                                                           | 7.01 ms: 1.23x slower                                                                                                   |
| async_tree_cpu_io_mixed_tg | 707 ms                                                                                                            | 869 ms: 1.23x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 725 ms                                                                                                            | 910 ms: 1.26x slower                                                                                                    |
| python_startup_no_site     | 9.03 ms                                                                                                           | 11.7 ms: 1.30x slower                                                                                                   |
| mdp                        | 3.36 sec                                                                                                          | 4.37 sec: 1.30x slower                                                                                                  |
| async_tree_io              | 1.07 sec                                                                                                          | 1.40 sec: 1.31x slower                                                                                                  |
| async_tree_memoization_tg  | 536 ms                                                                                                            | 702 ms: 1.31x slower                                                                                                    |
| python_startup             | 13.5 ms                                                                                                           | 17.6 ms: 1.31x slower                                                                                                   |
| json_dumps                 | 13.4 ms                                                                                                           | 17.6 ms: 1.31x slower                                                                                                   |
| docutils                   | 3.12 sec                                                                                                          | 4.10 sec: 1.31x slower                                                                                                  |
| async_tree_memoization     | 562 ms                                                                                                            | 748 ms: 1.33x slower                                                                                                    |
| coverage                   | 100 ms                                                                                                            | 134 ms: 1.33x slower                                                                                                    |
| scimark_fft                | 446 ms                                                                                                            | 601 ms: 1.35x slower                                                                                                    |
| coroutines                 | 29.0 ms                                                                                                           | 39.2 ms: 1.35x slower                                                                                                   |
| async_generators           | 494 ms                                                                                                            | 678 ms: 1.37x slower                                                                                                    |
| scimark_sparse_mat_mult    | 6.53 ms                                                                                                           | 9.05 ms: 1.39x slower                                                                                                   |
| async_tree_none_tg         | 407 ms                                                                                                            | 566 ms: 1.39x slower                                                                                                    |
| async_tree_none            | 437 ms                                                                                                            | 611 ms: 1.40x slower                                                                                                    |
| xml_etree_generate         | 114 ms                                                                                                            | 160 ms: 1.40x slower                                                                                                    |
| pylint                     | 342 ms                                                                                                            | 504 ms: 1.47x slower                                                                                                    |
| tornado_http               | 136 ms                                                                                                            | 202 ms: 1.49x slower                                                                                                    |
| bench_thread_pool          | 1.27 ms                                                                                                           | 1.91 ms: 1.50x slower                                                                                                   |
| nqueens                    | 100 ms                                                                                                            | 151 ms: 1.50x slower                                                                                                    |
| dulwich_log                | 64.6 ms                                                                                                           | 97.3 ms: 1.51x slower                                                                                                   |
| generators                 | 38.0 ms                                                                                                           | 58.4 ms: 1.54x slower                                                                                                   |
| meteor_contest             | 112 ms                                                                                                            | 174 ms: 1.55x slower                                                                                                    |
| sympy_integrate            | 21.7 ms                                                                                                           | 35.0 ms: 1.62x slower                                                                                                   |
| xml_etree_process          | 79.6 ms                                                                                                           | 129 ms: 1.62x slower                                                                                                    |
| fannkuch                   | 460 ms                                                                                                            | 750 ms: 1.63x slower                                                                                                    |
| bpe_tokeniser              | 5.79 sec                                                                                                          | 9.48 sec: 1.64x slower                                                                                                  |
| tomli_loads                | 2.53 sec                                                                                                          | 4.20 sec: 1.66x slower                                                                                                  |
| spectral_norm              | 141 ms                                                                                                            | 237 ms: 1.68x slower                                                                                                    |
| deepcopy                   | 333 us                                                                                                            | 559 us: 1.68x slower                                                                                                    |
| pycparser                  | 1.23 sec                                                                                                          | 2.06 sec: 1.68x slower                                                                                                  |
| genshi_xml                 | 61.5 ms                                                                                                           | 104 ms: 1.68x slower                                                                                                    |
| 2to3                       | 306 ms                                                                                                            | 517 ms: 1.69x slower                                                                                                    |
| crypto_pyaes               | 81.9 ms                                                                                                           | 140 ms: 1.70x slower                                                                                                    |
| typing_runtime_protocols   | 194 us                                                                                                            | 331 us: 1.70x slower                                                                                                    |
| thrift                     | 969 us                                                                                                            | 1.67 ms: 1.72x slower                                                                                                   |
| pyflate                    | 578 ms                                                                                                            | 1.02 sec: 1.76x slower                                                                                                  |
| deepcopy_reduce            | 3.39 us                                                                                                           | 6.02 us: 1.77x slower                                                                                                   |
| html5lib                   | 68.2 ms                                                                                                           | 121 ms: 1.77x slower                                                                                                    |
| sqlglot_normalize          | 129 ms                                                                                                            | 230 ms: 1.78x slower                                                                                                    |
| deepcopy_memo              | 39.3 us                                                                                                           | 72.0 us: 1.83x slower                                                                                                   |
| sqlglot_optimize           | 62.9 ms                                                                                                           | 116 ms: 1.84x slower                                                                                                    |
| pprint_safe_repr           | 952 ms                                                                                                            | 1.77 sec: 1.86x slower                                                                                                  |
| pprint_pformat             | 1.95 sec                                                                                                          | 3.64 sec: 1.87x slower                                                                                                  |
| genshi_text                | 28.0 ms                                                                                                           | 53.2 ms: 1.90x slower                                                                                                   |
| sympy_str                  | 271 ms                                                                                                            | 519 ms: 1.91x slower                                                                                                    |
| django_template            | 42.3 ms                                                                                                           | 83.2 ms: 1.97x slower                                                                                                   |
| comprehensions             | 20.5 us                                                                                                           | 40.7 us: 1.98x slower                                                                                                   |
| regex_compile              | 128 ms                                                                                                            | 256 ms: 2.00x slower                                                                                                    |
| logging_format             | 7.64 us                                                                                                           | 15.6 us: 2.05x slower                                                                                                   |
| sympy_expand               | 465 ms                                                                                                            | 956 ms: 2.06x slower                                                                                                    |
| logging_simple             | 6.92 us                                                                                                           | 14.6 us: 2.11x slower                                                                                                   |
| mako                       | 13.6 ms                                                                                                           | 28.8 ms: 2.11x slower                                                                                                   |
| scimark_monte_carlo        | 82.8 ms                                                                                                           | 175 ms: 2.12x slower                                                                                                    |
| sympy_sum                  | 150 ms                                                                                                            | 318 ms: 2.12x slower                                                                                                    |
| unpickle_pure_python       | 254 us                                                                                                            | 542 us: 2.13x slower                                                                                                    |
| pickle_pure_python         | 360 us                                                                                                            | 774 us: 2.15x slower                                                                                                    |
| scimark_sor                | 158 ms                                                                                                            | 343 ms: 2.17x slower                                                                                                    |
| logging_silent             | 132 ns                                                                                                            | 287 ns: 2.17x slower                                                                                                    |
| hexiom                     | 7.13 ms                                                                                                           | 15.6 ms: 2.19x slower                                                                                                   |
| float                      | 93.0 ms                                                                                                           | 210 ms: 2.25x slower                                                                                                    |
| chaos                      | 68.7 ms                                                                                                           | 161 ms: 2.35x slower                                                                                                    |
| richards                   | 53.0 ms                                                                                                           | 127 ms: 2.40x slower                                                                                                    |
| richards_super             | 59.9 ms                                                                                                           | 145 ms: 2.43x slower                                                                                                    |
| nbody                      | 116 ms                                                                                                            | 289 ms: 2.49x slower                                                                                                    |
| sqlglot_transpile          | 1.73 ms                                                                                                           | 4.38 ms: 2.53x slower                                                                                                   |
| scimark_lu                 | 138 ms                                                                                                            | 355 ms: 2.58x slower                                                                                                    |
| sqlglot_parse              | 1.41 ms                                                                                                           | 3.78 ms: 2.68x slower                                                                                                   |
| raytrace                   | 299 ms                                                                                                            | 825 ms: 2.76x slower                                                                                                    |
| go                         | 161 ms                                                                                                            | 448 ms: 2.79x slower                                                                                                    |
| deltablue                  | 3.84 ms                                                                                                           | 12.9 ms: 3.36x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.59x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (1) of results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: dask

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.47x
- 95% likely to have a slowdown of 1.45x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: 1.15x