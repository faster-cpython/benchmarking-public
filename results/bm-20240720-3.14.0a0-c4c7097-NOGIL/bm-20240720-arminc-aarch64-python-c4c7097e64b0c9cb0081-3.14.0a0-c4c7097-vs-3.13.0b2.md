# Results vs. 3.13.0b2

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: linux-aarch64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.56x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 513 ms: 1.68x slower                                                    |
| docutils       | 3.10 sec                                                     | 4.11 sec: 1.33x slower                                                  |
| html5lib       | 66.1 ms                                                      | 121 ms: 1.83x slower                                                    |
| tornado_http   | 128 ms                                                       | 207 ms: 1.62x slower                                                    |
| Geometric mean | (ref)                                                        | 1.60x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.36 sec: 1.07x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 859 ms: 1.13x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 688 ms: 1.14x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.39 sec: 1.14x slower                                                  |
| async_tree_memoization     | 645 ms                                                       | 739 ms: 1.14x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 912 ms: 1.15x slower                                                    |
| async_tree_none_tg         | 476 ms                                                       | 560 ms: 1.18x slower                                                    |
| async_tree_none            | 492 ms                                                       | 604 ms: 1.23x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 209 ms: 2.29x slower                                                    |
| nbody          | 114 ms                                                       | 290 ms: 2.54x slower                                                    |
| Geometric mean | (ref)                                                        | 1.80x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.43 ms: 1.12x faster                                                   |
| regex_v8       | 31.1 ms                                                      | 32.6 ms: 1.05x slower                                                   |
| regex_compile  | 128 ms                                                       | 254 ms: 1.98x slower                                                    |
| Geometric mean | (ref)                                                        | 1.16x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 191 ms                                                       | 182 ms: 1.05x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 156 ms: 1.07x slower                                                    |
| json_loads           | 32.1 us                                                      | 38.8 us: 1.21x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 17.7 ms: 1.35x slower                                                   |
| xml_etree_generate   | 114 ms                                                       | 157 ms: 1.39x slower                                                    |
| xml_etree_process    | 80.8 ms                                                      | 130 ms: 1.60x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 4.20 sec: 1.64x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 538 us: 2.14x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 773 us: 2.16x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.45x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 17.6 ms: 1.36x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 11.8 ms: 1.38x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.37x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.4 ms                                                      | 104 ms: 1.72x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 52.2 ms: 1.90x slower                                                   |
| django_template | 42.3 ms                                                      | 81.3 ms: 1.92x slower                                                   |
| mako            | 13.2 ms                                                      | 28.9 ms: 2.20x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.93x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.17 ms                                                      | 3.45 ms: 1.50x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 1.60 ms: 1.46x faster                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 6.23 ms: 1.13x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.43 ms: 1.12x faster                                                   |
| xml_etree_parse            | 191 ms                                                       | 182 ms: 1.05x faster                                                    |
| asyncio_websockets         | 657 ms                                                       | 672 ms: 1.02x slower                                                    |
| regex_v8                   | 31.1 ms                                                      | 32.6 ms: 1.05x slower                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.36 sec: 1.07x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                       | 156 ms: 1.07x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.46 sec: 1.11x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 859 ms: 1.13x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 688 ms: 1.14x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.39 sec: 1.14x slower                                                  |
| async_tree_memoization     | 645 ms                                                       | 739 ms: 1.14x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 671 ms: 1.15x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 912 ms: 1.15x slower                                                    |
| pathlib                    | 22.8 ms                                                      | 26.6 ms: 1.17x slower                                                   |
| async_tree_none_tg         | 476 ms                                                       | 560 ms: 1.18x slower                                                    |
| json_loads                 | 32.1 us                                                      | 38.8 us: 1.21x slower                                                   |
| async_tree_none            | 492 ms                                                       | 604 ms: 1.23x slower                                                    |
| deepcopy                   | 448 us                                                       | 553 us: 1.23x slower                                                    |
| json                       | 5.64 ms                                                      | 6.97 ms: 1.24x slower                                                   |
| telco                      | 10.0 ms                                                      | 12.5 ms: 1.25x slower                                                   |
| mdp                        | 3.33 sec                                                     | 4.38 sec: 1.31x slower                                                  |
| coroutines                 | 29.0 ms                                                      | 38.5 ms: 1.33x slower                                                   |
| docutils                   | 3.10 sec                                                     | 4.11 sec: 1.33x slower                                                  |
| coverage                   | 98.4 ms                                                      | 132 ms: 1.34x slower                                                    |
| scimark_fft                | 445 ms                                                       | 599 ms: 1.35x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 17.7 ms: 1.35x slower                                                   |
| python_startup             | 13.0 ms                                                      | 17.6 ms: 1.36x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 8.92 ms: 1.36x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 11.8 ms: 1.38x slower                                                   |
| xml_etree_generate         | 114 ms                                                       | 157 ms: 1.39x slower                                                    |
| async_generators           | 488 ms                                                       | 686 ms: 1.41x slower                                                    |
| deepcopy_memo              | 50.8 us                                                      | 72.8 us: 1.43x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 5.99 us: 1.48x slower                                                   |
| pylint                     | 337 ms                                                       | 502 ms: 1.49x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.87 ms: 1.49x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 149 ms: 1.51x slower                                                    |
| meteor_contest             | 113 ms                                                       | 172 ms: 1.51x slower                                                    |
| generators                 | 37.1 ms                                                      | 57.7 ms: 1.55x slower                                                   |
| xml_etree_process          | 80.8 ms                                                      | 130 ms: 1.60x slower                                                    |
| tornado_http               | 128 ms                                                       | 207 ms: 1.62x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 4.20 sec: 1.64x slower                                                  |
| fannkuch                   | 451 ms                                                       | 740 ms: 1.64x slower                                                    |
| bpe_tokeniser              | 5.83 sec                                                     | 9.57 sec: 1.64x slower                                                  |
| dulwich_log                | 58.5 ms                                                      | 98.3 ms: 1.68x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 35.1 ms: 1.68x slower                                                   |
| 2to3                       | 305 ms                                                       | 513 ms: 1.68x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 2.06 sec: 1.69x slower                                                  |
| spectral_norm              | 141 ms                                                       | 239 ms: 1.69x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 140 ms: 1.71x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 332 us: 1.72x slower                                                    |
| thrift                     | 962 us                                                       | 1.65 ms: 1.72x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 104 ms: 1.72x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 231 ms: 1.79x slower                                                    |
| pyflate                    | 557 ms                                                       | 1.01 sec: 1.82x slower                                                  |
| html5lib                   | 66.1 ms                                                      | 121 ms: 1.83x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 3.59 sec: 1.86x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 1.74 sec: 1.86x slower                                                  |
| sqlglot_optimize           | 62.6 ms                                                      | 117 ms: 1.87x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 52.2 ms: 1.90x slower                                                   |
| django_template            | 42.3 ms                                                      | 81.3 ms: 1.92x slower                                                   |
| sympy_str                  | 265 ms                                                       | 520 ms: 1.96x slower                                                    |
| comprehensions             | 20.5 us                                                      | 40.5 us: 1.97x slower                                                   |
| regex_compile              | 128 ms                                                       | 254 ms: 1.98x slower                                                    |
| logging_format             | 7.82 us                                                      | 15.7 us: 2.01x slower                                                   |
| logging_simple             | 7.21 us                                                      | 14.7 us: 2.04x slower                                                   |
| sympy_expand               | 457 ms                                                       | 953 ms: 2.08x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 172 ms: 2.09x slower                                                    |
| richards                   | 55.9 ms                                                      | 117 ms: 2.09x slower                                                    |
| logging_silent             | 133 ns                                                       | 281 ns: 2.11x slower                                                    |
| scimark_sor                | 159 ms                                                       | 341 ms: 2.14x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 538 us: 2.14x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 773 us: 2.16x slower                                                    |
| mako                       | 13.2 ms                                                      | 28.9 ms: 2.20x slower                                                   |
| richards_super             | 62.3 ms                                                      | 137 ms: 2.20x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 15.6 ms: 2.20x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 317 ms: 2.21x slower                                                    |
| float                      | 91.4 ms                                                      | 209 ms: 2.29x slower                                                    |
| chaos                      | 68.3 ms                                                      | 161 ms: 2.35x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 348 ms: 2.46x slower                                                    |
| nbody                      | 114 ms                                                       | 290 ms: 2.54x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 4.41 ms: 2.58x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 3.83 ms: 2.69x slower                                                   |
| go                         | 161 ms                                                       | 446 ms: 2.77x slower                                                    |
| raytrace                   | 297 ms                                                       | 829 ms: 2.79x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 12.7 ms: 3.28x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.56x slower                                                            |

Benchmark hidden because not significant (2): regex_dna, pidigits
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.44x
- 95% likely to have a slowdown of 1.39x
- 99% likely to have a slowdown of 1.35x

# Memory
- memory change: 1.16x