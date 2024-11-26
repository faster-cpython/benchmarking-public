# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b1
- machine: linux-aarch64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.028x slower
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| chameleon      | 9.08 ms                                                  | 9.23 ms: 1.02x slower                                        |
| docutils       | 2.89 sec                                                 | 3.12 sec: 1.08x slower                                       |
| Geometric mean | (ref)                                                    | 1.02x slower                                                 |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 628 ms: 1.03x faster                                         |
| asyncio_websockets         | 659 ms                                                   | 666 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 795 ms: 1.03x slower                                         |
| coroutines                 | 28.5 ms                                                  | 29.7 ms: 1.04x slower                                        |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 799 ms: 1.04x slower                                         |
| async_tree_io_tg           | 1.13 sec                                                 | 1.23 sec: 1.09x slower                                       |
| async_tree_io              | 1.11 sec                                                 | 1.21 sec: 1.09x slower                                       |
| Geometric mean             | (ref)                                                    | 1.02x slower                                                 |

Benchmark hidden because not significant (4): async_tree_none, async_tree_memoization, async_generators, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                         |
| float          | 93.3 ms                                                  | 90.7 ms: 1.03x faster                                        |
| pidigits       | 234 ms                                                   | 236 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                    | 1.02x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 253 ms                                                   | 257 ms: 1.01x slower                                         |
| regex_compile  | 127 ms                                                   | 130 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 251 us                                                   | 255 us: 1.02x slower                                         |
| pickle_pure_python   | 357 us                                                   | 363 us: 1.02x slower                                         |
| json_loads           | 31.7 us                                                  | 32.3 us: 1.02x slower                                        |
| tomli_loads          | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                       |
| Geometric mean       | (ref)                                                    | 1.02x slower                                                 |

Benchmark hidden because not significant (5): json_dumps, xml_etree_iterparse, xml_etree_parse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 12.6 ms: 1.22x faster                                        |
| python_startup_no_site | 8.73 ms                                                  | 8.49 ms: 1.03x faster                                        |
| Geometric mean         | (ref)                                                    | 1.12x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.2 ms: 1.02x faster                                        |
| django_template | 41.6 ms                                                  | 42.6 ms: 1.02x slower                                        |
| Geometric mean  | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mypy2                      | 1.15 sec                                                 | 771 ms: 1.50x faster                                         |
| create_gc_cycles           | 3.35 ms                                                  | 2.43 ms: 1.38x faster                                        |
| python_startup             | 15.4 ms                                                  | 12.6 ms: 1.22x faster                                        |
| gc_traversal               | 5.77 ms                                                  | 5.09 ms: 1.13x faster                                        |
| bench_mp_pool              | 7.68 ms                                                  | 7.04 ms: 1.09x faster                                        |
| nbody                      | 114 ms                                                   | 110 ms: 1.04x faster                                         |
| async_tree_memoization_tg  | 649 ms                                                   | 628 ms: 1.03x faster                                         |
| pycparser                  | 1.27 sec                                                 | 1.23 sec: 1.03x faster                                       |
| float                      | 93.3 ms                                                  | 90.7 ms: 1.03x faster                                        |
| python_startup_no_site     | 8.73 ms                                                  | 8.49 ms: 1.03x faster                                        |
| spectral_norm              | 143 ms                                                   | 139 ms: 1.02x faster                                         |
| thrift                     | 968 us                                                   | 946 us: 1.02x faster                                         |
| chaos                      | 68.0 ms                                                  | 66.5 ms: 1.02x faster                                        |
| crypto_pyaes               | 83.7 ms                                                  | 82.4 ms: 1.02x faster                                        |
| mako                       | 13.4 ms                                                  | 13.2 ms: 1.02x faster                                        |
| scimark_fft                | 447 ms                                                   | 442 ms: 1.01x faster                                         |
| raytrace                   | 300 ms                                                   | 297 ms: 1.01x faster                                         |
| pidigits                   | 234 ms                                                   | 236 ms: 1.01x slower                                         |
| asyncio_websockets         | 659 ms                                                   | 666 ms: 1.01x slower                                         |
| regex_dna                  | 253 ms                                                   | 257 ms: 1.01x slower                                         |
| sympy_sum                  | 144 ms                                                   | 146 ms: 1.02x slower                                         |
| chameleon                  | 9.08 ms                                                  | 9.23 ms: 1.02x slower                                        |
| pathlib                    | 22.7 ms                                                  | 23.1 ms: 1.02x slower                                        |
| unpickle_pure_python       | 251 us                                                   | 255 us: 1.02x slower                                         |
| sqlglot_normalize          | 127 ms                                                   | 129 ms: 1.02x slower                                         |
| pickle_pure_python         | 357 us                                                   | 363 us: 1.02x slower                                         |
| json_loads                 | 31.7 us                                                  | 32.3 us: 1.02x slower                                        |
| django_template            | 41.6 ms                                                  | 42.6 ms: 1.02x slower                                        |
| sympy_str                  | 264 ms                                                   | 270 ms: 1.02x slower                                         |
| pprint_pformat             | 1.90 sec                                                 | 1.94 sec: 1.02x slower                                       |
| pprint_safe_repr           | 926 ms                                                   | 948 ms: 1.02x slower                                         |
| regex_compile              | 127 ms                                                   | 130 ms: 1.02x slower                                         |
| sympy_integrate            | 20.8 ms                                                  | 21.4 ms: 1.03x slower                                        |
| sympy_expand               | 457 ms                                                   | 470 ms: 1.03x slower                                         |
| sqlglot_parse              | 1.38 ms                                                  | 1.42 ms: 1.03x slower                                        |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 795 ms: 1.03x slower                                         |
| tomli_loads                | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                       |
| coroutines                 | 28.5 ms                                                  | 29.7 ms: 1.04x slower                                        |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 799 ms: 1.04x slower                                         |
| richards_super             | 60.1 ms                                                  | 62.8 ms: 1.04x slower                                        |
| richards                   | 53.6 ms                                                  | 56.3 ms: 1.05x slower                                        |
| typing_runtime_protocols   | 193 us                                                   | 203 us: 1.05x slower                                         |
| pyflate                    | 556 ms                                                   | 595 ms: 1.07x slower                                         |
| docutils                   | 2.89 sec                                                 | 3.12 sec: 1.08x slower                                       |
| async_tree_io_tg           | 1.13 sec                                                 | 1.23 sec: 1.09x slower                                       |
| async_tree_io              | 1.11 sec                                                 | 1.21 sec: 1.09x slower                                       |
| telco                      | 9.74 ms                                                  | 167 ms: 17.19x slower                                        |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                 |

Benchmark hidden because not significant (41): json, json_dumps, async_tree_none, regex_v8, async_tree_memoization, generators, scimark_monte_carlo, coverage, hexiom, logging_format, async_generators, comprehensions, scimark_sor, meteor_contest, mdp, go, scimark_lu, sqlglot_transpile, html5lib, bench_thread_pool, deepcopy_reduce, pylint, async_tree_none_tg, xml_etree_iterparse, scimark_sparse_mat_mult, fannkuch, 2to3, regex_effbot, nqueens, logging_simple, genshi_text, deepcopy_memo, xml_etree_parse, logging_silent, deepcopy, tornado_http, xml_etree_process, deltablue, sqlglot_optimize, genshi_xml, xml_etree_generate
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.028x slower
# HPT report

- Reliability score: 99.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.90x