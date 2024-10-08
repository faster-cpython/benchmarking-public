# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.00x faster
- HPT reliability: 72.33%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.00 sec                                                                | 3.04 sec: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_tcp     | 557 ms                                                                  | 566 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl | 2.18 sec                                                                | 2.21 sec: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (11): async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization, asyncio_websockets, async_tree_memoization_tg, coroutines, async_tree_io_tg, async_generators, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.4 ms                                                                 | 93.4 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                                  | 254 ms: 1.02x slower                                                    |
| regex_effbot   | 4.80 ms                                                                 | 4.91 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 149 ms                                                                  | 146 ms: 1.02x faster                                                    |
| pickle_pure_python   | 365 us                                                                  | 358 us: 1.02x faster                                                    |
| unpickle_pure_python | 255 us                                                                  | 252 us: 1.02x faster                                                    |
| json_dumps           | 13.5 ms                                                                 | 13.3 ms: 1.01x faster                                                   |
| tomli_loads          | 2.62 sec                                                                | 2.64 sec: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (4): json_loads, xml_etree_process, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.4 ms                                                                 | 13.5 ms: 1.01x slower                                                   |
| genshi_text    | 27.1 ms                                                                 | 27.5 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|--------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pprint_safe_repr         | 933 ms                                                                  | 904 ms: 1.03x faster                                                    |
| pprint_pformat           | 1.90 sec                                                                | 1.85 sec: 1.03x faster                                                  |
| xml_etree_iterparse      | 149 ms                                                                  | 146 ms: 1.02x faster                                                    |
| nqueens                  | 101 ms                                                                  | 99.5 ms: 1.02x faster                                                   |
| typing_runtime_protocols | 194 us                                                                  | 190 us: 1.02x faster                                                    |
| pickle_pure_python       | 365 us                                                                  | 358 us: 1.02x faster                                                    |
| sympy_str                | 265 ms                                                                  | 261 ms: 1.02x faster                                                    |
| deepcopy_reduce          | 3.56 us                                                                 | 3.50 us: 1.02x faster                                                   |
| sympy_expand             | 462 ms                                                                  | 455 ms: 1.02x faster                                                    |
| unpickle_pure_python     | 255 us                                                                  | 252 us: 1.02x faster                                                    |
| json_dumps               | 13.5 ms                                                                 | 13.3 ms: 1.01x faster                                                   |
| logging_format           | 7.76 us                                                                 | 7.64 us: 1.01x faster                                                   |
| richards_super           | 60.2 ms                                                                 | 59.4 ms: 1.01x faster                                                   |
| sqlglot_optimize         | 62.3 ms                                                                 | 61.4 ms: 1.01x faster                                                   |
| sqlglot_parse            | 1.41 ms                                                                 | 1.39 ms: 1.01x faster                                                   |
| thrift                   | 942 us                                                                  | 930 us: 1.01x faster                                                    |
| richards                 | 53.5 ms                                                                 | 53.0 ms: 1.01x faster                                                   |
| generators               | 35.0 ms                                                                 | 34.7 ms: 1.01x faster                                                   |
| scimark_monte_carlo      | 82.3 ms                                                                 | 81.6 ms: 1.01x faster                                                   |
| spectral_norm            | 141 ms                                                                  | 140 ms: 1.01x faster                                                    |
| scimark_sparse_mat_mult  | 6.42 ms                                                                 | 6.39 ms: 1.00x faster                                                   |
| mako                     | 13.4 ms                                                                 | 13.5 ms: 1.01x slower                                                   |
| tomli_loads              | 2.62 sec                                                                | 2.64 sec: 1.01x slower                                                  |
| logging_silent           | 132 ns                                                                  | 133 ns: 1.01x slower                                                    |
| float                    | 92.4 ms                                                                 | 93.4 ms: 1.01x slower                                                   |
| docutils                 | 3.00 sec                                                                | 3.04 sec: 1.01x slower                                                  |
| asyncio_tcp              | 557 ms                                                                  | 566 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl          | 2.18 sec                                                                | 2.21 sec: 1.01x slower                                                  |
| comprehensions           | 20.4 us                                                                 | 20.7 us: 1.02x slower                                                   |
| genshi_text              | 27.1 ms                                                                 | 27.5 ms: 1.02x slower                                                   |
| pyflate                  | 571 ms                                                                  | 581 ms: 1.02x slower                                                    |
| bench_mp_pool            | 6.96 ms                                                                 | 7.09 ms: 1.02x slower                                                   |
| regex_dna                | 249 ms                                                                  | 254 ms: 1.02x slower                                                    |
| regex_effbot             | 4.80 ms                                                                 | 4.91 ms: 1.02x slower                                                   |
| fannkuch                 | 464 ms                                                                  | 475 ms: 1.03x slower                                                    |
| Geometric mean           | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (54): gc_traversal, bench_thread_pool, deepcopy_memo, sympy_sum, genshi_xml, coverage, tornado_http, pycparser, regex_compile, json, go, telco, async_tree_io, async_tree_cpu_io_mixed, scimark_fft, json_loads, async_tree_memoization, xml_etree_process, django_template, logging_simple, crypto_pyaes, xml_etree_generate, scimark_lu, mdp, asyncio_websockets, async_tree_memoization_tg, pidigits, deltablue, coroutines, pathlib, deepcopy, python_startup, async_tree_io_tg, bpe_tokeniser, xml_etree_parse, hexiom, raytrace, sqlglot_transpile, chaos, regex_v8, sympy_integrate, pylint, python_startup_no_site, create_gc_cycles, async_generators, async_tree_none_tg, scimark_sor, async_tree_cpu_io_mixed_tg, meteor_contest, 2to3, async_tree_none, sqlglot_normalize, nbody, html5lib

# HPT report

- Reliability score: 72.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x