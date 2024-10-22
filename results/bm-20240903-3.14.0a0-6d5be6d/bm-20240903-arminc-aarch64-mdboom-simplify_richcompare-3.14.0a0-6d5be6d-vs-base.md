# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.00x faster
- HPT reliability: 83.10%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (13): async_tree_cpu_io_mixed, async_generators, coroutines, async_tree_cpu_io_mixed_tg, async_tree_none, asyncio_tcp_ssl, async_tree_memoization_tg, async_tree_memoization, asyncio_websockets, async_tree_io, asyncio_tcp, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 110 ms                                                                  | 108 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.84 ms                                                                 | 4.89 ms: 1.01x slower                                                   |
| regex_dna      | 247 ms                                                                  | 253 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads    | 2.63 sec                                                                | 2.64 sec: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (8): xml_etree_iterparse, xml_etree_generate, pickle_pure_python, json_dumps, unpickle_pure_python, xml_etree_process, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                 | 13.0 ms: 1.01x faster                                                   |
| python_startup_no_site | 8.81 ms                                                                 | 8.77 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.5 ms                                                                 | 13.4 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (3): genshi_xml, django_template, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|--------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pprint_safe_repr         | 942 ms                                                                  | 907 ms: 1.04x faster                                                    |
| nqueens                  | 101 ms                                                                  | 97.4 ms: 1.04x faster                                                   |
| telco                    | 10.1 ms                                                                 | 9.81 ms: 1.03x faster                                                   |
| deepcopy_reduce          | 3.56 us                                                                 | 3.47 us: 1.03x faster                                                   |
| pprint_pformat           | 1.91 sec                                                                | 1.87 sec: 1.02x faster                                                  |
| bench_mp_pool            | 7.04 ms                                                                 | 6.94 ms: 1.02x faster                                                   |
| nbody                    | 110 ms                                                                  | 108 ms: 1.01x faster                                                    |
| typing_runtime_protocols | 194 us                                                                  | 192 us: 1.01x faster                                                    |
| scimark_monte_carlo      | 81.4 ms                                                                 | 80.4 ms: 1.01x faster                                                   |
| meteor_contest           | 112 ms                                                                  | 110 ms: 1.01x faster                                                    |
| python_startup           | 13.1 ms                                                                 | 13.0 ms: 1.01x faster                                                   |
| mako                     | 13.5 ms                                                                 | 13.4 ms: 1.01x faster                                                   |
| mdp                      | 3.34 sec                                                                | 3.32 sec: 1.01x faster                                                  |
| python_startup_no_site   | 8.81 ms                                                                 | 8.77 ms: 1.00x faster                                                   |
| tomli_loads              | 2.63 sec                                                                | 2.64 sec: 1.01x slower                                                  |
| scimark_sparse_mat_mult  | 6.33 ms                                                                 | 6.39 ms: 1.01x slower                                                   |
| regex_effbot             | 4.84 ms                                                                 | 4.89 ms: 1.01x slower                                                   |
| sqlglot_normalize        | 125 ms                                                                  | 127 ms: 1.01x slower                                                    |
| scimark_fft              | 440 ms                                                                  | 446 ms: 1.01x slower                                                    |
| regex_dna                | 247 ms                                                                  | 253 ms: 1.02x slower                                                    |
| pyflate                  | 560 ms                                                                  | 575 ms: 1.03x slower                                                    |
| gc_traversal             | 4.84 ms                                                                 | 4.99 ms: 1.03x slower                                                   |
| Geometric mean           | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (67): genshi_xml, deltablue, sqlglot_parse, xml_etree_iterparse, xml_etree_generate, pickle_pure_python, coverage, sympy_sum, sympy_integrate, django_template, genshi_text, scimark_sor, thrift, json_dumps, scimark_lu, richards, comprehensions, unpickle_pure_python, async_tree_cpu_io_mixed, logging_silent, raytrace, async_generators, deepcopy_memo, coroutines, logging_simple, html5lib, async_tree_cpu_io_mixed_tg, go, deepcopy, bench_thread_pool, async_tree_none, asyncio_tcp_ssl, pylint, tornado_http, logging_format, generators, crypto_pyaes, float, 2to3, sqlglot_optimize, xml_etree_process, sympy_expand, async_tree_memoization_tg, fannkuch, hexiom, regex_v8, chaos, create_gc_cycles, sympy_str, spectral_norm, bpe_tokeniser, docutils, regex_compile, richards_super, pidigits, sqlglot_transpile, async_tree_memoization, pathlib, asyncio_websockets, async_tree_io, pycparser, json, json_loads, asyncio_tcp, xml_etree_parse, async_tree_none_tg, async_tree_io_tg

# HPT report

- Reliability score: 83.10% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x