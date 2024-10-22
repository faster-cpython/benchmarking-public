# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: darwin-arm64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.00x slower
- HPT reliability: 52.79%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 160 ms                                                                | 162 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager                 | 60.7 ms                                                               | 60.3 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl                  | 1.28 sec                                                              | 1.27 sec: 1.01x faster                                                |
| async_generators                 | 282 ms                                                                | 281 ms: 1.00x faster                                                  |
| async_tree_eager_tg              | 42.1 ms                                                               | 41.9 ms: 1.00x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 337 ms                                                                | 336 ms: 1.00x faster                                                  |
| async_tree_io                    | 594 ms                                                                | 595 ms: 1.00x slower                                                  |
| coroutines                       | 16.2 ms                                                               | 16.8 ms: 1.04x slower                                                 |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (14): asyncio_tcp, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed, async_tree_eager_io_tg, asyncio_websockets, async_tree_memoization, async_tree_eager_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                                | 281 ms: 1.00x faster                                                  |
| float          | 48.6 ms                                                               | 48.7 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.50 ms                                                               | 2.47 ms: 1.01x faster                                                 |
| regex_v8       | 16.6 ms                                                               | 16.5 ms: 1.00x faster                                                 |
| regex_compile  | 67.6 ms                                                               | 67.8 ms: 1.00x slower                                                 |
| regex_dna      | 146 ms                                                                | 147 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads        | 1.48 sec                                                              | 1.47 sec: 1.01x faster                                                |
| json_dumps         | 6.38 ms                                                               | 6.43 ms: 1.01x slower                                                 |
| xml_etree_process  | 37.5 ms                                                               | 37.8 ms: 1.01x slower                                                 |
| pickle_pure_python | 182 us                                                                | 183 us: 1.01x slower                                                  |
| json_loads         | 17.1 us                                                               | 17.3 us: 1.01x slower                                                 |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_parse, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.6 ms                                                               | 13.7 ms: 1.00x slower                                                 |
| python_startup         | 16.5 ms                                                               | 16.6 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 19.9 ms                                                               | 19.6 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (3): mako, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators                       | 20.8 ms                                                               | 20.4 ms: 1.02x faster                                                 |
| django_template                  | 19.9 ms                                                               | 19.6 ms: 1.01x faster                                                 |
| regex_effbot                     | 2.50 ms                                                               | 2.47 ms: 1.01x faster                                                 |
| tomli_loads                      | 1.48 sec                                                              | 1.47 sec: 1.01x faster                                                |
| pprint_safe_repr                 | 453 ms                                                                | 450 ms: 1.01x faster                                                  |
| richards_super                   | 35.4 ms                                                               | 35.1 ms: 1.01x faster                                                 |
| pprint_pformat                   | 928 ms                                                                | 922 ms: 1.01x faster                                                  |
| async_tree_eager                 | 60.7 ms                                                               | 60.3 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl                  | 1.28 sec                                                              | 1.27 sec: 1.01x faster                                                |
| regex_v8                         | 16.6 ms                                                               | 16.5 ms: 1.00x faster                                                 |
| async_generators                 | 282 ms                                                                | 281 ms: 1.00x faster                                                  |
| async_tree_eager_tg              | 42.1 ms                                                               | 41.9 ms: 1.00x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 337 ms                                                                | 336 ms: 1.00x faster                                                  |
| richards                         | 31.5 ms                                                               | 31.4 ms: 1.00x faster                                                 |
| deltablue                        | 2.15 ms                                                               | 2.15 ms: 1.00x faster                                                 |
| raytrace                         | 149 ms                                                                | 149 ms: 1.00x faster                                                  |
| pidigits                         | 282 ms                                                                | 281 ms: 1.00x faster                                                  |
| async_tree_io                    | 594 ms                                                                | 595 ms: 1.00x slower                                                  |
| pyflate                          | 320 ms                                                                | 321 ms: 1.00x slower                                                  |
| comprehensions                   | 9.95 us                                                               | 9.96 us: 1.00x slower                                                 |
| scimark_fft                      | 185 ms                                                                | 185 ms: 1.00x slower                                                  |
| deepcopy                         | 144 us                                                                | 144 us: 1.00x slower                                                  |
| scimark_monte_carlo              | 43.1 ms                                                               | 43.2 ms: 1.00x slower                                                 |
| fannkuch                         | 262 ms                                                                | 263 ms: 1.00x slower                                                  |
| regex_compile                    | 67.6 ms                                                               | 67.8 ms: 1.00x slower                                                 |
| logging_simple                   | 3.08 us                                                               | 3.09 us: 1.00x slower                                                 |
| meteor_contest                   | 72.2 ms                                                               | 72.4 ms: 1.00x slower                                                 |
| telco                            | 4.82 ms                                                               | 4.84 ms: 1.00x slower                                                 |
| float                            | 48.6 ms                                                               | 48.7 ms: 1.00x slower                                                 |
| sympy_str                        | 131 ms                                                                | 131 ms: 1.00x slower                                                  |
| bpe_tokeniser                    | 3.13 sec                                                              | 3.14 sec: 1.00x slower                                                |
| sympy_expand                     | 226 ms                                                                | 227 ms: 1.00x slower                                                  |
| python_startup_no_site           | 13.6 ms                                                               | 13.7 ms: 1.00x slower                                                 |
| sqlglot_parse                    | 738 us                                                                | 741 us: 1.00x slower                                                  |
| python_startup                   | 16.5 ms                                                               | 16.6 ms: 1.00x slower                                                 |
| sympy_sum                        | 68.7 ms                                                               | 69.1 ms: 1.01x slower                                                 |
| regex_dna                        | 146 ms                                                                | 147 ms: 1.01x slower                                                  |
| sqlglot_transpile                | 897 us                                                                | 902 us: 1.01x slower                                                  |
| logging_silent                   | 60.9 ns                                                               | 61.3 ns: 1.01x slower                                                 |
| logging_format                   | 3.39 us                                                               | 3.41 us: 1.01x slower                                                 |
| create_gc_cycles                 | 898 us                                                                | 905 us: 1.01x slower                                                  |
| spectral_norm                    | 67.0 ms                                                               | 67.5 ms: 1.01x slower                                                 |
| json_dumps                       | 6.38 ms                                                               | 6.43 ms: 1.01x slower                                                 |
| xml_etree_process                | 37.5 ms                                                               | 37.8 ms: 1.01x slower                                                 |
| nqueens                          | 53.1 ms                                                               | 53.6 ms: 1.01x slower                                                 |
| pickle_pure_python               | 182 us                                                                | 183 us: 1.01x slower                                                  |
| json_loads                       | 17.1 us                                                               | 17.3 us: 1.01x slower                                                 |
| 2to3                             | 160 ms                                                                | 162 ms: 1.01x slower                                                  |
| coverage                         | 44.4 ms                                                               | 45.0 ms: 1.01x slower                                                 |
| pathlib                          | 23.5 ms                                                               | 24.0 ms: 1.02x slower                                                 |
| coroutines                       | 16.2 ms                                                               | 16.8 ms: 1.04x slower                                                 |
| Geometric mean                   | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (47): asyncio_tcp, async_tree_none, unpickle_pure_python, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, xml_etree_parse, async_tree_eager_memoization_tg, gc_traversal, docutils, async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed, async_tree_eager_io_tg, xml_etree_generate, json, thrift, sqlglot_normalize, tornado_http, mako, deepcopy_reduce, chaos, dulwich_log, bench_mp_pool, crypto_pyaes, hexiom, pycparser, scimark_sor, genshi_xml, bench_thread_pool, go, scimark_sparse_mat_mult, mdp, sympy_integrate, sqlglot_optimize, asyncio_websockets, deepcopy_memo, genshi_text, nbody, scimark_lu, html5lib, async_tree_memoization, async_tree_eager_io, typing_runtime_protocols, xml_etree_iterparse, pylint, async_tree_io_tg

# HPT report

- Reliability score: 52.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x