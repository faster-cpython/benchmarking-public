# Results vs. base

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-x86_64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.00x faster
- HPT reliability: 55.22%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                      | 281 ms: 1.00x faster                                                        |
| html5lib       | 75.1 ms                                                                     | 73.1 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 392 ms                                                                      | 379 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed   | 575 ms                                                                      | 558 ms: 1.03x faster                                                        |
| asyncio_tcp               | 372 ms                                                                      | 366 ms: 1.02x faster                                                        |
| async_tree_io_tg          | 783 ms                                                                      | 775 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl           | 1.58 sec                                                                    | 1.59 sec: 1.01x slower                                                      |
| coroutines                | 21.2 ms                                                                     | 21.3 ms: 1.01x slower                                                       |
| async_tree_io             | 807 ms                                                                      | 827 ms: 1.03x slower                                                        |
| Geometric mean            | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (6): async_tree_none, async_tree_none_tg, async_generators, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                                     | 88.1 ms: 1.03x faster                                                       |
| pidigits       | 251 ms                                                                      | 252 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                                     | 25.3 ms: 1.03x faster                                                       |
| regex_effbot   | 3.50 ms                                                                     | 3.51 ms: 1.00x slower                                                       |
| regex_compile  | 139 ms                                                                      | 140 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 220 us                                                                      | 216 us: 1.02x faster                                                        |
| pickle_pure_python   | 314 us                                                                      | 317 us: 1.01x slower                                                        |
| tomli_loads          | 2.54 sec                                                                    | 2.56 sec: 1.01x slower                                                      |
| xml_etree_iterparse  | 101 ms                                                                      | 102 ms: 1.01x slower                                                        |
| xml_etree_process    | 59.7 ms                                                                     | 60.8 ms: 1.02x slower                                                       |
| xml_etree_generate   | 84.1 ms                                                                     | 87.4 ms: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (3): json_dumps, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 41.3 ms                                                                     | 39.0 ms: 1.06x faster                                                       |
| genshi_xml      | 55.1 ms                                                                     | 54.3 ms: 1.02x faster                                                       |
| mako            | 10.3 ms                                                                     | 10.4 ms: 1.01x slower                                                       |
| genshi_text     | 24.7 ms                                                                     | 24.9 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template           | 41.3 ms                                                                     | 39.0 ms: 1.06x faster                                                       |
| pyflate                   | 498 ms                                                                      | 474 ms: 1.05x faster                                                        |
| raytrace                  | 277 ms                                                                      | 267 ms: 1.04x faster                                                        |
| thrift                    | 878 us                                                                      | 846 us: 1.04x faster                                                        |
| async_tree_memoization_tg | 392 ms                                                                      | 379 ms: 1.03x faster                                                        |
| regex_v8                  | 26.0 ms                                                                     | 25.3 ms: 1.03x faster                                                       |
| nbody                     | 90.7 ms                                                                     | 88.1 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed   | 575 ms                                                                      | 558 ms: 1.03x faster                                                        |
| html5lib                  | 75.1 ms                                                                     | 73.1 ms: 1.03x faster                                                       |
| telco                     | 8.39 ms                                                                     | 8.18 ms: 1.03x faster                                                       |
| fannkuch                  | 361 ms                                                                      | 352 ms: 1.02x faster                                                        |
| nqueens                   | 91.8 ms                                                                     | 90.0 ms: 1.02x faster                                                       |
| unpickle_pure_python      | 220 us                                                                      | 216 us: 1.02x faster                                                        |
| asyncio_tcp               | 372 ms                                                                      | 366 ms: 1.02x faster                                                        |
| deepcopy                  | 290 us                                                                      | 285 us: 1.02x faster                                                        |
| genshi_xml                | 55.1 ms                                                                     | 54.3 ms: 1.02x faster                                                       |
| richards_super            | 56.8 ms                                                                     | 56.0 ms: 1.01x faster                                                       |
| pprint_pformat            | 1.66 sec                                                                    | 1.64 sec: 1.01x faster                                                      |
| coverage                  | 84.2 ms                                                                     | 83.1 ms: 1.01x faster                                                       |
| async_tree_io_tg          | 783 ms                                                                      | 775 ms: 1.01x faster                                                        |
| mdp                       | 2.50 sec                                                                    | 2.48 sec: 1.01x faster                                                      |
| comprehensions            | 17.5 us                                                                     | 17.3 us: 1.01x faster                                                       |
| json                      | 5.44 ms                                                                     | 5.40 ms: 1.01x faster                                                       |
| deepcopy_memo             | 29.2 us                                                                     | 29.0 us: 1.01x faster                                                       |
| richards                  | 50.5 ms                                                                     | 50.3 ms: 1.01x faster                                                       |
| chaos                     | 61.4 ms                                                                     | 61.1 ms: 1.00x faster                                                       |
| sympy_expand              | 501 ms                                                                      | 499 ms: 1.00x faster                                                        |
| hexiom                    | 6.24 ms                                                                     | 6.23 ms: 1.00x faster                                                       |
| 2to3                      | 282 ms                                                                      | 281 ms: 1.00x faster                                                        |
| python_startup            | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| regex_effbot              | 3.50 ms                                                                     | 3.51 ms: 1.00x slower                                                       |
| sympy_integrate           | 22.9 ms                                                                     | 23.0 ms: 1.00x slower                                                       |
| pidigits                  | 251 ms                                                                      | 252 ms: 1.00x slower                                                        |
| regex_compile             | 139 ms                                                                      | 140 ms: 1.00x slower                                                        |
| sqlglot_parse             | 1.42 ms                                                                     | 1.43 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl           | 1.58 sec                                                                    | 1.59 sec: 1.01x slower                                                      |
| coroutines                | 21.2 ms                                                                     | 21.3 ms: 1.01x slower                                                       |
| spectral_norm             | 96.2 ms                                                                     | 96.8 ms: 1.01x slower                                                       |
| bpe_tokeniser             | 4.87 sec                                                                    | 4.91 sec: 1.01x slower                                                      |
| pickle_pure_python        | 314 us                                                                      | 317 us: 1.01x slower                                                        |
| tomli_loads               | 2.54 sec                                                                    | 2.56 sec: 1.01x slower                                                      |
| generators                | 28.6 ms                                                                     | 28.8 ms: 1.01x slower                                                       |
| xml_etree_iterparse       | 101 ms                                                                      | 102 ms: 1.01x slower                                                        |
| mako                      | 10.3 ms                                                                     | 10.4 ms: 1.01x slower                                                       |
| sqlglot_optimize          | 58.4 ms                                                                     | 59.0 ms: 1.01x slower                                                       |
| genshi_text               | 24.7 ms                                                                     | 24.9 ms: 1.01x slower                                                       |
| sqlglot_normalize         | 118 ms                                                                      | 119 ms: 1.01x slower                                                        |
| logging_silent            | 98.0 ns                                                                     | 99.3 ns: 1.01x slower                                                       |
| scimark_sor               | 116 ms                                                                      | 118 ms: 1.02x slower                                                        |
| deltablue                 | 3.38 ms                                                                     | 3.44 ms: 1.02x slower                                                       |
| pathlib                   | 15.6 ms                                                                     | 15.9 ms: 1.02x slower                                                       |
| xml_etree_process         | 59.7 ms                                                                     | 60.8 ms: 1.02x slower                                                       |
| scimark_lu                | 95.0 ms                                                                     | 96.8 ms: 1.02x slower                                                       |
| async_tree_io             | 807 ms                                                                      | 827 ms: 1.03x slower                                                        |
| scimark_sparse_mat_mult   | 4.23 ms                                                                     | 4.34 ms: 1.03x slower                                                       |
| crypto_pyaes              | 72.5 ms                                                                     | 74.6 ms: 1.03x slower                                                       |
| logging_format            | 6.97 us                                                                     | 7.19 us: 1.03x slower                                                       |
| logging_simple            | 6.31 us                                                                     | 6.52 us: 1.03x slower                                                       |
| pycparser                 | 1.23 sec                                                                    | 1.27 sec: 1.03x slower                                                      |
| xml_etree_generate        | 84.1 ms                                                                     | 87.4 ms: 1.04x slower                                                       |
| Geometric mean            | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (29): async_tree_none, async_tree_none_tg, async_generators, json_dumps, scimark_monte_carlo, gc_traversal, xml_etree_parse, deepcopy_reduce, pprint_safe_repr, asyncio_websockets, sqlglot_transpile, scimark_fft, sympy_str, python_startup_no_site, pylint, async_tree_cpu_io_mixed_tg, float, meteor_contest, regex_dna, docutils, sympy_sum, json_loads, go, typing_runtime_protocols, async_tree_memoization, tornado_http, bench_thread_pool, create_gc_cycles, bench_mp_pool

# HPT report

- Reliability score: 55.22% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x