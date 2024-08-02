# Results vs. base

- fork: python
- ref: 22b0de2755ee2d0e2dd2
- machine: linux-aarch64
- commit hash: 22b0de2
- commit date: 2024-06-27
- overall geometric mean: 1.00x slower
- HPT reliability: 99.67%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240626-arminc-aarch64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.10 sec                                                                | 3.13 sec: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240626-arminc-aarch64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                                 | 91.6 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240626-arminc-aarch64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 30.0 ms                                                                 | 30.7 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240626-arminc-aarch64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|--------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python | 366 us                                                                  | 358 us: 1.02x faster                                                    |
| Geometric mean     | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (8): xml_etree_generate, xml_etree_process, tomli_loads, json_loads, json_dumps, unpickle_pure_python, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240626-arminc-aarch64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.5 ms                                                                 | 13.8 ms: 1.02x slower                                                   |
| genshi_text    | 28.2 ms                                                                 | 28.8 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark          | bm-20240626-arminc-aarch64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|--------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo      | 39.3 us                                                                 | 38.3 us: 1.03x faster                                                   |
| create_gc_cycles   | 2.33 ms                                                                 | 2.28 ms: 1.02x faster                                                   |
| pickle_pure_python | 366 us                                                                  | 358 us: 1.02x faster                                                    |
| pathlib            | 22.1 ms                                                                 | 21.7 ms: 1.02x faster                                                   |
| fannkuch           | 456 ms                                                                  | 453 ms: 1.01x faster                                                    |
| float              | 92.1 ms                                                                 | 91.6 ms: 1.01x faster                                                   |
| pyflate            | 558 ms                                                                  | 561 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl    | 2.20 sec                                                                | 2.21 sec: 1.01x slower                                                  |
| scimark_fft        | 447 ms                                                                  | 451 ms: 1.01x slower                                                    |
| docutils           | 3.10 sec                                                                | 3.13 sec: 1.01x slower                                                  |
| logging_simple     | 7.00 us                                                                 | 7.07 us: 1.01x slower                                                   |
| sympy_expand       | 459 ms                                                                  | 464 ms: 1.01x slower                                                    |
| sympy_str          | 267 ms                                                                  | 270 ms: 1.01x slower                                                    |
| sqlglot_transpile  | 1.73 ms                                                                 | 1.75 ms: 1.01x slower                                                   |
| pprint_safe_repr   | 947 ms                                                                  | 964 ms: 1.02x slower                                                    |
| mako               | 13.5 ms                                                                 | 13.8 ms: 1.02x slower                                                   |
| richards           | 53.0 ms                                                                 | 54.2 ms: 1.02x slower                                                   |
| genshi_text        | 28.2 ms                                                                 | 28.8 ms: 1.02x slower                                                   |
| regex_v8           | 30.0 ms                                                                 | 30.7 ms: 1.02x slower                                                   |
| pprint_pformat     | 1.94 sec                                                                | 1.99 sec: 1.03x slower                                                  |
| Geometric mean     | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (71): sqlglot_optimize, deltablue, xml_etree_generate, tornado_http, scimark_sparse_mat_mult, async_tree_io_tg, django_template, regex_dna, pycparser, regex_effbot, crypto_pyaes, nqueens, chaos, json, comprehensions, scimark_sor, bench_mp_pool, richards_super, xml_etree_process, sympy_sum, asyncio_tcp, bench_thread_pool, raytrace, python_startup, generators, asyncio_websockets, meteor_contest, async_tree_io, logging_format, tomli_loads, regex_compile, go, pidigits, sympy_integrate, json_loads, async_tree_memoization_tg, python_startup_no_site, coverage, json_dumps, async_generators, unpickle_pure_python, mdp, nbody, spectral_norm, bpe_tokeniser, xml_etree_parse, scimark_monte_carlo, telco, deepcopy, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, hexiom, sqlglot_parse, thrift, pylint, html5lib, typing_runtime_protocols, 2to3, scimark_lu, coroutines, sqlglot_normalize, genshi_xml, async_tree_none_tg, logging_silent, async_tree_memoization, async_tree_none, deepcopy_reduce, gc_traversal, dulwich_log, xml_etree_iterparse, dask

# HPT report

- Reliability score: 99.67% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x