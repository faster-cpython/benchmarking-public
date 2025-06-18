# Results vs. base

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-aarch64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.114x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 357 ms                                                                                                            | 446 ms: 1.25x slower                                                                                                    |
| docutils       | 3.44 sec                                                                                                          | 3.94 sec: 1.14x slower                                                                                                  |
| html5lib       | 67.3 ms                                                                                                           | 84.1 ms: 1.25x slower                                                                                                   |
| sphinx         | 1.36 sec                                                                                                          | 1.59 sec: 1.17x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.20x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg          | 1.04 sec                                                                                                          | 977 ms: 1.06x faster                                                                                                    |
| async_tree_memoization_tg | 534 ms                                                                                                            | 518 ms: 1.03x faster                                                                                                    |
| async_tree_none_tg        | 434 ms                                                                                                            | 425 ms: 1.02x faster                                                                                                    |
| async_tree_io             | 1.01 sec                                                                                                          | 1.03 sec: 1.01x slower                                                                                                  |
| async_tree_none           | 449 ms                                                                                                            | 469 ms: 1.04x slower                                                                                                    |
| async_tree_cpu_io_mixed   | 823 ms                                                                                                            | 859 ms: 1.04x slower                                                                                                    |
| async_tree_memoization    | 532 ms                                                                                                            | 557 ms: 1.05x slower                                                                                                    |
| asyncio_tcp               | 570 ms                                                                                                            | 639 ms: 1.12x slower                                                                                                    |
| asyncio_tcp_ssl           | 2.24 sec                                                                                                          | 2.54 sec: 1.13x slower                                                                                                  |
| coroutines                | 33.0 ms                                                                                                           | 38.5 ms: 1.17x slower                                                                                                   |
| async_generators          | 515 ms                                                                                                            | 613 ms: 1.19x slower                                                                                                    |
| Geometric mean            | (ref)                                                                                                             | 1.05x slower                                                                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 96.7 ms                                                                                                           | 106 ms: 1.09x slower                                                                                                    |
| nbody          | 141 ms                                                                                                            | 191 ms: 1.35x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.14x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 30.3 ms                                                                                                           | 30.8 ms: 1.02x slower                                                                                                   |
| regex_dna      | 225 ms                                                                                                            | 235 ms: 1.04x slower                                                                                                    |
| regex_compile  | 155 ms                                                                                                            | 201 ms: 1.29x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.08x slower                                                                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 170 ms                                                                                                            | 159 ms: 1.07x faster                                                                                                    |
| pickle               | 20.5 us                                                                                                           | 20.0 us: 1.02x faster                                                                                                   |
| xml_etree_parse      | 227 ms                                                                                                            | 239 ms: 1.05x slower                                                                                                    |
| unpickle_list        | 6.80 us                                                                                                           | 7.58 us: 1.11x slower                                                                                                   |
| json_dumps           | 17.4 ms                                                                                                           | 19.7 ms: 1.14x slower                                                                                                   |
| xml_etree_generate   | 163 ms                                                                                                            | 189 ms: 1.16x slower                                                                                                    |
| json_loads           | 38.5 us                                                                                                           | 44.6 us: 1.16x slower                                                                                                   |
| unpickle             | 22.6 us                                                                                                           | 26.4 us: 1.17x slower                                                                                                   |
| xml_etree_process    | 110 ms                                                                                                            | 128 ms: 1.17x slower                                                                                                    |
| tomli_loads          | 2.93 sec                                                                                                          | 3.61 sec: 1.23x slower                                                                                                  |
| pickle_pure_python   | 468 us                                                                                                            | 593 us: 1.27x slower                                                                                                    |
| unpickle_pure_python | 329 us                                                                                                            | 418 us: 1.27x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.11x slower                                                                                                            |

Benchmark hidden because not significant (2): pickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 17.1 ms                                                                                                           | 23.3 ms: 1.36x slower                                                                                                   |
| python_startup_no_site | 9.73 ms                                                                                                           | 13.8 ms: 1.41x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.39x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 75.1 ms                                                                                                           | 98.2 ms: 1.31x slower                                                                                                   |
| mako            | 17.0 ms                                                                                                           | 23.8 ms: 1.39x slower                                                                                                   |
| genshi_text     | 33.3 ms                                                                                                           | 46.5 ms: 1.40x slower                                                                                                   |
| django_template | 53.6 ms                                                                                                           | 75.2 ms: 1.40x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.37x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                 | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool             | 5.40 sec                                                                                                          | 72.7 ms: 74.34x faster                                                                                                  |
| gc_traversal              | 7.30 ms                                                                                                           | 3.70 ms: 1.97x faster                                                                                                   |
| create_gc_cycles          | 3.86 ms                                                                                                           | 2.53 ms: 1.53x faster                                                                                                   |
| sqlite_synth              | 4.82 us                                                                                                           | 4.43 us: 1.09x faster                                                                                                   |
| xml_etree_iterparse       | 170 ms                                                                                                            | 159 ms: 1.07x faster                                                                                                    |
| async_tree_io_tg          | 1.04 sec                                                                                                          | 977 ms: 1.06x faster                                                                                                    |
| async_tree_memoization_tg | 534 ms                                                                                                            | 518 ms: 1.03x faster                                                                                                    |
| pickle                    | 20.5 us                                                                                                           | 20.0 us: 1.02x faster                                                                                                   |
| async_tree_none_tg        | 434 ms                                                                                                            | 425 ms: 1.02x faster                                                                                                    |
| async_tree_io             | 1.01 sec                                                                                                          | 1.03 sec: 1.01x slower                                                                                                  |
| regex_v8                  | 30.3 ms                                                                                                           | 30.8 ms: 1.02x slower                                                                                                   |
| regex_dna                 | 225 ms                                                                                                            | 235 ms: 1.04x slower                                                                                                    |
| async_tree_none           | 449 ms                                                                                                            | 469 ms: 1.04x slower                                                                                                    |
| async_tree_cpu_io_mixed   | 823 ms                                                                                                            | 859 ms: 1.04x slower                                                                                                    |
| async_tree_memoization    | 532 ms                                                                                                            | 557 ms: 1.05x slower                                                                                                    |
| xml_etree_parse           | 227 ms                                                                                                            | 239 ms: 1.05x slower                                                                                                    |
| float                     | 96.7 ms                                                                                                           | 106 ms: 1.09x slower                                                                                                    |
| unpickle_list             | 6.80 us                                                                                                           | 7.58 us: 1.11x slower                                                                                                   |
| asyncio_tcp               | 570 ms                                                                                                            | 639 ms: 1.12x slower                                                                                                    |
| pathlib                   | 26.8 ms                                                                                                           | 30.2 ms: 1.13x slower                                                                                                   |
| asyncio_tcp_ssl           | 2.24 sec                                                                                                          | 2.54 sec: 1.13x slower                                                                                                  |
| json_dumps                | 17.4 ms                                                                                                           | 19.7 ms: 1.14x slower                                                                                                   |
| pyflate                   | 581 ms                                                                                                            | 664 ms: 1.14x slower                                                                                                    |
| docutils                  | 3.44 sec                                                                                                          | 3.94 sec: 1.14x slower                                                                                                  |
| scimark_sor               | 169 ms                                                                                                            | 194 ms: 1.15x slower                                                                                                    |
| k_core                    | 2.95 sec                                                                                                          | 3.39 sec: 1.15x slower                                                                                                  |
| xml_etree_generate        | 163 ms                                                                                                            | 189 ms: 1.16x slower                                                                                                    |
| json_loads                | 38.5 us                                                                                                           | 44.6 us: 1.16x slower                                                                                                   |
| json                      | 6.86 ms                                                                                                           | 7.96 ms: 1.16x slower                                                                                                   |
| scimark_fft               | 498 ms                                                                                                            | 580 ms: 1.16x slower                                                                                                    |
| sphinx                    | 1.36 sec                                                                                                          | 1.59 sec: 1.17x slower                                                                                                  |
| scimark_sparse_mat_mult   | 7.76 ms                                                                                                           | 9.05 ms: 1.17x slower                                                                                                   |
| coroutines                | 33.0 ms                                                                                                           | 38.5 ms: 1.17x slower                                                                                                   |
| shortest_path             | 608 ms                                                                                                            | 710 ms: 1.17x slower                                                                                                    |
| unpack_sequence           | 62.4 ns                                                                                                           | 73.0 ns: 1.17x slower                                                                                                   |
| unpickle                  | 22.6 us                                                                                                           | 26.4 us: 1.17x slower                                                                                                   |
| xml_etree_process         | 110 ms                                                                                                            | 128 ms: 1.17x slower                                                                                                    |
| fannkuch                  | 590 ms                                                                                                            | 693 ms: 1.17x slower                                                                                                    |
| pycparser                 | 1.49 sec                                                                                                          | 1.76 sec: 1.18x slower                                                                                                  |
| generators                | 39.7 ms                                                                                                           | 47.0 ms: 1.18x slower                                                                                                   |
| async_generators          | 515 ms                                                                                                            | 613 ms: 1.19x slower                                                                                                    |
| connected_components      | 565 ms                                                                                                            | 674 ms: 1.19x slower                                                                                                    |
| pprint_safe_repr          | 1.34 sec                                                                                                          | 1.60 sec: 1.19x slower                                                                                                  |
| logging_silent            | 946 ns                                                                                                            | 1.13 us: 1.20x slower                                                                                                   |
| chaos                     | 82.7 ms                                                                                                           | 99.4 ms: 1.20x slower                                                                                                   |
| hexiom                    | 8.23 ms                                                                                                           | 9.96 ms: 1.21x slower                                                                                                   |
| pprint_pformat            | 2.70 sec                                                                                                          | 3.27 sec: 1.21x slower                                                                                                  |
| spectral_norm             | 156 ms                                                                                                            | 190 ms: 1.21x slower                                                                                                    |
| meteor_contest            | 128 ms                                                                                                            | 156 ms: 1.22x slower                                                                                                    |
| deltablue                 | 4.54 ms                                                                                                           | 5.55 ms: 1.22x slower                                                                                                   |
| nqueens                   | 125 ms                                                                                                            | 153 ms: 1.23x slower                                                                                                    |
| tomli_loads               | 2.93 sec                                                                                                          | 3.61 sec: 1.23x slower                                                                                                  |
| 2to3                      | 357 ms                                                                                                            | 446 ms: 1.25x slower                                                                                                    |
| scimark_lu                | 186 ms                                                                                                            | 232 ms: 1.25x slower                                                                                                    |
| pylint                    | 367 ms                                                                                                            | 457 ms: 1.25x slower                                                                                                    |
| html5lib                  | 67.3 ms                                                                                                           | 84.1 ms: 1.25x slower                                                                                                   |
| logging_simple            | 9.40 us                                                                                                           | 11.8 us: 1.25x slower                                                                                                   |
| subparsers                | 36.2 ms                                                                                                           | 45.6 ms: 1.26x slower                                                                                                   |
| coverage                  | 141 ms                                                                                                            | 177 ms: 1.26x slower                                                                                                    |
| dulwich_log               | 66.0 ms                                                                                                           | 83.3 ms: 1.26x slower                                                                                                   |
| pickle_pure_python        | 468 us                                                                                                            | 593 us: 1.27x slower                                                                                                    |
| sqlglot_v2_optimize       | 77.0 ms                                                                                                           | 97.6 ms: 1.27x slower                                                                                                   |
| logging_format            | 10.3 us                                                                                                           | 13.1 us: 1.27x slower                                                                                                   |
| unpickle_pure_python      | 329 us                                                                                                            | 418 us: 1.27x slower                                                                                                    |
| go                        | 141 ms                                                                                                            | 178 ms: 1.27x slower                                                                                                    |
| sqlglot_v2_transpile      | 2.22 ms                                                                                                           | 2.83 ms: 1.27x slower                                                                                                   |
| raytrace                  | 390 ms                                                                                                            | 498 ms: 1.28x slower                                                                                                    |
| sqlglot_v2_normalize      | 161 ms                                                                                                            | 207 ms: 1.28x slower                                                                                                    |
| mdp                       | 1.97 sec                                                                                                          | 2.52 sec: 1.28x slower                                                                                                  |
| many_optionals            | 957 us                                                                                                            | 1.23 ms: 1.29x slower                                                                                                   |
| regex_compile             | 155 ms                                                                                                            | 201 ms: 1.29x slower                                                                                                    |
| bench_thread_pool         | 1.52 ms                                                                                                           | 1.96 ms: 1.29x slower                                                                                                   |
| genshi_xml                | 75.1 ms                                                                                                           | 98.2 ms: 1.31x slower                                                                                                   |
| telco                     | 13.6 ms                                                                                                           | 17.8 ms: 1.31x slower                                                                                                   |
| deepcopy_memo             | 43.3 us                                                                                                           | 56.7 us: 1.31x slower                                                                                                   |
| sqlglot_v2_parse          | 1.77 ms                                                                                                           | 2.33 ms: 1.31x slower                                                                                                   |
| deepcopy                  | 406 us                                                                                                            | 534 us: 1.32x slower                                                                                                    |
| sympy_sum                 | 180 ms                                                                                                            | 239 ms: 1.32x slower                                                                                                    |
| richards                  | 64.0 ms                                                                                                           | 84.8 ms: 1.32x slower                                                                                                   |
| bpe_tokeniser             | 6.73 sec                                                                                                          | 8.94 sec: 1.33x slower                                                                                                  |
| sympy_str                 | 339 ms                                                                                                            | 450 ms: 1.33x slower                                                                                                    |
| sympy_expand              | 606 ms                                                                                                            | 807 ms: 1.33x slower                                                                                                    |
| comprehensions            | 23.1 us                                                                                                           | 30.8 us: 1.34x slower                                                                                                   |
| nbody                     | 141 ms                                                                                                            | 191 ms: 1.35x slower                                                                                                    |
| thrift                    | 1.25 ms                                                                                                           | 1.69 ms: 1.35x slower                                                                                                   |
| deepcopy_reduce           | 4.59 us                                                                                                           | 6.22 us: 1.36x slower                                                                                                   |
| sympy_integrate           | 23.5 ms                                                                                                           | 32.0 ms: 1.36x slower                                                                                                   |
| python_startup            | 17.1 ms                                                                                                           | 23.3 ms: 1.36x slower                                                                                                   |
| typing_runtime_protocols  | 259 us                                                                                                            | 358 us: 1.38x slower                                                                                                    |
| mako                      | 17.0 ms                                                                                                           | 23.8 ms: 1.39x slower                                                                                                   |
| genshi_text               | 33.3 ms                                                                                                           | 46.5 ms: 1.40x slower                                                                                                   |
| django_template           | 53.6 ms                                                                                                           | 75.2 ms: 1.40x slower                                                                                                   |
| richards_super            | 72.2 ms                                                                                                           | 101 ms: 1.40x slower                                                                                                    |
| crypto_pyaes              | 105 ms                                                                                                            | 148 ms: 1.41x slower                                                                                                    |
| python_startup_no_site    | 9.73 ms                                                                                                           | 13.8 ms: 1.41x slower                                                                                                   |
| scimark_monte_carlo       | 95.9 ms                                                                                                           | 139 ms: 1.45x slower                                                                                                    |
| Geometric mean            | (ref)                                                                                                             | 1.13x slower                                                                                                            |

Benchmark hidden because not significant (6): asyncio_websockets, async_tree_cpu_io_mixed_tg, pidigits, pickle_list, pickle_dict, regex_effbot
Ignored benchmarks (1) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: djangocms

- Geometric mean (including insignificant results): 1.114x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.17x
- 95% likely to have a slowdown of 1.16x
- 99% likely to have a slowdown of 1.16x

# Memory
- memory change: 1.23x