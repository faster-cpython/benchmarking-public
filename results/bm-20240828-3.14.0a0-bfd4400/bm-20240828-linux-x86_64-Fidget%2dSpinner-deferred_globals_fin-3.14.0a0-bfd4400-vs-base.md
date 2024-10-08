# Results vs. base

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.01x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 260 ms                                                                | 261 ms: 1.00x slower                                                            |
| html5lib       | 64.5 ms                                                               | 64.8 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_generators | 436 ms                                                                | 434 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl  | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                          |
| async_tree_none  | 322 ms                                                                | 325 ms: 1.01x slower                                                            |
| coroutines       | 22.9 ms                                                               | 23.3 ms: 1.02x slower                                                           |
| Geometric mean   | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (9): asyncio_tcp, asyncio_websockets, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 186 ms: 1.00x faster                                                            |
| nbody          | 84.7 ms                                                               | 87.3 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.62 ms                                                               | 3.60 ms: 1.01x faster                                                           |
| regex_dna      | 219 ms                                                                | 221 ms: 1.01x slower                                                            |
| regex_compile  | 129 ms                                                                | 130 ms: 1.01x slower                                                            |
| regex_v8       | 23.9 ms                                                               | 24.5 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 28.5 us                                                               | 28.3 us: 1.01x faster                                                           |
| pickle_pure_python   | 298 us                                                                | 300 us: 1.00x slower                                                            |
| tomli_loads          | 2.06 sec                                                              | 2.08 sec: 1.01x slower                                                          |
| xml_etree_process    | 59.1 ms                                                               | 59.8 ms: 1.01x slower                                                           |
| unpickle_pure_python | 209 us                                                                | 214 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (4): json_dumps, xml_etree_generate, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                           |
| python_startup_no_site | 7.06 ms                                                               | 7.05 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 33.8 ms                                                               | 34.3 ms: 1.01x slower                                                           |
| genshi_xml      | 50.0 ms                                                               | 51.0 ms: 1.02x slower                                                           |
| genshi_text     | 22.5 ms                                                               | 23.0 ms: 1.02x slower                                                           |
| mako            | 11.1 ms                                                               | 11.3 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| fannkuch                | 405 ms                                                                | 396 ms: 1.02x faster                                                            |
| mdp                     | 2.71 sec                                                              | 2.67 sec: 1.02x faster                                                          |
| pathlib                 | 16.2 ms                                                               | 15.9 ms: 1.02x faster                                                           |
| comprehensions          | 16.7 us                                                               | 16.5 us: 1.01x faster                                                           |
| crypto_pyaes            | 74.4 ms                                                               | 73.5 ms: 1.01x faster                                                           |
| spectral_norm           | 115 ms                                                                | 114 ms: 1.01x faster                                                            |
| hexiom                  | 6.17 ms                                                               | 6.10 ms: 1.01x faster                                                           |
| deltablue               | 3.17 ms                                                               | 3.14 ms: 1.01x faster                                                           |
| sympy_expand            | 460 ms                                                                | 457 ms: 1.01x faster                                                            |
| json_loads              | 28.5 us                                                               | 28.3 us: 1.01x faster                                                           |
| regex_effbot            | 3.62 ms                                                               | 3.60 ms: 1.01x faster                                                           |
| async_generators        | 436 ms                                                                | 434 ms: 1.00x faster                                                            |
| pidigits                | 187 ms                                                                | 186 ms: 1.00x faster                                                            |
| pyflate                 | 466 ms                                                                | 464 ms: 1.00x faster                                                            |
| chaos                   | 58.3 ms                                                               | 58.1 ms: 1.00x faster                                                           |
| meteor_contest          | 107 ms                                                                | 107 ms: 1.00x faster                                                            |
| sqlglot_normalize       | 107 ms                                                                | 107 ms: 1.00x faster                                                            |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                           |
| python_startup_no_site  | 7.06 ms                                                               | 7.05 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                          |
| sqlglot_optimize        | 53.1 ms                                                               | 53.2 ms: 1.00x slower                                                           |
| 2to3                    | 260 ms                                                                | 261 ms: 1.00x slower                                                            |
| pickle_pure_python      | 298 us                                                                | 300 us: 1.00x slower                                                            |
| html5lib                | 64.5 ms                                                               | 64.8 ms: 1.00x slower                                                           |
| tomli_loads             | 2.06 sec                                                              | 2.08 sec: 1.01x slower                                                          |
| deepcopy                | 258 us                                                                | 259 us: 1.01x slower                                                            |
| sqlglot_parse           | 1.28 ms                                                               | 1.28 ms: 1.01x slower                                                           |
| sqlglot_transpile       | 1.57 ms                                                               | 1.58 ms: 1.01x slower                                                           |
| richards                | 45.1 ms                                                               | 45.4 ms: 1.01x slower                                                           |
| scimark_monte_carlo     | 66.2 ms                                                               | 66.6 ms: 1.01x slower                                                           |
| create_gc_cycles        | 1.74 ms                                                               | 1.75 ms: 1.01x slower                                                           |
| go                      | 138 ms                                                                | 139 ms: 1.01x slower                                                            |
| regex_dna               | 219 ms                                                                | 221 ms: 1.01x slower                                                            |
| regex_compile           | 129 ms                                                                | 130 ms: 1.01x slower                                                            |
| async_tree_none         | 322 ms                                                                | 325 ms: 1.01x slower                                                            |
| xml_etree_process       | 59.1 ms                                                               | 59.8 ms: 1.01x slower                                                           |
| pprint_pformat          | 1.50 sec                                                              | 1.52 sec: 1.01x slower                                                          |
| raytrace                | 253 ms                                                                | 256 ms: 1.01x slower                                                            |
| django_template         | 33.8 ms                                                               | 34.3 ms: 1.01x slower                                                           |
| pprint_safe_repr        | 736 ms                                                                | 746 ms: 1.01x slower                                                            |
| scimark_lu              | 111 ms                                                                | 113 ms: 1.01x slower                                                            |
| richards_super          | 51.2 ms                                                               | 51.9 ms: 1.01x slower                                                           |
| scimark_fft             | 356 ms                                                                | 361 ms: 1.01x slower                                                            |
| generators              | 27.7 ms                                                               | 28.1 ms: 1.02x slower                                                           |
| coroutines              | 22.9 ms                                                               | 23.3 ms: 1.02x slower                                                           |
| scimark_sor             | 124 ms                                                                | 126 ms: 1.02x slower                                                            |
| unpickle_pure_python    | 209 us                                                                | 214 us: 1.02x slower                                                            |
| genshi_xml              | 50.0 ms                                                               | 51.0 ms: 1.02x slower                                                           |
| deepcopy_memo           | 29.1 us                                                               | 29.8 us: 1.02x slower                                                           |
| genshi_text             | 22.5 ms                                                               | 23.0 ms: 1.02x slower                                                           |
| mako                    | 11.1 ms                                                               | 11.3 ms: 1.02x slower                                                           |
| regex_v8                | 23.9 ms                                                               | 24.5 ms: 1.03x slower                                                           |
| nbody                   | 84.7 ms                                                               | 87.3 ms: 1.03x slower                                                           |
| logging_silent          | 96.5 ns                                                               | 104 ns: 1.07x slower                                                            |
| gc_traversal            | 3.57 ms                                                               | 3.85 ms: 1.08x slower                                                           |
| scimark_sparse_mat_mult | 4.52 ms                                                               | 4.96 ms: 1.10x slower                                                           |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (33): pycparser, json_dumps, telco, asyncio_tcp, logging_simple, bench_thread_pool, asyncio_websockets, bench_mp_pool, deepcopy_reduce, xml_etree_generate, typing_runtime_protocols, sympy_str, tornado_http, async_tree_io_tg, sympy_sum, float, docutils, sympy_integrate, coverage, pylint, nqueens, bpe_tokeniser, thrift, xml_etree_iterparse, logging_format, async_tree_cpu_io_mixed, json, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg, xml_etree_parse, async_tree_memoization_tg, async_tree_memoization

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x