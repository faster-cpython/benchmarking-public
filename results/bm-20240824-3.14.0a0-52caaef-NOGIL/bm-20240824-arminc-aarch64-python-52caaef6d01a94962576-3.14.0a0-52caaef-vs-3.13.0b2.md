# Results vs. 3.13.0b2

- fork: python
- ref: 52caaef6d01a94962576
- machine: linux-aarch64
- commit hash: 52caaef
- commit date: 2024-08-24
- overall geometric mean: 1.57x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x slower
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 521 ms: 1.71x slower                                                    |
| docutils       | 3.10 sec                                                     | 4.04 sec: 1.30x slower                                                  |
| html5lib       | 66.1 ms                                                      | 122 ms: 1.85x slower                                                    |
| tornado_http   | 128 ms                                                       | 204 ms: 1.60x slower                                                    |
| Geometric mean | (ref)                                                        | 1.60x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.37 sec: 1.08x slower                                                  |
| async_tree_memoization     | 645 ms                                                       | 738 ms: 1.14x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 908 ms: 1.15x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 695 ms: 1.15x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.41 sec: 1.15x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 877 ms: 1.15x slower                                                    |
| async_tree_none_tg         | 476 ms                                                       | 570 ms: 1.20x slower                                                    |
| async_tree_none            | 492 ms                                                       | 606 ms: 1.23x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 209 ms: 2.28x slower                                                    |
| nbody          | 114 ms                                                       | 282 ms: 2.47x slower                                                    |
| Geometric mean | (ref)                                                        | 1.78x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.48 ms: 1.11x faster                                                   |
| regex_v8       | 31.1 ms                                                      | 32.8 ms: 1.06x slower                                                   |
| regex_compile  | 128 ms                                                       | 260 ms: 2.03x slower                                                    |
| Geometric mean | (ref)                                                        | 1.18x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 191 ms                                                       | 184 ms: 1.04x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 160 ms: 1.09x slower                                                    |
| json_loads           | 32.1 us                                                      | 39.5 us: 1.23x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 18.3 ms: 1.40x slower                                                   |
| xml_etree_generate   | 114 ms                                                       | 162 ms: 1.43x slower                                                    |
| xml_etree_process    | 80.8 ms                                                      | 131 ms: 1.62x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 4.20 sec: 1.63x slower                                                  |
| pickle_pure_python   | 359 us                                                       | 776 us: 2.16x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 548 us: 2.18x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.47x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 18.0 ms: 1.39x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 12.1 ms: 1.41x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.40x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.4 ms                                                      | 105 ms: 1.74x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 53.4 ms: 1.95x slower                                                   |
| django_template | 42.3 ms                                                      | 84.2 ms: 1.99x slower                                                   |
| mako            | 13.2 ms                                                      | 28.9 ms: 2.20x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.96x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.17 ms                                                      | 3.50 ms: 1.48x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 1.64 ms: 1.42x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.48 ms: 1.11x faster                                                   |
| xml_etree_parse            | 191 ms                                                       | 184 ms: 1.04x faster                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 6.96 ms: 1.01x faster                                                   |
| asyncio_websockets         | 657 ms                                                       | 672 ms: 1.02x slower                                                    |
| regex_v8                   | 31.1 ms                                                      | 32.8 ms: 1.06x slower                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.37 sec: 1.08x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                       | 160 ms: 1.09x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 642 ms: 1.10x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.46 sec: 1.11x slower                                                  |
| async_tree_memoization     | 645 ms                                                       | 738 ms: 1.14x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 908 ms: 1.15x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 695 ms: 1.15x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.41 sec: 1.15x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 877 ms: 1.15x slower                                                    |
| pathlib                    | 22.8 ms                                                      | 26.8 ms: 1.18x slower                                                   |
| async_tree_none_tg         | 476 ms                                                       | 570 ms: 1.20x slower                                                    |
| async_tree_none            | 492 ms                                                       | 606 ms: 1.23x slower                                                    |
| json_loads                 | 32.1 us                                                      | 39.5 us: 1.23x slower                                                   |
| json                       | 5.64 ms                                                      | 7.12 ms: 1.26x slower                                                   |
| deepcopy                   | 448 us                                                       | 566 us: 1.26x slower                                                    |
| scimark_fft                | 445 ms                                                       | 576 ms: 1.29x slower                                                    |
| mdp                        | 3.33 sec                                                     | 4.34 sec: 1.30x slower                                                  |
| docutils                   | 3.10 sec                                                     | 4.04 sec: 1.30x slower                                                  |
| telco                      | 10.0 ms                                                      | 13.2 ms: 1.32x slower                                                   |
| async_generators           | 488 ms                                                       | 665 ms: 1.36x slower                                                    |
| coverage                   | 98.4 ms                                                      | 136 ms: 1.38x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 9.03 ms: 1.38x slower                                                   |
| python_startup             | 13.0 ms                                                      | 18.0 ms: 1.39x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 18.3 ms: 1.40x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 12.1 ms: 1.41x slower                                                   |
| deepcopy_memo              | 50.8 us                                                      | 72.2 us: 1.42x slower                                                   |
| coroutines                 | 29.0 ms                                                      | 41.3 ms: 1.42x slower                                                   |
| xml_etree_generate         | 114 ms                                                       | 162 ms: 1.43x slower                                                    |
| meteor_contest             | 113 ms                                                       | 167 ms: 1.47x slower                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 6.08 us: 1.51x slower                                                   |
| pylint                     | 337 ms                                                       | 509 ms: 1.51x slower                                                    |
| generators                 | 37.1 ms                                                      | 57.4 ms: 1.54x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 153 ms: 1.55x slower                                                    |
| tornado_http               | 128 ms                                                       | 204 ms: 1.60x slower                                                    |
| xml_etree_process          | 80.8 ms                                                      | 131 ms: 1.62x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 4.20 sec: 1.63x slower                                                  |
| bpe_tokeniser              | 5.83 sec                                                     | 9.54 sec: 1.64x slower                                                  |
| fannkuch                   | 451 ms                                                       | 740 ms: 1.64x slower                                                    |
| spectral_norm              | 141 ms                                                       | 233 ms: 1.65x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 2.03 sec: 1.66x slower                                                  |
| sympy_integrate            | 20.9 ms                                                      | 34.7 ms: 1.67x slower                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 2.10 ms: 1.67x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 137 ms: 1.68x slower                                                    |
| 2to3                       | 305 ms                                                       | 521 ms: 1.71x slower                                                    |
| thrift                     | 962 us                                                       | 1.66 ms: 1.72x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 105 ms: 1.74x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 339 us: 1.75x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 234 ms: 1.81x slower                                                    |
| pyflate                    | 557 ms                                                       | 1.01 sec: 1.82x slower                                                  |
| html5lib                   | 66.1 ms                                                      | 122 ms: 1.85x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 117 ms: 1.87x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 3.66 sec: 1.90x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 1.78 sec: 1.90x slower                                                  |
| sympy_str                  | 265 ms                                                       | 514 ms: 1.94x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 53.4 ms: 1.95x slower                                                   |
| comprehensions             | 20.5 us                                                      | 40.7 us: 1.98x slower                                                   |
| django_template            | 42.3 ms                                                      | 84.2 ms: 1.99x slower                                                   |
| logging_format             | 7.82 us                                                      | 15.7 us: 2.00x slower                                                   |
| logging_simple             | 7.21 us                                                      | 14.5 us: 2.01x slower                                                   |
| regex_compile              | 128 ms                                                       | 260 ms: 2.03x slower                                                    |
| richards                   | 55.9 ms                                                      | 118 ms: 2.10x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 174 ms: 2.11x slower                                                    |
| sympy_expand               | 457 ms                                                       | 969 ms: 2.12x slower                                                    |
| scimark_sor                | 159 ms                                                       | 342 ms: 2.15x slower                                                    |
| logging_silent             | 133 ns                                                       | 287 ns: 2.15x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 776 us: 2.16x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 548 us: 2.18x slower                                                    |
| mako                       | 13.2 ms                                                      | 28.9 ms: 2.20x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 315 ms: 2.20x slower                                                    |
| richards_super             | 62.3 ms                                                      | 138 ms: 2.21x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 15.9 ms: 2.25x slower                                                   |
| float                      | 91.4 ms                                                      | 209 ms: 2.28x slower                                                    |
| chaos                      | 68.3 ms                                                      | 159 ms: 2.34x slower                                                    |
| nbody                      | 114 ms                                                       | 282 ms: 2.47x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 355 ms: 2.51x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 4.30 ms: 2.51x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 3.70 ms: 2.60x slower                                                   |
| raytrace                   | 297 ms                                                       | 817 ms: 2.75x slower                                                    |
| go                         | 161 ms                                                       | 443 ms: 2.75x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 12.8 ms: 3.31x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.57x slower                                                            |

Benchmark hidden because not significant (2): regex_dna, pidigits
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.43x
- 95% likely to have a slowdown of 1.40x
- 99% likely to have a slowdown of 1.35x

# Memory
- memory change: 1.18x