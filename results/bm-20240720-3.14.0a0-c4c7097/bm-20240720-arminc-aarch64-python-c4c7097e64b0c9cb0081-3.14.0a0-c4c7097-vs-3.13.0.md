# Results vs. 3.13.0

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: linux-aarch64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.01x faster
- HPT reliability: 85.37%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 303 ms: 1.01x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.09 sec: 1.06x slower                                                  |
| html5lib       | 64.3 ms                                                  | 68.0 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 536 ms: 1.21x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 413 ms: 1.13x faster                                                    |
| async_tree_none            | 493 ms                                                   | 446 ms: 1.11x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 574 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 732 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 718 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.14 sec: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (5): async_generators, coroutines, asyncio_websockets, asyncio_tcp, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 91.9 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| regex_dna      | 246 ms                                                   | 251 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|--------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse    | 188 ms                                                   | 186 ms: 1.01x faster                                                    |
| pickle_pure_python | 359 us                                                   | 364 us: 1.01x slower                                                    |
| tomli_loads        | 2.53 sec                                                 | 2.56 sec: 1.01x slower                                                  |
| json_loads         | 31.4 us                                                  | 33.5 us: 1.07x slower                                                   |
| Geometric mean     | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (5): unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.3 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| genshi_xml     | 60.2 ms                                                  | 60.9 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 332 us: 1.36x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 38.7 us: 1.32x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 536 ms: 1.21x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.50 us: 1.16x faster                                                   |
| async_tree_none_tg         | 467 ms                                                   | 413 ms: 1.13x faster                                                    |
| async_tree_none            | 493 ms                                                   | 446 ms: 1.11x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 574 ms: 1.09x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.9 ms: 1.08x faster                                                   |
| logging_silent             | 135 ns                                                   | 129 ns: 1.05x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 732 ms: 1.04x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 21.6 ms: 1.04x faster                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 7.09 ms: 1.03x faster                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 81.5 ms: 1.03x faster                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.23 sec: 1.03x faster                                                  |
| float                      | 94.4 ms                                                  | 91.9 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 718 ms: 1.02x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 136 ms: 1.02x faster                                                    |
| richards                   | 53.5 ms                                                  | 52.3 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.43 ms: 1.02x faster                                                   |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| hexiom                     | 7.13 ms                                                  | 6.99 ms: 1.02x faster                                                   |
| richards_super             | 60.3 ms                                                  | 59.2 ms: 1.02x faster                                                   |
| go                         | 163 ms                                                   | 160 ms: 1.02x faster                                                    |
| scimark_fft                | 447 ms                                                   | 441 ms: 1.02x faster                                                    |
| 2to3                       | 306 ms                                                   | 303 ms: 1.01x faster                                                    |
| bpe_tokeniser              | 5.90 sec                                                 | 5.85 sec: 1.01x faster                                                  |
| xml_etree_parse            | 188 ms                                                   | 186 ms: 1.01x faster                                                    |
| sqlglot_optimize           | 62.4 ms                                                  | 61.9 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                  |
| pprint_pformat             | 1.90 sec                                                 | 1.91 sec: 1.01x slower                                                  |
| coverage                   | 98.5 ms                                                  | 99.4 ms: 1.01x slower                                                   |
| nqueens                    | 98.7 ms                                                  | 99.7 ms: 1.01x slower                                                   |
| mako                       | 13.3 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| comprehensions             | 20.4 us                                                  | 20.6 us: 1.01x slower                                                   |
| typing_runtime_protocols   | 192 us                                                   | 194 us: 1.01x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 60.9 ms: 1.01x slower                                                   |
| sympy_str                  | 264 ms                                                   | 267 ms: 1.01x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 364 us: 1.01x slower                                                    |
| fannkuch                   | 452 ms                                                   | 458 ms: 1.01x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 940 ms: 1.01x slower                                                    |
| tomli_loads                | 2.53 sec                                                 | 2.56 sec: 1.01x slower                                                  |
| thrift                     | 946 us                                                   | 961 us: 1.02x slower                                                    |
| regex_dna                  | 246 ms                                                   | 251 ms: 1.02x slower                                                    |
| logging_simple             | 7.04 us                                                  | 7.18 us: 1.02x slower                                                   |
| telco                      | 9.73 ms                                                  | 9.93 ms: 1.02x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.02x slower                                                   |
| pyflate                    | 556 ms                                                   | 574 ms: 1.03x slower                                                    |
| json                       | 5.61 ms                                                  | 5.81 ms: 1.04x slower                                                   |
| dask                       | 350 ms                                                   | 364 ms: 1.04x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.14 sec: 1.05x slower                                                  |
| html5lib                   | 64.3 ms                                                  | 68.0 ms: 1.06x slower                                                   |
| docutils                   | 2.91 sec                                                 | 3.09 sec: 1.06x slower                                                  |
| json_loads                 | 31.4 us                                                  | 33.5 us: 1.07x slower                                                   |
| create_gc_cycles           | 2.12 ms                                                  | 2.33 ms: 1.10x slower                                                   |
| gc_traversal               | 4.53 ms                                                  | 4.99 ms: 1.10x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (32): pylint, tornado_http, unpickle_pure_python, xml_etree_generate, django_template, crypto_pyaes, spectral_norm, async_generators, deltablue, regex_compile, scimark_sor, genshi_text, chaos, mdp, sqlglot_normalize, nbody, pidigits, xml_etree_iterparse, coroutines, sqlglot_transpile, logging_format, asyncio_websockets, json_dumps, sympy_sum, sympy_expand, sympy_integrate, asyncio_tcp, raytrace, regex_effbot, async_tree_io, xml_etree_process, python_startup_no_site
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: dulwich_log

# HPT report

- Reliability score: 85.37% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x