# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: darwin-arm64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.00x slower
- HPT reliability: 92.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines       | 16.2 ms                                                               | 16.1 ms: 1.00x faster                                                 |
| async_tree_eager | 60.7 ms                                                               | 60.5 ms: 1.00x faster                                                 |
| async_tree_io    | 594 ms                                                                | 596 ms: 1.00x slower                                                  |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (18): async_tree_none, async_tree_memoization_tg, asyncio_tcp, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_generators, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_tg, asyncio_websockets, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization, asyncio_tcp_ssl, async_tree_memoization, async_tree_eager_io, async_tree_eager_io_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                               | 48.7 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.50 ms                                                               | 2.46 ms: 1.02x faster                                                 |
| regex_v8       | 16.6 ms                                                               | 16.6 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 143 us                                                                | 142 us: 1.01x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                               | 53.6 ms: 1.00x slower                                                 |
| xml_etree_process    | 37.5 ms                                                               | 37.7 ms: 1.01x slower                                                 |
| xml_etree_iterparse  | 73.8 ms                                                               | 74.3 ms: 1.01x slower                                                 |
| json_dumps           | 6.38 ms                                                               | 6.43 ms: 1.01x slower                                                 |
| pickle_pure_python   | 182 us                                                                | 183 us: 1.01x slower                                                  |
| json_loads           | 17.1 us                                                               | 17.3 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 16.5 ms                                                               | 16.6 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 19.9 ms                                                               | 19.9 ms: 1.00x slower                                                 |
| mako            | 6.94 ms                                                               | 6.97 ms: 1.00x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators               | 20.8 ms                                                               | 20.4 ms: 1.02x faster                                                 |
| regex_effbot             | 2.50 ms                                                               | 2.46 ms: 1.02x faster                                                 |
| unpickle_pure_python     | 143 us                                                                | 142 us: 1.01x faster                                                  |
| typing_runtime_protocols | 91.3 us                                                               | 90.5 us: 1.01x faster                                                 |
| gc_traversal             | 2.47 ms                                                               | 2.45 ms: 1.01x faster                                                 |
| richards_super           | 35.4 ms                                                               | 35.2 ms: 1.01x faster                                                 |
| coroutines               | 16.2 ms                                                               | 16.1 ms: 1.00x faster                                                 |
| deltablue                | 2.15 ms                                                               | 2.14 ms: 1.00x faster                                                 |
| scimark_sparse_mat_mult  | 2.79 ms                                                               | 2.78 ms: 1.00x faster                                                 |
| async_tree_eager         | 60.7 ms                                                               | 60.5 ms: 1.00x faster                                                 |
| richards                 | 31.5 ms                                                               | 31.4 ms: 1.00x faster                                                 |
| scimark_lu               | 66.6 ms                                                               | 66.5 ms: 1.00x faster                                                 |
| meteor_contest           | 72.2 ms                                                               | 72.1 ms: 1.00x faster                                                 |
| regex_v8                 | 16.6 ms                                                               | 16.6 ms: 1.00x slower                                                 |
| scimark_fft              | 185 ms                                                                | 185 ms: 1.00x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                               | 53.6 ms: 1.00x slower                                                 |
| pprint_pformat           | 928 ms                                                                | 929 ms: 1.00x slower                                                  |
| async_tree_io            | 594 ms                                                                | 596 ms: 1.00x slower                                                  |
| comprehensions           | 9.95 us                                                               | 9.97 us: 1.00x slower                                                 |
| float                    | 48.6 ms                                                               | 48.7 ms: 1.00x slower                                                 |
| deepcopy                 | 144 us                                                                | 144 us: 1.00x slower                                                  |
| raytrace                 | 149 ms                                                                | 149 ms: 1.00x slower                                                  |
| django_template          | 19.9 ms                                                               | 19.9 ms: 1.00x slower                                                 |
| fannkuch                 | 262 ms                                                                | 263 ms: 1.00x slower                                                  |
| dulwich_log              | 27.0 ms                                                               | 27.1 ms: 1.00x slower                                                 |
| logging_silent           | 60.9 ns                                                               | 61.1 ns: 1.00x slower                                                 |
| mdp                      | 1.43 sec                                                              | 1.43 sec: 1.00x slower                                                |
| logging_format           | 3.39 us                                                               | 3.40 us: 1.00x slower                                                 |
| nqueens                  | 53.1 ms                                                               | 53.3 ms: 1.00x slower                                                 |
| spectral_norm            | 67.0 ms                                                               | 67.3 ms: 1.00x slower                                                 |
| mako                     | 6.94 ms                                                               | 6.97 ms: 1.00x slower                                                 |
| sqlglot_parse            | 738 us                                                                | 741 us: 1.00x slower                                                  |
| bench_thread_pool        | 450 us                                                                | 452 us: 1.00x slower                                                  |
| sympy_sum                | 68.7 ms                                                               | 69.0 ms: 1.00x slower                                                 |
| pprint_safe_repr         | 453 ms                                                                | 455 ms: 1.00x slower                                                  |
| bpe_tokeniser            | 3.13 sec                                                              | 3.14 sec: 1.00x slower                                                |
| sympy_str                | 131 ms                                                                | 132 ms: 1.01x slower                                                  |
| telco                    | 4.82 ms                                                               | 4.85 ms: 1.01x slower                                                 |
| xml_etree_process        | 37.5 ms                                                               | 37.7 ms: 1.01x slower                                                 |
| thrift                   | 422 us                                                                | 425 us: 1.01x slower                                                  |
| xml_etree_iterparse      | 73.8 ms                                                               | 74.3 ms: 1.01x slower                                                 |
| deepcopy_memo            | 16.5 us                                                               | 16.6 us: 1.01x slower                                                 |
| python_startup           | 16.5 ms                                                               | 16.6 ms: 1.01x slower                                                 |
| json_dumps               | 6.38 ms                                                               | 6.43 ms: 1.01x slower                                                 |
| pickle_pure_python       | 182 us                                                                | 183 us: 1.01x slower                                                  |
| sympy_expand             | 226 ms                                                                | 228 ms: 1.01x slower                                                  |
| crypto_pyaes             | 50.6 ms                                                               | 51.3 ms: 1.01x slower                                                 |
| json_loads               | 17.1 us                                                               | 17.3 us: 1.01x slower                                                 |
| pathlib                  | 23.5 ms                                                               | 23.9 ms: 1.02x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (49): tornado_http, async_tree_none, async_tree_memoization_tg, asyncio_tcp, async_tree_none_tg, xml_etree_parse, python_startup_no_site, async_tree_cpu_io_mixed_tg, bench_mp_pool, chaos, async_tree_eager_memoization_tg, async_generators, async_tree_eager_cpu_io_mixed_tg, pycparser, sqlglot_normalize, async_tree_cpu_io_mixed, genshi_text, async_tree_eager_tg, sympy_integrate, sqlglot_optimize, json, regex_dna, logging_simple, go, scimark_sor, hexiom, html5lib, nbody, regex_compile, asyncio_websockets, deepcopy_reduce, async_tree_eager_cpu_io_mixed, scimark_monte_carlo, docutils, async_tree_eager_memoization, pidigits, create_gc_cycles, tomli_loads, genshi_xml, 2to3, pyflate, coverage, pylint, asyncio_tcp_ssl, async_tree_memoization, async_tree_eager_io, sqlglot_transpile, async_tree_eager_io_tg, async_tree_io_tg

# HPT report

- Reliability score: 92.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x