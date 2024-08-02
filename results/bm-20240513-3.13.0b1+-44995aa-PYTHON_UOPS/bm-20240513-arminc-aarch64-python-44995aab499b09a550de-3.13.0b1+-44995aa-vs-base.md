# Results vs. base

- fork: python
- ref: 44995aab499b09a550de
- machine: linux-aarch64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.15x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-PYTHON_UOPS/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 302 ms                                                                                                              | 360 ms: 1.19x slower                                                                                                            |
| chameleon      | 9.02 ms                                                                                                             | 10.3 ms: 1.14x slower                                                                                                           |
| docutils       | 3.13 sec                                                                                                            | 3.54 sec: 1.13x slower                                                                                                          |
| html5lib       | 68.4 ms                                                                                                             | 75.0 ms: 1.10x slower                                                                                                           |
| Geometric mean | (ref)                                                                                                               | 1.12x slower                                                                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-PYTHON_UOPS/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 472 ms                                                                                                              | 486 ms: 1.03x slower                                                                                                            |
| async_tree_cpu_io_mixed    | 791 ms                                                                                                              | 813 ms: 1.03x slower                                                                                                            |
| async_tree_cpu_io_mixed_tg | 794 ms                                                                                                              | 820 ms: 1.03x slower                                                                                                            |
| async_tree_none            | 491 ms                                                                                                              | 507 ms: 1.03x slower                                                                                                            |
| async_tree_memoization     | 643 ms                                                                                                              | 673 ms: 1.05x slower                                                                                                            |
| Geometric mean             | (ref)                                                                                                               | 1.02x slower                                                                                                                    |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-PYTHON_UOPS/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|
| float          | 90.5 ms                                                                                                             | 116 ms: 1.28x slower                                                                                                            |
| nbody          | 112 ms                                                                                                              | 150 ms: 1.35x slower                                                                                                            |
| Geometric mean | (ref)                                                                                                               | 1.20x slower                                                                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-PYTHON_UOPS/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                                                              | 173 ms: 1.35x slower                                                                                                            |
| Geometric mean | (ref)                                                                                                               | 1.08x slower                                                                                                                    |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-PYTHON_UOPS/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|
| pickle               | 13.6 us                                                                                                             | 13.8 us: 1.02x slower                                                                                                           |
| pickle_list          | 5.12 us                                                                                                             | 5.27 us: 1.03x slower                                                                                                           |
| unpickle_list        | 6.46 us                                                                                                             | 6.73 us: 1.04x slower                                                                                                           |
| xml_etree_iterparse  | 149 ms                                                                                                              | 161 ms: 1.08x slower                                                                                                            |
| xml_etree_process    | 81.0 ms                                                                                                             | 89.8 ms: 1.11x slower                                                                                                           |
| xml_etree_generate   | 113 ms                                                                                                              | 128 ms: 1.13x slower                                                                                                            |
| tomli_loads          | 2.54 sec                                                                                                            | 3.25 sec: 1.28x slower                                                                                                          |
| pickle_pure_python   | 361 us                                                                                                              | 470 us: 1.30x slower                                                                                                            |
| unpickle_pure_python | 251 us                                                                                                              | 367 us: 1.46x slower                                                                                                            |
| Geometric mean       | (ref)                                                                                                               | 1.10x slower                                                                                                                    |

Benchmark hidden because not significant (5): json_loads, unpickle, pickle_dict, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-PYTHON_UOPS/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|
| django_template | 41.3 ms                                                                                                             | 51.0 ms: 1.24x slower                                                                                                           |
| genshi_xml      | 61.0 ms                                                                                                             | 77.7 ms: 1.27x slower                                                                                                           |
| mako            | 13.2 ms                                                                                                             | 17.5 ms: 1.32x slower                                                                                                           |
| genshi_text     | 27.9 ms                                                                                                             | 37.0 ms: 1.33x slower                                                                                                           |
| Geometric mean  | (ref)                                                                                                               | 1.29x slower                                                                                                                    |

All benchmarks:
===============

| Benchmark                  | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-PYTHON_UOPS/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.22 sec                                                                                                            | 2.17 sec: 1.02x faster                                                                                                          |
| pickle                     | 13.6 us                                                                                                             | 13.8 us: 1.02x slower                                                                                                           |
| thrift                     | 967 us                                                                                                              | 986 us: 1.02x slower                                                                                                            |
| asyncio_tcp                | 568 ms                                                                                                              | 581 ms: 1.02x slower                                                                                                            |
| json                       | 5.73 ms                                                                                                             | 5.88 ms: 1.03x slower                                                                                                           |
| async_tree_none_tg         | 472 ms                                                                                                              | 486 ms: 1.03x slower                                                                                                            |
| pickle_list                | 5.12 us                                                                                                             | 5.27 us: 1.03x slower                                                                                                           |
| async_tree_cpu_io_mixed    | 791 ms                                                                                                              | 813 ms: 1.03x slower                                                                                                            |
| async_tree_cpu_io_mixed_tg | 794 ms                                                                                                              | 820 ms: 1.03x slower                                                                                                            |
| async_tree_none            | 491 ms                                                                                                              | 507 ms: 1.03x slower                                                                                                            |
| gc_traversal               | 5.13 ms                                                                                                             | 5.32 ms: 1.04x slower                                                                                                           |
| pathlib                    | 22.9 ms                                                                                                             | 23.9 ms: 1.04x slower                                                                                                           |
| unpickle_list              | 6.46 us                                                                                                             | 6.73 us: 1.04x slower                                                                                                           |
| flaskblogging              | 4.86 ms                                                                                                             | 5.07 ms: 1.04x slower                                                                                                           |
| coverage                   | 97.5 ms                                                                                                             | 102 ms: 1.05x slower                                                                                                            |
| sqlite_synth               | 3.88 us                                                                                                             | 4.06 us: 1.05x slower                                                                                                           |
| async_tree_memoization     | 643 ms                                                                                                              | 673 ms: 1.05x slower                                                                                                            |
| logging_format             | 7.88 us                                                                                                             | 8.28 us: 1.05x slower                                                                                                           |
| generators                 | 37.6 ms                                                                                                             | 39.5 ms: 1.05x slower                                                                                                           |
| logging_simple             | 7.12 us                                                                                                             | 7.49 us: 1.05x slower                                                                                                           |
| coroutines                 | 29.0 ms                                                                                                             | 30.7 ms: 1.06x slower                                                                                                           |
| bench_thread_pool          | 1.27 ms                                                                                                             | 1.36 ms: 1.07x slower                                                                                                           |
| async_generators           | 488 ms                                                                                                              | 524 ms: 1.08x slower                                                                                                            |
| xml_etree_iterparse        | 149 ms                                                                                                              | 161 ms: 1.08x slower                                                                                                            |
| mdp                        | 3.35 sec                                                                                                            | 3.61 sec: 1.08x slower                                                                                                          |
| bench_mp_pool              | 7.16 ms                                                                                                             | 7.77 ms: 1.08x slower                                                                                                           |
| html5lib                   | 68.4 ms                                                                                                             | 75.0 ms: 1.10x slower                                                                                                           |
| aiohttp                    | 1.19 ms                                                                                                             | 1.31 ms: 1.10x slower                                                                                                           |
| gunicorn                   | 1.21 ms                                                                                                             | 1.33 ms: 1.10x slower                                                                                                           |
| xml_etree_process          | 81.0 ms                                                                                                             | 89.8 ms: 1.11x slower                                                                                                           |
| pycparser                  | 1.23 sec                                                                                                            | 1.38 sec: 1.13x slower                                                                                                          |
| docutils                   | 3.13 sec                                                                                                            | 3.54 sec: 1.13x slower                                                                                                          |
| dulwich_log                | 58.7 ms                                                                                                             | 66.4 ms: 1.13x slower                                                                                                           |
| xml_etree_generate         | 113 ms                                                                                                              | 128 ms: 1.13x slower                                                                                                            |
| sympy_expand               | 463 ms                                                                                                              | 525 ms: 1.13x slower                                                                                                            |
| chameleon                  | 9.02 ms                                                                                                             | 10.3 ms: 1.14x slower                                                                                                           |
| mypy2                      | 762 ms                                                                                                              | 873 ms: 1.15x slower                                                                                                            |
| typing_runtime_protocols   | 197 us                                                                                                              | 227 us: 1.15x slower                                                                                                            |
| pylint                     | 340 ms                                                                                                              | 393 ms: 1.16x slower                                                                                                            |
| raytrace                   | 297 ms                                                                                                              | 348 ms: 1.17x slower                                                                                                            |
| sqlglot_optimize           | 62.6 ms                                                                                                             | 73.7 ms: 1.18x slower                                                                                                           |
| sympy_str                  | 270 ms                                                                                                              | 320 ms: 1.18x slower                                                                                                            |
| meteor_contest             | 114 ms                                                                                                              | 136 ms: 1.19x slower                                                                                                            |
| sqlglot_normalize          | 128 ms                                                                                                              | 152 ms: 1.19x slower                                                                                                            |
| 2to3                       | 302 ms                                                                                                              | 360 ms: 1.19x slower                                                                                                            |
| sympy_sum                  | 145 ms                                                                                                              | 173 ms: 1.19x slower                                                                                                            |
| deepcopy_reduce            | 4.04 us                                                                                                             | 4.83 us: 1.19x slower                                                                                                           |
| richards_super             | 62.4 ms                                                                                                             | 76.9 ms: 1.23x slower                                                                                                           |
| django_template            | 41.3 ms                                                                                                             | 51.0 ms: 1.24x slower                                                                                                           |
| go                         | 162 ms                                                                                                              | 201 ms: 1.24x slower                                                                                                            |
| sqlglot_parse              | 1.45 ms                                                                                                             | 1.80 ms: 1.24x slower                                                                                                           |
| pprint_safe_repr           | 953 ms                                                                                                              | 1.20 sec: 1.26x slower                                                                                                          |
| scimark_fft                | 446 ms                                                                                                              | 561 ms: 1.26x slower                                                                                                            |
| sympy_integrate            | 21.0 ms                                                                                                             | 26.4 ms: 1.26x slower                                                                                                           |
| deepcopy                   | 443 us                                                                                                              | 558 us: 1.26x slower                                                                                                            |
| pprint_pformat             | 1.93 sec                                                                                                            | 2.45 sec: 1.27x slower                                                                                                          |
| richards                   | 54.9 ms                                                                                                             | 69.6 ms: 1.27x slower                                                                                                           |
| genshi_xml                 | 61.0 ms                                                                                                             | 77.7 ms: 1.27x slower                                                                                                           |
| scimark_sor                | 158 ms                                                                                                              | 202 ms: 1.28x slower                                                                                                            |
| float                      | 90.5 ms                                                                                                             | 116 ms: 1.28x slower                                                                                                            |
| tomli_loads                | 2.54 sec                                                                                                            | 3.25 sec: 1.28x slower                                                                                                          |
| scimark_sparse_mat_mult    | 6.57 ms                                                                                                             | 8.47 ms: 1.29x slower                                                                                                           |
| fannkuch                   | 463 ms                                                                                                              | 599 ms: 1.29x slower                                                                                                            |
| crypto_pyaes               | 81.2 ms                                                                                                             | 106 ms: 1.30x slower                                                                                                            |
| pickle_pure_python         | 361 us                                                                                                              | 470 us: 1.30x slower                                                                                                            |
| sqlglot_transpile          | 1.72 ms                                                                                                             | 2.25 ms: 1.31x slower                                                                                                           |
| chaos                      | 67.9 ms                                                                                                             | 89.5 ms: 1.32x slower                                                                                                           |
| mako                       | 13.2 ms                                                                                                             | 17.5 ms: 1.32x slower                                                                                                           |
| genshi_text                | 27.9 ms                                                                                                             | 37.0 ms: 1.33x slower                                                                                                           |
| nbody                      | 112 ms                                                                                                              | 150 ms: 1.35x slower                                                                                                            |
| regex_compile              | 128 ms                                                                                                              | 173 ms: 1.35x slower                                                                                                            |
| nqueens                    | 99.0 ms                                                                                                             | 134 ms: 1.36x slower                                                                                                            |
| pyflate                    | 557 ms                                                                                                              | 759 ms: 1.36x slower                                                                                                            |
| deltablue                  | 3.88 ms                                                                                                             | 5.32 ms: 1.37x slower                                                                                                           |
| spectral_norm              | 140 ms                                                                                                              | 194 ms: 1.38x slower                                                                                                            |
| scimark_monte_carlo        | 82.3 ms                                                                                                             | 119 ms: 1.45x slower                                                                                                            |
| unpickle_pure_python       | 251 us                                                                                                              | 367 us: 1.46x slower                                                                                                            |
| logging_silent             | 133 ns                                                                                                              | 199 ns: 1.50x slower                                                                                                            |
| deepcopy_memo              | 50.4 us                                                                                                             | 75.9 us: 1.51x slower                                                                                                           |
| scimark_lu                 | 138 ms                                                                                                              | 213 ms: 1.54x slower                                                                                                            |
| comprehensions             | 20.2 us                                                                                                             | 32.0 us: 1.58x slower                                                                                                           |
| hexiom                     | 7.01 ms                                                                                                             | 11.4 ms: 1.63x slower                                                                                                           |
| Geometric mean             | (ref)                                                                                                               | 1.15x slower                                                                                                                    |

Benchmark hidden because not significant (19): json_loads, create_gc_cycles, regex_effbot, unpickle, async_tree_memoization_tg, regex_dna, python_startup, asyncio_websockets, regex_v8, pickle_dict, python_startup_no_site, pidigits, telco, async_tree_io_tg, xml_etree_parse, async_tree_io, dask, json_dumps, tornado_http

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.01x