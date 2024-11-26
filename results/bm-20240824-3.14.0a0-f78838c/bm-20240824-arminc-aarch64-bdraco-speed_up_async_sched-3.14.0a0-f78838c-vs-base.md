# Results vs. base

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-aarch64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.001x slower
- HPT reliability: 88.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.06 sec                                                                | 3.09 sec: 1.01x slower                                                  |
| html5lib       | 67.0 ms                                                                 | 65.0 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg | 1.18 sec                                                                | 1.14 sec: 1.03x faster                                                  |
| asyncio_tcp_ssl  | 2.21 sec                                                                | 2.24 sec: 1.01x slower                                                  |
| async_generators | 485 ms                                                                  | 493 ms: 1.02x slower                                                    |
| asyncio_tcp      | 572 ms                                                                  | 582 ms: 1.02x slower                                                    |
| async_tree_io    | 1.13 sec                                                                | 1.20 sec: 1.06x slower                                                  |
| Geometric mean   | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_none, asyncio_websockets, async_tree_cpu_io_mixed_tg, coroutines, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.9 ms                                                                 | 91.1 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 30.6 ms                                                                 | 31.2 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (3): regex_compile, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|--------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python | 363 us                                                                  | 355 us: 1.02x faster                                                    |
| json_dumps         | 13.2 ms                                                                 | 13.1 ms: 1.01x faster                                                   |
| Geometric mean     | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (7): unpickle_pure_python, xml_etree_process, xml_etree_iterparse, json_loads, tomli_loads, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.68 ms                                                                 | 8.81 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): mako, genshi_xml, django_template, genshi_text

All benchmarks:
===============

| Benchmark              | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg       | 1.18 sec                                                                | 1.14 sec: 1.03x faster                                                  |
| html5lib               | 67.0 ms                                                                 | 65.0 ms: 1.03x faster                                                   |
| pickle_pure_python     | 363 us                                                                  | 355 us: 1.02x faster                                                    |
| crypto_pyaes           | 83.1 ms                                                                 | 81.7 ms: 1.02x faster                                                   |
| pycparser              | 1.24 sec                                                                | 1.22 sec: 1.02x faster                                                  |
| nqueens                | 100 ms                                                                  | 98.8 ms: 1.01x faster                                                   |
| pprint_safe_repr       | 936 ms                                                                  | 924 ms: 1.01x faster                                                    |
| json_dumps             | 13.2 ms                                                                 | 13.1 ms: 1.01x faster                                                   |
| scimark_lu             | 136 ms                                                                  | 135 ms: 1.01x faster                                                    |
| float                  | 91.9 ms                                                                 | 91.1 ms: 1.01x faster                                                   |
| pprint_pformat         | 1.93 sec                                                                | 1.91 sec: 1.01x faster                                                  |
| bpe_tokeniser          | 5.84 sec                                                                | 5.87 sec: 1.00x slower                                                  |
| mdp                    | 3.34 sec                                                                | 3.36 sec: 1.01x slower                                                  |
| docutils               | 3.06 sec                                                                | 3.09 sec: 1.01x slower                                                  |
| richards_super         | 59.4 ms                                                                 | 60.2 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.68 ms                                                                 | 8.81 ms: 1.01x slower                                                   |
| logging_silent         | 131 ns                                                                  | 133 ns: 1.01x slower                                                    |
| asyncio_tcp_ssl        | 2.21 sec                                                                | 2.24 sec: 1.01x slower                                                  |
| async_generators       | 485 ms                                                                  | 493 ms: 1.02x slower                                                    |
| asyncio_tcp            | 572 ms                                                                  | 582 ms: 1.02x slower                                                    |
| telco                  | 9.84 ms                                                                 | 10.0 ms: 1.02x slower                                                   |
| regex_v8               | 30.6 ms                                                                 | 31.2 ms: 1.02x slower                                                   |
| logging_simple         | 6.96 us                                                                 | 7.13 us: 1.02x slower                                                   |
| pyflate                | 562 ms                                                                  | 593 ms: 1.05x slower                                                    |
| async_tree_io          | 1.13 sec                                                                | 1.20 sec: 1.06x slower                                                  |
| Geometric mean         | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (64): tornado_http, async_tree_memoization_tg, thrift, sqlglot_normalize, pylint, generators, unpickle_pure_python, pathlib, deltablue, sqlglot_transpile, coverage, scimark_monte_carlo, raytrace, create_gc_cycles, go, 2to3, xml_etree_process, xml_etree_iterparse, async_tree_none, bench_thread_pool, sympy_sum, mako, deepcopy_reduce, bench_mp_pool, deepcopy_memo, sympy_integrate, chaos, asyncio_websockets, json_loads, scimark_sparse_mat_mult, genshi_xml, regex_compile, django_template, hexiom, deepcopy, spectral_norm, scimark_fft, pidigits, python_startup, async_tree_cpu_io_mixed_tg, tomli_loads, xml_etree_generate, sympy_expand, regex_dna, genshi_text, fannkuch, scimark_sor, coroutines, meteor_contest, regex_effbot, nbody, logging_format, async_tree_cpu_io_mixed, async_tree_none_tg, xml_etree_parse, typing_runtime_protocols, comprehensions, sympy_str, sqlglot_optimize, richards, json, gc_traversal, sqlglot_parse, async_tree_memoization

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 88.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x