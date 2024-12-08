# Results vs. base

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: linux-aarch64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.308x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json | results/bm-20241207-3.14.0a2+-79b7cab-NOGIL/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 307 ms                                                                                                              | 468 ms: 1.53x slower                                                                                                      |
| docutils       | 3.05 sec                                                                                                            | 3.77 sec: 1.24x slower                                                                                                    |
| html5lib       | 63.8 ms                                                                                                             | 118 ms: 1.84x slower                                                                                                      |
| sphinx         | 1.18 sec                                                                                                            | 1.52 sec: 1.29x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.46x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json | results/bm-20241207-3.14.0a2+-79b7cab-NOGIL/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 29.1 ms                                                                                                             | 33.4 ms: 1.15x slower                                                                                                     |
| async_generators           | 510 ms                                                                                                              | 637 ms: 1.25x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 698 ms                                                                                                              | 874 ms: 1.25x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 690 ms                                                                                                              | 900 ms: 1.30x slower                                                                                                      |
| async_tree_memoization_tg  | 520 ms                                                                                                              | 693 ms: 1.33x slower                                                                                                      |
| async_tree_memoization     | 528 ms                                                                                                              | 708 ms: 1.34x slower                                                                                                      |
| async_tree_io_tg           | 946 ms                                                                                                              | 1.30 sec: 1.37x slower                                                                                                    |
| async_tree_none_tg         | 411 ms                                                                                                              | 578 ms: 1.41x slower                                                                                                      |
| async_tree_io              | 917 ms                                                                                                              | 1.31 sec: 1.43x slower                                                                                                    |
| async_tree_none            | 401 ms                                                                                                              | 592 ms: 1.48x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.30x slower                                                                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json | results/bm-20241207-3.14.0a2+-79b7cab-NOGIL/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 238 ms                                                                                                              | 232 ms: 1.03x faster                                                                                                      |
| nbody          | 120 ms                                                                                                              | 183 ms: 1.53x slower                                                                                                      |
| float          | 95.8 ms                                                                                                             | 198 ms: 2.07x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.45x slower                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json | results/bm-20241207-3.14.0a2+-79b7cab-NOGIL/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                                                              | 203 ms: 1.59x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.14x slower                                                                                                              |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json | results/bm-20241207-3.14.0a2+-79b7cab-NOGIL/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| json_loads           | 32.0 us                                                                                                             | 37.1 us: 1.16x slower                                                                                                     |
| xml_etree_generate   | 116 ms                                                                                                              | 144 ms: 1.25x slower                                                                                                      |
| tomli_loads          | 2.76 sec                                                                                                            | 3.69 sec: 1.33x slower                                                                                                    |
| json_dumps           | 14.2 ms                                                                                                             | 19.3 ms: 1.35x slower                                                                                                     |
| xml_etree_process    | 83.6 ms                                                                                                             | 116 ms: 1.39x slower                                                                                                      |
| unpickle_pure_python | 268 us                                                                                                              | 459 us: 1.71x slower                                                                                                      |
| pickle_pure_python   | 386 us                                                                                                              | 668 us: 1.73x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.30x slower                                                                                                              |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json | results/bm-20241207-3.14.0a2+-79b7cab-NOGIL/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.2 ms                                                                                                             | 21.6 ms: 1.33x slower                                                                                                     |
| python_startup_no_site | 9.08 ms                                                                                                             | 12.8 ms: 1.41x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.37x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json | results/bm-20241207-3.14.0a2+-79b7cab-NOGIL/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 63.3 ms                                                                                                             | 84.5 ms: 1.33x slower                                                                                                     |
| genshi_text     | 29.4 ms                                                                                                             | 43.3 ms: 1.47x slower                                                                                                     |
| django_template | 40.5 ms                                                                                                             | 68.5 ms: 1.69x slower                                                                                                     |
| mako            | 14.4 ms                                                                                                             | 26.3 ms: 1.83x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.57x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                  | results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json | results/bm-20241207-3.14.0a2+-79b7cab-NOGIL/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 3.66 sec                                                                                                            | 66.8 ms: 54.83x faster                                                                                                    |
| gc_traversal               | 6.92 ms                                                                                                             | 5.06 ms: 1.37x faster                                                                                                     |
| create_gc_cycles           | 3.30 ms                                                                                                             | 2.94 ms: 1.12x faster                                                                                                     |
| pidigits                   | 238 ms                                                                                                              | 232 ms: 1.03x faster                                                                                                      |
| json                       | 5.72 ms                                                                                                             | 6.55 ms: 1.15x slower                                                                                                     |
| coroutines                 | 29.1 ms                                                                                                             | 33.4 ms: 1.15x slower                                                                                                     |
| spectral_norm              | 146 ms                                                                                                              | 168 ms: 1.15x slower                                                                                                      |
| pathlib                    | 23.1 ms                                                                                                             | 26.6 ms: 1.15x slower                                                                                                     |
| json_loads                 | 32.0 us                                                                                                             | 37.1 us: 1.16x slower                                                                                                     |
| telco                      | 10.00 ms                                                                                                            | 11.8 ms: 1.18x slower                                                                                                     |
| scimark_fft                | 453 ms                                                                                                              | 536 ms: 1.18x slower                                                                                                      |
| mdp                        | 3.44 sec                                                                                                            | 4.10 sec: 1.19x slower                                                                                                    |
| scimark_sparse_mat_mult    | 6.86 ms                                                                                                             | 8.23 ms: 1.20x slower                                                                                                     |
| k_core                     | 2.84 sec                                                                                                            | 3.42 sec: 1.20x slower                                                                                                    |
| connected_components       | 549 ms                                                                                                              | 678 ms: 1.23x slower                                                                                                      |
| docutils                   | 3.05 sec                                                                                                            | 3.77 sec: 1.24x slower                                                                                                    |
| shortest_path              | 572 ms                                                                                                              | 711 ms: 1.24x slower                                                                                                      |
| xml_etree_generate         | 116 ms                                                                                                              | 144 ms: 1.25x slower                                                                                                      |
| async_generators           | 510 ms                                                                                                              | 637 ms: 1.25x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 698 ms                                                                                                              | 874 ms: 1.25x slower                                                                                                      |
| sphinx                     | 1.18 sec                                                                                                            | 1.52 sec: 1.29x slower                                                                                                    |
| nqueens                    | 107 ms                                                                                                              | 138 ms: 1.30x slower                                                                                                      |
| deepcopy                   | 344 us                                                                                                              | 449 us: 1.30x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 690 ms                                                                                                              | 900 ms: 1.30x slower                                                                                                      |
| python_startup             | 16.2 ms                                                                                                             | 21.6 ms: 1.33x slower                                                                                                     |
| meteor_contest             | 118 ms                                                                                                              | 158 ms: 1.33x slower                                                                                                      |
| async_tree_memoization_tg  | 520 ms                                                                                                              | 693 ms: 1.33x slower                                                                                                      |
| tomli_loads                | 2.76 sec                                                                                                            | 3.69 sec: 1.33x slower                                                                                                    |
| genshi_xml                 | 63.3 ms                                                                                                             | 84.5 ms: 1.33x slower                                                                                                     |
| sqlglot_normalize          | 134 ms                                                                                                              | 179 ms: 1.34x slower                                                                                                      |
| async_tree_memoization     | 528 ms                                                                                                              | 708 ms: 1.34x slower                                                                                                      |
| json_dumps                 | 14.2 ms                                                                                                             | 19.3 ms: 1.35x slower                                                                                                     |
| deepcopy_reduce            | 3.62 us                                                                                                             | 4.94 us: 1.36x slower                                                                                                     |
| async_tree_io_tg           | 946 ms                                                                                                              | 1.30 sec: 1.37x slower                                                                                                    |
| bpe_tokeniser              | 5.73 sec                                                                                                            | 7.87 sec: 1.37x slower                                                                                                    |
| coverage                   | 98.7 ms                                                                                                             | 136 ms: 1.38x slower                                                                                                      |
| typing_runtime_protocols   | 205 us                                                                                                              | 284 us: 1.39x slower                                                                                                      |
| xml_etree_process          | 83.6 ms                                                                                                             | 116 ms: 1.39x slower                                                                                                      |
| crypto_pyaes               | 85.2 ms                                                                                                             | 118 ms: 1.39x slower                                                                                                      |
| python_startup_no_site     | 9.08 ms                                                                                                             | 12.8 ms: 1.41x slower                                                                                                     |
| fannkuch                   | 490 ms                                                                                                              | 690 ms: 1.41x slower                                                                                                      |
| async_tree_none_tg         | 411 ms                                                                                                              | 578 ms: 1.41x slower                                                                                                      |
| pprint_safe_repr           | 952 ms                                                                                                              | 1.36 sec: 1.43x slower                                                                                                    |
| async_tree_io              | 917 ms                                                                                                              | 1.31 sec: 1.43x slower                                                                                                    |
| pprint_pformat             | 1.95 sec                                                                                                            | 2.80 sec: 1.44x slower                                                                                                    |
| many_optionals             | 712 us                                                                                                              | 1.03 ms: 1.44x slower                                                                                                     |
| deepcopy_memo              | 40.3 us                                                                                                             | 58.8 us: 1.46x slower                                                                                                     |
| sqlglot_optimize           | 62.9 ms                                                                                                             | 92.2 ms: 1.46x slower                                                                                                     |
| dulwich_log                | 60.6 ms                                                                                                             | 88.9 ms: 1.47x slower                                                                                                     |
| genshi_text                | 29.4 ms                                                                                                             | 43.3 ms: 1.47x slower                                                                                                     |
| async_tree_none            | 401 ms                                                                                                              | 592 ms: 1.48x slower                                                                                                      |
| sympy_integrate            | 21.9 ms                                                                                                             | 32.6 ms: 1.49x slower                                                                                                     |
| pylint                     | 318 ms                                                                                                              | 480 ms: 1.51x slower                                                                                                      |
| bench_thread_pool          | 1.33 ms                                                                                                             | 2.00 ms: 1.51x slower                                                                                                     |
| 2to3                       | 307 ms                                                                                                              | 468 ms: 1.53x slower                                                                                                      |
| nbody                      | 120 ms                                                                                                              | 183 ms: 1.53x slower                                                                                                      |
| pyflate                    | 605 ms                                                                                                              | 927 ms: 1.53x slower                                                                                                      |
| generators                 | 36.6 ms                                                                                                             | 56.4 ms: 1.54x slower                                                                                                     |
| pycparser                  | 1.23 sec                                                                                                            | 1.91 sec: 1.56x slower                                                                                                    |
| subparsers                 | 25.9 ms                                                                                                             | 40.8 ms: 1.58x slower                                                                                                     |
| regex_compile              | 128 ms                                                                                                              | 203 ms: 1.59x slower                                                                                                      |
| thrift                     | 977 us                                                                                                              | 1.60 ms: 1.63x slower                                                                                                     |
| sympy_str                  | 278 ms                                                                                                              | 458 ms: 1.65x slower                                                                                                      |
| django_template            | 40.5 ms                                                                                                             | 68.5 ms: 1.69x slower                                                                                                     |
| unpickle_pure_python       | 268 us                                                                                                              | 459 us: 1.71x slower                                                                                                      |
| pickle_pure_python         | 386 us                                                                                                              | 668 us: 1.73x slower                                                                                                      |
| hexiom                     | 7.25 ms                                                                                                             | 12.8 ms: 1.77x slower                                                                                                     |
| logging_format             | 7.74 us                                                                                                             | 14.0 us: 1.81x slower                                                                                                     |
| logging_simple             | 7.24 us                                                                                                             | 13.1 us: 1.82x slower                                                                                                     |
| sympy_expand               | 471 ms                                                                                                              | 859 ms: 1.82x slower                                                                                                      |
| mako                       | 14.4 ms                                                                                                             | 26.3 ms: 1.83x slower                                                                                                     |
| comprehensions             | 21.0 us                                                                                                             | 38.7 us: 1.84x slower                                                                                                     |
| html5lib                   | 63.8 ms                                                                                                             | 118 ms: 1.84x slower                                                                                                      |
| logging_silent             | 143 ns                                                                                                              | 265 ns: 1.85x slower                                                                                                      |
| sqlalchemy_declarative     | 145 ms                                                                                                              | 271 ms: 1.87x slower                                                                                                      |
| sqlalchemy_imperative      | 15.5 ms                                                                                                             | 29.1 ms: 1.87x slower                                                                                                     |
| chaos                      | 71.1 ms                                                                                                             | 136 ms: 1.91x slower                                                                                                      |
| scimark_sor                | 164 ms                                                                                                              | 314 ms: 1.92x slower                                                                                                      |
| scimark_monte_carlo        | 85.4 ms                                                                                                             | 164 ms: 1.92x slower                                                                                                      |
| richards                   | 55.0 ms                                                                                                             | 106 ms: 1.92x slower                                                                                                      |
| richards_super             | 61.8 ms                                                                                                             | 119 ms: 1.93x slower                                                                                                      |
| scimark_lu                 | 137 ms                                                                                                              | 271 ms: 1.97x slower                                                                                                      |
| sympy_sum                  | 143 ms                                                                                                              | 287 ms: 2.01x slower                                                                                                      |
| float                      | 95.8 ms                                                                                                             | 198 ms: 2.07x slower                                                                                                      |
| sqlglot_transpile          | 1.78 ms                                                                                                             | 3.96 ms: 2.22x slower                                                                                                     |
| raytrace                   | 321 ms                                                                                                              | 736 ms: 2.29x slower                                                                                                      |
| sqlglot_parse              | 1.45 ms                                                                                                             | 3.38 ms: 2.33x slower                                                                                                     |
| go                         | 144 ms                                                                                                              | 373 ms: 2.59x slower                                                                                                      |
| deltablue                  | 3.98 ms                                                                                                             | 11.8 ms: 2.97x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.39x slower                                                                                                              |

Benchmark hidden because not significant (7): regex_effbot, xml_etree_parse, sqlite_synth, xml_etree_iterparse, asyncio_websockets, regex_dna, regex_v8
Ignored benchmarks (1) of results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: djangocms

- Geometric mean (including insignificant results): 1.308x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.36x
- 95% likely to have a slowdown of 1.35x
- 99% likely to have a slowdown of 1.33x

# Memory
- memory change: 1.20x