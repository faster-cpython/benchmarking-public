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
| 2to3           | 299 ms                                                                  | 303 ms: 1.01x slower                                                              |
| docutils       | 3.14 sec                                                                | 3.20 sec: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                                      |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp_ssl | 2.19 sec                                                                | 2.20 sec: 1.01x slower                                                            |
| async_tree_io   | 1.08 sec                                                                | 1.12 sec: 1.03x slower                                                            |
| Geometric mean  | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (11): async_tree_none, async_tree_memoization, async_tree_none_tg, coroutines, async_tree_cpu_io_mixed, asyncio_websockets, async_generators, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, asyncio_tcp, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 91.8 ms                                                                 | 93.7 ms: 1.02x slower                                                             |
| nbody          | 107 ms                                                                  | 111 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                  | 253 ms: 1.02x faster                                                              |
| regex_v8       | 30.2 ms                                                                 | 30.5 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads    | 2.53 sec                                                                | 2.56 sec: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (8): xml_etree_process, unpickle_pure_python, xml_etree_parse, json_loads, json_dumps, pickle_pure_python, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 41.4 ms                                                                 | 42.3 ms: 1.02x slower                                                             |
| mako            | 13.2 ms                                                                 | 13.5 ms: 1.02x slower                                                             |
| genshi_xml      | 59.7 ms                                                                 | 61.6 ms: 1.03x slower                                                             |
| Geometric mean  | (ref)                                                                   | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| telco                    | 10.0 ms                                                                 | 9.77 ms: 1.03x faster                                                             |
| regex_dna                | 257 ms                                                                  | 253 ms: 1.02x faster                                                              |
| pprint_pformat           | 1.94 sec                                                                | 1.93 sec: 1.01x faster                                                            |
| pprint_safe_repr         | 949 ms                                                                  | 942 ms: 1.01x faster                                                              |
| asyncio_tcp_ssl          | 2.19 sec                                                                | 2.20 sec: 1.01x slower                                                            |
| sqlglot_transpile        | 1.71 ms                                                                 | 1.72 ms: 1.01x slower                                                             |
| deepcopy_memo            | 38.0 us                                                                 | 38.3 us: 1.01x slower                                                             |
| sympy_str                | 266 ms                                                                  | 268 ms: 1.01x slower                                                              |
| json                     | 5.64 ms                                                                 | 5.70 ms: 1.01x slower                                                             |
| tomli_loads              | 2.53 sec                                                                | 2.56 sec: 1.01x slower                                                            |
| regex_v8                 | 30.2 ms                                                                 | 30.5 ms: 1.01x slower                                                             |
| scimark_sparse_mat_mult  | 6.41 ms                                                                 | 6.50 ms: 1.01x slower                                                             |
| 2to3                     | 299 ms                                                                  | 303 ms: 1.01x slower                                                              |
| sympy_sum                | 143 ms                                                                  | 145 ms: 1.01x slower                                                              |
| logging_format           | 7.58 us                                                                 | 7.70 us: 1.02x slower                                                             |
| generators               | 34.9 ms                                                                 | 35.4 ms: 1.02x slower                                                             |
| meteor_contest           | 112 ms                                                                  | 114 ms: 1.02x slower                                                              |
| scimark_monte_carlo      | 82.1 ms                                                                 | 83.4 ms: 1.02x slower                                                             |
| richards                 | 52.0 ms                                                                 | 52.9 ms: 1.02x slower                                                             |
| docutils                 | 3.14 sec                                                                | 3.20 sec: 1.02x slower                                                            |
| gc_traversal             | 4.85 ms                                                                 | 4.95 ms: 1.02x slower                                                             |
| scimark_fft              | 439 ms                                                                  | 448 ms: 1.02x slower                                                              |
| float                    | 91.8 ms                                                                 | 93.7 ms: 1.02x slower                                                             |
| scimark_lu               | 136 ms                                                                  | 139 ms: 1.02x slower                                                              |
| django_template          | 41.4 ms                                                                 | 42.3 ms: 1.02x slower                                                             |
| mako                     | 13.2 ms                                                                 | 13.5 ms: 1.02x slower                                                             |
| thrift                   | 943 us                                                                  | 965 us: 1.02x slower                                                              |
| deltablue                | 3.80 ms                                                                 | 3.89 ms: 1.02x slower                                                             |
| typing_runtime_protocols | 194 us                                                                  | 199 us: 1.03x slower                                                              |
| async_tree_io            | 1.08 sec                                                                | 1.12 sec: 1.03x slower                                                            |
| genshi_xml               | 59.7 ms                                                                 | 61.6 ms: 1.03x slower                                                             |
| scimark_sor              | 157 ms                                                                  | 162 ms: 1.03x slower                                                              |
| nbody                    | 107 ms                                                                  | 111 ms: 1.04x slower                                                              |
| Geometric mean           | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (57): async_tree_none, dask, xml_etree_process, deepcopy, unpickle_pure_python, logging_silent, async_tree_memoization, async_tree_none_tg, regex_effbot, pidigits, pyflate, coroutines, crypto_pyaes, async_tree_cpu_io_mixed, fannkuch, bench_thread_pool, pathlib, bench_mp_pool, deepcopy_reduce, asyncio_websockets, spectral_norm, go, xml_etree_parse, mdp, sympy_expand, bpe_tokeniser, async_generators, comprehensions, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, asyncio_tcp, pycparser, coverage, json_loads, chaos, logging_simple, json_dumps, raytrace, sqlglot_optimize, python_startup_no_site, sympy_integrate, regex_compile, async_tree_io_tg, genshi_text, hexiom, richards_super, sqlglot_normalize, nqueens, python_startup, pickle_pure_python, xml_etree_generate, sqlglot_parse, tornado_http, create_gc_cycles, xml_etree_iterparse, pylint, html5lib

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x