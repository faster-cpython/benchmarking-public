# Results vs. base

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: c5de9e3
- commit date: 2024-09-05
- overall geometric mean: 1.001x slower
- HPT reliability: 92.39%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 275 ms                                                                | 274 ms: 1.00x faster                                                      |
| docutils       | 3.03 sec                                                              | 3.02 sec: 1.00x faster                                                    |
| html5lib       | 64.7 ms                                                               | 64.3 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 571 ms                                                                | 556 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed_tg | 553 ms                                                                | 538 ms: 1.03x faster                                                      |
| async_generators           | 460 ms                                                                | 453 ms: 1.02x faster                                                      |
| asyncio_tcp_ssl            | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                    |
| asyncio_tcp                | 485 ms                                                                | 488 ms: 1.00x slower                                                      |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_memoization_tg, coroutines, asyncio_websockets, async_tree_memoization, async_tree_io, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 70.2 ms                                                               | 71.4 ms: 1.02x slower                                                     |
| nbody          | 79.1 ms                                                               | 80.7 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                | 215 ms: 1.02x faster                                                      |
| regex_v8       | 24.8 ms                                                               | 24.4 ms: 1.02x faster                                                     |
| regex_compile  | 142 ms                                                                | 140 ms: 1.01x faster                                                      |
| regex_effbot   | 3.55 ms                                                               | 3.64 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                                | 211 us: 1.02x faster                                                      |
| pickle_pure_python   | 301 us                                                                | 298 us: 1.01x faster                                                      |
| xml_etree_process    | 55.2 ms                                                               | 54.7 ms: 1.01x faster                                                     |
| tomli_loads          | 1.93 sec                                                              | 1.92 sec: 1.01x faster                                                    |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                     |
| xml_etree_parse      | 145 ms                                                                | 148 ms: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (3): xml_etree_generate, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                     |
| python_startup_no_site | 7.11 ms                                                               | 7.18 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako           | 9.77 ms                                                               | 9.86 ms: 1.01x slower                                                     |
| genshi_xml     | 58.1 ms                                                               | 59.4 ms: 1.02x slower                                                     |
| genshi_text    | 24.2 ms                                                               | 24.9 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json                       | 5.56 ms                                                               | 5.32 ms: 1.05x faster                                                     |
| logging_silent             | 104 ns                                                                | 99.5 ns: 1.05x faster                                                     |
| async_tree_cpu_io_mixed    | 571 ms                                                                | 556 ms: 1.03x faster                                                      |
| deepcopy_memo              | 27.3 us                                                               | 26.6 us: 1.03x faster                                                     |
| async_tree_cpu_io_mixed_tg | 553 ms                                                                | 538 ms: 1.03x faster                                                      |
| unpickle_pure_python       | 216 us                                                                | 211 us: 1.02x faster                                                      |
| pprint_pformat             | 1.52 sec                                                              | 1.49 sec: 1.02x faster                                                    |
| regex_dna                  | 219 ms                                                                | 215 ms: 1.02x faster                                                      |
| async_generators           | 460 ms                                                                | 453 ms: 1.02x faster                                                      |
| regex_v8                   | 24.8 ms                                                               | 24.4 ms: 1.02x faster                                                     |
| pprint_safe_repr           | 724 ms                                                                | 713 ms: 1.01x faster                                                      |
| regex_compile              | 142 ms                                                                | 140 ms: 1.01x faster                                                      |
| pickle_pure_python         | 301 us                                                                | 298 us: 1.01x faster                                                      |
| richards_super             | 45.4 ms                                                               | 44.9 ms: 1.01x faster                                                     |
| dulwich_log                | 68.8 ms                                                               | 68.1 ms: 1.01x faster                                                     |
| xml_etree_process          | 55.2 ms                                                               | 54.7 ms: 1.01x faster                                                     |
| logging_simple             | 5.70 us                                                               | 5.65 us: 1.01x faster                                                     |
| sqlglot_parse              | 1.34 ms                                                               | 1.33 ms: 1.01x faster                                                     |
| tomli_loads                | 1.93 sec                                                              | 1.92 sec: 1.01x faster                                                    |
| sqlglot_transpile          | 1.70 ms                                                               | 1.68 ms: 1.01x faster                                                     |
| html5lib                   | 64.7 ms                                                               | 64.3 ms: 1.01x faster                                                     |
| 2to3                       | 275 ms                                                                | 274 ms: 1.00x faster                                                      |
| docutils                   | 3.03 sec                                                              | 3.02 sec: 1.00x faster                                                    |
| go                         | 130 ms                                                                | 130 ms: 1.00x faster                                                      |
| mdp                        | 2.54 sec                                                              | 2.53 sec: 1.00x faster                                                    |
| bench_thread_pool          | 836 us                                                                | 833 us: 1.00x faster                                                      |
| asyncio_tcp_ssl            | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                    |
| sympy_integrate            | 22.7 ms                                                               | 22.8 ms: 1.00x slower                                                     |
| pathlib                    | 15.9 ms                                                               | 16.0 ms: 1.00x slower                                                     |
| asyncio_tcp                | 485 ms                                                                | 488 ms: 1.00x slower                                                      |
| generators                 | 32.9 ms                                                               | 33.1 ms: 1.01x slower                                                     |
| sympy_expand               | 504 ms                                                                | 507 ms: 1.01x slower                                                      |
| json_dumps                 | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                     |
| python_startup             | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                     |
| meteor_contest             | 106 ms                                                                | 107 ms: 1.01x slower                                                      |
| mako                       | 9.77 ms                                                               | 9.86 ms: 1.01x slower                                                     |
| python_startup_no_site     | 7.11 ms                                                               | 7.18 ms: 1.01x slower                                                     |
| raytrace                   | 274 ms                                                                | 276 ms: 1.01x slower                                                      |
| sqlglot_optimize           | 57.7 ms                                                               | 58.3 ms: 1.01x slower                                                     |
| scimark_fft                | 303 ms                                                                | 307 ms: 1.01x slower                                                      |
| create_gc_cycles           | 1.75 ms                                                               | 1.78 ms: 1.01x slower                                                     |
| gc_traversal               | 3.56 ms                                                               | 3.62 ms: 1.02x slower                                                     |
| float                      | 70.2 ms                                                               | 71.4 ms: 1.02x slower                                                     |
| xml_etree_parse            | 145 ms                                                                | 148 ms: 1.02x slower                                                      |
| nbody                      | 79.1 ms                                                               | 80.7 ms: 1.02x slower                                                     |
| genshi_xml                 | 58.1 ms                                                               | 59.4 ms: 1.02x slower                                                     |
| regex_effbot               | 3.55 ms                                                               | 3.64 ms: 1.03x slower                                                     |
| genshi_text                | 24.2 ms                                                               | 24.9 ms: 1.03x slower                                                     |
| scimark_lu                 | 109 ms                                                                | 113 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult    | 4.20 ms                                                               | 4.55 ms: 1.08x slower                                                     |
| coverage                   | 86.5 ms                                                               | 94.0 ms: 1.09x slower                                                     |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (39): deepcopy_reduce, async_tree_none_tg, async_tree_memoization_tg, chaos, thrift, scimark_monte_carlo, sqlglot_normalize, coroutines, django_template, typing_runtime_protocols, scimark_sor, xml_etree_generate, asyncio_websockets, richards, bpe_tokeniser, pyflate, fannkuch, hexiom, pylint, spectral_norm, tornado_http, deepcopy, nqueens, bench_mp_pool, async_tree_memoization, deltablue, pidigits, sympy_sum, async_tree_io, comprehensions, json_loads, sympy_str, crypto_pyaes, logging_format, pycparser, async_tree_none, xml_etree_iterparse, telco, async_tree_io_tg

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 92.39% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x