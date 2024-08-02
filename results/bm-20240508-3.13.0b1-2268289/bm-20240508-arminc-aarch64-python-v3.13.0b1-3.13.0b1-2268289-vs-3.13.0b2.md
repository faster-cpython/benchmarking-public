# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0b1
- machine: linux-aarch64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.04x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| chameleon      | 8.95 ms                                                      | 9.23 ms: 1.03x slower                                        |
| html5lib       | 66.1 ms                                                      | 66.6 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.23 sec: 1.03x faster                                       |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 795 ms: 1.04x slower                                         |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                 |

Benchmark hidden because not significant (6): async_tree_io, async_tree_none_tg, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 110 ms: 1.03x faster                                         |
| float          | 91.4 ms                                                      | 90.7 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.93 ms: 1.01x faster                                        |
| regex_compile  | 128 ms                                                       | 130 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                        | 1.00x slower                                                 |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_list        | 6.52 us                                                      | 6.31 us: 1.03x faster                                        |
| unpickle             | 19.8 us                                                      | 19.5 us: 1.01x faster                                        |
| json_loads           | 32.1 us                                                      | 32.3 us: 1.01x slower                                        |
| pickle_dict          | 37.6 us                                                      | 38.0 us: 1.01x slower                                        |
| unpickle_pure_python | 251 us                                                       | 255 us: 1.01x slower                                         |
| xml_etree_process    | 80.8 ms                                                      | 82.2 ms: 1.02x slower                                        |
| pickle               | 13.4 us                                                      | 13.7 us: 1.02x slower                                        |
| tomli_loads          | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                       |
| xml_etree_iterparse  | 147 ms                                                       | 150 ms: 1.03x slower                                         |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (5): pickle_list, pickle_pure_python, json_dumps, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 12.6 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (3): mako, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_tcp                | 584 ms                                                       | 545 ms: 1.07x faster                                         |
| async_tree_io_tg           | 1.27 sec                                                     | 1.23 sec: 1.03x faster                                       |
| nbody                      | 114 ms                                                       | 110 ms: 1.03x faster                                         |
| unpickle_list              | 6.52 us                                                      | 6.31 us: 1.03x faster                                        |
| python_startup             | 13.0 ms                                                      | 12.6 ms: 1.03x faster                                        |
| chaos                      | 68.3 ms                                                      | 66.5 ms: 1.03x faster                                        |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.17 sec: 1.02x faster                                       |
| gc_traversal               | 5.17 ms                                                      | 5.09 ms: 1.02x faster                                        |
| thrift                     | 962 us                                                       | 946 us: 1.02x faster                                         |
| scimark_lu                 | 141 ms                                                       | 139 ms: 1.01x faster                                         |
| unpickle                   | 19.8 us                                                      | 19.5 us: 1.01x faster                                        |
| regex_effbot               | 4.98 ms                                                      | 4.93 ms: 1.01x faster                                        |
| float                      | 91.4 ms                                                      | 90.7 ms: 1.01x faster                                        |
| scimark_fft                | 445 ms                                                       | 442 ms: 1.01x faster                                         |
| pprint_pformat             | 1.93 sec                                                     | 1.94 sec: 1.00x slower                                       |
| json_loads                 | 32.1 us                                                      | 32.3 us: 1.01x slower                                        |
| html5lib                   | 66.1 ms                                                      | 66.6 ms: 1.01x slower                                        |
| pickle_dict                | 37.6 us                                                      | 38.0 us: 1.01x slower                                        |
| pycparser                  | 1.22 sec                                                     | 1.23 sec: 1.01x slower                                       |
| deepcopy_reduce            | 4.04 us                                                      | 4.09 us: 1.01x slower                                        |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                        |
| pathlib                    | 22.8 ms                                                      | 23.1 ms: 1.01x slower                                        |
| asyncio_websockets         | 657 ms                                                       | 666 ms: 1.01x slower                                         |
| unpickle_pure_python       | 251 us                                                       | 255 us: 1.01x slower                                         |
| sympy_sum                  | 144 ms                                                       | 146 ms: 1.02x slower                                         |
| pprint_safe_repr           | 933 ms                                                       | 948 ms: 1.02x slower                                         |
| regex_compile              | 128 ms                                                       | 130 ms: 1.02x slower                                         |
| bench_thread_pool          | 1.26 ms                                                      | 1.28 ms: 1.02x slower                                        |
| xml_etree_process          | 80.8 ms                                                      | 82.2 ms: 1.02x slower                                        |
| dulwich_log                | 58.5 ms                                                      | 59.5 ms: 1.02x slower                                        |
| sympy_str                  | 265 ms                                                       | 270 ms: 1.02x slower                                         |
| nqueens                    | 98.9 ms                                                      | 101 ms: 1.02x slower                                         |
| genshi_text                | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                        |
| coroutines                 | 29.0 ms                                                      | 29.7 ms: 1.02x slower                                        |
| pickle                     | 13.4 us                                                      | 13.7 us: 1.02x slower                                        |
| sympy_integrate            | 20.9 ms                                                      | 21.4 ms: 1.03x slower                                        |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                       |
| xml_etree_iterparse        | 147 ms                                                       | 150 ms: 1.03x slower                                         |
| sympy_expand               | 457 ms                                                       | 470 ms: 1.03x slower                                         |
| fannkuch                   | 451 ms                                                       | 465 ms: 1.03x slower                                         |
| chameleon                  | 8.95 ms                                                      | 9.23 ms: 1.03x slower                                        |
| create_gc_cycles           | 2.33 ms                                                      | 2.43 ms: 1.04x slower                                        |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 795 ms: 1.04x slower                                         |
| typing_runtime_protocols   | 193 us                                                       | 203 us: 1.05x slower                                         |
| pyflate                    | 557 ms                                                       | 595 ms: 1.07x slower                                         |
| telco                      | 10.0 ms                                                      | 167 ms: 16.72x slower                                        |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                 |

Benchmark hidden because not significant (55): spectral_norm, python_startup_no_site, async_tree_io, comprehensions, async_tree_none_tg, logging_simple, regex_dna, go, logging_format, sqlglot_normalize, sqlite_synth, pickle_list, async_tree_none, sqlglot_parse, async_generators, hexiom, async_tree_memoization, meteor_contest, raytrace, mako, scimark_sor, bench_mp_pool, scimark_sparse_mat_mult, json, mdp, coverage, 2to3, deepcopy_memo, mypy2, crypto_pyaes, generators, docutils, django_template, pidigits, deltablue, richards_super, richards, logging_silent, async_tree_cpu_io_mixed, scimark_monte_carlo, deepcopy, regex_v8, pickle_pure_python, aiohttp, sqlglot_optimize, dask, pylint, tornado_http, gunicorn, genshi_xml, json_dumps, flaskblogging, async_tree_memoization_tg, xml_etree_generate, xml_etree_parse
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x