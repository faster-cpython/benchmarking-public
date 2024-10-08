# Results vs. 3.13.0b2

- fork: mdboom
- ref: marshal_slice
- machine: linux-aarch64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.05x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 296 ms: 1.03x faster                                             |
| docutils       | 3.10 sec                                                     | 3.01 sec: 1.03x faster                                           |
| html5lib       | 66.1 ms                                                      | 63.1 ms: 1.05x faster                                            |
| Geometric mean | (ref)                                                        | 1.03x faster                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization     | 645 ms                                                       | 553 ms: 1.17x faster                                             |
| async_tree_none            | 492 ms                                                       | 429 ms: 1.15x faster                                             |
| async_tree_none_tg         | 476 ms                                                       | 421 ms: 1.13x faster                                             |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 714 ms: 1.11x faster                                             |
| async_tree_memoization_tg  | 604 ms                                                       | 550 ms: 1.10x faster                                             |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                           |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 705 ms: 1.08x faster                                             |
| async_tree_io              | 1.22 sec                                                     | 1.17 sec: 1.04x faster                                           |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 110 ms: 1.04x faster                                             |
| float          | 91.4 ms                                                      | 94.4 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 128 ms                                                       | 125 ms: 1.02x faster                                             |
| regex_dna      | 259 ms                                                       | 254 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_loads           | 32.1 us                                                      | 31.1 us: 1.03x faster                                            |
| unpickle             | 19.8 us                                                      | 19.5 us: 1.01x faster                                            |
| pickle_list          | 5.27 us                                                      | 5.23 us: 1.01x faster                                            |
| json_dumps           | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                            |
| pickle_dict          | 37.6 us                                                      | 38.1 us: 1.01x slower                                            |
| unpickle_pure_python | 251 us                                                       | 255 us: 1.01x slower                                             |
| unpickle_list        | 6.52 us                                                      | 6.64 us: 1.02x slower                                            |
| pickle_pure_python   | 359 us                                                       | 366 us: 1.02x slower                                             |
| tomli_loads          | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                           |
| pickle               | 13.4 us                                                      | 13.9 us: 1.03x slower                                            |
| xml_etree_iterparse  | 147 ms                                                       | 152 ms: 1.04x slower                                             |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako           | 13.2 ms                                                      | 13.3 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 331 us: 1.36x faster                                             |
| deepcopy_memo              | 50.8 us                                                      | 37.9 us: 1.34x faster                                            |
| deepcopy_reduce            | 4.04 us                                                      | 3.45 us: 1.17x faster                                            |
| async_tree_memoization     | 645 ms                                                       | 553 ms: 1.17x faster                                             |
| go                         | 161 ms                                                       | 138 ms: 1.16x faster                                             |
| async_tree_none            | 492 ms                                                       | 429 ms: 1.15x faster                                             |
| async_tree_none_tg         | 476 ms                                                       | 421 ms: 1.13x faster                                             |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 714 ms: 1.11x faster                                             |
| async_tree_memoization_tg  | 604 ms                                                       | 550 ms: 1.10x faster                                             |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                           |
| telco                      | 10.0 ms                                                      | 9.25 ms: 1.08x faster                                            |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 705 ms: 1.08x faster                                             |
| scimark_lu                 | 141 ms                                                       | 132 ms: 1.07x faster                                             |
| richards                   | 55.9 ms                                                      | 52.7 ms: 1.06x faster                                            |
| pathlib                    | 22.8 ms                                                      | 21.5 ms: 1.06x faster                                            |
| generators                 | 37.1 ms                                                      | 35.2 ms: 1.06x faster                                            |
| html5lib                   | 66.1 ms                                                      | 63.1 ms: 1.05x faster                                            |
| scimark_fft                | 445 ms                                                       | 426 ms: 1.04x faster                                             |
| richards_super             | 62.3 ms                                                      | 59.6 ms: 1.04x faster                                            |
| asyncio_tcp                | 584 ms                                                       | 560 ms: 1.04x faster                                             |
| async_tree_io              | 1.22 sec                                                     | 1.17 sec: 1.04x faster                                           |
| pprint_pformat             | 1.93 sec                                                     | 1.86 sec: 1.04x faster                                           |
| nbody                      | 114 ms                                                       | 110 ms: 1.04x faster                                             |
| pprint_safe_repr           | 933 ms                                                       | 904 ms: 1.03x faster                                             |
| json_loads                 | 32.1 us                                                      | 31.1 us: 1.03x faster                                            |
| 2to3                       | 305 ms                                                       | 296 ms: 1.03x faster                                             |
| docutils                   | 3.10 sec                                                     | 3.01 sec: 1.03x faster                                           |
| async_generators           | 488 ms                                                       | 475 ms: 1.03x faster                                             |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.39 ms: 1.03x faster                                            |
| json                       | 5.64 ms                                                      | 5.50 ms: 1.03x faster                                            |
| meteor_contest             | 113 ms                                                       | 111 ms: 1.02x faster                                             |
| sympy_sum                  | 144 ms                                                       | 140 ms: 1.02x faster                                             |
| gc_traversal               | 5.17 ms                                                      | 5.07 ms: 1.02x faster                                            |
| regex_compile              | 128 ms                                                       | 125 ms: 1.02x faster                                             |
| sqlite_synth               | 3.90 us                                                      | 3.83 us: 1.02x faster                                            |
| bpe_tokeniser              | 5.83 sec                                                     | 5.72 sec: 1.02x faster                                           |
| regex_dna                  | 259 ms                                                       | 254 ms: 1.02x faster                                             |
| scimark_sor                | 159 ms                                                       | 157 ms: 1.02x faster                                             |
| logging_silent             | 133 ns                                                       | 132 ns: 1.01x faster                                             |
| unpickle                   | 19.8 us                                                      | 19.5 us: 1.01x faster                                            |
| pickle_list                | 5.27 us                                                      | 5.23 us: 1.01x faster                                            |
| coverage                   | 98.4 ms                                                      | 99.0 ms: 1.01x slower                                            |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                            |
| pickle_dict                | 37.6 us                                                      | 38.1 us: 1.01x slower                                            |
| sympy_integrate            | 20.9 ms                                                      | 21.1 ms: 1.01x slower                                            |
| unpickle_pure_python       | 251 us                                                       | 255 us: 1.01x slower                                             |
| bench_thread_pool          | 1.26 ms                                                      | 1.27 ms: 1.01x slower                                            |
| mako                       | 13.2 ms                                                      | 13.3 ms: 1.02x slower                                            |
| pycparser                  | 1.22 sec                                                     | 1.24 sec: 1.02x slower                                           |
| unpickle_list              | 6.52 us                                                      | 6.64 us: 1.02x slower                                            |
| sqlglot_transpile          | 1.71 ms                                                      | 1.74 ms: 1.02x slower                                            |
| chaos                      | 68.3 ms                                                      | 69.7 ms: 1.02x slower                                            |
| pickle_pure_python         | 359 us                                                       | 366 us: 1.02x slower                                             |
| raytrace                   | 297 ms                                                       | 304 ms: 1.03x slower                                             |
| tomli_loads                | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                           |
| float                      | 91.4 ms                                                      | 94.4 ms: 1.03x slower                                            |
| pickle                     | 13.4 us                                                      | 13.9 us: 1.03x slower                                            |
| xml_etree_iterparse        | 147 ms                                                       | 152 ms: 1.04x slower                                             |
| fannkuch                   | 451 ms                                                       | 471 ms: 1.04x slower                                             |
| pyflate                    | 557 ms                                                       | 583 ms: 1.05x slower                                             |
| bench_mp_pool              | 7.03 ms                                                      | 5.20 sec: 740.14x slower                                         |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                     |

Benchmark hidden because not significant (35): tornado_http, sqlglot_normalize, logging_simple, coroutines, sqlglot_optimize, regex_v8, genshi_text, xml_etree_generate, xml_etree_process, hexiom, nqueens, django_template, comprehensions, logging_format, pidigits, sympy_str, genshi_xml, crypto_pyaes, scimark_monte_carlo, thrift, dulwich_log, spectral_norm, regex_effbot, python_startup, asyncio_websockets, mdp, sqlglot_parse, asyncio_tcp_ssl, sympy_expand, typing_runtime_protocols, xml_etree_parse, create_gc_cycles, python_startup_no_site, deltablue, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: unpack_sequence

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x