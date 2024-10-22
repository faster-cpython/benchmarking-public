# Results vs. base

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-aarch64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.00x slower
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 359 ms                                                                  | 362 ms: 1.01x slower                                                          |
| docutils       | 3.52 sec                                                                | 3.59 sec: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                  |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 712 ms                                                                  | 720 ms: 1.01x slower                                                          |
| async_tree_memoization     | 581 ms                                                                  | 594 ms: 1.02x slower                                                          |
| Geometric mean             | (ref)                                                                   | 1.01x slower                                                                  |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none, async_tree_io, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 89.1 ms                                                                 | 91.9 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                  |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_compile, regex_v8, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|--------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_pure_python | 412 us                                                                  | 400 us: 1.03x faster                                                          |
| tomli_loads        | 2.63 sec                                                                | 2.62 sec: 1.00x faster                                                        |
| json_dumps         | 13.4 ms                                                                 | 13.5 ms: 1.01x slower                                                         |
| Geometric mean     | (ref)                                                                   | 1.00x faster                                                                  |

Benchmark hidden because not significant (6): xml_etree_iterparse, unpickle_pure_python, json_loads, xml_etree_generate, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 8.83 ms                                                                 | 8.72 ms: 1.01x faster                                                         |
| python_startup         | 13.0 ms                                                                 | 12.9 ms: 1.01x faster                                                         |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 79.6 ms                                                                 | 78.7 ms: 1.01x faster                                                         |
| django_template | 50.2 ms                                                                 | 50.6 ms: 1.01x slower                                                         |
| Geometric mean  | (ref)                                                                   | 1.00x faster                                                                  |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| bench_mp_pool              | 8.21 ms                                                                 | 7.91 ms: 1.04x faster                                                         |
| generators                 | 38.6 ms                                                                 | 37.3 ms: 1.04x faster                                                         |
| bpe_tokeniser              | 6.03 sec                                                                | 5.84 sec: 1.03x faster                                                        |
| pickle_pure_python         | 412 us                                                                  | 400 us: 1.03x faster                                                          |
| richards_super             | 61.6 ms                                                                 | 60.5 ms: 1.02x faster                                                         |
| scimark_fft                | 467 ms                                                                  | 460 ms: 1.02x faster                                                          |
| coroutines                 | 29.4 ms                                                                 | 29.0 ms: 1.01x faster                                                         |
| python_startup_no_site     | 8.83 ms                                                                 | 8.72 ms: 1.01x faster                                                         |
| richards                   | 54.3 ms                                                                 | 53.6 ms: 1.01x faster                                                         |
| genshi_xml                 | 79.6 ms                                                                 | 78.7 ms: 1.01x faster                                                         |
| python_startup             | 13.0 ms                                                                 | 12.9 ms: 1.01x faster                                                         |
| nqueens                    | 118 ms                                                                  | 118 ms: 1.01x faster                                                          |
| tomli_loads                | 2.63 sec                                                                | 2.62 sec: 1.00x faster                                                        |
| json_dumps                 | 13.4 ms                                                                 | 13.5 ms: 1.01x slower                                                         |
| django_template            | 50.2 ms                                                                 | 50.6 ms: 1.01x slower                                                         |
| sqlglot_transpile          | 2.01 ms                                                                 | 2.03 ms: 1.01x slower                                                         |
| 2to3                       | 359 ms                                                                  | 362 ms: 1.01x slower                                                          |
| mdp                        | 3.44 sec                                                                | 3.47 sec: 1.01x slower                                                        |
| pprint_safe_repr           | 1.15 sec                                                                | 1.16 sec: 1.01x slower                                                        |
| async_tree_cpu_io_mixed_tg | 712 ms                                                                  | 720 ms: 1.01x slower                                                          |
| raytrace                   | 325 ms                                                                  | 329 ms: 1.01x slower                                                          |
| scimark_sparse_mat_mult    | 6.89 ms                                                                 | 6.99 ms: 1.01x slower                                                         |
| sympy_sum                  | 192 ms                                                                  | 195 ms: 1.01x slower                                                          |
| deepcopy_memo              | 38.1 us                                                                 | 38.8 us: 1.02x slower                                                         |
| hexiom                     | 9.01 ms                                                                 | 9.16 ms: 1.02x slower                                                         |
| async_generators           | 499 ms                                                                  | 509 ms: 1.02x slower                                                          |
| docutils                   | 3.52 sec                                                                | 3.59 sec: 1.02x slower                                                        |
| sympy_str                  | 332 ms                                                                  | 339 ms: 1.02x slower                                                          |
| crypto_pyaes               | 87.5 ms                                                                 | 89.5 ms: 1.02x slower                                                         |
| async_tree_memoization     | 581 ms                                                                  | 594 ms: 1.02x slower                                                          |
| logging_silent             | 136 ns                                                                  | 139 ns: 1.02x slower                                                          |
| pycparser                  | 1.35 sec                                                                | 1.38 sec: 1.02x slower                                                        |
| deepcopy                   | 374 us                                                                  | 383 us: 1.02x slower                                                          |
| sympy_expand               | 550 ms                                                                  | 565 ms: 1.03x slower                                                          |
| pyflate                    | 599 ms                                                                  | 616 ms: 1.03x slower                                                          |
| float                      | 89.1 ms                                                                 | 91.9 ms: 1.03x slower                                                         |
| dulwich_log                | 71.9 ms                                                                 | 74.2 ms: 1.03x slower                                                         |
| deepcopy_reduce            | 4.08 us                                                                 | 4.28 us: 1.05x slower                                                         |
| Geometric mean             | (ref)                                                                   | 1.00x slower                                                                  |

Benchmark hidden because not significant (53): pylint, xml_etree_iterparse, regex_compile, fannkuch, spectral_norm, unpickle_pure_python, deltablue, asyncio_tcp, nbody, meteor_contest, asyncio_tcp_ssl, json_loads, mako, tornado_http, regex_v8, coverage, scimark_monte_carlo, go, sympy_integrate, async_tree_cpu_io_mixed, regex_effbot, bench_thread_pool, sqlglot_optimize, logging_simple, pidigits, async_tree_io_tg, async_tree_none, pprint_pformat, genshi_text, json, async_tree_io, gc_traversal, pathlib, regex_dna, asyncio_websockets, xml_etree_generate, comprehensions, chaos, scimark_lu, typing_runtime_protocols, create_gc_cycles, async_tree_none_tg, telco, async_tree_memoization_tg, scimark_sor, thrift, logging_format, sqlglot_normalize, xml_etree_parse, dask, sqlglot_parse, xml_etree_process, html5lib

# HPT report

- Reliability score: 99.83% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x