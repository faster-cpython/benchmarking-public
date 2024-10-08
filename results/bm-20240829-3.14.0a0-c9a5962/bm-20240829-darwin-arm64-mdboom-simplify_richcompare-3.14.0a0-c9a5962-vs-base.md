# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: darwin-arm64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.00x faster
- HPT reliability: 60.66%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                                | 162 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager    | 61.5 ms                                                               | 60.3 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl     | 1.28 sec                                                              | 1.27 sec: 1.01x faster                                                |
| async_tree_eager_tg | 42.3 ms                                                               | 41.9 ms: 1.01x faster                                                 |
| async_generators    | 281 ms                                                                | 281 ms: 1.00x faster                                                  |
| coroutines          | 16.1 ms                                                               | 16.8 ms: 1.04x slower                                                 |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (16): async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_tcp, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_io, asyncio_websockets, async_tree_memoization, async_tree_eager_io, async_tree_eager_io_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 16.6 ms                                                               | 16.5 ms: 1.01x faster                                                 |
| regex_effbot   | 2.48 ms                                                               | 2.47 ms: 1.00x faster                                                 |
| regex_compile  | 67.1 ms                                                               | 67.8 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 143 us                                                                | 142 us: 1.01x faster                                                  |
| tomli_loads          | 1.48 sec                                                              | 1.47 sec: 1.01x faster                                                |
| xml_etree_process    | 37.7 ms                                                               | 37.8 ms: 1.00x slower                                                 |
| json_dumps           | 6.40 ms                                                               | 6.43 ms: 1.00x slower                                                 |
| pickle_pure_python   | 182 us                                                                | 183 us: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, xml_etree_generate, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.10 ms                                                               | 6.94 ms: 1.02x faster                                                 |
| django_template | 19.8 ms                                                               | 19.6 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark            | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako                 | 7.10 ms                                                               | 6.94 ms: 1.02x faster                                                 |
| async_tree_eager     | 61.5 ms                                                               | 60.3 ms: 1.02x faster                                                 |
| richards_super       | 35.8 ms                                                               | 35.1 ms: 1.02x faster                                                 |
| scimark_lu           | 67.9 ms                                                               | 66.7 ms: 1.02x faster                                                 |
| thrift               | 429 us                                                                | 422 us: 1.02x faster                                                  |
| asyncio_tcp_ssl      | 1.28 sec                                                              | 1.27 sec: 1.01x faster                                                |
| django_template      | 19.8 ms                                                               | 19.6 ms: 1.01x faster                                                 |
| async_tree_eager_tg  | 42.3 ms                                                               | 41.9 ms: 1.01x faster                                                 |
| richards             | 31.6 ms                                                               | 31.4 ms: 1.01x faster                                                 |
| unpickle_pure_python | 143 us                                                                | 142 us: 1.01x faster                                                  |
| regex_v8             | 16.6 ms                                                               | 16.5 ms: 1.01x faster                                                 |
| tomli_loads          | 1.48 sec                                                              | 1.47 sec: 1.01x faster                                                |
| pprint_pformat       | 925 ms                                                                | 922 ms: 1.00x faster                                                  |
| comprehensions       | 10.0 us                                                               | 9.96 us: 1.00x faster                                                 |
| deepcopy_memo        | 16.6 us                                                               | 16.5 us: 1.00x faster                                                 |
| crypto_pyaes         | 50.8 ms                                                               | 50.6 ms: 1.00x faster                                                 |
| async_generators     | 281 ms                                                                | 281 ms: 1.00x faster                                                  |
| regex_effbot         | 2.48 ms                                                               | 2.47 ms: 1.00x faster                                                 |
| telco                | 4.85 ms                                                               | 4.84 ms: 1.00x faster                                                 |
| pprint_safe_repr     | 451 ms                                                                | 450 ms: 1.00x faster                                                  |
| sqlglot_normalize    | 167 ms                                                                | 167 ms: 1.00x slower                                                  |
| sqlglot_optimize     | 31.1 ms                                                               | 31.2 ms: 1.00x slower                                                 |
| xml_etree_process    | 37.7 ms                                                               | 37.8 ms: 1.00x slower                                                 |
| hexiom               | 4.05 ms                                                               | 4.07 ms: 1.00x slower                                                 |
| scimark_monte_carlo  | 43.1 ms                                                               | 43.2 ms: 1.00x slower                                                 |
| scimark_fft          | 184 ms                                                                | 185 ms: 1.00x slower                                                  |
| json_dumps           | 6.40 ms                                                               | 6.43 ms: 1.00x slower                                                 |
| create_gc_cycles     | 900 us                                                                | 905 us: 1.01x slower                                                  |
| sqlglot_transpile    | 897 us                                                                | 902 us: 1.01x slower                                                  |
| pickle_pure_python   | 182 us                                                                | 183 us: 1.01x slower                                                  |
| spectral_norm        | 67.1 ms                                                               | 67.5 ms: 1.01x slower                                                 |
| 2to3                 | 161 ms                                                                | 162 ms: 1.01x slower                                                  |
| nqueens              | 53.2 ms                                                               | 53.6 ms: 1.01x slower                                                 |
| sympy_sum            | 68.6 ms                                                               | 69.1 ms: 1.01x slower                                                 |
| meteor_contest       | 71.9 ms                                                               | 72.4 ms: 1.01x slower                                                 |
| regex_compile        | 67.1 ms                                                               | 67.8 ms: 1.01x slower                                                 |
| coverage             | 44.5 ms                                                               | 45.0 ms: 1.01x slower                                                 |
| pathlib              | 23.5 ms                                                               | 24.0 ms: 1.02x slower                                                 |
| coroutines           | 16.1 ms                                                               | 16.8 ms: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (59): tornado_http, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_tcp, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, mdp, xml_etree_parse, pylint, deepcopy_reduce, async_tree_eager_memoization, json, go, bench_thread_pool, raytrace, async_tree_eager_memoization_tg, scimark_sor, python_startup, xml_etree_iterparse, docutils, regex_dna, sympy_str, deepcopy, logging_simple, deltablue, pidigits, chaos, sympy_integrate, sympy_expand, python_startup_no_site, dulwich_log, gc_traversal, bench_mp_pool, pyflate, async_tree_io, bpe_tokeniser, pycparser, nbody, logging_silent, generators, fannkuch, sqlglot_parse, genshi_text, asyncio_websockets, html5lib, async_tree_memoization, xml_etree_generate, genshi_xml, float, logging_format, typing_runtime_protocols, json_loads, scimark_sparse_mat_mult, async_tree_eager_io, async_tree_eager_io_tg, async_tree_io_tg

# HPT report

- Reliability score: 60.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x