# Results vs. 3.13.0

- fork: python
- ref: e38d0afe3548b856ccf0
- machine: linux-aarch64
- commit hash: e38d0af
- commit date: 2024-08-24
- overall geometric mean: 1.01x faster
- HPT reliability: 95.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 295 ms: 1.04x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.06 sec: 1.05x slower                                                  |
| html5lib       | 64.3 ms                                                  | 67.0 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 550 ms: 1.18x faster                                                    |
| async_tree_none           | 493 ms                                                   | 427 ms: 1.15x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 563 ms: 1.11x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 421 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 729 ms: 1.05x faster                                                    |
| async_generators          | 496 ms                                                   | 485 ms: 1.02x faster                                                    |
| coroutines                | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                                  |
| async_tree_io             | 1.11 sec                                                 | 1.13 sec: 1.02x slower                                                  |
| async_tree_io_tg          | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| Geometric mean            | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, asyncio_tcp, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.04x faster                                                    |
| float          | 94.4 ms                                                  | 91.9 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.6 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (3): regex_compile, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|--------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python | 359 us                                                   | 363 us: 1.01x slower                                                    |
| tomli_loads        | 2.53 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| json_loads         | 31.4 us                                                  | 32.9 us: 1.05x slower                                                   |
| Geometric mean     | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (6): xml_etree_generate, json_dumps, xml_etree_process, unpickle_pure_python, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.3 ms                                                  | 13.4 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 38.0 us: 1.34x faster                                                   |
| deepcopy                  | 451 us                                                   | 338 us: 1.34x faster                                                    |
| async_tree_memoization_tg | 649 ms                                                   | 550 ms: 1.18x faster                                                    |
| async_tree_none           | 493 ms                                                   | 427 ms: 1.15x faster                                                    |
| deepcopy_reduce           | 4.07 us                                                  | 3.54 us: 1.15x faster                                                   |
| async_tree_memoization    | 626 ms                                                   | 563 ms: 1.11x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 421 ms: 1.11x faster                                                    |
| generators                | 37.8 ms                                                  | 35.2 ms: 1.08x faster                                                   |
| pathlib                   | 22.4 ms                                                  | 21.3 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 729 ms: 1.05x faster                                                    |
| nbody                     | 114 ms                                                   | 109 ms: 1.04x faster                                                    |
| 2to3                      | 306 ms                                                   | 295 ms: 1.04x faster                                                    |
| logging_silent            | 135 ns                                                   | 131 ns: 1.03x faster                                                    |
| bench_thread_pool         | 1.28 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| regex_v8                  | 31.5 ms                                                  | 30.6 ms: 1.03x faster                                                   |
| float                     | 94.4 ms                                                  | 91.9 ms: 1.03x faster                                                   |
| async_generators          | 496 ms                                                   | 485 ms: 1.02x faster                                                    |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.44 ms: 1.02x faster                                                   |
| python_startup            | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| scimark_lu                | 139 ms                                                   | 136 ms: 1.02x faster                                                    |
| scimark_sor               | 159 ms                                                   | 156 ms: 1.02x faster                                                    |
| scimark_monte_carlo       | 83.8 ms                                                  | 82.3 ms: 1.02x faster                                                   |
| meteor_contest            | 113 ms                                                   | 112 ms: 1.02x faster                                                    |
| richards_super            | 60.3 ms                                                  | 59.4 ms: 1.02x faster                                                   |
| pycparser                 | 1.26 sec                                                 | 1.24 sec: 1.01x faster                                                  |
| logging_simple            | 7.04 us                                                  | 6.96 us: 1.01x faster                                                   |
| bpe_tokeniser             | 5.90 sec                                                 | 5.84 sec: 1.01x faster                                                  |
| scimark_fft               | 447 ms                                                   | 444 ms: 1.01x faster                                                    |
| mdp                       | 3.36 sec                                                 | 3.34 sec: 1.01x faster                                                  |
| mako                      | 13.3 ms                                                  | 13.4 ms: 1.01x slower                                                   |
| telco                     | 9.73 ms                                                  | 9.84 ms: 1.01x slower                                                   |
| pprint_safe_repr          | 926 ms                                                   | 936 ms: 1.01x slower                                                    |
| pyflate                   | 556 ms                                                   | 562 ms: 1.01x slower                                                    |
| pickle_pure_python        | 359 us                                                   | 363 us: 1.01x slower                                                    |
| coroutines                | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                                  |
| nqueens                   | 98.7 ms                                                  | 100 ms: 1.02x slower                                                    |
| sympy_expand              | 455 ms                                                   | 462 ms: 1.02x slower                                                    |
| pprint_pformat            | 1.90 sec                                                 | 1.93 sec: 1.02x slower                                                  |
| raytrace                  | 298 ms                                                   | 303 ms: 1.02x slower                                                    |
| fannkuch                  | 452 ms                                                   | 460 ms: 1.02x slower                                                    |
| json                      | 5.61 ms                                                  | 5.72 ms: 1.02x slower                                                   |
| async_tree_io             | 1.11 sec                                                 | 1.13 sec: 1.02x slower                                                  |
| sqlglot_parse             | 1.38 ms                                                  | 1.43 ms: 1.03x slower                                                   |
| html5lib                  | 64.3 ms                                                  | 67.0 ms: 1.04x slower                                                   |
| tomli_loads               | 2.53 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| json_loads                | 31.4 us                                                  | 32.9 us: 1.05x slower                                                   |
| docutils                  | 2.91 sec                                                 | 3.06 sec: 1.05x slower                                                  |
| gc_traversal              | 4.53 ms                                                  | 4.89 ms: 1.08x slower                                                   |
| async_tree_io_tg          | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| create_gc_cycles          | 2.12 ms                                                  | 2.31 ms: 1.09x slower                                                   |
| go                        | 163 ms                                                   | 192 ms: 1.18x slower                                                    |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (37): bench_mp_pool, tornado_http, thrift, regex_compile, xml_etree_generate, logging_format, json_dumps, regex_effbot, sympy_integrate, sympy_sum, python_startup_no_site, async_tree_cpu_io_mixed_tg, hexiom, richards, django_template, chaos, sqlglot_optimize, comprehensions, spectral_norm, pidigits, genshi_text, sqlglot_normalize, regex_dna, xml_etree_process, sympy_str, unpickle_pure_python, coverage, crypto_pyaes, typing_runtime_protocols, genshi_xml, asyncio_tcp, sqlglot_transpile, asyncio_websockets, xml_etree_parse, xml_etree_iterparse, deltablue, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 95.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x