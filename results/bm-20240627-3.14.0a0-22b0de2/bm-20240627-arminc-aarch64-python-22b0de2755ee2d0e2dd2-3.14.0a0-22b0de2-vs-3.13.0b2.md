# Results vs. 3.13.0b2

- fork: python
- ref: 22b0de2755ee2d0e2dd2
- machine: linux-aarch64
- commit hash: 22b0de2
- commit date: 2024-06-27
- overall geometric mean: 1.02x faster
- HPT reliability: 64.44%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.10 sec                                                     | 3.13 sec: 1.01x slower                                                  |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.09 sec: 1.16x faster                                                  |
| async_tree_none_tg         | 476 ms                                                       | 410 ms: 1.16x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.06 sec: 1.15x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 536 ms: 1.13x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 579 ms: 1.11x faster                                                    |
| async_tree_none            | 492 ms                                                       | 444 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 729 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 710 ms: 1.07x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.12x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 255 ms: 1.01x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.7 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|---------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate  | 114 ms                                                       | 113 ms: 1.01x faster                                                    |
| tomli_loads         | 2.57 sec                                                     | 2.56 sec: 1.00x faster                                                  |
| xml_etree_iterparse | 147 ms                                                       | 150 ms: 1.02x slower                                                    |
| json_loads          | 32.1 us                                                      | 33.3 us: 1.04x slower                                                   |
| json_dumps          | 13.1 ms                                                      | 13.7 ms: 1.04x slower                                                   |
| Geometric mean      | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 60.4 ms                                                      | 61.5 ms: 1.02x slower                                                   |
| mako           | 13.2 ms                                                      | 13.8 ms: 1.05x slower                                                   |
| genshi_text    | 27.4 ms                                                      | 28.8 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 333 us: 1.35x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 38.3 us: 1.33x faster                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.09 sec: 1.16x faster                                                  |
| deepcopy_reduce            | 4.04 us                                                      | 3.48 us: 1.16x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 410 ms: 1.16x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.06 sec: 1.15x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 536 ms: 1.13x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 579 ms: 1.11x faster                                                    |
| async_tree_none            | 492 ms                                                       | 444 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 729 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 710 ms: 1.07x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 4.90 ms: 1.06x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 21.7 ms: 1.05x faster                                                   |
| richards_super             | 62.3 ms                                                      | 59.7 ms: 1.04x faster                                                   |
| richards                   | 55.9 ms                                                      | 54.2 ms: 1.03x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 138 ms: 1.03x faster                                                    |
| create_gc_cycles           | 2.33 ms                                                      | 2.28 ms: 1.02x faster                                                   |
| logging_simple             | 7.21 us                                                      | 7.07 us: 1.02x faster                                                   |
| nbody                      | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| regex_dna                  | 259 ms                                                       | 255 ms: 1.01x faster                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.01x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.7 ms: 1.01x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 113 ms: 1.01x faster                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.56 sec: 1.00x faster                                                  |
| mdp                        | 3.33 sec                                                     | 3.34 sec: 1.00x slower                                                  |
| pyflate                    | 557 ms                                                       | 561 ms: 1.01x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.13 sec: 1.01x slower                                                  |
| scimark_fft                | 445 ms                                                       | 451 ms: 1.01x slower                                                    |
| generators                 | 37.1 ms                                                      | 37.6 ms: 1.01x slower                                                   |
| sympy_expand               | 457 ms                                                       | 464 ms: 1.02x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 61.5 ms: 1.02x slower                                                   |
| sympy_str                  | 265 ms                                                       | 270 ms: 1.02x slower                                                    |
| coverage                   | 98.4 ms                                                      | 100 ms: 1.02x slower                                                    |
| coroutines                 | 29.0 ms                                                      | 29.6 ms: 1.02x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 150 ms: 1.02x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 1.75 ms: 1.02x slower                                                   |
| json                       | 5.64 ms                                                      | 5.80 ms: 1.03x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 199 us: 1.03x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.99 sec: 1.03x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 964 ms: 1.03x slower                                                    |
| json_loads                 | 32.1 us                                                      | 33.3 us: 1.04x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.7 ms: 1.04x slower                                                   |
| mako                       | 13.2 ms                                                      | 13.8 ms: 1.05x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 28.8 ms: 1.05x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (47): xml_etree_parse, meteor_contest, telco, regex_effbot, asyncio_tcp, logging_format, deltablue, crypto_pyaes, xml_etree_process, bench_mp_pool, nqueens, django_template, pidigits, pickle_pure_python, python_startup, sqlglot_normalize, chaos, thrift, scimark_sor, bpe_tokeniser, asyncio_tcp_ssl, asyncio_websockets, sqlglot_optimize, sqlglot_parse, dask, go, async_generators, float, fannkuch, raytrace, comprehensions, unpickle_pure_python, pycparser, scimark_sparse_mat_mult, regex_compile, spectral_norm, hexiom, scimark_monte_carlo, tornado_http, sympy_sum, sympy_integrate, 2to3, dulwich_log, logging_silent, python_startup_no_site, pylint, html5lib
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 64.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x