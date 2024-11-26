# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.000x faster
- HPT reliability: 78.39%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.01 sec                                                                | 3.04 sec: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (13): async_tree_memoization_tg, async_tree_cpu_io_mixed, coroutines, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io, async_generators, asyncio_websockets, asyncio_tcp_ssl, asyncio_tcp, async_tree_none, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.6 ms                                                                 | 93.4 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.84 ms                                                                 | 4.91 ms: 1.01x slower                                                   |
| regex_dna      | 247 ms                                                                  | 254 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|---------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse | 149 ms                                                                  | 146 ms: 1.02x faster                                                    |
| json_dumps          | 13.6 ms                                                                 | 13.3 ms: 1.02x faster                                                   |
| pickle_pure_python  | 363 us                                                                  | 358 us: 1.01x faster                                                    |
| tomli_loads         | 2.63 sec                                                                | 2.64 sec: 1.00x slower                                                  |
| Geometric mean      | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (5): unpickle_pure_python, json_loads, xml_etree_generate, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.1 ms                                                                 | 13.1 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, django_template, genshi_text, mako

All benchmarks:
===============

| Benchmark                | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|--------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pprint_safe_repr         | 942 ms                                                                  | 904 ms: 1.04x faster                                                    |
| pprint_pformat           | 1.91 sec                                                                | 1.85 sec: 1.03x faster                                                  |
| thrift                   | 954 us                                                                  | 930 us: 1.03x faster                                                    |
| sqlglot_parse            | 1.42 ms                                                                 | 1.39 ms: 1.02x faster                                                   |
| typing_runtime_protocols | 194 us                                                                  | 190 us: 1.02x faster                                                    |
| xml_etree_iterparse      | 149 ms                                                                  | 146 ms: 1.02x faster                                                    |
| json_dumps               | 13.6 ms                                                                 | 13.3 ms: 1.02x faster                                                   |
| deepcopy_reduce          | 3.56 us                                                                 | 3.50 us: 1.02x faster                                                   |
| nqueens                  | 101 ms                                                                  | 99.5 ms: 1.02x faster                                                   |
| sympy_str                | 265 ms                                                                  | 261 ms: 1.01x faster                                                    |
| pickle_pure_python       | 363 us                                                                  | 358 us: 1.01x faster                                                    |
| spectral_norm            | 141 ms                                                                  | 140 ms: 1.01x faster                                                    |
| mdp                      | 3.34 sec                                                                | 3.31 sec: 1.01x faster                                                  |
| python_startup           | 13.1 ms                                                                 | 13.1 ms: 1.01x faster                                                   |
| tomli_loads              | 2.63 sec                                                                | 2.64 sec: 1.00x slower                                                  |
| float                    | 92.6 ms                                                                 | 93.4 ms: 1.01x slower                                                   |
| scimark_sparse_mat_mult  | 6.33 ms                                                                 | 6.39 ms: 1.01x slower                                                   |
| docutils                 | 3.01 sec                                                                | 3.04 sec: 1.01x slower                                                  |
| hexiom                   | 7.02 ms                                                                 | 7.10 ms: 1.01x slower                                                   |
| regex_effbot             | 4.84 ms                                                                 | 4.91 ms: 1.01x slower                                                   |
| comprehensions           | 20.4 us                                                                 | 20.7 us: 1.01x slower                                                   |
| regex_dna                | 247 ms                                                                  | 254 ms: 1.03x slower                                                    |
| fannkuch                 | 460 ms                                                                  | 475 ms: 1.03x slower                                                    |
| pyflate                  | 560 ms                                                                  | 581 ms: 1.04x slower                                                    |
| Geometric mean           | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (65): genshi_xml, sympy_sum, deepcopy, richards, telco, sympy_integrate, sqlglot_optimize, sympy_expand, async_tree_memoization_tg, async_tree_cpu_io_mixed, unpickle_pure_python, django_template, genshi_text, bench_thread_pool, coverage, 2to3, json_loads, crypto_pyaes, logging_simple, coroutines, async_tree_memoization, async_tree_cpu_io_mixed_tg, richards_super, deepcopy_memo, generators, pycparser, async_tree_io, logging_format, async_generators, python_startup_no_site, pidigits, asyncio_websockets, json, deltablue, xml_etree_generate, regex_v8, go, asyncio_tcp_ssl, sqlglot_transpile, gc_traversal, scimark_fft, create_gc_cycles, bpe_tokeniser, scimark_monte_carlo, mako, scimark_sor, asyncio_tcp, chaos, async_tree_none, pylint, async_tree_io_tg, xml_etree_process, bench_mp_pool, logging_silent, raytrace, tornado_http, async_tree_none_tg, regex_compile, scimark_lu, pathlib, xml_etree_parse, nbody, meteor_contest, sqlglot_normalize, html5lib

- Geometric mean (including insignificant results): 1.000x faster
# HPT report

- Reliability score: 78.39% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x