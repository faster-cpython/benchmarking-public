# Results vs. base

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-aarch64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.150x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 314 ms                                                                                                              | 376 ms: 1.20x slower                                                                                                      |
| docutils       | 3.05 sec                                                                                                            | 3.33 sec: 1.09x slower                                                                                                    |
| html5lib       | 64.6 ms                                                                                                             | 77.0 ms: 1.19x slower                                                                                                     |
| sphinx         | 1.18 sec                                                                                                            | 1.37 sec: 1.16x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.16x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|---------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 681 ms                                                                                                              | 709 ms: 1.04x slower                                                                                                      |
| async_tree_io             | 929 ms                                                                                                              | 968 ms: 1.04x slower                                                                                                      |
| async_tree_memoization_tg | 478 ms                                                                                                              | 499 ms: 1.04x slower                                                                                                      |
| async_tree_none_tg        | 386 ms                                                                                                              | 403 ms: 1.05x slower                                                                                                      |
| coroutines                | 28.5 ms                                                                                                             | 31.0 ms: 1.08x slower                                                                                                     |
| async_tree_memoization    | 488 ms                                                                                                              | 532 ms: 1.09x slower                                                                                                      |
| asyncio_tcp               | 558 ms                                                                                                              | 608 ms: 1.09x slower                                                                                                      |
| async_tree_none           | 388 ms                                                                                                              | 434 ms: 1.12x slower                                                                                                      |
| asyncio_tcp_ssl           | 2.25 sec                                                                                                            | 2.56 sec: 1.14x slower                                                                                                    |
| async_generators          | 459 ms                                                                                                              | 540 ms: 1.18x slower                                                                                                      |
| Geometric mean            | (ref)                                                                                                               | 1.07x slower                                                                                                              |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 87.4 ms                                                                                                             | 103 ms: 1.17x slower                                                                                                      |
| nbody          | 123 ms                                                                                                              | 185 ms: 1.51x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.21x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                                                              | 163 ms: 1.27x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.05x slower                                                                                                              |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 148 ms                                                                                                              | 131 ms: 1.13x faster                                                                                                      |
| pickle_list          | 5.73 us                                                                                                             | 6.08 us: 1.06x slower                                                                                                     |
| unpickle_list        | 6.87 us                                                                                                             | 7.60 us: 1.11x slower                                                                                                     |
| json_loads           | 35.9 us                                                                                                             | 40.5 us: 1.13x slower                                                                                                     |
| unpickle             | 18.2 us                                                                                                             | 20.7 us: 1.14x slower                                                                                                     |
| pickle_pure_python   | 397 us                                                                                                              | 462 us: 1.17x slower                                                                                                      |
| unpickle_pure_python | 276 us                                                                                                              | 323 us: 1.17x slower                                                                                                      |
| json_dumps           | 13.9 ms                                                                                                             | 17.0 ms: 1.22x slower                                                                                                     |
| tomli_loads          | 2.56 sec                                                                                                            | 3.15 sec: 1.23x slower                                                                                                    |
| xml_etree_generate   | 118 ms                                                                                                              | 146 ms: 1.25x slower                                                                                                      |
| xml_etree_process    | 82.6 ms                                                                                                             | 104 ms: 1.25x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.12x slower                                                                                                              |

Benchmark hidden because not significant (3): xml_etree_parse, pickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.4 ms                                                                                                             | 20.1 ms: 1.23x slower                                                                                                     |
| python_startup_no_site | 9.05 ms                                                                                                             | 12.3 ms: 1.36x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.29x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 64.9 ms                                                                                                             | 79.5 ms: 1.23x slower                                                                                                     |
| django_template | 39.4 ms                                                                                                             | 54.3 ms: 1.38x slower                                                                                                     |
| genshi_text     | 27.5 ms                                                                                                             | 38.0 ms: 1.38x slower                                                                                                     |
| mako            | 14.1 ms                                                                                                             | 22.6 ms: 1.60x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.39x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                 | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|---------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool             | 7.33 sec                                                                                                            | 56.7 ms: 129.13x faster                                                                                                   |
| gc_traversal              | 7.33 ms                                                                                                             | 2.67 ms: 2.75x faster                                                                                                     |
| create_gc_cycles          | 3.72 ms                                                                                                             | 2.09 ms: 1.78x faster                                                                                                     |
| sqlite_synth              | 4.20 us                                                                                                             | 3.62 us: 1.16x faster                                                                                                     |
| xml_etree_iterparse       | 148 ms                                                                                                              | 131 ms: 1.13x faster                                                                                                      |
| async_tree_cpu_io_mixed   | 681 ms                                                                                                              | 709 ms: 1.04x slower                                                                                                      |
| async_tree_io             | 929 ms                                                                                                              | 968 ms: 1.04x slower                                                                                                      |
| async_tree_memoization_tg | 478 ms                                                                                                              | 499 ms: 1.04x slower                                                                                                      |
| async_tree_none_tg        | 386 ms                                                                                                              | 403 ms: 1.05x slower                                                                                                      |
| pickle_list               | 5.73 us                                                                                                             | 6.08 us: 1.06x slower                                                                                                     |
| pathlib                   | 23.0 ms                                                                                                             | 24.3 ms: 1.06x slower                                                                                                     |
| unpack_sequence           | 72.2 ns                                                                                                             | 77.4 ns: 1.07x slower                                                                                                     |
| coroutines                | 28.5 ms                                                                                                             | 31.0 ms: 1.08x slower                                                                                                     |
| async_tree_memoization    | 488 ms                                                                                                              | 532 ms: 1.09x slower                                                                                                      |
| asyncio_tcp               | 558 ms                                                                                                              | 608 ms: 1.09x slower                                                                                                      |
| json                      | 6.06 ms                                                                                                             | 6.63 ms: 1.09x slower                                                                                                     |
| k_core                    | 2.92 sec                                                                                                            | 3.20 sec: 1.09x slower                                                                                                    |
| docutils                  | 3.05 sec                                                                                                            | 3.33 sec: 1.09x slower                                                                                                    |
| unpickle_list             | 6.87 us                                                                                                             | 7.60 us: 1.11x slower                                                                                                     |
| logging_silent            | 135 ns                                                                                                              | 149 ns: 1.11x slower                                                                                                      |
| pycparser                 | 1.30 sec                                                                                                            | 1.44 sec: 1.11x slower                                                                                                    |
| async_tree_none           | 388 ms                                                                                                              | 434 ms: 1.12x slower                                                                                                      |
| json_loads                | 35.9 us                                                                                                             | 40.5 us: 1.13x slower                                                                                                     |
| spectral_norm             | 126 ms                                                                                                              | 142 ms: 1.13x slower                                                                                                      |
| asyncio_tcp_ssl           | 2.25 sec                                                                                                            | 2.56 sec: 1.14x slower                                                                                                    |
| unpickle                  | 18.2 us                                                                                                             | 20.7 us: 1.14x slower                                                                                                     |
| mdp                       | 3.44 sec                                                                                                            | 3.92 sec: 1.14x slower                                                                                                    |
| generators                | 37.6 ms                                                                                                             | 43.2 ms: 1.15x slower                                                                                                     |
| scimark_sor               | 155 ms                                                                                                              | 178 ms: 1.15x slower                                                                                                      |
| pyflate                   | 564 ms                                                                                                              | 651 ms: 1.15x slower                                                                                                      |
| sphinx                    | 1.18 sec                                                                                                            | 1.37 sec: 1.16x slower                                                                                                    |
| scimark_fft               | 429 ms                                                                                                              | 498 ms: 1.16x slower                                                                                                      |
| pickle_pure_python        | 397 us                                                                                                              | 462 us: 1.17x slower                                                                                                      |
| unpickle_pure_python      | 276 us                                                                                                              | 323 us: 1.17x slower                                                                                                      |
| float                     | 87.4 ms                                                                                                             | 103 ms: 1.17x slower                                                                                                      |
| async_generators          | 459 ms                                                                                                              | 540 ms: 1.18x slower                                                                                                      |
| dulwich_log               | 60.3 ms                                                                                                             | 70.9 ms: 1.18x slower                                                                                                     |
| pprint_safe_repr          | 978 ms                                                                                                              | 1.16 sec: 1.18x slower                                                                                                    |
| pprint_pformat            | 2.03 sec                                                                                                            | 2.40 sec: 1.18x slower                                                                                                    |
| deepcopy                  | 361 us                                                                                                              | 430 us: 1.19x slower                                                                                                      |
| html5lib                  | 64.6 ms                                                                                                             | 77.0 ms: 1.19x slower                                                                                                     |
| 2to3                      | 314 ms                                                                                                              | 376 ms: 1.20x slower                                                                                                      |
| logging_simple            | 7.47 us                                                                                                             | 9.01 us: 1.21x slower                                                                                                     |
| sqlglot_normalize         | 128 ms                                                                                                              | 154 ms: 1.21x slower                                                                                                      |
| sqlglot_optimize          | 66.2 ms                                                                                                             | 80.2 ms: 1.21x slower                                                                                                     |
| shortest_path             | 575 ms                                                                                                              | 696 ms: 1.21x slower                                                                                                      |
| logging_format            | 8.03 us                                                                                                             | 9.79 us: 1.22x slower                                                                                                     |
| json_dumps                | 13.9 ms                                                                                                             | 17.0 ms: 1.22x slower                                                                                                     |
| genshi_xml                | 64.9 ms                                                                                                             | 79.5 ms: 1.23x slower                                                                                                     |
| python_startup            | 16.4 ms                                                                                                             | 20.1 ms: 1.23x slower                                                                                                     |
| tomli_loads               | 2.56 sec                                                                                                            | 3.15 sec: 1.23x slower                                                                                                    |
| comprehensions            | 21.5 us                                                                                                             | 26.4 us: 1.23x slower                                                                                                     |
| connected_components      | 543 ms                                                                                                              | 669 ms: 1.23x slower                                                                                                      |
| telco                     | 9.81 ms                                                                                                             | 12.1 ms: 1.23x slower                                                                                                     |
| subparsers                | 26.3 ms                                                                                                             | 32.5 ms: 1.24x slower                                                                                                     |
| deepcopy_reduce           | 3.83 us                                                                                                             | 4.75 us: 1.24x slower                                                                                                     |
| go                        | 142 ms                                                                                                              | 177 ms: 1.24x slower                                                                                                      |
| xml_etree_generate        | 118 ms                                                                                                              | 146 ms: 1.25x slower                                                                                                      |
| hexiom                    | 7.49 ms                                                                                                             | 9.37 ms: 1.25x slower                                                                                                     |
| xml_etree_process         | 82.6 ms                                                                                                             | 104 ms: 1.25x slower                                                                                                      |
| regex_compile             | 129 ms                                                                                                              | 163 ms: 1.27x slower                                                                                                      |
| thrift                    | 978 us                                                                                                              | 1.25 ms: 1.27x slower                                                                                                     |
| chaos                     | 69.7 ms                                                                                                             | 89.0 ms: 1.28x slower                                                                                                     |
| raytrace                  | 326 ms                                                                                                              | 416 ms: 1.28x slower                                                                                                      |
| pylint                    | 304 ms                                                                                                              | 389 ms: 1.28x slower                                                                                                      |
| nqueens                   | 104 ms                                                                                                              | 133 ms: 1.29x slower                                                                                                      |
| sympy_sum                 | 148 ms                                                                                                              | 190 ms: 1.29x slower                                                                                                      |
| many_optionals            | 853 us                                                                                                              | 1.10 ms: 1.29x slower                                                                                                     |
| crypto_pyaes              | 86.7 ms                                                                                                             | 112 ms: 1.29x slower                                                                                                      |
| sympy_expand              | 474 ms                                                                                                              | 613 ms: 1.29x slower                                                                                                      |
| deltablue                 | 4.03 ms                                                                                                             | 5.24 ms: 1.30x slower                                                                                                     |
| sympy_str                 | 281 ms                                                                                                              | 367 ms: 1.30x slower                                                                                                      |
| deepcopy_memo             | 40.6 us                                                                                                             | 53.0 us: 1.31x slower                                                                                                     |
| scimark_sparse_mat_mult   | 6.32 ms                                                                                                             | 8.30 ms: 1.31x slower                                                                                                     |
| meteor_contest            | 120 ms                                                                                                              | 157 ms: 1.31x slower                                                                                                      |
| bpe_tokeniser             | 5.77 sec                                                                                                            | 7.60 sec: 1.32x slower                                                                                                    |
| scimark_monte_carlo       | 85.9 ms                                                                                                             | 113 ms: 1.32x slower                                                                                                      |
| sympy_integrate           | 21.9 ms                                                                                                             | 28.8 ms: 1.32x slower                                                                                                     |
| sqlalchemy_declarative    | 145 ms                                                                                                              | 194 ms: 1.33x slower                                                                                                      |
| typing_runtime_protocols  | 209 us                                                                                                              | 281 us: 1.34x slower                                                                                                      |
| scimark_lu                | 141 ms                                                                                                              | 192 ms: 1.36x slower                                                                                                      |
| sqlglot_transpile         | 1.79 ms                                                                                                             | 2.43 ms: 1.36x slower                                                                                                     |
| python_startup_no_site    | 9.05 ms                                                                                                             | 12.3 ms: 1.36x slower                                                                                                     |
| coverage                  | 98.7 ms                                                                                                             | 135 ms: 1.37x slower                                                                                                      |
| django_template           | 39.4 ms                                                                                                             | 54.3 ms: 1.38x slower                                                                                                     |
| fannkuch                  | 494 ms                                                                                                              | 681 ms: 1.38x slower                                                                                                      |
| genshi_text               | 27.5 ms                                                                                                             | 38.0 ms: 1.38x slower                                                                                                     |
| richards                  | 53.3 ms                                                                                                             | 73.9 ms: 1.39x slower                                                                                                     |
| sqlglot_parse             | 1.44 ms                                                                                                             | 2.02 ms: 1.41x slower                                                                                                     |
| richards_super            | 59.1 ms                                                                                                             | 83.7 ms: 1.42x slower                                                                                                     |
| bench_thread_pool         | 1.32 ms                                                                                                             | 1.88 ms: 1.42x slower                                                                                                     |
| sqlalchemy_imperative     | 15.2 ms                                                                                                             | 21.8 ms: 1.43x slower                                                                                                     |
| nbody                     | 123 ms                                                                                                              | 185 ms: 1.51x slower                                                                                                      |
| mako                      | 14.1 ms                                                                                                             | 22.6 ms: 1.60x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                               | 1.12x slower                                                                                                              |

Benchmark hidden because not significant (10): regex_dna, regex_effbot, async_tree_io_tg, xml_etree_parse, async_tree_cpu_io_mixed_tg, regex_v8, pidigits, asyncio_websockets, pickle, pickle_dict

- Geometric mean (including insignificant results): 1.150x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.16x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: 1.20x