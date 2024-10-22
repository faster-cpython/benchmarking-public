# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-aarch64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.01x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.52 sec                                                                | 3.55 sec: 1.01x slower                                                  |
| tornado_http   | 139 ms                                                                  | 144 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                            |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 581 ms                                                                  | 587 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed_tg | 712 ms                                                                  | 722 ms: 1.01x slower                                                    |
| Geometric mean             | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                                  | 122 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                            |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 180 ms                                                                  | 175 ms: 1.03x faster                                                    |
| regex_v8       | 30.5 ms                                                                 | 30.3 ms: 1.01x faster                                                   |
| regex_effbot   | 4.89 ms                                                                 | 4.95 ms: 1.01x slower                                                   |
| regex_dna      | 248 ms                                                                  | 259 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.63 sec                                                                | 2.67 sec: 1.02x slower                                                  |
| unpickle_pure_python | 274 us                                                                  | 279 us: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (7): xml_etree_iterparse, xml_etree_parse, xml_etree_generate, json_loads, pickle_pure_python, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.83 ms                                                                 | 8.90 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.1 ms                                                                 | 13.4 ms: 1.02x slower                                                   |
| genshi_xml     | 79.6 ms                                                                 | 84.9 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| sympy_sum                  | 192 ms                                                                  | 183 ms: 1.05x faster                                                    |
| regex_compile              | 180 ms                                                                  | 175 ms: 1.03x faster                                                    |
| sympy_str                  | 332 ms                                                                  | 323 ms: 1.03x faster                                                    |
| hexiom                     | 9.01 ms                                                                 | 8.81 ms: 1.02x faster                                                   |
| sympy_expand               | 550 ms                                                                  | 542 ms: 1.02x faster                                                    |
| scimark_sor                | 179 ms                                                                  | 177 ms: 1.01x faster                                                    |
| sympy_integrate            | 26.6 ms                                                                 | 26.3 ms: 1.01x faster                                                   |
| telco                      | 10.6 ms                                                                 | 10.4 ms: 1.01x faster                                                   |
| json                       | 5.87 ms                                                                 | 5.81 ms: 1.01x faster                                                   |
| nqueens                    | 118 ms                                                                  | 117 ms: 1.01x faster                                                    |
| logging_format             | 7.98 us                                                                 | 7.90 us: 1.01x faster                                                   |
| regex_v8                   | 30.5 ms                                                                 | 30.3 ms: 1.01x faster                                                   |
| python_startup_no_site     | 8.83 ms                                                                 | 8.90 ms: 1.01x slower                                                   |
| gc_traversal               | 5.00 ms                                                                 | 5.04 ms: 1.01x slower                                                   |
| docutils                   | 3.52 sec                                                                | 3.55 sec: 1.01x slower                                                  |
| richards                   | 54.3 ms                                                                 | 54.8 ms: 1.01x slower                                                   |
| async_tree_memoization     | 581 ms                                                                  | 587 ms: 1.01x slower                                                    |
| sqlglot_transpile          | 2.01 ms                                                                 | 2.04 ms: 1.01x slower                                                   |
| regex_effbot               | 4.89 ms                                                                 | 4.95 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed_tg | 712 ms                                                                  | 722 ms: 1.01x slower                                                    |
| scimark_sparse_mat_mult    | 6.89 ms                                                                 | 7.00 ms: 1.02x slower                                                   |
| tomli_loads                | 2.63 sec                                                                | 2.67 sec: 1.02x slower                                                  |
| pprint_pformat             | 2.38 sec                                                                | 2.42 sec: 1.02x slower                                                  |
| deepcopy_memo              | 38.1 us                                                                 | 38.8 us: 1.02x slower                                                   |
| pprint_safe_repr           | 1.15 sec                                                                | 1.16 sec: 1.02x slower                                                  |
| comprehensions             | 23.3 us                                                                 | 23.7 us: 1.02x slower                                                   |
| mako                       | 13.1 ms                                                                 | 13.4 ms: 1.02x slower                                                   |
| unpickle_pure_python       | 274 us                                                                  | 279 us: 1.02x slower                                                    |
| create_gc_cycles           | 2.32 ms                                                                 | 2.37 ms: 1.02x slower                                                   |
| thrift                     | 958 us                                                                  | 978 us: 1.02x slower                                                    |
| deepcopy                   | 374 us                                                                  | 382 us: 1.02x slower                                                    |
| async_generators           | 499 ms                                                                  | 511 ms: 1.02x slower                                                    |
| scimark_monte_carlo        | 89.2 ms                                                                 | 91.5 ms: 1.03x slower                                                   |
| crypto_pyaes               | 87.5 ms                                                                 | 90.0 ms: 1.03x slower                                                   |
| deepcopy_reduce            | 4.08 us                                                                 | 4.21 us: 1.03x slower                                                   |
| tornado_http               | 139 ms                                                                  | 144 ms: 1.03x slower                                                    |
| pyflate                    | 599 ms                                                                  | 621 ms: 1.04x slower                                                    |
| spectral_norm              | 144 ms                                                                  | 149 ms: 1.04x slower                                                    |
| pathlib                    | 21.7 ms                                                                 | 22.6 ms: 1.04x slower                                                   |
| regex_dna                  | 248 ms                                                                  | 259 ms: 1.04x slower                                                    |
| logging_silent             | 136 ns                                                                  | 142 ns: 1.04x slower                                                    |
| chaos                      | 89.3 ms                                                                 | 93.3 ms: 1.04x slower                                                   |
| nbody                      | 114 ms                                                                  | 122 ms: 1.07x slower                                                    |
| genshi_xml                 | 79.6 ms                                                                 | 84.9 ms: 1.07x slower                                                   |
| bench_mp_pool              | 8.21 ms                                                                 | 13.2 ms: 1.61x slower                                                   |
| Geometric mean             | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (46): xml_etree_iterparse, sqlglot_optimize, pylint, coverage, async_tree_none_tg, generators, fannkuch, mdp, xml_etree_parse, typing_runtime_protocols, xml_etree_generate, go, json_loads, pickle_pure_python, async_tree_memoization_tg, pidigits, bpe_tokeniser, deltablue, async_tree_io_tg, raytrace, async_tree_none, float, asyncio_tcp, asyncio_tcp_ssl, python_startup, django_template, sqlglot_normalize, dask, bench_thread_pool, async_tree_cpu_io_mixed, asyncio_websockets, scimark_lu, async_tree_io, 2to3, json_dumps, pycparser, logging_simple, richards_super, genshi_text, coroutines, dulwich_log, scimark_fft, meteor_contest, sqlglot_parse, xml_etree_process, html5lib

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x