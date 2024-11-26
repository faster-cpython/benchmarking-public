# Results vs. base

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.000x faster
- HPT reliability: 54.34%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                                      | 287 ms: 1.01x slower                                                                  |
| html5lib       | 72.7 ms                                                                     | 73.8 ms: 1.02x slower                                                                 |
| tornado_http   | 118 ms                                                                      | 116 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| coroutines       | 22.1 ms                                                                     | 21.7 ms: 1.01x faster                                                                 |
| async_generators | 352 ms                                                                      | 356 ms: 1.01x slower                                                                  |
| Geometric mean   | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (11): async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, asyncio_tcp_ssl, async_tree_cpu_io_mixed, asyncio_tcp, asyncio_websockets, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 89.8 ms                                                                     | 86.9 ms: 1.03x faster                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_effbot   | 3.56 ms                                                                     | 3.46 ms: 1.03x faster                                                                 |
| regex_v8       | 25.6 ms                                                                     | 25.4 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                                      | 211 us: 1.01x faster                                                                  |
| pickle_pure_python   | 313 us                                                                      | 311 us: 1.01x faster                                                                  |
| xml_etree_generate   | 83.8 ms                                                                     | 84.6 ms: 1.01x slower                                                                 |
| xml_etree_iterparse  | 100 ms                                                                      | 101 ms: 1.01x slower                                                                  |
| json_dumps           | 10.7 ms                                                                     | 10.9 ms: 1.02x slower                                                                 |
| tomli_loads          | 2.26 sec                                                                    | 2.30 sec: 1.02x slower                                                                |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (3): xml_etree_parse, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 55.3 ms                                                                     | 54.9 ms: 1.01x faster                                                                 |
| django_template | 39.5 ms                                                                     | 39.3 ms: 1.01x faster                                                                 |
| genshi_text     | 25.1 ms                                                                     | 25.3 ms: 1.01x slower                                                                 |
| Geometric mean  | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| fannkuch                | 374 ms                                                                      | 358 ms: 1.04x faster                                                                  |
| nbody                   | 89.8 ms                                                                     | 86.9 ms: 1.03x faster                                                                 |
| deepcopy_memo           | 30.3 us                                                                     | 29.4 us: 1.03x faster                                                                 |
| regex_effbot            | 3.56 ms                                                                     | 3.46 ms: 1.03x faster                                                                 |
| pyflate                 | 491 ms                                                                      | 478 ms: 1.03x faster                                                                  |
| mdp                     | 2.54 sec                                                                    | 2.48 sec: 1.02x faster                                                                |
| crypto_pyaes            | 72.8 ms                                                                     | 71.5 ms: 1.02x faster                                                                 |
| tornado_http            | 118 ms                                                                      | 116 ms: 1.02x faster                                                                  |
| coroutines              | 22.1 ms                                                                     | 21.7 ms: 1.01x faster                                                                 |
| pprint_safe_repr        | 839 ms                                                                      | 827 ms: 1.01x faster                                                                  |
| sqlglot_normalize       | 121 ms                                                                      | 120 ms: 1.01x faster                                                                  |
| richards_super          | 56.7 ms                                                                     | 56.2 ms: 1.01x faster                                                                 |
| scimark_sor             | 108 ms                                                                      | 107 ms: 1.01x faster                                                                  |
| logging_silent          | 98.1 ns                                                                     | 97.2 ns: 1.01x faster                                                                 |
| nqueens                 | 90.4 ms                                                                     | 89.7 ms: 1.01x faster                                                                 |
| unpickle_pure_python    | 213 us                                                                      | 211 us: 1.01x faster                                                                  |
| json                    | 5.41 ms                                                                     | 5.37 ms: 1.01x faster                                                                 |
| regex_v8                | 25.6 ms                                                                     | 25.4 ms: 1.01x faster                                                                 |
| genshi_xml              | 55.3 ms                                                                     | 54.9 ms: 1.01x faster                                                                 |
| pickle_pure_python      | 313 us                                                                      | 311 us: 1.01x faster                                                                  |
| django_template         | 39.5 ms                                                                     | 39.3 ms: 1.01x faster                                                                 |
| spectral_norm           | 96.1 ms                                                                     | 95.7 ms: 1.00x faster                                                                 |
| scimark_sparse_mat_mult | 4.19 ms                                                                     | 4.18 ms: 1.00x faster                                                                 |
| pprint_pformat          | 1.70 sec                                                                    | 1.70 sec: 1.00x slower                                                                |
| meteor_contest          | 126 ms                                                                      | 127 ms: 1.00x slower                                                                  |
| hexiom                  | 6.32 ms                                                                     | 6.34 ms: 1.00x slower                                                                 |
| comprehensions          | 17.3 us                                                                     | 17.4 us: 1.01x slower                                                                 |
| 2to3                    | 285 ms                                                                      | 287 ms: 1.01x slower                                                                  |
| deltablue               | 3.41 ms                                                                     | 3.43 ms: 1.01x slower                                                                 |
| bpe_tokeniser           | 4.89 sec                                                                    | 4.92 sec: 1.01x slower                                                                |
| scimark_lu              | 94.1 ms                                                                     | 94.8 ms: 1.01x slower                                                                 |
| scimark_fft             | 299 ms                                                                      | 301 ms: 1.01x slower                                                                  |
| sympy_expand            | 499 ms                                                                      | 503 ms: 1.01x slower                                                                  |
| xml_etree_generate      | 83.8 ms                                                                     | 84.6 ms: 1.01x slower                                                                 |
| chaos                   | 61.4 ms                                                                     | 62.0 ms: 1.01x slower                                                                 |
| sympy_integrate         | 23.2 ms                                                                     | 23.5 ms: 1.01x slower                                                                 |
| xml_etree_iterparse     | 100 ms                                                                      | 101 ms: 1.01x slower                                                                  |
| sympy_str               | 293 ms                                                                      | 296 ms: 1.01x slower                                                                  |
| thrift                  | 863 us                                                                      | 872 us: 1.01x slower                                                                  |
| genshi_text             | 25.1 ms                                                                     | 25.3 ms: 1.01x slower                                                                 |
| telco                   | 7.90 ms                                                                     | 7.98 ms: 1.01x slower                                                                 |
| async_generators        | 352 ms                                                                      | 356 ms: 1.01x slower                                                                  |
| gc_traversal            | 4.40 ms                                                                     | 4.45 ms: 1.01x slower                                                                 |
| sympy_sum               | 153 ms                                                                      | 155 ms: 1.01x slower                                                                  |
| sqlglot_transpile       | 1.77 ms                                                                     | 1.80 ms: 1.01x slower                                                                 |
| pycparser               | 1.24 sec                                                                    | 1.26 sec: 1.02x slower                                                                |
| html5lib                | 72.7 ms                                                                     | 73.8 ms: 1.02x slower                                                                 |
| json_dumps              | 10.7 ms                                                                     | 10.9 ms: 1.02x slower                                                                 |
| tomli_loads             | 2.26 sec                                                                    | 2.30 sec: 1.02x slower                                                                |
| sqlglot_parse           | 1.40 ms                                                                     | 1.43 ms: 1.02x slower                                                                 |
| bench_mp_pool           | 4.51 ms                                                                     | 4.67 ms: 1.04x slower                                                                 |
| coverage                | 79.6 ms                                                                     | 83.6 ms: 1.05x slower                                                                 |
| Geometric mean          | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (37): async_tree_io_tg, async_tree_io, mako, typing_runtime_protocols, async_tree_none_tg, go, scimark_monte_carlo, deepcopy_reduce, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, bench_thread_pool, pathlib, deepcopy, regex_dna, asyncio_tcp_ssl, sqlglot_optimize, docutils, async_tree_cpu_io_mixed, asyncio_tcp, pidigits, regex_compile, python_startup_no_site, asyncio_websockets, python_startup, raytrace, richards, xml_etree_parse, pylint, logging_format, float, logging_simple, json_loads, async_tree_none, xml_etree_process, async_tree_memoization, generators, create_gc_cycles

- Geometric mean (including insignificant results): 1.000x faster
# HPT report

- Reliability score: 54.34% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x