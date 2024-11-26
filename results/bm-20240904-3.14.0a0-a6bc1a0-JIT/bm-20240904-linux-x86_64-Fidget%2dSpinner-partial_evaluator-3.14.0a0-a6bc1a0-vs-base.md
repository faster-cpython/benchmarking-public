# Results vs. base

- fork: Fidget-Spinner
- ref: partial_evaluator
- machine: linux-x86_64
- commit hash: a6bc1a0
- commit date: 2024-09-04
- overall geometric mean: 1.002x slower
- HPT reliability: 96.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                              | 2.95 sec: 1.00x faster                                                       |
| html5lib       | 64.7 ms                                                               | 62.4 ms: 1.04x faster                                                        |
| tornado_http   | 94.4 ms                                                               | 95.0 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                       |
| coroutines                 | 22.7 ms                                                               | 22.9 ms: 1.01x slower                                                        |
| async_generators           | 455 ms                                                                | 459 ms: 1.01x slower                                                         |
| async_tree_io              | 933 ms                                                                | 946 ms: 1.01x slower                                                         |
| async_tree_none_tg         | 310 ms                                                                | 316 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 537 ms                                                                | 550 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed    | 554 ms                                                                | 568 ms: 1.03x slower                                                         |
| async_tree_memoization     | 401 ms                                                                | 414 ms: 1.03x slower                                                         |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                                 |

Benchmark hidden because not significant (5): asyncio_tcp, asyncio_websockets, async_tree_memoization_tg, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 70.1 ms                                                               | 70.9 ms: 1.01x slower                                                        |
| pidigits       | 185 ms                                                                | 188 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 217 ms                                                                | 212 ms: 1.02x faster                                                         |
| regex_effbot   | 3.52 ms                                                               | 3.58 ms: 1.02x slower                                                        |
| regex_v8       | 24.0 ms                                                               | 24.7 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 304 us                                                                | 300 us: 1.01x faster                                                         |
| json_dumps           | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                        |
| xml_etree_process    | 55.1 ms                                                               | 54.5 ms: 1.01x faster                                                        |
| unpickle_pure_python | 215 us                                                                | 214 us: 1.01x faster                                                         |
| xml_etree_iterparse  | 98.3 ms                                                               | 98.8 ms: 1.00x slower                                                        |
| xml_etree_parse      | 145 ms                                                                | 146 ms: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                 |

Benchmark hidden because not significant (3): xml_etree_generate, json_loads, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                        |
| python_startup_no_site | 7.15 ms                                                               | 7.21 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 58.3 ms                                                               | 56.6 ms: 1.03x faster                                                        |
| mako           | 9.97 ms                                                               | 9.72 ms: 1.03x faster                                                        |
| genshi_text    | 24.9 ms                                                               | 24.6 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| html5lib                   | 64.7 ms                                                               | 62.4 ms: 1.04x faster                                                        |
| genshi_xml                 | 58.3 ms                                                               | 56.6 ms: 1.03x faster                                                        |
| mako                       | 9.97 ms                                                               | 9.72 ms: 1.03x faster                                                        |
| deepcopy                   | 267 us                                                                | 261 us: 1.02x faster                                                         |
| regex_dna                  | 217 ms                                                                | 212 ms: 1.02x faster                                                         |
| pathlib                    | 16.0 ms                                                               | 15.7 ms: 1.02x faster                                                        |
| richards_super             | 45.4 ms                                                               | 44.8 ms: 1.02x faster                                                        |
| genshi_text                | 24.9 ms                                                               | 24.6 ms: 1.01x faster                                                        |
| scimark_lu                 | 111 ms                                                                | 110 ms: 1.01x faster                                                         |
| pickle_pure_python         | 304 us                                                                | 300 us: 1.01x faster                                                         |
| json_dumps                 | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                        |
| raytrace                   | 275 ms                                                                | 272 ms: 1.01x faster                                                         |
| xml_etree_process          | 55.1 ms                                                               | 54.5 ms: 1.01x faster                                                        |
| go                         | 131 ms                                                                | 130 ms: 1.01x faster                                                         |
| sqlglot_optimize           | 58.4 ms                                                               | 57.8 ms: 1.01x faster                                                        |
| sqlglot_parse              | 1.34 ms                                                               | 1.33 ms: 1.01x faster                                                        |
| sqlglot_normalize          | 113 ms                                                                | 112 ms: 1.01x faster                                                         |
| thrift                     | 786 us                                                                | 782 us: 1.01x faster                                                         |
| generators                 | 33.1 ms                                                               | 32.9 ms: 1.01x faster                                                        |
| sqlglot_transpile          | 1.69 ms                                                               | 1.68 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 215 us                                                                | 214 us: 1.01x faster                                                         |
| mdp                        | 2.55 sec                                                              | 2.54 sec: 1.00x faster                                                       |
| docutils                   | 2.96 sec                                                              | 2.95 sec: 1.00x faster                                                       |
| sympy_str                  | 301 ms                                                                | 299 ms: 1.00x faster                                                         |
| fannkuch                   | 372 ms                                                                | 371 ms: 1.00x faster                                                         |
| sympy_integrate            | 22.8 ms                                                               | 22.7 ms: 1.00x faster                                                        |
| scimark_fft                | 309 ms                                                                | 309 ms: 1.00x faster                                                         |
| asyncio_tcp_ssl            | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                       |
| python_startup             | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                        |
| xml_etree_iterparse        | 98.3 ms                                                               | 98.8 ms: 1.00x slower                                                        |
| coroutines                 | 22.7 ms                                                               | 22.9 ms: 1.01x slower                                                        |
| bpe_tokeniser              | 4.43 sec                                                              | 4.46 sec: 1.01x slower                                                       |
| tornado_http               | 94.4 ms                                                               | 95.0 ms: 1.01x slower                                                        |
| async_generators           | 455 ms                                                                | 459 ms: 1.01x slower                                                         |
| xml_etree_parse            | 145 ms                                                                | 146 ms: 1.01x slower                                                         |
| python_startup_no_site     | 7.15 ms                                                               | 7.21 ms: 1.01x slower                                                        |
| hexiom                     | 6.86 ms                                                               | 6.92 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 165 us                                                                | 166 us: 1.01x slower                                                         |
| float                      | 70.1 ms                                                               | 70.9 ms: 1.01x slower                                                        |
| logging_format             | 6.07 us                                                               | 6.14 us: 1.01x slower                                                        |
| coverage                   | 85.4 ms                                                               | 86.4 ms: 1.01x slower                                                        |
| pidigits                   | 185 ms                                                                | 188 ms: 1.01x slower                                                         |
| deepcopy_memo              | 26.7 us                                                               | 27.0 us: 1.01x slower                                                        |
| pyflate                    | 449 ms                                                                | 456 ms: 1.01x slower                                                         |
| async_tree_io              | 933 ms                                                                | 946 ms: 1.01x slower                                                         |
| pprint_safe_repr           | 718 ms                                                                | 729 ms: 1.02x slower                                                         |
| regex_effbot               | 3.52 ms                                                               | 3.58 ms: 1.02x slower                                                        |
| create_gc_cycles           | 1.75 ms                                                               | 1.78 ms: 1.02x slower                                                        |
| async_tree_none_tg         | 310 ms                                                                | 316 ms: 1.02x slower                                                         |
| logging_simple             | 5.51 us                                                               | 5.61 us: 1.02x slower                                                        |
| scimark_sor                | 116 ms                                                                | 118 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 537 ms                                                                | 550 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed    | 554 ms                                                                | 568 ms: 1.03x slower                                                         |
| spectral_norm              | 99.9 ms                                                               | 103 ms: 1.03x slower                                                         |
| pprint_pformat             | 1.47 sec                                                              | 1.51 sec: 1.03x slower                                                       |
| regex_v8                   | 24.0 ms                                                               | 24.7 ms: 1.03x slower                                                        |
| async_tree_memoization     | 401 ms                                                                | 414 ms: 1.03x slower                                                         |
| pycparser                  | 1.18 sec                                                              | 1.22 sec: 1.03x slower                                                       |
| gc_traversal               | 3.56 ms                                                               | 3.77 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                                 |

Benchmark hidden because not significant (31): django_template, json, comprehensions, deltablue, xml_etree_generate, richards, sympy_sum, bench_thread_pool, telco, meteor_contest, bench_mp_pool, asyncio_tcp, logging_silent, pylint, regex_compile, json_loads, sympy_expand, crypto_pyaes, 2to3, asyncio_websockets, dulwich_log, nqueens, nbody, scimark_monte_carlo, tomli_loads, scimark_sparse_mat_mult, deepcopy_reduce, async_tree_memoization_tg, chaos, async_tree_io_tg, async_tree_none

- Geometric mean (including insignificant results): 1.002x slower
# HPT report

- Reliability score: 96.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x