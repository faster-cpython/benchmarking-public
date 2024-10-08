# Results vs. 3.13.0b2

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-aarch64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.58x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 522 ms: 1.71x slower                                                    |
| docutils       | 3.10 sec                                                     | 4.12 sec: 1.33x slower                                                  |
| html5lib       | 66.1 ms                                                      | 123 ms: 1.86x slower                                                    |
| tornado_http   | 128 ms                                                       | 209 ms: 1.64x slower                                                    |
| Geometric mean | (ref)                                                        | 1.62x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.35 sec: 1.06x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 868 ms: 1.14x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.39 sec: 1.14x slower                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 695 ms: 1.15x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 743 ms: 1.15x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 917 ms: 1.16x slower                                                    |
| async_tree_none_tg         | 476 ms                                                       | 571 ms: 1.20x slower                                                    |
| async_tree_none            | 492 ms                                                       | 612 ms: 1.24x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 209 ms: 2.29x slower                                                    |
| nbody          | 114 ms                                                       | 285 ms: 2.50x slower                                                    |
| Geometric mean | (ref)                                                        | 1.79x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.47 ms: 1.11x faster                                                   |
| regex_dna      | 259 ms                                                       | 256 ms: 1.01x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 33.0 ms: 1.06x slower                                                   |
| regex_compile  | 128 ms                                                       | 258 ms: 2.02x slower                                                    |
| Geometric mean | (ref)                                                        | 1.18x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 191 ms                                                       | 180 ms: 1.06x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 159 ms: 1.09x slower                                                    |
| json_loads           | 32.1 us                                                      | 38.9 us: 1.21x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 18.2 ms: 1.39x slower                                                   |
| xml_etree_generate   | 114 ms                                                       | 163 ms: 1.43x slower                                                    |
| xml_etree_process    | 80.8 ms                                                      | 131 ms: 1.62x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 4.28 sec: 1.66x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 546 us: 2.17x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 787 us: 2.20x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.47x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 18.1 ms: 1.40x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 12.2 ms: 1.42x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.41x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.4 ms                                                      | 109 ms: 1.80x slower                                                    |
| django_template | 42.3 ms                                                      | 84.1 ms: 1.99x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 55.1 ms: 2.01x slower                                                   |
| mako            | 13.2 ms                                                      | 28.9 ms: 2.20x slower                                                   |
| Geometric mean  | (ref)                                                        | 2.00x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.17 ms                                                      | 3.51 ms: 1.47x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 1.62 ms: 1.44x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.47 ms: 1.11x faster                                                   |
| xml_etree_parse            | 191 ms                                                       | 180 ms: 1.06x faster                                                    |
| regex_dna                  | 259 ms                                                       | 256 ms: 1.01x faster                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 7.16 ms: 1.02x slower                                                   |
| asyncio_websockets         | 657 ms                                                       | 672 ms: 1.02x slower                                                    |
| regex_v8                   | 31.1 ms                                                      | 33.0 ms: 1.06x slower                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.35 sec: 1.06x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                       | 159 ms: 1.09x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.47 sec: 1.12x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 868 ms: 1.14x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.39 sec: 1.14x slower                                                  |
| asyncio_tcp                | 584 ms                                                       | 672 ms: 1.15x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 695 ms: 1.15x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 743 ms: 1.15x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 917 ms: 1.16x slower                                                    |
| pathlib                    | 22.8 ms                                                      | 26.6 ms: 1.17x slower                                                   |
| async_tree_none_tg         | 476 ms                                                       | 571 ms: 1.20x slower                                                    |
| json_loads                 | 32.1 us                                                      | 38.9 us: 1.21x slower                                                   |
| async_tree_none            | 492 ms                                                       | 612 ms: 1.24x slower                                                    |
| json                       | 5.64 ms                                                      | 7.04 ms: 1.25x slower                                                   |
| deepcopy                   | 448 us                                                       | 564 us: 1.26x slower                                                    |
| mdp                        | 3.33 sec                                                     | 4.34 sec: 1.30x slower                                                  |
| scimark_fft                | 445 ms                                                       | 582 ms: 1.31x slower                                                    |
| telco                      | 10.0 ms                                                      | 13.1 ms: 1.31x slower                                                   |
| docutils                   | 3.10 sec                                                     | 4.12 sec: 1.33x slower                                                  |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 8.96 ms: 1.37x slower                                                   |
| async_generators           | 488 ms                                                       | 670 ms: 1.37x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 18.2 ms: 1.39x slower                                                   |
| python_startup             | 13.0 ms                                                      | 18.1 ms: 1.40x slower                                                   |
| coverage                   | 98.4 ms                                                      | 138 ms: 1.40x slower                                                    |
| coroutines                 | 29.0 ms                                                      | 41.1 ms: 1.42x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 12.2 ms: 1.42x slower                                                   |
| xml_etree_generate         | 114 ms                                                       | 163 ms: 1.43x slower                                                    |
| deepcopy_memo              | 50.8 us                                                      | 73.0 us: 1.44x slower                                                   |
| meteor_contest             | 113 ms                                                       | 168 ms: 1.48x slower                                                    |
| pylint                     | 337 ms                                                       | 509 ms: 1.51x slower                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 6.10 us: 1.51x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 152 ms: 1.54x slower                                                    |
| generators                 | 37.1 ms                                                      | 57.2 ms: 1.54x slower                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 9.40 sec: 1.61x slower                                                  |
| xml_etree_process          | 80.8 ms                                                      | 131 ms: 1.62x slower                                                    |
| spectral_norm              | 141 ms                                                       | 231 ms: 1.63x slower                                                    |
| tornado_http               | 128 ms                                                       | 209 ms: 1.64x slower                                                    |
| fannkuch                   | 451 ms                                                       | 746 ms: 1.65x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 4.28 sec: 1.66x slower                                                  |
| bench_thread_pool          | 1.26 ms                                                      | 2.11 ms: 1.68x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 2.06 sec: 1.69x slower                                                  |
| sympy_integrate            | 20.9 ms                                                      | 35.2 ms: 1.69x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 139 ms: 1.69x slower                                                    |
| 2to3                       | 305 ms                                                       | 522 ms: 1.71x slower                                                    |
| thrift                     | 962 us                                                       | 1.67 ms: 1.73x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 344 us: 1.78x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 232 ms: 1.80x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 109 ms: 1.80x slower                                                    |
| pyflate                    | 557 ms                                                       | 1.01 sec: 1.82x slower                                                  |
| html5lib                   | 66.1 ms                                                      | 123 ms: 1.86x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 117 ms: 1.87x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 3.66 sec: 1.90x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 1.78 sec: 1.91x slower                                                  |
| sympy_str                  | 265 ms                                                       | 523 ms: 1.97x slower                                                    |
| django_template            | 42.3 ms                                                      | 84.1 ms: 1.99x slower                                                   |
| logging_format             | 7.82 us                                                      | 15.6 us: 1.99x slower                                                   |
| comprehensions             | 20.5 us                                                      | 41.2 us: 2.01x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 55.1 ms: 2.01x slower                                                   |
| logging_simple             | 7.21 us                                                      | 14.5 us: 2.01x slower                                                   |
| regex_compile              | 128 ms                                                       | 258 ms: 2.02x slower                                                    |
| richards                   | 55.9 ms                                                      | 117 ms: 2.10x slower                                                    |
| sympy_expand               | 457 ms                                                       | 971 ms: 2.12x slower                                                    |
| scimark_sor                | 159 ms                                                       | 342 ms: 2.14x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 546 us: 2.17x slower                                                    |
| logging_silent             | 133 ns                                                       | 291 ns: 2.18x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 180 ms: 2.19x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 787 us: 2.20x slower                                                    |
| mako                       | 13.2 ms                                                      | 28.9 ms: 2.20x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 318 ms: 2.22x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 15.7 ms: 2.22x slower                                                   |
| richards_super             | 62.3 ms                                                      | 141 ms: 2.26x slower                                                    |
| float                      | 91.4 ms                                                      | 209 ms: 2.29x slower                                                    |
| chaos                      | 68.3 ms                                                      | 160 ms: 2.34x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 351 ms: 2.48x slower                                                    |
| nbody                      | 114 ms                                                       | 285 ms: 2.50x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 4.37 ms: 2.56x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 3.72 ms: 2.61x slower                                                   |
| raytrace                   | 297 ms                                                       | 820 ms: 2.76x slower                                                    |
| go                         | 161 ms                                                       | 447 ms: 2.78x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 12.7 ms: 3.28x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.58x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.44x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: 1.16x