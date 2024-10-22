# Results vs. 3.13.0

- fork: python
- ref: f4bc84d261c828ed81f1
- machine: linux-aarch64
- commit hash: f4bc84d
- commit date: 2024-07-17
- overall geometric mean: 1.01x faster
- HPT reliability: 64.69%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 301 ms: 1.01x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.06 sec: 1.05x slower                                                  |
| html5lib       | 64.3 ms                                                  | 68.0 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 534 ms: 1.22x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 407 ms: 1.15x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 551 ms: 1.14x faster                                                    |
| async_tree_none            | 493 ms                                                   | 439 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 729 ms: 1.05x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.07 sec: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 718 ms: 1.03x faster                                                    |
| async_generators           | 496 ms                                                   | 485 ms: 1.02x faster                                                    |
| asyncio_tcp                | 568 ms                                                   | 579 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 29.0 ms: 1.03x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 93.1 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.8 ms: 1.02x faster                                                   |
| regex_dna      | 246 ms                                                   | 252 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|--------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python | 359 us                                                   | 357 us: 1.01x faster                                                    |
| tomli_loads        | 2.53 sec                                                 | 2.56 sec: 1.01x slower                                                  |
| json_dumps         | 13.4 ms                                                  | 13.9 ms: 1.04x slower                                                   |
| json_loads         | 31.4 us                                                  | 33.1 us: 1.05x slower                                                   |
| Geometric mean     | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, unpickle_pure_python, xml_etree_parse, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.3 ms                                                  | 13.6 ms: 1.02x slower                                                   |
| genshi_xml     | 60.2 ms                                                  | 62.3 ms: 1.04x slower                                                   |
| genshi_text    | 27.7 ms                                                  | 28.8 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 329 us: 1.37x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 39.3 us: 1.30x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 534 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.42 us: 1.19x faster                                                   |
| async_tree_none_tg         | 467 ms                                                   | 407 ms: 1.15x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 551 ms: 1.14x faster                                                    |
| async_tree_none            | 493 ms                                                   | 439 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 729 ms: 1.05x faster                                                    |
| pathlib                    | 22.4 ms                                                  | 21.6 ms: 1.04x faster                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.07 sec: 1.03x faster                                                  |
| bench_mp_pool              | 7.30 ms                                                  | 7.08 ms: 1.03x faster                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.23 sec: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 718 ms: 1.03x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.8 ms: 1.02x faster                                                   |
| async_generators           | 496 ms                                                   | 485 ms: 1.02x faster                                                    |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.5 ms: 1.02x faster                                                   |
| 2to3                       | 306 ms                                                   | 301 ms: 1.01x faster                                                    |
| float                      | 94.4 ms                                                  | 93.1 ms: 1.01x faster                                                   |
| mdp                        | 3.36 sec                                                 | 3.33 sec: 1.01x faster                                                  |
| bpe_tokeniser              | 5.90 sec                                                 | 5.84 sec: 1.01x faster                                                  |
| pickle_pure_python         | 359 us                                                   | 357 us: 1.01x faster                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.40 ms: 1.01x slower                                                   |
| tomli_loads                | 2.53 sec                                                 | 2.56 sec: 1.01x slower                                                  |
| pprint_safe_repr           | 926 ms                                                   | 939 ms: 1.01x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.92 sec: 1.01x slower                                                  |
| sympy_str                  | 264 ms                                                   | 268 ms: 1.02x slower                                                    |
| sympy_expand               | 455 ms                                                   | 463 ms: 1.02x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 579 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                                  |
| mako                       | 13.3 ms                                                  | 13.6 ms: 1.02x slower                                                   |
| regex_dna                  | 246 ms                                                   | 252 ms: 1.02x slower                                                    |
| thrift                     | 946 us                                                   | 970 us: 1.03x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 29.0 ms: 1.03x slower                                                   |
| logging_simple             | 7.04 us                                                  | 7.28 us: 1.03x slower                                                   |
| genshi_xml                 | 60.2 ms                                                  | 62.3 ms: 1.04x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 28.8 ms: 1.04x slower                                                   |
| json_dumps                 | 13.4 ms                                                  | 13.9 ms: 1.04x slower                                                   |
| typing_runtime_protocols   | 192 us                                                   | 200 us: 1.04x slower                                                    |
| fannkuch                   | 452 ms                                                   | 470 ms: 1.04x slower                                                    |
| json                       | 5.61 ms                                                  | 5.85 ms: 1.04x slower                                                   |
| pyflate                    | 556 ms                                                   | 580 ms: 1.04x slower                                                    |
| json_loads                 | 31.4 us                                                  | 33.1 us: 1.05x slower                                                   |
| docutils                   | 2.91 sec                                                 | 3.06 sec: 1.05x slower                                                  |
| html5lib                   | 64.3 ms                                                  | 68.0 ms: 1.06x slower                                                   |
| telco                      | 9.73 ms                                                  | 10.3 ms: 1.06x slower                                                   |
| create_gc_cycles           | 2.12 ms                                                  | 2.29 ms: 1.08x slower                                                   |
| gc_traversal               | 4.53 ms                                                  | 5.07 ms: 1.12x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (39): pylint, tornado_http, crypto_pyaes, go, chaos, scimark_lu, logging_silent, xml_etree_generate, unpickle_pure_python, nbody, sqlglot_transpile, spectral_norm, xml_etree_parse, hexiom, richards_super, generators, pidigits, scimark_fft, sqlglot_optimize, xml_etree_iterparse, asyncio_websockets, django_template, richards, nqueens, logging_format, deltablue, coverage, comprehensions, scimark_sor, async_tree_io_tg, regex_compile, raytrace, regex_effbot, sympy_integrate, sqlglot_normalize, scimark_sparse_mat_mult, sympy_sum, xml_etree_process, python_startup_no_site
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240717-3.14.0a0-f4bc84d/bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d.json: dulwich_log

# HPT report

- Reliability score: 64.69% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x