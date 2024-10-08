# Results vs. 3.13.0b2

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-aarch64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 361 ms: 1.18x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.55 sec: 1.14x slower                                                  |
| html5lib       | 66.1 ms                                                      | 69.9 ms: 1.06x slower                                                   |
| tornado_http   | 128 ms                                                       | 142 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                        | 1.12x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 414 ms: 1.15x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.15x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 542 ms: 1.11x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 590 ms: 1.09x faster                                                    |
| async_tree_none            | 492 ms                                                       | 451 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 739 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 720 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| regex_compile  | 128 ms                                                       | 178 ms: 1.39x slower                                                    |
| Geometric mean | (ref)                                                        | 1.08x slower                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 110 ms: 1.03x faster                                                    |
| xml_etree_process    | 80.8 ms                                                      | 79.0 ms: 1.02x faster                                                   |
| json_dumps           | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| json_loads           | 32.1 us                                                      | 32.9 us: 1.02x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 274 us: 1.09x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 415 us: 1.16x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.0 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.94 ms: 1.04x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 50.9 ms: 1.20x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 34.4 ms: 1.25x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 80.5 ms: 1.33x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.19x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.0 us: 1.34x faster                                                   |
| deepcopy                   | 448 us                                                       | 372 us: 1.20x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 414 ms: 1.15x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.15x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 542 ms: 1.11x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 590 ms: 1.09x faster                                                    |
| async_tree_none            | 492 ms                                                       | 451 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 739 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 720 ms: 1.06x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 22.0 ms: 1.04x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 5.02 ms: 1.03x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 110 ms: 1.03x faster                                                    |
| richards                   | 55.9 ms                                                      | 54.3 ms: 1.03x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| xml_etree_process          | 80.8 ms                                                      | 79.0 ms: 1.02x faster                                                   |
| richards_super             | 62.3 ms                                                      | 61.4 ms: 1.02x faster                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| python_startup             | 13.0 ms                                                      | 13.0 ms: 1.01x slower                                                   |
| thrift                     | 962 us                                                       | 974 us: 1.01x slower                                                    |
| logging_silent             | 133 ns                                                       | 136 ns: 1.02x slower                                                    |
| spectral_norm              | 141 ms                                                       | 144 ms: 1.02x slower                                                    |
| meteor_contest             | 113 ms                                                       | 116 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.26 sec: 1.02x slower                                                  |
| json_loads                 | 32.1 us                                                      | 32.9 us: 1.02x slower                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 2.39 ms: 1.03x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| bpe_tokeniser              | 5.83 sec                                                     | 6.00 sec: 1.03x slower                                                  |
| coverage                   | 98.4 ms                                                      | 101 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.76 ms: 1.03x slower                                                   |
| async_generators           | 488 ms                                                       | 505 ms: 1.04x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.94 ms: 1.04x slower                                                   |
| scimark_fft                | 445 ms                                                       | 463 ms: 1.04x slower                                                    |
| generators                 | 37.1 ms                                                      | 38.6 ms: 1.04x slower                                                   |
| telco                      | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                   |
| fannkuch                   | 451 ms                                                       | 470 ms: 1.04x slower                                                    |
| mdp                        | 3.33 sec                                                     | 3.47 sec: 1.04x slower                                                  |
| json                       | 5.64 ms                                                      | 5.92 ms: 1.05x slower                                                   |
| dask                       | 370 ms                                                       | 391 ms: 1.05x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.33 ms: 1.06x slower                                                   |
| html5lib                   | 66.1 ms                                                      | 69.9 ms: 1.06x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 87.0 ms: 1.06x slower                                                   |
| asyncio_tcp                | 584 ms                                                       | 625 ms: 1.07x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 209 us: 1.08x slower                                                    |
| pyflate                    | 557 ms                                                       | 603 ms: 1.08x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 274 us: 1.09x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 89.9 ms: 1.09x slower                                                   |
| raytrace                   | 297 ms                                                       | 325 ms: 1.10x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 69.1 ms: 1.10x slower                                                   |
| sqlglot_normalize          | 129 ms                                                       | 144 ms: 1.11x slower                                                    |
| tornado_http               | 128 ms                                                       | 142 ms: 1.11x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.36 sec: 1.11x slower                                                  |
| scimark_sor                | 159 ms                                                       | 178 ms: 1.12x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 1.59 ms: 1.12x slower                                                   |
| go                         | 161 ms                                                       | 181 ms: 1.13x slower                                                    |
| comprehensions             | 20.5 us                                                      | 23.4 us: 1.14x slower                                                   |
| docutils                   | 3.10 sec                                                     | 3.55 sec: 1.14x slower                                                  |
| deltablue                  | 3.88 ms                                                      | 4.45 ms: 1.15x slower                                                   |
| pickle_pure_python         | 359 us                                                       | 415 us: 1.16x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 8.27 ms: 1.18x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 2.02 ms: 1.18x slower                                                   |
| sympy_expand               | 457 ms                                                       | 541 ms: 1.18x slower                                                    |
| 2to3                       | 305 ms                                                       | 361 ms: 1.18x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 118 ms: 1.19x slower                                                    |
| django_template            | 42.3 ms                                                      | 50.9 ms: 1.20x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.13 sec: 1.21x slower                                                  |
| pprint_pformat             | 1.93 sec                                                     | 2.34 sec: 1.21x slower                                                  |
| dulwich_log                | 58.5 ms                                                      | 71.1 ms: 1.22x slower                                                   |
| sympy_str                  | 265 ms                                                       | 324 ms: 1.22x slower                                                    |
| pylint                     | 337 ms                                                       | 413 ms: 1.22x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 34.4 ms: 1.25x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 26.2 ms: 1.26x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 9.03 ms: 1.28x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 185 ms: 1.29x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 183 ms: 1.29x slower                                                    |
| chaos                      | 68.3 ms                                                      | 90.9 ms: 1.33x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 80.5 ms: 1.33x slower                                                   |
| regex_compile              | 128 ms                                                       | 178 ms: 1.39x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                            |

Benchmark hidden because not significant (13): xml_etree_parse, float, regex_effbot, logging_simple, coroutines, nbody, mako, deepcopy_reduce, regex_dna, pidigits, asyncio_websockets, logging_format, xml_etree_iterparse
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.08x