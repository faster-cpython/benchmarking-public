# Results vs. base

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-aarch64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_generators | 489 ms                                                                  | 476 ms: 1.03x faster                                                   |
| async_tree_io    | 1.17 sec                                                                | 1.15 sec: 1.02x faster                                                 |
| asyncio_tcp      | 551 ms                                                                  | 568 ms: 1.03x slower                                                   |
| Geometric mean   | (ref)                                                                   | 1.01x faster                                                           |

Benchmark hidden because not significant (10): async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none, coroutines, asyncio_tcp_ssl, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 126 ms                                                                  | 124 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                           |

Benchmark hidden because not significant (3): regex_dna, regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 368 us                                                                  | 358 us: 1.03x faster                                                   |
| unpickle_pure_python | 254 us                                                                  | 250 us: 1.02x faster                                                   |
| tomli_loads          | 2.63 sec                                                                | 2.61 sec: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                                   | 1.00x faster                                                           |

Benchmark hidden because not significant (11): xml_etree_generate, pickle, json_loads, json_dumps, unpickle_list, unpickle, pickle_dict, pickle_list, xml_etree_process, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 8.58 ms                                                                 | 8.62 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                   | 1.00x slower                                                           |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 41.4 ms                                                                 | 42.7 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                                   | 1.00x slower                                                           |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, mako

All benchmarks:
===============

| Benchmark               | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| scimark_fft             | 471 ms                                                                  | 439 ms: 1.07x faster                                                   |
| nqueens                 | 100 ms                                                                  | 97.0 ms: 1.03x faster                                                  |
| unpack_sequence         | 58.9 ns                                                                 | 57.3 ns: 1.03x faster                                                  |
| async_generators        | 489 ms                                                                  | 476 ms: 1.03x faster                                                   |
| pickle_pure_python      | 368 us                                                                  | 358 us: 1.03x faster                                                   |
| sympy_sum               | 142 ms                                                                  | 139 ms: 1.02x faster                                                   |
| logging_simple          | 7.06 us                                                                 | 6.92 us: 1.02x faster                                                  |
| gc_traversal            | 5.12 ms                                                                 | 5.02 ms: 1.02x faster                                                  |
| async_tree_io           | 1.17 sec                                                                | 1.15 sec: 1.02x faster                                                 |
| scimark_sor             | 157 ms                                                                  | 155 ms: 1.02x faster                                                   |
| unpickle_pure_python    | 254 us                                                                  | 250 us: 1.02x faster                                                   |
| regex_compile           | 126 ms                                                                  | 124 ms: 1.02x faster                                                   |
| mdp                     | 3.34 sec                                                                | 3.29 sec: 1.02x faster                                                 |
| deepcopy_reduce         | 3.54 us                                                                 | 3.49 us: 1.02x faster                                                  |
| go                      | 138 ms                                                                  | 136 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult | 6.49 ms                                                                 | 6.39 ms: 1.01x faster                                                  |
| pprint_pformat          | 1.88 sec                                                                | 1.86 sec: 1.01x faster                                                 |
| pprint_safe_repr        | 911 ms                                                                  | 904 ms: 1.01x faster                                                   |
| tomli_loads             | 2.63 sec                                                                | 2.61 sec: 1.01x faster                                                 |
| python_startup_no_site  | 8.58 ms                                                                 | 8.62 ms: 1.00x slower                                                  |
| pathlib                 | 20.9 ms                                                                 | 21.2 ms: 1.01x slower                                                  |
| django_template         | 41.4 ms                                                                 | 42.7 ms: 1.03x slower                                                  |
| asyncio_tcp             | 551 ms                                                                  | 568 ms: 1.03x slower                                                   |
| Geometric mean          | (ref)                                                                   | 1.01x faster                                                           |

Benchmark hidden because not significant (74): html5lib, genshi_xml, xml_etree_generate, async_tree_none_tg, sqlite_synth, logging_format, pycparser, async_tree_memoization, typing_runtime_protocols, async_tree_memoization_tg, sympy_str, sympy_expand, asyncio_websockets, async_tree_cpu_io_mixed_tg, deepcopy, async_tree_io_tg, deepcopy_memo, spectral_norm, nbody, regex_dna, telco, tornado_http, docutils, meteor_contest, richards_super, async_tree_none, scimark_lu, thrift, logging_silent, bench_thread_pool, create_gc_cycles, json, bpe_tokeniser, coroutines, chaos, pickle, richards, asyncio_tcp_ssl, regex_v8, pylint, sqlglot_optimize, sympy_integrate, pidigits, fannkuch, genshi_text, raytrace, json_loads, deltablue, sqlglot_normalize, coverage, sqlglot_transpile, json_dumps, unpickle_list, generators, hexiom, crypto_pyaes, async_tree_cpu_io_mixed, unpickle, pickle_dict, pickle_list, bench_mp_pool, float, pyflate, python_startup, scimark_monte_carlo, mako, dulwich_log, xml_etree_process, sqlglot_parse, xml_etree_parse, regex_effbot, comprehensions, xml_etree_iterparse, 2to3

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x