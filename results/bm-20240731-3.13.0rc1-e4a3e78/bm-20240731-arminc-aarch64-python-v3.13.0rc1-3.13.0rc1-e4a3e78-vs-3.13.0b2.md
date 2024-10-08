# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc1
- machine: linux-aarch64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.00x slower
- HPT reliability: 82.94%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| chameleon      | 8.95 ms                                                      | 9.16 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                        | 1.00x slower                                                   |

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io_tg, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 253 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                        | 1.00x faster                                                   |

Benchmark hidden because not significant (3): regex_effbot, regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| json_loads          | 32.1 us                                                      | 31.4 us: 1.02x faster                                          |
| tomli_loads         | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                         |
| xml_etree_iterparse | 147 ms                                                       | 148 ms: 1.01x slower                                           |
| json_dumps          | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                          |
| Geometric mean      | (ref)                                                        | 1.00x slower                                                   |

Benchmark hidden because not significant (5): pickle_pure_python, xml_etree_process, xml_etree_generate, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.75 ms: 1.02x slower                                          |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml     | 60.4 ms                                                      | 62.0 ms: 1.03x slower                                          |
| genshi_text    | 27.4 ms                                                      | 28.4 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                        | 1.02x slower                                                   |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| richards               | 55.9 ms                                                      | 53.0 ms: 1.05x faster                                          |
| telco                  | 10.0 ms                                                      | 9.54 ms: 1.05x faster                                          |
| richards_super         | 62.3 ms                                                      | 59.9 ms: 1.04x faster                                          |
| json                   | 5.64 ms                                                      | 5.47 ms: 1.03x faster                                          |
| regex_dna              | 259 ms                                                       | 253 ms: 1.02x faster                                           |
| json_loads             | 32.1 us                                                      | 31.4 us: 1.02x faster                                          |
| logging_simple         | 7.21 us                                                      | 7.06 us: 1.02x faster                                          |
| gc_traversal           | 5.17 ms                                                      | 5.07 ms: 1.02x faster                                          |
| tomli_loads            | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                         |
| scimark_lu             | 141 ms                                                       | 139 ms: 1.02x faster                                           |
| thrift                 | 962 us                                                       | 949 us: 1.01x faster                                           |
| deepcopy_reduce        | 4.04 us                                                      | 4.01 us: 1.01x faster                                          |
| xml_etree_iterparse    | 147 ms                                                       | 148 ms: 1.01x slower                                           |
| mdp                    | 3.33 sec                                                     | 3.36 sec: 1.01x slower                                         |
| asyncio_tcp_ssl        | 2.21 sec                                                     | 2.24 sec: 1.01x slower                                         |
| bench_mp_pool          | 7.03 ms                                                      | 7.12 ms: 1.01x slower                                          |
| generators             | 37.1 ms                                                      | 37.7 ms: 1.02x slower                                          |
| pprint_safe_repr       | 933 ms                                                       | 948 ms: 1.02x slower                                           |
| python_startup_no_site | 8.60 ms                                                      | 8.75 ms: 1.02x slower                                          |
| bench_thread_pool      | 1.26 ms                                                      | 1.28 ms: 1.02x slower                                          |
| chameleon              | 8.95 ms                                                      | 9.16 ms: 1.02x slower                                          |
| sympy_integrate        | 20.9 ms                                                      | 21.4 ms: 1.02x slower                                          |
| genshi_xml             | 60.4 ms                                                      | 62.0 ms: 1.03x slower                                          |
| json_dumps             | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                          |
| genshi_text            | 27.4 ms                                                      | 28.4 ms: 1.03x slower                                          |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                   |

Benchmark hidden because not significant (67): sqlglot_parse, async_tree_io, sqlglot_normalize, pickle_pure_python, async_tree_memoization_tg, async_tree_cpu_io_mixed, xml_etree_process, pathlib, scimark_sparse_mat_mult, deepcopy_memo, coverage, xml_etree_generate, bpe_tokeniser, tornado_http, async_tree_cpu_io_mixed_tg, scimark_fft, 2to3, nqueens, asyncio_tcp, mypy2, comprehensions, float, scimark_sor, pycparser, pprint_pformat, spectral_norm, django_template, go, docutils, sqlglot_transpile, crypto_pyaes, regex_effbot, pidigits, html5lib, logging_format, create_gc_cycles, async_tree_none_tg, deltablue, regex_compile, raytrace, coroutines, typing_runtime_protocols, scimark_monte_carlo, nbody, async_tree_io_tg, deepcopy, chaos, fannkuch, sqlglot_optimize, async_tree_none, meteor_contest, sympy_str, python_startup, pyflate, sympy_expand, hexiom, async_tree_memoization, asyncio_websockets, regex_v8, unpickle_pure_python, dask, sympy_sum, async_generators, logging_silent, xml_etree_parse, mako, pylint
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, dulwich_log, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 82.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x