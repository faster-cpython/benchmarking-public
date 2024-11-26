# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: darwin-arm64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.001x slower
- HPT reliability: 53.10%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 160 ms                                                                | 161 ms: 1.00x slower                                                  |
| html5lib       | 30.0 ms                                                               | 30.2 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_tg              | 42.1 ms                                                               | 41.5 ms: 1.01x faster                                                 |
| async_tree_eager                 | 60.7 ms                                                               | 60.2 ms: 1.01x faster                                                 |
| coroutines                       | 16.2 ms                                                               | 16.1 ms: 1.00x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 337 ms                                                                | 336 ms: 1.00x faster                                                  |
| async_tree_io                    | 594 ms                                                                | 597 ms: 1.00x slower                                                  |
| async_generators                 | 282 ms                                                                | 284 ms: 1.01x slower                                                  |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (15): asyncio_tcp, async_tree_none, async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed, async_tree_none_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, asyncio_tcp_ssl, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_memoization, async_tree_eager_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 59.4 ms                                                               | 59.3 ms: 1.00x faster                                                 |
| float          | 48.6 ms                                                               | 48.9 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.50 ms                                                               | 2.46 ms: 1.01x faster                                                 |
| regex_v8       | 16.6 ms                                                               | 16.6 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse    | 110 ms                                                                | 108 ms: 1.01x faster                                                  |
| xml_etree_generate | 53.5 ms                                                               | 53.3 ms: 1.00x faster                                                 |
| xml_etree_process  | 37.5 ms                                                               | 37.6 ms: 1.00x slower                                                 |
| pickle_pure_python | 182 us                                                                | 183 us: 1.01x slower                                                  |
| json_dumps         | 6.38 ms                                                               | 6.44 ms: 1.01x slower                                                 |
| json_loads         | 17.1 us                                                               | 17.3 us: 1.01x slower                                                 |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (3): unpickle_pure_python, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text    | 13.9 ms                                                               | 13.8 ms: 1.00x faster                                                 |
| mako           | 6.94 ms                                                               | 7.08 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                        | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators                       | 20.8 ms                                                               | 20.4 ms: 1.02x faster                                                 |
| xml_etree_parse                  | 110 ms                                                                | 108 ms: 1.01x faster                                                  |
| regex_effbot                     | 2.50 ms                                                               | 2.46 ms: 1.01x faster                                                 |
| async_tree_eager_tg              | 42.1 ms                                                               | 41.5 ms: 1.01x faster                                                 |
| async_tree_eager                 | 60.7 ms                                                               | 60.2 ms: 1.01x faster                                                 |
| json                             | 2.96 ms                                                               | 2.95 ms: 1.01x faster                                                 |
| sympy_integrate                  | 10.3 ms                                                               | 10.3 ms: 1.00x faster                                                 |
| coroutines                       | 16.2 ms                                                               | 16.1 ms: 1.00x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 337 ms                                                                | 336 ms: 1.00x faster                                                  |
| genshi_text                      | 13.9 ms                                                               | 13.8 ms: 1.00x faster                                                 |
| xml_etree_generate               | 53.5 ms                                                               | 53.3 ms: 1.00x faster                                                 |
| crypto_pyaes                     | 50.6 ms                                                               | 50.4 ms: 1.00x faster                                                 |
| scimark_fft                      | 185 ms                                                                | 184 ms: 1.00x faster                                                  |
| hexiom                           | 4.07 ms                                                               | 4.06 ms: 1.00x faster                                                 |
| nbody                            | 59.4 ms                                                               | 59.3 ms: 1.00x faster                                                 |
| meteor_contest                   | 72.2 ms                                                               | 72.1 ms: 1.00x faster                                                 |
| regex_v8                         | 16.6 ms                                                               | 16.6 ms: 1.00x faster                                                 |
| scimark_monte_carlo              | 43.1 ms                                                               | 43.2 ms: 1.00x slower                                                 |
| bpe_tokeniser                    | 3.13 sec                                                              | 3.13 sec: 1.00x slower                                                |
| deepcopy_memo                    | 16.5 us                                                               | 16.5 us: 1.00x slower                                                 |
| create_gc_cycles                 | 898 us                                                                | 901 us: 1.00x slower                                                  |
| deepcopy                         | 144 us                                                                | 144 us: 1.00x slower                                                  |
| sqlglot_parse                    | 738 us                                                                | 740 us: 1.00x slower                                                  |
| telco                            | 4.82 ms                                                               | 4.84 ms: 1.00x slower                                                 |
| pprint_safe_repr                 | 453 ms                                                                | 455 ms: 1.00x slower                                                  |
| fannkuch                         | 262 ms                                                                | 263 ms: 1.00x slower                                                  |
| nqueens                          | 53.1 ms                                                               | 53.3 ms: 1.00x slower                                                 |
| sympy_sum                        | 68.7 ms                                                               | 69.0 ms: 1.00x slower                                                 |
| deepcopy_reduce                  | 1.50 us                                                               | 1.51 us: 1.00x slower                                                 |
| sqlglot_transpile                | 897 us                                                                | 901 us: 1.00x slower                                                  |
| async_tree_io                    | 594 ms                                                                | 597 ms: 1.00x slower                                                  |
| spectral_norm                    | 67.0 ms                                                               | 67.3 ms: 1.00x slower                                                 |
| xml_etree_process                | 37.5 ms                                                               | 37.6 ms: 1.00x slower                                                 |
| logging_silent                   | 60.9 ns                                                               | 61.2 ns: 1.00x slower                                                 |
| 2to3                             | 160 ms                                                                | 161 ms: 1.00x slower                                                  |
| sympy_str                        | 131 ms                                                                | 132 ms: 1.01x slower                                                  |
| html5lib                         | 30.0 ms                                                               | 30.2 ms: 1.01x slower                                                 |
| pickle_pure_python               | 182 us                                                                | 183 us: 1.01x slower                                                  |
| float                            | 48.6 ms                                                               | 48.9 ms: 1.01x slower                                                 |
| async_generators                 | 282 ms                                                                | 284 ms: 1.01x slower                                                  |
| json_dumps                       | 6.38 ms                                                               | 6.44 ms: 1.01x slower                                                 |
| sympy_expand                     | 226 ms                                                                | 228 ms: 1.01x slower                                                  |
| thrift                           | 422 us                                                                | 427 us: 1.01x slower                                                  |
| json_loads                       | 17.1 us                                                               | 17.3 us: 1.01x slower                                                 |
| pathlib                          | 23.5 ms                                                               | 23.8 ms: 1.01x slower                                                 |
| mako                             | 6.94 ms                                                               | 7.08 ms: 1.02x slower                                                 |
| coverage                         | 44.4 ms                                                               | 45.4 ms: 1.02x slower                                                 |
| Geometric mean                   | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (51): asyncio_tcp, async_tree_none, async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed, gc_traversal, bench_mp_pool, regex_compile, deltablue, richards_super, async_tree_none_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, docutils, chaos, bench_thread_pool, scimark_sparse_mat_mult, async_tree_eager_memoization_tg, unpickle_pure_python, richards, xml_etree_iterparse, typing_runtime_protocols, asyncio_tcp_ssl, sqlglot_normalize, async_tree_cpu_io_mixed, scimark_sor, pyflate, sqlglot_optimize, pylint, comprehensions, asyncio_websockets, pprint_pformat, tomli_loads, python_startup, pidigits, pycparser, regex_dna, genshi_xml, go, raytrace, django_template, logging_format, mdp, logging_simple, async_tree_memoization, scimark_lu, dulwich_log, tornado_http, async_tree_eager_io, python_startup_no_site, async_tree_io_tg

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 53.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x