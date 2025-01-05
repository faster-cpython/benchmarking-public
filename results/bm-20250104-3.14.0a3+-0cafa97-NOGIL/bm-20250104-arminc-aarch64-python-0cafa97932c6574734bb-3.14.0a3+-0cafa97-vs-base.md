# Results vs. base

- fork: python
- ref: 0cafa97932c6574734bb
- machine: linux-aarch64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.272x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-NOGIL/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 307 ms                                                                                                              | 468 ms: 1.53x slower                                                                                                      |
| docutils       | 3.03 sec                                                                                                            | 3.72 sec: 1.23x slower                                                                                                    |
| html5lib       | 63.8 ms                                                                                                             | 111 ms: 1.74x slower                                                                                                      |
| sphinx         | 1.20 sec                                                                                                            | 1.49 sec: 1.25x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.42x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-NOGIL/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 29.2 ms                                                                                                             | 33.8 ms: 1.16x slower                                                                                                     |
| async_tree_cpu_io_mixed    | 687 ms                                                                                                              | 833 ms: 1.21x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 669 ms                                                                                                              | 814 ms: 1.22x slower                                                                                                      |
| async_generators           | 486 ms                                                                                                              | 619 ms: 1.27x slower                                                                                                      |
| async_tree_io              | 928 ms                                                                                                              | 1.18 sec: 1.28x slower                                                                                                    |
| async_tree_memoization     | 508 ms                                                                                                              | 660 ms: 1.30x slower                                                                                                      |
| async_tree_io_tg           | 896 ms                                                                                                              | 1.17 sec: 1.31x slower                                                                                                    |
| async_tree_memoization_tg  | 479 ms                                                                                                              | 628 ms: 1.31x slower                                                                                                      |
| async_tree_none_tg         | 382 ms                                                                                                              | 510 ms: 1.33x slower                                                                                                      |
| async_tree_none            | 395 ms                                                                                                              | 536 ms: 1.35x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.25x slower                                                                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-NOGIL/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 125 ms                                                                                                              | 186 ms: 1.49x slower                                                                                                      |
| float          | 91.8 ms                                                                                                             | 154 ms: 1.67x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.37x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-NOGIL/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                                                              | 187 ms: 1.44x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.12x slower                                                                                                              |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-NOGIL/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 148 ms                                                                                                              | 137 ms: 1.08x faster                                                                                                      |
| json_loads           | 32.5 us                                                                                                             | 37.4 us: 1.15x slower                                                                                                     |
| xml_etree_generate   | 123 ms                                                                                                              | 145 ms: 1.17x slower                                                                                                      |
| json_dumps           | 14.5 ms                                                                                                             | 18.4 ms: 1.26x slower                                                                                                     |
| xml_etree_process    | 85.7 ms                                                                                                             | 109 ms: 1.28x slower                                                                                                      |
| tomli_loads          | 2.64 sec                                                                                                            | 3.60 sec: 1.36x slower                                                                                                    |
| unpickle_pure_python | 270 us                                                                                                              | 453 us: 1.68x slower                                                                                                      |
| pickle_pure_python   | 401 us                                                                                                              | 701 us: 1.75x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.26x slower                                                                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-NOGIL/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.2 ms                                                                                                             | 20.4 ms: 1.26x slower                                                                                                     |
| python_startup_no_site | 9.05 ms                                                                                                             | 12.4 ms: 1.37x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.31x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-NOGIL/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 63.7 ms                                                                                                             | 86.6 ms: 1.36x slower                                                                                                     |
| genshi_text     | 29.4 ms                                                                                                             | 41.3 ms: 1.40x slower                                                                                                     |
| django_template | 41.4 ms                                                                                                             | 65.3 ms: 1.58x slower                                                                                                     |
| mako            | 14.2 ms                                                                                                             | 25.6 ms: 1.80x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.53x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                  | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-NOGIL/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 4.34 sec                                                                                                            | 62.6 ms: 69.29x faster                                                                                                    |
| gc_traversal               | 6.83 ms                                                                                                             | 5.03 ms: 1.36x faster                                                                                                     |
| create_gc_cycles           | 3.61 ms                                                                                                             | 2.87 ms: 1.26x faster                                                                                                     |
| xml_etree_iterparse        | 148 ms                                                                                                              | 137 ms: 1.08x faster                                                                                                      |
| pathlib                    | 21.7 ms                                                                                                             | 23.9 ms: 1.10x slower                                                                                                     |
| k_core                     | 2.93 sec                                                                                                            | 3.30 sec: 1.13x slower                                                                                                    |
| json                       | 5.71 ms                                                                                                             | 6.54 ms: 1.15x slower                                                                                                     |
| json_loads                 | 32.5 us                                                                                                             | 37.4 us: 1.15x slower                                                                                                     |
| coroutines                 | 29.2 ms                                                                                                             | 33.8 ms: 1.16x slower                                                                                                     |
| mdp                        | 3.45 sec                                                                                                            | 4.01 sec: 1.16x slower                                                                                                    |
| spectral_norm              | 132 ms                                                                                                              | 154 ms: 1.17x slower                                                                                                      |
| scimark_fft                | 427 ms                                                                                                              | 501 ms: 1.17x slower                                                                                                      |
| xml_etree_generate         | 123 ms                                                                                                              | 145 ms: 1.17x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 687 ms                                                                                                              | 833 ms: 1.21x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 669 ms                                                                                                              | 814 ms: 1.22x slower                                                                                                      |
| docutils                   | 3.03 sec                                                                                                            | 3.72 sec: 1.23x slower                                                                                                    |
| connected_components       | 550 ms                                                                                                              | 676 ms: 1.23x slower                                                                                                      |
| shortest_path              | 571 ms                                                                                                              | 707 ms: 1.24x slower                                                                                                      |
| sphinx                     | 1.20 sec                                                                                                            | 1.49 sec: 1.25x slower                                                                                                    |
| python_startup             | 16.2 ms                                                                                                             | 20.4 ms: 1.26x slower                                                                                                     |
| json_dumps                 | 14.5 ms                                                                                                             | 18.4 ms: 1.26x slower                                                                                                     |
| deepcopy                   | 342 us                                                                                                              | 432 us: 1.26x slower                                                                                                      |
| async_generators           | 486 ms                                                                                                              | 619 ms: 1.27x slower                                                                                                      |
| async_tree_io              | 928 ms                                                                                                              | 1.18 sec: 1.28x slower                                                                                                    |
| xml_etree_process          | 85.7 ms                                                                                                             | 109 ms: 1.28x slower                                                                                                      |
| sqlglot_optimize           | 66.7 ms                                                                                                             | 86.0 ms: 1.29x slower                                                                                                     |
| async_tree_memoization     | 508 ms                                                                                                              | 660 ms: 1.30x slower                                                                                                      |
| telco                      | 9.48 ms                                                                                                             | 12.4 ms: 1.30x slower                                                                                                     |
| nqueens                    | 105 ms                                                                                                              | 136 ms: 1.30x slower                                                                                                      |
| async_tree_io_tg           | 896 ms                                                                                                              | 1.17 sec: 1.31x slower                                                                                                    |
| async_tree_memoization_tg  | 479 ms                                                                                                              | 628 ms: 1.31x slower                                                                                                      |
| scimark_sparse_mat_mult    | 6.47 ms                                                                                                             | 8.49 ms: 1.31x slower                                                                                                     |
| async_tree_none_tg         | 382 ms                                                                                                              | 510 ms: 1.33x slower                                                                                                      |
| dulwich_log                | 62.0 ms                                                                                                             | 82.9 ms: 1.34x slower                                                                                                     |
| sympy_expand               | 473 ms                                                                                                              | 635 ms: 1.34x slower                                                                                                      |
| sqlglot_normalize          | 134 ms                                                                                                              | 180 ms: 1.35x slower                                                                                                      |
| pycparser                  | 1.29 sec                                                                                                            | 1.73 sec: 1.35x slower                                                                                                    |
| deepcopy_reduce            | 3.60 us                                                                                                             | 4.85 us: 1.35x slower                                                                                                     |
| async_tree_none            | 395 ms                                                                                                              | 536 ms: 1.35x slower                                                                                                      |
| genshi_xml                 | 63.7 ms                                                                                                             | 86.6 ms: 1.36x slower                                                                                                     |
| tomli_loads                | 2.64 sec                                                                                                            | 3.60 sec: 1.36x slower                                                                                                    |
| python_startup_no_site     | 9.05 ms                                                                                                             | 12.4 ms: 1.37x slower                                                                                                     |
| bpe_tokeniser              | 5.77 sec                                                                                                            | 7.94 sec: 1.38x slower                                                                                                    |
| deepcopy_memo              | 41.1 us                                                                                                             | 56.6 us: 1.38x slower                                                                                                     |
| thrift                     | 994 us                                                                                                              | 1.38 ms: 1.39x slower                                                                                                     |
| many_optionals             | 708 us                                                                                                              | 983 us: 1.39x slower                                                                                                      |
| meteor_contest             | 116 ms                                                                                                              | 161 ms: 1.39x slower                                                                                                      |
| sympy_integrate            | 21.6 ms                                                                                                             | 30.1 ms: 1.39x slower                                                                                                     |
| pprint_safe_repr           | 966 ms                                                                                                              | 1.34 sec: 1.39x slower                                                                                                    |
| sympy_sum                  | 148 ms                                                                                                              | 208 ms: 1.40x slower                                                                                                      |
| genshi_text                | 29.4 ms                                                                                                             | 41.3 ms: 1.40x slower                                                                                                     |
| fannkuch                   | 491 ms                                                                                                              | 692 ms: 1.41x slower                                                                                                      |
| pprint_pformat             | 1.96 sec                                                                                                            | 2.78 sec: 1.42x slower                                                                                                    |
| coverage                   | 101 ms                                                                                                              | 144 ms: 1.42x slower                                                                                                      |
| crypto_pyaes               | 84.8 ms                                                                                                             | 121 ms: 1.43x slower                                                                                                      |
| pylint                     | 306 ms                                                                                                              | 438 ms: 1.43x slower                                                                                                      |
| regex_compile              | 130 ms                                                                                                              | 187 ms: 1.44x slower                                                                                                      |
| typing_runtime_protocols   | 210 us                                                                                                              | 302 us: 1.44x slower                                                                                                      |
| sympy_str                  | 275 ms                                                                                                              | 399 ms: 1.45x slower                                                                                                      |
| mypy2                      | 1.03 sec                                                                                                            | 1.51 sec: 1.47x slower                                                                                                    |
| subparsers                 | 25.6 ms                                                                                                             | 37.9 ms: 1.48x slower                                                                                                     |
| nbody                      | 125 ms                                                                                                              | 186 ms: 1.49x slower                                                                                                      |
| sqlalchemy_declarative     | 152 ms                                                                                                              | 227 ms: 1.50x slower                                                                                                      |
| bench_thread_pool          | 1.32 ms                                                                                                             | 2.00 ms: 1.51x slower                                                                                                     |
| generators                 | 36.9 ms                                                                                                             | 56.1 ms: 1.52x slower                                                                                                     |
| pyflate                    | 597 ms                                                                                                              | 911 ms: 1.52x slower                                                                                                      |
| 2to3                       | 307 ms                                                                                                              | 468 ms: 1.53x slower                                                                                                      |
| logging_simple             | 7.23 us                                                                                                             | 11.2 us: 1.55x slower                                                                                                     |
| logging_format             | 7.87 us                                                                                                             | 12.3 us: 1.56x slower                                                                                                     |
| django_template            | 41.4 ms                                                                                                             | 65.3 ms: 1.58x slower                                                                                                     |
| scimark_lu                 | 139 ms                                                                                                              | 228 ms: 1.63x slower                                                                                                      |
| float                      | 91.8 ms                                                                                                             | 154 ms: 1.67x slower                                                                                                      |
| sqlalchemy_imperative      | 15.3 ms                                                                                                             | 25.7 ms: 1.67x slower                                                                                                     |
| unpickle_pure_python       | 270 us                                                                                                              | 453 us: 1.68x slower                                                                                                      |
| html5lib                   | 63.8 ms                                                                                                             | 111 ms: 1.74x slower                                                                                                      |
| chaos                      | 74.2 ms                                                                                                             | 129 ms: 1.74x slower                                                                                                      |
| pickle_pure_python         | 401 us                                                                                                              | 701 us: 1.75x slower                                                                                                      |
| comprehensions             | 21.9 us                                                                                                             | 38.5 us: 1.75x slower                                                                                                     |
| scimark_sor                | 162 ms                                                                                                              | 285 ms: 1.76x slower                                                                                                      |
| scimark_monte_carlo        | 87.4 ms                                                                                                             | 154 ms: 1.76x slower                                                                                                      |
| richards_super             | 60.4 ms                                                                                                             | 108 ms: 1.79x slower                                                                                                      |
| mako                       | 14.2 ms                                                                                                             | 25.6 ms: 1.80x slower                                                                                                     |
| hexiom                     | 7.39 ms                                                                                                             | 13.4 ms: 1.81x slower                                                                                                     |
| richards                   | 53.5 ms                                                                                                             | 97.6 ms: 1.82x slower                                                                                                     |
| logging_silent             | 140 ns                                                                                                              | 261 ns: 1.87x slower                                                                                                      |
| raytrace                   | 324 ms                                                                                                              | 666 ms: 2.05x slower                                                                                                      |
| sqlglot_transpile          | 1.80 ms                                                                                                             | 3.73 ms: 2.07x slower                                                                                                     |
| sqlglot_parse              | 1.47 ms                                                                                                             | 3.13 ms: 2.12x slower                                                                                                     |
| go                         | 150 ms                                                                                                              | 337 ms: 2.25x slower                                                                                                      |
| deltablue                  | 4.01 ms                                                                                                             | 11.1 ms: 2.76x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.32x slower                                                                                                              |

Benchmark hidden because not significant (7): sqlite_synth, xml_etree_parse, asyncio_websockets, regex_v8, regex_effbot, pidigits, regex_dna
Ignored benchmarks (1) of results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: djangocms

- Geometric mean (including insignificant results): 1.272x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.31x
- 95% likely to have a slowdown of 1.30x
- 99% likely to have a slowdown of 1.29x

# Memory
- memory change: 1.19x