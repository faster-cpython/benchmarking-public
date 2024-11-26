# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.001x slower
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| coroutines             | 28.7 ms                                                                 | 28.3 ms: 1.01x faster                                                   |
| async_tree_memoization | 555 ms                                                                  | 568 ms: 1.02x slower                                                    |
| async_tree_none        | 424 ms                                                                  | 437 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (10): async_generators, asyncio_tcp_ssl, async_tree_memoization_tg, async_tree_io, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_tcp

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 125 ms                                                                  | 127 ms: 1.02x slower                                                    |
| regex_effbot   | 4.84 ms                                                                 | 4.94 ms: 1.02x slower                                                   |
| regex_dna      | 247 ms                                                                  | 254 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|---------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse | 149 ms                                                                  | 146 ms: 1.02x faster                                                    |
| Geometric mean      | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (8): xml_etree_generate, pickle_pure_python, json_dumps, unpickle_pure_python, tomli_loads, json_loads, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.8 ms                                                                 | 41.7 ms: 1.03x faster                                                   |
| genshi_text     | 27.7 ms                                                                 | 27.1 ms: 1.02x faster                                                   |
| Geometric mean  | (ref)                                                                   | 1.02x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark               | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pprint_safe_repr        | 942 ms                                                                  | 905 ms: 1.04x faster                                                    |
| django_template         | 42.8 ms                                                                 | 41.7 ms: 1.03x faster                                                   |
| pprint_pformat          | 1.91 sec                                                                | 1.87 sec: 1.02x faster                                                  |
| xml_etree_iterparse     | 149 ms                                                                  | 146 ms: 1.02x faster                                                    |
| deepcopy_reduce         | 3.56 us                                                                 | 3.48 us: 1.02x faster                                                   |
| nqueens                 | 101 ms                                                                  | 98.9 ms: 1.02x faster                                                   |
| genshi_text             | 27.7 ms                                                                 | 27.1 ms: 1.02x faster                                                   |
| deepcopy                | 334 us                                                                  | 329 us: 1.02x faster                                                    |
| thrift                  | 954 us                                                                  | 939 us: 1.02x faster                                                    |
| bench_thread_pool       | 1.24 ms                                                                 | 1.23 ms: 1.02x faster                                                   |
| coroutines              | 28.7 ms                                                                 | 28.3 ms: 1.01x faster                                                   |
| richards_super          | 59.6 ms                                                                 | 59.2 ms: 1.01x faster                                                   |
| mdp                     | 3.34 sec                                                                | 3.35 sec: 1.01x slower                                                  |
| scimark_sparse_mat_mult | 6.33 ms                                                                 | 6.39 ms: 1.01x slower                                                   |
| fannkuch                | 460 ms                                                                  | 465 ms: 1.01x slower                                                    |
| comprehensions          | 20.4 us                                                                 | 20.6 us: 1.01x slower                                                   |
| pycparser               | 1.22 sec                                                                | 1.23 sec: 1.01x slower                                                  |
| regex_compile           | 125 ms                                                                  | 127 ms: 1.02x slower                                                    |
| bpe_tokeniser           | 5.85 sec                                                                | 5.94 sec: 1.02x slower                                                  |
| regex_effbot            | 4.84 ms                                                                 | 4.94 ms: 1.02x slower                                                   |
| async_tree_memoization  | 555 ms                                                                  | 568 ms: 1.02x slower                                                    |
| hexiom                  | 7.02 ms                                                                 | 7.22 ms: 1.03x slower                                                   |
| regex_dna               | 247 ms                                                                  | 254 ms: 1.03x slower                                                    |
| async_tree_none         | 424 ms                                                                  | 437 ms: 1.03x slower                                                    |
| gc_traversal            | 4.84 ms                                                                 | 4.99 ms: 1.03x slower                                                   |
| meteor_contest          | 112 ms                                                                  | 115 ms: 1.03x slower                                                    |
| pyflate                 | 560 ms                                                                  | 582 ms: 1.04x slower                                                    |
| Geometric mean          | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (62): genshi_xml, xml_etree_generate, pickle_pure_python, sqlglot_parse, 2to3, logging_simple, deltablue, pathlib, richards, async_generators, go, generators, tornado_http, logging_silent, json_dumps, nbody, asyncio_tcp_ssl, scimark_fft, sympy_integrate, telco, unpickle_pure_python, python_startup_no_site, tomli_loads, sympy_str, pidigits, float, docutils, mako, sqlglot_transpile, scimark_sor, python_startup, async_tree_memoization_tg, async_tree_io, sqlglot_optimize, json_loads, create_gc_cycles, logging_format, html5lib, chaos, sympy_expand, raytrace, xml_etree_parse, spectral_norm, asyncio_websockets, sqlglot_normalize, bench_mp_pool, async_tree_cpu_io_mixed_tg, coverage, regex_v8, async_tree_io_tg, pylint, json, crypto_pyaes, deepcopy_memo, scimark_monte_carlo, async_tree_cpu_io_mixed, sympy_sum, scimark_lu, typing_runtime_protocols, xml_etree_process, async_tree_none_tg, asyncio_tcp

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 99.83% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x