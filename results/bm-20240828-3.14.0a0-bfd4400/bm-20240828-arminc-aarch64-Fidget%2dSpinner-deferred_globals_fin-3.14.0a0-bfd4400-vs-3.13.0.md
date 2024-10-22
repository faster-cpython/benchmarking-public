# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-aarch64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.02x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 300 ms: 1.02x faster                                                              |
| docutils       | 2.91 sec                                                 | 3.13 sec: 1.08x slower                                                            |
| html5lib       | 64.3 ms                                                  | 66.2 ms: 1.03x slower                                                             |
| tornado_http   | 131 ms                                                   | 125 ms: 1.05x faster                                                              |
| Geometric mean | (ref)                                                    | 1.01x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 532 ms: 1.22x faster                                                              |
| async_tree_none_tg         | 467 ms                                                   | 398 ms: 1.17x faster                                                              |
| async_tree_memoization     | 626 ms                                                   | 553 ms: 1.13x faster                                                              |
| async_tree_none            | 493 ms                                                   | 436 ms: 1.13x faster                                                              |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 723 ms: 1.06x faster                                                              |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 698 ms: 1.05x faster                                                              |
| async_tree_io              | 1.11 sec                                                 | 1.07 sec: 1.03x faster                                                            |
| async_generators           | 496 ms                                                   | 487 ms: 1.02x faster                                                              |
| coroutines                 | 28.2 ms                                                  | 28.3 ms: 1.00x slower                                                             |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                                      |

Benchmark hidden because not significant (4): asyncio_tcp, asyncio_websockets, asyncio_tcp_ssl, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                                              |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.0 ms: 1.05x faster                                                             |
| regex_dna      | 246 ms                                                   | 253 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 359 us                                                   | 351 us: 1.02x faster                                                              |
| unpickle_pure_python | 254 us                                                   | 250 us: 1.02x faster                                                              |
| tomli_loads          | 2.53 sec                                                 | 2.57 sec: 1.02x slower                                                            |
| json_loads           | 31.4 us                                                  | 32.5 us: 1.04x slower                                                             |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                                      |

Benchmark hidden because not significant (5): json_dumps, xml_etree_generate, xml_etree_process, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): django_template, genshi_xml, genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 330 us: 1.37x faster                                                              |
| deepcopy_memo              | 51.0 us                                                  | 37.6 us: 1.36x faster                                                             |
| async_tree_memoization_tg  | 649 ms                                                   | 532 ms: 1.22x faster                                                              |
| deepcopy_reduce            | 4.07 us                                                  | 3.45 us: 1.18x faster                                                             |
| async_tree_none_tg         | 467 ms                                                   | 398 ms: 1.17x faster                                                              |
| async_tree_memoization     | 626 ms                                                   | 553 ms: 1.13x faster                                                              |
| async_tree_none            | 493 ms                                                   | 436 ms: 1.13x faster                                                              |
| generators                 | 37.8 ms                                                  | 34.8 ms: 1.09x faster                                                             |
| pathlib                    | 22.4 ms                                                  | 21.1 ms: 1.06x faster                                                             |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 723 ms: 1.06x faster                                                              |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 698 ms: 1.05x faster                                                              |
| tornado_http               | 131 ms                                                   | 125 ms: 1.05x faster                                                              |
| regex_v8                   | 31.5 ms                                                  | 30.0 ms: 1.05x faster                                                             |
| bench_mp_pool              | 7.30 ms                                                  | 7.00 ms: 1.04x faster                                                             |
| pycparser                  | 1.26 sec                                                 | 1.21 sec: 1.04x faster                                                            |
| logging_silent             | 135 ns                                                   | 130 ns: 1.04x faster                                                              |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                              |
| nbody                      | 114 ms                                                   | 110 ms: 1.04x faster                                                              |
| hexiom                     | 7.13 ms                                                  | 6.91 ms: 1.03x faster                                                             |
| async_tree_io              | 1.11 sec                                                 | 1.07 sec: 1.03x faster                                                            |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.39 ms: 1.03x faster                                                             |
| bench_thread_pool          | 1.28 ms                                                  | 1.24 ms: 1.03x faster                                                             |
| richards_super             | 60.3 ms                                                  | 58.6 ms: 1.03x faster                                                             |
| logging_format             | 7.83 us                                                  | 7.62 us: 1.03x faster                                                             |
| python_startup             | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                             |
| scimark_monte_carlo        | 83.8 ms                                                  | 81.6 ms: 1.03x faster                                                             |
| pickle_pure_python         | 359 us                                                   | 351 us: 1.02x faster                                                              |
| go                         | 163 ms                                                   | 159 ms: 1.02x faster                                                              |
| 2to3                       | 306 ms                                                   | 300 ms: 1.02x faster                                                              |
| richards                   | 53.5 ms                                                  | 52.5 ms: 1.02x faster                                                             |
| async_generators           | 496 ms                                                   | 487 ms: 1.02x faster                                                              |
| scimark_sor                | 159 ms                                                   | 156 ms: 1.02x faster                                                              |
| unpickle_pure_python       | 254 us                                                   | 250 us: 1.02x faster                                                              |
| sqlglot_normalize          | 128 ms                                                   | 126 ms: 1.01x faster                                                              |
| chaos                      | 68.8 ms                                                  | 67.9 ms: 1.01x faster                                                             |
| crypto_pyaes               | 82.7 ms                                                  | 81.7 ms: 1.01x faster                                                             |
| mdp                        | 3.36 sec                                                 | 3.33 sec: 1.01x faster                                                            |
| pprint_safe_repr           | 926 ms                                                   | 916 ms: 1.01x faster                                                              |
| pprint_pformat             | 1.90 sec                                                 | 1.88 sec: 1.01x faster                                                            |
| scimark_fft                | 447 ms                                                   | 444 ms: 1.01x faster                                                              |
| coroutines                 | 28.2 ms                                                  | 28.3 ms: 1.00x slower                                                             |
| bpe_tokeniser              | 5.90 sec                                                 | 5.94 sec: 1.01x slower                                                            |
| thrift                     | 946 us                                                   | 956 us: 1.01x slower                                                              |
| sympy_str                  | 264 ms                                                   | 268 ms: 1.02x slower                                                              |
| tomli_loads                | 2.53 sec                                                 | 2.57 sec: 1.02x slower                                                            |
| sympy_expand               | 455 ms                                                   | 462 ms: 1.02x slower                                                              |
| nqueens                    | 98.7 ms                                                  | 100 ms: 1.02x slower                                                              |
| json                       | 5.61 ms                                                  | 5.72 ms: 1.02x slower                                                             |
| regex_dna                  | 246 ms                                                   | 253 ms: 1.03x slower                                                              |
| html5lib                   | 64.3 ms                                                  | 66.2 ms: 1.03x slower                                                             |
| telco                      | 9.73 ms                                                  | 10.1 ms: 1.03x slower                                                             |
| typing_runtime_protocols   | 192 us                                                   | 198 us: 1.03x slower                                                              |
| json_loads                 | 31.4 us                                                  | 32.5 us: 1.04x slower                                                             |
| pyflate                    | 556 ms                                                   | 579 ms: 1.04x slower                                                              |
| fannkuch                   | 452 ms                                                   | 471 ms: 1.04x slower                                                              |
| gc_traversal               | 4.53 ms                                                  | 4.85 ms: 1.07x slower                                                             |
| docutils                   | 2.91 sec                                                 | 3.13 sec: 1.08x slower                                                            |
| create_gc_cycles           | 2.12 ms                                                  | 2.29 ms: 1.08x slower                                                             |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                                      |

Benchmark hidden because not significant (31): regex_compile, meteor_contest, django_template, asyncio_tcp, sqlglot_transpile, raytrace, deltablue, comprehensions, sqlglot_optimize, logging_simple, coverage, json_dumps, xml_etree_generate, python_startup_no_site, xml_etree_process, genshi_xml, asyncio_websockets, asyncio_tcp_ssl, float, pidigits, regex_effbot, spectral_norm, genshi_text, sympy_integrate, sympy_sum, xml_etree_iterparse, async_tree_io_tg, xml_etree_parse, mako, sqlglot_parse, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x