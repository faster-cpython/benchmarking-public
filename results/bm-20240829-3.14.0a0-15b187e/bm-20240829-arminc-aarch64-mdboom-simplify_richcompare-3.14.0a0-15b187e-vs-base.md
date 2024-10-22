# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.00x faster
- HPT reliability: 66.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.01 sec                                                                | 2.98 sec: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_tcp     | 564 ms                                                                  | 538 ms: 1.05x faster                                                    |
| asyncio_tcp_ssl | 2.21 sec                                                                | 2.16 sec: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (11): async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_generators, async_tree_none_tg, async_tree_none, async_tree_io_tg, async_tree_memoization, asyncio_websockets, async_tree_io, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 110 ms                                                                  | 112 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 125 ms                                                                  | 127 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|---------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse | 149 ms                                                                  | 146 ms: 1.02x faster                                                    |
| tomli_loads         | 2.63 sec                                                                | 2.65 sec: 1.01x slower                                                  |
| Geometric mean      | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (7): pickle_pure_python, xml_etree_process, xml_etree_parse, unpickle_pure_python, xml_etree_generate, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                 | 13.0 ms: 1.01x faster                                                   |
| python_startup_no_site | 8.81 ms                                                                 | 8.73 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, django_template, genshi_text, mako

All benchmarks:
===============

| Benchmark               | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_tcp             | 564 ms                                                                  | 538 ms: 1.05x faster                                                    |
| pprint_safe_repr        | 942 ms                                                                  | 910 ms: 1.04x faster                                                    |
| thrift                  | 954 us                                                                  | 926 us: 1.03x faster                                                    |
| pprint_pformat          | 1.91 sec                                                                | 1.87 sec: 1.02x faster                                                  |
| asyncio_tcp_ssl         | 2.21 sec                                                                | 2.16 sec: 1.02x faster                                                  |
| deepcopy_reduce         | 3.56 us                                                                 | 3.49 us: 1.02x faster                                                   |
| xml_etree_iterparse     | 149 ms                                                                  | 146 ms: 1.02x faster                                                    |
| richards                | 53.6 ms                                                                 | 52.7 ms: 1.02x faster                                                   |
| telco                   | 10.1 ms                                                                 | 9.94 ms: 1.01x faster                                                   |
| bench_thread_pool       | 1.24 ms                                                                 | 1.23 ms: 1.01x faster                                                   |
| python_startup          | 13.1 ms                                                                 | 13.0 ms: 1.01x faster                                                   |
| nqueens                 | 101 ms                                                                  | 99.9 ms: 1.01x faster                                                   |
| docutils                | 3.01 sec                                                                | 2.98 sec: 1.01x faster                                                  |
| python_startup_no_site  | 8.81 ms                                                                 | 8.73 ms: 1.01x faster                                                   |
| pyflate                 | 560 ms                                                                  | 562 ms: 1.01x slower                                                    |
| tomli_loads             | 2.63 sec                                                                | 2.65 sec: 1.01x slower                                                  |
| bpe_tokeniser           | 5.85 sec                                                                | 5.90 sec: 1.01x slower                                                  |
| fannkuch                | 460 ms                                                                  | 464 ms: 1.01x slower                                                    |
| scimark_fft             | 440 ms                                                                  | 445 ms: 1.01x slower                                                    |
| mdp                     | 3.34 sec                                                                | 3.37 sec: 1.01x slower                                                  |
| scimark_sparse_mat_mult | 6.33 ms                                                                 | 6.42 ms: 1.01x slower                                                   |
| regex_compile           | 125 ms                                                                  | 127 ms: 1.01x slower                                                    |
| json                    | 5.69 ms                                                                 | 5.77 ms: 1.01x slower                                                   |
| bench_mp_pool           | 7.04 ms                                                                 | 7.15 ms: 1.02x slower                                                   |
| scimark_lu              | 134 ms                                                                  | 136 ms: 1.02x slower                                                    |
| nbody                   | 110 ms                                                                  | 112 ms: 1.02x slower                                                    |
| gc_traversal            | 4.84 ms                                                                 | 4.97 ms: 1.03x slower                                                   |
| hexiom                  | 7.02 ms                                                                 | 7.21 ms: 1.03x slower                                                   |
| Geometric mean          | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (61): genshi_xml, tornado_http, sqlglot_parse, 2to3, pickle_pure_python, async_tree_memoization_tg, xml_etree_process, async_tree_cpu_io_mixed, deltablue, async_tree_cpu_io_mixed_tg, sqlglot_transpile, django_template, generators, logging_simple, sympy_str, richards_super, genshi_text, async_generators, regex_dna, sympy_expand, spectral_norm, mako, async_tree_none_tg, async_tree_none, pylint, coverage, deepcopy_memo, pidigits, async_tree_io_tg, sympy_integrate, html5lib, pycparser, async_tree_memoization, create_gc_cycles, scimark_monte_carlo, xml_etree_parse, pathlib, unpickle_pure_python, regex_effbot, xml_etree_generate, json_dumps, crypto_pyaes, sympy_sum, regex_v8, float, sqlglot_optimize, chaos, asyncio_websockets, meteor_contest, typing_runtime_protocols, async_tree_io, raytrace, deepcopy, scimark_sor, logging_silent, json_loads, coroutines, logging_format, comprehensions, go, sqlglot_normalize

# HPT report

- Reliability score: 66.52% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x