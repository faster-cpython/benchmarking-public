# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: darwin-arm64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.00x faster
- HPT reliability: 64.53%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager                 | 61.5 ms                                                               | 60.2 ms: 1.02x faster                                                 |
| async_tree_eager_tg              | 42.3 ms                                                               | 41.5 ms: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 337 ms                                                                | 336 ms: 1.00x faster                                                  |
| async_tree_io                    | 595 ms                                                                | 597 ms: 1.00x slower                                                  |
| async_generators                 | 281 ms                                                                | 284 ms: 1.01x slower                                                  |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (16): async_tree_none, asyncio_tcp_ssl, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization, asyncio_tcp, async_tree_cpu_io_mixed_tg, coroutines, async_tree_eager_memoization_tg, asyncio_websockets, async_tree_memoization, async_tree_eager_io_tg, async_tree_eager_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 59.5 ms                                                               | 59.3 ms: 1.00x faster                                                 |
| float          | 48.6 ms                                                               | 48.9 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.48 ms                                                               | 2.46 ms: 1.01x faster                                                 |
| regex_dna      | 147 ms                                                                | 146 ms: 1.01x faster                                                  |
| regex_compile  | 67.1 ms                                                               | 67.4 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse    | 110 ms                                                                | 108 ms: 1.01x faster                                                  |
| pickle_pure_python | 182 us                                                                | 183 us: 1.00x slower                                                  |
| json_dumps         | 6.40 ms                                                               | 6.44 ms: 1.01x slower                                                 |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (6): xml_etree_iterparse, unpickle_pure_python, xml_etree_process, xml_etree_generate, json_loads, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 16.6 ms                                                               | 16.5 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                               | 13.8 ms: 1.00x faster                                                 |
| mako            | 7.10 ms                                                               | 7.08 ms: 1.00x faster                                                 |
| django_template | 19.8 ms                                                               | 19.9 ms: 1.00x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20240829-darwin-arm64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager                 | 61.5 ms                                                               | 60.2 ms: 1.02x faster                                                 |
| async_tree_eager_tg              | 42.3 ms                                                               | 41.5 ms: 1.02x faster                                                 |
| scimark_lu                       | 67.9 ms                                                               | 66.7 ms: 1.02x faster                                                 |
| xml_etree_parse                  | 110 ms                                                                | 108 ms: 1.01x faster                                                  |
| richards_super                   | 35.8 ms                                                               | 35.3 ms: 1.01x faster                                                 |
| regex_effbot                     | 2.48 ms                                                               | 2.46 ms: 1.01x faster                                                 |
| crypto_pyaes                     | 50.8 ms                                                               | 50.4 ms: 1.01x faster                                                 |
| sympy_integrate                  | 10.3 ms                                                               | 10.3 ms: 1.01x faster                                                 |
| json                             | 2.96 ms                                                               | 2.95 ms: 1.01x faster                                                 |
| comprehensions                   | 10.0 us                                                               | 9.95 us: 1.01x faster                                                 |
| regex_dna                        | 147 ms                                                                | 146 ms: 1.01x faster                                                  |
| thrift                           | 429 us                                                                | 427 us: 1.01x faster                                                  |
| python_startup                   | 16.6 ms                                                               | 16.5 ms: 1.01x faster                                                 |
| richards                         | 31.6 ms                                                               | 31.5 ms: 1.00x faster                                                 |
| genshi_text                      | 13.9 ms                                                               | 13.8 ms: 1.00x faster                                                 |
| bench_thread_pool                | 451 us                                                                | 450 us: 1.00x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 337 ms                                                                | 336 ms: 1.00x faster                                                  |
| logging_format                   | 3.40 us                                                               | 3.39 us: 1.00x faster                                                 |
| nbody                            | 59.5 ms                                                               | 59.3 ms: 1.00x faster                                                 |
| telco                            | 4.85 ms                                                               | 4.84 ms: 1.00x faster                                                 |
| deepcopy_memo                    | 16.6 us                                                               | 16.5 us: 1.00x faster                                                 |
| mako                             | 7.10 ms                                                               | 7.08 ms: 1.00x faster                                                 |
| logging_simple                   | 3.09 us                                                               | 3.08 us: 1.00x faster                                                 |
| chaos                            | 35.7 ms                                                               | 35.6 ms: 1.00x faster                                                 |
| logging_silent                   | 61.2 ns                                                               | 61.2 ns: 1.00x faster                                                 |
| generators                       | 20.4 ms                                                               | 20.4 ms: 1.00x slower                                                 |
| hexiom                           | 4.05 ms                                                               | 4.06 ms: 1.00x slower                                                 |
| sqlglot_normalize                | 167 ms                                                                | 167 ms: 1.00x slower                                                  |
| nqueens                          | 53.2 ms                                                               | 53.3 ms: 1.00x slower                                                 |
| fannkuch                         | 263 ms                                                                | 263 ms: 1.00x slower                                                  |
| sqlglot_optimize                 | 31.1 ms                                                               | 31.1 ms: 1.00x slower                                                 |
| scimark_monte_carlo              | 43.1 ms                                                               | 43.2 ms: 1.00x slower                                                 |
| pprint_pformat                   | 925 ms                                                                | 928 ms: 1.00x slower                                                  |
| meteor_contest                   | 71.9 ms                                                               | 72.1 ms: 1.00x slower                                                 |
| django_template                  | 19.8 ms                                                               | 19.9 ms: 1.00x slower                                                 |
| spectral_norm                    | 67.1 ms                                                               | 67.3 ms: 1.00x slower                                                 |
| async_tree_io                    | 595 ms                                                                | 597 ms: 1.00x slower                                                  |
| pickle_pure_python               | 182 us                                                                | 183 us: 1.00x slower                                                  |
| sqlglot_transpile                | 897 us                                                                | 901 us: 1.00x slower                                                  |
| sympy_expand                     | 227 ms                                                                | 228 ms: 1.00x slower                                                  |
| regex_compile                    | 67.1 ms                                                               | 67.4 ms: 1.00x slower                                                 |
| json_dumps                       | 6.40 ms                                                               | 6.44 ms: 1.01x slower                                                 |
| sympy_sum                        | 68.6 ms                                                               | 69.0 ms: 1.01x slower                                                 |
| float                            | 48.6 ms                                                               | 48.9 ms: 1.01x slower                                                 |
| pprint_safe_repr                 | 451 ms                                                                | 455 ms: 1.01x slower                                                  |
| async_generators                 | 281 ms                                                                | 284 ms: 1.01x slower                                                  |
| pathlib                          | 23.5 ms                                                               | 23.8 ms: 1.01x slower                                                 |
| coverage                         | 44.5 ms                                                               | 45.4 ms: 1.02x slower                                                 |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (50): tornado_http, pylint, async_tree_none, asyncio_tcp_ssl, async_tree_memoization_tg, xml_etree_iterparse, async_tree_eager_cpu_io_mixed, async_tree_none_tg, 2to3, async_tree_cpu_io_mixed, mdp, bench_mp_pool, scimark_sor, async_tree_eager_memoization, asyncio_tcp, async_tree_cpu_io_mixed_tg, typing_runtime_protocols, go, regex_v8, bpe_tokeniser, pyflate, coroutines, unpickle_pure_python, xml_etree_process, deepcopy, scimark_fft, gc_traversal, xml_etree_generate, async_tree_eager_memoization_tg, docutils, sqlglot_parse, deltablue, asyncio_websockets, pidigits, create_gc_cycles, async_tree_memoization, pycparser, json_loads, scimark_sparse_mat_mult, async_tree_eager_io_tg, raytrace, sympy_str, deepcopy_reduce, genshi_xml, dulwich_log, tomli_loads, async_tree_eager_io, html5lib, python_startup_no_site, async_tree_io_tg

# HPT report

- Reliability score: 64.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x