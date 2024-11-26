# Results vs. base

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-aarch64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.377x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-NOGIL/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 294 ms                                                                                                              | 512 ms: 1.74x slower                                                                                                      |
| docutils       | 3.01 sec                                                                                                            | 4.09 sec: 1.36x slower                                                                                                    |
| html5lib       | 65.3 ms                                                                                                             | 119 ms: 1.82x slower                                                                                                      |
| sphinx         | 1.19 sec                                                                                                            | 1.64 sec: 1.39x slower                                                                                                    |
| tornado_http   | 125 ms                                                                                                              | 205 ms: 1.63x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.58x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-NOGIL/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets         | 658 ms                                                                                                              | 673 ms: 1.02x slower                                                                                                      |
| async_tree_io_tg           | 1.25 sec                                                                                                            | 1.36 sec: 1.09x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 733 ms                                                                                                              | 884 ms: 1.21x slower                                                                                                      |
| async_tree_io              | 1.13 sec                                                                                                            | 1.39 sec: 1.23x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 743 ms                                                                                                              | 917 ms: 1.23x slower                                                                                                      |
| async_tree_memoization     | 578 ms                                                                                                              | 742 ms: 1.28x slower                                                                                                      |
| async_tree_none_tg         | 438 ms                                                                                                              | 583 ms: 1.33x slower                                                                                                      |
| async_tree_memoization_tg  | 528 ms                                                                                                              | 710 ms: 1.35x slower                                                                                                      |
| async_tree_none            | 445 ms                                                                                                              | 608 ms: 1.37x slower                                                                                                      |
| async_generators           | 477 ms                                                                                                              | 658 ms: 1.38x slower                                                                                                      |
| coroutines                 | 28.6 ms                                                                                                             | 40.0 ms: 1.40x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.26x slower                                                                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-NOGIL/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 95.1 ms                                                                                                             | 209 ms: 2.20x slower                                                                                                      |
| nbody          | 117 ms                                                                                                              | 286 ms: 2.44x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.75x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-NOGIL/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 4.96 ms                                                                                                             | 4.48 ms: 1.11x faster                                                                                                     |
| regex_v8       | 31.9 ms                                                                                                             | 32.9 ms: 1.03x slower                                                                                                     |
| regex_compile  | 125 ms                                                                                                              | 250 ms: 2.00x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.17x slower                                                                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-NOGIL/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_parse      | 186 ms                                                                                                              | 182 ms: 1.03x faster                                                                                                      |
| xml_etree_iterparse  | 147 ms                                                                                                              | 153 ms: 1.04x slower                                                                                                      |
| json_loads           | 31.3 us                                                                                                             | 37.3 us: 1.19x slower                                                                                                     |
| json_dumps           | 14.1 ms                                                                                                             | 18.9 ms: 1.34x slower                                                                                                     |
| xml_etree_generate   | 113 ms                                                                                                              | 158 ms: 1.40x slower                                                                                                      |
| xml_etree_process    | 80.9 ms                                                                                                             | 127 ms: 1.58x slower                                                                                                      |
| tomli_loads          | 2.63 sec                                                                                                            | 4.19 sec: 1.60x slower                                                                                                    |
| unpickle_pure_python | 257 us                                                                                                              | 532 us: 2.07x slower                                                                                                      |
| pickle_pure_python   | 371 us                                                                                                              | 778 us: 2.09x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.43x slower                                                                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-NOGIL/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                                                                             | 20.4 ms: 1.31x slower                                                                                                     |
| python_startup_no_site | 8.67 ms                                                                                                             | 12.1 ms: 1.40x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.35x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-NOGIL/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 60.1 ms                                                                                                             | 101 ms: 1.69x slower                                                                                                      |
| genshi_text     | 27.6 ms                                                                                                             | 51.4 ms: 1.87x slower                                                                                                     |
| django_template | 41.9 ms                                                                                                             | 80.6 ms: 1.92x slower                                                                                                     |
| mako            | 13.6 ms                                                                                                             | 29.2 ms: 2.15x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.90x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                  | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-NOGIL/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 4.94 sec                                                                                                            | 61.1 ms: 80.86x faster                                                                                                    |
| gc_traversal               | 6.31 ms                                                                                                             | 4.43 ms: 1.42x faster                                                                                                     |
| create_gc_cycles           | 3.60 ms                                                                                                             | 2.56 ms: 1.40x faster                                                                                                     |
| regex_effbot               | 4.96 ms                                                                                                             | 4.48 ms: 1.11x faster                                                                                                     |
| xml_etree_parse            | 186 ms                                                                                                              | 182 ms: 1.03x faster                                                                                                      |
| asyncio_websockets         | 658 ms                                                                                                              | 673 ms: 1.02x slower                                                                                                      |
| regex_v8                   | 31.9 ms                                                                                                             | 32.9 ms: 1.03x slower                                                                                                     |
| xml_etree_iterparse        | 147 ms                                                                                                              | 153 ms: 1.04x slower                                                                                                      |
| async_tree_io_tg           | 1.25 sec                                                                                                            | 1.36 sec: 1.09x slower                                                                                                    |
| json_loads                 | 31.3 us                                                                                                             | 37.3 us: 1.19x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 733 ms                                                                                                              | 884 ms: 1.21x slower                                                                                                      |
| pathlib                    | 21.5 ms                                                                                                             | 26.1 ms: 1.22x slower                                                                                                     |
| async_tree_io              | 1.13 sec                                                                                                            | 1.39 sec: 1.23x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 743 ms                                                                                                              | 917 ms: 1.23x slower                                                                                                      |
| json                       | 5.46 ms                                                                                                             | 6.75 ms: 1.24x slower                                                                                                     |
| async_tree_memoization     | 578 ms                                                                                                              | 742 ms: 1.28x slower                                                                                                      |
| mdp                        | 3.35 sec                                                                                                            | 4.31 sec: 1.29x slower                                                                                                    |
| scimark_fft                | 438 ms                                                                                                              | 569 ms: 1.30x slower                                                                                                      |
| python_startup             | 15.6 ms                                                                                                             | 20.4 ms: 1.31x slower                                                                                                     |
| async_tree_none_tg         | 438 ms                                                                                                              | 583 ms: 1.33x slower                                                                                                      |
| json_dumps                 | 14.1 ms                                                                                                             | 18.9 ms: 1.34x slower                                                                                                     |
| telco                      | 9.45 ms                                                                                                             | 12.6 ms: 1.34x slower                                                                                                     |
| scimark_sparse_mat_mult    | 6.57 ms                                                                                                             | 8.82 ms: 1.34x slower                                                                                                     |
| async_tree_memoization_tg  | 528 ms                                                                                                              | 710 ms: 1.35x slower                                                                                                      |
| docutils                   | 3.01 sec                                                                                                            | 4.09 sec: 1.36x slower                                                                                                    |
| coverage                   | 97.2 ms                                                                                                             | 133 ms: 1.37x slower                                                                                                      |
| async_tree_none            | 445 ms                                                                                                              | 608 ms: 1.37x slower                                                                                                      |
| async_generators           | 477 ms                                                                                                              | 658 ms: 1.38x slower                                                                                                      |
| sphinx                     | 1.19 sec                                                                                                            | 1.64 sec: 1.39x slower                                                                                                    |
| python_startup_no_site     | 8.67 ms                                                                                                             | 12.1 ms: 1.40x slower                                                                                                     |
| coroutines                 | 28.6 ms                                                                                                             | 40.0 ms: 1.40x slower                                                                                                     |
| xml_etree_generate         | 113 ms                                                                                                              | 158 ms: 1.40x slower                                                                                                      |
| pylint                     | 352 ms                                                                                                              | 507 ms: 1.44x slower                                                                                                      |
| meteor_contest             | 113 ms                                                                                                              | 166 ms: 1.47x slower                                                                                                      |
| bench_thread_pool          | 1.28 ms                                                                                                             | 1.96 ms: 1.53x slower                                                                                                     |
| nqueens                    | 98.9 ms                                                                                                             | 153 ms: 1.55x slower                                                                                                      |
| xml_etree_process          | 80.9 ms                                                                                                             | 127 ms: 1.58x slower                                                                                                      |
| bpe_tokeniser              | 5.79 sec                                                                                                            | 9.17 sec: 1.58x slower                                                                                                    |
| deepcopy                   | 336 us                                                                                                              | 536 us: 1.59x slower                                                                                                      |
| tomli_loads                | 2.63 sec                                                                                                            | 4.19 sec: 1.60x slower                                                                                                    |
| spectral_norm              | 144 ms                                                                                                              | 231 ms: 1.60x slower                                                                                                      |
| fannkuch                   | 468 ms                                                                                                              | 751 ms: 1.60x slower                                                                                                      |
| dulwich_log                | 58.7 ms                                                                                                             | 95.8 ms: 1.63x slower                                                                                                     |
| tornado_http               | 125 ms                                                                                                              | 205 ms: 1.63x slower                                                                                                      |
| deepcopy_reduce            | 3.54 us                                                                                                             | 5.84 us: 1.65x slower                                                                                                     |
| pycparser                  | 1.24 sec                                                                                                            | 2.05 sec: 1.66x slower                                                                                                    |
| sympy_integrate            | 21.2 ms                                                                                                             | 35.2 ms: 1.66x slower                                                                                                     |
| typing_runtime_protocols   | 194 us                                                                                                              | 325 us: 1.68x slower                                                                                                      |
| genshi_xml                 | 60.1 ms                                                                                                             | 101 ms: 1.69x slower                                                                                                      |
| crypto_pyaes               | 82.7 ms                                                                                                             | 140 ms: 1.70x slower                                                                                                      |
| generators                 | 34.8 ms                                                                                                             | 59.3 ms: 1.70x slower                                                                                                     |
| sqlglot_normalize          | 128 ms                                                                                                              | 222 ms: 1.74x slower                                                                                                      |
| 2to3                       | 294 ms                                                                                                              | 512 ms: 1.74x slower                                                                                                      |
| pyflate                    | 585 ms                                                                                                              | 1.02 sec: 1.75x slower                                                                                                    |
| thrift                     | 945 us                                                                                                              | 1.69 ms: 1.79x slower                                                                                                     |
| pprint_safe_repr           | 939 ms                                                                                                              | 1.69 sec: 1.80x slower                                                                                                    |
| pprint_pformat             | 1.92 sec                                                                                                            | 3.47 sec: 1.80x slower                                                                                                    |
| deepcopy_memo              | 38.4 us                                                                                                             | 69.5 us: 1.81x slower                                                                                                     |
| sqlglot_optimize           | 62.0 ms                                                                                                             | 113 ms: 1.82x slower                                                                                                      |
| html5lib                   | 65.3 ms                                                                                                             | 119 ms: 1.82x slower                                                                                                      |
| genshi_text                | 27.6 ms                                                                                                             | 51.4 ms: 1.87x slower                                                                                                     |
| sqlalchemy_declarative     | 140 ms                                                                                                              | 268 ms: 1.91x slower                                                                                                      |
| sympy_str                  | 264 ms                                                                                                              | 506 ms: 1.92x slower                                                                                                      |
| django_template            | 41.9 ms                                                                                                             | 80.6 ms: 1.92x slower                                                                                                     |
| sqlalchemy_imperative      | 15.4 ms                                                                                                             | 29.7 ms: 1.93x slower                                                                                                     |
| comprehensions             | 20.8 us                                                                                                             | 41.2 us: 1.98x slower                                                                                                     |
| regex_compile              | 125 ms                                                                                                              | 250 ms: 2.00x slower                                                                                                      |
| logging_format             | 7.62 us                                                                                                             | 15.7 us: 2.06x slower                                                                                                     |
| sympy_expand               | 459 ms                                                                                                              | 948 ms: 2.07x slower                                                                                                      |
| unpickle_pure_python       | 257 us                                                                                                              | 532 us: 2.07x slower                                                                                                      |
| logging_simple             | 6.91 us                                                                                                             | 14.4 us: 2.09x slower                                                                                                     |
| pickle_pure_python         | 371 us                                                                                                              | 778 us: 2.09x slower                                                                                                      |
| mako                       | 13.6 ms                                                                                                             | 29.2 ms: 2.15x slower                                                                                                     |
| logging_silent             | 132 ns                                                                                                              | 285 ns: 2.16x slower                                                                                                      |
| scimark_sor                | 160 ms                                                                                                              | 346 ms: 2.17x slower                                                                                                      |
| scimark_monte_carlo        | 83.3 ms                                                                                                             | 181 ms: 2.17x slower                                                                                                      |
| sympy_sum                  | 142 ms                                                                                                              | 311 ms: 2.18x slower                                                                                                      |
| richards                   | 53.9 ms                                                                                                             | 118 ms: 2.19x slower                                                                                                      |
| float                      | 95.1 ms                                                                                                             | 209 ms: 2.20x slower                                                                                                      |
| hexiom                     | 7.11 ms                                                                                                             | 15.7 ms: 2.21x slower                                                                                                     |
| chaos                      | 70.3 ms                                                                                                             | 159 ms: 2.26x slower                                                                                                      |
| richards_super             | 60.0 ms                                                                                                             | 141 ms: 2.35x slower                                                                                                      |
| nbody                      | 117 ms                                                                                                              | 286 ms: 2.44x slower                                                                                                      |
| sqlglot_transpile          | 1.74 ms                                                                                                             | 4.26 ms: 2.45x slower                                                                                                     |
| scimark_lu                 | 135 ms                                                                                                              | 333 ms: 2.46x slower                                                                                                      |
| sqlglot_parse              | 1.41 ms                                                                                                             | 3.72 ms: 2.64x slower                                                                                                     |
| raytrace                   | 310 ms                                                                                                              | 821 ms: 2.65x slower                                                                                                      |
| go                         | 137 ms                                                                                                              | 391 ms: 2.85x slower                                                                                                      |
| deltablue                  | 3.94 ms                                                                                                             | 12.6 ms: 3.20x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.53x slower                                                                                                              |

Benchmark hidden because not significant (2): pidigits, regex_dna

- Geometric mean (including insignificant results): 1.377x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.51x
- 95% likely to have a slowdown of 1.47x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: 1.16x