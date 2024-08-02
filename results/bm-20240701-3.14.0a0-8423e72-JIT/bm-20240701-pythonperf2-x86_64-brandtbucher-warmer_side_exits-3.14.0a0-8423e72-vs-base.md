# Results vs. base

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-x86_64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.00x faster
- HPT reliability: 86.58%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                                      | 309 ms: 1.01x slower                                                           |
| docutils       | 3.12 sec                                                                    | 3.14 sec: 1.01x slower                                                         |
| html5lib       | 74.0 ms                                                                     | 73.0 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|---------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 385 ms                                                                      | 389 ms: 1.01x slower                                                           |
| Geometric mean            | (ref)                                                                       | 1.00x slower                                                                   |

Benchmark hidden because not significant (7): async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 85.2 ms                                                                     | 83.1 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 264 ms                                                                      | 240 ms: 1.10x faster                                                           |
| regex_v8       | 27.0 ms                                                                     | 25.5 ms: 1.06x faster                                                          |
| regex_effbot   | 3.74 ms                                                                     | 3.66 ms: 1.02x faster                                                          |
| regex_compile  | 137 ms                                                                      | 138 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                       | 1.04x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                                      | 202 us: 1.07x faster                                                           |
| json_dumps           | 10.9 ms                                                                     | 10.8 ms: 1.01x faster                                                          |
| xml_etree_iterparse  | 99.4 ms                                                                     | 98.9 ms: 1.00x faster                                                          |
| xml_etree_generate   | 82.1 ms                                                                     | 82.5 ms: 1.00x slower                                                          |
| json_loads           | 25.0 us                                                                     | 25.2 us: 1.01x slower                                                          |
| tomli_loads          | 2.09 sec                                                                    | 2.10 sec: 1.01x slower                                                         |
| xml_etree_parse      | 141 ms                                                                      | 143 ms: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 9.08 ms                                                                     | 9.11 ms: 1.00x slower                                                          |
| python_startup         | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                          |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 65.5 ms                                                                     | 62.0 ms: 1.06x faster                                                          |
| genshi_text     | 28.4 ms                                                                     | 27.2 ms: 1.04x faster                                                          |
| mako            | 9.26 ms                                                                     | 8.97 ms: 1.03x faster                                                          |
| django_template | 41.3 ms                                                                     | 42.2 ms: 1.02x slower                                                          |
| Geometric mean  | (ref)                                                                       | 1.03x faster                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|---------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna                 | 264 ms                                                                      | 240 ms: 1.10x faster                                                           |
| unpickle_pure_python      | 216 us                                                                      | 202 us: 1.07x faster                                                           |
| regex_v8                  | 27.0 ms                                                                     | 25.5 ms: 1.06x faster                                                          |
| genshi_xml                | 65.5 ms                                                                     | 62.0 ms: 1.06x faster                                                          |
| pyflate                   | 466 ms                                                                      | 443 ms: 1.05x faster                                                           |
| spectral_norm             | 87.4 ms                                                                     | 83.2 ms: 1.05x faster                                                          |
| genshi_text               | 28.4 ms                                                                     | 27.2 ms: 1.04x faster                                                          |
| gc_traversal              | 4.66 ms                                                                     | 4.49 ms: 1.04x faster                                                          |
| thrift                    | 922 us                                                                      | 889 us: 1.04x faster                                                           |
| logging_silent            | 105 ns                                                                      | 101 ns: 1.03x faster                                                           |
| mako                      | 9.26 ms                                                                     | 8.97 ms: 1.03x faster                                                          |
| async_generators          | 398 ms                                                                      | 385 ms: 1.03x faster                                                           |
| nbody                     | 85.2 ms                                                                     | 83.1 ms: 1.02x faster                                                          |
| regex_effbot              | 3.74 ms                                                                     | 3.66 ms: 1.02x faster                                                          |
| deepcopy_reduce           | 3.12 us                                                                     | 3.06 us: 1.02x faster                                                          |
| sqlglot_normalize         | 130 ms                                                                      | 128 ms: 1.02x faster                                                           |
| mdp                       | 2.59 sec                                                                    | 2.54 sec: 1.02x faster                                                         |
| coverage                  | 83.5 ms                                                                     | 82.0 ms: 1.02x faster                                                          |
| deepcopy_memo             | 29.5 us                                                                     | 29.1 us: 1.02x faster                                                          |
| telco                     | 8.21 ms                                                                     | 8.10 ms: 1.01x faster                                                          |
| html5lib                  | 74.0 ms                                                                     | 73.0 ms: 1.01x faster                                                          |
| json_dumps                | 10.9 ms                                                                     | 10.8 ms: 1.01x faster                                                          |
| coroutines                | 21.5 ms                                                                     | 21.2 ms: 1.01x faster                                                          |
| pprint_safe_repr          | 806 ms                                                                      | 797 ms: 1.01x faster                                                           |
| hexiom                    | 6.75 ms                                                                     | 6.70 ms: 1.01x faster                                                          |
| xml_etree_iterparse       | 99.4 ms                                                                     | 98.9 ms: 1.00x faster                                                          |
| pathlib                   | 16.2 ms                                                                     | 16.1 ms: 1.00x faster                                                          |
| meteor_contest            | 131 ms                                                                      | 131 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl           | 1.58 sec                                                                    | 1.58 sec: 1.00x slower                                                         |
| python_startup_no_site    | 9.08 ms                                                                     | 9.11 ms: 1.00x slower                                                          |
| scimark_lu                | 114 ms                                                                      | 115 ms: 1.00x slower                                                           |
| python_startup            | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                          |
| xml_etree_generate        | 82.1 ms                                                                     | 82.5 ms: 1.00x slower                                                          |
| bpe_tokeniser             | 5.12 sec                                                                    | 5.15 sec: 1.01x slower                                                         |
| json_loads                | 25.0 us                                                                     | 25.2 us: 1.01x slower                                                          |
| tomli_loads               | 2.09 sec                                                                    | 2.10 sec: 1.01x slower                                                         |
| docutils                  | 3.12 sec                                                                    | 3.14 sec: 1.01x slower                                                         |
| regex_compile             | 137 ms                                                                      | 138 ms: 1.01x slower                                                           |
| sqlglot_optimize          | 62.7 ms                                                                     | 63.1 ms: 1.01x slower                                                          |
| sympy_str                 | 309 ms                                                                      | 311 ms: 1.01x slower                                                           |
| json                      | 5.43 ms                                                                     | 5.47 ms: 1.01x slower                                                          |
| scimark_sparse_mat_mult   | 4.01 ms                                                                     | 4.05 ms: 1.01x slower                                                          |
| chaos                     | 66.4 ms                                                                     | 67.0 ms: 1.01x slower                                                          |
| create_gc_cycles          | 1.93 ms                                                                     | 1.95 ms: 1.01x slower                                                          |
| async_tree_memoization_tg | 385 ms                                                                      | 389 ms: 1.01x slower                                                           |
| sympy_expand              | 522 ms                                                                      | 528 ms: 1.01x slower                                                           |
| sympy_sum                 | 165 ms                                                                      | 167 ms: 1.01x slower                                                           |
| xml_etree_parse           | 141 ms                                                                      | 143 ms: 1.01x slower                                                           |
| 2to3                      | 305 ms                                                                      | 309 ms: 1.01x slower                                                           |
| go                        | 163 ms                                                                      | 165 ms: 1.02x slower                                                           |
| generators                | 34.6 ms                                                                     | 35.2 ms: 1.02x slower                                                          |
| sympy_integrate           | 25.5 ms                                                                     | 26.0 ms: 1.02x slower                                                          |
| bench_mp_pool             | 4.75 ms                                                                     | 4.86 ms: 1.02x slower                                                          |
| django_template           | 41.3 ms                                                                     | 42.2 ms: 1.02x slower                                                          |
| scimark_sor               | 129 ms                                                                      | 132 ms: 1.02x slower                                                           |
| fannkuch                  | 343 ms                                                                      | 352 ms: 1.03x slower                                                           |
| asyncio_websockets        | 390 ms                                                                      | 401 ms: 1.03x slower                                                           |
| raytrace                  | 288 ms                                                                      | 300 ms: 1.04x slower                                                           |
| logging_format            | 6.84 us                                                                     | 7.11 us: 1.04x slower                                                          |
| logging_simple            | 6.13 us                                                                     | 6.40 us: 1.04x slower                                                          |
| deltablue                 | 3.63 ms                                                                     | 3.80 ms: 1.05x slower                                                          |
| pycparser                 | 1.21 sec                                                                    | 1.29 sec: 1.06x slower                                                         |
| Geometric mean            | (ref)                                                                       | 1.00x faster                                                                   |

Benchmark hidden because not significant (29): richards_super, pprint_pformat, nqueens, async_tree_io, async_tree_io_tg, bench_thread_pool, typing_runtime_protocols, xml_etree_process, sqlglot_transpile, sqlglot_parse, scimark_fft, scimark_monte_carlo, comprehensions, richards, pidigits, pickle_pure_python, dulwich_log, deepcopy, float, async_tree_cpu_io_mixed, async_tree_memoization, asyncio_tcp, async_tree_cpu_io_mixed_tg, dask, tornado_http, crypto_pyaes, async_tree_none_tg, async_tree_none, pylint

# HPT report

- Reliability score: 86.58% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x