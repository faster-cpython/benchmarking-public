# Results vs. base

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: darwin-arm64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 190 ms                                                                | 163 ms: 1.16x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                                    |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg              | 543 ms                                                                | 507 ms: 1.07x faster                                                            |
| coroutines                    | 16.3 ms                                                               | 16.1 ms: 1.01x faster                                                           |
| async_generators              | 282 ms                                                                | 279 ms: 1.01x faster                                                            |
| async_tree_eager_cpu_io_mixed | 365 ms                                                                | 362 ms: 1.01x faster                                                            |
| async_tree_eager              | 63.0 ms                                                               | 62.8 ms: 1.00x faster                                                           |
| Geometric mean                | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (16): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_eager_io, async_tree_memoization, async_tree_eager_memoization_tg, async_tree_none, async_tree_eager_memoization, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_eager_tg, async_tree_none_tg, asyncio_tcp_ssl, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 48.8 ms                                                               | 48.4 ms: 1.01x faster                                                           |
| nbody          | 59.5 ms                                                               | 59.4 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 69.2 ms                                                               | 68.5 ms: 1.01x faster                                                           |
| regex_v8       | 16.6 ms                                                               | 16.6 ms: 1.00x faster                                                           |
| regex_dna      | 145 ms                                                                | 146 ms: 1.01x slower                                                            |
| regex_effbot   | 2.47 ms                                                               | 2.50 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 110 ms                                                                | 109 ms: 1.01x faster                                                            |
| pickle_pure_python   | 187 us                                                                | 184 us: 1.01x faster                                                            |
| unpickle_pure_python | 145 us                                                                | 144 us: 1.01x faster                                                            |
| xml_etree_generate   | 54.0 ms                                                               | 53.4 ms: 1.01x faster                                                           |
| xml_etree_process    | 38.6 ms                                                               | 38.3 ms: 1.01x faster                                                           |
| xml_etree_iterparse  | 74.8 ms                                                               | 74.3 ms: 1.01x faster                                                           |
| json_loads           | 17.2 us                                                               | 17.3 us: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): json_dumps, tomli_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 20.2 ms                                                               | 19.8 ms: 1.02x faster                                                           |
| mako            | 7.20 ms                                                               | 7.16 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                     | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3                          | 190 ms                                                                | 163 ms: 1.16x faster                                                            |
| async_tree_io_tg              | 543 ms                                                                | 507 ms: 1.07x faster                                                            |
| logging_silent                | 62.0 ns                                                               | 60.4 ns: 1.03x faster                                                           |
| spectral_norm                 | 68.1 ms                                                               | 66.5 ms: 1.02x faster                                                           |
| hexiom                        | 4.14 ms                                                               | 4.06 ms: 1.02x faster                                                           |
| deepcopy_memo                 | 17.4 us                                                               | 17.1 us: 1.02x faster                                                           |
| django_template               | 20.2 ms                                                               | 19.8 ms: 1.02x faster                                                           |
| deltablue                     | 2.15 ms                                                               | 2.12 ms: 1.02x faster                                                           |
| xml_etree_parse               | 110 ms                                                                | 109 ms: 1.01x faster                                                            |
| logging_simple                | 3.10 us                                                               | 3.06 us: 1.01x faster                                                           |
| deepcopy                      | 148 us                                                                | 146 us: 1.01x faster                                                            |
| coroutines                    | 16.3 ms                                                               | 16.1 ms: 1.01x faster                                                           |
| sqlglot_optimize              | 32.2 ms                                                               | 31.8 ms: 1.01x faster                                                           |
| pickle_pure_python            | 187 us                                                                | 184 us: 1.01x faster                                                            |
| pprint_safe_repr              | 481 ms                                                                | 475 ms: 1.01x faster                                                            |
| unpickle_pure_python          | 145 us                                                                | 144 us: 1.01x faster                                                            |
| create_gc_cycles              | 896 us                                                                | 886 us: 1.01x faster                                                            |
| sympy_integrate               | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                           |
| pathlib                       | 23.6 ms                                                               | 23.3 ms: 1.01x faster                                                           |
| pprint_pformat                | 980 ms                                                                | 969 ms: 1.01x faster                                                            |
| xml_etree_generate            | 54.0 ms                                                               | 53.4 ms: 1.01x faster                                                           |
| gc_traversal                  | 2.48 ms                                                               | 2.45 ms: 1.01x faster                                                           |
| regex_compile                 | 69.2 ms                                                               | 68.5 ms: 1.01x faster                                                           |
| sympy_sum                     | 71.5 ms                                                               | 70.8 ms: 1.01x faster                                                           |
| sympy_expand                  | 233 ms                                                                | 231 ms: 1.01x faster                                                            |
| async_generators              | 282 ms                                                                | 279 ms: 1.01x faster                                                            |
| async_tree_eager_cpu_io_mixed | 365 ms                                                                | 362 ms: 1.01x faster                                                            |
| go                            | 98.1 ms                                                               | 97.2 ms: 1.01x faster                                                           |
| meteor_contest                | 72.4 ms                                                               | 71.8 ms: 1.01x faster                                                           |
| coverage                      | 45.2 ms                                                               | 44.9 ms: 1.01x faster                                                           |
| xml_etree_process             | 38.6 ms                                                               | 38.3 ms: 1.01x faster                                                           |
| bpe_tokeniser                 | 3.13 sec                                                              | 3.11 sec: 1.01x faster                                                          |
| richards_super                | 34.9 ms                                                               | 34.6 ms: 1.01x faster                                                           |
| float                         | 48.8 ms                                                               | 48.4 ms: 1.01x faster                                                           |
| logging_format                | 3.39 us                                                               | 3.37 us: 1.01x faster                                                           |
| xml_etree_iterparse           | 74.8 ms                                                               | 74.3 ms: 1.01x faster                                                           |
| richards                      | 31.7 ms                                                               | 31.4 ms: 1.01x faster                                                           |
| sqlglot_transpile             | 913 us                                                                | 907 us: 1.01x faster                                                            |
| thrift                        | 432 us                                                                | 430 us: 1.01x faster                                                            |
| nqueens                       | 53.4 ms                                                               | 53.1 ms: 1.01x faster                                                           |
| mako                          | 7.20 ms                                                               | 7.16 ms: 1.01x faster                                                           |
| generators                    | 20.7 ms                                                               | 20.6 ms: 1.01x faster                                                           |
| scimark_lu                    | 67.9 ms                                                               | 67.5 ms: 1.01x faster                                                           |
| mdp                           | 1.45 sec                                                              | 1.44 sec: 1.01x faster                                                          |
| sqlglot_normalize             | 173 ms                                                                | 172 ms: 1.00x faster                                                            |
| sympy_str                     | 135 ms                                                                | 135 ms: 1.00x faster                                                            |
| regex_v8                      | 16.6 ms                                                               | 16.6 ms: 1.00x faster                                                           |
| async_tree_eager              | 63.0 ms                                                               | 62.8 ms: 1.00x faster                                                           |
| dulwich_log                   | 27.0 ms                                                               | 26.9 ms: 1.00x faster                                                           |
| nbody                         | 59.5 ms                                                               | 59.4 ms: 1.00x faster                                                           |
| fannkuch                      | 262 ms                                                                | 262 ms: 1.00x slower                                                            |
| regex_dna                     | 145 ms                                                                | 146 ms: 1.01x slower                                                            |
| scimark_sparse_mat_mult       | 2.79 ms                                                               | 2.80 ms: 1.01x slower                                                           |
| json_loads                    | 17.2 us                                                               | 17.3 us: 1.01x slower                                                           |
| deepcopy_reduce               | 1.51 us                                                               | 1.52 us: 1.01x slower                                                           |
| scimark_fft                   | 184 ms                                                                | 186 ms: 1.01x slower                                                            |
| crypto_pyaes                  | 50.6 ms                                                               | 51.1 ms: 1.01x slower                                                           |
| comprehensions                | 10.9 us                                                               | 11.0 us: 1.01x slower                                                           |
| regex_effbot                  | 2.47 ms                                                               | 2.50 ms: 1.01x slower                                                           |
| json                          | 2.96 ms                                                               | 3.01 ms: 1.01x slower                                                           |
| telco                         | 4.59 ms                                                               | 4.67 ms: 1.02x slower                                                           |
| chaos                         | 35.5 ms                                                               | 36.2 ms: 1.02x slower                                                           |
| Geometric mean                | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (36): tornado_http, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, typing_runtime_protocols, async_tree_eager_io, async_tree_memoization, bench_mp_pool, async_tree_eager_memoization_tg, async_tree_none, async_tree_eager_memoization, sqlglot_parse, scimark_monte_carlo, genshi_text, async_tree_eager_cpu_io_mixed_tg, pylint, pycparser, asyncio_websockets, json_dumps, async_tree_memoization_tg, html5lib, async_tree_eager_io_tg, async_tree_eager_tg, python_startup_no_site, pidigits, docutils, bench_thread_pool, scimark_sor, raytrace, pyflate, tomli_loads, python_startup, async_tree_none_tg, asyncio_tcp_ssl, genshi_xml, asyncio_tcp

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x