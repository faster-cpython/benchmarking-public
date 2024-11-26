# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc3
- machine: linux-aarch64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.014x faster
- HPT reliability: 99.44%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (5): 2to3, chameleon, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 726 ms: 1.06x faster                                           |
| async_tree_memoization     | 651 ms                                                   | 614 ms: 1.06x faster                                           |
| async_tree_io_tg           | 1.13 sec                                                 | 1.08 sec: 1.05x faster                                         |
| async_tree_none            | 497 ms                                                   | 489 ms: 1.02x faster                                           |
| async_tree_none_tg         | 470 ms                                                   | 464 ms: 1.01x faster                                           |
| async_tree_memoization_tg  | 649 ms                                                   | 643 ms: 1.01x faster                                           |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                   |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, coroutines, async_tree_io, asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.3 ms: 1.05x faster                                          |
| Geometric mean | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_iterparse  | 149 ms                                                   | 146 ms: 1.02x faster                                           |
| json_loads           | 31.7 us                                                  | 31.3 us: 1.01x faster                                          |
| pickle_pure_python   | 357 us                                                   | 363 us: 1.02x slower                                           |
| unpickle_pure_python | 251 us                                                   | 256 us: 1.02x slower                                           |
| Geometric mean       | (ref)                                                    | 1.00x faster                                                   |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_generate, xml_etree_process, tomli_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.2 ms: 1.17x faster                                          |
| Geometric mean | (ref)                                                    | 1.08x faster                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| mako           | 13.4 ms                                                  | 13.3 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                    | 1.00x slower                                                   |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.14 ms: 1.56x faster                                          |
| gc_traversal               | 5.77 ms                                                  | 4.56 ms: 1.27x faster                                          |
| python_startup             | 15.4 ms                                                  | 13.2 ms: 1.17x faster                                          |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 726 ms: 1.06x faster                                           |
| async_tree_memoization     | 651 ms                                                   | 614 ms: 1.06x faster                                           |
| regex_v8                   | 31.8 ms                                                  | 30.3 ms: 1.05x faster                                          |
| bench_mp_pool              | 7.68 ms                                                  | 7.33 ms: 1.05x faster                                          |
| async_tree_io_tg           | 1.13 sec                                                 | 1.08 sec: 1.05x faster                                         |
| json                       | 5.73 ms                                                  | 5.53 ms: 1.04x faster                                          |
| thrift                     | 968 us                                                   | 947 us: 1.02x faster                                           |
| crypto_pyaes               | 83.7 ms                                                  | 81.9 ms: 1.02x faster                                          |
| xml_etree_iterparse        | 149 ms                                                   | 146 ms: 1.02x faster                                           |
| fannkuch                   | 461 ms                                                   | 452 ms: 1.02x faster                                           |
| async_tree_none            | 497 ms                                                   | 489 ms: 1.02x faster                                           |
| pycparser                  | 1.27 sec                                                 | 1.26 sec: 1.01x faster                                         |
| async_tree_none_tg         | 470 ms                                                   | 464 ms: 1.01x faster                                           |
| sympy_sum                  | 144 ms                                                   | 142 ms: 1.01x faster                                           |
| raytrace                   | 300 ms                                                   | 296 ms: 1.01x faster                                           |
| json_loads                 | 31.7 us                                                  | 31.3 us: 1.01x faster                                          |
| async_tree_memoization_tg  | 649 ms                                                   | 643 ms: 1.01x faster                                           |
| mako                       | 13.4 ms                                                  | 13.3 ms: 1.01x faster                                          |
| mdp                        | 3.34 sec                                                 | 3.35 sec: 1.00x slower                                         |
| pyflate                    | 556 ms                                                   | 561 ms: 1.01x slower                                           |
| pickle_pure_python         | 357 us                                                   | 363 us: 1.02x slower                                           |
| richards_super             | 60.1 ms                                                  | 61.1 ms: 1.02x slower                                          |
| deepcopy_reduce            | 4.07 us                                                  | 4.14 us: 1.02x slower                                          |
| go                         | 160 ms                                                   | 163 ms: 1.02x slower                                           |
| unpickle_pure_python       | 251 us                                                   | 256 us: 1.02x slower                                           |
| deepcopy                   | 447 us                                                   | 459 us: 1.02x slower                                           |
| deepcopy_memo              | 50.4 us                                                  | 51.7 us: 1.03x slower                                          |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (59): xml_etree_parse, html5lib, logging_format, xml_etree_generate, nqueens, coverage, scimark_monte_carlo, hexiom, spectral_norm, async_tree_cpu_io_mixed, logging_simple, scimark_sor, telco, sqlglot_transpile, nbody, bench_thread_pool, xml_etree_process, meteor_contest, chameleon, tomli_loads, django_template, regex_dna, docutils, coroutines, async_tree_io, bpe_tokeniser, 2to3, richards, pylint, sympy_str, deltablue, pprint_pformat, scimark_fft, typing_runtime_protocols, sqlglot_parse, asyncio_websockets, pprint_safe_repr, pidigits, python_startup_no_site, scimark_lu, regex_effbot, comprehensions, sympy_expand, pathlib, generators, logging_silent, float, scimark_sparse_mat_mult, json_dumps, sqlglot_normalize, async_generators, chaos, sympy_integrate, genshi_text, regex_compile, sqlglot_optimize, genshi_xml, mypy2, tornado_http
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.014x faster
# HPT report

- Reliability score: 99.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.90x