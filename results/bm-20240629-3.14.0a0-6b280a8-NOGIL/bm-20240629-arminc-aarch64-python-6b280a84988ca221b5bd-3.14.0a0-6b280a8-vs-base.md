# Results vs. base

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: linux-aarch64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.60x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-NOGIL/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                                                            | 523 ms: 1.71x slower                                                                                                    |
| docutils       | 3.07 sec                                                                                                          | 4.12 sec: 1.34x slower                                                                                                  |
| html5lib       | 66.1 ms                                                                                                           | 120 ms: 1.82x slower                                                                                                    |
| tornado_http   | 127 ms                                                                                                            | 202 ms: 1.59x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.60x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-NOGIL/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 713 ms                                                                                                            | 871 ms: 1.22x slower                                                                                                    |
| async_tree_io_tg           | 1.11 sec                                                                                                          | 1.36 sec: 1.23x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 731 ms                                                                                                            | 925 ms: 1.26x slower                                                                                                    |
| async_tree_memoization_tg  | 533 ms                                                                                                            | 698 ms: 1.31x slower                                                                                                    |
| async_tree_io              | 1.07 sec                                                                                                          | 1.42 sec: 1.33x slower                                                                                                  |
| async_tree_memoization     | 569 ms                                                                                                            | 762 ms: 1.34x slower                                                                                                    |
| async_tree_none_tg         | 409 ms                                                                                                            | 579 ms: 1.42x slower                                                                                                    |
| async_tree_none            | 441 ms                                                                                                            | 625 ms: 1.42x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.31x slower                                                                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-NOGIL/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 92.7 ms                                                                                                           | 211 ms: 2.27x slower                                                                                                    |
| nbody          | 112 ms                                                                                                            | 293 ms: 2.62x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.82x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-NOGIL/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 4.88 ms                                                                                                           | 4.27 ms: 1.14x faster                                                                                                   |
| regex_dna      | 248 ms                                                                                                            | 241 ms: 1.03x faster                                                                                                    |
| regex_v8       | 31.0 ms                                                                                                           | 32.2 ms: 1.04x slower                                                                                                   |
| regex_compile  | 128 ms                                                                                                            | 258 ms: 2.01x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.15x slower                                                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-NOGIL/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_parse      | 190 ms                                                                                                            | 182 ms: 1.04x faster                                                                                                    |
| xml_etree_iterparse  | 149 ms                                                                                                            | 155 ms: 1.04x slower                                                                                                    |
| json_loads           | 33.0 us                                                                                                           | 38.4 us: 1.16x slower                                                                                                   |
| json_dumps           | 13.5 ms                                                                                                           | 18.1 ms: 1.34x slower                                                                                                   |
| xml_etree_generate   | 118 ms                                                                                                            | 164 ms: 1.39x slower                                                                                                    |
| xml_etree_process    | 81.1 ms                                                                                                           | 131 ms: 1.62x slower                                                                                                    |
| tomli_loads          | 2.54 sec                                                                                                          | 4.29 sec: 1.69x slower                                                                                                  |
| pickle_pure_python   | 359 us                                                                                                            | 778 us: 2.17x slower                                                                                                    |
| unpickle_pure_python | 252 us                                                                                                            | 546 us: 2.17x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.45x slower                                                                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-NOGIL/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.82 ms                                                                                                           | 11.9 ms: 1.35x slower                                                                                                   |
| python_startup         | 13.0 ms                                                                                                           | 17.7 ms: 1.36x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.35x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-NOGIL/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 61.1 ms                                                                                                           | 105 ms: 1.71x slower                                                                                                    |
| genshi_text     | 28.0 ms                                                                                                           | 52.5 ms: 1.88x slower                                                                                                   |
| django_template | 42.9 ms                                                                                                           | 82.4 ms: 1.92x slower                                                                                                   |
| mako            | 13.6 ms                                                                                                           | 28.7 ms: 2.12x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.90x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-NOGIL/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| create_gc_cycles           | 2.36 ms                                                                                                           | 1.59 ms: 1.49x faster                                                                                                   |
| gc_traversal               | 4.86 ms                                                                                                           | 3.43 ms: 1.42x faster                                                                                                   |
| regex_effbot               | 4.88 ms                                                                                                           | 4.27 ms: 1.14x faster                                                                                                   |
| bench_mp_pool              | 6.97 ms                                                                                                           | 6.25 ms: 1.11x faster                                                                                                   |
| xml_etree_parse            | 190 ms                                                                                                            | 182 ms: 1.04x faster                                                                                                    |
| regex_dna                  | 248 ms                                                                                                            | 241 ms: 1.03x faster                                                                                                    |
| asyncio_websockets         | 661 ms                                                                                                            | 668 ms: 1.01x slower                                                                                                    |
| regex_v8                   | 31.0 ms                                                                                                           | 32.2 ms: 1.04x slower                                                                                                   |
| xml_etree_iterparse        | 149 ms                                                                                                            | 155 ms: 1.04x slower                                                                                                    |
| asyncio_tcp_ssl            | 2.24 sec                                                                                                          | 2.48 sec: 1.11x slower                                                                                                  |
| json_loads                 | 33.0 us                                                                                                           | 38.4 us: 1.16x slower                                                                                                   |
| asyncio_tcp                | 581 ms                                                                                                            | 681 ms: 1.17x slower                                                                                                    |
| json                       | 5.81 ms                                                                                                           | 6.89 ms: 1.18x slower                                                                                                   |
| async_tree_cpu_io_mixed_tg | 713 ms                                                                                                            | 871 ms: 1.22x slower                                                                                                    |
| async_tree_io_tg           | 1.11 sec                                                                                                          | 1.36 sec: 1.23x slower                                                                                                  |
| pathlib                    | 21.9 ms                                                                                                           | 26.9 ms: 1.23x slower                                                                                                   |
| telco                      | 10.1 ms                                                                                                           | 12.6 ms: 1.25x slower                                                                                                   |
| async_tree_cpu_io_mixed    | 731 ms                                                                                                            | 925 ms: 1.26x slower                                                                                                    |
| async_tree_memoization_tg  | 533 ms                                                                                                            | 698 ms: 1.31x slower                                                                                                    |
| scimark_fft                | 448 ms                                                                                                            | 589 ms: 1.31x slower                                                                                                    |
| mdp                        | 3.35 sec                                                                                                          | 4.42 sec: 1.32x slower                                                                                                  |
| async_tree_io              | 1.07 sec                                                                                                          | 1.42 sec: 1.33x slower                                                                                                  |
| async_tree_memoization     | 569 ms                                                                                                            | 762 ms: 1.34x slower                                                                                                    |
| docutils                   | 3.07 sec                                                                                                          | 4.12 sec: 1.34x slower                                                                                                  |
| json_dumps                 | 13.5 ms                                                                                                           | 18.1 ms: 1.34x slower                                                                                                   |
| python_startup_no_site     | 8.82 ms                                                                                                           | 11.9 ms: 1.35x slower                                                                                                   |
| coroutines                 | 29.6 ms                                                                                                           | 39.9 ms: 1.35x slower                                                                                                   |
| python_startup             | 13.0 ms                                                                                                           | 17.7 ms: 1.36x slower                                                                                                   |
| async_generators           | 488 ms                                                                                                            | 667 ms: 1.37x slower                                                                                                    |
| xml_etree_generate         | 118 ms                                                                                                            | 164 ms: 1.39x slower                                                                                                    |
| scimark_sparse_mat_mult    | 6.57 ms                                                                                                           | 9.16 ms: 1.40x slower                                                                                                   |
| coverage                   | 100 ms                                                                                                            | 142 ms: 1.42x slower                                                                                                    |
| async_tree_none_tg         | 409 ms                                                                                                            | 579 ms: 1.42x slower                                                                                                    |
| async_tree_none            | 441 ms                                                                                                            | 625 ms: 1.42x slower                                                                                                    |
| pylint                     | 342 ms                                                                                                            | 507 ms: 1.48x slower                                                                                                    |
| generators                 | 38.1 ms                                                                                                           | 57.2 ms: 1.50x slower                                                                                                   |
| bench_thread_pool          | 1.25 ms                                                                                                           | 1.87 ms: 1.50x slower                                                                                                   |
| meteor_contest             | 113 ms                                                                                                            | 176 ms: 1.56x slower                                                                                                    |
| nqueens                    | 98.9 ms                                                                                                           | 156 ms: 1.58x slower                                                                                                    |
| tornado_http               | 127 ms                                                                                                            | 202 ms: 1.59x slower                                                                                                    |
| xml_etree_process          | 81.1 ms                                                                                                           | 131 ms: 1.62x slower                                                                                                    |
| dulwich_log                | 59.1 ms                                                                                                           | 95.9 ms: 1.62x slower                                                                                                   |
| typing_runtime_protocols   | 207 us                                                                                                            | 338 us: 1.63x slower                                                                                                    |
| bpe_tokeniser              | 5.83 sec                                                                                                          | 9.55 sec: 1.64x slower                                                                                                  |
| spectral_norm              | 142 ms                                                                                                            | 235 ms: 1.66x slower                                                                                                    |
| pycparser                  | 1.23 sec                                                                                                          | 2.06 sec: 1.68x slower                                                                                                  |
| sympy_integrate            | 21.0 ms                                                                                                           | 35.3 ms: 1.68x slower                                                                                                   |
| fannkuch                   | 456 ms                                                                                                            | 769 ms: 1.69x slower                                                                                                    |
| tomli_loads                | 2.54 sec                                                                                                          | 4.29 sec: 1.69x slower                                                                                                  |
| deepcopy                   | 331 us                                                                                                            | 562 us: 1.70x slower                                                                                                    |
| 2to3                       | 306 ms                                                                                                            | 523 ms: 1.71x slower                                                                                                    |
| genshi_xml                 | 61.1 ms                                                                                                           | 105 ms: 1.71x slower                                                                                                    |
| pyflate                    | 583 ms                                                                                                            | 1.01 sec: 1.73x slower                                                                                                  |
| crypto_pyaes               | 81.7 ms                                                                                                           | 142 ms: 1.74x slower                                                                                                    |
| deepcopy_reduce            | 3.47 us                                                                                                           | 6.11 us: 1.76x slower                                                                                                   |
| thrift                     | 964 us                                                                                                            | 1.72 ms: 1.78x slower                                                                                                   |
| sqlglot_normalize          | 129 ms                                                                                                            | 232 ms: 1.80x slower                                                                                                    |
| html5lib                   | 66.1 ms                                                                                                           | 120 ms: 1.82x slower                                                                                                    |
| sqlglot_optimize           | 62.8 ms                                                                                                           | 116 ms: 1.85x slower                                                                                                    |
| genshi_text                | 28.0 ms                                                                                                           | 52.5 ms: 1.88x slower                                                                                                   |
| pprint_safe_repr           | 946 ms                                                                                                            | 1.81 sec: 1.91x slower                                                                                                  |
| deepcopy_memo              | 37.8 us                                                                                                           | 72.6 us: 1.92x slower                                                                                                   |
| django_template            | 42.9 ms                                                                                                           | 82.4 ms: 1.92x slower                                                                                                   |
| pprint_pformat             | 1.93 sec                                                                                                          | 3.73 sec: 1.93x slower                                                                                                  |
| sympy_str                  | 268 ms                                                                                                            | 519 ms: 1.94x slower                                                                                                    |
| comprehensions             | 20.5 us                                                                                                           | 40.8 us: 1.98x slower                                                                                                   |
| regex_compile              | 128 ms                                                                                                            | 258 ms: 2.01x slower                                                                                                    |
| sympy_expand               | 462 ms                                                                                                            | 956 ms: 2.07x slower                                                                                                    |
| logging_silent             | 133 ns                                                                                                            | 276 ns: 2.07x slower                                                                                                    |
| logging_format             | 7.69 us                                                                                                           | 16.0 us: 2.08x slower                                                                                                   |
| scimark_monte_carlo        | 82.3 ms                                                                                                           | 172 ms: 2.09x slower                                                                                                    |
| logging_simple             | 6.93 us                                                                                                           | 14.6 us: 2.11x slower                                                                                                   |
| mako                       | 13.6 ms                                                                                                           | 28.7 ms: 2.12x slower                                                                                                   |
| scimark_sor                | 159 ms                                                                                                            | 340 ms: 2.14x slower                                                                                                    |
| sympy_sum                  | 145 ms                                                                                                            | 314 ms: 2.16x slower                                                                                                    |
| pickle_pure_python         | 359 us                                                                                                            | 778 us: 2.17x slower                                                                                                    |
| unpickle_pure_python       | 252 us                                                                                                            | 546 us: 2.17x slower                                                                                                    |
| hexiom                     | 7.14 ms                                                                                                           | 15.9 ms: 2.23x slower                                                                                                   |
| richards                   | 52.8 ms                                                                                                           | 119 ms: 2.26x slower                                                                                                    |
| float                      | 92.7 ms                                                                                                           | 211 ms: 2.27x slower                                                                                                    |
| chaos                      | 68.8 ms                                                                                                           | 163 ms: 2.36x slower                                                                                                    |
| richards_super             | 59.2 ms                                                                                                           | 142 ms: 2.39x slower                                                                                                    |
| sqlglot_transpile          | 1.73 ms                                                                                                           | 4.28 ms: 2.48x slower                                                                                                   |
| scimark_lu                 | 137 ms                                                                                                            | 345 ms: 2.52x slower                                                                                                    |
| sqlglot_parse              | 1.41 ms                                                                                                           | 3.69 ms: 2.61x slower                                                                                                   |
| nbody                      | 112 ms                                                                                                            | 293 ms: 2.62x slower                                                                                                    |
| raytrace                   | 299 ms                                                                                                            | 824 ms: 2.76x slower                                                                                                    |
| go                         | 161 ms                                                                                                            | 449 ms: 2.79x slower                                                                                                    |
| deltablue                  | 3.86 ms                                                                                                           | 12.3 ms: 3.20x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.60x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (1) of results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json: dask

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.50x
- 95% likely to have a slowdown of 1.47x
- 99% likely to have a slowdown of 1.41x

# Memory
- memory change: 1.15x