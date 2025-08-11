# Results vs. base

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-aarch64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.131x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 299 ms                                                                                                            | 352 ms: 1.17x slower                                                                                                    |
| docutils       | 2.90 sec                                                                                                          | 3.20 sec: 1.10x slower                                                                                                  |
| html5lib       | 64.2 ms                                                                                                           | 69.9 ms: 1.09x slower                                                                                                   |
| sphinx         | 1.13 sec                                                                                                          | 1.31 sec: 1.16x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.13x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg          | 902 ms                                                                                                            | 843 ms: 1.07x faster                                                                                                    |
| async_tree_memoization_tg | 453 ms                                                                                                            | 448 ms: 1.01x faster                                                                                                    |
| async_tree_memoization    | 461 ms                                                                                                            | 475 ms: 1.03x slower                                                                                                    |
| async_tree_cpu_io_mixed   | 646 ms                                                                                                            | 668 ms: 1.03x slower                                                                                                    |
| async_tree_none           | 384 ms                                                                                                            | 400 ms: 1.04x slower                                                                                                    |
| asyncio_tcp               | 541 ms                                                                                                            | 568 ms: 1.05x slower                                                                                                    |
| asyncio_tcp_ssl           | 2.20 sec                                                                                                          | 2.41 sec: 1.09x slower                                                                                                  |
| async_generators          | 454 ms                                                                                                            | 515 ms: 1.13x slower                                                                                                    |
| Geometric mean            | (ref)                                                                                                             | 1.03x slower                                                                                                            |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io, async_tree_none_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 84.5 ms                                                                                                           | 95.0 ms: 1.12x slower                                                                                                   |
| nbody          | 119 ms                                                                                                            | 181 ms: 1.52x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.19x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 222 ms                                                                                                            | 241 ms: 1.09x slower                                                                                                    |
| regex_compile  | 124 ms                                                                                                            | 148 ms: 1.20x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.07x slower                                                                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 143 ms                                                                                                            | 131 ms: 1.09x faster                                                                                                    |
| xml_etree_parse      | 177 ms                                                                                                            | 183 ms: 1.04x slower                                                                                                    |
| unpickle_list        | 6.50 us                                                                                                           | 6.91 us: 1.06x slower                                                                                                   |
| json_dumps           | 12.0 ms                                                                                                           | 13.1 ms: 1.10x slower                                                                                                   |
| unpickle             | 18.4 us                                                                                                           | 20.2 us: 1.10x slower                                                                                                   |
| json_loads           | 32.5 us                                                                                                           | 36.4 us: 1.12x slower                                                                                                   |
| pickle_pure_python   | 385 us                                                                                                            | 437 us: 1.14x slower                                                                                                    |
| unpickle_pure_python | 259 us                                                                                                            | 299 us: 1.16x slower                                                                                                    |
| tomli_loads          | 2.45 sec                                                                                                          | 2.87 sec: 1.17x slower                                                                                                  |
| xml_etree_process    | 81.2 ms                                                                                                           | 101 ms: 1.24x slower                                                                                                    |
| xml_etree_generate   | 113 ms                                                                                                            | 142 ms: 1.26x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.09x slower                                                                                                            |

Benchmark hidden because not significant (3): pickle, pickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.1 ms                                                                                                           | 19.9 ms: 1.31x slower                                                                                                   |
| python_startup_no_site | 8.56 ms                                                                                                           | 12.0 ms: 1.40x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.36x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 60.0 ms                                                                                                           | 76.4 ms: 1.27x slower                                                                                                   |
| django_template | 39.3 ms                                                                                                           | 51.5 ms: 1.31x slower                                                                                                   |
| genshi_text     | 27.1 ms                                                                                                           | 35.8 ms: 1.33x slower                                                                                                   |
| mako            | 13.5 ms                                                                                                           | 21.0 ms: 1.56x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.36x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                 | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool             | 5.71 sec                                                                                                          | 66.8 ms: 85.56x faster                                                                                                  |
| gc_traversal              | 7.01 ms                                                                                                           | 2.85 ms: 2.46x faster                                                                                                   |
| create_gc_cycles          | 3.90 ms                                                                                                           | 2.27 ms: 1.72x faster                                                                                                   |
| xml_etree_iterparse       | 143 ms                                                                                                            | 131 ms: 1.09x faster                                                                                                    |
| sqlite_synth              | 3.79 us                                                                                                           | 3.52 us: 1.08x faster                                                                                                   |
| async_tree_io_tg          | 902 ms                                                                                                            | 843 ms: 1.07x faster                                                                                                    |
| async_tree_memoization_tg | 453 ms                                                                                                            | 448 ms: 1.01x faster                                                                                                    |
| async_tree_memoization    | 461 ms                                                                                                            | 475 ms: 1.03x slower                                                                                                    |
| async_tree_cpu_io_mixed   | 646 ms                                                                                                            | 668 ms: 1.03x slower                                                                                                    |
| xml_etree_parse           | 177 ms                                                                                                            | 183 ms: 1.04x slower                                                                                                    |
| async_tree_none           | 384 ms                                                                                                            | 400 ms: 1.04x slower                                                                                                    |
| asyncio_tcp               | 541 ms                                                                                                            | 568 ms: 1.05x slower                                                                                                    |
| unpickle_list             | 6.50 us                                                                                                           | 6.91 us: 1.06x slower                                                                                                   |
| k_core                    | 2.81 sec                                                                                                          | 3.01 sec: 1.07x slower                                                                                                  |
| logging_silent            | 130 ns                                                                                                            | 140 ns: 1.07x slower                                                                                                    |
| json                      | 5.84 ms                                                                                                           | 6.30 ms: 1.08x slower                                                                                                   |
| regex_dna                 | 222 ms                                                                                                            | 241 ms: 1.09x slower                                                                                                    |
| html5lib                  | 64.2 ms                                                                                                           | 69.9 ms: 1.09x slower                                                                                                   |
| asyncio_tcp_ssl           | 2.20 sec                                                                                                          | 2.41 sec: 1.09x slower                                                                                                  |
| json_dumps                | 12.0 ms                                                                                                           | 13.1 ms: 1.10x slower                                                                                                   |
| unpickle                  | 18.4 us                                                                                                           | 20.2 us: 1.10x slower                                                                                                   |
| docutils                  | 2.90 sec                                                                                                          | 3.20 sec: 1.10x slower                                                                                                  |
| scimark_fft               | 424 ms                                                                                                            | 471 ms: 1.11x slower                                                                                                    |
| scimark_sor               | 144 ms                                                                                                            | 160 ms: 1.11x slower                                                                                                    |
| pycparser                 | 1.22 sec                                                                                                          | 1.36 sec: 1.11x slower                                                                                                  |
| pyflate                   | 534 ms                                                                                                            | 595 ms: 1.11x slower                                                                                                    |
| dulwich_log               | 53.3 ms                                                                                                           | 59.7 ms: 1.12x slower                                                                                                   |
| json_loads                | 32.5 us                                                                                                           | 36.4 us: 1.12x slower                                                                                                   |
| float                     | 84.5 ms                                                                                                           | 95.0 ms: 1.12x slower                                                                                                   |
| async_generators          | 454 ms                                                                                                            | 515 ms: 1.13x slower                                                                                                    |
| pickle_pure_python        | 385 us                                                                                                            | 437 us: 1.14x slower                                                                                                    |
| generators                | 35.9 ms                                                                                                           | 40.9 ms: 1.14x slower                                                                                                   |
| telco                     | 162 ms                                                                                                            | 187 ms: 1.15x slower                                                                                                    |
| scimark_sparse_mat_mult   | 6.85 ms                                                                                                           | 7.91 ms: 1.15x slower                                                                                                   |
| shortest_path             | 589 ms                                                                                                            | 681 ms: 1.16x slower                                                                                                    |
| hexiom                    | 6.90 ms                                                                                                           | 7.98 ms: 1.16x slower                                                                                                   |
| unpickle_pure_python      | 259 us                                                                                                            | 299 us: 1.16x slower                                                                                                    |
| sphinx                    | 1.13 sec                                                                                                          | 1.31 sec: 1.16x slower                                                                                                  |
| mdp                       | 1.66 sec                                                                                                          | 1.94 sec: 1.17x slower                                                                                                  |
| connected_components      | 559 ms                                                                                                            | 652 ms: 1.17x slower                                                                                                    |
| tomli_loads               | 2.45 sec                                                                                                          | 2.87 sec: 1.17x slower                                                                                                  |
| 2to3                      | 299 ms                                                                                                            | 352 ms: 1.17x slower                                                                                                    |
| deepcopy                  | 326 us                                                                                                            | 386 us: 1.18x slower                                                                                                    |
| many_optionals            | 932 us                                                                                                            | 1.10 ms: 1.18x slower                                                                                                   |
| nqueens                   | 99.5 ms                                                                                                           | 118 ms: 1.19x slower                                                                                                    |
| pprint_safe_repr          | 881 ms                                                                                                            | 1.05 sec: 1.19x slower                                                                                                  |
| sqlglot_v2_optimize       | 61.3 ms                                                                                                           | 73.4 ms: 1.20x slower                                                                                                   |
| pprint_pformat            | 1.80 sec                                                                                                          | 2.16 sec: 1.20x slower                                                                                                  |
| regex_compile             | 124 ms                                                                                                            | 148 ms: 1.20x slower                                                                                                    |
| deepcopy_reduce           | 3.51 us                                                                                                           | 4.21 us: 1.20x slower                                                                                                   |
| go                        | 127 ms                                                                                                            | 153 ms: 1.20x slower                                                                                                    |
| subparsers                | 48.1 ms                                                                                                           | 58.0 ms: 1.21x slower                                                                                                   |
| logging_simple            | 6.75 us                                                                                                           | 8.17 us: 1.21x slower                                                                                                   |
| comprehensions            | 20.0 us                                                                                                           | 24.2 us: 1.21x slower                                                                                                   |
| sqlglot_v2_normalize      | 126 ms                                                                                                            | 152 ms: 1.21x slower                                                                                                    |
| logging_format            | 7.49 us                                                                                                           | 9.14 us: 1.22x slower                                                                                                   |
| pylint                    | 311 ms                                                                                                            | 381 ms: 1.22x slower                                                                                                    |
| raytrace                  | 323 ms                                                                                                            | 396 ms: 1.23x slower                                                                                                    |
| spectral_norm             | 116 ms                                                                                                            | 142 ms: 1.23x slower                                                                                                    |
| chaos                     | 65.3 ms                                                                                                           | 80.0 ms: 1.23x slower                                                                                                   |
| bpe_tokeniser             | 5.51 sec                                                                                                          | 6.80 sec: 1.23x slower                                                                                                  |
| xml_etree_process         | 81.2 ms                                                                                                           | 101 ms: 1.24x slower                                                                                                    |
| deepcopy_memo             | 36.5 us                                                                                                           | 45.5 us: 1.25x slower                                                                                                   |
| deltablue                 | 3.88 ms                                                                                                           | 4.85 ms: 1.25x slower                                                                                                   |
| thrift                    | 940 us                                                                                                            | 1.18 ms: 1.25x slower                                                                                                   |
| xml_etree_generate        | 113 ms                                                                                                            | 142 ms: 1.26x slower                                                                                                    |
| fannkuch                  | 466 ms                                                                                                            | 593 ms: 1.27x slower                                                                                                    |
| genshi_xml                | 60.0 ms                                                                                                           | 76.4 ms: 1.27x slower                                                                                                   |
| sympy_expand              | 464 ms                                                                                                            | 591 ms: 1.27x slower                                                                                                    |
| sympy_integrate           | 20.1 ms                                                                                                           | 25.6 ms: 1.28x slower                                                                                                   |
| sympy_str                 | 267 ms                                                                                                            | 342 ms: 1.28x slower                                                                                                    |
| scimark_monte_carlo       | 80.7 ms                                                                                                           | 104 ms: 1.29x slower                                                                                                    |
| typing_runtime_protocols  | 194 us                                                                                                            | 250 us: 1.29x slower                                                                                                    |
| scimark_lu                | 146 ms                                                                                                            | 188 ms: 1.29x slower                                                                                                    |
| crypto_pyaes              | 84.3 ms                                                                                                           | 109 ms: 1.30x slower                                                                                                    |
| meteor_contest            | 107 ms                                                                                                            | 140 ms: 1.30x slower                                                                                                    |
| django_template           | 39.3 ms                                                                                                           | 51.5 ms: 1.31x slower                                                                                                   |
| python_startup            | 15.1 ms                                                                                                           | 19.9 ms: 1.31x slower                                                                                                   |
| sqlglot_v2_transpile      | 1.74 ms                                                                                                           | 2.30 ms: 1.32x slower                                                                                                   |
| genshi_text               | 27.1 ms                                                                                                           | 35.8 ms: 1.33x slower                                                                                                   |
| sympy_sum                 | 141 ms                                                                                                            | 187 ms: 1.33x slower                                                                                                    |
| richards                  | 52.7 ms                                                                                                           | 70.6 ms: 1.34x slower                                                                                                   |
| sqlglot_v2_parse          | 1.39 ms                                                                                                           | 1.86 ms: 1.34x slower                                                                                                   |
| bench_thread_pool         | 1.37 ms                                                                                                           | 1.86 ms: 1.35x slower                                                                                                   |
| richards_super            | 59.8 ms                                                                                                           | 81.2 ms: 1.36x slower                                                                                                   |
| python_startup_no_site    | 8.56 ms                                                                                                           | 12.0 ms: 1.40x slower                                                                                                   |
| coverage                  | 102 ms                                                                                                            | 144 ms: 1.41x slower                                                                                                    |
| unpack_sequence           | 51.2 ns                                                                                                           | 74.3 ns: 1.45x slower                                                                                                   |
| nbody                     | 119 ms                                                                                                            | 181 ms: 1.52x slower                                                                                                    |
| mako                      | 13.5 ms                                                                                                           | 21.0 ms: 1.56x slower                                                                                                   |
| Geometric mean            | (ref)                                                                                                             | 1.10x slower                                                                                                            |

Benchmark hidden because not significant (12): pickle, regex_v8, pidigits, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io, async_tree_none_tg, regex_effbot, pickle_list, pathlib, pickle_dict, coroutines
Ignored benchmarks (1) of results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: djangocms

- Geometric mean (including insignificant results): 1.131x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: 1.20x