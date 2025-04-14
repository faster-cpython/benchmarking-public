# Results vs. base

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-aarch64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.136x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 296 ms                                                                                                              | 363 ms: 1.23x slower                                                                                                      |
| docutils       | 2.96 sec                                                                                                            | 3.25 sec: 1.10x slower                                                                                                    |
| html5lib       | 65.1 ms                                                                                                             | 74.1 ms: 1.14x slower                                                                                                     |
| sphinx         | 1.16 sec                                                                                                            | 1.32 sec: 1.14x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.15x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|---------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg          | 907 ms                                                                                                              | 844 ms: 1.07x faster                                                                                                      |
| async_tree_memoization_tg | 461 ms                                                                                                              | 455 ms: 1.01x faster                                                                                                      |
| async_tree_cpu_io_mixed   | 659 ms                                                                                                              | 679 ms: 1.03x slower                                                                                                      |
| asyncio_tcp               | 546 ms                                                                                                              | 584 ms: 1.07x slower                                                                                                      |
| async_tree_memoization    | 465 ms                                                                                                              | 499 ms: 1.07x slower                                                                                                      |
| async_tree_none           | 386 ms                                                                                                              | 415 ms: 1.08x slower                                                                                                      |
| asyncio_tcp_ssl           | 2.16 sec                                                                                                            | 2.46 sec: 1.14x slower                                                                                                    |
| async_generators          | 449 ms                                                                                                              | 525 ms: 1.17x slower                                                                                                      |
| Geometric mean            | (ref)                                                                                                               | 1.03x slower                                                                                                              |

Benchmark hidden because not significant (5): coroutines, asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 87.7 ms                                                                                                             | 102 ms: 1.17x slower                                                                                                      |
| nbody          | 121 ms                                                                                                              | 186 ms: 1.54x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.21x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 27.9 ms                                                                                                             | 27.6 ms: 1.01x faster                                                                                                     |
| regex_compile  | 127 ms                                                                                                              | 161 ms: 1.27x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.06x slower                                                                                                              |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 141 ms                                                                                                              | 130 ms: 1.08x faster                                                                                                      |
| unpickle_list        | 6.60 us                                                                                                             | 7.30 us: 1.11x slower                                                                                                     |
| pickle_pure_python   | 397 us                                                                                                              | 441 us: 1.11x slower                                                                                                      |
| json_loads           | 34.3 us                                                                                                             | 38.2 us: 1.11x slower                                                                                                     |
| unpickle_pure_python | 273 us                                                                                                              | 308 us: 1.13x slower                                                                                                      |
| unpickle             | 17.9 us                                                                                                             | 20.3 us: 1.13x slower                                                                                                     |
| json_dumps           | 14.0 ms                                                                                                             | 16.0 ms: 1.14x slower                                                                                                     |
| xml_etree_generate   | 115 ms                                                                                                              | 135 ms: 1.17x slower                                                                                                      |
| xml_etree_process    | 80.1 ms                                                                                                             | 98.0 ms: 1.22x slower                                                                                                     |
| tomli_loads          | 2.46 sec                                                                                                            | 3.09 sec: 1.26x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                               | 1.09x slower                                                                                                              |

Benchmark hidden because not significant (4): pickle, pickle_list, xml_etree_parse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.3 ms                                                                                                             | 19.5 ms: 1.20x slower                                                                                                     |
| python_startup_no_site | 10.2 ms                                                                                                             | 14.4 ms: 1.41x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.30x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 60.2 ms                                                                                                             | 76.7 ms: 1.27x slower                                                                                                     |
| genshi_text     | 27.6 ms                                                                                                             | 36.1 ms: 1.31x slower                                                                                                     |
| django_template | 40.4 ms                                                                                                             | 53.7 ms: 1.33x slower                                                                                                     |
| mako            | 14.2 ms                                                                                                             | 22.1 ms: 1.56x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.36x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                 | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|---------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool             | 2.75 sec                                                                                                            | 57.7 ms: 47.56x faster                                                                                                    |
| gc_traversal              | 6.68 ms                                                                                                             | 2.72 ms: 2.45x faster                                                                                                     |
| create_gc_cycles          | 3.82 ms                                                                                                             | 2.10 ms: 1.81x faster                                                                                                     |
| xml_etree_iterparse       | 141 ms                                                                                                              | 130 ms: 1.08x faster                                                                                                      |
| sqlite_synth              | 3.76 us                                                                                                             | 3.49 us: 1.08x faster                                                                                                     |
| async_tree_io_tg          | 907 ms                                                                                                              | 844 ms: 1.07x faster                                                                                                      |
| async_tree_memoization_tg | 461 ms                                                                                                              | 455 ms: 1.01x faster                                                                                                      |
| regex_v8                  | 27.9 ms                                                                                                             | 27.6 ms: 1.01x faster                                                                                                     |
| async_tree_cpu_io_mixed   | 659 ms                                                                                                              | 679 ms: 1.03x slower                                                                                                      |
| asyncio_tcp               | 546 ms                                                                                                              | 584 ms: 1.07x slower                                                                                                      |
| async_tree_memoization    | 465 ms                                                                                                              | 499 ms: 1.07x slower                                                                                                      |
| async_tree_none           | 386 ms                                                                                                              | 415 ms: 1.08x slower                                                                                                      |
| pyflate                   | 572 ms                                                                                                              | 622 ms: 1.09x slower                                                                                                      |
| pycparser                 | 1.28 sec                                                                                                            | 1.39 sec: 1.09x slower                                                                                                    |
| docutils                  | 2.96 sec                                                                                                            | 3.25 sec: 1.10x slower                                                                                                    |
| unpickle_list             | 6.60 us                                                                                                             | 7.30 us: 1.11x slower                                                                                                     |
| pickle_pure_python        | 397 us                                                                                                              | 441 us: 1.11x slower                                                                                                      |
| generators                | 37.1 ms                                                                                                             | 41.2 ms: 1.11x slower                                                                                                     |
| json_loads                | 34.3 us                                                                                                             | 38.2 us: 1.11x slower                                                                                                     |
| scimark_fft               | 429 ms                                                                                                              | 482 ms: 1.12x slower                                                                                                      |
| mdp                       | 3.32 sec                                                                                                            | 3.74 sec: 1.13x slower                                                                                                    |
| k_core                    | 2.81 sec                                                                                                            | 3.17 sec: 1.13x slower                                                                                                    |
| logging_silent            | 129 ns                                                                                                              | 146 ns: 1.13x slower                                                                                                      |
| unpickle_pure_python      | 273 us                                                                                                              | 308 us: 1.13x slower                                                                                                      |
| json                      | 5.81 ms                                                                                                             | 6.58 ms: 1.13x slower                                                                                                     |
| unpickle                  | 17.9 us                                                                                                             | 20.3 us: 1.13x slower                                                                                                     |
| sphinx                    | 1.16 sec                                                                                                            | 1.32 sec: 1.14x slower                                                                                                    |
| html5lib                  | 65.1 ms                                                                                                             | 74.1 ms: 1.14x slower                                                                                                     |
| pprint_safe_repr          | 965 ms                                                                                                              | 1.10 sec: 1.14x slower                                                                                                    |
| asyncio_tcp_ssl           | 2.16 sec                                                                                                            | 2.46 sec: 1.14x slower                                                                                                    |
| json_dumps                | 14.0 ms                                                                                                             | 16.0 ms: 1.14x slower                                                                                                     |
| scimark_sor               | 150 ms                                                                                                              | 172 ms: 1.15x slower                                                                                                      |
| pprint_pformat            | 1.97 sec                                                                                                            | 2.26 sec: 1.15x slower                                                                                                    |
| sqlglot_v2_optimize       | 64.0 ms                                                                                                             | 73.7 ms: 1.15x slower                                                                                                     |
| dulwich_log               | 51.8 ms                                                                                                             | 59.7 ms: 1.15x slower                                                                                                     |
| spectral_norm             | 121 ms                                                                                                              | 140 ms: 1.16x slower                                                                                                      |
| shortest_path             | 582 ms                                                                                                              | 675 ms: 1.16x slower                                                                                                      |
| float                     | 87.7 ms                                                                                                             | 102 ms: 1.17x slower                                                                                                      |
| async_generators          | 449 ms                                                                                                              | 525 ms: 1.17x slower                                                                                                      |
| connected_components      | 562 ms                                                                                                              | 656 ms: 1.17x slower                                                                                                      |
| xml_etree_generate        | 115 ms                                                                                                              | 135 ms: 1.17x slower                                                                                                      |
| sqlglot_v2_normalize      | 127 ms                                                                                                              | 150 ms: 1.18x slower                                                                                                      |
| pylint                    | 317 ms                                                                                                              | 375 ms: 1.18x slower                                                                                                      |
| many_optionals            | 855 us                                                                                                              | 1.02 ms: 1.19x slower                                                                                                     |
| thrift                    | 967 us                                                                                                              | 1.16 ms: 1.20x slower                                                                                                     |
| python_startup            | 16.3 ms                                                                                                             | 19.5 ms: 1.20x slower                                                                                                     |
| chaos                     | 71.0 ms                                                                                                             | 85.1 ms: 1.20x slower                                                                                                     |
| deepcopy                  | 342 us                                                                                                              | 412 us: 1.20x slower                                                                                                      |
| scimark_sparse_mat_mult   | 6.85 ms                                                                                                             | 8.27 ms: 1.21x slower                                                                                                     |
| logging_simple            | 7.05 us                                                                                                             | 8.54 us: 1.21x slower                                                                                                     |
| subparsers                | 26.1 ms                                                                                                             | 31.7 ms: 1.21x slower                                                                                                     |
| deepcopy_reduce           | 3.59 us                                                                                                             | 4.35 us: 1.21x slower                                                                                                     |
| sympy_sum                 | 153 ms                                                                                                              | 187 ms: 1.22x slower                                                                                                      |
| xml_etree_process         | 80.1 ms                                                                                                             | 98.0 ms: 1.22x slower                                                                                                     |
| 2to3                      | 296 ms                                                                                                              | 363 ms: 1.23x slower                                                                                                      |
| telco                     | 9.50 ms                                                                                                             | 11.7 ms: 1.23x slower                                                                                                     |
| crypto_pyaes              | 90.0 ms                                                                                                             | 111 ms: 1.23x slower                                                                                                      |
| logging_format            | 7.75 us                                                                                                             | 9.57 us: 1.23x slower                                                                                                     |
| go                        | 137 ms                                                                                                              | 171 ms: 1.25x slower                                                                                                      |
| tomli_loads               | 2.46 sec                                                                                                            | 3.09 sec: 1.26x slower                                                                                                    |
| hexiom                    | 7.41 ms                                                                                                             | 9.31 ms: 1.26x slower                                                                                                     |
| unpack_sequence           | 60.7 ns                                                                                                             | 76.3 ns: 1.26x slower                                                                                                     |
| nqueens                   | 102 ms                                                                                                              | 129 ms: 1.26x slower                                                                                                      |
| regex_compile             | 127 ms                                                                                                              | 161 ms: 1.27x slower                                                                                                      |
| sympy_expand              | 467 ms                                                                                                              | 592 ms: 1.27x slower                                                                                                      |
| comprehensions            | 21.2 us                                                                                                             | 26.9 us: 1.27x slower                                                                                                     |
| genshi_xml                | 60.2 ms                                                                                                             | 76.7 ms: 1.27x slower                                                                                                     |
| deltablue                 | 3.90 ms                                                                                                             | 4.98 ms: 1.28x slower                                                                                                     |
| raytrace                  | 318 ms                                                                                                              | 406 ms: 1.28x slower                                                                                                      |
| sympy_integrate           | 20.8 ms                                                                                                             | 26.6 ms: 1.28x slower                                                                                                     |
| deepcopy_memo             | 39.3 us                                                                                                             | 50.4 us: 1.28x slower                                                                                                     |
| fannkuch                  | 507 ms                                                                                                              | 652 ms: 1.29x slower                                                                                                      |
| bpe_tokeniser             | 5.64 sec                                                                                                            | 7.26 sec: 1.29x slower                                                                                                    |
| sqlglot_v2_transpile      | 1.81 ms                                                                                                             | 2.34 ms: 1.29x slower                                                                                                     |
| scimark_lu                | 143 ms                                                                                                              | 187 ms: 1.31x slower                                                                                                      |
| richards                  | 54.0 ms                                                                                                             | 70.6 ms: 1.31x slower                                                                                                     |
| genshi_text               | 27.6 ms                                                                                                             | 36.1 ms: 1.31x slower                                                                                                     |
| scimark_monte_carlo       | 84.1 ms                                                                                                             | 110 ms: 1.31x slower                                                                                                      |
| sqlglot_v2_parse          | 1.44 ms                                                                                                             | 1.92 ms: 1.33x slower                                                                                                     |
| django_template           | 40.4 ms                                                                                                             | 53.7 ms: 1.33x slower                                                                                                     |
| sympy_str                 | 266 ms                                                                                                              | 354 ms: 1.33x slower                                                                                                      |
| sqlalchemy_declarative    | 145 ms                                                                                                              | 194 ms: 1.33x slower                                                                                                      |
| meteor_contest            | 113 ms                                                                                                              | 151 ms: 1.34x slower                                                                                                      |
| typing_runtime_protocols  | 195 us                                                                                                              | 262 us: 1.34x slower                                                                                                      |
| bench_thread_pool         | 1.35 ms                                                                                                             | 1.84 ms: 1.36x slower                                                                                                     |
| sqlalchemy_imperative     | 15.5 ms                                                                                                             | 21.2 ms: 1.37x slower                                                                                                     |
| richards_super            | 59.4 ms                                                                                                             | 82.8 ms: 1.39x slower                                                                                                     |
| python_startup_no_site    | 10.2 ms                                                                                                             | 14.4 ms: 1.41x slower                                                                                                     |
| coverage                  | 98.6 ms                                                                                                             | 142 ms: 1.44x slower                                                                                                      |
| nbody                     | 121 ms                                                                                                              | 186 ms: 1.54x slower                                                                                                      |
| mako                      | 14.2 ms                                                                                                             | 22.1 ms: 1.56x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                               | 1.11x slower                                                                                                              |

Benchmark hidden because not significant (13): pickle, pidigits, coroutines, pickle_list, asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed_tg, regex_dna, regex_effbot, async_tree_io, xml_etree_parse, pathlib, pickle_dict

- Geometric mean (including insignificant results): 1.136x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: 1.21x