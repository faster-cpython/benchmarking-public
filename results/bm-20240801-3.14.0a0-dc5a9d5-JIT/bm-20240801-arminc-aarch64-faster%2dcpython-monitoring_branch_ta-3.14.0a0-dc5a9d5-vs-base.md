# Results vs. base

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: linux-aarch64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.00x slower
- HPT reliability: 76.67%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp_ssl  | 2.27 sec                                                                | 2.29 sec: 1.01x slower                                                            |
| async_generators | 504 ms                                                                  | 511 ms: 1.01x slower                                                              |
| asyncio_tcp      | 624 ms                                                                  | 653 ms: 1.05x slower                                                              |
| Geometric mean   | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (10): async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, coroutines, async_tree_none, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 187 ms                                                                  | 182 ms: 1.02x faster                                                              |
| regex_v8       | 30.6 ms                                                                 | 30.0 ms: 1.02x faster                                                             |
| regex_dna      | 260 ms                                                                  | 258 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|--------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python | 401 us                                                                  | 398 us: 1.01x faster                                                              |
| Geometric mean     | (ref)                                                                   | 1.00x faster                                                                      |

Benchmark hidden because not significant (8): xml_etree_process, json_dumps, xml_etree_parse, tomli_loads, unpickle_pure_python, xml_etree_iterparse, json_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 51.4 ms                                                                 | 50.6 ms: 1.02x faster                                                             |
| genshi_xml      | 73.3 ms                                                                 | 75.3 ms: 1.03x slower                                                             |
| Geometric mean  | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark           | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|---------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| bench_mp_pool       | 8.28 ms                                                                 | 7.89 ms: 1.05x faster                                                             |
| dask                | 401 ms                                                                  | 391 ms: 1.03x faster                                                              |
| regex_compile       | 187 ms                                                                  | 182 ms: 1.02x faster                                                              |
| fannkuch            | 488 ms                                                                  | 477 ms: 1.02x faster                                                              |
| regex_v8            | 30.6 ms                                                                 | 30.0 ms: 1.02x faster                                                             |
| meteor_contest      | 121 ms                                                                  | 119 ms: 1.02x faster                                                              |
| django_template     | 51.4 ms                                                                 | 50.6 ms: 1.02x faster                                                             |
| deepcopy            | 388 us                                                                  | 382 us: 1.02x faster                                                              |
| pathlib             | 22.4 ms                                                                 | 22.0 ms: 1.01x faster                                                             |
| thrift              | 974 us                                                                  | 964 us: 1.01x faster                                                              |
| regex_dna           | 260 ms                                                                  | 258 ms: 1.01x faster                                                              |
| pickle_pure_python  | 401 us                                                                  | 398 us: 1.01x faster                                                              |
| scimark_lu          | 180 ms                                                                  | 180 ms: 1.00x faster                                                              |
| asyncio_tcp_ssl     | 2.27 sec                                                                | 2.29 sec: 1.01x slower                                                            |
| sympy_sum           | 200 ms                                                                  | 203 ms: 1.01x slower                                                              |
| async_generators    | 504 ms                                                                  | 511 ms: 1.01x slower                                                              |
| nqueens             | 123 ms                                                                  | 124 ms: 1.01x slower                                                              |
| bench_thread_pool   | 1.31 ms                                                                 | 1.33 ms: 1.02x slower                                                             |
| gc_traversal        | 5.01 ms                                                                 | 5.09 ms: 1.02x slower                                                             |
| create_gc_cycles    | 2.33 ms                                                                 | 2.39 ms: 1.02x slower                                                             |
| scimark_monte_carlo | 87.6 ms                                                                 | 89.8 ms: 1.03x slower                                                             |
| genshi_xml          | 73.3 ms                                                                 | 75.3 ms: 1.03x slower                                                             |
| pyflate             | 597 ms                                                                  | 616 ms: 1.03x slower                                                              |
| coverage            | 97.8 ms                                                                 | 101 ms: 1.03x slower                                                              |
| telco               | 10.3 ms                                                                 | 10.7 ms: 1.03x slower                                                             |
| pprint_safe_repr    | 1.14 sec                                                                | 1.18 sec: 1.04x slower                                                            |
| pprint_pformat      | 2.34 sec                                                                | 2.43 sec: 1.04x slower                                                            |
| asyncio_tcp         | 624 ms                                                                  | 653 ms: 1.05x slower                                                              |
| Geometric mean      | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (62): json, logging_format, xml_etree_process, logging_simple, scimark_sor, sqlglot_optimize, spectral_norm, tornado_http, comprehensions, logging_silent, richards, async_tree_io, json_dumps, deepcopy_reduce, richards_super, 2to3, async_tree_io_tg, xml_etree_parse, html5lib, tomli_loads, python_startup_no_site, go, python_startup, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_memoization_tg, deepcopy_memo, sympy_integrate, mako, async_tree_cpu_io_mixed_tg, regex_effbot, unpickle_pure_python, typing_runtime_protocols, docutils, xml_etree_iterparse, coroutines, pidigits, bpe_tokeniser, mdp, generators, hexiom, nbody, scimark_sparse_mat_mult, crypto_pyaes, sqlglot_parse, float, sympy_expand, scimark_fft, deltablue, sympy_str, chaos, async_tree_none, sqlglot_normalize, json_loads, pycparser, genshi_text, raytrace, async_tree_none_tg, pylint, async_tree_memoization, sqlglot_transpile, xml_etree_generate

# HPT report

- Reliability score: 76.67% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x