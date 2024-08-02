# Results vs. 3.13.0b2

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: linux-aarch64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.03x slower
- HPT reliability: 81.92%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (5): 2to3, chameleon, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.23 sec: 1.04x faster                                                  |
| async_tree_none_tg         | 476 ms                                                       | 465 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 789 ms: 1.03x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (5): async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| float          | 91.4 ms                                                      | 90.2 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.7 ms: 1.01x faster                                                   |
| regex_compile  | 128 ms                                                       | 130 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|---------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_process   | 80.8 ms                                                      | 79.3 ms: 1.02x faster                                                   |
| xml_etree_generate  | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| pickle_list         | 5.27 us                                                      | 5.20 us: 1.01x faster                                                   |
| unpickle            | 19.8 us                                                      | 19.6 us: 1.01x faster                                                   |
| pickle_dict         | 37.6 us                                                      | 37.3 us: 1.01x faster                                                   |
| tomli_loads         | 2.57 sec                                                     | 2.58 sec: 1.00x slower                                                  |
| unpickle_list       | 6.52 us                                                      | 6.59 us: 1.01x slower                                                   |
| json_dumps          | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| xml_etree_iterparse | 147 ms                                                       | 149 ms: 1.02x slower                                                    |
| pickle              | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| Geometric mean      | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (4): unpickle_pure_python, pickle_pure_python, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 12.5 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.2 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| genshi_text    | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| richards                   | 55.9 ms                                                      | 53.4 ms: 1.05x faster                                                   |
| python_startup             | 13.0 ms                                                      | 12.5 ms: 1.04x faster                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.23 sec: 1.04x faster                                                  |
| richards_super             | 62.3 ms                                                      | 60.3 ms: 1.03x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 465 ms: 1.03x faster                                                    |
| scimark_lu                 | 141 ms                                                       | 138 ms: 1.02x faster                                                    |
| nbody                      | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| xml_etree_process          | 80.8 ms                                                      | 79.3 ms: 1.02x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| regex_dna                  | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| pickle_list                | 5.27 us                                                      | 5.20 us: 1.01x faster                                                   |
| float                      | 91.4 ms                                                      | 90.2 ms: 1.01x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.7 ms: 1.01x faster                                                   |
| scimark_sor                | 159 ms                                                       | 158 ms: 1.01x faster                                                    |
| unpickle                   | 19.8 us                                                      | 19.6 us: 1.01x faster                                                   |
| coverage                   | 98.4 ms                                                      | 97.5 ms: 1.01x faster                                                   |
| pickle_dict                | 37.6 us                                                      | 37.3 us: 1.01x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 5.14 ms: 1.01x faster                                                   |
| pprint_pformat             | 1.93 sec                                                     | 1.92 sec: 1.00x faster                                                  |
| tomli_loads                | 2.57 sec                                                     | 2.58 sec: 1.00x slower                                                  |
| mako                       | 13.2 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.35 sec: 1.01x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 941 ms: 1.01x slower                                                    |
| asyncio_websockets         | 657 ms                                                       | 663 ms: 1.01x slower                                                    |
| unpickle_list              | 6.52 us                                                      | 6.59 us: 1.01x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| deepcopy                   | 448 us                                                       | 454 us: 1.01x slower                                                    |
| regex_compile              | 128 ms                                                       | 130 ms: 1.01x slower                                                    |
| sympy_str                  | 265 ms                                                       | 269 ms: 1.01x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 7.14 ms: 1.02x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 149 ms: 1.02x slower                                                    |
| pathlib                    | 22.8 ms                                                      | 23.1 ms: 1.02x slower                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.28 ms: 1.02x slower                                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 83.9 ms: 1.02x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 1.75 ms: 1.02x slower                                                   |
| fannkuch                   | 451 ms                                                       | 461 ms: 1.02x slower                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 4.15 us: 1.03x slower                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 2.40 ms: 1.03x slower                                                   |
| pickle                     | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 789 ms: 1.03x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 21.6 ms: 1.04x slower                                                   |
| dask                       | 370 ms                                                       | 384 ms: 1.04x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 149 ms: 1.04x slower                                                    |
| pyflate                    | 557 ms                                                       | 581 ms: 1.04x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 61.4 ms: 1.05x slower                                                   |
| generators                 | 37.1 ms                                                      | 39.3 ms: 1.06x slower                                                   |
| flaskblogging              | 4.70 ms                                                      | 4.98 ms: 1.06x slower                                                   |
| telco                      | 10.0 ms                                                      | 164 ms: 16.35x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (49): sqlglot_parse, asyncio_tcp, thrift, async_tree_none, regex_effbot, django_template, nqueens, logging_format, logging_simple, chaos, deltablue, python_startup_no_site, scimark_fft, meteor_contest, docutils, async_tree_memoization, asyncio_tcp_ssl, raytrace, sqlglot_normalize, crypto_pyaes, sqlite_synth, spectral_norm, pycparser, sqlglot_optimize, async_tree_cpu_io_mixed, logging_silent, async_tree_io, pidigits, async_generators, unpickle_pure_python, 2to3, sympy_expand, pickle_pure_python, chameleon, go, json, scimark_sparse_mat_mult, hexiom, coroutines, json_loads, genshi_xml, xml_etree_parse, deepcopy_memo, typing_runtime_protocols, html5lib, comprehensions, pylint, async_tree_memoization_tg, tornado_http
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 81.92% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x