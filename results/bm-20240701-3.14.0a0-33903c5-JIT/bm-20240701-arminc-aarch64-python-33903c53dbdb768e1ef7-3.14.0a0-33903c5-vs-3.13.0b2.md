# Results vs. 3.13.0b2

- fork: python
- ref: 33903c53dbdb768e1ef7
- machine: linux-aarch64
- commit hash: 33903c5
- commit date: 2024-07-01
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 358 ms: 1.17x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.53 sec: 1.14x slower                                                  |
| html5lib       | 66.1 ms                                                      | 70.9 ms: 1.07x slower                                                   |
| tornado_http   | 128 ms                                                       | 139 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                        | 1.12x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 406 ms: 1.17x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.15x faster                                                  |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 539 ms: 1.12x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 582 ms: 1.11x faster                                                    |
| async_tree_none            | 492 ms                                                       | 444 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 735 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 723 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.12x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 89.6 ms: 1.02x faster                                                   |
| nbody          | 114 ms                                                       | 117 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 250 ms: 1.03x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.6 ms: 1.02x faster                                                   |
| regex_effbot   | 4.98 ms                                                      | 4.92 ms: 1.01x faster                                                   |
| regex_compile  | 128 ms                                                       | 174 ms: 1.36x slower                                                    |
| Geometric mean | (ref)                                                        | 1.06x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 147 ms                                                       | 150 ms: 1.02x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| json_dumps           | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| json_loads           | 32.1 us                                                      | 33.4 us: 1.04x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 277 us: 1.10x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 398 us: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.93 ms: 1.04x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.03x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| django_template | 42.3 ms                                                      | 49.6 ms: 1.17x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 34.2 ms: 1.25x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 81.7 ms: 1.35x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.19x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.8 us: 1.31x faster                                                   |
| deepcopy                   | 448 us                                                       | 376 us: 1.19x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 406 ms: 1.17x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.15x faster                                                  |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 539 ms: 1.12x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 582 ms: 1.11x faster                                                    |
| async_tree_none            | 492 ms                                                       | 444 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 735 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 723 ms: 1.06x faster                                                    |
| richards                   | 55.9 ms                                                      | 53.5 ms: 1.04x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 22.0 ms: 1.03x faster                                                   |
| regex_dna                  | 259 ms                                                       | 250 ms: 1.03x faster                                                    |
| richards_super             | 62.3 ms                                                      | 60.5 ms: 1.03x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 5.05 ms: 1.02x faster                                                   |
| float                      | 91.4 ms                                                      | 89.6 ms: 1.02x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.6 ms: 1.02x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.92 ms: 1.01x faster                                                   |
| mako                       | 13.2 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| asyncio_websockets         | 657 ms                                                       | 664 ms: 1.01x slower                                                    |
| python_startup             | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                                   |
| coverage                   | 98.4 ms                                                      | 100 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.26 sec: 1.02x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                       | 150 ms: 1.02x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| nbody                      | 114 ms                                                       | 117 ms: 1.02x slower                                                    |
| meteor_contest             | 113 ms                                                       | 116 ms: 1.02x slower                                                    |
| logging_silent             | 133 ns                                                       | 138 ns: 1.03x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| scimark_fft                | 445 ms                                                       | 461 ms: 1.03x slower                                                    |
| telco                      | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                   |
| coroutines                 | 29.0 ms                                                      | 30.1 ms: 1.04x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.93 ms: 1.04x slower                                                   |
| json_loads                 | 32.1 us                                                      | 33.4 us: 1.04x slower                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 6.07 sec: 1.04x slower                                                  |
| mdp                        | 3.33 sec                                                     | 3.47 sec: 1.04x slower                                                  |
| deepcopy_reduce            | 4.04 us                                                      | 4.21 us: 1.04x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.86 ms: 1.05x slower                                                   |
| async_generators           | 488 ms                                                       | 512 ms: 1.05x slower                                                    |
| json                       | 5.64 ms                                                      | 5.93 ms: 1.05x slower                                                   |
| spectral_norm              | 141 ms                                                       | 148 ms: 1.05x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 614 ms: 1.05x slower                                                    |
| dask                       | 370 ms                                                       | 391 ms: 1.05x slower                                                    |
| fannkuch                   | 451 ms                                                       | 476 ms: 1.06x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.33 ms: 1.06x slower                                                   |
| generators                 | 37.1 ms                                                      | 39.3 ms: 1.06x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 87.0 ms: 1.06x slower                                                   |
| html5lib                   | 66.1 ms                                                      | 70.9 ms: 1.07x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 209 us: 1.08x slower                                                    |
| tornado_http               | 128 ms                                                       | 139 ms: 1.08x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 141 ms: 1.09x slower                                                    |
| raytrace                   | 297 ms                                                       | 324 ms: 1.09x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 90.4 ms: 1.10x slower                                                   |
| pyflate                    | 557 ms                                                       | 613 ms: 1.10x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.35 sec: 1.10x slower                                                  |
| unpickle_pure_python       | 251 us                                                       | 277 us: 1.10x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 69.4 ms: 1.11x slower                                                   |
| pickle_pure_python         | 359 us                                                       | 398 us: 1.11x slower                                                    |
| scimark_sor                | 159 ms                                                       | 177 ms: 1.11x slower                                                    |
| go                         | 161 ms                                                       | 179 ms: 1.11x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 1.60 ms: 1.12x slower                                                   |
| comprehensions             | 20.5 us                                                      | 23.2 us: 1.13x slower                                                   |
| docutils                   | 3.10 sec                                                     | 3.53 sec: 1.14x slower                                                  |
| deltablue                  | 3.88 ms                                                      | 4.47 ms: 1.15x slower                                                   |
| django_template            | 42.3 ms                                                      | 49.6 ms: 1.17x slower                                                   |
| 2to3                       | 305 ms                                                       | 358 ms: 1.17x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 2.01 ms: 1.18x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 118 ms: 1.19x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 8.40 ms: 1.19x slower                                                   |
| sympy_expand               | 457 ms                                                       | 547 ms: 1.20x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 2.32 sec: 1.20x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 1.12 sec: 1.20x slower                                                  |
| dulwich_log                | 58.5 ms                                                      | 71.5 ms: 1.22x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 34.2 ms: 1.25x slower                                                   |
| sympy_str                  | 265 ms                                                       | 331 ms: 1.25x slower                                                    |
| pylint                     | 337 ms                                                       | 423 ms: 1.25x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 9.00 ms: 1.27x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 26.8 ms: 1.28x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 186 ms: 1.30x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 185 ms: 1.31x slower                                                    |
| chaos                      | 68.3 ms                                                      | 89.3 ms: 1.31x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 81.7 ms: 1.35x slower                                                   |
| regex_compile              | 128 ms                                                       | 174 ms: 1.36x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                            |

Benchmark hidden because not significant (8): xml_etree_process, create_gc_cycles, logging_format, pidigits, logging_simple, xml_etree_parse, thrift, xml_etree_generate
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.08x