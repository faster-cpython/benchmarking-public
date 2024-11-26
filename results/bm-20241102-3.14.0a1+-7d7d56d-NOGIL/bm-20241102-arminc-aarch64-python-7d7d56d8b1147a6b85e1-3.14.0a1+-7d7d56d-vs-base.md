# Results vs. base

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: linux-aarch64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.361x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.38x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-NOGIL/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 307 ms                                                                                                              | 532 ms: 1.73x slower                                                                                                      |
| docutils       | 3.12 sec                                                                                                            | 4.17 sec: 1.34x slower                                                                                                    |
| html5lib       | 66.4 ms                                                                                                             | 120 ms: 1.80x slower                                                                                                      |
| sphinx         | 1.22 sec                                                                                                            | 1.69 sec: 1.39x slower                                                                                                    |
| tornado_http   | 128 ms                                                                                                              | 196 ms: 1.53x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.55x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-NOGIL/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.28 sec                                                                                                            | 1.42 sec: 1.11x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 761 ms                                                                                                              | 917 ms: 1.21x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 763 ms                                                                                                              | 950 ms: 1.25x slower                                                                                                      |
| async_tree_io              | 1.17 sec                                                                                                            | 1.46 sec: 1.25x slower                                                                                                    |
| async_tree_memoization     | 611 ms                                                                                                              | 780 ms: 1.28x slower                                                                                                      |
| async_tree_none_tg         | 457 ms                                                                                                              | 609 ms: 1.33x slower                                                                                                      |
| coroutines                 | 30.0 ms                                                                                                             | 40.3 ms: 1.34x slower                                                                                                     |
| async_tree_memoization_tg  | 550 ms                                                                                                              | 755 ms: 1.37x slower                                                                                                      |
| async_generators           | 498 ms                                                                                                              | 684 ms: 1.37x slower                                                                                                      |
| async_tree_none            | 457 ms                                                                                                              | 636 ms: 1.39x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.26x slower                                                                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-NOGIL/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 99.9 ms                                                                                                             | 213 ms: 2.13x slower                                                                                                      |
| nbody          | 120 ms                                                                                                              | 295 ms: 2.45x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.74x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-NOGIL/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 5.11 ms                                                                                                             | 4.63 ms: 1.10x faster                                                                                                     |
| regex_compile  | 132 ms                                                                                                              | 260 ms: 1.97x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.17x slower                                                                                                              |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-NOGIL/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| json_loads           | 32.7 us                                                                                                             | 39.1 us: 1.20x slower                                                                                                     |
| json_dumps           | 14.8 ms                                                                                                             | 20.0 ms: 1.35x slower                                                                                                     |
| xml_etree_generate   | 115 ms                                                                                                              | 170 ms: 1.48x slower                                                                                                      |
| tomli_loads          | 2.74 sec                                                                                                            | 4.33 sec: 1.58x slower                                                                                                    |
| xml_etree_process    | 84.7 ms                                                                                                             | 135 ms: 1.59x slower                                                                                                      |
| unpickle_pure_python | 269 us                                                                                                              | 566 us: 2.10x slower                                                                                                      |
| pickle_pure_python   | 381 us                                                                                                              | 828 us: 2.17x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.44x slower                                                                                                              |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-NOGIL/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.2 ms                                                                                                             | 20.8 ms: 1.28x slower                                                                                                     |
| python_startup_no_site | 8.95 ms                                                                                                             | 12.3 ms: 1.37x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.33x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-NOGIL/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 63.9 ms                                                                                                             | 109 ms: 1.71x slower                                                                                                      |
| genshi_text     | 29.4 ms                                                                                                             | 54.0 ms: 1.84x slower                                                                                                     |
| django_template | 43.6 ms                                                                                                             | 85.1 ms: 1.95x slower                                                                                                     |
| mako            | 14.0 ms                                                                                                             | 29.7 ms: 2.12x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.90x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                  | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-NOGIL/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 5.50 sec                                                                                                            | 63.9 ms: 86.07x faster                                                                                                    |
| gc_traversal               | 6.88 ms                                                                                                             | 4.59 ms: 1.50x faster                                                                                                     |
| create_gc_cycles           | 3.89 ms                                                                                                             | 2.71 ms: 1.44x faster                                                                                                     |
| k_core                     | 4.56 sec                                                                                                            | 3.52 sec: 1.29x faster                                                                                                    |
| regex_effbot               | 5.11 ms                                                                                                             | 4.63 ms: 1.10x faster                                                                                                     |
| sqlite_synth               | 4.15 us                                                                                                             | 4.34 us: 1.05x slower                                                                                                     |
| async_tree_io_tg           | 1.28 sec                                                                                                            | 1.42 sec: 1.11x slower                                                                                                    |
| json                       | 5.91 ms                                                                                                             | 6.87 ms: 1.16x slower                                                                                                     |
| json_loads                 | 32.7 us                                                                                                             | 39.1 us: 1.20x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 761 ms                                                                                                              | 917 ms: 1.21x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 763 ms                                                                                                              | 950 ms: 1.25x slower                                                                                                      |
| async_tree_io              | 1.17 sec                                                                                                            | 1.46 sec: 1.25x slower                                                                                                    |
| connected_components       | 551 ms                                                                                                              | 701 ms: 1.27x slower                                                                                                      |
| async_tree_memoization     | 611 ms                                                                                                              | 780 ms: 1.28x slower                                                                                                      |
| python_startup             | 16.2 ms                                                                                                             | 20.8 ms: 1.28x slower                                                                                                     |
| shortest_path              | 573 ms                                                                                                              | 736 ms: 1.28x slower                                                                                                      |
| scimark_fft                | 457 ms                                                                                                              | 593 ms: 1.30x slower                                                                                                      |
| mdp                        | 3.46 sec                                                                                                            | 4.48 sec: 1.30x slower                                                                                                    |
| pathlib                    | 22.1 ms                                                                                                             | 29.0 ms: 1.31x slower                                                                                                     |
| telco                      | 9.87 ms                                                                                                             | 13.0 ms: 1.32x slower                                                                                                     |
| scimark_sparse_mat_mult    | 6.77 ms                                                                                                             | 8.97 ms: 1.33x slower                                                                                                     |
| async_tree_none_tg         | 457 ms                                                                                                              | 609 ms: 1.33x slower                                                                                                      |
| docutils                   | 3.12 sec                                                                                                            | 4.17 sec: 1.34x slower                                                                                                    |
| coroutines                 | 30.0 ms                                                                                                             | 40.3 ms: 1.34x slower                                                                                                     |
| json_dumps                 | 14.8 ms                                                                                                             | 20.0 ms: 1.35x slower                                                                                                     |
| python_startup_no_site     | 8.95 ms                                                                                                             | 12.3 ms: 1.37x slower                                                                                                     |
| async_tree_memoization_tg  | 550 ms                                                                                                              | 755 ms: 1.37x slower                                                                                                      |
| async_generators           | 498 ms                                                                                                              | 684 ms: 1.37x slower                                                                                                      |
| sphinx                     | 1.22 sec                                                                                                            | 1.69 sec: 1.39x slower                                                                                                    |
| async_tree_none            | 457 ms                                                                                                              | 636 ms: 1.39x slower                                                                                                      |
| coverage                   | 100 ms                                                                                                              | 142 ms: 1.42x slower                                                                                                      |
| pylint                     | 362 ms                                                                                                              | 522 ms: 1.44x slower                                                                                                      |
| xml_etree_generate         | 115 ms                                                                                                              | 170 ms: 1.48x slower                                                                                                      |
| meteor_contest             | 113 ms                                                                                                              | 172 ms: 1.51x slower                                                                                                      |
| spectral_norm              | 152 ms                                                                                                              | 231 ms: 1.52x slower                                                                                                      |
| nqueens                    | 103 ms                                                                                                              | 157 ms: 1.53x slower                                                                                                      |
| tornado_http               | 128 ms                                                                                                              | 196 ms: 1.53x slower                                                                                                      |
| deepcopy                   | 355 us                                                                                                              | 551 us: 1.55x slower                                                                                                      |
| dulwich_log                | 61.9 ms                                                                                                             | 97.7 ms: 1.58x slower                                                                                                     |
| tomli_loads                | 2.74 sec                                                                                                            | 4.33 sec: 1.58x slower                                                                                                    |
| bench_thread_pool          | 1.28 ms                                                                                                             | 2.03 ms: 1.59x slower                                                                                                     |
| xml_etree_process          | 84.7 ms                                                                                                             | 135 ms: 1.59x slower                                                                                                      |
| bpe_tokeniser              | 5.87 sec                                                                                                            | 9.40 sec: 1.60x slower                                                                                                    |
| typing_runtime_protocols   | 208 us                                                                                                              | 338 us: 1.63x slower                                                                                                      |
| deepcopy_reduce            | 3.73 us                                                                                                             | 6.10 us: 1.64x slower                                                                                                     |
| pycparser                  | 1.29 sec                                                                                                            | 2.14 sec: 1.66x slower                                                                                                    |
| fannkuch                   | 478 ms                                                                                                              | 797 ms: 1.67x slower                                                                                                      |
| sympy_integrate            | 21.7 ms                                                                                                             | 36.3 ms: 1.67x slower                                                                                                     |
| crypto_pyaes               | 85.8 ms                                                                                                             | 145 ms: 1.69x slower                                                                                                      |
| generators                 | 36.2 ms                                                                                                             | 61.5 ms: 1.70x slower                                                                                                     |
| genshi_xml                 | 63.9 ms                                                                                                             | 109 ms: 1.71x slower                                                                                                      |
| pyflate                    | 605 ms                                                                                                              | 1.04 sec: 1.72x slower                                                                                                    |
| 2to3                       | 307 ms                                                                                                              | 532 ms: 1.73x slower                                                                                                      |
| sqlglot_normalize          | 134 ms                                                                                                              | 234 ms: 1.74x slower                                                                                                      |
| sqlglot_optimize           | 65.8 ms                                                                                                             | 118 ms: 1.80x slower                                                                                                      |
| html5lib                   | 66.4 ms                                                                                                             | 120 ms: 1.80x slower                                                                                                      |
| pprint_pformat             | 1.99 sec                                                                                                            | 3.61 sec: 1.81x slower                                                                                                    |
| thrift                     | 985 us                                                                                                              | 1.79 ms: 1.82x slower                                                                                                     |
| genshi_text                | 29.4 ms                                                                                                             | 54.0 ms: 1.84x slower                                                                                                     |
| pprint_safe_repr           | 963 ms                                                                                                              | 1.77 sec: 1.84x slower                                                                                                    |
| sqlalchemy_imperative      | 16.1 ms                                                                                                             | 30.0 ms: 1.87x slower                                                                                                     |
| sympy_str                  | 283 ms                                                                                                              | 530 ms: 1.87x slower                                                                                                      |
| sqlalchemy_declarative     | 143 ms                                                                                                              | 271 ms: 1.89x slower                                                                                                      |
| deepcopy_memo              | 39.6 us                                                                                                             | 76.2 us: 1.93x slower                                                                                                     |
| django_template            | 43.6 ms                                                                                                             | 85.1 ms: 1.95x slower                                                                                                     |
| regex_compile              | 132 ms                                                                                                              | 260 ms: 1.97x slower                                                                                                      |
| scimark_monte_carlo        | 88.8 ms                                                                                                             | 177 ms: 2.00x slower                                                                                                      |
| logging_format             | 8.13 us                                                                                                             | 16.3 us: 2.01x slower                                                                                                     |
| comprehensions             | 21.3 us                                                                                                             | 42.9 us: 2.01x slower                                                                                                     |
| logging_simple             | 7.20 us                                                                                                             | 14.5 us: 2.01x slower                                                                                                     |
| sympy_expand               | 476 ms                                                                                                              | 980 ms: 2.06x slower                                                                                                      |
| unpickle_pure_python       | 269 us                                                                                                              | 566 us: 2.10x slower                                                                                                      |
| mako                       | 14.0 ms                                                                                                             | 29.7 ms: 2.12x slower                                                                                                     |
| logging_silent             | 137 ns                                                                                                              | 290 ns: 2.12x slower                                                                                                      |
| float                      | 99.9 ms                                                                                                             | 213 ms: 2.13x slower                                                                                                      |
| scimark_sor                | 166 ms                                                                                                              | 359 ms: 2.16x slower                                                                                                      |
| pickle_pure_python         | 381 us                                                                                                              | 828 us: 2.17x slower                                                                                                      |
| richards_super             | 63.8 ms                                                                                                             | 139 ms: 2.19x slower                                                                                                      |
| hexiom                     | 7.35 ms                                                                                                             | 16.1 ms: 2.19x slower                                                                                                     |
| richards                   | 56.1 ms                                                                                                             | 124 ms: 2.21x slower                                                                                                      |
| chaos                      | 71.9 ms                                                                                                             | 161 ms: 2.25x slower                                                                                                      |
| sympy_sum                  | 147 ms                                                                                                              | 329 ms: 2.25x slower                                                                                                      |
| sqlglot_transpile          | 1.85 ms                                                                                                             | 4.51 ms: 2.44x slower                                                                                                     |
| nbody                      | 120 ms                                                                                                              | 295 ms: 2.45x slower                                                                                                      |
| scimark_lu                 | 138 ms                                                                                                              | 347 ms: 2.51x slower                                                                                                      |
| sqlglot_parse              | 1.48 ms                                                                                                             | 3.80 ms: 2.58x slower                                                                                                     |
| raytrace                   | 327 ms                                                                                                              | 891 ms: 2.72x slower                                                                                                      |
| go                         | 143 ms                                                                                                              | 407 ms: 2.85x slower                                                                                                      |
| deltablue                  | 4.11 ms                                                                                                             | 12.8 ms: 3.11x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.50x slower                                                                                                              |

Benchmark hidden because not significant (6): xml_etree_parse, xml_etree_iterparse, pidigits, regex_v8, regex_dna, asyncio_websockets

- Geometric mean (including insignificant results): 1.361x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.45x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.38x

# Memory
- memory change: 1.17x