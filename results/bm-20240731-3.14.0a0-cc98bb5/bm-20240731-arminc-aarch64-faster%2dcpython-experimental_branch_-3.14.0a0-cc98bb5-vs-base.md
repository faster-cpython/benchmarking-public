# Results vs. base

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-aarch64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.00x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tornado_http   | 124 ms                                                                  | 130 ms: 1.05x slower                                                              |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_generators | 484 ms                                                                  | 480 ms: 1.01x faster                                                              |
| asyncio_tcp_ssl  | 2.19 sec                                                                | 2.22 sec: 1.02x slower                                                            |
| asyncio_tcp      | 558 ms                                                                  | 585 ms: 1.05x slower                                                              |
| Geometric mean   | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (10): async_tree_none_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none, coroutines, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 109 ms                                                                  | 112 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 30.0 ms                                                                 | 30.9 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads    | 2.52 sec                                                                | 2.48 sec: 1.02x faster                                                            |
| json_dumps     | 13.4 ms                                                                 | 13.3 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                                      |

Benchmark hidden because not significant (7): json_loads, pickle_pure_python, unpickle_pure_python, xml_etree_iterparse, xml_etree_parse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 13.4 ms                                                                 | 13.4 ms: 1.01x slower                                                             |
| genshi_xml     | 60.9 ms                                                                 | 62.2 ms: 1.02x slower                                                             |
| genshi_text    | 27.4 ms                                                                 | 28.0 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark           | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|---------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json                | 5.76 ms                                                                 | 5.65 ms: 1.02x faster                                                             |
| tomli_loads         | 2.52 sec                                                                | 2.48 sec: 1.02x faster                                                            |
| json_dumps          | 13.4 ms                                                                 | 13.3 ms: 1.01x faster                                                             |
| go                  | 160 ms                                                                  | 158 ms: 1.01x faster                                                              |
| async_generators    | 484 ms                                                                  | 480 ms: 1.01x faster                                                              |
| mako                | 13.4 ms                                                                 | 13.4 ms: 1.01x slower                                                             |
| raytrace            | 294 ms                                                                  | 297 ms: 1.01x slower                                                              |
| crypto_pyaes        | 82.1 ms                                                                 | 83.0 ms: 1.01x slower                                                             |
| nqueens             | 99.8 ms                                                                 | 101 ms: 1.01x slower                                                              |
| fannkuch            | 460 ms                                                                  | 466 ms: 1.01x slower                                                              |
| sympy_sum           | 143 ms                                                                  | 146 ms: 1.02x slower                                                              |
| asyncio_tcp_ssl     | 2.19 sec                                                                | 2.22 sec: 1.02x slower                                                            |
| sympy_integrate     | 21.0 ms                                                                 | 21.3 ms: 1.02x slower                                                             |
| hexiom              | 7.10 ms                                                                 | 7.22 ms: 1.02x slower                                                             |
| chaos               | 67.0 ms                                                                 | 68.4 ms: 1.02x slower                                                             |
| genshi_xml          | 60.9 ms                                                                 | 62.2 ms: 1.02x slower                                                             |
| genshi_text         | 27.4 ms                                                                 | 28.0 ms: 1.02x slower                                                             |
| deepcopy_memo       | 37.6 us                                                                 | 38.6 us: 1.03x slower                                                             |
| deepcopy_reduce     | 3.34 us                                                                 | 3.44 us: 1.03x slower                                                             |
| nbody               | 109 ms                                                                  | 112 ms: 1.03x slower                                                              |
| regex_v8            | 30.0 ms                                                                 | 30.9 ms: 1.03x slower                                                             |
| scimark_monte_carlo | 80.4 ms                                                                 | 83.0 ms: 1.03x slower                                                             |
| tornado_http        | 124 ms                                                                  | 130 ms: 1.05x slower                                                              |
| asyncio_tcp         | 558 ms                                                                  | 585 ms: 1.05x slower                                                              |
| Geometric mean      | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (66): html5lib, logging_format, json_loads, python_startup, logging_simple, thrift, pickle_pure_python, richards, async_tree_none_tg, create_gc_cycles, meteor_contest, telco, sqlglot_normalize, pylint, unpickle_pure_python, sqlglot_transpile, python_startup_no_site, scimark_lu, async_tree_memoization_tg, regex_dna, pprint_pformat, coverage, gc_traversal, pathlib, pprint_safe_repr, bpe_tokeniser, dask, pidigits, asyncio_websockets, mdp, sqlglot_optimize, pyflate, comprehensions, scimark_fft, docutils, generators, async_tree_io, deepcopy, scimark_sor, xml_etree_iterparse, float, xml_etree_parse, logging_silent, richards_super, django_template, sympy_expand, async_tree_cpu_io_mixed_tg, bench_thread_pool, 2to3, sympy_str, pycparser, scimark_sparse_mat_mult, regex_effbot, async_tree_memoization, typing_runtime_protocols, bench_mp_pool, regex_compile, spectral_norm, async_tree_none, coroutines, deltablue, async_tree_cpu_io_mixed, xml_etree_process, async_tree_io_tg, sqlglot_parse, xml_etree_generate

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x