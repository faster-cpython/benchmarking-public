# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.025x slower
- HPT reliability: 99.14%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 318 ms: 1.11x slower                                                            |
| docutils       | 2.87 sec                                                     | 3.21 sec: 1.12x slower                                                          |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 379 ms: 1.42x faster                                                            |
| async_tree_none_tg         | 431 ms                                                       | 326 ms: 1.32x faster                                                            |
| async_tree_none            | 452 ms                                                       | 345 ms: 1.31x faster                                                            |
| async_tree_memoization     | 544 ms                                                       | 416 ms: 1.31x faster                                                            |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 568 ms: 1.23x faster                                                            |
| async_tree_io              | 1.04 sec                                                     | 855 ms: 1.22x faster                                                            |
| async_tree_io_tg           | 1.05 sec                                                     | 869 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 582 ms: 1.20x faster                                                            |
| Geometric mean             | (ref)                                                        | 1.27x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.05x faster                                                            |
| nbody          | 88.0 ms                                                      | 86.1 ms: 1.02x faster                                                           |
| float          | 76.6 ms                                                      | 78.6 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                            |
| regex_effbot   | 3.57 ms                                                      | 3.66 ms: 1.02x slower                                                           |
| regex_dna      | 239 ms                                                       | 256 ms: 1.07x slower                                                            |
| regex_v8       | 23.6 ms                                                      | 26.1 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 81.9 ms: 1.05x faster                                                           |
| xml_etree_iterparse  | 103 ms                                                       | 100.0 ms: 1.03x faster                                                          |
| tomli_loads          | 2.16 sec                                                     | 2.18 sec: 1.01x slower                                                          |
| json_loads           | 24.4 us                                                      | 24.7 us: 1.01x slower                                                           |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.01x slower                                                            |
| xml_etree_process    | 58.4 ms                                                      | 61.0 ms: 1.04x slower                                                           |
| unpickle_pure_python | 210 us                                                       | 227 us: 1.08x slower                                                            |
| pickle_pure_python   | 318 us                                                       | 349 us: 1.10x slower                                                            |
| json_dumps           | 10.2 ms                                                      | 11.3 ms: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                           |
| python_startup         | 11.6 ms                                                      | 14.9 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 42.2 ms: 1.11x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 379 ms: 1.42x faster                                                            |
| async_tree_none_tg         | 431 ms                                                       | 326 ms: 1.32x faster                                                            |
| async_tree_none            | 452 ms                                                       | 345 ms: 1.31x faster                                                            |
| async_tree_memoization     | 544 ms                                                       | 416 ms: 1.31x faster                                                            |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 568 ms: 1.23x faster                                                            |
| async_tree_io              | 1.04 sec                                                     | 855 ms: 1.22x faster                                                            |
| deepcopy_memo              | 36.8 us                                                      | 30.3 us: 1.22x faster                                                           |
| async_tree_io_tg           | 1.05 sec                                                     | 869 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 582 ms: 1.20x faster                                                            |
| pathlib                    | 18.9 ms                                                      | 16.1 ms: 1.17x faster                                                           |
| deepcopy                   | 368 us                                                       | 317 us: 1.16x faster                                                            |
| comprehensions             | 21.9 us                                                      | 19.9 us: 1.10x faster                                                           |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.08x faster                                                           |
| crypto_pyaes               | 80.3 ms                                                      | 75.1 ms: 1.07x faster                                                           |
| deepcopy_reduce            | 3.37 us                                                      | 3.17 us: 1.06x faster                                                           |
| pidigits                   | 265 ms                                                       | 251 ms: 1.05x faster                                                            |
| xml_etree_generate         | 86.1 ms                                                      | 81.9 ms: 1.05x faster                                                           |
| dulwich_log                | 65.4 ms                                                      | 62.8 ms: 1.04x faster                                                           |
| xml_etree_iterparse        | 103 ms                                                       | 100.0 ms: 1.03x faster                                                          |
| async_generators           | 390 ms                                                       | 380 ms: 1.03x faster                                                            |
| logging_format             | 7.48 us                                                      | 7.30 us: 1.02x faster                                                           |
| nbody                      | 88.0 ms                                                      | 86.1 ms: 1.02x faster                                                           |
| asyncio_websockets         | 387 ms                                                       | 381 ms: 1.02x faster                                                            |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.5 ms: 1.01x faster                                                           |
| logging_simple             | 6.71 us                                                      | 6.63 us: 1.01x faster                                                           |
| scimark_fft                | 301 ms                                                       | 299 ms: 1.01x faster                                                            |
| tomli_loads                | 2.16 sec                                                     | 2.18 sec: 1.01x slower                                                          |
| json                       | 5.12 ms                                                      | 5.17 ms: 1.01x slower                                                           |
| json_loads                 | 24.4 us                                                      | 24.7 us: 1.01x slower                                                           |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.01x slower                                                            |
| richards_super             | 51.3 ms                                                      | 52.1 ms: 1.01x slower                                                           |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                          |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                            |
| mdp                        | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                          |
| regex_effbot               | 3.57 ms                                                      | 3.66 ms: 1.02x slower                                                           |
| float                      | 76.6 ms                                                      | 78.6 ms: 1.03x slower                                                           |
| xml_etree_process          | 58.4 ms                                                      | 61.0 ms: 1.04x slower                                                           |
| go                         | 150 ms                                                       | 157 ms: 1.05x slower                                                            |
| raytrace                   | 298 ms                                                       | 312 ms: 1.05x slower                                                            |
| python_startup_no_site     | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                           |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.41 ms: 1.05x slower                                                           |
| spectral_norm              | 91.6 ms                                                      | 96.2 ms: 1.05x slower                                                           |
| sqlalchemy_declarative     | 159 ms                                                       | 168 ms: 1.05x slower                                                            |
| deltablue                  | 3.24 ms                                                      | 3.41 ms: 1.05x slower                                                           |
| meteor_contest             | 128 ms                                                       | 135 ms: 1.05x slower                                                            |
| logging_silent             | 94.4 ns                                                      | 100 ns: 1.06x slower                                                            |
| sympy_str                  | 302 ms                                                       | 322 ms: 1.07x slower                                                            |
| scimark_monte_carlo        | 69.0 ms                                                      | 73.6 ms: 1.07x slower                                                           |
| sqlglot_parse              | 1.38 ms                                                      | 1.47 ms: 1.07x slower                                                           |
| chaos                      | 64.0 ms                                                      | 68.6 ms: 1.07x slower                                                           |
| regex_dna                  | 239 ms                                                       | 256 ms: 1.07x slower                                                            |
| richards                   | 45.7 ms                                                      | 49.2 ms: 1.08x slower                                                           |
| generators                 | 37.4 ms                                                      | 40.6 ms: 1.08x slower                                                           |
| unpickle_pure_python       | 210 us                                                       | 227 us: 1.08x slower                                                            |
| sympy_sum                  | 162 ms                                                       | 176 ms: 1.09x slower                                                            |
| fannkuch                   | 350 ms                                                       | 381 ms: 1.09x slower                                                            |
| pickle_pure_python         | 318 us                                                       | 349 us: 1.10x slower                                                            |
| sqlglot_transpile          | 1.78 ms                                                      | 1.95 ms: 1.10x slower                                                           |
| scimark_sor                | 109 ms                                                       | 120 ms: 1.10x slower                                                            |
| sympy_expand               | 484 ms                                                       | 535 ms: 1.11x slower                                                            |
| django_template            | 38.2 ms                                                      | 42.2 ms: 1.11x slower                                                           |
| json_dumps                 | 10.2 ms                                                      | 11.3 ms: 1.11x slower                                                           |
| regex_v8                   | 23.6 ms                                                      | 26.1 ms: 1.11x slower                                                           |
| 2to3                       | 285 ms                                                       | 318 ms: 1.11x slower                                                            |
| docutils                   | 2.87 sec                                                     | 3.21 sec: 1.12x slower                                                          |
| pyflate                    | 439 ms                                                       | 494 ms: 1.13x slower                                                            |
| telco                      | 6.96 ms                                                      | 7.99 ms: 1.15x slower                                                           |
| sympy_integrate            | 23.9 ms                                                      | 27.6 ms: 1.15x slower                                                           |
| sqlglot_normalize          | 116 ms                                                       | 136 ms: 1.17x slower                                                            |
| nqueens                    | 89.9 ms                                                      | 106 ms: 1.18x slower                                                            |
| sqlglot_optimize           | 57.5 ms                                                      | 69.9 ms: 1.22x slower                                                           |
| typing_runtime_protocols   | 152 us                                                       | 186 us: 1.23x slower                                                            |
| coverage                   | 66.7 ms                                                      | 83.5 ms: 1.25x slower                                                           |
| hexiom                     | 5.96 ms                                                      | 7.51 ms: 1.26x slower                                                           |
| python_startup             | 11.6 ms                                                      | 14.9 ms: 1.28x slower                                                           |
| gc_traversal               | 3.48 ms                                                      | 5.51 ms: 1.58x slower                                                           |
| create_gc_cycles           | 1.59 ms                                                      | 2.88 ms: 1.81x slower                                                           |
| bench_mp_pool              | 4.76 ms                                                      | 1.70 sec: 356.21x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.10x slower                                                                    |

Benchmark hidden because not significant (6): mako, scimark_lu, tornado_http, pprint_pformat, pprint_safe_repr, bench_thread_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241025-3.14.0a1+-64b198a-JIT/bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.025x slower
# HPT report

- Reliability score: 99.14% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x