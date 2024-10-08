# Results vs. base

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-aarch64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.62x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-NOGIL/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 302 ms                                                                                                            | 522 ms: 1.73x slower                                                                                                    |
| docutils       | 3.13 sec                                                                                                          | 4.12 sec: 1.32x slower                                                                                                  |
| html5lib       | 66.4 ms                                                                                                           | 123 ms: 1.85x slower                                                                                                    |
| tornado_http   | 121 ms                                                                                                            | 209 ms: 1.72x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.64x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-NOGIL/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets         | 660 ms                                                                                                            | 672 ms: 1.02x slower                                                                                                    |
| asyncio_tcp_ssl            | 2.20 sec                                                                                                          | 2.47 sec: 1.12x slower                                                                                                  |
| asyncio_tcp                | 576 ms                                                                                                            | 672 ms: 1.17x slower                                                                                                    |
| async_tree_io_tg           | 1.11 sec                                                                                                          | 1.35 sec: 1.22x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 706 ms                                                                                                            | 868 ms: 1.23x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                                                                            | 917 ms: 1.26x slower                                                                                                    |
| async_tree_io              | 1.08 sec                                                                                                          | 1.39 sec: 1.29x slower                                                                                                  |
| async_tree_memoization_tg  | 533 ms                                                                                                            | 695 ms: 1.30x slower                                                                                                    |
| async_tree_memoization     | 549 ms                                                                                                            | 743 ms: 1.35x slower                                                                                                    |
| async_generators           | 482 ms                                                                                                            | 670 ms: 1.39x slower                                                                                                    |
| async_tree_none            | 438 ms                                                                                                            | 612 ms: 1.40x slower                                                                                                    |
| async_tree_none_tg         | 400 ms                                                                                                            | 571 ms: 1.43x slower                                                                                                    |
| coroutines                 | 28.4 ms                                                                                                           | 41.1 ms: 1.45x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.27x slower                                                                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-NOGIL/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 93.1 ms                                                                                                           | 209 ms: 2.25x slower                                                                                                    |
| nbody          | 111 ms                                                                                                            | 285 ms: 2.58x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.80x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-NOGIL/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 4.92 ms                                                                                                           | 4.47 ms: 1.10x faster                                                                                                   |
| regex_v8       | 30.7 ms                                                                                                           | 33.0 ms: 1.08x slower                                                                                                   |
| regex_compile  | 126 ms                                                                                                            | 258 ms: 2.04x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.19x slower                                                                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-NOGIL/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_parse      | 189 ms                                                                                                            | 180 ms: 1.05x faster                                                                                                    |
| xml_etree_iterparse  | 148 ms                                                                                                            | 159 ms: 1.08x slower                                                                                                    |
| json_loads           | 32.8 us                                                                                                           | 38.9 us: 1.19x slower                                                                                                   |
| json_dumps           | 13.4 ms                                                                                                           | 18.2 ms: 1.36x slower                                                                                                   |
| xml_etree_generate   | 111 ms                                                                                                            | 163 ms: 1.46x slower                                                                                                    |
| xml_etree_process    | 80.2 ms                                                                                                           | 131 ms: 1.63x slower                                                                                                    |
| tomli_loads          | 2.55 sec                                                                                                          | 4.28 sec: 1.68x slower                                                                                                  |
| unpickle_pure_python | 252 us                                                                                                            | 546 us: 2.16x slower                                                                                                    |
| pickle_pure_python   | 356 us                                                                                                            | 787 us: 2.21x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.47x slower                                                                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-NOGIL/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.81 ms                                                                                                           | 12.2 ms: 1.38x slower                                                                                                   |
| python_startup         | 13.1 ms                                                                                                           | 18.1 ms: 1.39x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.39x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-NOGIL/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 60.1 ms                                                                                                           | 109 ms: 1.81x slower                                                                                                    |
| django_template | 42.9 ms                                                                                                           | 84.1 ms: 1.96x slower                                                                                                   |
| genshi_text     | 27.6 ms                                                                                                           | 55.1 ms: 1.99x slower                                                                                                   |
| mako            | 13.3 ms                                                                                                           | 28.9 ms: 2.17x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.98x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json | results/bm-20240817-3.14.0a0-79c542b-NOGIL/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| create_gc_cycles           | 2.29 ms                                                                                                           | 1.62 ms: 1.41x faster                                                                                                   |
| gc_traversal               | 4.79 ms                                                                                                           | 3.51 ms: 1.36x faster                                                                                                   |
| regex_effbot               | 4.92 ms                                                                                                           | 4.47 ms: 1.10x faster                                                                                                   |
| xml_etree_parse            | 189 ms                                                                                                            | 180 ms: 1.05x faster                                                                                                    |
| asyncio_websockets         | 660 ms                                                                                                            | 672 ms: 1.02x slower                                                                                                    |
| bench_mp_pool              | 7.00 ms                                                                                                           | 7.16 ms: 1.02x slower                                                                                                   |
| regex_v8                   | 30.7 ms                                                                                                           | 33.0 ms: 1.08x slower                                                                                                   |
| xml_etree_iterparse        | 148 ms                                                                                                            | 159 ms: 1.08x slower                                                                                                    |
| asyncio_tcp_ssl            | 2.20 sec                                                                                                          | 2.47 sec: 1.12x slower                                                                                                  |
| asyncio_tcp                | 576 ms                                                                                                            | 672 ms: 1.17x slower                                                                                                    |
| json_loads                 | 32.8 us                                                                                                           | 38.9 us: 1.19x slower                                                                                                   |
| async_tree_io_tg           | 1.11 sec                                                                                                          | 1.35 sec: 1.22x slower                                                                                                  |
| json                       | 5.72 ms                                                                                                           | 7.04 ms: 1.23x slower                                                                                                   |
| async_tree_cpu_io_mixed_tg | 706 ms                                                                                                            | 868 ms: 1.23x slower                                                                                                    |
| pathlib                    | 21.1 ms                                                                                                           | 26.6 ms: 1.26x slower                                                                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                                                                            | 917 ms: 1.26x slower                                                                                                    |
| telco                      | 10.3 ms                                                                                                           | 13.1 ms: 1.27x slower                                                                                                   |
| mdp                        | 3.38 sec                                                                                                          | 4.34 sec: 1.28x slower                                                                                                  |
| async_tree_io              | 1.08 sec                                                                                                          | 1.39 sec: 1.29x slower                                                                                                  |
| async_tree_memoization_tg  | 533 ms                                                                                                            | 695 ms: 1.30x slower                                                                                                    |
| scimark_fft                | 444 ms                                                                                                            | 582 ms: 1.31x slower                                                                                                    |
| docutils                   | 3.13 sec                                                                                                          | 4.12 sec: 1.32x slower                                                                                                  |
| async_tree_memoization     | 549 ms                                                                                                            | 743 ms: 1.35x slower                                                                                                    |
| json_dumps                 | 13.4 ms                                                                                                           | 18.2 ms: 1.36x slower                                                                                                   |
| python_startup_no_site     | 8.81 ms                                                                                                           | 12.2 ms: 1.38x slower                                                                                                   |
| python_startup             | 13.1 ms                                                                                                           | 18.1 ms: 1.39x slower                                                                                                   |
| async_generators           | 482 ms                                                                                                            | 670 ms: 1.39x slower                                                                                                    |
| async_tree_none            | 438 ms                                                                                                            | 612 ms: 1.40x slower                                                                                                    |
| scimark_sparse_mat_mult    | 6.37 ms                                                                                                           | 8.96 ms: 1.41x slower                                                                                                   |
| coverage                   | 97.6 ms                                                                                                           | 138 ms: 1.41x slower                                                                                                    |
| pylint                     | 359 ms                                                                                                            | 509 ms: 1.42x slower                                                                                                    |
| async_tree_none_tg         | 400 ms                                                                                                            | 571 ms: 1.43x slower                                                                                                    |
| coroutines                 | 28.4 ms                                                                                                           | 41.1 ms: 1.45x slower                                                                                                   |
| xml_etree_generate         | 111 ms                                                                                                            | 163 ms: 1.46x slower                                                                                                    |
| meteor_contest             | 113 ms                                                                                                            | 168 ms: 1.49x slower                                                                                                    |
| nqueens                    | 98.8 ms                                                                                                           | 152 ms: 1.54x slower                                                                                                    |
| bpe_tokeniser              | 5.85 sec                                                                                                          | 9.40 sec: 1.61x slower                                                                                                  |
| fannkuch                   | 460 ms                                                                                                            | 746 ms: 1.62x slower                                                                                                    |
| xml_etree_process          | 80.2 ms                                                                                                           | 131 ms: 1.63x slower                                                                                                    |
| spectral_norm              | 140 ms                                                                                                            | 231 ms: 1.65x slower                                                                                                    |
| generators                 | 34.4 ms                                                                                                           | 57.2 ms: 1.66x slower                                                                                                   |
| sympy_integrate            | 21.1 ms                                                                                                           | 35.2 ms: 1.67x slower                                                                                                   |
| tomli_loads                | 2.55 sec                                                                                                          | 4.28 sec: 1.68x slower                                                                                                  |
| pycparser                  | 1.22 sec                                                                                                          | 2.06 sec: 1.68x slower                                                                                                  |
| crypto_pyaes               | 82.0 ms                                                                                                           | 139 ms: 1.69x slower                                                                                                    |
| bench_thread_pool          | 1.25 ms                                                                                                           | 2.11 ms: 1.70x slower                                                                                                   |
| deepcopy                   | 330 us                                                                                                            | 564 us: 1.71x slower                                                                                                    |
| typing_runtime_protocols   | 201 us                                                                                                            | 344 us: 1.71x slower                                                                                                    |
| tornado_http               | 121 ms                                                                                                            | 209 ms: 1.72x slower                                                                                                    |
| 2to3                       | 302 ms                                                                                                            | 522 ms: 1.73x slower                                                                                                    |
| thrift                     | 957 us                                                                                                            | 1.67 ms: 1.74x slower                                                                                                   |
| pyflate                    | 577 ms                                                                                                            | 1.01 sec: 1.75x slower                                                                                                  |
| deepcopy_reduce            | 3.40 us                                                                                                           | 6.10 us: 1.80x slower                                                                                                   |
| genshi_xml                 | 60.1 ms                                                                                                           | 109 ms: 1.81x slower                                                                                                    |
| sqlglot_normalize          | 127 ms                                                                                                            | 232 ms: 1.82x slower                                                                                                    |
| html5lib                   | 66.4 ms                                                                                                           | 123 ms: 1.85x slower                                                                                                    |
| pprint_safe_repr           | 942 ms                                                                                                            | 1.78 sec: 1.89x slower                                                                                                  |
| sqlglot_optimize           | 61.8 ms                                                                                                           | 117 ms: 1.89x slower                                                                                                    |
| pprint_pformat             | 1.92 sec                                                                                                          | 3.66 sec: 1.90x slower                                                                                                  |
| deepcopy_memo              | 37.5 us                                                                                                           | 73.0 us: 1.95x slower                                                                                                   |
| sympy_str                  | 268 ms                                                                                                            | 523 ms: 1.95x slower                                                                                                    |
| django_template            | 42.9 ms                                                                                                           | 84.1 ms: 1.96x slower                                                                                                   |
| genshi_text                | 27.6 ms                                                                                                           | 55.1 ms: 1.99x slower                                                                                                   |
| comprehensions             | 20.5 us                                                                                                           | 41.2 us: 2.01x slower                                                                                                   |
| logging_format             | 7.69 us                                                                                                           | 15.6 us: 2.03x slower                                                                                                   |
| regex_compile              | 126 ms                                                                                                            | 258 ms: 2.04x slower                                                                                                    |
| logging_simple             | 6.93 us                                                                                                           | 14.5 us: 2.09x slower                                                                                                   |
| sympy_expand               | 464 ms                                                                                                            | 971 ms: 2.10x slower                                                                                                    |
| unpickle_pure_python       | 252 us                                                                                                            | 546 us: 2.16x slower                                                                                                    |
| mako                       | 13.3 ms                                                                                                           | 28.9 ms: 2.17x slower                                                                                                   |
| sympy_sum                  | 145 ms                                                                                                            | 318 ms: 2.20x slower                                                                                                    |
| scimark_monte_carlo        | 81.8 ms                                                                                                           | 180 ms: 2.20x slower                                                                                                    |
| pickle_pure_python         | 356 us                                                                                                            | 787 us: 2.21x slower                                                                                                    |
| scimark_sor                | 154 ms                                                                                                            | 342 ms: 2.22x slower                                                                                                    |
| float                      | 93.1 ms                                                                                                           | 209 ms: 2.25x slower                                                                                                    |
| logging_silent             | 130 ns                                                                                                            | 291 ns: 2.25x slower                                                                                                    |
| hexiom                     | 6.98 ms                                                                                                           | 15.7 ms: 2.25x slower                                                                                                   |
| richards                   | 51.9 ms                                                                                                           | 117 ms: 2.26x slower                                                                                                    |
| chaos                      | 67.7 ms                                                                                                           | 160 ms: 2.36x slower                                                                                                    |
| richards_super             | 58.4 ms                                                                                                           | 141 ms: 2.41x slower                                                                                                    |
| sqlglot_transpile          | 1.73 ms                                                                                                           | 4.37 ms: 2.53x slower                                                                                                   |
| nbody                      | 111 ms                                                                                                            | 285 ms: 2.58x slower                                                                                                    |
| sqlglot_parse              | 1.43 ms                                                                                                           | 3.72 ms: 2.59x slower                                                                                                   |
| scimark_lu                 | 134 ms                                                                                                            | 351 ms: 2.62x slower                                                                                                    |
| raytrace                   | 294 ms                                                                                                            | 820 ms: 2.79x slower                                                                                                    |
| go                         | 159 ms                                                                                                            | 447 ms: 2.80x slower                                                                                                    |
| deltablue                  | 3.77 ms                                                                                                           | 12.7 ms: 3.37x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.62x slower                                                                                                            |

Benchmark hidden because not significant (2): pidigits, regex_dna

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.49x
- 95% likely to have a slowdown of 1.47x
- 99% likely to have a slowdown of 1.41x

# Memory
- memory change: 1.15x