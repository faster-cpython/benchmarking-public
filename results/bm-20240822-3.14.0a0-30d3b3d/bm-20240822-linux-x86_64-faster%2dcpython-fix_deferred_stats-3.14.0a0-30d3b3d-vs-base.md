# Results vs. base

- fork: faster-cpython
- ref: fix_deferred_stats
- machine: linux-x86_64
- commit hash: 30d3b3d
- commit date: 2024-08-22
- overall geometric mean: 1.00x faster
- HPT reliability: 96.53%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                                | 263 ms: 1.00x faster                                                          |
| docutils       | 2.70 sec                                                              | 2.69 sec: 1.00x faster                                                        |
| tornado_http   | 90.5 ms                                                               | 90.1 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 548 ms                                                                | 534 ms: 1.03x faster                                                          |
| async_tree_cpu_io_mixed    | 566 ms                                                                | 553 ms: 1.02x faster                                                          |
| async_tree_io              | 936 ms                                                                | 931 ms: 1.01x faster                                                          |
| asyncio_websockets         | 555 ms                                                                | 558 ms: 1.00x slower                                                          |
| asyncio_tcp_ssl            | 1.78 sec                                                              | 1.79 sec: 1.01x slower                                                        |
| async_generators           | 432 ms                                                                | 435 ms: 1.01x slower                                                          |
| coroutines                 | 23.1 ms                                                               | 23.4 ms: 1.01x slower                                                         |
| asyncio_tcp                | 474 ms                                                                | 484 ms: 1.02x slower                                                          |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 86.7 ms                                                               | 85.8 ms: 1.01x faster                                                         |
| float          | 78.1 ms                                                               | 79.1 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                               | 23.7 ms: 1.11x faster                                                         |
| regex_dna      | 223 ms                                                                | 225 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                  |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.08 sec                                                              | 2.04 sec: 1.02x faster                                                        |
| xml_etree_iterparse  | 106 ms                                                                | 105 ms: 1.01x faster                                                          |
| pickle_pure_python   | 306 us                                                                | 304 us: 1.01x faster                                                          |
| unpickle_pure_python | 214 us                                                                | 215 us: 1.01x slower                                                          |
| json_dumps           | 10.5 ms                                                               | 10.5 ms: 1.01x slower                                                         |
| xml_etree_generate   | 85.0 ms                                                               | 86.2 ms: 1.01x slower                                                         |
| xml_etree_process    | 58.9 ms                                                               | 59.7 ms: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 7.08 ms                                                               | 7.07 ms: 1.00x faster                                                         |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                         |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                  |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): django_template, mako, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8                   | 26.2 ms                                                               | 23.7 ms: 1.11x faster                                                         |
| gc_traversal               | 3.86 ms                                                               | 3.64 ms: 1.06x faster                                                         |
| scimark_fft                | 368 ms                                                                | 352 ms: 1.05x faster                                                          |
| pycparser                  | 1.19 sec                                                              | 1.14 sec: 1.04x faster                                                        |
| spectral_norm              | 114 ms                                                                | 111 ms: 1.03x faster                                                          |
| richards                   | 47.4 ms                                                               | 46.1 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 548 ms                                                                | 534 ms: 1.03x faster                                                          |
| richards_super             | 53.3 ms                                                               | 52.0 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed    | 566 ms                                                                | 553 ms: 1.02x faster                                                          |
| hexiom                     | 6.30 ms                                                               | 6.18 ms: 1.02x faster                                                         |
| fannkuch                   | 407 ms                                                                | 399 ms: 1.02x faster                                                          |
| tomli_loads                | 2.08 sec                                                              | 2.04 sec: 1.02x faster                                                        |
| generators                 | 28.1 ms                                                               | 27.6 ms: 1.02x faster                                                         |
| thrift                     | 779 us                                                                | 766 us: 1.02x faster                                                          |
| meteor_contest             | 109 ms                                                                | 107 ms: 1.02x faster                                                          |
| logging_silent             | 105 ns                                                                | 103 ns: 1.02x faster                                                          |
| sqlglot_parse              | 1.30 ms                                                               | 1.29 ms: 1.01x faster                                                         |
| nbody                      | 86.7 ms                                                               | 85.8 ms: 1.01x faster                                                         |
| xml_etree_iterparse        | 106 ms                                                                | 105 ms: 1.01x faster                                                          |
| sqlglot_transpile          | 1.60 ms                                                               | 1.58 ms: 1.01x faster                                                         |
| deltablue                  | 3.26 ms                                                               | 3.23 ms: 1.01x faster                                                         |
| chaos                      | 59.6 ms                                                               | 59.1 ms: 1.01x faster                                                         |
| pickle_pure_python         | 306 us                                                                | 304 us: 1.01x faster                                                          |
| coverage                   | 85.7 ms                                                               | 85.2 ms: 1.01x faster                                                         |
| create_gc_cycles           | 1.76 ms                                                               | 1.75 ms: 1.01x faster                                                         |
| crypto_pyaes               | 72.5 ms                                                               | 72.1 ms: 1.01x faster                                                         |
| async_tree_io              | 936 ms                                                                | 931 ms: 1.01x faster                                                          |
| comprehensions             | 16.6 us                                                               | 16.5 us: 1.01x faster                                                         |
| tornado_http               | 90.5 ms                                                               | 90.1 ms: 1.01x faster                                                         |
| 2to3                       | 264 ms                                                                | 263 ms: 1.00x faster                                                          |
| docutils                   | 2.70 sec                                                              | 2.69 sec: 1.00x faster                                                        |
| bench_thread_pool          | 789 us                                                                | 786 us: 1.00x faster                                                          |
| sympy_integrate            | 19.7 ms                                                               | 19.6 ms: 1.00x faster                                                         |
| sqlglot_normalize          | 107 ms                                                                | 107 ms: 1.00x faster                                                          |
| python_startup_no_site     | 7.08 ms                                                               | 7.07 ms: 1.00x faster                                                         |
| python_startup             | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                         |
| deepcopy                   | 262 us                                                                | 263 us: 1.00x slower                                                          |
| sqlglot_optimize           | 53.4 ms                                                               | 53.6 ms: 1.00x slower                                                         |
| raytrace                   | 264 ms                                                                | 265 ms: 1.00x slower                                                          |
| asyncio_websockets         | 555 ms                                                                | 558 ms: 1.00x slower                                                          |
| unpickle_pure_python       | 214 us                                                                | 215 us: 1.01x slower                                                          |
| asyncio_tcp_ssl            | 1.78 sec                                                              | 1.79 sec: 1.01x slower                                                        |
| async_generators           | 432 ms                                                                | 435 ms: 1.01x slower                                                          |
| pathlib                    | 16.1 ms                                                               | 16.3 ms: 1.01x slower                                                         |
| go                         | 142 ms                                                                | 143 ms: 1.01x slower                                                          |
| logging_simple             | 5.47 us                                                               | 5.51 us: 1.01x slower                                                         |
| regex_dna                  | 223 ms                                                                | 225 ms: 1.01x slower                                                          |
| deepcopy_memo              | 29.8 us                                                               | 30.1 us: 1.01x slower                                                         |
| typing_runtime_protocols   | 162 us                                                                | 164 us: 1.01x slower                                                          |
| json_dumps                 | 10.5 ms                                                               | 10.5 ms: 1.01x slower                                                         |
| pprint_safe_repr           | 743 ms                                                                | 751 ms: 1.01x slower                                                          |
| float                      | 78.1 ms                                                               | 79.1 ms: 1.01x slower                                                         |
| coroutines                 | 23.1 ms                                                               | 23.4 ms: 1.01x slower                                                         |
| deepcopy_reduce            | 2.66 us                                                               | 2.69 us: 1.01x slower                                                         |
| json                       | 5.32 ms                                                               | 5.39 ms: 1.01x slower                                                         |
| xml_etree_generate         | 85.0 ms                                                               | 86.2 ms: 1.01x slower                                                         |
| pprint_pformat             | 1.51 sec                                                              | 1.53 sec: 1.01x slower                                                        |
| xml_etree_process          | 58.9 ms                                                               | 59.7 ms: 1.01x slower                                                         |
| pyflate                    | 466 ms                                                                | 474 ms: 1.02x slower                                                          |
| scimark_sor                | 126 ms                                                                | 128 ms: 1.02x slower                                                          |
| asyncio_tcp                | 474 ms                                                                | 484 ms: 1.02x slower                                                          |
| mdp                        | 2.53 sec                                                              | 2.73 sec: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (27): async_tree_none_tg, xml_etree_parse, scimark_sparse_mat_mult, async_tree_memoization, async_tree_memoization_tg, async_tree_io_tg, logging_format, async_tree_none, django_template, sympy_str, sympy_sum, regex_effbot, telco, sympy_expand, pylint, nqueens, scimark_lu, mako, genshi_xml, pidigits, bench_mp_pool, scimark_monte_carlo, regex_compile, bpe_tokeniser, json_loads, genshi_text, html5lib

# HPT report

- Reliability score: 96.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x