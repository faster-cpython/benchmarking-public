# Results vs. 3.13.0b2

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-aarch64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.57x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 517 ms: 1.70x slower                                                    |
| docutils       | 3.10 sec                                                     | 4.10 sec: 1.32x slower                                                  |
| html5lib       | 66.1 ms                                                      | 121 ms: 1.83x slower                                                    |
| tornado_http   | 128 ms                                                       | 202 ms: 1.58x slower                                                    |
| Geometric mean | (ref)                                                        | 1.60x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.35 sec: 1.06x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 869 ms: 1.14x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.40 sec: 1.14x slower                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 910 ms: 1.15x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 748 ms: 1.16x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 702 ms: 1.16x slower                                                    |
| async_tree_none_tg         | 476 ms                                                       | 566 ms: 1.19x slower                                                    |
| async_tree_none            | 492 ms                                                       | 611 ms: 1.24x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 210 ms: 2.29x slower                                                    |
| nbody          | 114 ms                                                       | 289 ms: 2.53x slower                                                    |
| Geometric mean | (ref)                                                        | 1.80x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.30 ms: 1.16x faster                                                   |
| regex_dna      | 259 ms                                                       | 245 ms: 1.06x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 32.5 ms: 1.05x slower                                                   |
| regex_compile  | 128 ms                                                       | 256 ms: 2.00x slower                                                    |
| Geometric mean | (ref)                                                        | 1.14x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 191 ms                                                       | 182 ms: 1.05x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 156 ms: 1.07x slower                                                    |
| json_loads           | 32.1 us                                                      | 38.7 us: 1.20x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 17.6 ms: 1.34x slower                                                   |
| xml_etree_generate   | 114 ms                                                       | 160 ms: 1.41x slower                                                    |
| xml_etree_process    | 80.8 ms                                                      | 129 ms: 1.60x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 4.20 sec: 1.64x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 542 us: 2.15x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 774 us: 2.16x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.45x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 17.6 ms: 1.36x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 11.7 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.36x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.4 ms                                                      | 104 ms: 1.72x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 53.2 ms: 1.94x slower                                                   |
| django_template | 42.3 ms                                                      | 83.2 ms: 1.97x slower                                                   |
| mako            | 13.2 ms                                                      | 28.8 ms: 2.19x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.95x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.17 ms                                                      | 3.42 ms: 1.51x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 1.58 ms: 1.47x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.30 ms: 1.16x faster                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 6.25 ms: 1.13x faster                                                   |
| regex_dna                  | 259 ms                                                       | 245 ms: 1.06x faster                                                    |
| xml_etree_parse            | 191 ms                                                       | 182 ms: 1.05x faster                                                    |
| asyncio_websockets         | 657 ms                                                       | 671 ms: 1.02x slower                                                    |
| regex_v8                   | 31.1 ms                                                      | 32.5 ms: 1.05x slower                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.35 sec: 1.06x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                       | 156 ms: 1.07x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.47 sec: 1.12x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 869 ms: 1.14x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.40 sec: 1.14x slower                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 910 ms: 1.15x slower                                                    |
| pathlib                    | 22.8 ms                                                      | 26.3 ms: 1.15x slower                                                   |
| async_tree_memoization     | 645 ms                                                       | 748 ms: 1.16x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 702 ms: 1.16x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 684 ms: 1.17x slower                                                    |
| telco                      | 10.0 ms                                                      | 11.8 ms: 1.18x slower                                                   |
| async_tree_none_tg         | 476 ms                                                       | 566 ms: 1.19x slower                                                    |
| json_loads                 | 32.1 us                                                      | 38.7 us: 1.20x slower                                                   |
| json                       | 5.64 ms                                                      | 7.01 ms: 1.24x slower                                                   |
| async_tree_none            | 492 ms                                                       | 611 ms: 1.24x slower                                                    |
| deepcopy                   | 448 us                                                       | 559 us: 1.25x slower                                                    |
| mdp                        | 3.33 sec                                                     | 4.37 sec: 1.31x slower                                                  |
| docutils                   | 3.10 sec                                                     | 4.10 sec: 1.32x slower                                                  |
| json_dumps                 | 13.1 ms                                                      | 17.6 ms: 1.34x slower                                                   |
| scimark_fft                | 445 ms                                                       | 601 ms: 1.35x slower                                                    |
| coroutines                 | 29.0 ms                                                      | 39.2 ms: 1.35x slower                                                   |
| coverage                   | 98.4 ms                                                      | 134 ms: 1.36x slower                                                    |
| python_startup             | 13.0 ms                                                      | 17.6 ms: 1.36x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 11.7 ms: 1.36x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 9.05 ms: 1.38x slower                                                   |
| async_generators           | 488 ms                                                       | 678 ms: 1.39x slower                                                    |
| xml_etree_generate         | 114 ms                                                       | 160 ms: 1.41x slower                                                    |
| deepcopy_memo              | 50.8 us                                                      | 72.0 us: 1.42x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 6.02 us: 1.49x slower                                                   |
| pylint                     | 337 ms                                                       | 504 ms: 1.50x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.91 ms: 1.52x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 151 ms: 1.53x slower                                                    |
| meteor_contest             | 113 ms                                                       | 174 ms: 1.53x slower                                                    |
| generators                 | 37.1 ms                                                      | 58.4 ms: 1.57x slower                                                   |
| tornado_http               | 128 ms                                                       | 202 ms: 1.58x slower                                                    |
| xml_etree_process          | 80.8 ms                                                      | 129 ms: 1.60x slower                                                    |
| bpe_tokeniser              | 5.83 sec                                                     | 9.48 sec: 1.63x slower                                                  |
| tomli_loads                | 2.57 sec                                                     | 4.20 sec: 1.64x slower                                                  |
| dulwich_log                | 58.5 ms                                                      | 97.3 ms: 1.66x slower                                                   |
| fannkuch                   | 451 ms                                                       | 750 ms: 1.66x slower                                                    |
| spectral_norm              | 141 ms                                                       | 237 ms: 1.68x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 35.0 ms: 1.68x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 2.06 sec: 1.69x slower                                                  |
| 2to3                       | 305 ms                                                       | 517 ms: 1.70x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 140 ms: 1.70x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 331 us: 1.71x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 104 ms: 1.72x slower                                                    |
| thrift                     | 962 us                                                       | 1.67 ms: 1.73x slower                                                   |
| sqlglot_normalize          | 129 ms                                                       | 230 ms: 1.78x slower                                                    |
| pyflate                    | 557 ms                                                       | 1.02 sec: 1.82x slower                                                  |
| html5lib                   | 66.1 ms                                                      | 121 ms: 1.83x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 116 ms: 1.85x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 3.64 sec: 1.89x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 1.77 sec: 1.90x slower                                                  |
| genshi_text                | 27.4 ms                                                      | 53.2 ms: 1.94x slower                                                   |
| sympy_str                  | 265 ms                                                       | 519 ms: 1.95x slower                                                    |
| django_template            | 42.3 ms                                                      | 83.2 ms: 1.97x slower                                                   |
| comprehensions             | 20.5 us                                                      | 40.7 us: 1.98x slower                                                   |
| logging_format             | 7.82 us                                                      | 15.6 us: 2.00x slower                                                   |
| regex_compile              | 128 ms                                                       | 256 ms: 2.00x slower                                                    |
| logging_simple             | 7.21 us                                                      | 14.6 us: 2.02x slower                                                   |
| sympy_expand               | 457 ms                                                       | 956 ms: 2.09x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 175 ms: 2.13x slower                                                    |
| logging_silent             | 133 ns                                                       | 287 ns: 2.15x slower                                                    |
| scimark_sor                | 159 ms                                                       | 343 ms: 2.15x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 542 us: 2.15x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 774 us: 2.16x slower                                                    |
| mako                       | 13.2 ms                                                      | 28.8 ms: 2.19x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 15.6 ms: 2.21x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 318 ms: 2.21x slower                                                    |
| richards                   | 55.9 ms                                                      | 127 ms: 2.28x slower                                                    |
| float                      | 91.4 ms                                                      | 210 ms: 2.29x slower                                                    |
| richards_super             | 62.3 ms                                                      | 145 ms: 2.34x slower                                                    |
| chaos                      | 68.3 ms                                                      | 161 ms: 2.36x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 355 ms: 2.51x slower                                                    |
| nbody                      | 114 ms                                                       | 289 ms: 2.53x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 4.38 ms: 2.56x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 3.78 ms: 2.65x slower                                                   |
| raytrace                   | 297 ms                                                       | 825 ms: 2.78x slower                                                    |
| go                         | 161 ms                                                       | 448 ms: 2.79x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 12.9 ms: 3.32x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.57x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.45x
- 95% likely to have a slowdown of 1.40x
- 99% likely to have a slowdown of 1.35x

# Memory
- memory change: 1.16x