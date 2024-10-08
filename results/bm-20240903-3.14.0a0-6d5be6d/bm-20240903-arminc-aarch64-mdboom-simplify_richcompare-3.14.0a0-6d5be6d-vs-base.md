# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.00x faster
- HPT reliability: 79.06%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_tcp_ssl | 2.18 sec                                                                | 2.20 sec: 1.01x slower                                                  |
| asyncio_tcp     | 557 ms                                                                  | 568 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, coroutines, async_tree_none, async_tree_io, async_generators, async_tree_memoization, asyncio_websockets, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 110 ms                                                                  | 108 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 127 ms                                                                  | 125 ms: 1.01x faster                                                    |
| regex_effbot   | 4.80 ms                                                                 | 4.89 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 365 us                                                                  | 358 us: 1.02x faster                                                    |
| unpickle_pure_python | 255 us                                                                  | 252 us: 1.01x faster                                                    |
| tomli_loads          | 2.62 sec                                                                | 2.64 sec: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (6): xml_etree_generate, xml_etree_iterparse, xml_etree_process, json_dumps, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.4 ms                                                                 | 13.4 ms: 1.00x faster                                                   |
| genshi_text    | 27.1 ms                                                                 | 27.5 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark            | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nqueens              | 101 ms                                                                  | 97.4 ms: 1.04x faster                                                   |
| pprint_safe_repr     | 933 ms                                                                  | 907 ms: 1.03x faster                                                    |
| deepcopy_reduce      | 3.56 us                                                                 | 3.47 us: 1.03x faster                                                   |
| scimark_monte_carlo  | 82.3 ms                                                                 | 80.4 ms: 1.02x faster                                                   |
| telco                | 10.0 ms                                                                 | 9.81 ms: 1.02x faster                                                   |
| meteor_contest       | 113 ms                                                                  | 110 ms: 1.02x faster                                                    |
| pickle_pure_python   | 365 us                                                                  | 358 us: 1.02x faster                                                    |
| scimark_lu           | 136 ms                                                                  | 133 ms: 1.02x faster                                                    |
| pprint_pformat       | 1.90 sec                                                                | 1.87 sec: 1.02x faster                                                  |
| deepcopy_memo        | 38.5 us                                                                 | 37.9 us: 1.02x faster                                                   |
| logging_format       | 7.76 us                                                                 | 7.64 us: 1.01x faster                                                   |
| nbody                | 110 ms                                                                  | 108 ms: 1.01x faster                                                    |
| regex_compile        | 127 ms                                                                  | 125 ms: 1.01x faster                                                    |
| unpickle_pure_python | 255 us                                                                  | 252 us: 1.01x faster                                                    |
| coverage             | 99.0 ms                                                                 | 97.8 ms: 1.01x faster                                                   |
| hexiom               | 7.08 ms                                                                 | 7.02 ms: 1.01x faster                                                   |
| fannkuch             | 464 ms                                                                  | 460 ms: 1.01x faster                                                    |
| comprehensions       | 20.4 us                                                                 | 20.3 us: 1.01x faster                                                   |
| mako                 | 13.4 ms                                                                 | 13.4 ms: 1.00x faster                                                   |
| pyflate              | 571 ms                                                                  | 575 ms: 1.01x slower                                                    |
| tomli_loads          | 2.62 sec                                                                | 2.64 sec: 1.01x slower                                                  |
| deepcopy             | 330 us                                                                  | 333 us: 1.01x slower                                                    |
| asyncio_tcp_ssl      | 2.18 sec                                                                | 2.20 sec: 1.01x slower                                                  |
| genshi_text          | 27.1 ms                                                                 | 27.5 ms: 1.01x slower                                                   |
| regex_effbot         | 4.80 ms                                                                 | 4.89 ms: 1.02x slower                                                   |
| asyncio_tcp          | 557 ms                                                                  | 568 ms: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (63): tornado_http, genshi_xml, deltablue, xml_etree_generate, xml_etree_iterparse, bench_thread_pool, xml_etree_process, typing_runtime_protocols, go, sqlglot_parse, raytrace, generators, sympy_sum, sympy_expand, richards_super, pathlib, sqlglot_optimize, django_template, scimark_sparse_mat_mult, async_tree_cpu_io_mixed, richards, scimark_sor, logging_simple, json_dumps, pylint, logging_silent, xml_etree_parse, bench_mp_pool, html5lib, sympy_str, crypto_pyaes, float, python_startup, chaos, coroutines, mdp, async_tree_none, sqlglot_normalize, json, async_tree_io, pycparser, bpe_tokeniser, spectral_norm, pidigits, async_generators, python_startup_no_site, create_gc_cycles, docutils, sympy_integrate, async_tree_memoization, regex_v8, asyncio_websockets, scimark_fft, thrift, sqlglot_transpile, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, json_loads, async_tree_none_tg, async_tree_io_tg, gc_traversal, 2to3, regex_dna

# HPT report

- Reliability score: 79.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x