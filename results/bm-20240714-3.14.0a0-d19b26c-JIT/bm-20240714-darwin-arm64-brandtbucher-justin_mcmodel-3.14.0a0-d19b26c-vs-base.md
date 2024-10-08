# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel
- machine: darwin-arm64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.00x slower
- HPT reliability: 81.37%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 171 ms                                                                | 172 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_tg | 41.8 ms                                                               | 41.7 ms: 1.00x faster                                                 |
| async_tree_eager    | 63.8 ms                                                               | 64.2 ms: 1.01x slower                                                 |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (14): async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_eager_io, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io, async_tree_eager_cpu_io_mixed, async_tree_none_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 47.3 ms                                                               | 47.4 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                               | 2.57 ms: 1.00x faster                                                 |
| regex_compile  | 73.1 ms                                                               | 72.9 ms: 1.00x faster                                                 |
| regex_dna      | 149 ms                                                                | 149 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps         | 6.45 ms                                                               | 6.41 ms: 1.01x faster                                                 |
| pickle_pure_python | 173 us                                                                | 174 us: 1.01x slower                                                  |
| tomli_loads        | 1.24 sec                                                              | 1.28 sec: 1.03x slower                                                |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (6): xml_etree_iterparse, unpickle_pure_python, xml_etree_process, json_loads, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 15.7 ms                                                               | 15.4 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.48 ms                                                               | 6.53 ms: 1.01x slower                                                 |
| genshi_xml      | 40.0 ms                                                               | 40.3 ms: 1.01x slower                                                 |
| django_template | 21.8 ms                                                               | 22.2 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup          | 15.7 ms                                                               | 15.4 ms: 1.02x faster                                                 |
| thrift                  | 441 us                                                                | 435 us: 1.01x faster                                                  |
| deepcopy_reduce         | 1.56 us                                                               | 1.54 us: 1.01x faster                                                 |
| sympy_str               | 139 ms                                                                | 138 ms: 1.01x faster                                                  |
| comprehensions          | 12.4 us                                                               | 12.3 us: 1.01x faster                                                 |
| json_dumps              | 6.45 ms                                                               | 6.41 ms: 1.01x faster                                                 |
| raytrace                | 165 ms                                                                | 164 ms: 1.01x faster                                                  |
| nqueens                 | 57.9 ms                                                               | 57.6 ms: 1.01x faster                                                 |
| scimark_monte_carlo     | 44.1 ms                                                               | 43.9 ms: 1.00x faster                                                 |
| regex_effbot            | 2.58 ms                                                               | 2.57 ms: 1.00x faster                                                 |
| chaos                   | 39.6 ms                                                               | 39.4 ms: 1.00x faster                                                 |
| async_tree_eager_tg     | 41.8 ms                                                               | 41.7 ms: 1.00x faster                                                 |
| regex_compile           | 73.1 ms                                                               | 72.9 ms: 1.00x faster                                                 |
| regex_dna               | 149 ms                                                                | 149 ms: 1.00x faster                                                  |
| scimark_fft             | 191 ms                                                                | 191 ms: 1.00x faster                                                  |
| scimark_sparse_mat_mult | 3.03 ms                                                               | 3.02 ms: 1.00x faster                                                 |
| spectral_norm           | 68.4 ms                                                               | 68.6 ms: 1.00x slower                                                 |
| sympy_integrate         | 11.0 ms                                                               | 11.0 ms: 1.00x slower                                                 |
| async_generators        | 293 ms                                                                | 294 ms: 1.00x slower                                                  |
| float                   | 47.3 ms                                                               | 47.4 ms: 1.00x slower                                                 |
| sqlglot_optimize        | 33.0 ms                                                               | 33.1 ms: 1.00x slower                                                 |
| scimark_sor             | 102 ms                                                                | 102 ms: 1.00x slower                                                  |
| meteor_contest          | 72.3 ms                                                               | 72.7 ms: 1.01x slower                                                 |
| sqlglot_normalize       | 178 ms                                                                | 178 ms: 1.01x slower                                                  |
| async_tree_eager        | 63.8 ms                                                               | 64.2 ms: 1.01x slower                                                 |
| pickle_pure_python      | 173 us                                                                | 174 us: 1.01x slower                                                  |
| mako                    | 6.48 ms                                                               | 6.53 ms: 1.01x slower                                                 |
| mdp                     | 1.46 sec                                                              | 1.47 sec: 1.01x slower                                                |
| coverage                | 45.9 ms                                                               | 46.2 ms: 1.01x slower                                                 |
| genshi_xml              | 40.0 ms                                                               | 40.3 ms: 1.01x slower                                                 |
| 2to3                    | 171 ms                                                                | 172 ms: 1.01x slower                                                  |
| create_gc_cycles        | 905 us                                                                | 913 us: 1.01x slower                                                  |
| fannkuch                | 245 ms                                                                | 248 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl         | 1.29 sec                                                              | 1.30 sec: 1.01x slower                                                |
| django_template         | 21.8 ms                                                               | 22.2 ms: 1.02x slower                                                 |
| tomli_loads             | 1.24 sec                                                              | 1.28 sec: 1.03x slower                                                |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (62): asyncio_tcp, xml_etree_iterparse, unpickle_pure_python, async_tree_none, pycparser, pprint_safe_repr, gc_traversal, python_startup_no_site, coroutines, docutils, go, richards, telco, sympy_sum, deltablue, sympy_expand, logging_format, deepcopy, bpe_tokeniser, async_tree_memoization, xml_etree_process, logging_simple, pidigits, json_loads, crypto_pyaes, pylint, dask, async_tree_cpu_io_mixed, async_tree_eager_io, logging_silent, hexiom, pyflate, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, scimark_lu, async_tree_eager_io_tg, regex_v8, sqlglot_parse, async_tree_eager_memoization_tg, html5lib, bench_thread_pool, richards_super, bench_mp_pool, async_tree_io_tg, generators, pprint_pformat, async_tree_cpu_io_mixed_tg, xml_etree_generate, deepcopy_memo, async_tree_memoization_tg, async_tree_io, async_tree_eager_cpu_io_mixed, genshi_text, tornado_http, nbody, sqlglot_transpile, pathlib, json, xml_etree_parse, async_tree_none_tg, typing_runtime_protocols, async_tree_eager_memoization

# HPT report

- Reliability score: 81.37% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x