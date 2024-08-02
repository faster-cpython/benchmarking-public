# Results vs. base

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-aarch64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                                                            | 359 ms: 1.17x slower                                                                                                          |
| chameleon      | 9.16 ms                                                                                                           | 10.2 ms: 1.12x slower                                                                                                         |
| docutils       | 3.09 sec                                                                                                          | 3.54 sec: 1.15x slower                                                                                                        |
| html5lib       | 65.8 ms                                                                                                           | 74.4 ms: 1.13x slower                                                                                                         |
| tornado_http   | 130 ms                                                                                                            | 138 ms: 1.06x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                             | 1.13x slower                                                                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 600 ms                                                                                                            | 640 ms: 1.07x slower                                                                                                          |
| async_tree_cpu_io_mixed_tg | 756 ms                                                                                                            | 809 ms: 1.07x slower                                                                                                          |
| async_tree_none_tg         | 467 ms                                                                                                            | 501 ms: 1.07x slower                                                                                                          |
| async_tree_memoization     | 647 ms                                                                                                            | 697 ms: 1.08x slower                                                                                                          |
| async_tree_io              | 1.20 sec                                                                                                          | 1.30 sec: 1.08x slower                                                                                                        |
| async_tree_none            | 490 ms                                                                                                            | 529 ms: 1.08x slower                                                                                                          |
| async_tree_cpu_io_mixed    | 784 ms                                                                                                            | 850 ms: 1.08x slower                                                                                                          |
| Geometric mean             | (ref)                                                                                                             | 1.06x slower                                                                                                                  |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| float          | 91.9 ms                                                                                                           | 117 ms: 1.27x slower                                                                                                          |
| nbody          | 113 ms                                                                                                            | 151 ms: 1.33x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                             | 1.20x slower                                                                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 250 ms                                                                                                            | 257 ms: 1.03x slower                                                                                                          |
| regex_compile  | 129 ms                                                                                                            | 171 ms: 1.32x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                             | 1.08x slower                                                                                                                  |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| unpickle             | 19.5 us                                                                                                           | 19.7 us: 1.01x slower                                                                                                         |
| pickle_dict          | 37.3 us                                                                                                           | 37.8 us: 1.01x slower                                                                                                         |
| pickle_list          | 5.24 us                                                                                                           | 5.32 us: 1.02x slower                                                                                                         |
| json_dumps           | 13.3 ms                                                                                                           | 13.7 ms: 1.03x slower                                                                                                         |
| xml_etree_iterparse  | 153 ms                                                                                                            | 162 ms: 1.05x slower                                                                                                          |
| xml_etree_process    | 81.2 ms                                                                                                           | 88.2 ms: 1.09x slower                                                                                                         |
| xml_etree_generate   | 113 ms                                                                                                            | 128 ms: 1.13x slower                                                                                                          |
| tomli_loads          | 2.53 sec                                                                                                          | 3.25 sec: 1.28x slower                                                                                                        |
| pickle_pure_python   | 361 us                                                                                                            | 467 us: 1.29x slower                                                                                                          |
| unpickle_pure_python | 252 us                                                                                                            | 367 us: 1.46x slower                                                                                                          |
| Geometric mean       | (ref)                                                                                                             | 1.09x slower                                                                                                                  |

Benchmark hidden because not significant (4): unpickle_list, xml_etree_parse, json_loads, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                                                                           | 12.8 ms: 1.01x slower                                                                                                         |
| python_startup_no_site | 8.41 ms                                                                                                           | 8.57 ms: 1.02x slower                                                                                                         |
| Geometric mean         | (ref)                                                                                                             | 1.02x slower                                                                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| django_template | 41.6 ms                                                                                                           | 50.1 ms: 1.20x slower                                                                                                         |
| genshi_xml      | 60.8 ms                                                                                                           | 78.5 ms: 1.29x slower                                                                                                         |
| mako            | 13.2 ms                                                                                                           | 17.3 ms: 1.30x slower                                                                                                         |
| genshi_text     | 27.9 ms                                                                                                           | 37.6 ms: 1.35x slower                                                                                                         |
| Geometric mean  | (ref)                                                                                                             | 1.29x slower                                                                                                                  |

All benchmarks:
===============

| Benchmark                  | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| unpickle                   | 19.5 us                                                                                                           | 19.7 us: 1.01x slower                                                                                                         |
| asyncio_tcp_ssl            | 2.21 sec                                                                                                          | 2.23 sec: 1.01x slower                                                                                                        |
| pickle_dict                | 37.3 us                                                                                                           | 37.8 us: 1.01x slower                                                                                                         |
| python_startup             | 12.6 ms                                                                                                           | 12.8 ms: 1.01x slower                                                                                                         |
| pickle_list                | 5.24 us                                                                                                           | 5.32 us: 1.02x slower                                                                                                         |
| python_startup_no_site     | 8.41 ms                                                                                                           | 8.57 ms: 1.02x slower                                                                                                         |
| sqlite_synth               | 3.84 us                                                                                                           | 3.93 us: 1.03x slower                                                                                                         |
| json                       | 5.68 ms                                                                                                           | 5.83 ms: 1.03x slower                                                                                                         |
| asyncio_tcp                | 573 ms                                                                                                            | 588 ms: 1.03x slower                                                                                                          |
| logging_format             | 7.78 us                                                                                                           | 8.01 us: 1.03x slower                                                                                                         |
| regex_dna                  | 250 ms                                                                                                            | 257 ms: 1.03x slower                                                                                                          |
| json_dumps                 | 13.3 ms                                                                                                           | 13.7 ms: 1.03x slower                                                                                                         |
| coverage                   | 97.9 ms                                                                                                           | 101 ms: 1.03x slower                                                                                                          |
| logging_simple             | 7.11 us                                                                                                           | 7.36 us: 1.03x slower                                                                                                         |
| pathlib                    | 21.4 ms                                                                                                           | 22.3 ms: 1.05x slower                                                                                                         |
| xml_etree_iterparse        | 153 ms                                                                                                            | 162 ms: 1.05x slower                                                                                                          |
| dask                       | 368 ms                                                                                                            | 389 ms: 1.06x slower                                                                                                          |
| coroutines                 | 29.0 ms                                                                                                           | 30.8 ms: 1.06x slower                                                                                                         |
| tornado_http               | 130 ms                                                                                                            | 138 ms: 1.06x slower                                                                                                          |
| async_generators           | 483 ms                                                                                                            | 515 ms: 1.07x slower                                                                                                          |
| async_tree_memoization_tg  | 600 ms                                                                                                            | 640 ms: 1.07x slower                                                                                                          |
| async_tree_cpu_io_mixed_tg | 756 ms                                                                                                            | 809 ms: 1.07x slower                                                                                                          |
| async_tree_none_tg         | 467 ms                                                                                                            | 501 ms: 1.07x slower                                                                                                          |
| async_tree_memoization     | 647 ms                                                                                                            | 697 ms: 1.08x slower                                                                                                          |
| async_tree_io              | 1.20 sec                                                                                                          | 1.30 sec: 1.08x slower                                                                                                        |
| async_tree_none            | 490 ms                                                                                                            | 529 ms: 1.08x slower                                                                                                          |
| generators                 | 37.6 ms                                                                                                           | 40.7 ms: 1.08x slower                                                                                                         |
| mdp                        | 3.32 sec                                                                                                          | 3.60 sec: 1.08x slower                                                                                                        |
| async_tree_cpu_io_mixed    | 784 ms                                                                                                            | 850 ms: 1.08x slower                                                                                                          |
| xml_etree_process          | 81.2 ms                                                                                                           | 88.2 ms: 1.09x slower                                                                                                         |
| telco                      | 9.85 ms                                                                                                           | 10.8 ms: 1.10x slower                                                                                                         |
| bench_thread_pool          | 1.27 ms                                                                                                           | 1.39 ms: 1.10x slower                                                                                                         |
| flaskblogging              | 4.74 ms                                                                                                           | 5.22 ms: 1.10x slower                                                                                                         |
| dulwich_log                | 59.4 ms                                                                                                           | 66.1 ms: 1.11x slower                                                                                                         |
| chameleon                  | 9.16 ms                                                                                                           | 10.2 ms: 1.12x slower                                                                                                         |
| xml_etree_generate         | 113 ms                                                                                                            | 128 ms: 1.13x slower                                                                                                          |
| html5lib                   | 65.8 ms                                                                                                           | 74.4 ms: 1.13x slower                                                                                                         |
| typing_runtime_protocols   | 200 us                                                                                                            | 226 us: 1.13x slower                                                                                                          |
| pycparser                  | 1.23 sec                                                                                                          | 1.40 sec: 1.14x slower                                                                                                        |
| docutils                   | 3.09 sec                                                                                                          | 3.54 sec: 1.15x slower                                                                                                        |
| sympy_expand               | 461 ms                                                                                                            | 533 ms: 1.16x slower                                                                                                          |
| sqlglot_normalize          | 128 ms                                                                                                            | 149 ms: 1.17x slower                                                                                                          |
| raytrace                   | 297 ms                                                                                                            | 348 ms: 1.17x slower                                                                                                          |
| pylint                     | 342 ms                                                                                                            | 401 ms: 1.17x slower                                                                                                          |
| 2to3                       | 306 ms                                                                                                            | 359 ms: 1.17x slower                                                                                                          |
| sqlglot_optimize           | 62.1 ms                                                                                                           | 72.9 ms: 1.17x slower                                                                                                         |
| sympy_str                  | 268 ms                                                                                                            | 321 ms: 1.20x slower                                                                                                          |
| meteor_contest             | 112 ms                                                                                                            | 135 ms: 1.20x slower                                                                                                          |
| django_template            | 41.6 ms                                                                                                           | 50.1 ms: 1.20x slower                                                                                                         |
| deepcopy_reduce            | 4.02 us                                                                                                           | 4.88 us: 1.21x slower                                                                                                         |
| sympy_sum                  | 144 ms                                                                                                            | 176 ms: 1.22x slower                                                                                                          |
| bench_mp_pool              | 7.02 ms                                                                                                           | 8.62 ms: 1.23x slower                                                                                                         |
| richards_super             | 60.4 ms                                                                                                           | 74.7 ms: 1.24x slower                                                                                                         |
| deepcopy                   | 445 us                                                                                                            | 553 us: 1.24x slower                                                                                                          |
| scimark_fft                | 446 ms                                                                                                            | 558 ms: 1.25x slower                                                                                                          |
| sympy_integrate            | 21.3 ms                                                                                                           | 26.6 ms: 1.25x slower                                                                                                         |
| scimark_sparse_mat_mult    | 6.65 ms                                                                                                           | 8.35 ms: 1.26x slower                                                                                                         |
| go                         | 160 ms                                                                                                            | 202 ms: 1.26x slower                                                                                                          |
| scimark_sor                | 159 ms                                                                                                            | 202 ms: 1.27x slower                                                                                                          |
| float                      | 91.9 ms                                                                                                           | 117 ms: 1.27x slower                                                                                                          |
| richards                   | 53.7 ms                                                                                                           | 68.2 ms: 1.27x slower                                                                                                         |
| tomli_loads                | 2.53 sec                                                                                                          | 3.25 sec: 1.28x slower                                                                                                        |
| sqlglot_parse              | 1.40 ms                                                                                                           | 1.81 ms: 1.29x slower                                                                                                         |
| crypto_pyaes               | 82.0 ms                                                                                                           | 106 ms: 1.29x slower                                                                                                          |
| genshi_xml                 | 60.8 ms                                                                                                           | 78.5 ms: 1.29x slower                                                                                                         |
| pickle_pure_python         | 361 us                                                                                                            | 467 us: 1.29x slower                                                                                                          |
| pprint_pformat             | 1.91 sec                                                                                                          | 2.47 sec: 1.30x slower                                                                                                        |
| pprint_safe_repr           | 930 ms                                                                                                            | 1.21 sec: 1.30x slower                                                                                                        |
| fannkuch                   | 460 ms                                                                                                            | 598 ms: 1.30x slower                                                                                                          |
| mako                       | 13.2 ms                                                                                                           | 17.3 ms: 1.30x slower                                                                                                         |
| sqlglot_transpile          | 1.73 ms                                                                                                           | 2.26 ms: 1.31x slower                                                                                                         |
| chaos                      | 67.9 ms                                                                                                           | 89.4 ms: 1.32x slower                                                                                                         |
| regex_compile              | 129 ms                                                                                                            | 171 ms: 1.32x slower                                                                                                          |
| nbody                      | 113 ms                                                                                                            | 151 ms: 1.33x slower                                                                                                          |
| genshi_text                | 27.9 ms                                                                                                           | 37.6 ms: 1.35x slower                                                                                                         |
| deltablue                  | 3.90 ms                                                                                                           | 5.31 ms: 1.36x slower                                                                                                         |
| pyflate                    | 557 ms                                                                                                            | 760 ms: 1.37x slower                                                                                                          |
| spectral_norm              | 141 ms                                                                                                            | 194 ms: 1.38x slower                                                                                                          |
| nqueens                    | 98.0 ms                                                                                                           | 136 ms: 1.39x slower                                                                                                          |
| unpickle_pure_python       | 252 us                                                                                                            | 367 us: 1.46x slower                                                                                                          |
| scimark_monte_carlo        | 81.1 ms                                                                                                           | 119 ms: 1.47x slower                                                                                                          |
| logging_silent             | 134 ns                                                                                                            | 197 ns: 1.47x slower                                                                                                          |
| deepcopy_memo              | 50.1 us                                                                                                           | 75.9 us: 1.51x slower                                                                                                         |
| scimark_lu                 | 137 ms                                                                                                            | 211 ms: 1.54x slower                                                                                                          |
| comprehensions             | 20.4 us                                                                                                           | 31.8 us: 1.56x slower                                                                                                         |
| hexiom                     | 7.07 ms                                                                                                           | 11.3 ms: 1.60x slower                                                                                                         |
| Geometric mean             | (ref)                                                                                                             | 1.16x slower                                                                                                                  |

Benchmark hidden because not significant (12): async_tree_io_tg, unpickle_list, asyncio_websockets, regex_v8, xml_etree_parse, create_gc_cycles, json_loads, regex_effbot, pidigits, pickle, gc_traversal, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 1.02x