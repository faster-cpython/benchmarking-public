# Results vs. 3.13.0b2

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-aarch64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.57x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 516 ms: 1.69x slower                                                    |
| docutils       | 3.10 sec                                                     | 4.15 sec: 1.34x slower                                                  |
| html5lib       | 66.1 ms                                                      | 121 ms: 1.84x slower                                                    |
| tornado_http   | 128 ms                                                       | 200 ms: 1.56x slower                                                    |
| Geometric mean | (ref)                                                        | 1.60x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.35 sec: 1.06x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 871 ms: 1.14x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 696 ms: 1.15x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.44 sec: 1.18x slower                                                  |
| async_tree_none_tg         | 476 ms                                                       | 566 ms: 1.19x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 767 ms: 1.19x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 942 ms: 1.19x slower                                                    |
| async_tree_none            | 492 ms                                                       | 631 ms: 1.28x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.17x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 207 ms: 2.27x slower                                                    |
| nbody          | 114 ms                                                       | 285 ms: 2.50x slower                                                    |
| Geometric mean | (ref)                                                        | 1.79x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.41 ms: 1.13x faster                                                   |
| regex_dna      | 259 ms                                                       | 253 ms: 1.02x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 32.8 ms: 1.05x slower                                                   |
| regex_compile  | 128 ms                                                       | 256 ms: 2.00x slower                                                    |
| Geometric mean | (ref)                                                        | 1.16x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 191 ms                                                       | 177 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 155 ms: 1.06x slower                                                    |
| json_loads           | 32.1 us                                                      | 39.1 us: 1.22x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 17.9 ms: 1.36x slower                                                   |
| xml_etree_generate   | 114 ms                                                       | 162 ms: 1.43x slower                                                    |
| xml_etree_process    | 80.8 ms                                                      | 130 ms: 1.61x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 4.19 sec: 1.63x slower                                                  |
| pickle_pure_python   | 359 us                                                       | 781 us: 2.18x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 550 us: 2.19x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.45x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 17.6 ms: 1.35x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 11.7 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.36x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.4 ms                                                      | 105 ms: 1.74x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 52.8 ms: 1.92x slower                                                   |
| django_template | 42.3 ms                                                      | 82.3 ms: 1.95x slower                                                   |
| mako            | 13.2 ms                                                      | 29.1 ms: 2.21x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.95x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.17 ms                                                      | 3.45 ms: 1.50x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 1.60 ms: 1.46x faster                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 6.14 ms: 1.15x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.41 ms: 1.13x faster                                                   |
| xml_etree_parse            | 191 ms                                                       | 177 ms: 1.08x faster                                                    |
| regex_dna                  | 259 ms                                                       | 253 ms: 1.02x faster                                                    |
| asyncio_websockets         | 657 ms                                                       | 672 ms: 1.02x slower                                                    |
| regex_v8                   | 31.1 ms                                                      | 32.8 ms: 1.05x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 155 ms: 1.06x slower                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.35 sec: 1.06x slower                                                  |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.46 sec: 1.11x slower                                                  |
| asyncio_tcp                | 584 ms                                                       | 660 ms: 1.13x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 871 ms: 1.14x slower                                                    |
| pathlib                    | 22.8 ms                                                      | 26.0 ms: 1.14x slower                                                   |
| async_tree_memoization_tg  | 604 ms                                                       | 696 ms: 1.15x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.44 sec: 1.18x slower                                                  |
| async_tree_none_tg         | 476 ms                                                       | 566 ms: 1.19x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 767 ms: 1.19x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 942 ms: 1.19x slower                                                    |
| json_loads                 | 32.1 us                                                      | 39.1 us: 1.22x slower                                                   |
| json                       | 5.64 ms                                                      | 6.96 ms: 1.23x slower                                                   |
| telco                      | 10.0 ms                                                      | 12.4 ms: 1.23x slower                                                   |
| deepcopy                   | 448 us                                                       | 566 us: 1.26x slower                                                    |
| async_tree_none            | 492 ms                                                       | 631 ms: 1.28x slower                                                    |
| mdp                        | 3.33 sec                                                     | 4.33 sec: 1.30x slower                                                  |
| scimark_fft                | 445 ms                                                       | 593 ms: 1.33x slower                                                    |
| docutils                   | 3.10 sec                                                     | 4.15 sec: 1.34x slower                                                  |
| coroutines                 | 29.0 ms                                                      | 39.0 ms: 1.35x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 8.82 ms: 1.35x slower                                                   |
| python_startup             | 13.0 ms                                                      | 17.6 ms: 1.35x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 11.7 ms: 1.36x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 17.9 ms: 1.36x slower                                                   |
| coverage                   | 98.4 ms                                                      | 135 ms: 1.38x slower                                                    |
| deepcopy_memo              | 50.8 us                                                      | 71.9 us: 1.42x slower                                                   |
| async_generators           | 488 ms                                                       | 692 ms: 1.42x slower                                                    |
| xml_etree_generate         | 114 ms                                                       | 162 ms: 1.43x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.87 ms: 1.49x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 6.07 us: 1.50x slower                                                   |
| pylint                     | 337 ms                                                       | 508 ms: 1.51x slower                                                    |
| meteor_contest             | 113 ms                                                       | 173 ms: 1.52x slower                                                    |
| generators                 | 37.1 ms                                                      | 57.0 ms: 1.53x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 152 ms: 1.53x slower                                                    |
| tornado_http               | 128 ms                                                       | 200 ms: 1.56x slower                                                    |
| xml_etree_process          | 80.8 ms                                                      | 130 ms: 1.61x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 4.19 sec: 1.63x slower                                                  |
| bpe_tokeniser              | 5.83 sec                                                     | 9.52 sec: 1.63x slower                                                  |
| spectral_norm              | 141 ms                                                       | 233 ms: 1.65x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 34.9 ms: 1.68x slower                                                   |
| fannkuch                   | 451 ms                                                       | 758 ms: 1.68x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 2.06 sec: 1.68x slower                                                  |
| 2to3                       | 305 ms                                                       | 516 ms: 1.69x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 334 us: 1.72x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 141 ms: 1.72x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 105 ms: 1.74x slower                                                    |
| thrift                     | 962 us                                                       | 1.69 ms: 1.76x slower                                                   |
| sqlglot_normalize          | 129 ms                                                       | 231 ms: 1.79x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 114 ms: 1.83x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 121 ms: 1.84x slower                                                    |
| pyflate                    | 557 ms                                                       | 1.02 sec: 1.84x slower                                                  |
| pprint_pformat             | 1.93 sec                                                     | 3.64 sec: 1.88x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 1.77 sec: 1.90x slower                                                  |
| genshi_text                | 27.4 ms                                                      | 52.8 ms: 1.92x slower                                                   |
| sympy_str                  | 265 ms                                                       | 514 ms: 1.94x slower                                                    |
| django_template            | 42.3 ms                                                      | 82.3 ms: 1.95x slower                                                   |
| regex_compile              | 128 ms                                                       | 256 ms: 2.00x slower                                                    |
| comprehensions             | 20.5 us                                                      | 41.3 us: 2.01x slower                                                   |
| logging_format             | 7.82 us                                                      | 15.8 us: 2.02x slower                                                   |
| logging_simple             | 7.21 us                                                      | 14.7 us: 2.04x slower                                                   |
| sympy_expand               | 457 ms                                                       | 951 ms: 2.08x slower                                                    |
| logging_silent             | 133 ns                                                       | 285 ns: 2.13x slower                                                    |
| scimark_sor                | 159 ms                                                       | 345 ms: 2.16x slower                                                    |
| richards                   | 55.9 ms                                                      | 121 ms: 2.17x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 179 ms: 2.18x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 781 us: 2.18x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 313 ms: 2.18x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 550 us: 2.19x slower                                                    |
| mako                       | 13.2 ms                                                      | 29.1 ms: 2.21x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 15.8 ms: 2.23x slower                                                   |
| richards_super             | 62.3 ms                                                      | 139 ms: 2.23x slower                                                    |
| float                      | 91.4 ms                                                      | 207 ms: 2.27x slower                                                    |
| chaos                      | 68.3 ms                                                      | 162 ms: 2.37x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 343 ms: 2.42x slower                                                    |
| nbody                      | 114 ms                                                       | 285 ms: 2.50x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 4.29 ms: 2.51x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 3.70 ms: 2.60x slower                                                   |
| raytrace                   | 297 ms                                                       | 826 ms: 2.79x slower                                                    |
| go                         | 161 ms                                                       | 448 ms: 2.79x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 12.8 ms: 3.31x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.57x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.44x
- 95% likely to have a slowdown of 1.40x
- 99% likely to have a slowdown of 1.35x

# Memory
- memory change: 1.16x