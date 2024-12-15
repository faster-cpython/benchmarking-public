# Results vs. base

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-aarch64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.309x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                                                              | 472 ms: 1.54x slower                                                                                                      |
| docutils       | 3.05 sec                                                                                                            | 3.83 sec: 1.26x slower                                                                                                    |
| html5lib       | 64.6 ms                                                                                                             | 117 ms: 1.81x slower                                                                                                      |
| sphinx         | 1.19 sec                                                                                                            | 1.51 sec: 1.27x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.45x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 29.2 ms                                                                                                             | 33.8 ms: 1.16x slower                                                                                                     |
| async_generators           | 501 ms                                                                                                              | 635 ms: 1.27x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 671 ms                                                                                                              | 869 ms: 1.29x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 686 ms                                                                                                              | 895 ms: 1.30x slower                                                                                                      |
| async_tree_io              | 922 ms                                                                                                              | 1.30 sec: 1.41x slower                                                                                                    |
| async_tree_io_tg           | 904 ms                                                                                                              | 1.29 sec: 1.42x slower                                                                                                    |
| async_tree_memoization_tg  | 481 ms                                                                                                              | 687 ms: 1.43x slower                                                                                                      |
| async_tree_memoization     | 512 ms                                                                                                              | 735 ms: 1.44x slower                                                                                                      |
| async_tree_none            | 401 ms                                                                                                              | 587 ms: 1.46x slower                                                                                                      |
| async_tree_none_tg         | 390 ms                                                                                                              | 575 ms: 1.48x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.33x slower                                                                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 121 ms                                                                                                              | 193 ms: 1.59x slower                                                                                                      |
| float          | 97.1 ms                                                                                                             | 194 ms: 2.00x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.46x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 32.3 ms                                                                                                             | 33.9 ms: 1.05x slower                                                                                                     |
| regex_compile  | 131 ms                                                                                                              | 201 ms: 1.53x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.15x slower                                                                                                              |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| json_loads           | 32.5 us                                                                                                             | 36.8 us: 1.13x slower                                                                                                     |
| xml_etree_generate   | 115 ms                                                                                                              | 144 ms: 1.26x slower                                                                                                      |
| json_dumps           | 14.8 ms                                                                                                             | 18.8 ms: 1.27x slower                                                                                                     |
| tomli_loads          | 2.70 sec                                                                                                            | 3.59 sec: 1.33x slower                                                                                                    |
| xml_etree_process    | 80.5 ms                                                                                                             | 113 ms: 1.41x slower                                                                                                      |
| unpickle_pure_python | 266 us                                                                                                              | 460 us: 1.73x slower                                                                                                      |
| pickle_pure_python   | 400 us                                                                                                              | 702 us: 1.75x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.29x slower                                                                                                              |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.3 ms                                                                                                             | 21.5 ms: 1.31x slower                                                                                                     |
| python_startup_no_site | 9.05 ms                                                                                                             | 12.7 ms: 1.40x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.36x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 62.2 ms                                                                                                             | 85.6 ms: 1.38x slower                                                                                                     |
| genshi_text     | 28.1 ms                                                                                                             | 42.4 ms: 1.51x slower                                                                                                     |
| django_template | 42.7 ms                                                                                                             | 66.9 ms: 1.57x slower                                                                                                     |
| mako            | 14.3 ms                                                                                                             | 25.7 ms: 1.80x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.56x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                  | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 6.14 sec                                                                                                            | 62.8 ms: 97.80x faster                                                                                                    |
| gc_traversal               | 6.95 ms                                                                                                             | 5.03 ms: 1.38x faster                                                                                                     |
| create_gc_cycles           | 3.72 ms                                                                                                             | 2.95 ms: 1.26x faster                                                                                                     |
| regex_v8                   | 32.3 ms                                                                                                             | 33.9 ms: 1.05x slower                                                                                                     |
| json_loads                 | 32.5 us                                                                                                             | 36.8 us: 1.13x slower                                                                                                     |
| pathlib                    | 21.8 ms                                                                                                             | 24.8 ms: 1.14x slower                                                                                                     |
| k_core                     | 2.86 sec                                                                                                            | 3.27 sec: 1.14x slower                                                                                                    |
| coroutines                 | 29.2 ms                                                                                                             | 33.8 ms: 1.16x slower                                                                                                     |
| json                       | 5.61 ms                                                                                                             | 6.57 ms: 1.17x slower                                                                                                     |
| scimark_fft                | 419 ms                                                                                                              | 507 ms: 1.21x slower                                                                                                      |
| mdp                        | 3.38 sec                                                                                                            | 4.09 sec: 1.21x slower                                                                                                    |
| spectral_norm              | 130 ms                                                                                                              | 160 ms: 1.23x slower                                                                                                      |
| telco                      | 9.73 ms                                                                                                             | 12.1 ms: 1.24x slower                                                                                                     |
| xml_etree_generate         | 115 ms                                                                                                              | 144 ms: 1.26x slower                                                                                                      |
| docutils                   | 3.05 sec                                                                                                            | 3.83 sec: 1.26x slower                                                                                                    |
| deepcopy                   | 353 us                                                                                                              | 444 us: 1.26x slower                                                                                                      |
| async_generators           | 501 ms                                                                                                              | 635 ms: 1.27x slower                                                                                                      |
| sphinx                     | 1.19 sec                                                                                                            | 1.51 sec: 1.27x slower                                                                                                    |
| json_dumps                 | 14.8 ms                                                                                                             | 18.8 ms: 1.27x slower                                                                                                     |
| connected_components       | 536 ms                                                                                                              | 685 ms: 1.28x slower                                                                                                      |
| shortest_path              | 566 ms                                                                                                              | 723 ms: 1.28x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 671 ms                                                                                                              | 869 ms: 1.29x slower                                                                                                      |
| scimark_sparse_mat_mult    | 6.28 ms                                                                                                             | 8.17 ms: 1.30x slower                                                                                                     |
| async_tree_cpu_io_mixed    | 686 ms                                                                                                              | 895 ms: 1.30x slower                                                                                                      |
| python_startup             | 16.3 ms                                                                                                             | 21.5 ms: 1.31x slower                                                                                                     |
| nqueens                    | 103 ms                                                                                                              | 137 ms: 1.33x slower                                                                                                      |
| tomli_loads                | 2.70 sec                                                                                                            | 3.59 sec: 1.33x slower                                                                                                    |
| meteor_contest             | 118 ms                                                                                                              | 158 ms: 1.34x slower                                                                                                      |
| deepcopy_reduce            | 3.65 us                                                                                                             | 4.94 us: 1.35x slower                                                                                                     |
| genshi_xml                 | 62.2 ms                                                                                                             | 85.6 ms: 1.38x slower                                                                                                     |
| sqlglot_optimize           | 64.6 ms                                                                                                             | 89.1 ms: 1.38x slower                                                                                                     |
| pprint_safe_repr           | 997 ms                                                                                                              | 1.38 sec: 1.38x slower                                                                                                    |
| deepcopy_memo              | 42.7 us                                                                                                             | 59.2 us: 1.38x slower                                                                                                     |
| pprint_pformat             | 2.05 sec                                                                                                            | 2.84 sec: 1.39x slower                                                                                                    |
| bpe_tokeniser              | 5.74 sec                                                                                                            | 8.01 sec: 1.40x slower                                                                                                    |
| python_startup_no_site     | 9.05 ms                                                                                                             | 12.7 ms: 1.40x slower                                                                                                     |
| async_tree_io              | 922 ms                                                                                                              | 1.30 sec: 1.41x slower                                                                                                    |
| xml_etree_process          | 80.5 ms                                                                                                             | 113 ms: 1.41x slower                                                                                                      |
| async_tree_io_tg           | 904 ms                                                                                                              | 1.29 sec: 1.42x slower                                                                                                    |
| sqlglot_normalize          | 132 ms                                                                                                              | 189 ms: 1.43x slower                                                                                                      |
| async_tree_memoization_tg  | 481 ms                                                                                                              | 687 ms: 1.43x slower                                                                                                      |
| async_tree_memoization     | 512 ms                                                                                                              | 735 ms: 1.44x slower                                                                                                      |
| crypto_pyaes               | 85.2 ms                                                                                                             | 123 ms: 1.44x slower                                                                                                      |
| many_optionals             | 715 us                                                                                                              | 1.04 ms: 1.46x slower                                                                                                     |
| typing_runtime_protocols   | 209 us                                                                                                              | 305 us: 1.46x slower                                                                                                      |
| dulwich_log                | 62.3 ms                                                                                                             | 91.1 ms: 1.46x slower                                                                                                     |
| async_tree_none            | 401 ms                                                                                                              | 587 ms: 1.46x slower                                                                                                      |
| fannkuch                   | 477 ms                                                                                                              | 698 ms: 1.46x slower                                                                                                      |
| async_tree_none_tg         | 390 ms                                                                                                              | 575 ms: 1.48x slower                                                                                                      |
| sympy_integrate            | 22.2 ms                                                                                                             | 33.2 ms: 1.50x slower                                                                                                     |
| bench_thread_pool          | 1.35 ms                                                                                                             | 2.03 ms: 1.50x slower                                                                                                     |
| genshi_text                | 28.1 ms                                                                                                             | 42.4 ms: 1.51x slower                                                                                                     |
| coverage                   | 97.7 ms                                                                                                             | 147 ms: 1.51x slower                                                                                                      |
| pylint                     | 306 ms                                                                                                              | 463 ms: 1.52x slower                                                                                                      |
| regex_compile              | 131 ms                                                                                                              | 201 ms: 1.53x slower                                                                                                      |
| 2to3                       | 306 ms                                                                                                              | 472 ms: 1.54x slower                                                                                                      |
| pycparser                  | 1.26 sec                                                                                                            | 1.95 sec: 1.54x slower                                                                                                    |
| generators                 | 36.6 ms                                                                                                             | 56.6 ms: 1.55x slower                                                                                                     |
| logging_simple             | 7.65 us                                                                                                             | 12.0 us: 1.57x slower                                                                                                     |
| django_template            | 42.7 ms                                                                                                             | 66.9 ms: 1.57x slower                                                                                                     |
| mypy2                      | 1.05 sec                                                                                                            | 1.65 sec: 1.57x slower                                                                                                    |
| subparsers                 | 25.8 ms                                                                                                             | 40.9 ms: 1.58x slower                                                                                                     |
| nbody                      | 121 ms                                                                                                              | 193 ms: 1.59x slower                                                                                                      |
| pyflate                    | 561 ms                                                                                                              | 925 ms: 1.65x slower                                                                                                      |
| thrift                     | 967 us                                                                                                              | 1.61 ms: 1.66x slower                                                                                                     |
| logging_format             | 8.02 us                                                                                                             | 13.3 us: 1.66x slower                                                                                                     |
| sympy_str                  | 278 ms                                                                                                              | 465 ms: 1.67x slower                                                                                                      |
| sqlalchemy_declarative     | 145 ms                                                                                                              | 248 ms: 1.71x slower                                                                                                      |
| unpickle_pure_python       | 266 us                                                                                                              | 460 us: 1.73x slower                                                                                                      |
| pickle_pure_python         | 400 us                                                                                                              | 702 us: 1.75x slower                                                                                                      |
| mako                       | 14.3 ms                                                                                                             | 25.7 ms: 1.80x slower                                                                                                     |
| sympy_expand               | 484 ms                                                                                                              | 873 ms: 1.81x slower                                                                                                      |
| html5lib                   | 64.6 ms                                                                                                             | 117 ms: 1.81x slower                                                                                                      |
| hexiom                     | 7.45 ms                                                                                                             | 13.7 ms: 1.83x slower                                                                                                     |
| sqlalchemy_imperative      | 15.5 ms                                                                                                             | 28.4 ms: 1.83x slower                                                                                                     |
| comprehensions             | 21.2 us                                                                                                             | 38.9 us: 1.83x slower                                                                                                     |
| logging_silent             | 142 ns                                                                                                              | 270 ns: 1.91x slower                                                                                                      |
| chaos                      | 73.7 ms                                                                                                             | 142 ms: 1.92x slower                                                                                                      |
| scimark_monte_carlo        | 86.5 ms                                                                                                             | 166 ms: 1.92x slower                                                                                                      |
| scimark_lu                 | 139 ms                                                                                                              | 268 ms: 1.93x slower                                                                                                      |
| scimark_sor                | 161 ms                                                                                                              | 313 ms: 1.95x slower                                                                                                      |
| richards_super             | 61.7 ms                                                                                                             | 121 ms: 1.95x slower                                                                                                      |
| float                      | 97.1 ms                                                                                                             | 194 ms: 2.00x slower                                                                                                      |
| sympy_sum                  | 145 ms                                                                                                              | 293 ms: 2.02x slower                                                                                                      |
| richards                   | 55.9 ms                                                                                                             | 115 ms: 2.06x slower                                                                                                      |
| sqlglot_transpile          | 1.87 ms                                                                                                             | 3.97 ms: 2.13x slower                                                                                                     |
| sqlglot_parse              | 1.50 ms                                                                                                             | 3.34 ms: 2.23x slower                                                                                                     |
| raytrace                   | 324 ms                                                                                                              | 739 ms: 2.28x slower                                                                                                      |
| go                         | 144 ms                                                                                                              | 378 ms: 2.62x slower                                                                                                      |
| deltablue                  | 4.01 ms                                                                                                             | 12.2 ms: 3.05x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.38x slower                                                                                                              |

Benchmark hidden because not significant (7): sqlite_synth, xml_etree_iterparse, pidigits, xml_etree_parse, regex_dna, asyncio_websockets, regex_effbot
Ignored benchmarks (1) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: djangocms

- Geometric mean (including insignificant results): 1.309x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.38x
- 95% likely to have a slowdown of 1.37x
- 99% likely to have a slowdown of 1.35x

# Memory
- memory change: 1.19x