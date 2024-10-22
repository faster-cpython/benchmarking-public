# Results vs. base

- fork: faster-cpython
- ref: bound_method_instrum
- machine: linux-aarch64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.00x faster
- HPT reliability: 65.42%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 3.08 sec                                                                | 3.05 sec: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization | 569 ms                                                                  | 552 ms: 1.03x faster                                                              |
| asyncio_tcp            | 587 ms                                                                  | 570 ms: 1.03x faster                                                              |
| async_generators       | 486 ms                                                                  | 492 ms: 1.01x slower                                                              |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                                      |

Benchmark hidden because not significant (10): async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 258 ms                                                                  | 249 ms: 1.03x faster                                                              |
| regex_effbot   | 4.96 ms                                                                 | 4.88 ms: 1.02x faster                                                             |
| regex_v8       | 30.4 ms                                                                 | 31.2 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): xml_etree_generate, xml_etree_iterparse, pickle_pure_python, json_loads, unpickle_pure_python, tomli_loads, json_dumps, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 41.7 ms                                                                 | 41.5 ms: 1.01x faster                                                             |
| mako            | 13.3 ms                                                                 | 13.4 ms: 1.01x slower                                                             |
| Geometric mean  | (ref)                                                                   | 1.00x faster                                                                      |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| gc_traversal            | 5.08 ms                                                                 | 4.88 ms: 1.04x faster                                                             |
| regex_dna               | 258 ms                                                                  | 249 ms: 1.03x faster                                                              |
| fannkuch                | 478 ms                                                                  | 463 ms: 1.03x faster                                                              |
| async_tree_memoization  | 569 ms                                                                  | 552 ms: 1.03x faster                                                              |
| asyncio_tcp             | 587 ms                                                                  | 570 ms: 1.03x faster                                                              |
| scimark_sparse_mat_mult | 6.52 ms                                                                 | 6.38 ms: 1.02x faster                                                             |
| regex_effbot            | 4.96 ms                                                                 | 4.88 ms: 1.02x faster                                                             |
| pycparser               | 1.23 sec                                                                | 1.22 sec: 1.01x faster                                                            |
| create_gc_cycles        | 2.31 ms                                                                 | 2.28 ms: 1.01x faster                                                             |
| go                      | 161 ms                                                                  | 159 ms: 1.01x faster                                                              |
| docutils                | 3.08 sec                                                                | 3.05 sec: 1.01x faster                                                            |
| django_template         | 41.7 ms                                                                 | 41.5 ms: 1.01x faster                                                             |
| sqlglot_transpile       | 1.71 ms                                                                 | 1.72 ms: 1.01x slower                                                             |
| pprint_pformat          | 1.92 sec                                                                | 1.94 sec: 1.01x slower                                                            |
| mako                    | 13.3 ms                                                                 | 13.4 ms: 1.01x slower                                                             |
| sympy_sum               | 143 ms                                                                  | 145 ms: 1.01x slower                                                              |
| async_generators        | 486 ms                                                                  | 492 ms: 1.01x slower                                                              |
| mdp                     | 3.32 sec                                                                | 3.37 sec: 1.01x slower                                                            |
| deepcopy_reduce         | 3.37 us                                                                 | 3.42 us: 1.01x slower                                                             |
| dulwich_log             | 57.9 ms                                                                 | 58.8 ms: 1.01x slower                                                             |
| thrift                  | 939 us                                                                  | 954 us: 1.02x slower                                                              |
| pprint_safe_repr        | 936 ms                                                                  | 952 ms: 1.02x slower                                                              |
| pyflate                 | 562 ms                                                                  | 576 ms: 1.02x slower                                                              |
| regex_v8                | 30.4 ms                                                                 | 31.2 ms: 1.03x slower                                                             |
| nqueens                 | 97.1 ms                                                                 | 99.5 ms: 1.03x slower                                                             |
| Geometric mean          | (ref)                                                                   | 1.00x faster                                                                      |

Benchmark hidden because not significant (66): sqlglot_normalize, async_tree_io, async_tree_io_tg, genshi_xml, logging_simple, xml_etree_generate, async_tree_cpu_io_mixed, xml_etree_iterparse, bench_thread_pool, async_tree_none, pickle_pure_python, scimark_fft, genshi_text, scimark_monte_carlo, pylint, python_startup, async_tree_memoization_tg, scimark_sor, async_tree_none_tg, sympy_integrate, hexiom, logging_silent, float, async_tree_cpu_io_mixed_tg, json_loads, unpickle_pure_python, richards, sympy_expand, tomli_loads, regex_compile, asyncio_tcp_ssl, richards_super, pidigits, coroutines, deepcopy, asyncio_websockets, typing_runtime_protocols, chaos, 2to3, nbody, coverage, meteor_contest, crypto_pyaes, spectral_norm, deepcopy_memo, bpe_tokeniser, pathlib, sqlglot_optimize, scimark_lu, sympy_str, bench_mp_pool, telco, generators, tornado_http, json, json_dumps, html5lib, logging_format, comprehensions, raytrace, python_startup_no_site, dask, deltablue, xml_etree_process, sqlglot_parse, xml_etree_parse

# HPT report

- Reliability score: 65.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x