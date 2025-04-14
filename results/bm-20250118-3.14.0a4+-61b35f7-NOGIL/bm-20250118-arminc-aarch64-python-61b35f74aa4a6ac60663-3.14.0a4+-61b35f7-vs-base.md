# Results vs. base

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: linux-aarch64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.172x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json | results/bm-20250118-3.14.0a4+-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                                                              | 387 ms: 1.26x slower                                                                                                      |
| docutils       | 3.01 sec                                                                                                            | 3.41 sec: 1.14x slower                                                                                                    |
| html5lib       | 62.9 ms                                                                                                             | 76.2 ms: 1.21x slower                                                                                                     |
| sphinx         | 1.18 sec                                                                                                            | 1.40 sec: 1.18x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.20x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json | results/bm-20250118-3.14.0a4+-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json |
|---------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 474 ms                                                                                                              | 492 ms: 1.04x slower                                                                                                      |
| async_tree_none_tg        | 374 ms                                                                                                              | 399 ms: 1.07x slower                                                                                                      |
| async_tree_io             | 895 ms                                                                                                              | 966 ms: 1.08x slower                                                                                                      |
| coroutines                | 29.5 ms                                                                                                             | 31.8 ms: 1.08x slower                                                                                                     |
| async_tree_cpu_io_mixed   | 678 ms                                                                                                              | 733 ms: 1.08x slower                                                                                                      |
| asyncio_tcp               | 570 ms                                                                                                              | 618 ms: 1.08x slower                                                                                                      |
| async_tree_memoization    | 490 ms                                                                                                              | 538 ms: 1.10x slower                                                                                                      |
| asyncio_tcp_ssl           | 2.26 sec                                                                                                            | 2.57 sec: 1.14x slower                                                                                                    |
| async_tree_none           | 385 ms                                                                                                              | 442 ms: 1.15x slower                                                                                                      |
| async_generators          | 454 ms                                                                                                              | 542 ms: 1.19x slower                                                                                                      |
| Geometric mean            | (ref)                                                                                                               | 1.08x slower                                                                                                              |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json | results/bm-20250118-3.14.0a4+-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 86.7 ms                                                                                                             | 103 ms: 1.19x slower                                                                                                      |
| nbody          | 123 ms                                                                                                              | 182 ms: 1.48x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.20x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json | results/bm-20250118-3.14.0a4+-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                                                              | 159 ms: 1.23x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.05x slower                                                                                                              |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json | results/bm-20250118-3.14.0a4+-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 146 ms                                                                                                              | 133 ms: 1.10x faster                                                                                                      |
| xml_etree_parse      | 184 ms                                                                                                              | 177 ms: 1.04x faster                                                                                                      |
| pickle_dict          | 39.6 us                                                                                                             | 40.6 us: 1.03x slower                                                                                                     |
| json_dumps           | 15.4 ms                                                                                                             | 16.7 ms: 1.09x slower                                                                                                     |
| unpickle_list        | 6.65 us                                                                                                             | 7.27 us: 1.09x slower                                                                                                     |
| json_loads           | 33.8 us                                                                                                             | 37.2 us: 1.10x slower                                                                                                     |
| unpickle             | 17.9 us                                                                                                             | 21.1 us: 1.17x slower                                                                                                     |
| xml_etree_generate   | 115 ms                                                                                                              | 140 ms: 1.22x slower                                                                                                      |
| pickle_pure_python   | 393 us                                                                                                              | 483 us: 1.23x slower                                                                                                      |
| unpickle_pure_python | 266 us                                                                                                              | 331 us: 1.24x slower                                                                                                      |
| tomli_loads          | 2.57 sec                                                                                                            | 3.25 sec: 1.26x slower                                                                                                    |
| xml_etree_process    | 82.2 ms                                                                                                             | 104 ms: 1.27x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.11x slower                                                                                                              |

Benchmark hidden because not significant (2): pickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json | results/bm-20250118-3.14.0a4+-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.4 ms                                                                                                             | 20.0 ms: 1.22x slower                                                                                                     |
| python_startup_no_site | 9.15 ms                                                                                                             | 12.2 ms: 1.34x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.28x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json | results/bm-20250118-3.14.0a4+-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                                                                             | 80.2 ms: 1.30x slower                                                                                                     |
| genshi_text     | 27.1 ms                                                                                                             | 37.2 ms: 1.37x slower                                                                                                     |
| django_template | 39.4 ms                                                                                                             | 56.5 ms: 1.44x slower                                                                                                     |
| mako            | 14.6 ms                                                                                                             | 23.6 ms: 1.62x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.43x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                 | results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json | results/bm-20250118-3.14.0a4+-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json |
|---------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool             | 7.08 sec                                                                                                            | 56.3 ms: 125.71x faster                                                                                                   |
| create_gc_cycles          | 3.61 ms                                                                                                             | 2.17 ms: 1.66x faster                                                                                                     |
| gc_traversal              | 6.96 ms                                                                                                             | 5.42 ms: 1.28x faster                                                                                                     |
| xml_etree_iterparse       | 146 ms                                                                                                              | 133 ms: 1.10x faster                                                                                                      |
| sqlite_synth              | 4.13 us                                                                                                             | 3.75 us: 1.10x faster                                                                                                     |
| xml_etree_parse           | 184 ms                                                                                                              | 177 ms: 1.04x faster                                                                                                      |
| pickle_dict               | 39.6 us                                                                                                             | 40.6 us: 1.03x slower                                                                                                     |
| async_tree_memoization_tg | 474 ms                                                                                                              | 492 ms: 1.04x slower                                                                                                      |
| async_tree_none_tg        | 374 ms                                                                                                              | 399 ms: 1.07x slower                                                                                                      |
| pathlib                   | 21.8 ms                                                                                                             | 23.5 ms: 1.08x slower                                                                                                     |
| async_tree_io             | 895 ms                                                                                                              | 966 ms: 1.08x slower                                                                                                      |
| coroutines                | 29.5 ms                                                                                                             | 31.8 ms: 1.08x slower                                                                                                     |
| async_tree_cpu_io_mixed   | 678 ms                                                                                                              | 733 ms: 1.08x slower                                                                                                      |
| asyncio_tcp               | 570 ms                                                                                                              | 618 ms: 1.08x slower                                                                                                      |
| json_dumps                | 15.4 ms                                                                                                             | 16.7 ms: 1.09x slower                                                                                                     |
| json                      | 5.80 ms                                                                                                             | 6.34 ms: 1.09x slower                                                                                                     |
| unpickle_list             | 6.65 us                                                                                                             | 7.27 us: 1.09x slower                                                                                                     |
| async_tree_memoization    | 490 ms                                                                                                              | 538 ms: 1.10x slower                                                                                                      |
| json_loads                | 33.8 us                                                                                                             | 37.2 us: 1.10x slower                                                                                                     |
| mdp                       | 3.42 sec                                                                                                            | 3.84 sec: 1.12x slower                                                                                                    |
| dulwich_log               | 61.4 ms                                                                                                             | 69.0 ms: 1.12x slower                                                                                                     |
| pycparser                 | 1.29 sec                                                                                                            | 1.46 sec: 1.13x slower                                                                                                    |
| k_core                    | 2.86 sec                                                                                                            | 3.23 sec: 1.13x slower                                                                                                    |
| docutils                  | 3.01 sec                                                                                                            | 3.41 sec: 1.14x slower                                                                                                    |
| asyncio_tcp_ssl           | 2.26 sec                                                                                                            | 2.57 sec: 1.14x slower                                                                                                    |
| logging_silent            | 139 ns                                                                                                              | 159 ns: 1.15x slower                                                                                                      |
| async_tree_none           | 385 ms                                                                                                              | 442 ms: 1.15x slower                                                                                                      |
| unpack_sequence           | 63.9 ns                                                                                                             | 74.3 ns: 1.16x slower                                                                                                     |
| pyflate                   | 567 ms                                                                                                              | 661 ms: 1.17x slower                                                                                                      |
| unpickle                  | 17.9 us                                                                                                             | 21.1 us: 1.17x slower                                                                                                     |
| scimark_fft               | 418 ms                                                                                                              | 494 ms: 1.18x slower                                                                                                      |
| sphinx                    | 1.18 sec                                                                                                            | 1.40 sec: 1.18x slower                                                                                                    |
| connected_components      | 550 ms                                                                                                              | 656 ms: 1.19x slower                                                                                                      |
| float                     | 86.7 ms                                                                                                             | 103 ms: 1.19x slower                                                                                                      |
| async_generators          | 454 ms                                                                                                              | 542 ms: 1.19x slower                                                                                                      |
| shortest_path             | 572 ms                                                                                                              | 685 ms: 1.20x slower                                                                                                      |
| spectral_norm             | 121 ms                                                                                                              | 145 ms: 1.20x slower                                                                                                      |
| pprint_pformat            | 1.97 sec                                                                                                            | 2.39 sec: 1.21x slower                                                                                                    |
| html5lib                  | 62.9 ms                                                                                                             | 76.2 ms: 1.21x slower                                                                                                     |
| scimark_sor               | 150 ms                                                                                                              | 183 ms: 1.21x slower                                                                                                      |
| python_startup            | 16.4 ms                                                                                                             | 20.0 ms: 1.22x slower                                                                                                     |
| generators                | 36.1 ms                                                                                                             | 43.9 ms: 1.22x slower                                                                                                     |
| sqlglot_normalize         | 131 ms                                                                                                              | 159 ms: 1.22x slower                                                                                                      |
| xml_etree_generate        | 115 ms                                                                                                              | 140 ms: 1.22x slower                                                                                                      |
| pprint_safe_repr          | 947 ms                                                                                                              | 1.16 sec: 1.23x slower                                                                                                    |
| pickle_pure_python        | 393 us                                                                                                              | 483 us: 1.23x slower                                                                                                      |
| regex_compile             | 130 ms                                                                                                              | 159 ms: 1.23x slower                                                                                                      |
| deepcopy                  | 349 us                                                                                                              | 429 us: 1.23x slower                                                                                                      |
| pylint                    | 318 ms                                                                                                              | 392 ms: 1.23x slower                                                                                                      |
| telco                     | 9.53 ms                                                                                                             | 11.8 ms: 1.24x slower                                                                                                     |
| unpickle_pure_python      | 266 us                                                                                                              | 331 us: 1.24x slower                                                                                                      |
| scimark_sparse_mat_mult   | 6.46 ms                                                                                                             | 8.06 ms: 1.25x slower                                                                                                     |
| sqlglot_optimize          | 63.4 ms                                                                                                             | 79.4 ms: 1.25x slower                                                                                                     |
| tomli_loads               | 2.57 sec                                                                                                            | 3.25 sec: 1.26x slower                                                                                                    |
| 2to3                      | 306 ms                                                                                                              | 387 ms: 1.26x slower                                                                                                      |
| xml_etree_process         | 82.2 ms                                                                                                             | 104 ms: 1.27x slower                                                                                                      |
| hexiom                    | 7.55 ms                                                                                                             | 9.63 ms: 1.28x slower                                                                                                     |
| go                        | 140 ms                                                                                                              | 181 ms: 1.29x slower                                                                                                      |
| deepcopy_memo             | 41.0 us                                                                                                             | 52.9 us: 1.29x slower                                                                                                     |
| thrift                    | 1.00 ms                                                                                                             | 1.29 ms: 1.29x slower                                                                                                     |
| coverage                  | 102 ms                                                                                                              | 132 ms: 1.30x slower                                                                                                      |
| logging_format            | 7.75 us                                                                                                             | 10.1 us: 1.30x slower                                                                                                     |
| meteor_contest            | 122 ms                                                                                                              | 158 ms: 1.30x slower                                                                                                      |
| genshi_xml                | 61.6 ms                                                                                                             | 80.2 ms: 1.30x slower                                                                                                     |
| chaos                     | 67.8 ms                                                                                                             | 88.7 ms: 1.31x slower                                                                                                     |
| logging_simple            | 6.99 us                                                                                                             | 9.16 us: 1.31x slower                                                                                                     |
| subparsers                | 26.0 ms                                                                                                             | 34.2 ms: 1.32x slower                                                                                                     |
| sympy_expand              | 471 ms                                                                                                              | 621 ms: 1.32x slower                                                                                                      |
| bpe_tokeniser             | 5.68 sec                                                                                                            | 7.53 sec: 1.33x slower                                                                                                    |
| scimark_monte_carlo       | 85.2 ms                                                                                                             | 113 ms: 1.33x slower                                                                                                      |
| crypto_pyaes              | 84.4 ms                                                                                                             | 112 ms: 1.33x slower                                                                                                      |
| sqlglot_transpile         | 1.86 ms                                                                                                             | 2.49 ms: 1.34x slower                                                                                                     |
| python_startup_no_site    | 9.15 ms                                                                                                             | 12.2 ms: 1.34x slower                                                                                                     |
| sympy_str                 | 272 ms                                                                                                              | 364 ms: 1.34x slower                                                                                                      |
| deepcopy_reduce           | 3.55 us                                                                                                             | 4.76 us: 1.34x slower                                                                                                     |
| many_optionals            | 699 us                                                                                                              | 938 us: 1.34x slower                                                                                                      |
| comprehensions            | 22.0 us                                                                                                             | 29.6 us: 1.34x slower                                                                                                     |
| raytrace                  | 315 ms                                                                                                              | 426 ms: 1.35x slower                                                                                                      |
| nqueens                   | 99.7 ms                                                                                                             | 135 ms: 1.35x slower                                                                                                      |
| sympy_sum                 | 146 ms                                                                                                              | 199 ms: 1.36x slower                                                                                                      |
| bench_thread_pool         | 1.34 ms                                                                                                             | 1.83 ms: 1.37x slower                                                                                                     |
| genshi_text               | 27.1 ms                                                                                                             | 37.2 ms: 1.37x slower                                                                                                     |
| scimark_lu                | 137 ms                                                                                                              | 189 ms: 1.38x slower                                                                                                      |
| sqlalchemy_declarative    | 148 ms                                                                                                              | 205 ms: 1.38x slower                                                                                                      |
| typing_runtime_protocols  | 207 us                                                                                                              | 288 us: 1.39x slower                                                                                                      |
| sqlalchemy_imperative     | 15.6 ms                                                                                                             | 21.8 ms: 1.40x slower                                                                                                     |
| fannkuch                  | 484 ms                                                                                                              | 678 ms: 1.40x slower                                                                                                      |
| richards                  | 51.9 ms                                                                                                             | 73.8 ms: 1.42x slower                                                                                                     |
| sympy_integrate           | 21.7 ms                                                                                                             | 31.0 ms: 1.43x slower                                                                                                     |
| django_template           | 39.4 ms                                                                                                             | 56.5 ms: 1.44x slower                                                                                                     |
| richards_super            | 61.7 ms                                                                                                             | 88.6 ms: 1.44x slower                                                                                                     |
| sqlglot_parse             | 1.45 ms                                                                                                             | 2.12 ms: 1.46x slower                                                                                                     |
| nbody                     | 123 ms                                                                                                              | 182 ms: 1.48x slower                                                                                                      |
| mako                      | 14.6 ms                                                                                                             | 23.6 ms: 1.62x slower                                                                                                     |
| deltablue                 | 3.86 ms                                                                                                             | 6.30 ms: 1.63x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                               | 1.14x slower                                                                                                              |

Benchmark hidden because not significant (9): regex_v8, pidigits, pickle, regex_effbot, regex_dna, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io_tg, pickle_list

- Geometric mean (including insignificant results): 1.172x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.18x
- 95% likely to have a slowdown of 1.18x
- 99% likely to have a slowdown of 1.17x

# Memory
- memory change: 1.20x