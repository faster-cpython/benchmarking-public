# Results vs. 3.13.0

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-aarch64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.02x faster
- HPT reliability: 99.08%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 297 ms: 1.03x faster                                                |
| docutils       | 2.91 sec                                                 | 3.03 sec: 1.04x slower                                              |
| Geometric mean | (ref)                                                    | 1.00x faster                                                        |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 550 ms: 1.18x faster                                                |
| async_tree_none            | 493 ms                                                   | 427 ms: 1.15x faster                                                |
| async_tree_none_tg         | 467 ms                                                   | 416 ms: 1.12x faster                                                |
| async_tree_memoization     | 626 ms                                                   | 562 ms: 1.11x faster                                                |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 734 ms: 1.04x faster                                                |
| async_generators           | 496 ms                                                   | 482 ms: 1.03x faster                                                |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 725 ms: 1.02x faster                                                |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.02x slower                                              |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                              |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                              |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                        |

Benchmark hidden because not significant (3): asyncio_tcp, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                    | 1.02x faster                                                        |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                   | 124 ms: 1.04x faster                                                |
| regex_v8       | 31.5 ms                                                  | 30.7 ms: 1.03x faster                                               |
| regex_effbot   | 4.87 ms                                                  | 5.01 ms: 1.03x slower                                               |
| regex_dna      | 246 ms                                                   | 253 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                    | 1.00x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|--------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_list      | 6.65 us                                                  | 6.38 us: 1.04x faster                                               |
| unpickle           | 20.2 us                                                  | 19.3 us: 1.04x faster                                               |
| pickle_list        | 5.34 us                                                  | 5.19 us: 1.03x faster                                               |
| pickle             | 13.5 us                                                  | 13.7 us: 1.02x slower                                               |
| pickle_pure_python | 359 us                                                   | 368 us: 1.02x slower                                                |
| tomli_loads        | 2.53 sec                                                 | 2.61 sec: 1.03x slower                                              |
| Geometric mean     | (ref)                                                    | 1.00x faster                                                        |

Benchmark hidden because not significant (8): xml_etree_process, unpickle_pure_python, pickle_dict, json_dumps, xml_etree_generate, json_loads, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                               |
| python_startup_no_site | 8.75 ms                                                  | 8.65 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                    | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 37.3 us: 1.37x faster                                               |
| deepcopy                   | 451 us                                                   | 337 us: 1.34x faster                                                |
| go                         | 163 ms                                                   | 137 ms: 1.19x faster                                                |
| async_tree_memoization_tg  | 649 ms                                                   | 550 ms: 1.18x faster                                                |
| async_tree_none            | 493 ms                                                   | 427 ms: 1.15x faster                                                |
| deepcopy_reduce            | 4.07 us                                                  | 3.57 us: 1.14x faster                                               |
| async_tree_none_tg         | 467 ms                                                   | 416 ms: 1.12x faster                                                |
| async_tree_memoization     | 626 ms                                                   | 562 ms: 1.11x faster                                                |
| generators                 | 37.8 ms                                                  | 34.8 ms: 1.09x faster                                               |
| pathlib                    | 22.4 ms                                                  | 20.9 ms: 1.07x faster                                               |
| nbody                      | 114 ms                                                   | 109 ms: 1.05x faster                                                |
| unpickle_list              | 6.65 us                                                  | 6.38 us: 1.04x faster                                               |
| unpickle                   | 20.2 us                                                  | 19.3 us: 1.04x faster                                               |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 734 ms: 1.04x faster                                                |
| pycparser                  | 1.26 sec                                                 | 1.21 sec: 1.04x faster                                              |
| scimark_monte_carlo        | 83.8 ms                                                  | 80.7 ms: 1.04x faster                                               |
| regex_compile              | 128 ms                                                   | 124 ms: 1.04x faster                                                |
| bench_thread_pool          | 1.28 ms                                                  | 1.24 ms: 1.03x faster                                               |
| async_generators           | 496 ms                                                   | 482 ms: 1.03x faster                                                |
| logging_silent             | 135 ns                                                   | 131 ns: 1.03x faster                                                |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.39 ms: 1.03x faster                                               |
| pickle_list                | 5.34 us                                                  | 5.19 us: 1.03x faster                                               |
| 2to3                       | 306 ms                                                   | 297 ms: 1.03x faster                                                |
| regex_v8                   | 31.5 ms                                                  | 30.7 ms: 1.03x faster                                               |
| bench_mp_pool              | 7.30 ms                                                  | 7.11 ms: 1.03x faster                                               |
| sympy_integrate            | 21.0 ms                                                  | 20.5 ms: 1.02x faster                                               |
| scimark_sor                | 159 ms                                                   | 156 ms: 1.02x faster                                                |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                               |
| scimark_fft                | 447 ms                                                   | 440 ms: 1.02x faster                                                |
| meteor_contest             | 113 ms                                                   | 112 ms: 1.02x faster                                                |
| coverage                   | 98.5 ms                                                  | 97.0 ms: 1.02x faster                                               |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 725 ms: 1.02x faster                                                |
| richards                   | 53.5 ms                                                  | 52.7 ms: 1.02x faster                                               |
| richards_super             | 60.3 ms                                                  | 59.5 ms: 1.01x faster                                               |
| python_startup_no_site     | 8.75 ms                                                  | 8.65 ms: 1.01x faster                                               |
| bpe_tokeniser              | 5.90 sec                                                 | 5.83 sec: 1.01x faster                                              |
| mdp                        | 3.36 sec                                                 | 3.33 sec: 1.01x faster                                              |
| chaos                      | 68.8 ms                                                  | 68.1 ms: 1.01x faster                                               |
| pprint_pformat             | 1.90 sec                                                 | 1.91 sec: 1.01x slower                                              |
| sympy_expand               | 455 ms                                                   | 460 ms: 1.01x slower                                                |
| logging_simple             | 7.04 us                                                  | 7.15 us: 1.02x slower                                               |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.02x slower                                              |
| pickle                     | 13.5 us                                                  | 13.7 us: 1.02x slower                                               |
| pickle_pure_python         | 359 us                                                   | 368 us: 1.02x slower                                                |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.02x slower                                               |
| nqueens                    | 98.7 ms                                                  | 101 ms: 1.03x slower                                                |
| regex_effbot               | 4.87 ms                                                  | 5.01 ms: 1.03x slower                                               |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                              |
| regex_dna                  | 246 ms                                                   | 253 ms: 1.03x slower                                                |
| tomli_loads                | 2.53 sec                                                 | 2.61 sec: 1.03x slower                                              |
| pyflate                    | 556 ms                                                   | 579 ms: 1.04x slower                                                |
| docutils                   | 2.91 sec                                                 | 3.03 sec: 1.04x slower                                              |
| fannkuch                   | 452 ms                                                   | 471 ms: 1.04x slower                                                |
| unpack_sequence            | 57.2 ns                                                  | 59.9 ns: 1.05x slower                                               |
| telco                      | 9.73 ms                                                  | 10.3 ms: 1.05x slower                                               |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                              |
| create_gc_cycles           | 2.12 ms                                                  | 2.37 ms: 1.12x slower                                               |
| gc_traversal               | 4.53 ms                                                  | 5.13 ms: 1.13x slower                                               |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                        |

Benchmark hidden because not significant (37): tornado_http, logging_format, sympy_sum, json, xml_etree_process, hexiom, unpickle_pure_python, pickle_dict, json_dumps, xml_etree_generate, sqlite_synth, comprehensions, asyncio_tcp, pprint_safe_repr, spectral_norm, thrift, genshi_text, float, pidigits, json_loads, mako, sympy_str, crypto_pyaes, sqlglot_transpile, genshi_xml, asyncio_websockets, coroutines, sqlglot_normalize, django_template, typing_runtime_protocols, sqlglot_optimize, deltablue, raytrace, xml_etree_parse, html5lib, xml_etree_iterparse, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: dulwich_log

# HPT report

- Reliability score: 99.08% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x