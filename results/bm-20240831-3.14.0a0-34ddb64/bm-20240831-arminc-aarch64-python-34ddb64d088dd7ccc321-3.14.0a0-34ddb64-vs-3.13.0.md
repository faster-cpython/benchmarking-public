# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.031x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 294 ms: 1.03x faster                                                    |
| docutils       | 2.89 sec                                                 | 3.04 sec: 1.05x slower                                                  |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 544 ms: 1.19x faster                                                    |
| async_tree_none            | 497 ms                                                   | 422 ms: 1.18x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 559 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 416 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 722 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 726 ms: 1.05x faster                                                    |
| async_generators           | 489 ms                                                   | 474 ms: 1.03x faster                                                    |
| coroutines                 | 28.5 ms                                                  | 28.3 ms: 1.01x faster                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.16 sec: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.07x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| float          | 93.3 ms                                                  | 92.7 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.2 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (3): regex_compile, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 186 ms: 1.05x faster                                                    |
| unpickle_pure_python | 251 us                                                   | 254 us: 1.01x slower                                                    |
| json_loads           | 31.7 us                                                  | 32.5 us: 1.03x slower                                                   |
| tomli_loads          | 2.54 sec                                                 | 2.62 sec: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (5): xml_etree_process, json_dumps, pickle_pure_python, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                                   |
| Geometric mean | (ref)                                                    | 1.08x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.7 ms                                                  | 27.5 ms: 1.01x faster                                                   |
| mako           | 13.4 ms                                                  | 13.3 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.29 ms: 1.46x faster                                                   |
| deepcopy                   | 447 us                                                   | 337 us: 1.33x faster                                                    |
| deepcopy_memo              | 50.4 us                                                  | 38.2 us: 1.32x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 544 ms: 1.19x faster                                                    |
| python_startup             | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                                   |
| async_tree_none            | 497 ms                                                   | 422 ms: 1.18x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 559 ms: 1.16x faster                                                    |
| go                         | 160 ms                                                   | 138 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.51 us: 1.16x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 4.99 ms: 1.16x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 416 ms: 1.13x faster                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 7.00 ms: 1.10x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 21.0 ms: 1.08x faster                                                   |
| generators                 | 37.6 ms                                                  | 35.0 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 722 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 726 ms: 1.05x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 30.2 ms: 1.05x faster                                                   |
| xml_etree_parse            | 197 ms                                                   | 186 ms: 1.05x faster                                                    |
| nbody                      | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| pycparser                  | 1.27 sec                                                 | 1.21 sec: 1.05x faster                                                  |
| thrift                     | 968 us                                                   | 931 us: 1.04x faster                                                    |
| 2to3                       | 304 ms                                                   | 294 ms: 1.03x faster                                                    |
| async_generators           | 489 ms                                                   | 474 ms: 1.03x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 135 ms: 1.03x faster                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| logging_format             | 7.82 us                                                  | 7.64 us: 1.02x faster                                                   |
| logging_simple             | 7.07 us                                                  | 6.91 us: 1.02x faster                                                   |
| scimark_sor                | 160 ms                                                   | 157 ms: 1.02x faster                                                    |
| sympy_sum                  | 144 ms                                                   | 141 ms: 1.02x faster                                                    |
| scimark_fft                | 447 ms                                                   | 439 ms: 1.02x faster                                                    |
| meteor_contest             | 114 ms                                                   | 112 ms: 1.02x faster                                                    |
| logging_silent             | 133 ns                                                   | 131 ns: 1.02x faster                                                    |
| pprint_safe_repr           | 926 ms                                                   | 915 ms: 1.01x faster                                                    |
| sympy_integrate            | 20.8 ms                                                  | 20.6 ms: 1.01x faster                                                   |
| genshi_text                | 27.7 ms                                                  | 27.5 ms: 1.01x faster                                                   |
| mako                       | 13.4 ms                                                  | 13.3 ms: 1.01x faster                                                   |
| coroutines                 | 28.5 ms                                                  | 28.3 ms: 1.01x faster                                                   |
| float                      | 93.3 ms                                                  | 92.7 ms: 1.01x faster                                                   |
| raytrace                   | 300 ms                                                   | 301 ms: 1.01x slower                                                    |
| sympy_expand               | 457 ms                                                   | 462 ms: 1.01x slower                                                    |
| unpickle_pure_python       | 251 us                                                   | 254 us: 1.01x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.40 ms: 1.02x slower                                                   |
| pyflate                    | 556 ms                                                   | 567 ms: 1.02x slower                                                    |
| comprehensions             | 20.4 us                                                  | 20.8 us: 1.02x slower                                                   |
| json_loads                 | 31.7 us                                                  | 32.5 us: 1.03x slower                                                   |
| deltablue                  | 3.82 ms                                                  | 3.92 ms: 1.03x slower                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.16 sec: 1.03x slower                                                  |
| tomli_loads                | 2.54 sec                                                 | 2.62 sec: 1.03x slower                                                  |
| docutils                   | 2.89 sec                                                 | 3.04 sec: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (38): html5lib, xml_etree_process, scimark_sparse_mat_mult, json_dumps, scimark_monte_carlo, regex_compile, spectral_norm, genshi_xml, django_template, json, crypto_pyaes, pickle_pure_python, xml_etree_generate, nqueens, typing_runtime_protocols, sympy_str, asyncio_websockets, coverage, sqlglot_normalize, bpe_tokeniser, sqlglot_transpile, regex_effbot, pprint_pformat, telco, xml_etree_iterparse, regex_dna, hexiom, pidigits, mdp, python_startup_no_site, sqlglot_optimize, fannkuch, chaos, richards_super, tornado_http, async_tree_io, richards, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x