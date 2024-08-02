# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: linux-aarch64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 370 ms: 1.21x slower                                                              |
| docutils       | 3.10 sec                                                     | 3.74 sec: 1.21x slower                                                            |
| html5lib       | 66.1 ms                                                      | 70.9 ms: 1.07x slower                                                             |
| tornado_http   | 128 ms                                                       | 139 ms: 1.09x slower                                                              |
| Geometric mean | (ref)                                                        | 1.14x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.14x faster                                                            |
| async_tree_none_tg         | 476 ms                                                       | 423 ms: 1.13x faster                                                              |
| async_tree_memoization_tg  | 604 ms                                                       | 543 ms: 1.11x faster                                                              |
| async_tree_none            | 492 ms                                                       | 443 ms: 1.11x faster                                                              |
| async_tree_memoization     | 645 ms                                                       | 588 ms: 1.10x faster                                                              |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 712 ms: 1.07x faster                                                              |
| async_tree_io              | 1.22 sec                                                     | 1.16 sec: 1.06x faster                                                            |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 754 ms: 1.05x faster                                                              |
| Geometric mean             | (ref)                                                        | 1.10x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 116 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.0 ms: 1.04x faster                                                             |
| regex_compile  | 128 ms                                                       | 182 ms: 1.43x slower                                                              |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                      |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_loads           | 32.1 us                                                      | 32.9 us: 1.02x slower                                                             |
| tomli_loads          | 2.57 sec                                                     | 2.66 sec: 1.03x slower                                                            |
| unpickle_pure_python | 251 us                                                       | 277 us: 1.10x slower                                                              |
| pickle_pure_python   | 359 us                                                       | 398 us: 1.11x slower                                                              |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                      |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_process, json_dumps, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                             |
| python_startup_no_site | 8.60 ms                                                      | 8.88 ms: 1.03x slower                                                             |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                             |
| django_template | 42.3 ms                                                      | 50.6 ms: 1.20x slower                                                             |
| genshi_text     | 27.4 ms                                                      | 33.2 ms: 1.21x slower                                                             |
| genshi_xml      | 60.4 ms                                                      | 75.3 ms: 1.25x slower                                                             |
| Geometric mean  | (ref)                                                        | 1.15x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.9 us: 1.30x faster                                                             |
| deepcopy                   | 448 us                                                       | 382 us: 1.17x faster                                                              |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.14x faster                                                            |
| async_tree_none_tg         | 476 ms                                                       | 423 ms: 1.13x faster                                                              |
| async_tree_memoization_tg  | 604 ms                                                       | 543 ms: 1.11x faster                                                              |
| async_tree_none            | 492 ms                                                       | 443 ms: 1.11x faster                                                              |
| async_tree_memoization     | 645 ms                                                       | 588 ms: 1.10x faster                                                              |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 712 ms: 1.07x faster                                                              |
| async_tree_io              | 1.22 sec                                                     | 1.16 sec: 1.06x faster                                                            |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 754 ms: 1.05x faster                                                              |
| regex_v8                   | 31.1 ms                                                      | 30.0 ms: 1.04x faster                                                             |
| pathlib                    | 22.8 ms                                                      | 22.0 ms: 1.03x faster                                                             |
| coroutines                 | 29.0 ms                                                      | 28.2 ms: 1.03x faster                                                             |
| mako                       | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                             |
| gc_traversal               | 5.17 ms                                                      | 5.09 ms: 1.02x faster                                                             |
| richards                   | 55.9 ms                                                      | 55.0 ms: 1.02x faster                                                             |
| richards_super             | 62.3 ms                                                      | 61.6 ms: 1.01x faster                                                             |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                             |
| logging_silent             | 133 ns                                                       | 135 ns: 1.01x slower                                                              |
| bpe_tokeniser              | 5.83 sec                                                     | 5.92 sec: 1.02x slower                                                            |
| nbody                      | 114 ms                                                       | 116 ms: 1.02x slower                                                              |
| spectral_norm              | 141 ms                                                       | 144 ms: 1.02x slower                                                              |
| logging_simple             | 7.21 us                                                      | 7.37 us: 1.02x slower                                                             |
| json                       | 5.64 ms                                                      | 5.77 ms: 1.02x slower                                                             |
| json_loads                 | 32.1 us                                                      | 32.9 us: 1.02x slower                                                             |
| coverage                   | 98.4 ms                                                      | 101 ms: 1.03x slower                                                              |
| logging_format             | 7.82 us                                                      | 8.05 us: 1.03x slower                                                             |
| python_startup_no_site     | 8.60 ms                                                      | 8.88 ms: 1.03x slower                                                             |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.29 sec: 1.03x slower                                                            |
| tomli_loads                | 2.57 sec                                                     | 2.66 sec: 1.03x slower                                                            |
| scimark_fft                | 445 ms                                                       | 462 ms: 1.04x slower                                                              |
| deepcopy_reduce            | 4.04 us                                                      | 4.22 us: 1.04x slower                                                             |
| meteor_contest             | 113 ms                                                       | 119 ms: 1.05x slower                                                              |
| async_generators           | 488 ms                                                       | 511 ms: 1.05x slower                                                              |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.87 ms: 1.05x slower                                                             |
| mdp                        | 3.33 sec                                                     | 3.49 sec: 1.05x slower                                                            |
| dask                       | 370 ms                                                       | 391 ms: 1.06x slower                                                              |
| fannkuch                   | 451 ms                                                       | 477 ms: 1.06x slower                                                              |
| bench_thread_pool          | 1.26 ms                                                      | 1.33 ms: 1.06x slower                                                             |
| telco                      | 10.0 ms                                                      | 10.7 ms: 1.06x slower                                                             |
| html5lib                   | 66.1 ms                                                      | 70.9 ms: 1.07x slower                                                             |
| tornado_http               | 128 ms                                                       | 139 ms: 1.09x slower                                                              |
| scimark_sor                | 159 ms                                                       | 173 ms: 1.09x slower                                                              |
| scimark_monte_carlo        | 82.3 ms                                                      | 89.8 ms: 1.09x slower                                                             |
| typing_runtime_protocols   | 193 us                                                       | 212 us: 1.09x slower                                                              |
| unpickle_pure_python       | 251 us                                                       | 277 us: 1.10x slower                                                              |
| crypto_pyaes               | 82.0 ms                                                      | 90.3 ms: 1.10x slower                                                             |
| pyflate                    | 557 ms                                                       | 616 ms: 1.11x slower                                                              |
| pickle_pure_python         | 359 us                                                       | 398 us: 1.11x slower                                                              |
| asyncio_tcp                | 584 ms                                                       | 653 ms: 1.12x slower                                                              |
| raytrace                   | 297 ms                                                       | 332 ms: 1.12x slower                                                              |
| bench_mp_pool              | 7.03 ms                                                      | 7.89 ms: 1.12x slower                                                             |
| go                         | 161 ms                                                       | 182 ms: 1.13x slower                                                              |
| deltablue                  | 3.88 ms                                                      | 4.44 ms: 1.15x slower                                                             |
| sqlglot_optimize           | 62.6 ms                                                      | 72.0 ms: 1.15x slower                                                             |
| sqlglot_normalize          | 129 ms                                                       | 149 ms: 1.16x slower                                                              |
| sqlglot_parse              | 1.42 ms                                                      | 1.67 ms: 1.17x slower                                                             |
| comprehensions             | 20.5 us                                                      | 24.1 us: 1.17x slower                                                             |
| pycparser                  | 1.22 sec                                                     | 1.45 sec: 1.19x slower                                                            |
| django_template            | 42.3 ms                                                      | 50.6 ms: 1.20x slower                                                             |
| docutils                   | 3.10 sec                                                     | 3.74 sec: 1.21x slower                                                            |
| genshi_text                | 27.4 ms                                                      | 33.2 ms: 1.21x slower                                                             |
| 2to3                       | 305 ms                                                       | 370 ms: 1.21x slower                                                              |
| sqlglot_transpile          | 1.71 ms                                                      | 2.13 ms: 1.25x slower                                                             |
| genshi_xml                 | 60.4 ms                                                      | 75.3 ms: 1.25x slower                                                             |
| nqueens                    | 98.9 ms                                                      | 124 ms: 1.26x slower                                                              |
| pprint_pformat             | 1.93 sec                                                     | 2.43 sec: 1.26x slower                                                            |
| pprint_safe_repr           | 933 ms                                                       | 1.18 sec: 1.26x slower                                                            |
| scimark_lu                 | 141 ms                                                       | 180 ms: 1.27x slower                                                              |
| chaos                      | 68.3 ms                                                      | 87.7 ms: 1.28x slower                                                             |
| sympy_expand               | 457 ms                                                       | 595 ms: 1.30x slower                                                              |
| pylint                     | 337 ms                                                       | 442 ms: 1.31x slower                                                              |
| sympy_str                  | 265 ms                                                       | 350 ms: 1.32x slower                                                              |
| sympy_integrate            | 20.9 ms                                                      | 27.7 ms: 1.33x slower                                                             |
| hexiom                     | 7.08 ms                                                      | 9.78 ms: 1.38x slower                                                             |
| sympy_sum                  | 144 ms                                                       | 203 ms: 1.41x slower                                                              |
| regex_compile              | 128 ms                                                       | 182 ms: 1.43x slower                                                              |
| generators                 | 37.1 ms                                                      | 57.4 ms: 1.54x slower                                                             |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                      |

Benchmark hidden because not significant (12): xml_etree_parse, xml_etree_process, regex_effbot, regex_dna, json_dumps, thrift, pidigits, float, asyncio_websockets, xml_etree_generate, xml_etree_iterparse, create_gc_cycles
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.09x