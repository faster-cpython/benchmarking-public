# Results vs. base

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-aarch64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.329x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                                                                              | 494 ms: 1.63x slower                                                                                                      |
| docutils       | 3.12 sec                                                                                                            | 3.94 sec: 1.26x slower                                                                                                    |
| html5lib       | 65.0 ms                                                                                                             | 117 ms: 1.80x slower                                                                                                      |
| sphinx         | 1.23 sec                                                                                                            | 1.58 sec: 1.29x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.48x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.24 sec                                                                                                            | 1.38 sec: 1.11x slower                                                                                                    |
| async_tree_io              | 1.17 sec                                                                                                            | 1.39 sec: 1.19x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 760 ms                                                                                                              | 915 ms: 1.20x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 751 ms                                                                                                              | 928 ms: 1.24x slower                                                                                                      |
| async_tree_none_tg         | 476 ms                                                                                                              | 603 ms: 1.27x slower                                                                                                      |
| async_tree_memoization_tg  | 564 ms                                                                                                              | 738 ms: 1.31x slower                                                                                                      |
| async_generators           | 509 ms                                                                                                              | 670 ms: 1.32x slower                                                                                                      |
| async_tree_memoization     | 573 ms                                                                                                              | 759 ms: 1.33x slower                                                                                                      |
| coroutines                 | 28.9 ms                                                                                                             | 39.3 ms: 1.36x slower                                                                                                     |
| async_tree_none            | 445 ms                                                                                                              | 618 ms: 1.39x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.24x slower                                                                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 240 ms                                                                                                              | 232 ms: 1.03x faster                                                                                                      |
| nbody          | 119 ms                                                                                                              | 199 ms: 1.67x slower                                                                                                      |
| float          | 99.0 ms                                                                                                             | 203 ms: 2.05x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.49x slower                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 32.7 ms                                                                                                             | 33.6 ms: 1.03x slower                                                                                                     |
| regex_compile  | 127 ms                                                                                                              | 224 ms: 1.76x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.17x slower                                                                                                              |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 154 ms                                                                                                              | 140 ms: 1.10x faster                                                                                                      |
| xml_etree_parse      | 197 ms                                                                                                              | 182 ms: 1.08x faster                                                                                                      |
| json_loads           | 32.2 us                                                                                                             | 37.9 us: 1.18x slower                                                                                                     |
| xml_etree_generate   | 117 ms                                                                                                              | 150 ms: 1.28x slower                                                                                                      |
| json_dumps           | 14.4 ms                                                                                                             | 19.3 ms: 1.34x slower                                                                                                     |
| xml_etree_process    | 83.6 ms                                                                                                             | 121 ms: 1.45x slower                                                                                                      |
| tomli_loads          | 2.74 sec                                                                                                            | 3.99 sec: 1.45x slower                                                                                                    |
| pickle_pure_python   | 411 us                                                                                                              | 735 us: 1.79x slower                                                                                                      |
| unpickle_pure_python | 265 us                                                                                                              | 518 us: 1.96x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.33x slower                                                                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.2 ms                                                                                                             | 21.4 ms: 1.32x slower                                                                                                     |
| python_startup_no_site | 9.05 ms                                                                                                             | 12.7 ms: 1.41x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.36x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 62.9 ms                                                                                                             | 89.7 ms: 1.43x slower                                                                                                     |
| genshi_text     | 29.2 ms                                                                                                             | 45.8 ms: 1.57x slower                                                                                                     |
| django_template | 40.6 ms                                                                                                             | 73.6 ms: 1.81x slower                                                                                                     |
| mako            | 14.3 ms                                                                                                             | 28.6 ms: 2.00x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.69x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                  | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 5.89 sec                                                                                                            | 65.5 ms: 89.90x faster                                                                                                    |
| gc_traversal               | 6.36 ms                                                                                                             | 5.10 ms: 1.25x faster                                                                                                     |
| create_gc_cycles           | 3.65 ms                                                                                                             | 2.94 ms: 1.24x faster                                                                                                     |
| xml_etree_iterparse        | 154 ms                                                                                                              | 140 ms: 1.10x faster                                                                                                      |
| xml_etree_parse            | 197 ms                                                                                                              | 182 ms: 1.08x faster                                                                                                      |
| pidigits                   | 240 ms                                                                                                              | 232 ms: 1.03x faster                                                                                                      |
| k_core                     | 3.55 sec                                                                                                            | 3.46 sec: 1.03x faster                                                                                                    |
| regex_v8                   | 32.7 ms                                                                                                             | 33.6 ms: 1.03x slower                                                                                                     |
| async_tree_io_tg           | 1.24 sec                                                                                                            | 1.38 sec: 1.11x slower                                                                                                    |
| pathlib                    | 23.0 ms                                                                                                             | 26.6 ms: 1.16x slower                                                                                                     |
| scimark_fft                | 459 ms                                                                                                              | 533 ms: 1.16x slower                                                                                                      |
| json_loads                 | 32.2 us                                                                                                             | 37.9 us: 1.18x slower                                                                                                     |
| async_tree_io              | 1.17 sec                                                                                                            | 1.39 sec: 1.19x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 760 ms                                                                                                              | 915 ms: 1.20x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 751 ms                                                                                                              | 928 ms: 1.24x slower                                                                                                      |
| json                       | 5.54 ms                                                                                                             | 6.87 ms: 1.24x slower                                                                                                     |
| spectral_norm              | 146 ms                                                                                                              | 181 ms: 1.25x slower                                                                                                      |
| mdp                        | 3.42 sec                                                                                                            | 4.26 sec: 1.25x slower                                                                                                    |
| docutils                   | 3.12 sec                                                                                                            | 3.94 sec: 1.26x slower                                                                                                    |
| async_tree_none_tg         | 476 ms                                                                                                              | 603 ms: 1.27x slower                                                                                                      |
| xml_etree_generate         | 117 ms                                                                                                              | 150 ms: 1.28x slower                                                                                                      |
| sphinx                     | 1.23 sec                                                                                                            | 1.58 sec: 1.29x slower                                                                                                    |
| connected_components       | 539 ms                                                                                                              | 700 ms: 1.30x slower                                                                                                      |
| scimark_sparse_mat_mult    | 6.75 ms                                                                                                             | 8.81 ms: 1.31x slower                                                                                                     |
| async_tree_memoization_tg  | 564 ms                                                                                                              | 738 ms: 1.31x slower                                                                                                      |
| async_generators           | 509 ms                                                                                                              | 670 ms: 1.32x slower                                                                                                      |
| shortest_path              | 562 ms                                                                                                              | 741 ms: 1.32x slower                                                                                                      |
| python_startup             | 16.2 ms                                                                                                             | 21.4 ms: 1.32x slower                                                                                                     |
| async_tree_memoization     | 573 ms                                                                                                              | 759 ms: 1.33x slower                                                                                                      |
| json_dumps                 | 14.4 ms                                                                                                             | 19.3 ms: 1.34x slower                                                                                                     |
| coroutines                 | 28.9 ms                                                                                                             | 39.3 ms: 1.36x slower                                                                                                     |
| deepcopy                   | 354 us                                                                                                              | 482 us: 1.36x slower                                                                                                      |
| coverage                   | 105 ms                                                                                                              | 145 ms: 1.38x slower                                                                                                      |
| nqueens                    | 107 ms                                                                                                              | 148 ms: 1.38x slower                                                                                                      |
| telco                      | 9.38 ms                                                                                                             | 13.0 ms: 1.38x slower                                                                                                     |
| async_tree_none            | 445 ms                                                                                                              | 618 ms: 1.39x slower                                                                                                      |
| meteor_contest             | 116 ms                                                                                                              | 161 ms: 1.39x slower                                                                                                      |
| python_startup_no_site     | 9.05 ms                                                                                                             | 12.7 ms: 1.41x slower                                                                                                     |
| genshi_xml                 | 62.9 ms                                                                                                             | 89.7 ms: 1.43x slower                                                                                                     |
| typing_runtime_protocols   | 206 us                                                                                                              | 296 us: 1.44x slower                                                                                                      |
| xml_etree_process          | 83.6 ms                                                                                                             | 121 ms: 1.45x slower                                                                                                      |
| tomli_loads                | 2.74 sec                                                                                                            | 3.99 sec: 1.45x slower                                                                                                    |
| dulwich_log                | 63.6 ms                                                                                                             | 92.8 ms: 1.46x slower                                                                                                     |
| sqlglot_normalize          | 138 ms                                                                                                              | 202 ms: 1.46x slower                                                                                                      |
| bpe_tokeniser              | 5.94 sec                                                                                                            | 8.72 sec: 1.47x slower                                                                                                    |
| fannkuch                   | 486 ms                                                                                                              | 746 ms: 1.53x slower                                                                                                      |
| deepcopy_memo              | 41.0 us                                                                                                             | 62.9 us: 1.53x slower                                                                                                     |
| bench_thread_pool          | 1.31 ms                                                                                                             | 2.01 ms: 1.54x slower                                                                                                     |
| sqlglot_optimize           | 63.0 ms                                                                                                             | 97.1 ms: 1.54x slower                                                                                                     |
| deepcopy_reduce            | 3.58 us                                                                                                             | 5.53 us: 1.54x slower                                                                                                     |
| many_optionals             | 719 us                                                                                                              | 1.12 ms: 1.56x slower                                                                                                     |
| pycparser                  | 1.28 sec                                                                                                            | 2.00 sec: 1.56x slower                                                                                                    |
| genshi_text                | 29.2 ms                                                                                                             | 45.8 ms: 1.57x slower                                                                                                     |
| pprint_pformat             | 1.96 sec                                                                                                            | 3.10 sec: 1.58x slower                                                                                                    |
| crypto_pyaes               | 84.5 ms                                                                                                             | 134 ms: 1.59x slower                                                                                                      |
| sympy_integrate            | 22.1 ms                                                                                                             | 35.1 ms: 1.59x slower                                                                                                     |
| pprint_safe_repr           | 947 ms                                                                                                              | 1.51 sec: 1.59x slower                                                                                                    |
| 2to3                       | 304 ms                                                                                                              | 494 ms: 1.63x slower                                                                                                      |
| subparsers                 | 26.7 ms                                                                                                             | 43.8 ms: 1.64x slower                                                                                                     |
| pylint                     | 297 ms                                                                                                              | 495 ms: 1.67x slower                                                                                                      |
| generators                 | 35.6 ms                                                                                                             | 59.5 ms: 1.67x slower                                                                                                     |
| nbody                      | 119 ms                                                                                                              | 199 ms: 1.67x slower                                                                                                      |
| pyflate                    | 601 ms                                                                                                              | 1.01 sec: 1.68x slower                                                                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                                                                             | 28.6 ms: 1.71x slower                                                                                                     |
| sympy_str                  | 283 ms                                                                                                              | 486 ms: 1.72x slower                                                                                                      |
| thrift                     | 968 us                                                                                                              | 1.70 ms: 1.75x slower                                                                                                     |
| regex_compile              | 127 ms                                                                                                              | 224 ms: 1.76x slower                                                                                                      |
| sqlalchemy_declarative     | 146 ms                                                                                                              | 259 ms: 1.77x slower                                                                                                      |
| pickle_pure_python         | 411 us                                                                                                              | 735 us: 1.79x slower                                                                                                      |
| html5lib                   | 65.0 ms                                                                                                             | 117 ms: 1.80x slower                                                                                                      |
| django_template            | 40.6 ms                                                                                                             | 73.6 ms: 1.81x slower                                                                                                     |
| scimark_monte_carlo        | 92.9 ms                                                                                                             | 170 ms: 1.83x slower                                                                                                      |
| sympy_expand               | 480 ms                                                                                                              | 895 ms: 1.86x slower                                                                                                      |
| comprehensions             | 21.8 us                                                                                                             | 41.3 us: 1.89x slower                                                                                                     |
| sympy_sum                  | 153 ms                                                                                                              | 292 ms: 1.91x slower                                                                                                      |
| scimark_sor                | 165 ms                                                                                                              | 316 ms: 1.91x slower                                                                                                      |
| logging_simple             | 6.99 us                                                                                                             | 13.6 us: 1.94x slower                                                                                                     |
| unpickle_pure_python       | 265 us                                                                                                              | 518 us: 1.96x slower                                                                                                      |
| logging_format             | 7.78 us                                                                                                             | 15.3 us: 1.96x slower                                                                                                     |
| mako                       | 14.3 ms                                                                                                             | 28.6 ms: 2.00x slower                                                                                                     |
| hexiom                     | 7.34 ms                                                                                                             | 14.7 ms: 2.00x slower                                                                                                     |
| float                      | 99.0 ms                                                                                                             | 203 ms: 2.05x slower                                                                                                      |
| logging_silent             | 143 ns                                                                                                              | 293 ns: 2.06x slower                                                                                                      |
| scimark_lu                 | 138 ms                                                                                                              | 287 ms: 2.07x slower                                                                                                      |
| richards                   | 56.4 ms                                                                                                             | 119 ms: 2.11x slower                                                                                                      |
| richards_super             | 62.3 ms                                                                                                             | 136 ms: 2.19x slower                                                                                                      |
| chaos                      | 72.0 ms                                                                                                             | 158 ms: 2.19x slower                                                                                                      |
| sqlglot_transpile          | 1.84 ms                                                                                                             | 4.20 ms: 2.28x slower                                                                                                     |
| sqlglot_parse              | 1.47 ms                                                                                                             | 3.52 ms: 2.39x slower                                                                                                     |
| raytrace                   | 323 ms                                                                                                              | 811 ms: 2.51x slower                                                                                                      |
| go                         | 142 ms                                                                                                              | 387 ms: 2.73x slower                                                                                                      |
| deltablue                  | 4.09 ms                                                                                                             | 12.3 ms: 3.01x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.42x slower                                                                                                              |

Benchmark hidden because not significant (4): sqlite_synth, regex_dna, asyncio_websockets, regex_effbot
Ignored benchmarks (1) of results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: djangocms

- Geometric mean (including insignificant results): 1.329x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.37x
- 95% likely to have a slowdown of 1.35x
- 99% likely to have a slowdown of 1.31x

# Memory
- memory change: 1.19x