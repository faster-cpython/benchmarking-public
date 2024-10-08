# Results vs. base

- fork: python
- ref: 52caaef6d01a94962576
- machine: linux-aarch64
- commit hash: 52caaef
- commit date: 2024-08-24
- overall geometric mean: 1.61x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json | results/bm-20240824-3.14.0a0-52caaef-NOGIL/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 297 ms                                                                                                            | 521 ms: 1.75x slower                                                                                                    |
| docutils       | 3.09 sec                                                                                                          | 4.04 sec: 1.31x slower                                                                                                  |
| html5lib       | 67.8 ms                                                                                                           | 122 ms: 1.80x slower                                                                                                    |
| tornado_http   | 125 ms                                                                                                            | 204 ms: 1.63x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.61x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json | results/bm-20240824-3.14.0a0-52caaef-NOGIL/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets         | 660 ms                                                                                                            | 672 ms: 1.02x slower                                                                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                                                                          | 2.46 sec: 1.11x slower                                                                                                  |
| asyncio_tcp                | 564 ms                                                                                                            | 642 ms: 1.14x slower                                                                                                    |
| async_tree_io_tg           | 1.17 sec                                                                                                          | 1.37 sec: 1.17x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 732 ms                                                                                                            | 877 ms: 1.20x slower                                                                                                    |
| async_tree_io              | 1.14 sec                                                                                                          | 1.41 sec: 1.23x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 727 ms                                                                                                            | 908 ms: 1.25x slower                                                                                                    |
| async_tree_memoization_tg  | 550 ms                                                                                                            | 695 ms: 1.26x slower                                                                                                    |
| async_tree_memoization     | 557 ms                                                                                                            | 738 ms: 1.33x slower                                                                                                    |
| async_tree_none_tg         | 419 ms                                                                                                            | 570 ms: 1.36x slower                                                                                                    |
| async_generators           | 485 ms                                                                                                            | 665 ms: 1.37x slower                                                                                                    |
| async_tree_none            | 423 ms                                                                                                            | 606 ms: 1.43x slower                                                                                                    |
| coroutines                 | 28.4 ms                                                                                                           | 41.3 ms: 1.45x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.25x slower                                                                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json | results/bm-20240824-3.14.0a0-52caaef-NOGIL/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 91.2 ms                                                                                                           | 209 ms: 2.29x slower                                                                                                    |
| nbody          | 108 ms                                                                                                            | 282 ms: 2.61x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.81x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json | results/bm-20240824-3.14.0a0-52caaef-NOGIL/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 4.88 ms                                                                                                           | 4.48 ms: 1.09x faster                                                                                                   |
| regex_dna      | 252 ms                                                                                                            | 258 ms: 1.02x slower                                                                                                    |
| regex_v8       | 30.5 ms                                                                                                           | 32.8 ms: 1.08x slower                                                                                                   |
| regex_compile  | 123 ms                                                                                                            | 260 ms: 2.11x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.21x slower                                                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json | results/bm-20240824-3.14.0a0-52caaef-NOGIL/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 151 ms                                                                                                            | 160 ms: 1.06x slower                                                                                                    |
| json_loads           | 32.6 us                                                                                                           | 39.5 us: 1.21x slower                                                                                                   |
| json_dumps           | 13.1 ms                                                                                                           | 18.3 ms: 1.40x slower                                                                                                   |
| xml_etree_generate   | 113 ms                                                                                                            | 162 ms: 1.44x slower                                                                                                    |
| tomli_loads          | 2.62 sec                                                                                                          | 4.20 sec: 1.61x slower                                                                                                  |
| xml_etree_process    | 78.3 ms                                                                                                           | 131 ms: 1.68x slower                                                                                                    |
| unpickle_pure_python | 252 us                                                                                                            | 548 us: 2.17x slower                                                                                                    |
| pickle_pure_python   | 356 us                                                                                                            | 776 us: 2.18x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.47x slower                                                                                                            |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json | results/bm-20240824-3.14.0a0-52caaef-NOGIL/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.77 ms                                                                                                           | 12.1 ms: 1.38x slower                                                                                                   |
| python_startup         | 13.0 ms                                                                                                           | 18.0 ms: 1.38x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.38x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json | results/bm-20240824-3.14.0a0-52caaef-NOGIL/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 59.8 ms                                                                                                           | 105 ms: 1.76x slower                                                                                                    |
| genshi_text     | 27.5 ms                                                                                                           | 53.4 ms: 1.94x slower                                                                                                   |
| django_template | 42.4 ms                                                                                                           | 84.2 ms: 1.98x slower                                                                                                   |
| mako            | 13.3 ms                                                                                                           | 28.9 ms: 2.17x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.96x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json | results/bm-20240824-3.14.0a0-52caaef-NOGIL/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| create_gc_cycles           | 2.31 ms                                                                                                           | 1.64 ms: 1.41x faster                                                                                                   |
| gc_traversal               | 4.91 ms                                                                                                           | 3.50 ms: 1.40x faster                                                                                                   |
| regex_effbot               | 4.88 ms                                                                                                           | 4.48 ms: 1.09x faster                                                                                                   |
| asyncio_websockets         | 660 ms                                                                                                            | 672 ms: 1.02x slower                                                                                                    |
| regex_dna                  | 252 ms                                                                                                            | 258 ms: 1.02x slower                                                                                                    |
| xml_etree_iterparse        | 151 ms                                                                                                            | 160 ms: 1.06x slower                                                                                                    |
| regex_v8                   | 30.5 ms                                                                                                           | 32.8 ms: 1.08x slower                                                                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                                                                          | 2.46 sec: 1.11x slower                                                                                                  |
| asyncio_tcp                | 564 ms                                                                                                            | 642 ms: 1.14x slower                                                                                                    |
| async_tree_io_tg           | 1.17 sec                                                                                                          | 1.37 sec: 1.17x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 732 ms                                                                                                            | 877 ms: 1.20x slower                                                                                                    |
| json_loads                 | 32.6 us                                                                                                           | 39.5 us: 1.21x slower                                                                                                   |
| async_tree_io              | 1.14 sec                                                                                                          | 1.41 sec: 1.23x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 727 ms                                                                                                            | 908 ms: 1.25x slower                                                                                                    |
| json                       | 5.66 ms                                                                                                           | 7.12 ms: 1.26x slower                                                                                                   |
| async_tree_memoization_tg  | 550 ms                                                                                                            | 695 ms: 1.26x slower                                                                                                    |
| pathlib                    | 21.2 ms                                                                                                           | 26.8 ms: 1.26x slower                                                                                                   |
| mdp                        | 3.37 sec                                                                                                          | 4.34 sec: 1.29x slower                                                                                                  |
| scimark_fft                | 443 ms                                                                                                            | 576 ms: 1.30x slower                                                                                                    |
| docutils                   | 3.09 sec                                                                                                          | 4.04 sec: 1.31x slower                                                                                                  |
| async_tree_memoization     | 557 ms                                                                                                            | 738 ms: 1.33x slower                                                                                                    |
| telco                      | 9.77 ms                                                                                                           | 13.2 ms: 1.35x slower                                                                                                   |
| async_tree_none_tg         | 419 ms                                                                                                            | 570 ms: 1.36x slower                                                                                                    |
| async_generators           | 485 ms                                                                                                            | 665 ms: 1.37x slower                                                                                                    |
| coverage                   | 98.4 ms                                                                                                           | 136 ms: 1.38x slower                                                                                                    |
| python_startup_no_site     | 8.77 ms                                                                                                           | 12.1 ms: 1.38x slower                                                                                                   |
| python_startup             | 13.0 ms                                                                                                           | 18.0 ms: 1.38x slower                                                                                                   |
| scimark_sparse_mat_mult    | 6.49 ms                                                                                                           | 9.03 ms: 1.39x slower                                                                                                   |
| json_dumps                 | 13.1 ms                                                                                                           | 18.3 ms: 1.40x slower                                                                                                   |
| pylint                     | 358 ms                                                                                                            | 509 ms: 1.42x slower                                                                                                    |
| async_tree_none            | 423 ms                                                                                                            | 606 ms: 1.43x slower                                                                                                    |
| xml_etree_generate         | 113 ms                                                                                                            | 162 ms: 1.44x slower                                                                                                    |
| coroutines                 | 28.4 ms                                                                                                           | 41.3 ms: 1.45x slower                                                                                                   |
| meteor_contest             | 111 ms                                                                                                            | 167 ms: 1.50x slower                                                                                                    |
| nqueens                    | 98.3 ms                                                                                                           | 153 ms: 1.56x slower                                                                                                    |
| tomli_loads                | 2.62 sec                                                                                                          | 4.20 sec: 1.61x slower                                                                                                  |
| fannkuch                   | 458 ms                                                                                                            | 740 ms: 1.62x slower                                                                                                    |
| tornado_http               | 125 ms                                                                                                            | 204 ms: 1.63x slower                                                                                                    |
| bpe_tokeniser              | 5.84 sec                                                                                                          | 9.54 sec: 1.64x slower                                                                                                  |
| generators                 | 35.0 ms                                                                                                           | 57.4 ms: 1.64x slower                                                                                                   |
| spectral_norm              | 140 ms                                                                                                            | 233 ms: 1.66x slower                                                                                                    |
| pycparser                  | 1.22 sec                                                                                                          | 2.03 sec: 1.66x slower                                                                                                  |
| crypto_pyaes               | 82.1 ms                                                                                                           | 137 ms: 1.67x slower                                                                                                    |
| xml_etree_process          | 78.3 ms                                                                                                           | 131 ms: 1.68x slower                                                                                                    |
| sympy_integrate            | 20.6 ms                                                                                                           | 34.7 ms: 1.69x slower                                                                                                   |
| deepcopy                   | 336 us                                                                                                            | 566 us: 1.69x slower                                                                                                    |
| bench_thread_pool          | 1.23 ms                                                                                                           | 2.10 ms: 1.70x slower                                                                                                   |
| deepcopy_reduce            | 3.50 us                                                                                                           | 6.08 us: 1.73x slower                                                                                                   |
| 2to3                       | 297 ms                                                                                                            | 521 ms: 1.75x slower                                                                                                    |
| genshi_xml                 | 59.8 ms                                                                                                           | 105 ms: 1.76x slower                                                                                                    |
| typing_runtime_protocols   | 192 us                                                                                                            | 339 us: 1.77x slower                                                                                                    |
| thrift                     | 921 us                                                                                                            | 1.66 ms: 1.80x slower                                                                                                   |
| html5lib                   | 67.8 ms                                                                                                           | 122 ms: 1.80x slower                                                                                                    |
| sqlglot_normalize          | 129 ms                                                                                                            | 234 ms: 1.82x slower                                                                                                    |
| pyflate                    | 554 ms                                                                                                            | 1.01 sec: 1.83x slower                                                                                                  |
| sqlglot_optimize           | 62.2 ms                                                                                                           | 117 ms: 1.88x slower                                                                                                    |
| deepcopy_memo              | 38.0 us                                                                                                           | 72.2 us: 1.90x slower                                                                                                   |
| sympy_str                  | 265 ms                                                                                                            | 514 ms: 1.94x slower                                                                                                    |
| genshi_text                | 27.5 ms                                                                                                           | 53.4 ms: 1.94x slower                                                                                                   |
| pprint_safe_repr           | 909 ms                                                                                                            | 1.78 sec: 1.95x slower                                                                                                  |
| pprint_pformat             | 1.87 sec                                                                                                          | 3.66 sec: 1.96x slower                                                                                                  |
| comprehensions             | 20.7 us                                                                                                           | 40.7 us: 1.96x slower                                                                                                   |
| django_template            | 42.4 ms                                                                                                           | 84.2 ms: 1.98x slower                                                                                                   |
| logging_format             | 7.61 us                                                                                                           | 15.7 us: 2.06x slower                                                                                                   |
| logging_simple             | 6.90 us                                                                                                           | 14.5 us: 2.10x slower                                                                                                   |
| regex_compile              | 123 ms                                                                                                            | 260 ms: 2.11x slower                                                                                                    |
| sympy_expand               | 459 ms                                                                                                            | 969 ms: 2.11x slower                                                                                                    |
| scimark_monte_carlo        | 81.5 ms                                                                                                           | 174 ms: 2.13x slower                                                                                                    |
| mako                       | 13.3 ms                                                                                                           | 28.9 ms: 2.17x slower                                                                                                   |
| unpickle_pure_python       | 252 us                                                                                                            | 548 us: 2.17x slower                                                                                                    |
| scimark_sor                | 158 ms                                                                                                            | 342 ms: 2.17x slower                                                                                                    |
| logging_silent             | 132 ns                                                                                                            | 287 ns: 2.18x slower                                                                                                    |
| pickle_pure_python         | 356 us                                                                                                            | 776 us: 2.18x slower                                                                                                    |
| richards                   | 53.0 ms                                                                                                           | 118 ms: 2.22x slower                                                                                                    |
| sympy_sum                  | 141 ms                                                                                                            | 315 ms: 2.23x slower                                                                                                    |
| hexiom                     | 7.02 ms                                                                                                           | 15.9 ms: 2.27x slower                                                                                                   |
| float                      | 91.2 ms                                                                                                           | 209 ms: 2.29x slower                                                                                                    |
| go                         | 193 ms                                                                                                            | 443 ms: 2.29x slower                                                                                                    |
| chaos                      | 68.4 ms                                                                                                           | 159 ms: 2.33x slower                                                                                                    |
| richards_super             | 59.0 ms                                                                                                           | 138 ms: 2.33x slower                                                                                                    |
| sqlglot_transpile          | 1.71 ms                                                                                                           | 4.30 ms: 2.52x slower                                                                                                   |
| sqlglot_parse              | 1.42 ms                                                                                                           | 3.70 ms: 2.60x slower                                                                                                   |
| nbody                      | 108 ms                                                                                                            | 282 ms: 2.61x slower                                                                                                    |
| scimark_lu                 | 134 ms                                                                                                            | 355 ms: 2.64x slower                                                                                                    |
| raytrace                   | 303 ms                                                                                                            | 817 ms: 2.69x slower                                                                                                    |
| deltablue                  | 3.89 ms                                                                                                           | 12.8 ms: 3.30x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.61x slower                                                                                                            |

Benchmark hidden because not significant (3): xml_etree_parse, bench_mp_pool, pidigits

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.48x
- 95% likely to have a slowdown of 1.45x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: 1.17x