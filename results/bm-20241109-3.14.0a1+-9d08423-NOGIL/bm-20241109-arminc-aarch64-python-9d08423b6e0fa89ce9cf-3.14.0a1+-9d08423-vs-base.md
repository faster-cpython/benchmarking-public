# Results vs. base

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-aarch64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.362x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.38x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                                                              | 538 ms: 1.76x slower                                                                                                      |
| docutils       | 3.13 sec                                                                                                            | 4.28 sec: 1.37x slower                                                                                                    |
| html5lib       | 72.8 ms                                                                                                             | 123 ms: 1.69x slower                                                                                                      |
| sphinx         | 1.24 sec                                                                                                            | 1.70 sec: 1.37x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.54x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                                                                            | 1.44 sec: 1.13x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 749 ms                                                                                                              | 925 ms: 1.23x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 763 ms                                                                                                              | 951 ms: 1.25x slower                                                                                                      |
| async_tree_io              | 1.16 sec                                                                                                            | 1.47 sec: 1.26x slower                                                                                                    |
| async_tree_memoization     | 611 ms                                                                                                              | 790 ms: 1.29x slower                                                                                                      |
| async_tree_none_tg         | 458 ms                                                                                                              | 614 ms: 1.34x slower                                                                                                      |
| async_tree_memoization_tg  | 552 ms                                                                                                              | 759 ms: 1.38x slower                                                                                                      |
| async_tree_none            | 458 ms                                                                                                              | 635 ms: 1.39x slower                                                                                                      |
| async_generators           | 496 ms                                                                                                              | 703 ms: 1.42x slower                                                                                                      |
| coroutines                 | 28.5 ms                                                                                                             | 40.6 ms: 1.43x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.28x slower                                                                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 98.6 ms                                                                                                             | 213 ms: 2.17x slower                                                                                                      |
| nbody          | 123 ms                                                                                                              | 280 ms: 2.27x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.70x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 5.07 ms                                                                                                             | 4.77 ms: 1.06x faster                                                                                                     |
| regex_v8       | 32.2 ms                                                                                                             | 35.4 ms: 1.10x slower                                                                                                     |
| regex_compile  | 130 ms                                                                                                              | 256 ms: 1.97x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.19x slower                                                                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                                                                              | 187 ms: 1.06x faster                                                                                                      |
| json_loads           | 32.8 us                                                                                                             | 39.2 us: 1.19x slower                                                                                                     |
| json_dumps           | 14.8 ms                                                                                                             | 20.2 ms: 1.36x slower                                                                                                     |
| xml_etree_generate   | 114 ms                                                                                                              | 164 ms: 1.45x slower                                                                                                      |
| tomli_loads          | 2.78 sec                                                                                                            | 4.28 sec: 1.54x slower                                                                                                    |
| xml_etree_process    | 84.2 ms                                                                                                             | 133 ms: 1.58x slower                                                                                                      |
| pickle_pure_python   | 401 us                                                                                                              | 842 us: 2.10x slower                                                                                                      |
| unpickle_pure_python | 268 us                                                                                                              | 567 us: 2.12x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.43x slower                                                                                                              |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.1 ms                                                                                                             | 21.1 ms: 1.31x slower                                                                                                     |
| python_startup_no_site | 9.02 ms                                                                                                             | 12.5 ms: 1.39x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.35x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 61.7 ms                                                                                                             | 104 ms: 1.68x slower                                                                                                      |
| django_template | 43.7 ms                                                                                                             | 83.8 ms: 1.92x slower                                                                                                     |
| genshi_text     | 28.8 ms                                                                                                             | 56.6 ms: 1.96x slower                                                                                                     |
| mako            | 14.4 ms                                                                                                             | 29.3 ms: 2.04x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.90x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                  | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 6.80 sec                                                                                                            | 63.5 ms: 107.02x faster                                                                                                   |
| gc_traversal               | 6.75 ms                                                                                                             | 4.48 ms: 1.51x faster                                                                                                     |
| create_gc_cycles           | 3.83 ms                                                                                                             | 2.65 ms: 1.44x faster                                                                                                     |
| k_core                     | 4.56 sec                                                                                                            | 3.59 sec: 1.27x faster                                                                                                    |
| regex_effbot               | 5.07 ms                                                                                                             | 4.77 ms: 1.06x faster                                                                                                     |
| xml_etree_parse            | 197 ms                                                                                                              | 187 ms: 1.06x faster                                                                                                      |
| regex_v8                   | 32.2 ms                                                                                                             | 35.4 ms: 1.10x slower                                                                                                     |
| async_tree_io_tg           | 1.27 sec                                                                                                            | 1.44 sec: 1.13x slower                                                                                                    |
| json_loads                 | 32.8 us                                                                                                             | 39.2 us: 1.19x slower                                                                                                     |
| scimark_fft                | 455 ms                                                                                                              | 549 ms: 1.21x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 749 ms                                                                                                              | 925 ms: 1.23x slower                                                                                                      |
| json                       | 5.63 ms                                                                                                             | 7.01 ms: 1.25x slower                                                                                                     |
| async_tree_cpu_io_mixed    | 763 ms                                                                                                              | 951 ms: 1.25x slower                                                                                                      |
| async_tree_io              | 1.16 sec                                                                                                            | 1.47 sec: 1.26x slower                                                                                                    |
| pathlib                    | 22.4 ms                                                                                                             | 28.4 ms: 1.27x slower                                                                                                     |
| shortest_path              | 574 ms                                                                                                              | 737 ms: 1.28x slower                                                                                                      |
| mdp                        | 3.51 sec                                                                                                            | 4.52 sec: 1.29x slower                                                                                                    |
| async_tree_memoization     | 611 ms                                                                                                              | 790 ms: 1.29x slower                                                                                                      |
| python_startup             | 16.1 ms                                                                                                             | 21.1 ms: 1.31x slower                                                                                                     |
| scimark_sparse_mat_mult    | 6.82 ms                                                                                                             | 8.93 ms: 1.31x slower                                                                                                     |
| connected_components       | 545 ms                                                                                                              | 714 ms: 1.31x slower                                                                                                      |
| async_tree_none_tg         | 458 ms                                                                                                              | 614 ms: 1.34x slower                                                                                                      |
| json_dumps                 | 14.8 ms                                                                                                             | 20.2 ms: 1.36x slower                                                                                                     |
| docutils                   | 3.13 sec                                                                                                            | 4.28 sec: 1.37x slower                                                                                                    |
| sphinx                     | 1.24 sec                                                                                                            | 1.70 sec: 1.37x slower                                                                                                    |
| async_tree_memoization_tg  | 552 ms                                                                                                              | 759 ms: 1.38x slower                                                                                                      |
| telco                      | 9.40 ms                                                                                                             | 13.0 ms: 1.39x slower                                                                                                     |
| async_tree_none            | 458 ms                                                                                                              | 635 ms: 1.39x slower                                                                                                      |
| python_startup_no_site     | 9.02 ms                                                                                                             | 12.5 ms: 1.39x slower                                                                                                     |
| coverage                   | 102 ms                                                                                                              | 142 ms: 1.40x slower                                                                                                      |
| async_generators           | 496 ms                                                                                                              | 703 ms: 1.42x slower                                                                                                      |
| coroutines                 | 28.5 ms                                                                                                             | 40.6 ms: 1.43x slower                                                                                                     |
| pylint                     | 365 ms                                                                                                              | 523 ms: 1.43x slower                                                                                                      |
| xml_etree_generate         | 114 ms                                                                                                              | 164 ms: 1.45x slower                                                                                                      |
| spectral_norm              | 150 ms                                                                                                              | 219 ms: 1.45x slower                                                                                                      |
| nqueens                    | 108 ms                                                                                                              | 159 ms: 1.47x slower                                                                                                      |
| meteor_contest             | 117 ms                                                                                                              | 177 ms: 1.51x slower                                                                                                      |
| fannkuch                   | 491 ms                                                                                                              | 751 ms: 1.53x slower                                                                                                      |
| tomli_loads                | 2.78 sec                                                                                                            | 4.28 sec: 1.54x slower                                                                                                    |
| deepcopy                   | 355 us                                                                                                              | 547 us: 1.54x slower                                                                                                      |
| xml_etree_process          | 84.2 ms                                                                                                             | 133 ms: 1.58x slower                                                                                                      |
| bpe_tokeniser              | 5.92 sec                                                                                                            | 9.36 sec: 1.58x slower                                                                                                    |
| bench_thread_pool          | 1.30 ms                                                                                                             | 2.07 ms: 1.59x slower                                                                                                     |
| sympy_integrate            | 21.9 ms                                                                                                             | 36.3 ms: 1.66x slower                                                                                                     |
| pycparser                  | 1.29 sec                                                                                                            | 2.14 sec: 1.66x slower                                                                                                    |
| pyflate                    | 616 ms                                                                                                              | 1.03 sec: 1.68x slower                                                                                                    |
| genshi_xml                 | 61.7 ms                                                                                                             | 104 ms: 1.68x slower                                                                                                      |
| dulwich_log                | 60.8 ms                                                                                                             | 102 ms: 1.68x slower                                                                                                      |
| html5lib                   | 72.8 ms                                                                                                             | 123 ms: 1.69x slower                                                                                                      |
| deepcopy_reduce            | 3.59 us                                                                                                             | 6.08 us: 1.69x slower                                                                                                     |
| typing_runtime_protocols   | 205 us                                                                                                              | 348 us: 1.70x slower                                                                                                      |
| crypto_pyaes               | 84.3 ms                                                                                                             | 144 ms: 1.71x slower                                                                                                      |
| deepcopy_memo              | 40.6 us                                                                                                             | 70.6 us: 1.74x slower                                                                                                     |
| generators                 | 35.8 ms                                                                                                             | 62.3 ms: 1.74x slower                                                                                                     |
| sqlglot_normalize          | 135 ms                                                                                                              | 236 ms: 1.75x slower                                                                                                      |
| 2to3                       | 306 ms                                                                                                              | 538 ms: 1.76x slower                                                                                                      |
| thrift                     | 961 us                                                                                                              | 1.72 ms: 1.79x slower                                                                                                     |
| sqlglot_optimize           | 63.9 ms                                                                                                             | 115 ms: 1.80x slower                                                                                                      |
| pprint_pformat             | 1.99 sec                                                                                                            | 3.61 sec: 1.81x slower                                                                                                    |
| pprint_safe_repr           | 966 ms                                                                                                              | 1.76 sec: 1.82x slower                                                                                                    |
| sqlalchemy_declarative     | 148 ms                                                                                                              | 273 ms: 1.85x slower                                                                                                      |
| sympy_str                  | 283 ms                                                                                                              | 532 ms: 1.88x slower                                                                                                      |
| django_template            | 43.7 ms                                                                                                             | 83.8 ms: 1.92x slower                                                                                                     |
| genshi_text                | 28.8 ms                                                                                                             | 56.6 ms: 1.96x slower                                                                                                     |
| regex_compile              | 130 ms                                                                                                              | 256 ms: 1.97x slower                                                                                                      |
| comprehensions             | 21.2 us                                                                                                             | 42.8 us: 2.02x slower                                                                                                     |
| mako                       | 14.4 ms                                                                                                             | 29.3 ms: 2.04x slower                                                                                                     |
| logging_silent             | 143 ns                                                                                                              | 292 ns: 2.05x slower                                                                                                      |
| scimark_monte_carlo        | 86.4 ms                                                                                                             | 177 ms: 2.05x slower                                                                                                      |
| logging_simple             | 7.30 us                                                                                                             | 15.0 us: 2.06x slower                                                                                                     |
| logging_format             | 8.01 us                                                                                                             | 16.5 us: 2.06x slower                                                                                                     |
| sqlalchemy_imperative      | 15.5 ms                                                                                                             | 32.2 ms: 2.07x slower                                                                                                     |
| pickle_pure_python         | 401 us                                                                                                              | 842 us: 2.10x slower                                                                                                      |
| sympy_expand               | 470 ms                                                                                                              | 988 ms: 2.10x slower                                                                                                      |
| scimark_sor                | 165 ms                                                                                                              | 346 ms: 2.10x slower                                                                                                      |
| unpickle_pure_python       | 268 us                                                                                                              | 567 us: 2.12x slower                                                                                                      |
| hexiom                     | 7.56 ms                                                                                                             | 16.0 ms: 2.12x slower                                                                                                     |
| float                      | 98.6 ms                                                                                                             | 213 ms: 2.17x slower                                                                                                      |
| richards                   | 55.0 ms                                                                                                             | 121 ms: 2.19x slower                                                                                                      |
| chaos                      | 71.4 ms                                                                                                             | 159 ms: 2.23x slower                                                                                                      |
| nbody                      | 123 ms                                                                                                              | 280 ms: 2.27x slower                                                                                                      |
| sympy_sum                  | 144 ms                                                                                                              | 329 ms: 2.28x slower                                                                                                      |
| richards_super             | 62.6 ms                                                                                                             | 147 ms: 2.35x slower                                                                                                      |
| sqlglot_transpile          | 1.83 ms                                                                                                             | 4.49 ms: 2.46x slower                                                                                                     |
| scimark_lu                 | 140 ms                                                                                                              | 346 ms: 2.48x slower                                                                                                      |
| sqlglot_parse              | 1.47 ms                                                                                                             | 3.81 ms: 2.60x slower                                                                                                     |
| raytrace                   | 320 ms                                                                                                              | 835 ms: 2.61x slower                                                                                                      |
| go                         | 147 ms                                                                                                              | 402 ms: 2.73x slower                                                                                                      |
| deltablue                  | 4.20 ms                                                                                                             | 13.4 ms: 3.18x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.49x slower                                                                                                              |

Benchmark hidden because not significant (5): regex_dna, pidigits, sqlite_synth, asyncio_websockets, xml_etree_iterparse

- Geometric mean (including insignificant results): 1.362x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.44x
- 95% likely to have a slowdown of 1.42x
- 99% likely to have a slowdown of 1.38x

# Memory
- memory change: 1.20x