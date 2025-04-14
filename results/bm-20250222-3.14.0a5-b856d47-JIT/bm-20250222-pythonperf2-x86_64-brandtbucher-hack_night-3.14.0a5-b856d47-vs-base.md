# Results vs. base

- fork: brandtbucher
- ref: hack_night
- machine: linux-x86_64
- commit hash: b856d47
- commit date: 2025-02-22
- overall geometric mean: 1.001x faster
- HPT reliability: 60.59%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 290 ms                                                           | 291 ms: 1.00x slower                                                    |
| docutils       | 2.94 sec                                                         | 2.96 sec: 1.01x slower                                                  |
| html5lib       | 67.3 ms                                                          | 68.5 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                            | 1.01x slower                                                            |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 359 ms                                                           | 353 ms: 1.02x faster                                                    |
| async_tree_io              | 650 ms                                                           | 640 ms: 1.02x faster                                                    |
| async_tree_none            | 296 ms                                                           | 291 ms: 1.01x faster                                                    |
| async_tree_memoization_tg  | 341 ms                                                           | 338 ms: 1.01x faster                                                    |
| async_tree_none_tg         | 282 ms                                                           | 280 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg | 514 ms                                                           | 511 ms: 1.00x faster                                                    |
| async_generators           | 428 ms                                                           | 434 ms: 1.01x slower                                                    |
| asyncio_websockets         | 384 ms                                                           | 389 ms: 1.01x slower                                                    |
| Geometric mean             | (ref)                                                            | 1.00x faster                                                            |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_io_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 253 ms                                                           | 253 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                            | 1.01x faster                                                            |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                           | 238 ms: 1.03x faster                                                    |
| regex_effbot   | 3.14 ms                                                          | 3.13 ms: 1.00x faster                                                   |
| regex_v8       | 24.5 ms                                                          | 25.5 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                            | 1.00x slower                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads           | 26.9 us                                                          | 26.6 us: 1.01x faster                                                   |
| tomli_loads          | 2.05 sec                                                         | 2.02 sec: 1.01x faster                                                  |
| xml_etree_process    | 56.2 ms                                                          | 55.9 ms: 1.01x faster                                                   |
| unpickle_pure_python | 205 us                                                           | 206 us: 1.01x slower                                                    |
| pickle_pure_python   | 335 us                                                           | 337 us: 1.01x slower                                                    |
| xml_etree_parse      | 136 ms                                                           | 137 ms: 1.01x slower                                                    |
| xml_etree_generate   | 79.0 ms                                                          | 79.8 ms: 1.01x slower                                                   |
| xml_etree_iterparse  | 95.5 ms                                                          | 96.6 ms: 1.01x slower                                                   |
| json_dumps           | 11.6 ms                                                          | 11.8 ms: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                            | 1.00x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 9.00 ms                                                          | 9.03 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                            | 1.00x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|-----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 9.74 ms                                                          | 9.61 ms: 1.01x faster                                                   |
| django_template | 36.5 ms                                                          | 36.3 ms: 1.01x faster                                                   |
| genshi_xml      | 55.5 ms                                                          | 58.3 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                            | 1.01x slower                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| coverage                   | 82.0 ms                                                          | 77.8 ms: 1.05x faster                                                   |
| generators                 | 29.8 ms                                                          | 28.9 ms: 1.03x faster                                                   |
| regex_dna                  | 244 ms                                                           | 238 ms: 1.03x faster                                                    |
| richards                   | 46.0 ms                                                          | 45.1 ms: 1.02x faster                                                   |
| async_tree_memoization     | 359 ms                                                           | 353 ms: 1.02x faster                                                    |
| async_tree_io              | 650 ms                                                           | 640 ms: 1.02x faster                                                    |
| subparsers                 | 23.4 ms                                                          | 23.0 ms: 1.02x faster                                                   |
| hexiom                     | 7.14 ms                                                          | 7.04 ms: 1.01x faster                                                   |
| async_tree_none            | 296 ms                                                           | 291 ms: 1.01x faster                                                    |
| mako                       | 9.74 ms                                                          | 9.61 ms: 1.01x faster                                                   |
| raytrace                   | 299 ms                                                           | 295 ms: 1.01x faster                                                    |
| json_loads                 | 26.9 us                                                          | 26.6 us: 1.01x faster                                                   |
| chaos                      | 62.9 ms                                                          | 62.1 ms: 1.01x faster                                                   |
| tomli_loads                | 2.05 sec                                                         | 2.02 sec: 1.01x faster                                                  |
| deepcopy_memo              | 29.2 us                                                          | 28.9 us: 1.01x faster                                                   |
| pyflate                    | 428 ms                                                           | 425 ms: 1.01x faster                                                    |
| deltablue                  | 3.47 ms                                                          | 3.44 ms: 1.01x faster                                                   |
| dulwich_log                | 68.0 ms                                                          | 67.4 ms: 1.01x faster                                                   |
| spectral_norm              | 83.1 ms                                                          | 82.4 ms: 1.01x faster                                                   |
| deepcopy                   | 283 us                                                           | 280 us: 1.01x faster                                                    |
| async_tree_memoization_tg  | 341 ms                                                           | 338 ms: 1.01x faster                                                    |
| richards_super             | 51.4 ms                                                          | 51.0 ms: 1.01x faster                                                   |
| async_tree_none_tg         | 282 ms                                                           | 280 ms: 1.01x faster                                                    |
| telco                      | 7.63 ms                                                          | 7.58 ms: 1.01x faster                                                   |
| django_template            | 36.5 ms                                                          | 36.3 ms: 1.01x faster                                                   |
| shortest_path              | 438 ms                                                           | 435 ms: 1.01x faster                                                    |
| xml_etree_process          | 56.2 ms                                                          | 55.9 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg | 514 ms                                                           | 511 ms: 1.00x faster                                                    |
| regex_effbot               | 3.14 ms                                                          | 3.13 ms: 1.00x faster                                                   |
| scimark_sparse_mat_mult    | 4.75 ms                                                          | 4.73 ms: 1.00x faster                                                   |
| sqlglot_optimize           | 60.5 ms                                                          | 60.3 ms: 1.00x faster                                                   |
| sqlalchemy_declarative     | 146 ms                                                           | 146 ms: 1.00x faster                                                    |
| logging_silent             | 97.5 ns                                                          | 97.3 ns: 1.00x faster                                                   |
| pidigits                   | 253 ms                                                           | 253 ms: 1.00x slower                                                    |
| bpe_tokeniser              | 4.57 sec                                                         | 4.58 sec: 1.00x slower                                                  |
| connected_components       | 402 ms                                                           | 403 ms: 1.00x slower                                                    |
| fannkuch                   | 381 ms                                                           | 382 ms: 1.00x slower                                                    |
| python_startup_no_site     | 9.00 ms                                                          | 9.03 ms: 1.00x slower                                                   |
| sympy_expand               | 514 ms                                                           | 515 ms: 1.00x slower                                                    |
| scimark_sor                | 106 ms                                                           | 107 ms: 1.00x slower                                                    |
| pathlib                    | 16.6 ms                                                          | 16.6 ms: 1.00x slower                                                   |
| comprehensions             | 18.9 us                                                          | 19.0 us: 1.00x slower                                                   |
| 2to3                       | 290 ms                                                           | 291 ms: 1.00x slower                                                    |
| gc_traversal               | 6.29 ms                                                          | 6.33 ms: 1.00x slower                                                   |
| scimark_fft                | 294 ms                                                           | 295 ms: 1.01x slower                                                    |
| sqlalchemy_imperative      | 18.0 ms                                                          | 18.1 ms: 1.01x slower                                                   |
| deepcopy_reduce            | 2.91 us                                                          | 2.93 us: 1.01x slower                                                   |
| docutils                   | 2.94 sec                                                         | 2.96 sec: 1.01x slower                                                  |
| unpickle_pure_python       | 205 us                                                           | 206 us: 1.01x slower                                                    |
| sympy_sum                  | 155 ms                                                           | 157 ms: 1.01x slower                                                    |
| pickle_pure_python         | 335 us                                                           | 337 us: 1.01x slower                                                    |
| xml_etree_parse            | 136 ms                                                           | 137 ms: 1.01x slower                                                    |
| sqlglot_transpile          | 1.77 ms                                                          | 1.78 ms: 1.01x slower                                                   |
| scimark_monte_carlo        | 60.6 ms                                                          | 61.1 ms: 1.01x slower                                                   |
| mdp                        | 2.55 sec                                                         | 2.57 sec: 1.01x slower                                                  |
| meteor_contest             | 132 ms                                                           | 133 ms: 1.01x slower                                                    |
| xml_etree_generate         | 79.0 ms                                                          | 79.8 ms: 1.01x slower                                                   |
| xml_etree_iterparse        | 95.5 ms                                                          | 96.6 ms: 1.01x slower                                                   |
| async_generators           | 428 ms                                                           | 434 ms: 1.01x slower                                                    |
| asyncio_websockets         | 384 ms                                                           | 389 ms: 1.01x slower                                                    |
| many_optionals             | 1.01 ms                                                          | 1.03 ms: 1.01x slower                                                   |
| json_dumps                 | 11.6 ms                                                          | 11.8 ms: 1.02x slower                                                   |
| html5lib                   | 67.3 ms                                                          | 68.5 ms: 1.02x slower                                                   |
| thrift                     | 856 us                                                           | 873 us: 1.02x slower                                                    |
| scimark_lu                 | 94.3 ms                                                          | 97.7 ms: 1.04x slower                                                   |
| regex_v8                   | 24.5 ms                                                          | 25.5 ms: 1.04x slower                                                   |
| genshi_xml                 | 55.5 ms                                                          | 58.3 ms: 1.05x slower                                                   |
| Geometric mean             | (ref)                                                            | 1.00x faster                                                            |

Benchmark hidden because not significant (29): bench_mp_pool, bench_thread_pool, float, nbody, pprint_pformat, async_tree_cpu_io_mixed, json, sympy_integrate, async_tree_io_tg, sqlglot_parse, coroutines, logging_simple, python_startup, sqlite_synth, crypto_pyaes, regex_compile, sympy_str, create_gc_cycles, pprint_safe_repr, sqlglot_normalize, logging_format, pycparser, go, pylint, typing_runtime_protocols, sphinx, genshi_text, nqueens, k_core

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 60.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x