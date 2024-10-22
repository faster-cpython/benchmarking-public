# Results vs. base

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-aarch64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 3.16 sec                                                                | 3.20 sec: 1.01x slower                                                            |
| tornado_http   | 124 ms                                                                  | 128 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp_ssl | 2.19 sec                                                                | 2.20 sec: 1.01x slower                                                            |
| coroutines      | 28.1 ms                                                                 | 28.5 ms: 1.01x slower                                                             |
| asyncio_tcp     | 558 ms                                                                  | 569 ms: 1.02x slower                                                              |
| Geometric mean  | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (10): async_tree_memoization_tg, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_io_tg, async_generators, asyncio_websockets, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 109 ms                                                                  | 111 ms: 1.02x slower                                                              |
| float          | 91.9 ms                                                                 | 93.7 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 255 ms                                                                  | 253 ms: 1.01x faster                                                              |
| regex_v8       | 30.0 ms                                                                 | 30.5 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads        | 2.52 sec                                                                | 2.56 sec: 1.02x slower                                                            |
| xml_etree_generate | 111 ms                                                                  | 114 ms: 1.03x slower                                                              |
| Geometric mean     | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (7): json_loads, pickle_pure_python, unpickle_pure_python, json_dumps, xml_etree_parse, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 13.4 ms                                                                 | 13.5 ms: 1.01x slower                                                             |
| genshi_text    | 27.4 ms                                                                 | 27.9 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna                | 255 ms                                                                  | 253 ms: 1.01x faster                                                              |
| thrift                   | 974 us                                                                  | 965 us: 1.01x faster                                                              |
| pprint_pformat           | 1.94 sec                                                                | 1.93 sec: 1.01x faster                                                            |
| logging_silent           | 129 ns                                                                  | 130 ns: 1.01x slower                                                              |
| asyncio_tcp_ssl          | 2.19 sec                                                                | 2.20 sec: 1.01x slower                                                            |
| raytrace                 | 294 ms                                                                  | 296 ms: 1.01x slower                                                              |
| bench_thread_pool        | 1.23 ms                                                                 | 1.24 ms: 1.01x slower                                                             |
| scimark_sparse_mat_mult  | 6.44 ms                                                                 | 6.50 ms: 1.01x slower                                                             |
| fannkuch                 | 460 ms                                                                  | 465 ms: 1.01x slower                                                              |
| mako                     | 13.4 ms                                                                 | 13.5 ms: 1.01x slower                                                             |
| sympy_expand             | 457 ms                                                                  | 463 ms: 1.01x slower                                                              |
| sympy_integrate          | 21.0 ms                                                                 | 21.2 ms: 1.01x slower                                                             |
| docutils                 | 3.16 sec                                                                | 3.20 sec: 1.01x slower                                                            |
| coroutines               | 28.1 ms                                                                 | 28.5 ms: 1.01x slower                                                             |
| sympy_sum                | 143 ms                                                                  | 145 ms: 1.01x slower                                                              |
| scimark_fft              | 441 ms                                                                  | 448 ms: 1.02x slower                                                              |
| tomli_loads              | 2.52 sec                                                                | 2.56 sec: 1.02x slower                                                            |
| typing_runtime_protocols | 196 us                                                                  | 199 us: 1.02x slower                                                              |
| generators               | 34.8 ms                                                                 | 35.4 ms: 1.02x slower                                                             |
| genshi_text              | 27.4 ms                                                                 | 27.9 ms: 1.02x slower                                                             |
| nbody                    | 109 ms                                                                  | 111 ms: 1.02x slower                                                              |
| scimark_lu               | 136 ms                                                                  | 139 ms: 1.02x slower                                                              |
| regex_v8                 | 30.0 ms                                                                 | 30.5 ms: 1.02x slower                                                             |
| float                    | 91.9 ms                                                                 | 93.7 ms: 1.02x slower                                                             |
| deepcopy_memo            | 37.6 us                                                                 | 38.3 us: 1.02x slower                                                             |
| asyncio_tcp              | 558 ms                                                                  | 569 ms: 1.02x slower                                                              |
| deltablue                | 3.80 ms                                                                 | 3.89 ms: 1.03x slower                                                             |
| sqlglot_parse            | 1.39 ms                                                                 | 1.42 ms: 1.03x slower                                                             |
| xml_etree_generate       | 111 ms                                                                  | 114 ms: 1.03x slower                                                              |
| tornado_http             | 124 ms                                                                  | 128 ms: 1.03x slower                                                              |
| deepcopy_reduce          | 3.34 us                                                                 | 3.45 us: 1.03x slower                                                             |
| pyflate                  | 562 ms                                                                  | 580 ms: 1.03x slower                                                              |
| scimark_sor              | 157 ms                                                                  | 162 ms: 1.03x slower                                                              |
| scimark_monte_carlo      | 80.4 ms                                                                 | 83.4 ms: 1.04x slower                                                             |
| Geometric mean           | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (56): gc_traversal, json_loads, json, async_tree_memoization_tg, pickle_pure_python, telco, async_tree_none_tg, pprint_safe_repr, logging_format, async_tree_none, dask, sqlglot_normalize, sqlglot_transpile, logging_simple, unpickle_pure_python, comprehensions, json_dumps, pycparser, go, async_tree_cpu_io_mixed, pidigits, pathlib, regex_effbot, nqueens, spectral_norm, 2to3, crypto_pyaes, mdp, bpe_tokeniser, async_tree_io_tg, python_startup, async_generators, asyncio_websockets, meteor_contest, deepcopy, richards, bench_mp_pool, async_tree_memoization, sympy_str, create_gc_cycles, sqlglot_optimize, xml_etree_parse, django_template, pylint, chaos, richards_super, async_tree_cpu_io_mixed_tg, regex_compile, genshi_xml, coverage, hexiom, html5lib, xml_etree_process, python_startup_no_site, xml_etree_iterparse, async_tree_io

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x