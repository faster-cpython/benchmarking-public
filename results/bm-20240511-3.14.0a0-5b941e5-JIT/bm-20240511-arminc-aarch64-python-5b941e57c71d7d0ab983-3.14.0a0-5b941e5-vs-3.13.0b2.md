# Results vs. 3.13.0b2

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: linux-aarch64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.11x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 364 ms: 1.19x slower                                                    |
| chameleon      | 8.95 ms                                                      | 9.32 ms: 1.04x slower                                                   |
| docutils       | 3.10 sec                                                     | 3.56 sec: 1.15x slower                                                  |
| html5lib       | 66.1 ms                                                      | 70.7 ms: 1.07x slower                                                   |
| tornado_http   | 128 ms                                                       | 144 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                        | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.24 sec: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 811 ms: 1.06x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_io, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 90.6 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 255 ms: 1.01x faster                                                    |
| regex_compile  | 128 ms                                                       | 171 ms: 1.33x slower                                                    |
| Geometric mean | (ref)                                                        | 1.07x slower                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_list        | 6.52 us                                                      | 6.35 us: 1.03x faster                                                   |
| unpickle             | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| xml_etree_generate   | 114 ms                                                       | 113 ms: 1.01x faster                                                    |
| json_dumps           | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.61 sec: 1.02x slower                                                  |
| xml_etree_iterparse  | 147 ms                                                       | 152 ms: 1.03x slower                                                    |
| pickle               | 13.4 us                                                      | 14.1 us: 1.05x slower                                                   |
| pickle_pure_python   | 359 us                                                       | 394 us: 1.10x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 276 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_process, pickle_dict, pickle_list, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 14.8 ms: 1.14x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 10.8 ms: 1.26x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 49.8 ms: 1.18x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 34.4 ms: 1.26x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 81.9 ms: 1.36x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.19x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| richards                   | 55.9 ms                                                      | 54.1 ms: 1.03x faster                                                   |
| unpickle_list              | 6.52 us                                                      | 6.35 us: 1.03x faster                                                   |
| sqlite_synth               | 3.90 us                                                      | 3.80 us: 1.03x faster                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.24 sec: 1.02x faster                                                  |
| richards_super             | 62.3 ms                                                      | 61.3 ms: 1.02x faster                                                   |
| deepcopy_memo              | 50.8 us                                                      | 50.1 us: 1.01x faster                                                   |
| regex_dna                  | 259 ms                                                       | 255 ms: 1.01x faster                                                    |
| unpickle                   | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| float                      | 91.4 ms                                                      | 90.6 ms: 1.01x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 113 ms: 1.01x faster                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| asyncio_websockets         | 657 ms                                                       | 665 ms: 1.01x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.61 sec: 1.02x slower                                                  |
| pathlib                    | 22.8 ms                                                      | 23.2 ms: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.26 sec: 1.02x slower                                                  |
| scimark_fft                | 445 ms                                                       | 455 ms: 1.02x slower                                                    |
| coverage                   | 98.4 ms                                                      | 101 ms: 1.02x slower                                                    |
| gc_traversal               | 5.17 ms                                                      | 5.35 ms: 1.03x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 152 ms: 1.03x slower                                                    |
| spectral_norm              | 141 ms                                                       | 146 ms: 1.03x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 605 ms: 1.04x slower                                                    |
| chameleon                  | 8.95 ms                                                      | 9.32 ms: 1.04x slower                                                   |
| generators                 | 37.1 ms                                                      | 38.7 ms: 1.04x slower                                                   |
| logging_silent             | 133 ns                                                       | 139 ns: 1.04x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.84 ms: 1.04x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.48 sec: 1.05x slower                                                  |
| meteor_contest             | 113 ms                                                       | 119 ms: 1.05x slower                                                    |
| pickle                     | 13.4 us                                                      | 14.1 us: 1.05x slower                                                   |
| async_generators           | 488 ms                                                       | 513 ms: 1.05x slower                                                    |
| fannkuch                   | 451 ms                                                       | 475 ms: 1.05x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.33 ms: 1.06x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 87.0 ms: 1.06x slower                                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 87.4 ms: 1.06x slower                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 811 ms: 1.06x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 207 us: 1.07x slower                                                    |
| create_gc_cycles           | 2.33 ms                                                      | 2.49 ms: 1.07x slower                                                   |
| html5lib                   | 66.1 ms                                                      | 70.7 ms: 1.07x slower                                                   |
| dask                       | 370 ms                                                       | 397 ms: 1.07x slower                                                    |
| flaskblogging              | 4.70 ms                                                      | 5.12 ms: 1.09x slower                                                   |
| raytrace                   | 297 ms                                                       | 325 ms: 1.10x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 394 us: 1.10x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 276 us: 1.10x slower                                                    |
| scimark_sor                | 159 ms                                                       | 176 ms: 1.10x slower                                                    |
| deepcopy                   | 448 us                                                       | 495 us: 1.10x slower                                                    |
| go                         | 161 ms                                                       | 179 ms: 1.11x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 144 ms: 1.11x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.36 sec: 1.11x slower                                                  |
| pyflate                    | 557 ms                                                       | 619 ms: 1.11x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 69.9 ms: 1.12x slower                                                   |
| comprehensions             | 20.5 us                                                      | 22.9 us: 1.12x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 1.60 ms: 1.12x slower                                                   |
| tornado_http               | 128 ms                                                       | 144 ms: 1.13x slower                                                    |
| python_startup             | 13.0 ms                                                      | 14.8 ms: 1.14x slower                                                   |
| docutils                   | 3.10 sec                                                     | 3.56 sec: 1.15x slower                                                  |
| deepcopy_reduce            | 4.04 us                                                      | 4.67 us: 1.16x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 8.24 ms: 1.17x slower                                                   |
| deltablue                  | 3.88 ms                                                      | 4.56 ms: 1.18x slower                                                   |
| django_template            | 42.3 ms                                                      | 49.8 ms: 1.18x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 2.29 sec: 1.19x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 1.11 sec: 1.19x slower                                                  |
| sqlglot_transpile          | 1.71 ms                                                      | 2.04 ms: 1.19x slower                                                   |
| 2to3                       | 305 ms                                                       | 364 ms: 1.19x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 118 ms: 1.19x slower                                                    |
| sympy_expand               | 457 ms                                                       | 554 ms: 1.21x slower                                                    |
| sympy_str                  | 265 ms                                                       | 326 ms: 1.23x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 71.8 ms: 1.23x slower                                                   |
| pylint                     | 337 ms                                                       | 419 ms: 1.24x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 34.4 ms: 1.26x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 10.8 ms: 1.26x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 26.4 ms: 1.26x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 8.99 ms: 1.27x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 182 ms: 1.29x slower                                                    |
| chaos                      | 68.3 ms                                                      | 88.7 ms: 1.30x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 189 ms: 1.31x slower                                                    |
| regex_compile              | 128 ms                                                       | 171 ms: 1.33x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 81.9 ms: 1.36x slower                                                   |
| telco                      | 10.0 ms                                                      | 166 ms: 16.53x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.11x slower                                                            |

Benchmark hidden because not significant (21): regex_v8, xml_etree_process, regex_effbot, coroutines, mako, nbody, pickle_dict, async_tree_none_tg, pickle_list, json_loads, thrift, pidigits, json, xml_etree_parse, async_tree_cpu_io_mixed, logging_format, async_tree_none, async_tree_io, async_tree_memoization, async_tree_memoization_tg, logging_simple
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x