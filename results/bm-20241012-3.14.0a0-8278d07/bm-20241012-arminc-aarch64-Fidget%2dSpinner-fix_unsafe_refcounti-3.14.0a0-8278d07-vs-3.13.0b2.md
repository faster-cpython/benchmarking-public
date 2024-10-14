# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: linux-aarch64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.05x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 293 ms: 1.04x faster                                                              |
| docutils       | 3.10 sec                                                     | 3.03 sec: 1.02x faster                                                            |
| html5lib       | 66.1 ms                                                      | 63.2 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 645 ms                                                       | 551 ms: 1.17x faster                                                              |
| async_tree_none            | 492 ms                                                       | 422 ms: 1.17x faster                                                              |
| async_tree_none_tg         | 476 ms                                                       | 419 ms: 1.14x faster                                                              |
| async_tree_io_tg           | 1.27 sec                                                     | 1.13 sec: 1.12x faster                                                            |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 709 ms: 1.12x faster                                                              |
| async_tree_memoization_tg  | 604 ms                                                       | 550 ms: 1.10x faster                                                              |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 710 ms: 1.07x faster                                                              |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                            |
| Geometric mean             | (ref)                                                        | 1.12x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 93.9 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                       | 125 ms: 1.03x faster                                                              |
| regex_dna      | 259 ms                                                       | 254 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                      |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_loads           | 32.1 us                                                      | 31.2 us: 1.03x faster                                                             |
| xml_etree_process    | 80.8 ms                                                      | 79.0 ms: 1.02x faster                                                             |
| unpickle             | 19.8 us                                                      | 19.4 us: 1.02x faster                                                             |
| unpickle_pure_python | 251 us                                                       | 254 us: 1.01x slower                                                              |
| pickle               | 13.4 us                                                      | 13.6 us: 1.01x slower                                                             |
| tomli_loads          | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                            |
| json_dumps           | 13.1 ms                                                      | 14.7 ms: 1.12x slower                                                             |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                      |

Benchmark hidden because not significant (7): xml_etree_parse, xml_etree_generate, pickle_list, xml_etree_iterparse, unpickle_list, pickle_pure_python, pickle_dict

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 13.2 ms                                                      | 13.6 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 330 us: 1.36x faster                                                              |
| deepcopy_memo              | 50.8 us                                                      | 38.0 us: 1.34x faster                                                             |
| async_tree_memoization     | 645 ms                                                       | 551 ms: 1.17x faster                                                              |
| deepcopy_reduce            | 4.04 us                                                      | 3.46 us: 1.17x faster                                                             |
| go                         | 161 ms                                                       | 138 ms: 1.17x faster                                                              |
| async_tree_none            | 492 ms                                                       | 422 ms: 1.17x faster                                                              |
| async_tree_none_tg         | 476 ms                                                       | 419 ms: 1.14x faster                                                              |
| async_tree_io_tg           | 1.27 sec                                                     | 1.13 sec: 1.12x faster                                                            |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 709 ms: 1.12x faster                                                              |
| async_tree_memoization_tg  | 604 ms                                                       | 550 ms: 1.10x faster                                                              |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 710 ms: 1.07x faster                                                              |
| generators                 | 37.1 ms                                                      | 34.6 ms: 1.07x faster                                                             |
| telco                      | 10.0 ms                                                      | 9.35 ms: 1.07x faster                                                             |
| pathlib                    | 22.8 ms                                                      | 21.4 ms: 1.06x faster                                                             |
| richards                   | 55.9 ms                                                      | 52.6 ms: 1.06x faster                                                             |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                            |
| scimark_lu                 | 141 ms                                                       | 134 ms: 1.05x faster                                                              |
| richards_super             | 62.3 ms                                                      | 59.4 ms: 1.05x faster                                                             |
| html5lib                   | 66.1 ms                                                      | 63.2 ms: 1.05x faster                                                             |
| asyncio_tcp                | 584 ms                                                       | 562 ms: 1.04x faster                                                              |
| 2to3                       | 305 ms                                                       | 293 ms: 1.04x faster                                                              |
| thrift                     | 962 us                                                       | 926 us: 1.04x faster                                                              |
| scimark_fft                | 445 ms                                                       | 432 ms: 1.03x faster                                                              |
| json_loads                 | 32.1 us                                                      | 31.2 us: 1.03x faster                                                             |
| meteor_contest             | 113 ms                                                       | 110 ms: 1.03x faster                                                              |
| pprint_safe_repr           | 933 ms                                                       | 908 ms: 1.03x faster                                                              |
| pprint_pformat             | 1.93 sec                                                     | 1.88 sec: 1.03x faster                                                            |
| regex_compile              | 128 ms                                                       | 125 ms: 1.03x faster                                                              |
| async_generators           | 488 ms                                                       | 475 ms: 1.03x faster                                                              |
| xml_etree_process          | 80.8 ms                                                      | 79.0 ms: 1.02x faster                                                             |
| bpe_tokeniser              | 5.83 sec                                                     | 5.70 sec: 1.02x faster                                                            |
| docutils                   | 3.10 sec                                                     | 3.03 sec: 1.02x faster                                                            |
| logging_silent             | 133 ns                                                       | 131 ns: 1.02x faster                                                              |
| unpickle                   | 19.8 us                                                      | 19.4 us: 1.02x faster                                                             |
| sympy_sum                  | 144 ms                                                       | 141 ms: 1.02x faster                                                              |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.44 ms: 1.02x faster                                                             |
| regex_dna                  | 259 ms                                                       | 254 ms: 1.02x faster                                                              |
| coroutines                 | 29.0 ms                                                      | 28.6 ms: 1.02x faster                                                             |
| logging_format             | 7.82 us                                                      | 7.72 us: 1.01x faster                                                             |
| spectral_norm              | 141 ms                                                       | 139 ms: 1.01x faster                                                              |
| sympy_str                  | 265 ms                                                       | 263 ms: 1.01x faster                                                              |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.20 sec: 1.01x faster                                                            |
| gc_traversal               | 5.17 ms                                                      | 5.22 ms: 1.01x slower                                                             |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                             |
| unpickle_pure_python       | 251 us                                                       | 254 us: 1.01x slower                                                              |
| pickle                     | 13.4 us                                                      | 13.6 us: 1.01x slower                                                             |
| sqlite_synth               | 3.90 us                                                      | 3.95 us: 1.01x slower                                                             |
| pycparser                  | 1.22 sec                                                     | 1.24 sec: 1.02x slower                                                            |
| bench_thread_pool          | 1.26 ms                                                      | 1.28 ms: 1.02x slower                                                             |
| chaos                      | 68.3 ms                                                      | 69.6 ms: 1.02x slower                                                             |
| create_gc_cycles           | 2.33 ms                                                      | 2.39 ms: 1.02x slower                                                             |
| float                      | 91.4 ms                                                      | 93.9 ms: 1.03x slower                                                             |
| fannkuch                   | 451 ms                                                       | 464 ms: 1.03x slower                                                              |
| tomli_loads                | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                            |
| mako                       | 13.2 ms                                                      | 13.6 ms: 1.04x slower                                                             |
| pyflate                    | 557 ms                                                       | 580 ms: 1.04x slower                                                              |
| raytrace                   | 297 ms                                                       | 312 ms: 1.05x slower                                                              |
| json_dumps                 | 13.1 ms                                                      | 14.7 ms: 1.12x slower                                                             |
| bench_mp_pool              | 7.03 ms                                                      | 5.94 sec: 844.64x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                      |

Benchmark hidden because not significant (37): xml_etree_parse, sqlglot_normalize, tornado_http, sqlglot_parse, xml_etree_generate, pickle_list, genshi_text, crypto_pyaes, hexiom, scimark_sor, sqlglot_optimize, coverage, logging_simple, regex_v8, nbody, sympy_expand, xml_etree_iterparse, unpickle_list, pickle_pure_python, regex_effbot, scimark_monte_carlo, genshi_xml, python_startup, python_startup_no_site, mdp, pickle_dict, asyncio_websockets, pidigits, typing_runtime_protocols, nqueens, django_template, json, sympy_integrate, comprehensions, deltablue, dulwich_log, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: unpack_sequence

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x