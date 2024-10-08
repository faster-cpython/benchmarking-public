# Results vs. 3.13.0b2

- fork: python
- ref: db6f5e193315a3bbfa7b
- machine: linux-aarch64
- commit hash: db6f5e1
- commit date: 2024-08-13
- overall geometric mean: 1.58x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 517 ms: 1.70x slower                                                    |
| docutils       | 3.10 sec                                                     | 4.11 sec: 1.33x slower                                                  |
| html5lib       | 66.1 ms                                                      | 121 ms: 1.84x slower                                                    |
| tornado_http   | 128 ms                                                       | 208 ms: 1.62x slower                                                    |
| Geometric mean | (ref)                                                        | 1.61x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.35 sec: 1.06x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 872 ms: 1.14x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 695 ms: 1.15x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.41 sec: 1.15x slower                                                  |
| async_tree_memoization     | 645 ms                                                       | 746 ms: 1.16x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 917 ms: 1.16x slower                                                    |
| async_tree_none_tg         | 476 ms                                                       | 565 ms: 1.19x slower                                                    |
| async_tree_none            | 492 ms                                                       | 608 ms: 1.23x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 212 ms: 2.32x slower                                                    |
| nbody          | 114 ms                                                       | 286 ms: 2.50x slower                                                    |
| Geometric mean | (ref)                                                        | 1.80x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.41 ms: 1.13x faster                                                   |
| regex_dna      | 259 ms                                                       | 249 ms: 1.04x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 33.0 ms: 1.06x slower                                                   |
| regex_compile  | 128 ms                                                       | 258 ms: 2.02x slower                                                    |
| Geometric mean | (ref)                                                        | 1.16x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 147 ms                                                       | 159 ms: 1.09x slower                                                    |
| json_loads           | 32.1 us                                                      | 38.9 us: 1.21x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 17.8 ms: 1.36x slower                                                   |
| xml_etree_generate   | 114 ms                                                       | 162 ms: 1.43x slower                                                    |
| xml_etree_process    | 80.8 ms                                                      | 132 ms: 1.64x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 4.23 sec: 1.65x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 543 us: 2.16x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 782 us: 2.18x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.47x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 18.1 ms: 1.40x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 12.1 ms: 1.41x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.40x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.4 ms                                                      | 106 ms: 1.75x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 53.6 ms: 1.95x slower                                                   |
| django_template | 42.3 ms                                                      | 84.2 ms: 1.99x slower                                                   |
| mako            | 13.2 ms                                                      | 29.0 ms: 2.21x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.97x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.17 ms                                                      | 3.48 ms: 1.49x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 1.61 ms: 1.45x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.41 ms: 1.13x faster                                                   |
| regex_dna                  | 259 ms                                                       | 249 ms: 1.04x faster                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 7.13 ms: 1.01x slower                                                   |
| asyncio_websockets         | 657 ms                                                       | 675 ms: 1.03x slower                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.35 sec: 1.06x slower                                                  |
| regex_v8                   | 31.1 ms                                                      | 33.0 ms: 1.06x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 159 ms: 1.09x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 872 ms: 1.14x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 695 ms: 1.15x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.41 sec: 1.15x slower                                                  |
| async_tree_memoization     | 645 ms                                                       | 746 ms: 1.16x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 917 ms: 1.16x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.59 sec: 1.17x slower                                                  |
| asyncio_tcp                | 584 ms                                                       | 684 ms: 1.17x slower                                                    |
| pathlib                    | 22.8 ms                                                      | 26.9 ms: 1.18x slower                                                   |
| async_tree_none_tg         | 476 ms                                                       | 565 ms: 1.19x slower                                                    |
| json_loads                 | 32.1 us                                                      | 38.9 us: 1.21x slower                                                   |
| async_tree_none            | 492 ms                                                       | 608 ms: 1.23x slower                                                    |
| json                       | 5.64 ms                                                      | 7.00 ms: 1.24x slower                                                   |
| deepcopy                   | 448 us                                                       | 563 us: 1.26x slower                                                    |
| telco                      | 10.0 ms                                                      | 12.9 ms: 1.29x slower                                                   |
| scimark_fft                | 445 ms                                                       | 580 ms: 1.30x slower                                                    |
| mdp                        | 3.33 sec                                                     | 4.36 sec: 1.31x slower                                                  |
| docutils                   | 3.10 sec                                                     | 4.11 sec: 1.33x slower                                                  |
| json_dumps                 | 13.1 ms                                                      | 17.8 ms: 1.36x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 8.95 ms: 1.37x slower                                                   |
| async_generators           | 488 ms                                                       | 673 ms: 1.38x slower                                                    |
| coroutines                 | 29.0 ms                                                      | 40.0 ms: 1.38x slower                                                   |
| coverage                   | 98.4 ms                                                      | 136 ms: 1.39x slower                                                    |
| python_startup             | 13.0 ms                                                      | 18.1 ms: 1.40x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 12.1 ms: 1.41x slower                                                   |
| deepcopy_memo              | 50.8 us                                                      | 72.2 us: 1.42x slower                                                   |
| xml_etree_generate         | 114 ms                                                       | 162 ms: 1.43x slower                                                    |
| meteor_contest             | 113 ms                                                       | 169 ms: 1.49x slower                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 6.08 us: 1.51x slower                                                   |
| pylint                     | 337 ms                                                       | 510 ms: 1.51x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 152 ms: 1.53x slower                                                    |
| generators                 | 37.1 ms                                                      | 57.1 ms: 1.54x slower                                                   |
| tornado_http               | 128 ms                                                       | 208 ms: 1.62x slower                                                    |
| bpe_tokeniser              | 5.83 sec                                                     | 9.48 sec: 1.63x slower                                                  |
| xml_etree_process          | 80.8 ms                                                      | 132 ms: 1.64x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 4.23 sec: 1.65x slower                                                  |
| spectral_norm              | 141 ms                                                       | 233 ms: 1.65x slower                                                    |
| fannkuch                   | 451 ms                                                       | 751 ms: 1.67x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 2.05 sec: 1.68x slower                                                  |
| crypto_pyaes               | 82.0 ms                                                      | 137 ms: 1.68x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 35.0 ms: 1.68x slower                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 2.13 ms: 1.70x slower                                                   |
| 2to3                       | 305 ms                                                       | 517 ms: 1.70x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 106 ms: 1.75x slower                                                    |
| thrift                     | 962 us                                                       | 1.69 ms: 1.76x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 343 us: 1.77x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 235 ms: 1.82x slower                                                    |
| pyflate                    | 557 ms                                                       | 1.02 sec: 1.83x slower                                                  |
| html5lib                   | 66.1 ms                                                      | 121 ms: 1.84x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 117 ms: 1.87x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 3.66 sec: 1.89x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 1.78 sec: 1.91x slower                                                  |
| genshi_text                | 27.4 ms                                                      | 53.6 ms: 1.95x slower                                                   |
| sympy_str                  | 265 ms                                                       | 521 ms: 1.96x slower                                                    |
| comprehensions             | 20.5 us                                                      | 40.8 us: 1.99x slower                                                   |
| django_template            | 42.3 ms                                                      | 84.2 ms: 1.99x slower                                                   |
| regex_compile              | 128 ms                                                       | 258 ms: 2.02x slower                                                    |
| logging_format             | 7.82 us                                                      | 16.1 us: 2.06x slower                                                   |
| logging_simple             | 7.21 us                                                      | 14.8 us: 2.06x slower                                                   |
| sympy_expand               | 457 ms                                                       | 964 ms: 2.11x slower                                                    |
| richards                   | 55.9 ms                                                      | 118 ms: 2.11x slower                                                    |
| scimark_sor                | 159 ms                                                       | 339 ms: 2.13x slower                                                    |
| logging_silent             | 133 ns                                                       | 286 ns: 2.14x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 177 ms: 2.15x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 543 us: 2.16x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 782 us: 2.18x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 317 ms: 2.20x slower                                                    |
| mako                       | 13.2 ms                                                      | 29.0 ms: 2.21x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 15.8 ms: 2.23x slower                                                   |
| richards_super             | 62.3 ms                                                      | 139 ms: 2.23x slower                                                    |
| float                      | 91.4 ms                                                      | 212 ms: 2.32x slower                                                    |
| chaos                      | 68.3 ms                                                      | 159 ms: 2.32x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 347 ms: 2.46x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 4.27 ms: 2.50x slower                                                   |
| nbody                      | 114 ms                                                       | 286 ms: 2.50x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 3.71 ms: 2.61x slower                                                   |
| raytrace                   | 297 ms                                                       | 816 ms: 2.75x slower                                                    |
| go                         | 161 ms                                                       | 445 ms: 2.77x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 12.7 ms: 3.27x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.58x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, pidigits
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.44x
- 95% likely to have a slowdown of 1.40x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: 1.17x