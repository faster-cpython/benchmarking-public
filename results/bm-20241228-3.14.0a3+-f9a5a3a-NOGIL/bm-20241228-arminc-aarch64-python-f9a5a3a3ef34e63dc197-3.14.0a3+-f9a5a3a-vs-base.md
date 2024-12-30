# Results vs. base

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-aarch64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.278x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x slower
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-NOGIL/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                                                              | 471 ms: 1.53x slower                                                                                                      |
| docutils       | 3.04 sec                                                                                                            | 3.71 sec: 1.22x slower                                                                                                    |
| html5lib       | 65.4 ms                                                                                                             | 110 ms: 1.68x slower                                                                                                      |
| sphinx         | 1.18 sec                                                                                                            | 1.51 sec: 1.28x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.42x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-NOGIL/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 29.1 ms                                                                                                             | 34.4 ms: 1.18x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 679 ms                                                                                                              | 825 ms: 1.22x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 694 ms                                                                                                              | 850 ms: 1.23x slower                                                                                                      |
| async_generators           | 488 ms                                                                                                              | 621 ms: 1.27x slower                                                                                                      |
| async_tree_memoization     | 519 ms                                                                                                              | 667 ms: 1.29x slower                                                                                                      |
| async_tree_io              | 929 ms                                                                                                              | 1.21 sec: 1.30x slower                                                                                                    |
| async_tree_io_tg           | 910 ms                                                                                                              | 1.18 sec: 1.30x slower                                                                                                    |
| async_tree_memoization_tg  | 486 ms                                                                                                              | 635 ms: 1.31x slower                                                                                                      |
| async_tree_none_tg         | 391 ms                                                                                                              | 519 ms: 1.33x slower                                                                                                      |
| async_tree_none            | 407 ms                                                                                                              | 543 ms: 1.34x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.25x slower                                                                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-NOGIL/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 126 ms                                                                                                              | 191 ms: 1.51x slower                                                                                                      |
| float          | 95.0 ms                                                                                                             | 162 ms: 1.71x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.36x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-NOGIL/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                                                                              | 267 ms: 1.08x slower                                                                                                      |
| regex_compile  | 131 ms                                                                                                              | 195 ms: 1.49x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.13x slower                                                                                                              |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-NOGIL/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| json_loads           | 33.4 us                                                                                                             | 37.3 us: 1.12x slower                                                                                                     |
| xml_etree_generate   | 116 ms                                                                                                              | 143 ms: 1.23x slower                                                                                                      |
| json_dumps           | 14.9 ms                                                                                                             | 18.6 ms: 1.25x slower                                                                                                     |
| xml_etree_process    | 83.5 ms                                                                                                             | 111 ms: 1.33x slower                                                                                                      |
| tomli_loads          | 2.61 sec                                                                                                            | 3.58 sec: 1.38x slower                                                                                                    |
| unpickle_pure_python | 274 us                                                                                                              | 467 us: 1.70x slower                                                                                                      |
| pickle_pure_python   | 395 us                                                                                                              | 701 us: 1.77x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.28x slower                                                                                                              |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-NOGIL/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.4 ms                                                                                                             | 20.6 ms: 1.26x slower                                                                                                     |
| python_startup_no_site | 9.03 ms                                                                                                             | 12.4 ms: 1.37x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.31x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-NOGIL/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 64.5 ms                                                                                                             | 85.3 ms: 1.32x slower                                                                                                     |
| genshi_text     | 27.7 ms                                                                                                             | 40.4 ms: 1.46x slower                                                                                                     |
| django_template | 40.5 ms                                                                                                             | 65.9 ms: 1.63x slower                                                                                                     |
| mako            | 14.4 ms                                                                                                             | 25.2 ms: 1.76x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.53x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                  | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-NOGIL/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 6.30 sec                                                                                                            | 63.2 ms: 99.71x faster                                                                                                    |
| gc_traversal               | 6.90 ms                                                                                                             | 5.02 ms: 1.38x faster                                                                                                     |
| create_gc_cycles           | 3.57 ms                                                                                                             | 2.92 ms: 1.22x faster                                                                                                     |
| sqlite_synth               | 4.08 us                                                                                                             | 3.80 us: 1.07x faster                                                                                                     |
| regex_dna                  | 247 ms                                                                                                              | 267 ms: 1.08x slower                                                                                                      |
| json_loads                 | 33.4 us                                                                                                             | 37.3 us: 1.12x slower                                                                                                     |
| json                       | 5.66 ms                                                                                                             | 6.37 ms: 1.13x slower                                                                                                     |
| pathlib                    | 22.3 ms                                                                                                             | 25.3 ms: 1.13x slower                                                                                                     |
| k_core                     | 2.86 sec                                                                                                            | 3.30 sec: 1.15x slower                                                                                                    |
| coroutines                 | 29.1 ms                                                                                                             | 34.4 ms: 1.18x slower                                                                                                     |
| scimark_fft                | 429 ms                                                                                                              | 509 ms: 1.19x slower                                                                                                      |
| mdp                        | 3.41 sec                                                                                                            | 4.05 sec: 1.19x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 679 ms                                                                                                              | 825 ms: 1.22x slower                                                                                                      |
| docutils                   | 3.04 sec                                                                                                            | 3.71 sec: 1.22x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 694 ms                                                                                                              | 850 ms: 1.23x slower                                                                                                      |
| xml_etree_generate         | 116 ms                                                                                                              | 143 ms: 1.23x slower                                                                                                      |
| spectral_norm              | 133 ms                                                                                                              | 165 ms: 1.24x slower                                                                                                      |
| connected_components       | 552 ms                                                                                                              | 685 ms: 1.24x slower                                                                                                      |
| shortest_path              | 569 ms                                                                                                              | 708 ms: 1.24x slower                                                                                                      |
| json_dumps                 | 14.9 ms                                                                                                             | 18.6 ms: 1.25x slower                                                                                                     |
| python_startup             | 16.4 ms                                                                                                             | 20.6 ms: 1.26x slower                                                                                                     |
| deepcopy                   | 344 us                                                                                                              | 437 us: 1.27x slower                                                                                                      |
| async_generators           | 488 ms                                                                                                              | 621 ms: 1.27x slower                                                                                                      |
| sphinx                     | 1.18 sec                                                                                                            | 1.51 sec: 1.28x slower                                                                                                    |
| telco                      | 9.65 ms                                                                                                             | 12.4 ms: 1.28x slower                                                                                                     |
| async_tree_memoization     | 519 ms                                                                                                              | 667 ms: 1.29x slower                                                                                                      |
| dulwich_log                | 63.9 ms                                                                                                             | 82.8 ms: 1.30x slower                                                                                                     |
| async_tree_io              | 929 ms                                                                                                              | 1.21 sec: 1.30x slower                                                                                                    |
| async_tree_io_tg           | 910 ms                                                                                                              | 1.18 sec: 1.30x slower                                                                                                    |
| async_tree_memoization_tg  | 486 ms                                                                                                              | 635 ms: 1.31x slower                                                                                                      |
| nqueens                    | 105 ms                                                                                                              | 138 ms: 1.32x slower                                                                                                      |
| genshi_xml                 | 64.5 ms                                                                                                             | 85.3 ms: 1.32x slower                                                                                                     |
| pycparser                  | 1.29 sec                                                                                                            | 1.71 sec: 1.33x slower                                                                                                    |
| async_tree_none_tg         | 391 ms                                                                                                              | 519 ms: 1.33x slower                                                                                                      |
| deepcopy_reduce            | 3.67 us                                                                                                             | 4.87 us: 1.33x slower                                                                                                     |
| xml_etree_process          | 83.5 ms                                                                                                             | 111 ms: 1.33x slower                                                                                                      |
| sqlglot_normalize          | 131 ms                                                                                                              | 176 ms: 1.34x slower                                                                                                      |
| async_tree_none            | 407 ms                                                                                                              | 543 ms: 1.34x slower                                                                                                      |
| sqlglot_optimize           | 64.4 ms                                                                                                             | 86.3 ms: 1.34x slower                                                                                                     |
| scimark_sparse_mat_mult    | 6.16 ms                                                                                                             | 8.32 ms: 1.35x slower                                                                                                     |
| python_startup_no_site     | 9.03 ms                                                                                                             | 12.4 ms: 1.37x slower                                                                                                     |
| pylint                     | 325 ms                                                                                                              | 446 ms: 1.37x slower                                                                                                      |
| tomli_loads                | 2.61 sec                                                                                                            | 3.58 sec: 1.38x slower                                                                                                    |
| sympy_integrate            | 22.2 ms                                                                                                             | 30.5 ms: 1.38x slower                                                                                                     |
| bpe_tokeniser              | 5.79 sec                                                                                                            | 7.99 sec: 1.38x slower                                                                                                    |
| deepcopy_memo              | 41.1 us                                                                                                             | 57.4 us: 1.40x slower                                                                                                     |
| meteor_contest             | 117 ms                                                                                                              | 163 ms: 1.40x slower                                                                                                      |
| many_optionals             | 724 us                                                                                                              | 1.01 ms: 1.40x slower                                                                                                     |
| sympy_sum                  | 146 ms                                                                                                              | 206 ms: 1.41x slower                                                                                                      |
| pprint_safe_repr           | 996 ms                                                                                                              | 1.40 sec: 1.41x slower                                                                                                    |
| coverage                   | 102 ms                                                                                                              | 143 ms: 1.41x slower                                                                                                      |
| subparsers                 | 26.8 ms                                                                                                             | 38.0 ms: 1.42x slower                                                                                                     |
| pprint_pformat             | 2.03 sec                                                                                                            | 2.89 sec: 1.42x slower                                                                                                    |
| sympy_expand               | 482 ms                                                                                                              | 687 ms: 1.42x slower                                                                                                      |
| thrift                     | 983 us                                                                                                              | 1.41 ms: 1.43x slower                                                                                                     |
| typing_runtime_protocols   | 202 us                                                                                                              | 290 us: 1.44x slower                                                                                                      |
| crypto_pyaes               | 85.2 ms                                                                                                             | 122 ms: 1.44x slower                                                                                                      |
| sympy_str                  | 277 ms                                                                                                              | 400 ms: 1.44x slower                                                                                                      |
| mypy2                      | 1.06 sec                                                                                                            | 1.53 sec: 1.45x slower                                                                                                    |
| genshi_text                | 27.7 ms                                                                                                             | 40.4 ms: 1.46x slower                                                                                                     |
| fannkuch                   | 480 ms                                                                                                              | 703 ms: 1.46x slower                                                                                                      |
| regex_compile              | 131 ms                                                                                                              | 195 ms: 1.49x slower                                                                                                      |
| nbody                      | 126 ms                                                                                                              | 191 ms: 1.51x slower                                                                                                      |
| bench_thread_pool          | 1.33 ms                                                                                                             | 2.02 ms: 1.52x slower                                                                                                     |
| 2to3                       | 308 ms                                                                                                              | 471 ms: 1.53x slower                                                                                                      |
| pyflate                    | 592 ms                                                                                                              | 921 ms: 1.55x slower                                                                                                      |
| logging_simple             | 7.22 us                                                                                                             | 11.3 us: 1.56x slower                                                                                                     |
| logging_format             | 7.89 us                                                                                                             | 12.3 us: 1.56x slower                                                                                                     |
| generators                 | 36.6 ms                                                                                                             | 57.3 ms: 1.57x slower                                                                                                     |
| sqlalchemy_declarative     | 148 ms                                                                                                              | 235 ms: 1.58x slower                                                                                                      |
| scimark_lu                 | 139 ms                                                                                                              | 220 ms: 1.59x slower                                                                                                      |
| django_template            | 40.5 ms                                                                                                             | 65.9 ms: 1.63x slower                                                                                                     |
| sqlalchemy_imperative      | 15.9 ms                                                                                                             | 26.7 ms: 1.68x slower                                                                                                     |
| html5lib                   | 65.4 ms                                                                                                             | 110 ms: 1.68x slower                                                                                                      |
| unpickle_pure_python       | 274 us                                                                                                              | 467 us: 1.70x slower                                                                                                      |
| float                      | 95.0 ms                                                                                                             | 162 ms: 1.71x slower                                                                                                      |
| mako                       | 14.4 ms                                                                                                             | 25.2 ms: 1.76x slower                                                                                                     |
| hexiom                     | 7.57 ms                                                                                                             | 13.4 ms: 1.77x slower                                                                                                     |
| pickle_pure_python         | 395 us                                                                                                              | 701 us: 1.77x slower                                                                                                      |
| chaos                      | 72.8 ms                                                                                                             | 129 ms: 1.78x slower                                                                                                      |
| richards_super             | 60.6 ms                                                                                                             | 109 ms: 1.79x slower                                                                                                      |
| comprehensions             | 22.4 us                                                                                                             | 40.3 us: 1.80x slower                                                                                                     |
| scimark_monte_carlo        | 85.1 ms                                                                                                             | 155 ms: 1.82x slower                                                                                                      |
| scimark_sor                | 157 ms                                                                                                              | 288 ms: 1.83x slower                                                                                                      |
| richards                   | 52.6 ms                                                                                                             | 98.2 ms: 1.87x slower                                                                                                     |
| sqlglot_transpile          | 1.86 ms                                                                                                             | 3.49 ms: 1.87x slower                                                                                                     |
| logging_silent             | 141 ns                                                                                                              | 265 ns: 1.89x slower                                                                                                      |
| raytrace                   | 321 ms                                                                                                              | 664 ms: 2.07x slower                                                                                                      |
| sqlglot_parse              | 1.48 ms                                                                                                             | 3.11 ms: 2.10x slower                                                                                                     |
| go                         | 145 ms                                                                                                              | 341 ms: 2.35x slower                                                                                                      |
| deltablue                  | 3.98 ms                                                                                                             | 11.1 ms: 2.80x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.32x slower                                                                                                              |

Benchmark hidden because not significant (6): xml_etree_parse, pidigits, xml_etree_iterparse, regex_v8, asyncio_websockets, regex_effbot
Ignored benchmarks (1) of results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: djangocms

- Geometric mean (including insignificant results): 1.278x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.31x
- 95% likely to have a slowdown of 1.30x
- 99% likely to have a slowdown of 1.29x

# Memory
- memory change: 1.18x