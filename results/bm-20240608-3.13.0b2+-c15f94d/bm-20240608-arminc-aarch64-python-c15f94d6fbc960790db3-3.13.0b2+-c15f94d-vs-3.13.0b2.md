# Results vs. 3.13.0b2

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-aarch64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.00x slower
- HPT reliability: 69.49%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (5): 2to3, chameleon, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 91.9 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                        | 1.00x faster                                                             |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 249 ms: 1.04x faster                                                     |
| regex_v8       | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                    |
| regex_compile  | 128 ms                                                       | 129 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                        | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads        | 2.57 sec                                                     | 2.54 sec: 1.01x faster                                                   |
| unpickle           | 19.8 us                                                      | 19.6 us: 1.01x faster                                                    |
| pickle             | 13.4 us                                                      | 13.6 us: 1.01x slower                                                    |
| pickle_pure_python | 359 us                                                       | 368 us: 1.03x slower                                                     |
| xml_etree_generate | 114 ms                                                       | 117 ms: 1.03x slower                                                     |
| json_dumps         | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                    |
| Geometric mean     | (ref)                                                        | 1.01x slower                                                             |

Benchmark hidden because not significant (8): unpickle_list, json_loads, unpickle_pure_python, pickle_dict, xml_etree_process, xml_etree_iterparse, xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                        | 1.02x slower                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, django_template, mako, genshi_xml

All benchmarks:
===============

| Benchmark          | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna          | 259 ms                                                       | 249 ms: 1.04x faster                                                     |
| gc_traversal       | 5.17 ms                                                      | 5.04 ms: 1.03x faster                                                    |
| comprehensions     | 20.5 us                                                      | 20.1 us: 1.02x faster                                                    |
| regex_v8           | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                    |
| regex_effbot       | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                    |
| telco              | 10.0 ms                                                      | 9.86 ms: 1.02x faster                                                    |
| tomli_loads        | 2.57 sec                                                     | 2.54 sec: 1.01x faster                                                   |
| fannkuch           | 451 ms                                                       | 447 ms: 1.01x faster                                                     |
| deepcopy_reduce    | 4.04 us                                                      | 4.00 us: 1.01x faster                                                    |
| unpickle           | 19.8 us                                                      | 19.6 us: 1.01x faster                                                    |
| mdp                | 3.33 sec                                                     | 3.31 sec: 1.01x faster                                                   |
| float              | 91.4 ms                                                      | 91.9 ms: 1.01x slower                                                    |
| generators         | 37.1 ms                                                      | 37.4 ms: 1.01x slower                                                    |
| sympy_expand       | 457 ms                                                       | 462 ms: 1.01x slower                                                     |
| regex_compile      | 128 ms                                                       | 129 ms: 1.01x slower                                                     |
| pprint_safe_repr   | 933 ms                                                       | 943 ms: 1.01x slower                                                     |
| scimark_sor        | 159 ms                                                       | 161 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl    | 2.21 sec                                                     | 2.24 sec: 1.01x slower                                                   |
| pickle             | 13.4 us                                                      | 13.6 us: 1.01x slower                                                    |
| python_startup     | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                                    |
| bench_thread_pool  | 1.26 ms                                                      | 1.28 ms: 1.02x slower                                                    |
| pickle_pure_python | 359 us                                                       | 368 us: 1.03x slower                                                     |
| xml_etree_generate | 114 ms                                                       | 117 ms: 1.03x slower                                                     |
| bench_mp_pool      | 7.03 ms                                                      | 7.22 ms: 1.03x slower                                                    |
| json_dumps         | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                    |
| aiohttp            | 1.18 ms                                                      | 1.22 ms: 1.03x slower                                                    |
| flaskblogging      | 4.70 ms                                                      | 4.87 ms: 1.04x slower                                                    |
| dulwich_log        | 58.5 ms                                                      | 61.0 ms: 1.04x slower                                                    |
| gunicorn           | 1.19 ms                                                      | 1.24 ms: 1.05x slower                                                    |
| Geometric mean     | (ref)                                                        | 1.00x slower                                                             |

Benchmark hidden because not significant (72): logging_simple, sqlglot_normalize, tornado_http, sqlglot_parse, deepcopy_memo, sqlglot_optimize, logging_format, mypy2, async_tree_io, nbody, scimark_monte_carlo, logging_silent, deltablue, typing_runtime_protocols, richards, unpickle_list, chaos, pycparser, pathlib, pyflate, meteor_contest, json_loads, async_tree_none_tg, async_tree_none, crypto_pyaes, async_generators, coverage, scimark_lu, docutils, hexiom, pprint_pformat, sympy_sum, async_tree_cpu_io_mixed_tg, spectral_norm, pidigits, richards_super, chameleon, deepcopy, json, go, async_tree_memoization_tg, async_tree_memoization, sqlite_synth, scimark_fft, html5lib, async_tree_cpu_io_mixed, create_gc_cycles, asyncio_websockets, pylint, asyncio_tcp, 2to3, async_tree_io_tg, dask, thrift, raytrace, genshi_text, unpickle_pure_python, nqueens, sympy_integrate, coroutines, django_template, sympy_str, pickle_dict, xml_etree_process, xml_etree_iterparse, xml_etree_parse, python_startup_no_site, pickle_list, scimark_sparse_mat_mult, mako, sqlglot_transpile, genshi_xml
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 69.49% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x