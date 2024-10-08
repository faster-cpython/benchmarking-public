# Results vs. base

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-x86_64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.00x faster
- HPT reliability: 98.32%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240824-linux-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                | 255 ms: 1.00x slower                                                  |
| tornado_http   | 90.3 ms                                                               | 89.9 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240824-linux-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 928 ms                                                                | 891 ms: 1.04x faster                                                  |
| coroutines                 | 23.6 ms                                                               | 22.9 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed    | 554 ms                                                                | 544 ms: 1.02x faster                                                  |
| asyncio_tcp                | 480 ms                                                                | 477 ms: 1.01x faster                                                  |
| async_generators           | 437 ms                                                                | 434 ms: 1.01x faster                                                  |
| asyncio_websockets         | 557 ms                                                                | 559 ms: 1.00x slower                                                  |
| async_tree_cpu_io_mixed_tg | 536 ms                                                                | 546 ms: 1.02x slower                                                  |
| async_tree_memoization     | 389 ms                                                                | 402 ms: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (5): async_tree_io_tg, asyncio_tcp_ssl, async_tree_none_tg, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240824-linux-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                               | 85.5 ms: 1.03x faster                                                 |
| pidigits       | 187 ms                                                                | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240824-linux-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                | 128 ms: 1.01x faster                                                  |
| regex_effbot   | 3.57 ms                                                               | 3.58 ms: 1.00x slower                                                 |
| regex_dna      | 215 ms                                                                | 220 ms: 1.02x slower                                                  |
| regex_v8       | 23.6 ms                                                               | 24.1 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240824-linux-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 59.1 ms                                                               | 58.2 ms: 1.02x faster                                                 |
| xml_etree_generate   | 84.8 ms                                                               | 83.8 ms: 1.01x faster                                                 |
| json_loads           | 28.6 us                                                               | 28.2 us: 1.01x faster                                                 |
| tomli_loads          | 2.08 sec                                                              | 2.07 sec: 1.01x faster                                                |
| json_dumps           | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                 |
| pickle_pure_python   | 300 us                                                                | 301 us: 1.00x slower                                                  |
| unpickle_pure_python | 211 us                                                                | 213 us: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240824-linux-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                 |
| python_startup_no_site | 7.08 ms                                                               | 7.10 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240824-linux-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako           | 11.4 ms                                                               | 11.1 ms: 1.03x faster                                                 |
| genshi_text    | 22.2 ms                                                               | 21.8 ms: 1.02x faster                                                 |
| genshi_xml     | 49.6 ms                                                               | 49.5 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240824-linux-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.72 sec                                                              | 2.53 sec: 1.08x faster                                                |
| async_tree_io              | 928 ms                                                                | 891 ms: 1.04x faster                                                  |
| mako                       | 11.4 ms                                                               | 11.1 ms: 1.03x faster                                                 |
| coroutines                 | 23.6 ms                                                               | 22.9 ms: 1.03x faster                                                 |
| nbody                      | 88.0 ms                                                               | 85.5 ms: 1.03x faster                                                 |
| spectral_norm              | 114 ms                                                                | 111 ms: 1.02x faster                                                  |
| deepcopy_reduce            | 2.69 us                                                               | 2.64 us: 1.02x faster                                                 |
| async_tree_cpu_io_mixed    | 554 ms                                                                | 544 ms: 1.02x faster                                                  |
| pathlib                    | 16.0 ms                                                               | 15.7 ms: 1.02x faster                                                 |
| crypto_pyaes               | 73.3 ms                                                               | 72.0 ms: 1.02x faster                                                 |
| xml_etree_process          | 59.1 ms                                                               | 58.2 ms: 1.02x faster                                                 |
| genshi_text                | 22.2 ms                                                               | 21.8 ms: 1.02x faster                                                 |
| deepcopy                   | 262 us                                                                | 259 us: 1.01x faster                                                  |
| scimark_sparse_mat_mult    | 4.82 ms                                                               | 4.76 ms: 1.01x faster                                                 |
| meteor_contest             | 108 ms                                                                | 107 ms: 1.01x faster                                                  |
| scimark_lu                 | 114 ms                                                                | 113 ms: 1.01x faster                                                  |
| xml_etree_generate         | 84.8 ms                                                               | 83.8 ms: 1.01x faster                                                 |
| json_loads                 | 28.6 us                                                               | 28.2 us: 1.01x faster                                                 |
| sympy_str                  | 268 ms                                                                | 265 ms: 1.01x faster                                                  |
| scimark_monte_carlo        | 67.9 ms                                                               | 67.3 ms: 1.01x faster                                                 |
| tomli_loads                | 2.08 sec                                                              | 2.07 sec: 1.01x faster                                                |
| json_dumps                 | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                 |
| chaos                      | 58.6 ms                                                               | 58.2 ms: 1.01x faster                                                 |
| asyncio_tcp                | 480 ms                                                                | 477 ms: 1.01x faster                                                  |
| async_generators           | 437 ms                                                                | 434 ms: 1.01x faster                                                  |
| comprehensions             | 16.6 us                                                               | 16.5 us: 1.01x faster                                                 |
| generators                 | 27.7 ms                                                               | 27.6 ms: 1.01x faster                                                 |
| sqlglot_parse              | 1.28 ms                                                               | 1.27 ms: 1.01x faster                                                 |
| sqlglot_transpile          | 1.58 ms                                                               | 1.57 ms: 1.01x faster                                                 |
| fannkuch                   | 403 ms                                                                | 401 ms: 1.01x faster                                                  |
| hexiom                     | 6.14 ms                                                               | 6.11 ms: 1.01x faster                                                 |
| regex_compile              | 129 ms                                                                | 128 ms: 1.01x faster                                                  |
| deepcopy_memo              | 29.6 us                                                               | 29.5 us: 1.00x faster                                                 |
| tornado_http               | 90.3 ms                                                               | 89.9 ms: 1.00x faster                                                 |
| sympy_expand               | 453 ms                                                                | 451 ms: 1.00x faster                                                  |
| sympy_integrate            | 19.5 ms                                                               | 19.5 ms: 1.00x faster                                                 |
| genshi_xml                 | 49.6 ms                                                               | 49.5 ms: 1.00x faster                                                 |
| pidigits                   | 187 ms                                                                | 186 ms: 1.00x faster                                                  |
| bench_thread_pool          | 781 us                                                                | 783 us: 1.00x slower                                                  |
| 2to3                       | 254 ms                                                                | 255 ms: 1.00x slower                                                  |
| python_startup             | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                 |
| pickle_pure_python         | 300 us                                                                | 301 us: 1.00x slower                                                  |
| scimark_fft                | 364 ms                                                                | 365 ms: 1.00x slower                                                  |
| python_startup_no_site     | 7.08 ms                                                               | 7.10 ms: 1.00x slower                                                 |
| regex_effbot               | 3.57 ms                                                               | 3.58 ms: 1.00x slower                                                 |
| asyncio_websockets         | 557 ms                                                                | 559 ms: 1.00x slower                                                  |
| pprint_pformat             | 1.46 sec                                                              | 1.47 sec: 1.01x slower                                                |
| scimark_sor                | 125 ms                                                                | 127 ms: 1.01x slower                                                  |
| unpickle_pure_python       | 211 us                                                                | 213 us: 1.01x slower                                                  |
| raytrace                   | 259 ms                                                                | 262 ms: 1.01x slower                                                  |
| logging_silent             | 100 ns                                                                | 101 ns: 1.01x slower                                                  |
| create_gc_cycles           | 1.73 ms                                                               | 1.76 ms: 1.01x slower                                                 |
| regex_dna                  | 215 ms                                                                | 220 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 536 ms                                                                | 546 ms: 1.02x slower                                                  |
| regex_v8                   | 23.6 ms                                                               | 24.1 ms: 1.02x slower                                                 |
| async_tree_memoization     | 389 ms                                                                | 402 ms: 1.03x slower                                                  |
| gc_traversal               | 3.50 ms                                                               | 3.75 ms: 1.07x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (32): async_tree_io_tg, xml_etree_iterparse, xml_etree_parse, sympy_sum, logging_format, typing_runtime_protocols, django_template, nqueens, asyncio_tcp_ssl, sqlglot_optimize, pprint_safe_repr, html5lib, thrift, bench_mp_pool, pyflate, docutils, pylint, richards_super, logging_simple, go, sqlglot_normalize, async_tree_none_tg, json, coverage, deltablue, async_tree_memoization_tg, bpe_tokeniser, richards, float, pycparser, telco, async_tree_none

# HPT report

- Reliability score: 98.32% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x