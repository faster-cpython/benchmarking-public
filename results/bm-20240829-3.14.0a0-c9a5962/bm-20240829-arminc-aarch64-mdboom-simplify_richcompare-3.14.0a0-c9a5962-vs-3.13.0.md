# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.02x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 295 ms: 1.04x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.04 sec: 1.04x slower                                                  |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 548 ms: 1.19x faster                                                    |
| async_tree_none            | 493 ms                                                   | 426 ms: 1.16x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 553 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 417 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 726 ms: 1.05x faster                                                    |
| async_generators           | 496 ms                                                   | 480 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 725 ms: 1.02x faster                                                    |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.02x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): asyncio_tcp, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| float          | 94.4 ms                                                  | 93.4 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| regex_compile  | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| regex_dna      | 246 ms                                                   | 254 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 254 us                                                   | 252 us: 1.01x faster                                                    |
| json_loads           | 31.4 us                                                  | 32.4 us: 1.03x slower                                                   |
| tomli_loads          | 2.53 sec                                                 | 2.64 sec: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (6): pickle_pure_python, json_dumps, xml_etree_generate, xml_etree_iterparse, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.3 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 330 us: 1.37x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 37.9 us: 1.35x faster                                                   |
| go                         | 163 ms                                                   | 137 ms: 1.19x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 548 ms: 1.19x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.50 us: 1.16x faster                                                   |
| async_tree_none            | 493 ms                                                   | 426 ms: 1.16x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 553 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 417 ms: 1.12x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.7 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 726 ms: 1.05x faster                                                    |
| pathlib                    | 22.4 ms                                                  | 21.4 ms: 1.05x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.21 sec: 1.04x faster                                                  |
| regex_v8                   | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| 2to3                       | 306 ms                                                   | 295 ms: 1.04x faster                                                    |
| async_generators           | 496 ms                                                   | 480 ms: 1.03x faster                                                    |
| bench_thread_pool          | 1.28 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 135 ms: 1.03x faster                                                    |
| bench_mp_pool              | 7.30 ms                                                  | 7.09 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.39 ms: 1.03x faster                                                   |
| sympy_sum                  | 143 ms                                                   | 140 ms: 1.03x faster                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 81.6 ms: 1.03x faster                                                   |
| nbody                      | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| logging_format             | 7.83 us                                                  | 7.64 us: 1.02x faster                                                   |
| pprint_safe_repr           | 926 ms                                                   | 904 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.85 sec: 1.02x faster                                                  |
| regex_compile              | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| python_startup             | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| mdp                        | 3.36 sec                                                 | 3.31 sec: 1.02x faster                                                  |
| thrift                     | 946 us                                                   | 930 us: 1.02x faster                                                    |
| sympy_integrate            | 21.0 ms                                                  | 20.7 ms: 1.02x faster                                                   |
| logging_silent             | 135 ns                                                   | 133 ns: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 725 ms: 1.02x faster                                                    |
| richards_super             | 60.3 ms                                                  | 59.4 ms: 1.02x faster                                                   |
| sqlglot_optimize           | 62.4 ms                                                  | 61.4 ms: 1.02x faster                                                   |
| scimark_fft                | 447 ms                                                   | 441 ms: 1.01x faster                                                    |
| unpickle_pure_python       | 254 us                                                   | 252 us: 1.01x faster                                                    |
| float                      | 94.4 ms                                                  | 93.4 ms: 1.01x faster                                                   |
| sympy_str                  | 264 ms                                                   | 261 ms: 1.01x faster                                                    |
| spectral_norm              | 141 ms                                                   | 140 ms: 1.01x faster                                                    |
| bpe_tokeniser              | 5.90 sec                                                 | 5.86 sec: 1.01x faster                                                  |
| sqlglot_parse              | 1.38 ms                                                  | 1.39 ms: 1.01x slower                                                   |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                                   |
| mako                       | 13.3 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| comprehensions             | 20.4 us                                                  | 20.7 us: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.02x slower                                                  |
| raytrace                   | 298 ms                                                   | 304 ms: 1.02x slower                                                    |
| telco                      | 9.73 ms                                                  | 9.97 ms: 1.02x slower                                                   |
| regex_dna                  | 246 ms                                                   | 254 ms: 1.03x slower                                                    |
| json_loads                 | 31.4 us                                                  | 32.4 us: 1.03x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| pyflate                    | 556 ms                                                   | 581 ms: 1.04x slower                                                    |
| docutils                   | 2.91 sec                                                 | 3.04 sec: 1.04x slower                                                  |
| tomli_loads                | 2.53 sec                                                 | 2.64 sec: 1.05x slower                                                  |
| fannkuch                   | 452 ms                                                   | 475 ms: 1.05x slower                                                    |
| gc_traversal               | 4.53 ms                                                  | 4.85 ms: 1.07x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                                  |
| create_gc_cycles           | 2.12 ms                                                  | 2.29 ms: 1.08x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (32): tornado_http, richards, crypto_pyaes, scimark_sor, genshi_text, typing_runtime_protocols, asyncio_tcp, hexiom, coverage, pickle_pure_python, chaos, logging_simple, json_dumps, sqlglot_transpile, xml_etree_generate, meteor_contest, xml_etree_iterparse, genshi_xml, sqlglot_normalize, pidigits, sympy_expand, xml_etree_process, asyncio_websockets, python_startup_no_site, django_template, nqueens, regex_effbot, html5lib, json, deltablue, xml_etree_parse, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x