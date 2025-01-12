# Results vs. base

- fork: python
- ref: 22a442181d5f1ac496da
- machine: linux-aarch64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.268x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-NOGIL/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 303 ms                                                                                                              | 458 ms: 1.51x slower                                                                                                      |
| docutils       | 3.02 sec                                                                                                            | 3.68 sec: 1.22x slower                                                                                                    |
| html5lib       | 63.8 ms                                                                                                             | 110 ms: 1.73x slower                                                                                                      |
| sphinx         | 1.18 sec                                                                                                            | 1.49 sec: 1.26x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.41x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-NOGIL/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp                | 569 ms                                                                                                              | 647 ms: 1.14x slower                                                                                                      |
| asyncio_tcp_ssl            | 2.28 sec                                                                                                            | 2.61 sec: 1.15x slower                                                                                                    |
| coroutines                 | 28.4 ms                                                                                                             | 32.6 ms: 1.15x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 667 ms                                                                                                              | 808 ms: 1.21x slower                                                                                                      |
| async_generators           | 496 ms                                                                                                              | 606 ms: 1.22x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 679 ms                                                                                                              | 840 ms: 1.24x slower                                                                                                      |
| async_tree_io_tg           | 883 ms                                                                                                              | 1.17 sec: 1.32x slower                                                                                                    |
| async_tree_memoization_tg  | 474 ms                                                                                                              | 631 ms: 1.33x slower                                                                                                      |
| async_tree_io              | 889 ms                                                                                                              | 1.20 sec: 1.35x slower                                                                                                    |
| async_tree_memoization     | 495 ms                                                                                                              | 666 ms: 1.35x slower                                                                                                      |
| async_tree_none            | 389 ms                                                                                                              | 543 ms: 1.40x slower                                                                                                      |
| async_tree_none_tg         | 367 ms                                                                                                              | 518 ms: 1.41x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.25x slower                                                                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-NOGIL/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 123 ms                                                                                                              | 185 ms: 1.50x slower                                                                                                      |
| float          | 89.1 ms                                                                                                             | 150 ms: 1.68x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.35x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-NOGIL/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 250 ms                                                                                                              | 263 ms: 1.05x slower                                                                                                      |
| regex_v8       | 32.4 ms                                                                                                             | 34.9 ms: 1.08x slower                                                                                                     |
| regex_compile  | 125 ms                                                                                                              | 186 ms: 1.49x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.14x slower                                                                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-NOGIL/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 143 ms                                                                                                              | 136 ms: 1.06x faster                                                                                                      |
| unpickle_list        | 6.76 us                                                                                                             | 7.52 us: 1.11x slower                                                                                                     |
| json_loads           | 32.3 us                                                                                                             | 36.4 us: 1.13x slower                                                                                                     |
| unpickle             | 18.3 us                                                                                                             | 20.9 us: 1.14x slower                                                                                                     |
| xml_etree_generate   | 118 ms                                                                                                              | 143 ms: 1.21x slower                                                                                                      |
| json_dumps           | 14.9 ms                                                                                                             | 18.4 ms: 1.24x slower                                                                                                     |
| tomli_loads          | 2.60 sec                                                                                                            | 3.34 sec: 1.28x slower                                                                                                    |
| xml_etree_process    | 84.2 ms                                                                                                             | 111 ms: 1.32x slower                                                                                                      |
| unpickle_pure_python | 265 us                                                                                                              | 440 us: 1.66x slower                                                                                                      |
| pickle_pure_python   | 385 us                                                                                                              | 661 us: 1.72x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.18x slower                                                                                                              |

Benchmark hidden because not significant (4): pickle_list, xml_etree_parse, pickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-NOGIL/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.3 ms                                                                                                             | 20.4 ms: 1.26x slower                                                                                                     |
| python_startup_no_site | 9.01 ms                                                                                                             | 12.3 ms: 1.36x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.31x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-NOGIL/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 64.4 ms                                                                                                             | 81.1 ms: 1.26x slower                                                                                                     |
| genshi_text     | 28.5 ms                                                                                                             | 39.7 ms: 1.39x slower                                                                                                     |
| django_template | 41.2 ms                                                                                                             | 64.2 ms: 1.56x slower                                                                                                     |
| mako            | 14.2 ms                                                                                                             | 25.2 ms: 1.77x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.48x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                  | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-NOGIL/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 4.18 sec                                                                                                            | 61.3 ms: 68.20x faster                                                                                                    |
| gc_traversal               | 6.85 ms                                                                                                             | 5.03 ms: 1.36x faster                                                                                                     |
| create_gc_cycles           | 3.60 ms                                                                                                             | 2.89 ms: 1.25x faster                                                                                                     |
| sqlite_synth               | 4.19 us                                                                                                             | 3.83 us: 1.09x faster                                                                                                     |
| xml_etree_iterparse        | 143 ms                                                                                                              | 136 ms: 1.06x faster                                                                                                      |
| regex_dna                  | 250 ms                                                                                                              | 263 ms: 1.05x slower                                                                                                      |
| pathlib                    | 22.2 ms                                                                                                             | 23.8 ms: 1.07x slower                                                                                                     |
| regex_v8                   | 32.4 ms                                                                                                             | 34.9 ms: 1.08x slower                                                                                                     |
| unpickle_list              | 6.76 us                                                                                                             | 7.52 us: 1.11x slower                                                                                                     |
| json_loads                 | 32.3 us                                                                                                             | 36.4 us: 1.13x slower                                                                                                     |
| json                       | 5.63 ms                                                                                                             | 6.38 ms: 1.13x slower                                                                                                     |
| asyncio_tcp                | 569 ms                                                                                                              | 647 ms: 1.14x slower                                                                                                      |
| k_core                     | 2.87 sec                                                                                                            | 3.27 sec: 1.14x slower                                                                                                    |
| unpickle                   | 18.3 us                                                                                                             | 20.9 us: 1.14x slower                                                                                                     |
| asyncio_tcp_ssl            | 2.28 sec                                                                                                            | 2.61 sec: 1.15x slower                                                                                                    |
| scimark_fft                | 429 ms                                                                                                              | 493 ms: 1.15x slower                                                                                                      |
| coroutines                 | 28.4 ms                                                                                                             | 32.6 ms: 1.15x slower                                                                                                     |
| spectral_norm              | 129 ms                                                                                                              | 150 ms: 1.16x slower                                                                                                      |
| mdp                        | 3.42 sec                                                                                                            | 4.00 sec: 1.17x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 667 ms                                                                                                              | 808 ms: 1.21x slower                                                                                                      |
| xml_etree_generate         | 118 ms                                                                                                              | 143 ms: 1.21x slower                                                                                                      |
| docutils                   | 3.02 sec                                                                                                            | 3.68 sec: 1.22x slower                                                                                                    |
| async_generators           | 496 ms                                                                                                              | 606 ms: 1.22x slower                                                                                                      |
| connected_components       | 545 ms                                                                                                              | 671 ms: 1.23x slower                                                                                                      |
| json_dumps                 | 14.9 ms                                                                                                             | 18.4 ms: 1.24x slower                                                                                                     |
| async_tree_cpu_io_mixed    | 679 ms                                                                                                              | 840 ms: 1.24x slower                                                                                                      |
| shortest_path              | 575 ms                                                                                                              | 716 ms: 1.25x slower                                                                                                      |
| python_startup             | 16.3 ms                                                                                                             | 20.4 ms: 1.26x slower                                                                                                     |
| genshi_xml                 | 64.4 ms                                                                                                             | 81.1 ms: 1.26x slower                                                                                                     |
| sphinx                     | 1.18 sec                                                                                                            | 1.49 sec: 1.26x slower                                                                                                    |
| deepcopy                   | 350 us                                                                                                              | 446 us: 1.27x slower                                                                                                      |
| tomli_loads                | 2.60 sec                                                                                                            | 3.34 sec: 1.28x slower                                                                                                    |
| deepcopy_reduce            | 3.74 us                                                                                                             | 4.81 us: 1.29x slower                                                                                                     |
| nqueens                    | 103 ms                                                                                                              | 134 ms: 1.30x slower                                                                                                      |
| thrift                     | 1.01 ms                                                                                                             | 1.33 ms: 1.31x slower                                                                                                     |
| xml_etree_process          | 84.2 ms                                                                                                             | 111 ms: 1.32x slower                                                                                                      |
| scimark_sparse_mat_mult    | 6.24 ms                                                                                                             | 8.22 ms: 1.32x slower                                                                                                     |
| pycparser                  | 1.28 sec                                                                                                            | 1.68 sec: 1.32x slower                                                                                                    |
| async_tree_io_tg           | 883 ms                                                                                                              | 1.17 sec: 1.32x slower                                                                                                    |
| dulwich_log                | 62.6 ms                                                                                                             | 83.0 ms: 1.33x slower                                                                                                     |
| telco                      | 9.96 ms                                                                                                             | 13.3 ms: 1.33x slower                                                                                                     |
| async_tree_memoization_tg  | 474 ms                                                                                                              | 631 ms: 1.33x slower                                                                                                      |
| async_tree_io              | 889 ms                                                                                                              | 1.20 sec: 1.35x slower                                                                                                    |
| async_tree_memoization     | 495 ms                                                                                                              | 666 ms: 1.35x slower                                                                                                      |
| python_startup_no_site     | 9.01 ms                                                                                                             | 12.3 ms: 1.36x slower                                                                                                     |
| pylint                     | 324 ms                                                                                                              | 443 ms: 1.37x slower                                                                                                      |
| bpe_tokeniser              | 5.75 sec                                                                                                            | 7.86 sec: 1.37x slower                                                                                                    |
| pprint_safe_repr           | 963 ms                                                                                                              | 1.32 sec: 1.37x slower                                                                                                    |
| typing_runtime_protocols   | 201 us                                                                                                              | 276 us: 1.37x slower                                                                                                      |
| pprint_pformat             | 1.98 sec                                                                                                            | 2.73 sec: 1.38x slower                                                                                                    |
| meteor_contest             | 115 ms                                                                                                              | 158 ms: 1.38x slower                                                                                                      |
| sqlglot_normalize          | 132 ms                                                                                                              | 181 ms: 1.38x slower                                                                                                      |
| sympy_expand               | 482 ms                                                                                                              | 665 ms: 1.38x slower                                                                                                      |
| sqlglot_optimize           | 62.9 ms                                                                                                             | 87.1 ms: 1.38x slower                                                                                                     |
| coverage                   | 99.7 ms                                                                                                             | 139 ms: 1.39x slower                                                                                                      |
| unpack_sequence            | 58.4 ns                                                                                                             | 81.2 ns: 1.39x slower                                                                                                     |
| sympy_integrate            | 21.6 ms                                                                                                             | 30.1 ms: 1.39x slower                                                                                                     |
| genshi_text                | 28.5 ms                                                                                                             | 39.7 ms: 1.39x slower                                                                                                     |
| async_tree_none            | 389 ms                                                                                                              | 543 ms: 1.40x slower                                                                                                      |
| subparsers                 | 26.9 ms                                                                                                             | 37.8 ms: 1.40x slower                                                                                                     |
| many_optionals             | 694 us                                                                                                              | 975 us: 1.41x slower                                                                                                      |
| fannkuch                   | 478 ms                                                                                                              | 674 ms: 1.41x slower                                                                                                      |
| async_tree_none_tg         | 367 ms                                                                                                              | 518 ms: 1.41x slower                                                                                                      |
| sympy_sum                  | 148 ms                                                                                                              | 210 ms: 1.42x slower                                                                                                      |
| crypto_pyaes               | 83.1 ms                                                                                                             | 119 ms: 1.44x slower                                                                                                      |
| logging_simple             | 7.44 us                                                                                                             | 10.8 us: 1.45x slower                                                                                                     |
| deepcopy_memo              | 40.2 us                                                                                                             | 59.2 us: 1.47x slower                                                                                                     |
| logging_format             | 8.00 us                                                                                                             | 11.8 us: 1.48x slower                                                                                                     |
| bench_thread_pool          | 1.34 ms                                                                                                             | 2.00 ms: 1.49x slower                                                                                                     |
| sympy_str                  | 268 ms                                                                                                              | 401 ms: 1.49x slower                                                                                                      |
| regex_compile              | 125 ms                                                                                                              | 186 ms: 1.49x slower                                                                                                      |
| nbody                      | 123 ms                                                                                                              | 185 ms: 1.50x slower                                                                                                      |
| 2to3                       | 303 ms                                                                                                              | 458 ms: 1.51x slower                                                                                                      |
| generators                 | 36.6 ms                                                                                                             | 55.4 ms: 1.51x slower                                                                                                     |
| pyflate                    | 569 ms                                                                                                              | 866 ms: 1.52x slower                                                                                                      |
| django_template            | 41.2 ms                                                                                                             | 64.2 ms: 1.56x slower                                                                                                     |
| sqlalchemy_declarative     | 146 ms                                                                                                              | 231 ms: 1.58x slower                                                                                                      |
| scimark_lu                 | 140 ms                                                                                                              | 223 ms: 1.59x slower                                                                                                      |
| hexiom                     | 7.70 ms                                                                                                             | 12.2 ms: 1.59x slower                                                                                                     |
| scimark_monte_carlo        | 87.3 ms                                                                                                             | 143 ms: 1.64x slower                                                                                                      |
| unpickle_pure_python       | 265 us                                                                                                              | 440 us: 1.66x slower                                                                                                      |
| float                      | 89.1 ms                                                                                                             | 150 ms: 1.68x slower                                                                                                      |
| scimark_sor                | 152 ms                                                                                                              | 258 ms: 1.69x slower                                                                                                      |
| pickle_pure_python         | 385 us                                                                                                              | 661 us: 1.72x slower                                                                                                      |
| chaos                      | 73.6 ms                                                                                                             | 126 ms: 1.72x slower                                                                                                      |
| richards_super             | 61.4 ms                                                                                                             | 106 ms: 1.72x slower                                                                                                      |
| html5lib                   | 63.8 ms                                                                                                             | 110 ms: 1.73x slower                                                                                                      |
| sqlalchemy_imperative      | 15.4 ms                                                                                                             | 26.7 ms: 1.74x slower                                                                                                     |
| comprehensions             | 21.7 us                                                                                                             | 38.0 us: 1.75x slower                                                                                                     |
| mako                       | 14.2 ms                                                                                                             | 25.2 ms: 1.77x slower                                                                                                     |
| richards                   | 52.1 ms                                                                                                             | 93.4 ms: 1.79x slower                                                                                                     |
| sqlglot_transpile          | 1.83 ms                                                                                                             | 3.49 ms: 1.91x slower                                                                                                     |
| logging_silent             | 139 ns                                                                                                              | 269 ns: 1.93x slower                                                                                                      |
| raytrace                   | 324 ms                                                                                                              | 655 ms: 2.02x slower                                                                                                      |
| sqlglot_parse              | 1.47 ms                                                                                                             | 3.16 ms: 2.15x slower                                                                                                     |
| go                         | 144 ms                                                                                                              | 332 ms: 2.30x slower                                                                                                      |
| deltablue                  | 3.98 ms                                                                                                             | 10.8 ms: 2.70x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.29x slower                                                                                                              |

Benchmark hidden because not significant (7): pickle_list, pidigits, regex_effbot, xml_etree_parse, pickle, pickle_dict, asyncio_websockets

- Geometric mean (including insignificant results): 1.268x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.32x
- 95% likely to have a slowdown of 1.31x
- 99% likely to have a slowdown of 1.29x

# Memory
- memory change: 1.20x